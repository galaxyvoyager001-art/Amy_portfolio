(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const touch = matchMedia('(hover: none)').matches;
  gsap.registerPlugin(ScrollTrigger);
  const lenis = new Lenis({ lerp: 0.09, smoothWheel: !reduce });
  lenis.on('scroll', ScrollTrigger.update);
  gsap.ticker.add(t => lenis.raf(t * 1000));
  gsap.ticker.lagSmoothing(0);

  /* enter: curtain lifts, title rises */
  gsap.set('.curtain', { y: '0%' });
  if (!document.querySelector('.w-hero')) gsap.to('.curtain', { y: '-100%', duration: 0.9, ease: 'power3.inOut', delay: 0.1 });
  else {
    const tl = gsap.timeline();
    tl.to('.curtain', { y: '-100%', duration: 0.9, ease: 'power3.inOut', delay: 0.1 })
      .from('.w-hero h1 .ln > span', { yPercent: 110, duration: 1.1, stagger: 0.08, ease: 'expo.out' }, '-=0.45')
      .from('.w-hero .kick, .w-hero .sub, .w-meta > div', { y: 30, opacity: 0, stagger: 0.06, duration: 0.8, ease: 'power3.out' }, '-=0.8')
      .from('.w-hero .heroimg', { y: 80, opacity: 0, scale: 0.94, duration: 1.3, ease: 'expo.out' }, '-=1.1');
    gsap.to('.w-hero .heroimg', { yPercent: 18, ease: 'none', scrollTrigger: { trigger: '.w-hero', start: 'top top', end: 'bottom top', scrub: true } });
    gsap.to('.w-hero h1', { yPercent: -20, ease: 'none', scrollTrigger: { trigger: '.w-hero', start: 'top top', end: 'bottom top', scrub: true } });
  }

  /* cursor */
  const cur = document.querySelector('.cursor'), ring = cur.querySelector('.ring'), dot = cur.querySelector('.dot');
  const mouse = { x: innerWidth / 2, y: innerHeight / 2 }, rp = { ...mouse };
  addEventListener('pointermove', e => { mouse.x = e.clientX; mouse.y = e.clientY; });
  gsap.ticker.add(() => {
    rp.x += (mouse.x - rp.x) * 0.16; rp.y += (mouse.y - rp.y) * 0.16;
    dot.style.transform = `translate(${mouse.x}px,${mouse.y}px) translate(-50%,-50%)`;
    ring.style.transform = `translate(${rp.x}px,${rp.y}px) translate(-50%,-50%)`;
  });
  document.querySelectorAll('[data-cursor]').forEach(el => {
    el.addEventListener('pointerenter', () => { ring.querySelector('span').textContent = el.dataset.cursor; cur.classList.add('big'); });
    el.addEventListener('pointerleave', () => cur.classList.remove('big'));
  });

  /* intro words light up */
  document.querySelectorAll('.split-words').forEach(p => {
    const walk = node => [...node.childNodes].forEach(n => {
      if (n.nodeType === 3) {
        const f = document.createDocumentFragment();
        n.textContent.split(/(\s+)/).forEach(w => {
          if (!w.trim()) { f.appendChild(document.createTextNode(w)); return; }
          const s = document.createElement('span'); s.className = 'w'; s.textContent = w; f.appendChild(s);
        });
        n.replaceWith(f);
      } else walk(n);
    });
    walk(p);
    gsap.to(p.querySelectorAll('.w'), { opacity: 1, stagger: 0.05, ease: 'none', scrollTrigger: { trigger: p, start: 'top 80%', end: 'bottom 50%', scrub: true } });
  });

  /* counters */
  document.querySelectorAll('[data-count]').forEach(el => {
    const o = { v: 0 }, end = +el.dataset.count, pre = el.dataset.prefix || '', suf = el.dataset.suffix || '', dec = +(el.dataset.dec || 0);
    ScrollTrigger.create({ trigger: el, start: 'top 90%', once: true, onEnter: () =>
      gsap.to(o, { v: end, duration: 1.8, ease: 'power3.out', onUpdate: () => el.textContent = pre + o.v.toFixed(dec) + suf }) });
  });

  /* figures: clip reveal + inner parallax */
  gsap.utils.toArray('.fig').forEach(f => {
    const fr = f.querySelector('.fr'), img = f.querySelector('img');
    gsap.from(fr, { clipPath: 'inset(14% 10% 14% 10% round 16px)', duration: 1.3, ease: 'expo.out', scrollTrigger: { trigger: f, start: 'top 88%' } });
    if (!f.classList.contains('contain') && !f.classList.contains('cut'))
      gsap.fromTo(img, { yPercent: -6 }, { yPercent: 6, ease: 'none', scrollTrigger: { trigger: f, start: 'top bottom', end: 'bottom top', scrub: true } });
  });
  gsap.utils.toArray('.blk h2, .quote blockquote, .band h2').forEach(h => gsap.from(h, { yPercent: 40, opacity: 0, duration: 1.1, ease: 'expo.out', scrollTrigger: { trigger: h, start: 'top 88%' } }));
  gsap.utils.toArray('.blk p, .step, .list div, .note').forEach(el => gsap.from(el, { y: 40, opacity: 0, duration: 0.9, ease: 'power3.out', scrollTrigger: { trigger: el, start: 'top 92%' } }));

  /* menu */
  const btn = document.querySelector('.navbtn');
  btn.addEventListener('click', () => {
    const open = document.documentElement.classList.toggle('menu-open');
    btn.setAttribute('aria-expanded', open); btn.querySelector('.lab').textContent = open ? 'Close' : 'Menu';
    open ? lenis.stop() : lenis.start();
  });
  document.querySelectorAll('.menu a').forEach(a => a.addEventListener('pointerenter', () => {
    document.querySelectorAll('.menu .imgs img').forEach(i => i.classList.toggle('on', i.dataset.k === a.dataset.k));
  }));

  /* leave transition for internal links */
  document.querySelectorAll('a[href]:not([href^="#"]):not([download]):not([target])').forEach(a => a.addEventListener('click', e => {
    const href = a.getAttribute('href'); if (/^https?:/.test(href)) return;
    e.preventDefault();
    gsap.fromTo('.curtain', { y: '100%' }, { y: '0%', duration: 0.7, ease: 'power3.inOut', onComplete: () => location.href = href });
  }));
  addEventListener('pageshow', e => { if (e.persisted) gsap.set('.curtain', { y: '-100%' }); });
  addEventListener('load', () => ScrollTrigger.refresh());
})();
