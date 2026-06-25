function updateProgressAll(prefix) {
  let count = 0;
  const total = tasksData.length;
  tasksData.forEach((_, idx) => {
    if (prefix) {
      const el = document.getElementById(prefix + idx);
      if (el && el.className === 'correct') count++;
    } else {
      const el = document.getElementById('ans-' + idx) || document.getElementById('sel-' + idx);
      if (el && el.className === 'correct') count++;
    }
  });
  const scoreEl = document.getElementById('score');
  if (scoreEl) scoreEl.textContent = count;
  const totalEl = document.getElementById('total');
  if (totalEl) totalEl.textContent = total;
}

function resetAllBase(prefix) {
  tasksData.forEach((_, idx) => {
    const ans = document.getElementById('ans-' + idx);
    const sel = document.getElementById('sel-' + idx);
    const xInp = document.getElementById('x-' + idx);
    const yInp = document.getElementById('y-' + idx);
    const uInp = document.getElementById('u-' + idx);
    const vInp = document.getElementById('v-' + idx);
    const res = document.getElementById('result-' + idx);
    if (ans) { ans.value = ''; ans.className = ''; }
    if (sel) { sel.value = ''; sel.className = ''; }
    if (xInp) { xInp.value = ''; xInp.className = ''; }
    if (yInp) { yInp.value = ''; yInp.className = ''; }
    if (uInp) { uInp.value = ''; uInp.className = ''; }
    if (vInp) { vInp.value = ''; vInp.className = ''; }
    if (res) res.innerHTML = '';
  });
  updateProgressAll(prefix);
}
