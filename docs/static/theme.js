/* DutchABC — theme toggle.
   Vanilla JS, no dependencies. Unlike its three predecessors this book has
   no mathematics, so there is no KaTeX bootstrap here. */

(function () {
  var KEY = "dutchabc-theme";
  var root = document.documentElement;

  // Apply saved preference as early as possible.
  try {
    var saved = localStorage.getItem(KEY);
    if (saved === "light" || saved === "dark") {
      root.setAttribute("data-theme", saved);
    }
  } catch (e) { /* localStorage may be unavailable */ }

  function currentTheme() {
    var attr = root.getAttribute("data-theme");
    if (attr) return attr;
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function setTheme(t) {
    root.setAttribute("data-theme", t);
    try { localStorage.setItem(KEY, t); } catch (e) {}
    updateLabel(t);
  }

  function updateLabel(t) {
    var btn = document.querySelector(".theme-toggle");
    if (!btn) return;
    var dark = t === "dark";
    btn.textContent = dark ? "☀ Light" : "☾ Dark";
    btn.setAttribute("aria-label", dark ? "Switch to light theme" : "Switch to dark theme");
  }

  document.addEventListener("DOMContentLoaded", function () {
    var btn = document.querySelector(".theme-toggle");
    if (btn) {
      updateLabel(currentTheme());
      btn.addEventListener("click", function () {
        setTheme(currentTheme() === "dark" ? "light" : "dark");
      });
    }
  });

  // Print: reveal every retrieval answer, then put them back.
  //
  // The kaart's terug column hides its answers behind <details> so the reader has
  // to attempt recall before seeing them. On paper there is nothing to click, so a
  // printed chapter would carry questions whose answers appear nowhere in the book.
  // The print stylesheet tries this too, but CSS cannot reliably reveal details
  // content in browsers that hide it with content-visibility rather than display,
  // so this is the mechanism and the CSS is the fallback.
  //
  // Only elements this opened are closed again, so a reader who had opened one by
  // hand still finds it open after printing.
  var opened = [];
  function expand() {
    opened = [];
    var all = document.querySelectorAll("details:not([open])");
    for (var i = 0; i < all.length; i++) { all[i].open = true; opened.push(all[i]); }
  }
  function restore() {
    for (var i = 0; i < opened.length; i++) { opened[i].open = false; }
    opened = [];
  }
  window.addEventListener("beforeprint", expand);
  window.addEventListener("afterprint", restore);
  // Safari fires no print events; it does change this media query.
  if (window.matchMedia) {
    var mq = window.matchMedia("print");
    var onChange = function (e) { (e.matches ? expand : restore)(); };
    if (mq.addEventListener) mq.addEventListener("change", onChange);
    else if (mq.addListener) mq.addListener(onChange);
  }
})();
