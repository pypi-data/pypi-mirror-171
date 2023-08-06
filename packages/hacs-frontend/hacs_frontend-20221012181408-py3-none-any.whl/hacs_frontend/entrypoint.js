
try {
  new Function("import('/hacsfiles/frontend/main-0de26b5f.js')")();
} catch (err) {
  var el = document.createElement('script');
  el.src = '/hacsfiles/frontend/main-0de26b5f.js';
  el.type = 'module';
  document.body.appendChild(el);
}
  