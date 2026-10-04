/* Essay pages for the two handmade books. Runs after work.js (cursor, menu, curtain, word light-up). */
(() => {
  const touch = matchMedia('(hover: none)').matches;
  const mouse = { x: innerWidth / 2, y: innerHeight / 2, moved: false };
  addEventListener('pointermove', e => { mouse.x = e.clientX; mouse.y = e.clientY; mouse.moved = true; });
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));

  /* braille: dot numbers per letter (grade 1). Cell order in a 2x3 grid, row by row: 1,4,2,5,3,6 */
  const BR = { a:'1',b:'12',c:'14',d:'145',e:'15',f:'124',g:'1245',h:'125',i:'24',j:'245',k:'13',l:'123',m:'134',n:'1345',o:'135',p:'1234',q:'12345',r:'1235',s:'234',t:'2345',u:'136',v:'1236',w:'2456',x:'1346',y:'13456',z:'1356' };
  const ORDER = [1, 4, 2, 5, 3, 6];
  const dots = ch => ORDER.map(n => `<i${(BR[ch] || '').includes(n) ? ' class="on"' : ''}></i>`).join('');

  /* ---------------- TOUCH ---------------- */
  const hero = document.querySelector('.t-hero');
  if (hero) {
    const h1 = hero.querySelector('.brl');
    h1.innerHTML = h1.dataset.text.split(' ').map(w => `<span class="wd">${[...w].map(c =>
      `<span class="c"><span class="b">${dots(c)}</span><span class="l">${c}</span></span>`).join('')}</span>`).join(' ');
    const cells = [...h1.querySelectorAll('.c')];
    const spot = { x: innerWidth * .5, y: innerHeight * .5 };
    let scrollP = 0, t0 = performance.now();
    ScrollTrigger.create({ trigger: hero, start: 'top top', end: 'bottom 40%', scrub: true, onUpdate: s => scrollP = s.progress });
    gsap.ticker.add(() => {
      const r = hero.getBoundingClientRect();
      if (r.bottom < 0) return;
      let tx = mouse.x, ty = mouse.y - r.top;
      if (touch || !mouse.moved) { /* wander when nobody is touching */
        const t = (performance.now() - t0) / 1000;
        tx = r.width * (.5 + .34 * Math.sin(t * .45)); ty = r.height * (.5 + .22 * Math.sin(t * .7 + 1));
      }
      spot.x += (tx - spot.x) * .09; spot.y += (ty - spot.y) * .09;
      hero.style.setProperty('--x', spot.x + 'px'); hero.style.setProperty('--y', spot.y + 'px');
      const R = Math.max(160, r.width * .16);
      cells.forEach(c => {
        const b = c.getBoundingClientRect(), d = Math.hypot(b.left + b.width / 2 - spot.x, b.top - r.top + b.height / 2 - spot.y);
        const p = Math.max(clamp(1 - d / R, 0, 1) * 1.4, scrollP * 1.6 - (c.dataset.i || 0) * .02);
        const v = clamp(p, 0, 1);
        c.firstChild.style.opacity = 1 - v; c.lastChild.style.opacity = v;
      });
    });
    cells.forEach((c, i) => c.dataset.i = i);
    gsap.from('.t-kick, .t-hint, .t-foot', { opacity: 0, y: 20, stagger: .1, duration: 1, delay: .6, ease: 'power3.out' });
  }

  document.querySelectorAll('[data-hands]').forEach(hands => {
    const track = hands.querySelector('.hands-track');
    gsap.to(track, { x: () => -(track.scrollWidth - innerWidth + innerWidth * .1), ease: 'none',
      scrollTrigger: { trigger: hands, start: 'top top', end: 'bottom bottom', scrub: true, invalidateOnRefresh: true } });
    track.querySelectorAll('figure').forEach((f, i) => gsap.from(f.querySelector('img'), { rotate: i % 2 ? 6 : -6, scale: .9, ease: 'none',
      scrollTrigger: { trigger: hands, start: 'top top', end: 'bottom bottom', scrub: true } }));
  });

  const cellBox = document.querySelector('[data-cells]');
  if (cellBox) {
    cellBox.innerHTML = [...'shape'].map(c => `<span class="cell">${dots(c)}</span>`).join('');
    const ds = [...cellBox.querySelectorAll('i')];
    let near = false;
    ScrollTrigger.create({ trigger: cellBox, start: 'top bottom', end: 'bottom top', onToggle: s => near = s.isActive });
    gsap.ticker.add(() => {
      if (!near) return;
      const auto = touch || !mouse.moved, t = performance.now() / 1000, box = cellBox.getBoundingClientRect();
      const mx = auto ? box.left + box.width * (.5 + .5 * Math.sin(t * .9)) : mouse.x, my = auto ? box.top + box.height / 2 : mouse.y;
      ds.forEach(d => { const b = d.getBoundingClientRect(); d.style.setProperty('--p', clamp(1 - Math.hypot(b.left + 9 - mx, b.top + 9 - my) / 120, 0, 1).toFixed(3)); });
    });
  }

  gsap.utils.toArray('.kp').forEach(k => gsap.from(k, { y: 120, opacity: 0, duration: 1.2, ease: 'expo.out', scrollTrigger: { trigger: k, start: 'top 92%' } }));
  gsap.utils.toArray('.vows li, .hn, .after, .fh, .cols p, .ktext p, .mtext p:not(.big), .oven-l p, .mem-txt p:not(.big), .year-head p').forEach(el =>
    gsap.from(el, { y: 40, opacity: 0, duration: 1, ease: 'power3.out', scrollTrigger: { trigger: el, start: 'top 90%' } }));
  gsap.utils.toArray('.mimg').forEach(m => gsap.from(m, { clipPath: 'inset(12% 12% 12% 12%)', duration: 1.4, ease: 'expo.out', scrollTrigger: { trigger: m, start: 'top 88%' } }));
  const coda = document.querySelector('.coda');
  if (coda) {
    gsap.from('.coda blockquote', { letterSpacing: '.18em', opacity: 0, duration: 1.6, ease: 'expo.out', scrollTrigger: { trigger: coda, start: 'top 75%' } });
    gsap.fromTo('.coda img', { rotate: -10, scale: .8 }, { rotate: 8, scale: 1.1, ease: 'none', scrollTrigger: { trigger: coda, start: 'top bottom', end: 'bottom top', scrub: true } });
  }

  /* ---------------- TASTE ---------------- */
  const ring = document.querySelector('.b-ring');
  if (ring) {
    gsap.to('.b-ring svg', { rotate: 360, duration: 80, repeat: -1, ease: 'none' });
    gsap.to('.b-ring img', { rotate: 40, yPercent: 20, ease: 'none', scrollTrigger: { trigger: '.b-hero', start: 'top top', end: 'bottom top', scrub: true } });
    gsap.from('.b-ring', { scale: .7, opacity: 0, duration: 1.6, delay: .4, ease: 'expo.out' });
    gsap.from('.b-title span', { yPercent: 100, opacity: 0, stagger: .1, duration: 1.2, delay: .55, ease: 'expo.out' });
    gsap.from('.b-kick, .b-sub', { y: 20, opacity: 0, stagger: .1, duration: 1, delay: .8 });
  }

  gsap.utils.toArray('.hw span').forEach(s => gsap.fromTo(s, { clipPath: 'inset(0 100% 0 0)' }, { clipPath: 'inset(0 0% 0 0)', duration: 1.6, ease: 'power2.inOut', scrollTrigger: { trigger: s, start: 'top 85%' } }));

  const oven = document.querySelector('[data-oven]');
  if (oven) {
    const inner = oven.querySelector('.oven-in'), out = oven.querySelector('[data-temp]'), evs = [...oven.querySelectorAll('.evs li')];
    const stops = [[20, [244, 235, 221]], [100, [236, 205, 160]], [150, [196, 112, 52]], [180, [74, 35, 14]]];
    const col = t => {
      for (let i = 1; i < stops.length; i++) if (t <= stops[i][0]) {
        const [a, ca] = stops[i - 1], [b, cb] = stops[i], k = (t - a) / (b - a);
        return `rgb(${ca.map((v, j) => Math.round(v + (cb[j] - v) * k)).join(',')})`;
      }
      return `rgb(${stops.at(-1)[1].join(',')})`;
    };
    const set = p => {
      const t = 20 + p * 160;
      out.textContent = Math.round(t);
      inner.style.background = col(t);
      inner.classList.toggle('hot', t > 135);
      evs.forEach(e => e.classList.toggle('on', t >= +e.dataset.t));
    };
    set(0);
    ScrollTrigger.create({ trigger: oven, start: 'top top', end: 'bottom bottom', scrub: true, onUpdate: s => set(s.progress) });
  }

  const vl = document.querySelector('.vlist'), peek = document.querySelector('.vpeek');
  if (vl && peek && !touch) {
    const pp = { x: 0, y: 0 };
    gsap.ticker.add(() => { pp.x += (mouse.x - pp.x) * .14; pp.y += (mouse.y - pp.y) * .14; peek.style.left = pp.x + 'px'; peek.style.top = pp.y + 'px'; });
    vl.querySelectorAll('li').forEach(li => {
      li.addEventListener('pointerenter', () => { peek.src = li.dataset.img; peek.classList.add('on'); });
      li.addEventListener('pointerleave', () => peek.classList.remove('on'));
    });
  }
  gsap.utils.toArray('.vlist li').forEach(li => gsap.from(li.querySelector('.vw'), { yPercent: 60, opacity: 0, duration: 1, ease: 'expo.out', scrollTrigger: { trigger: li, start: 'top 94%' } }));

  const mem = document.querySelector('.mem-img img');
  if (mem) gsap.from(mem, { y: 80, rotate: -3, opacity: 0, duration: 1.4, ease: 'expo.out', scrollTrigger: { trigger: '.memory', start: 'top 70%' } });

  const leaves = gsap.utils.toArray('.leaf');
  leaves.slice(0, -1).forEach((l, i) => gsap.to(l, { scale: .9, opacity: .35, ease: 'none',
    scrollTrigger: { trigger: leaves[i + 1], start: 'top bottom', end: 'top 25%', scrub: true } }));

  /* ---------------- one annotated page: a "finger" walks the pins until someone hovers ---------------- */
  const pins = [...document.querySelectorAll('.rp .pin')];
  if (pins.length) {
    let k = -1, timer = null, user = false;
    const step = () => { if (user) return; pins.forEach(p => p.classList.remove('on')); k = (k + 1) % pins.length; pins[k].classList.add('on'); };
    ScrollTrigger.create({ trigger: '.rp', start: 'top 70%', end: 'bottom 20%',
      onToggle: s => { clearInterval(timer); pins.forEach(p => p.classList.remove('on')); if (s.isActive && !user) { step(); timer = setInterval(step, 2600); } } });
    pins.forEach(p => {
      p.addEventListener('pointerenter', () => { user = true; clearInterval(timer); pins.forEach(q => q.classList.toggle('on', q === p)); });
      p.addEventListener('click', () => { user = true; clearInterval(timer); pins.forEach(q => q.classList.toggle('on', q === p && !q.classList.contains('on'))); });
    });
  }

  /* ---------------- SIGHT ---------------- */
  const shrink = document.querySelector('[data-shrink]');
  if (shrink) {
    const tl = gsap.timeline({ scrollTrigger: { trigger: shrink, start: 'top top', end: 'bottom bottom', scrub: true } });
    tl.to('.h-house', { scale: 1, ease: 'none' }, 0).to('.h-title span:first-child', { xPercent: -30, opacity: .15, ease: 'none' }, 0)
      .to('.h-title span:last-child', { xPercent: 30, opacity: .15, ease: 'none' }, 0).to('.h-sub', { opacity: 0, ease: 'none' }, 0);
    gsap.from('.h-house', { y: 120, opacity: 0, duration: 1.4, delay: .5, ease: 'expo.out' });
    gsap.from('.h-title span', { yPercent: 100, opacity: 0, stagger: .1, duration: 1.2, delay: .55, ease: 'expo.out' });
  }

  const loupe = document.querySelector('[data-loupe]');
  if (loupe) {
    const lp = { x: .5, y: .5 }; let inside = false;
    loupe.addEventListener('pointerenter', () => inside = true);
    loupe.addEventListener('pointerleave', () => inside = false);
    gsap.ticker.add(() => {
      const r = loupe.getBoundingClientRect();
      if (r.bottom < 0 || r.top > innerHeight) return;
      let tx, ty;
      if (inside && !touch) { tx = (mouse.x - r.left) / r.width; ty = (mouse.y - r.top) / r.height; }
      else { const t = performance.now() / 1000; tx = .5 + .32 * Math.sin(t * .5); ty = .5 + .25 * Math.sin(t * .8 + 1); }
      lp.x += (tx - lp.x) * .15; lp.y += (ty - lp.y) * .15;
      loupe.style.setProperty('--lx', lp.x * 100 + '%'); loupe.style.setProperty('--ly', lp.y * 100 + '%');
      loupe.style.setProperty('--px', lp.x * 100 + '%'); loupe.style.setProperty('--py', lp.y * 100 + '%');
    });
  }

  const moon = document.querySelector('[data-moon]');
  if (moon) {
    const hole = moon.querySelector('.moon-hole'), inner = moon.querySelector('.moon-in');
    const set = p => {
      const max = Math.hypot(innerWidth, innerHeight) / 2;
      const r = gsap.utils.interpolate(Math.min(innerWidth, innerHeight) * .16, max, gsap.parseEase('power2.in')(p));
      hole.style.setProperty('--r', r + 'px'); inner.style.setProperty('--r', r + 'px');
      hole.style.setProperty('--s', 1.3 - .3 * p); inner.style.setProperty('--ring', 1 - p * 1.4);
    };
    set(0);
    ScrollTrigger.create({ trigger: moon, start: 'top top', end: 'bottom bottom', scrub: true, onUpdate: s => set(s.progress) });
  }
  gsap.utils.toArray('.hsteps li, .tiny figure, .loupe-cap').forEach(el => gsap.from(el, { y: 50, opacity: 0, duration: 1, ease: 'power3.out', scrollTrigger: { trigger: el, start: 'top 90%' } }));

  /* ---------------- SOUND: 21 strings, plucked by the cursor ---------------- */
  const sh = document.querySelector('[data-strings]');
  if (sh) {
    const svg = sh.querySelector('svg'), N = 21, NS = 'http://www.w3.org/2000/svg';
    /* guzheng tuning: D pentatonic, low to high */
    const PENT = [0, 2, 4, 7, 9], freq = i => 146.83 * Math.pow(2, (Math.floor(i / 5) * 12 + PENT[i % 5]) / 12);
    const S = [...Array(N)].map((_, i) => { const p = document.createElementNS(NS, 'path'); svg.appendChild(p); return { p, a: 0, y: .5, ph: 0 }; });
    let W = 0, H = 0, ctx = null, on = false;
    const size = () => { W = sh.clientWidth; H = sh.clientHeight; svg.setAttribute('viewBox', `0 0 ${W} ${H}`); };
    size(); addEventListener('resize', size);
    const xs = i => W * (.06 + .88 * i / (N - 1));
    const pluck = (i, y, v) => {
      const s = S[i]; s.a = Math.min(28, 8 + v * .25); s.y = clamp(y / H, .1, .9); s.ph = 0;
      if (on && ctx) {
        const o = ctx.createOscillator(), g = ctx.createGain(), f = ctx.createBiquadFilter();
        o.type = 'triangle'; o.frequency.value = freq(i); f.type = 'lowpass'; f.frequency.value = 2400;
        g.gain.setValueAtTime(0, ctx.currentTime); g.gain.linearRampToValueAtTime(.16, ctx.currentTime + .005);
        g.gain.exponentialRampToValueAtTime(.0005, ctx.currentTime + 2.4);
        o.connect(f).connect(g).connect(ctx.destination); o.start(); o.stop(ctx.currentTime + 2.5);
      }
    };
    let last = null;
    sh.addEventListener('pointermove', e => {
      const r = sh.getBoundingClientRect(), x = e.clientX - r.left, y = e.clientY - r.top;
      if (last) {
        const v = Math.hypot(x - last.x, y - last.y);
        for (let i = 0; i < N; i++) { const sx = xs(i); if ((last.x - sx) * (x - sx) < 0) pluck(i, y, v); }
      }
      last = { x, y };
    });
    sh.addEventListener('pointerleave', () => last = null);
    const btn = sh.querySelector('.snd');
    btn.addEventListener('click', () => {
      ctx = ctx || new (window.AudioContext || window.webkitAudioContext)(); ctx.resume();
      on = !on; btn.setAttribute('aria-pressed', on); btn.textContent = on ? 'Sound on' : 'Sound off';
    });
    let t0 = performance.now(), auto = 0;
    gsap.ticker.add(() => {
      if (sh.getBoundingClientRect().bottom < 0) return;
      const now = performance.now();
      if ((touch || !mouse.moved) && now - auto > 700) { auto = now; pluck(Math.floor(Math.random() * N), H * (.3 + Math.random() * .4), 40); }
      S.forEach((s, i) => {
        s.ph += .55; s.a *= .965;
        const x = xs(i), off = s.a * Math.sin(s.ph);
        s.p.setAttribute('d', `M${x},0 Q${x + off * 2},${s.y * H} ${x},${H}`);
        s.p.classList.toggle('hot', s.a > 1.5);
      });
    });
    gsap.from('.s-title span', { yPercent: 100, opacity: 0, stagger: .1, duration: 1.2, delay: .5, ease: 'expo.out' });
    gsap.from('.s-zheng', { x: 120, opacity: 0, duration: 1.4, delay: .6, ease: 'expo.out' });
  }

  const still = document.querySelector('[data-still]');
  if (still) {
    gsap.timeline({ scrollTrigger: { trigger: still, start: 'top top', end: 'bottom bottom', scrub: true } })
      .fromTo('.still-fig', { scale: .8, rotate: -4 }, { scale: 1.05, rotate: 0, ease: 'none' })
      .from('.still-txt .lines span', { opacity: 0, x: -40, stagger: .2, ease: 'none' }, 0);
  }
  gsap.utils.toArray('.stage figure, .teach-grid figure, .pair img').forEach((el, i) => gsap.from(el, { y: 80, opacity: 0, duration: 1.2, ease: 'expo.out', scrollTrigger: { trigger: el, start: 'top 90%' } }));
  gsap.utils.toArray('.mat img').forEach(m => gsap.fromTo(m, { clipPath: 'inset(10% 8% 10% 8% round 20px)' }, { clipPath: 'inset(0% 0% 0% 0% round 0px)', ease: 'none', scrollTrigger: { trigger: m, start: 'top bottom', end: 'top 20%', scrub: true } }));
})();
