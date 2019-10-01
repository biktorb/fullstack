var dialog = document.querySelector('dialog');

document.querySelector('#btn_js').onclick = function() {
  dialog.show();
};

document.querySelector('#close').onclick = function() {
  dialog.close();
};
