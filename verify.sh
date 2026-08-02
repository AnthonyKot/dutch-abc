#!/usr/bin/env bash
# DutchABC — standing verification. Run from anywhere: ./verify.sh
#
# Ports the checks from The Bridge and No Such Form (count sync, link resolution,
# prev/next contiguity, quotation scan, self-assessment scan, no tracked PDFs)
# and adds the three this book needs:
#
#   * every piece of Dutch is marked up, so the corpus is extractable
#   * checks/forms.py validates the Dutch we assert   (HARD FAIL)
#   * checks/redaction.py catches personal data in real documents (HARD FAIL)
#   * checks/template.py asserts every chapter carries the teaching apparatus —
#     retrieval prompt, hidden worked answer, self-check, undecidable case (HARD FAIL)
#   * checks/lexicon.py reports vocabulary growth      (ADVISORY, by decision)
#
# Counts are COMPUTED, never typed. Exits non-zero on any hard failure.
set -u
cd "$(dirname "$0")"
fail=0

echo "== count sync (computed, not typed) =="
files=$(ls docs/chapters/*.html 2>/dev/null | wc -l | tr -d ' ')
links=$(grep -oE 'href="chapters/[0-9][^"]*\.html"' docs/index.html 2>/dev/null | sort -u | wc -l | tr -d ' ')
echo "  $files chapter files on disk; $links distinct chapter links on the contents page"
if [ "$files" != "$links" ]; then
  echo "  FAIL: contents page ($links) != chapter files ($files)"; fail=1
fi

echo "== HTML well-formed =="
python3 - <<'PY' || fail=1
import glob, sys
from html.parser import HTMLParser
KNOWN = {"meta","title","link","script","header","div","a","nav","button","main","p","h1","h2","h3",
         "span","section","ul","ol","li","em","strong","table","thead","tbody","tr","th","td","br",
         "footer","code","hr","sup","sub","abbr","figure","figcaption","blockquote","b","i",
         "details","summary","mark","dl","dt","dd"}
bad = 0
class P(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag not in KNOWN:
            print(f"  UNKNOWN TAG <{tag}> in {self.fn} line {self.getpos()[0]}")
            globals().__setitem__("bad", globals()["bad"] + 1)
for fn in sorted(glob.glob("docs/*.html") + glob.glob("docs/chapters/*.html")):
    t = open(fn, encoding="utf-8").read()
    if not t.lstrip().lower().startswith("<!doctype html>"):
        print(f"  MISSING DOCTYPE in {fn}"); bad += 1
    p = P(); p.fn = fn; p.feed(t)
sys.exit(1 if bad else 0)
PY

echo "== internal links resolve =="
python3 - <<'PY' || fail=1
import glob, os, re, sys
bad = 0
for fn in sorted(glob.glob("docs/*.html") + glob.glob("docs/chapters/*.html")):
    base = os.path.dirname(fn)
    for href in re.findall(r'href="([^"#?][^"]*)"', open(fn, encoding="utf-8").read()):
        if href.startswith(("http://", "https://", "mailto:")):
            continue
        target = os.path.normpath(os.path.join(base, href.split("#")[0]))
        if not os.path.exists(target):
            print(f"  BROKEN LINK in {fn}: {href}"); bad += 1
sys.exit(1 if bad else 0)
PY

echo "== every piece of Dutch is marked up (heuristic) =="
# The whole verification story depends on the corpus being extractable: a chapter
# that writes Dutch as bare prose silently opts out of checks/forms.py.
#
# The first version of this check used a regex with a backreference </\1?> that
# can never match a closing tag, so correctly marked <p class="nl"> blocks were
# reported as unmarked. It is now a real parser, shared with checks/. It remains a
# HEURISTIC: it can only spot Dutch it recognises from a function-word list, so it
# catches carelessness, not everything.
python3 checks/markup.py || fail=1

echo "== quotation scan (no reproduced source prose) =="
# Standing step. The sources are pedagogical texts full of exactly the sentences
# we would be tempted to lift, and real letters are quotable and must not be quoted.
# Multibyte trap from book 2: never trust one regex on curly quotes. Read the hits.
hits=$(grep -nE '"|“|”|<blockquote' docs/chapters/*.html 2>/dev/null | grep -vE '="|="[^"]*"' | wc -l | tr -d ' ')
echo "  $hits quotation-shaped lines to read by eye (not an automatic failure)"
grep -nE '<blockquote' docs/chapters/*.html 2>/dev/null | sed 's/^/  /'

echo "== self-assessment scan (the recurring tic) =="
# Caught in all three previous books. A verdict about the chapter or the book is
# the tic; an ordinary descriptive superlative about Dutch is fine.
tic=$(grep -rniE "cleanest|clearest|sharpest|the best|most (elegant|interesting|important)|in the whole book|worth saying|the heart of this book" docs/chapters/*.html 2>/dev/null | wc -l | tr -d ' ')
if [ "$tic" != "0" ]; then
  echo "  $tic possible self-assessments — replace the verdict with what earns it:"
  grep -rniE "cleanest|clearest|sharpest|the best|most (elegant|interesting|important)|in the whole book|worth saying|the heart of this book" docs/chapters/*.html 2>/dev/null | sed 's/^/    /'
else
  echo "  none"
fi

echo "== no source page numbers for books not in sources/ =="
# Tier C discipline: cite by topic only unless a copy is here.
if grep -rnE "(Contact!|Nederlands in gang|Delftse|Comprehensive Grammar)[^<]{0,40}(p\.|pp\.|page) ?[0-9]" \
     docs/chapters/*.html docs/about.html 2>/dev/null; then
  echo "  FAIL: page number cited for a book not in sources/"; fail=1
else
  echo "  none"
fi

echo "== no tracked source PDFs =="
if ls sources/*.pdf >/dev/null 2>&1 && git -C . ls-files --error-unmatch sources/*.pdf >/dev/null 2>&1; then
  echo "  FAIL: a source PDF is tracked by git"; fail=1
else
  echo "  none tracked"
fi

echo "== published surface is exactly docs/ =="
# Pages serves ONLY docs/. Anything the site needs must live there; anything that
# must not be public must not. Previously Pages published the repository root and
# served CONTEXT.md, the checks and the source register alongside the book.
python3 - <<'PY' || fail=1
import pathlib, subprocess, sys
tracked = subprocess.run(["git", "ls-files"], capture_output=True, text=True).stdout.split()
pub = sorted(f for f in tracked if f.startswith("docs/"))
allowed = {".html", ".css", ".js", ""}
bad = [f for f in pub if pathlib.Path(f).suffix not in allowed]
if bad:
    print("  FAIL unexpected file type published under docs/: " + ", ".join(bad)); sys.exit(1)
print(f"  {len(pub)} files published; nothing outside docs/ is served")
for f in sorted(set(tracked) - set(pub)):
    if f.endswith((".html", ".css")) :
        print(f"  WARNING web asset outside docs/, will NOT be served: {f}")
PY

echo "== checks/ =="
for f in checks/*.py; do
  [ -e "$f" ] || continue
  case "$f" in
    # Advisory means "raises no findings", NOT "cannot fail". It returns 0 by design,
    # so a non-zero exit is the script itself breaking — which is a real problem and
    # must not pass. Caught for real: a bad regex unpack crashed this check and the
    # suite still printed PASS.
    */lexicon.py) echo "  -- $f (advisory)"
                  if ! python3 "$f"; then echo "  FAIL: advisory check crashed"; fail=1; fi ;;
    *)            echo "  -- $f"; python3 "$f" || fail=1 ;;
  esac
done

echo
if [ "$fail" = "0" ]; then echo "PASS"; else echo "FAIL"; fi
exit "$fail"
