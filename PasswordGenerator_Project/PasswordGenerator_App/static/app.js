function copyPassword() {
  const el = document.getElementById('generated');
  if (!el) return;
  const text = el.innerText;
  navigator.clipboard.writeText(text).then(() => {
    alert('Password copied to clipboard');
  }).catch(() => {
    alert('Copy failed — select and Ctrl+C');
  });
}
