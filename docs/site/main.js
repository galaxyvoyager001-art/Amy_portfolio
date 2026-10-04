(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const touch = matchMedia('(hover: none)').matches;
  gsap.registerPlugin(ScrollTrigger);

  /* ---------- smooth scroll ---------- */
  const lenis = new Lenis({ lerp: 0.09, smoothWheel: !reduce });
  lenis.on('scroll', ScrollTrigger.update);
  gsap.ticker.add(t => lenis.raf(t * 1000));
  gsap.ticker.lagSmoothing(0);
  document.querySelectorAll('a[href^="#"]').forEach(a => a.addEventListener('click', e => {
    const t = document.querySelector(a.getAttribute('href'));
    if (!t) return; e.preventDefault(); closeMenu(); lenis.scrollTo(t, { duration: 1.6 });
  }));

  /* ---------- split helpers ---------- */
  document.querySelectorAll('.hero-title .ln').forEach(title => {
    title.innerHTML = [...title.textContent].map(c => `<span class="ch">${c}</span>`).join('');
  });
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
  });

  /* ---------- loader ---------- */
  let seen = false; try { seen = sessionStorage.getItem('amy-seen') === '1'; sessionStorage.setItem('amy-seen', '1'); } catch (e) {}
  lenis.stop();
  const cnt = document.querySelector('.loader .count');
  const intro = gsap.timeline({ onComplete: () => lenis.start() });
  if (seen) { cnt.textContent = '100'; gsap.set('.loader', { display: 'none' }); gsap.set('.curtain', { y: '0%' }); }
  intro.to({ v: seen ? 100 : 0 }, { v: 100, duration: seen ? 0 : (reduce ? 0.1 : 1.6), ease: 'power2.inOut', onUpdate() { cnt.textContent = Math.round(this.targets()[0].v); } })
       .to('.curtain', { y: '0%', duration: seen ? 0 : 0.7, ease: 'power3.inOut' })
       .set('.loader', { display: 'none' })
       .to('.curtain', { y: '-100%', duration: 0.8, ease: 'power3.inOut' })
       .from('.hero-title .ch', { yPercent: 110, opacity: 0, duration: 1.1, stagger: 0.05, ease: 'expo.out' }, '-=0.45')
       .from('.hero-portrait', { y: 120, opacity: 0, duration: 1.2, ease: 'expo.out' }, '<0.1')
       .from('.hero-sign', { opacity: 0, scale: 0.8, duration: 0.8, ease: 'back.out(2)' }, '-=0.6')
       .from('.hero-meta > *', { y: 30, opacity: 0, stagger: 0.08, duration: 0.7, ease: 'power3.out' }, '<');

  /* ---------- cursor ---------- */
  const cur = document.querySelector('.cursor'), ring = cur.querySelector('.ring'), dot = cur.querySelector('.dot');
  const mouse = { x: innerWidth / 2, y: innerHeight / 2 }, rp = { x: mouse.x, y: mouse.y };
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

  /* ---------- hero goo blobs (cursor-reactive) ---------- */
  const g = document.getElementById('goo-g');
  const hero = document.querySelector('.hero-sticky');
  const N = 14, blobs = [];
  for (let i = 0; i < N; i++) {
    const c = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    const r = i === 0 ? 70 : Math.max(16, 62 - i * 3.4);
    c.setAttribute('r', r); g.appendChild(c);
    blobs.push({ c, x: innerWidth * 0.5, y: innerHeight * 0.5, r });
  }
  const drift = [0, 1, 2].map(i => {
    const c = document.createElementNS('http://www.w3.org/2000/svg', 'circle'); c.setAttribute('r', 90 + i * 30); g.appendChild(c);
    return { c, a: i * 2.1, s: 0.0004 + i * 0.00017 };
  });
  let heroIn = true, idle = 0, last = { x: 0, y: 0 };
  ScrollTrigger.create({ trigger: '.hero', start: 'top top', end: 'bottom top', onToggle: s => heroIn = s.isActive });
  gsap.ticker.add((t) => {
    if (!heroIn || reduce) return;
    let tx = mouse.x, ty = mouse.y;
    if (touch || (Math.abs(mouse.x - last.x) + Math.abs(mouse.y - last.y) < 0.5 && ++idle > 120)) {
      tx = innerWidth * (0.5 + 0.28 * Math.sin(t * 0.6)); ty = innerHeight * (0.48 + 0.2 * Math.sin(t * 0.9));
    } else if (Math.abs(mouse.x - last.x) + Math.abs(mouse.y - last.y) >= 0.5) idle = 0;
    last.x = mouse.x; last.y = mouse.y;
    blobs.forEach((b, i) => {
      const lead = i === 0 ? { x: tx, y: ty } : blobs[i - 1];
      const k = i === 0 ? 0.2 : 0.34;
      b.x += (lead.x - b.x) * k; b.y += (lead.y - b.y) * k;
      b.c.setAttribute('cx', b.x.toFixed(1)); b.c.setAttribute('cy', b.y.toFixed(1));
    });
    drift.forEach((d, i) => {
      const a = t * (0.3 + i * 0.13) + d.a;
      d.c.setAttribute('cx', (innerWidth * (0.5 + 0.38 * Math.cos(a))).toFixed(1));
      d.c.setAttribute('cy', (innerHeight * (0.52 + 0.3 * Math.sin(a * 1.3))).toFixed(1));
    });
  });

  /* ---------- hero scroll ---------- */
  gsap.timeline({ scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true } })
    .to('.hero-title', { scale: 1.35, yPercent: -30, ease: 'none' }, 0)
    .to('.hero-portrait', { yPercent: 18, scale: 0.92, ease: 'none' }, 0)
    .to('.hero-sign', { yPercent: -160, rotate: -12, ease: 'none' }, 0)
    .to('.hero-meta', { opacity: 0, ease: 'none' }, 0)
    .to('.hero-goo', { opacity: 0.25, ease: 'none' }, 0.4);
  // gentle parallax of the portrait with the mouse
  if (!touch) addEventListener('pointermove', e => {
    const dx = (e.clientX / innerWidth - 0.5), dy = (e.clientY / innerHeight - 0.5);
    gsap.to('.hero-title', { x: dx * -40, duration: 1.2, ease: 'power3.out', overwrite: 'auto' });
    gsap.to('.hero-portrait', { x: dx * 26, y: dy * 10, duration: 1.2, ease: 'power3.out', overwrite: 'auto' });
  });

  /* ---------- marquees (scroll-velocity aware) ---------- */
  document.querySelectorAll('.marquee').forEach(m => {
    const track = m.querySelector('.track'); const item = track.firstElementChild;
    for (let i = 0; i < 3; i++) track.appendChild(item.cloneNode(true));
    let x = 0; const base = parseFloat(m.dataset.speed || 1);
    gsap.ticker.add(() => {
      const w = item.offsetWidth; if (!w) return;
      const v = lenis.velocity || 0;
      x -= base * (1.2 + Math.min(Math.abs(v) * 0.35, 14)) * (v < 0 ? -1 : 1);
      if (x <= -w) x += w; if (x > 0) x -= w;
      track.style.transform = `translate3d(${x}px,0,0)`;
    });
  });

  /* ---------- manifesto word light-up ---------- */
  document.querySelectorAll('.split-words').forEach(p => {
    gsap.to(p.querySelectorAll('.w'), { opacity: 1, stagger: 0.05, ease: 'none',
      scrollTrigger: { trigger: p, start: 'top 80%', end: 'bottom 45%', scrub: true } });
  });

  /* ---------- counters ---------- */
  document.querySelectorAll('[data-count]').forEach(el => {
    const o = { v: 0 }, end = +el.dataset.count, pre = el.dataset.prefix || '', suf = el.dataset.suffix || '';
    ScrollTrigger.create({ trigger: el, start: 'top 88%', once: true, onEnter: () =>
      gsap.to(o, { v: end, duration: 1.8, ease: 'power3.out', onUpdate: () => el.textContent = pre + Math.round(o.v) + suf }) });
  });

  /* ---------- theme changes ---------- */
  document.querySelectorAll('[data-theme-on]').forEach(s => {
    ScrollTrigger.create({ trigger: s, start: 'top 55%', end: 'bottom 55%',
      onToggle: st => { if (st.isActive) document.body.dataset.theme = s.dataset.themeOn; } });
  });
  ScrollTrigger.create({ trigger: '.hero', start: 'top top', end: 'bottom 55%', onToggle: st => { if (st.isActive) document.body.dataset.theme = 'ink'; } });

  /* ---------- in / off the lab ---------- */
  gsap.utils.toArray('.side').forEach((s, i) => {
    gsap.from(s, { clipPath: 'inset(18% 12% 18% 12% round 22px)', duration: 1.4, ease: 'expo.out',
      scrollTrigger: { trigger: s, start: 'top 85%' } });
    gsap.from(s.querySelectorAll('.big span'), { yPercent: 100, opacity: 0, stagger: 0.1, duration: 1.1, ease: 'expo.out',
      scrollTrigger: { trigger: s, start: 'top 70%' } });
    gsap.to(s.querySelector('.bg img'), { yPercent: -14, ease: 'none', scrollTrigger: { trigger: s, start: 'top bottom', end: 'bottom top', scrub: true } });
  });

  /* ---------- hall ---------- */
  gsap.from('.hall-head .d', { yPercent: 40, opacity: 0, duration: 1.2, ease: 'expo.out', scrollTrigger: { trigger: '.hall', start: 'top 75%' } });
  gsap.from('.thing', { y: 120, opacity: 0, rotate: (i) => (i % 2 ? 4 : -4), stagger: 0.08, duration: 1.1, ease: 'expo.out',
    scrollTrigger: { trigger: '.grid', start: 'top 85%' } });
  if (!touch) document.querySelectorAll('.thing').forEach(t => {
    const img = t.querySelector('.im img');
    t.addEventListener('pointermove', e => {
      const r = t.getBoundingClientRect(); const dx = (e.clientX - r.left) / r.width - 0.5, dy = (e.clientY - r.top) / r.height - 0.5;
      gsap.to(t, { rotateY: dx * 10, rotateX: -dy * 10, transformPerspective: 900, duration: 0.6, ease: 'power3.out' });
      gsap.to(img, { x: dx * 24, y: dy * 24, duration: 0.6, ease: 'power3.out' });
    });
    t.addEventListener('pointerleave', () => { gsap.to(t, { rotateY: 0, rotateX: 0, duration: 0.8, ease: 'elastic.out(1,.5)' }); gsap.to(img, { x: 0, y: 0, duration: 0.8 }); });
  });

  /* ---------- research list with image peek ---------- */
  gsap.from('.research .title', { yPercent: 30, opacity: 0, duration: 1.2, ease: 'expo.out', scrollTrigger: { trigger: '.research', start: 'top 75%' } });
  gsap.from('.rrow', { x: -60, opacity: 0, stagger: 0.07, duration: 1, ease: 'expo.out', scrollTrigger: { trigger: '.rlist', start: 'top 85%' } });
  const peek = document.querySelector('.peek'), pimg = peek.querySelector('img'), pp = { x: 0, y: 0 };
  if (!touch) {
    document.querySelectorAll('.rrow').forEach(r => {
      r.addEventListener('pointerenter', () => { pimg.src = r.dataset.img; peek.classList.add('on'); });
      r.addEventListener('pointerleave', () => peek.classList.remove('on'));
    });
    gsap.ticker.add(() => {
      pp.x += (mouse.x + 190 - pp.x) * 0.12; pp.y += (mouse.y - pp.y) * 0.12;
      peek.style.left = pp.x + 'px'; peek.style.top = pp.y + 'px';
    });
  }

  /* ---------- horizontal gallery ---------- */
  const hz = document.querySelector('.hz'), track = document.querySelector('.hz-track');
  const setH = () => { hz.style.height = (track.scrollWidth - innerWidth + innerHeight) + 'px'; };
  setH(); addEventListener('resize', () => { setH(); ScrollTrigger.refresh(); });
  const hzTween = gsap.to(track, { x: () => -(track.scrollWidth - innerWidth), ease: 'none',
    scrollTrigger: { trigger: hz, start: 'top top', end: 'bottom bottom', scrub: 0.6, invalidateOnRefresh: true } });
  gsap.utils.toArray('.hz-card img').forEach(img => {
    gsap.to(img, { xPercent: -10, ease: 'none', scrollTrigger: { trigger: img.closest('.hz-card'), containerAnimation: hzTween, start: 'left right', end: 'right left', scrub: true } });
  });
  gsap.utils.toArray('.hz-card').forEach(c => {
    gsap.from(c, { rotate: gsap.utils.random(-6, 6), scale: 0.86, ease: 'none',
      scrollTrigger: { trigger: c, containerAnimation: hzTween, start: 'left right', end: 'center center', scrub: true } });
  });

  /* ---------- footer ---------- */
  gsap.from('.footer .bigname', { yPercent: 60, ease: 'none', scrollTrigger: { trigger: '.footer', start: 'top bottom', end: 'bottom bottom', scrub: true } });

  /* ---------- menu ---------- */
  const btn = document.querySelector('.navbtn');
  function closeMenu() { document.documentElement.classList.remove('menu-open'); btn.setAttribute('aria-expanded', 'false'); btn.querySelector('.lab').textContent = 'Menu'; lenis.start(); }
  btn.addEventListener('click', () => {
    const open = document.documentElement.classList.toggle('menu-open');
    btn.setAttribute('aria-expanded', open); btn.querySelector('.lab').textContent = open ? 'Close' : 'Menu';
    open ? lenis.stop() : lenis.start();
  });
  document.querySelectorAll('.menu a').forEach(a => a.addEventListener('pointerenter', () => {
    document.querySelectorAll('.menu .imgs img').forEach(i => i.classList.toggle('on', i.dataset.k === a.dataset.k));
  }));

  /* ---------- page-leave transition ---------- */
  document.querySelectorAll('a[href^="portfolio/"]:not([download]), a[href^="work/"]').forEach(a => a.addEventListener('click', e => {
    e.preventDefault(); const href = a.getAttribute('href');
    gsap.fromTo('.curtain', { y: '100%' }, { y: '0%', duration: 0.7, ease: 'power3.inOut', onComplete: () => location.href = href });
  }));
  addEventListener('pageshow', e => { if (e.persisted) gsap.set('.curtain', { y: '100%' }); });

  addEventListener('load', () => ScrollTrigger.refresh());
})();
