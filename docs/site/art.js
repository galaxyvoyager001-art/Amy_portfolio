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

  const hands = document.querySelector('[data-hands]');
  if (hands) {
    const track = hands.querySelector('.hands-track');
    gsap.to(track, { x: () => -(track.scrollWidth - innerWidth + innerWidth * .1), ease: 'none',
      scrollTrigger: { trigger: hands, start: 'top top', end: 'bottom bottom', scrub: true, invalidateOnRefresh: true } });
    gsap.utils.toArray('.hands-track figure').forEach((f, i) => gsap.from(f.querySelector('img'), { rotate: i % 2 ? 6 : -6, scale: .9, ease: 'none',
      scrollTrigger: { trigger: hands, start: 'top top', end: 'bottom bottom', scrub: true } }));
  }

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
})();
