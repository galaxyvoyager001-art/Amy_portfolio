exec(open('/tmp/claude-0/-home-user-Amy-portfolio/2b4f3ce3-d4ad-5be4-9b15-7ee08bf2127f/scratchpad/m8common.py').read())
GO, DGO = '#C8641E', '#14233F'
grid = ''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="330" stroke="rgba(255,255,255,.07)" stroke-width=".6"/>' for x in range(0, 1920, 40))
grid += ''.join(f'<line x1="0" y1="{y}" x2="1920" y2="{y}" stroke="rgba(255,255,255,.07)" stroke-width=".6"/>' for y in range(0, 330, 40))
for k, a in enumerate([0.9, 0.62, 0.38]):
    pts = ' '.join(f'{x},{320 - a * 300 * (1 - math.exp(-x / 520)):.1f}' for x in range(0, 1930, 12))
    grid += f'<polyline points="{pts}" fill="none" stroke="rgba(242,170,90,.18)" stroke-width="2"/>'
sum20 = ('I wrote all five papers below, as team captain and main modeller, turning open problems into tested models: the optimal scale and cost of water-saving basins for the Panama Canal; the shape of a spinning jump rope for a humanoid robot; optimal sweep routes for responders in a burning building; whether Friday the 13th is really unlucky; and patrol routes and schedules for Etosha National Park. Three of the papers received Finalist awards. As captain I split each problem into sub-models, built and coded the core model myself, and wrote and edited the final paper within the contest deadline.')
papers = [
    ('IMMC 2024 · Problem A', 'Saving the Panama Canal\'s Water', '', '70058dcff24fac17f0138f980193230b', 'Water exchange between the lock and its water-saving basins.',
     ['Without water-saving basins, lock chambers continuously transfer water from upstream to downstream, leading to upstream scarcity, drought and navigation risk.',
      'From the water-exchange diagram between basins and chambers we derived how saved water depends on the number of basins and their size. This gave the optimal basin scale, so no saving potential is wasted.',
      'We then combined energy, maintenance, water, labour and material costs into one overall cost model and, with local data, found the economically optimal design and its annual cost.'],
     'Optimisation · cost model'),
    ('IMMC 2025 · Problem D', 'Teaching a Robot to Jump Rope', '', 'ff4b7949f3f380a474bb4065870c282b', 'The rope\'s 3-D trajectory through one full turn.',
     ['A company asked us to develop a rope-jumping function for its humanoid robot, FlexRobot. We first analysed the robot\'s motion on the ground and in the air.',
      'We treated the rope as a catenary, and noticed that the shape of a rotating catenary can be described by the Jacobi elliptic function sn. We built each of its parameters as a function of time and drew the rope at any moment of a jump in 2-D and 3-D in MATLAB.',
      'Finally we computed the ranges of initial jump velocity, jump time and rope length that make a successful jump possible.'],
     'Catenary · Jacobi sn · MATLAB'),
    ('HiMCM 2025 · Problem A · Finalist', 'Sweeping a Burning Building', '', 'FIRE', 'Potential field of an office floor (left) and simulated fire spread over time (right).',
     ['To plan the best route for responders sweeping a building in an emergency, we minimised total room-clearing time while prioritising occupants\' safety.',
      'A cellular automaton models fire spread, smoke spread, occupant movement and room importance as potential fields; occupants\' speed varies with age and crowd density. Mixed-integer linear programming with CP-SAT then finds the route and number of responders that scan every cell in the shortest time.',
      'We applied it to an office, a restaurant and a school lab, extended it to gas leaks, and tested it with the Fourier Amplitude Sensitivity Test.'],
     'Cellular automaton · MILP'),
    ('IMMC 2026 · Problem D', 'Is Friday the 13th Unlucky?', '', 'f0746e712799f7e00d185b26c3e08a26', 'Predicted "unluckiness" of every date in 2025.',
     ['A severity model combines casualties and economic loss for 2000–2025 disasters. An expectation model, an analogy of the Boltzmann distribution with "temperature" replaced by people\'s level of expectation, gives a Disaster Severity Expectation distribution; information theory turns the gap into surprisal.',
      'The maximum unluckiness was 18.21 and the median 4.42; Friday the 13th averaged 5.56, with no peak, so the superstition is disproved.',
      'A graph model with Greedy Clique Expansion predicted every date in 2025: all values lie within 7–8.'],
     'Boltzmann · entropy · graph cliques'),
    ('IMMC 2026', 'Guarding Etosha National Park', '', 'c23a2b810977e10e64751d8887c4eb4d', 'Risk map of Etosha National Park.',
     ['Etosha sets an immense area against a small ranger team. Our framework runs from risk mapping through topological decomposition and geometric routing to scheduling and staffing.',
      'A risk model merges human threats and natural volatility into one metric. Topological decomposition splits the park into traversable patrol units. Inside each, an Active Contour (Snake) algorithm draws a smooth closed loop, and outward-bulging "petals" reach remaining high-risk clusters.',
      'The Nyquist–Shannon theorem sets a baseline patrol frequency, and the Kalman-filter steady state gives a closed-form safety-critical revisit interval.'],
     'Risk map · Snake routing · Kalman'),
]
cols = ''
for i, (tag, t, _, img, cap, ps, kw) in enumerate(papers):
    x = 56 + i * 366
    ptxt = ''.join(f'<p>{p}</p>' for p in ps)
    if img == 'FIRE':
        imgs = '<img src="/_blob/3cc4032ddcf7b75485c91e6f90844814" alt="Potential field and 2-D graph of an office floor" style="height: 164px; display: block"><div style="display: flex; flex-direction: column; gap: 4px"><img src="/_blob/226909ee7234194fec585542c68a9bbf" alt="Cellular-automaton fire spread across the floor over time" style="width: 200px; display: block"><img src="/_blob/7ac24595d87d86d3f2fa3c35efabbdb5" alt="Smoke concentration spreading over time" style="width: 200px; display: block"></div>'
        cap = 'Potential field of an office floor (left); my simulated fire (top) and smoke (bottom) spreading over time.'
    else:
        imgs = f'<img src="/_blob/{img}" alt="{cap}" style="max-width: 100%; max-height: 164px; display: block">'
    cols += f'''<div style="position: absolute; left: {x}px; top: 358px; width: 340px; height: 572px; display: flex; flex-direction: column; gap: 6px">
<div class="m" style="font-size: 10px; color: {GO}; border-top: 3px solid {GO}; padding-top: 7px">{tag}</div>
<div class="pf" style="font-size: 21px; line-height: 1.1; font-weight: 900; color: {INK}">{t}</div>
<div style="height: 168px; display: flex; gap: 6px; align-items: center; justify-content: center; border-bottom: 1px solid #D9D2C3; padding-bottom: 4px">{imgs}</div>
<div class="fcap" style="padding-top: 0">Fig. {i + 1} · {cap}</div>
<div class="col" style="column-count: 1; font-size: 13px; line-height: 1.5; color: {INK}">{ptxt}</div>
<div class="m" style="font-size: 9.5px; color: #4A5A72; margin-top: auto">{kw}</div>
</div>
'''
body20 = f"""<div style="position: absolute; left: 0; top: 0; width: 1920px; height: 330px; background: {DGO}; overflow: hidden"><svg width="1920" height="330" viewBox="0 0 1920 330" style="position: absolute; left: 0; top: 0" aria-hidden="true">{grid}</svg></div>
<div class="m" style="position: absolute; left: 56px; top: 34px; right: 56px; display: flex; justify-content: space-between; font-size: 11px; color: #C9D6EA"><span>05 — Mind · Research Nº 06 · IMMC · HiMCM · school engineering &amp; mathematics journal</span><span>Amy Hu · 22</span></div>
<div style="position: absolute; left: 56px; top: 70px; width: 600px; display: flex; flex-direction: column; gap: 12px; color: #FFFFFF">
<div class="pf" style="font-size: 42px; line-height: 1.05; font-weight: 900">Mathematical Modelling <span style="color: #F2AA5A; font-style: italic">and Science Publishing</span></div>
<div class="sr" style="font-size: 15px; line-height: 1.4; font-style: italic; color: #C9D6EA"><b style="font-style: normal; color: #FFFFFF">Approach.</b> Turn a messy real problem into variables, assumptions and a model we can test, then explain it clearly.</div>
<div class="m" style="font-size: 10.5px; color: #C9D6EA">Amy Hu · team captain and main modeller · author of all five papers · 3 Finalist awards</div>
</div>
<div class="abs" style="position: absolute; left: 700px; top: 74px; width: 700px; color: #FFFFFF; border-top: 1px solid rgba(255,255,255,.5); padding-top: 10px"><b>Summary</b> &nbsp;{sum20}</div>
<div style="position: absolute; left: 1440px; top: 70px; width: 424px; display: grid; grid-template-columns: 124px minmax(0, 1fr); gap: 16px; color: #FFFFFF">
<img src="/_blob/c2ec89f47e3ad9dc90c13dd2569ab178" alt="Cover of our school journal, Applied Mathematics Vol. 2: IMMC" style="width: 124px; height: 166px; object-fit: cover; display: block; box-shadow: 0 6px 14px rgba(0,0,0,.35)">
<div style="border-left: 4px solid #F2AA5A; padding-left: 14px"><div class="lbl" style="color: #F2AA5A">A separate role: journal editor</div><div class="sr" style="font-size: 13px; line-height: 1.45; padding-top: 4px">I am also an editor of our school's mathematics journal. Our Vol. 2, <i>Applied Mathematics</i>, was an IMMC issue: it explained contest models, including ours, for every reader, alongside interviews with alumni and researchers.</div></div>
</div>
""" + kws([('5', 'papers, all written by me'), ('Captain', 'and main modeller'), ('3×', 'Finalist awards'), ('Vol. 2', 'journal issue on IMMC'), ('200+', 'journal readers')], 700, 1164, 0, col='#FFFFFF', top=250) + cols
write('Mind-Models.dc.html', 'Modelling the world', PAPER, body20)
