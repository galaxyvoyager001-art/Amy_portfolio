/* Research & Entrepreneurship pages. Runs after work.js (cursor, menu, curtain, leave transitions). */
(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const accent = getComputedStyle(document.body).getPropertyValue('--a').trim() || '#FF5A1F';
  const ink = getComputedStyle(document.body).getPropertyValue('--rf').trim() || '#111';
  const inView = (el, cb) => ScrollTrigger.create({ trigger: el, start: 'top bottom', end: 'bottom top', onToggle: s => cb(s.isActive) });

  /* hero: the question rises word by word */
  const q = document.querySelector('.r-q');
  if (q) {
    q.innerHTML = q.textContent.split(' ').map(w => `<span class="w">${w}</span>`).join(' ');
    gsap.from('.r-q .w', { yPercent: 60, opacity: 0, stagger: 0.04, duration: 1, delay: 0.5, ease: 'expo.out' });
    gsap.from('.r-name, .r-kick, .r-meta > div', { y: 24, opacity: 0, stagger: 0.05, duration: 0.9, delay: 0.4, ease: 'power3.out' });
    gsap.from('.r-heroimg', { y: 60, opacity: 0, scale: 0.95, duration: 1.3, delay: 0.6, ease: 'expo.out' });
  }

  /* sticky index follows the four sections */
  const links = [...document.querySelectorAll('.r-toc a')];
  document.querySelectorAll('.r-sec').forEach((s, i) => ScrollTrigger.create({ trigger: s, start: 'top 55%', end: 'bottom 55%',
    onToggle: st => { if (st.isActive) links.forEach((l, j) => l.classList.toggle('on', j === i)); } }));
  gsap.utils.toArray('.r-sh').forEach(h => gsap.from(h.children, { y: 40, opacity: 0, stagger: 0.08, duration: 1, ease: 'expo.out', scrollTrigger: { trigger: h, start: 'top 88%' } }));
  gsap.utils.toArray('.r-body > *').forEach(el => gsap.from(el, { y: 40, opacity: 0, duration: 1, ease: 'power3.out', scrollTrigger: { trigger: el, start: 'top 92%' } }));

  /* ---------- coupled pendulums (linear nearest-neighbour model) ---------- */
  document.querySelectorAll('[data-lab="pendulums"]').forEach(box => {
    const cv = box.querySelector('canvas'), ctx = cv.getContext('2d'), N = 5, w0 = 4, damp = 0.015;
    const slider = box.querySelector('input'), bars = box.querySelector('.pend-e');
    bars.innerHTML = '<i></i>'.repeat(N);
    const bi = [...bars.children];
    let th = Array(N).fill(0), om = Array(N).fill(0), run = false, first = true, W, H, dpr;
    const size = () => { dpr = devicePixelRatio || 1; W = cv.clientWidth; H = cv.clientHeight; cv.width = W * dpr; cv.height = H * dpr; };
    size(); addEventListener('resize', size);
    const kick = i => { om[i] += 1.4; };
    const xs = i => W * (0.14 + 0.72 * i / (N - 1));
    box.querySelector('[data-kick]').addEventListener('click', () => kick(0));
    cv.addEventListener('pointerdown', e => {
      const r = cv.getBoundingClientRect(), x = e.clientX - r.left;
      let best = 0; for (let i = 1; i < N; i++) if (Math.abs(xs(i) - x) < Math.abs(xs(best) - x)) best = i;
      kick(best);
    });
    const step = dt => {
      const k = +slider.value * 0.8, a = th.map((t, i) => -w0 * w0 * t + (i > 0 ? k * (th[i - 1] - t) : 0) + (i < N - 1 ? k * (th[i + 1] - t) : 0) - damp * om[i]);
      for (let i = 0; i < N; i++) { om[i] += a[i] * dt; th[i] += om[i] * dt; }
    };
    const draw = () => {
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0); ctx.clearRect(0, 0, W, H);
      const top = 26, L = H - 90;
      ctx.strokeStyle = ink; ctx.lineWidth = 3; ctx.beginPath(); ctx.moveTo(W * 0.06, top); ctx.lineTo(W * 0.94, top); ctx.stroke();
      const tips = th.map((t, i) => [xs(i) + L * Math.sin(t), top + L * Math.cos(t)]);
      ctx.setLineDash([4, 6]); ctx.lineWidth = 1; ctx.globalAlpha = 0.35; ctx.beginPath();
      tips.forEach(([x, y], i) => i ? ctx.lineTo(x, y) : ctx.moveTo(x, y)); ctx.stroke(); ctx.setLineDash([]); ctx.globalAlpha = 1;
      tips.forEach(([x, y], i) => {
        ctx.lineWidth = 2; ctx.strokeStyle = ink; ctx.beginPath(); ctx.moveTo(xs(i), top); ctx.lineTo(x, y); ctx.stroke();
        ctx.fillStyle = accent; ctx.beginPath(); ctx.arc(x, y, 15, 0, Math.PI * 2); ctx.fill();
        ctx.fillStyle = '#fff'; ctx.font = '11px monospace'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle'; ctx.fillText(i + 1, x, y);
      });
      const E = th.map((t, i) => 0.5 * om[i] * om[i] + 0.5 * w0 * w0 * t * t), m = 0.98; /* energy of one kick */
      bi.forEach((b, i) => b.style.height = Math.max(2, Math.min(46, E[i] / m * 46)) + 'px');
    };
    inView(box, a => { run = a; if (a && first) { first = false; kick(0); } });
    gsap.ticker.add((t, dt) => { if (!run) return; const h = Math.min(dt, 50) / 1000 / 8; for (let s = 0; s < 8; s++) step(h); draw(); });
    draw();
  });

  /* ---------- before / after slider ---------- */
  document.querySelectorAll('[data-lab="compare"]').forEach(c => {
    let down = false;
    const set = x => { const r = c.getBoundingClientRect(); c.style.setProperty('--p', Math.min(100, Math.max(0, (x - r.left) / r.width * 100)) + '%'); };
    c.addEventListener('pointerdown', e => { down = true; set(e.clientX); });
    addEventListener('pointerup', () => down = false);
    c.addEventListener('pointermove', e => { if (down || e.pointerType === 'mouse') set(e.clientX); });
    c.addEventListener('pointerleave', () => { if (!down) gsap.to(c, { '--p': '50%', duration: 0.8, ease: 'power3.out' }); });
  });

  /* ---------- Malus's law ---------- */
  document.querySelectorAll('[data-lab="malus"]').forEach(box => {
    const svg = box.querySelector('svg'), inp = box.querySelector('input'), out = box.querySelector('output');
    const gx = a => 250 + a / 180 * 360, gy = v => 250 - v * 200;
    let path = ''; for (let a = 0; a <= 180; a += 2) path += (a ? 'L' : 'M') + gx(a).toFixed(1) + ',' + gy(Math.cos(a * Math.PI / 180) ** 2).toFixed(1);
    svg.innerHTML = `
      <g stroke="currentColor" fill="none" stroke-width="1.5" opacity=".9">
        <circle cx="70" cy="95" r="52"/><line x1="70" y1="43" x2="70" y2="147" stroke-width="3"/>
        <circle cx="70" cy="225" r="52"/><line class="an" x1="70" y1="173" x2="70" y2="277" stroke="${accent}" stroke-width="3"/>
      </g>
      <text x="140" y="99" font-size="12" fill="currentColor" font-family="monospace">polariser</text>
      <text x="140" y="229" font-size="12" fill="${accent}" font-family="monospace">analyser</text>
      <g stroke="currentColor" stroke-width="1" opacity=".5"><line x1="250" y1="250" x2="615" y2="250"/><line x1="250" y1="40" x2="250" y2="250"/></g>
      <text x="250" y="270" font-size="11" fill="currentColor" font-family="monospace">0°</text><text x="420" y="270" font-size="11" fill="currentColor" font-family="monospace">90°</text><text x="590" y="270" font-size="11" fill="currentColor" font-family="monospace">180°</text>
      <text x="216" y="54" font-size="11" fill="currentColor" font-family="monospace">I/I₀</text>
      <path d="${path}" fill="none" stroke="currentColor" stroke-width="2"/>
      <line class="cur" y1="40" y2="250" stroke="${accent}" stroke-dasharray="4 5"/>
      <circle class="dot" r="7" fill="${accent}"/>
      <circle cx="${gx(45)}" cy="${gy(0.502)}" r="6" fill="none" stroke="currentColor" stroke-width="2"/>
      <text x="${gx(45) + 12}" y="${gy(0.502) - 10}" font-size="11" fill="currentColor" font-family="monospace">my data: 0.502</text>
      <text class="val" x="620" y="30" text-anchor="end" font-size="22" fill="${accent}" font-family="monospace"></text>`;
    const an = svg.querySelector('.an'), cur = svg.querySelector('.cur'), dot = svg.querySelector('.dot'), val = svg.querySelector('.val');
    const set = () => {
      const a = +inp.value, v = Math.cos(a * Math.PI / 180) ** 2;
      out.textContent = a + '°'; an.setAttribute('transform', `rotate(${a} 70 225)`);
      cur.setAttribute('x1', gx(a)); cur.setAttribute('x2', gx(a)); dot.setAttribute('cx', gx(a)); dot.setAttribute('cy', gy(v));
      val.textContent = 'I/I₀ = ' + v.toFixed(3);
    };
    inp.addEventListener('input', set); set();
  });

  /* ---------- which sound matters ---------- */
  document.querySelectorAll('[data-lab="scenes"]').forEach(box => {
    const bs = [...box.querySelectorAll('button')], sets = [...box.querySelectorAll('.sc-set')];
    let user = false, k = 0, timer;
    const show = i => { k = i; bs.forEach((b, j) => b.classList.toggle('on', j === i)); sets.forEach((s, j) => s.classList.toggle('on', j === i)); };
    bs.forEach((b, i) => b.addEventListener('click', () => { user = true; clearInterval(timer); show(i); }));
    inView(box, a => { clearInterval(timer); if (a && !user) timer = setInterval(() => show((k + 1) % bs.length), 2600); });
  });

  /* ---------- Curawave: a row of units passes the patient along ---------- */
  document.querySelectorAll('[data-lab="wave"]').forEach(box => {
    const us = [...box.querySelectorAll('.wv-u i')], pt = box.querySelector('.wv-p');
    let run = false, t = 0;
    inView(box, a => run = a);
    gsap.ticker.add((_, dt) => {
      if (!run || reduce) return;
      t += dt / 1000;
      const cyc = (t % 7) / 7, x = cyc * 0.66;
      us.forEach((u, i) => {
        const on = Math.sin(t * 5 + (i % 2) * Math.PI) > 0 ? 1 : 0;
        u.style.transform = `rotate(${on ? 12 : 0}deg) scaleY(${on ? 1.12 : 1})`; u.style.opacity = on ? 1 : 0.65;
      });
      pt.style.left = (x * 100) + '%'; pt.style.transform = `translateY(${Math.sin(t * 10) * 3}px)`;
    });
  });

  /* ---------- drag-to-scroll paper cards ---------- */
  document.querySelectorAll('[data-lab="drag"]').forEach(el => {
    let x0 = 0, s0 = 0, down = false;
    el.addEventListener('pointerdown', e => { if (e.pointerType !== 'mouse') return; down = true; x0 = e.clientX; s0 = el.scrollLeft; el.classList.add('drag'); });
    addEventListener('pointerup', () => { down = false; el.classList.remove('drag'); });
    el.addEventListener('pointermove', e => { if (down) el.scrollLeft = s0 - (e.clientX - x0); });
  });

  /* ---------- timeline fills in ---------- */
  document.querySelectorAll('[data-lab="timeline"] li').forEach((li, i) =>
    gsap.from(li, { opacity: 0.15, y: 20, duration: 0.8, delay: i * 0.15, ease: 'power3.out', scrollTrigger: { trigger: li.parentElement, start: 'top 80%' } }));
})();
