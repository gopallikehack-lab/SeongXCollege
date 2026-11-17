# =====================================================
#  CONFIG  -  change links ONLY here, nowhere else
# =====================================================
PORTAL_LINK  = "https://teaching-responded-pond-payday.trycloudflare.com"
VIDEO_URL    = "https://huggingface.co/datasets/gopallikehack/Seong_Study/resolve/main/a-261025-y6jc8x.mp4"
CHANNEL_LINK = "https://t.me/SeongEraStudy"
OWNER_LINK   = "https://t.me/SeongEra"
# =====================================================

from flask import Flask, Response

app = Flask(__name__)

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SeongEraStudy · Education is Free for Everyone</title>
<meta name="description" content="SeongEraStudy is a free study portal for every student. Made by Seong Gium Jee.">
<meta name="theme-color" content="#0b0b0d">
<meta property="og:title" content="SeongEraStudy">
<meta property="og:description" content="Education is free for everyone.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Barlow:wght@400;500;600;700&family=Noto+Sans+KR:wght@900&display=swap" rel="stylesheet">
<script>document.documentElement.classList.add('js')</script>
<style>
:root{
  --ink:#0b0b0d;
  --steel:#15161a;
  --paper:#efece4;
  --mut:rgba(239,236,228,.7);
  --red:#e3262e;
  --red-d:#8f1318;
  --line:rgba(239,236,228,.16);
  --impact:"Anton","Impact",sans-serif;
  --body:"Barlow",system-ui,sans-serif;
  --kr:"Noto Sans KR",sans-serif;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--paper);font-family:var(--body);font-size:17px;line-height:1.55;-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:inherit;text-decoration:none}
:focus-visible{outline:2px solid var(--red);outline-offset:3px}

/* ---------- Video backdrop ---------- */
.bg{position:fixed;inset:0;z-index:-3;background:radial-gradient(80% 60% at 70% 20%,#2a0b0e,var(--ink) 70%)}
.bg video{position:absolute;inset:0;width:100%;height:100%}
.bg #bgb{object-fit:cover;filter:blur(34px) brightness(.5) saturate(1.1);transform:scale(1.18);z-index:1}
.bg #bgf{object-fit:contain;z-index:2}
.shade{position:fixed;inset:0;z-index:-2;pointer-events:none;
  background:
    linear-gradient(90deg,rgba(11,11,13,.9) 0%,rgba(11,11,13,.55) 45%,rgba(11,11,13,.2) 100%),
    linear-gradient(180deg,rgba(11,11,13,.55),rgba(11,11,13,0) 30%,rgba(11,11,13,.92) 100%)}
.dots{position:fixed;inset:0;z-index:-1;pointer-events:none;opacity:.55;
  background-image:radial-gradient(rgba(255,255,255,.09) 1px,transparent 1.3px);background-size:5px 5px}

/* ---------- Nav ---------- */
.top{position:fixed;top:0;left:0;right:0;z-index:40;display:flex;align-items:center;justify-content:space-between;padding:14px clamp(18px,4vw,56px);
  background:linear-gradient(180deg,rgba(11,11,13,.92),rgba(11,11,13,0));}
.logo{font-family:var(--impact);font-size:1.55rem;letter-spacing:.04em;text-transform:uppercase}
.logo i{font-style:normal;color:var(--red)}
.menu{display:flex;gap:30px;font-weight:600;font-size:.92rem;letter-spacing:.14em;text-transform:uppercase;color:var(--mut)}
.menu a{padding:4px 0;border-bottom:2px solid transparent;transition:color .2s,border-color .2s}
.menu a:hover{color:var(--paper);border-color:var(--red)}
@media(max-width:760px){.menu{display:none}}

.btn{display:inline-flex;align-items:center;gap:12px;padding:16px 38px;font-family:var(--impact);font-size:1.1rem;letter-spacing:.08em;text-transform:uppercase;cursor:pointer;border:0;
  clip-path:polygon(14px 0,100% 0,calc(100% - 14px) 100%,0 100%);transition:transform .15s,background .2s,color .2s}
.btn.red{background:var(--red);color:#fff}
.btn.red:hover{background:#fff;color:var(--red-d);transform:translate(-3px,-3px)}
.btn.dark{background:rgba(239,236,228,.12);color:var(--paper)}
.btn.dark:hover{background:var(--paper);color:var(--ink);transform:translate(-3px,-3px)}
.btn svg{width:18px;height:18px}
.btn.sm{padding:11px 26px;font-size:.95rem}

/* ---------- Hero ---------- */
.hero{min-height:100svh;display:flex;flex-direction:column;justify-content:center;padding:120px clamp(18px,5vw,72px) 80px;max-width:1360px;margin:0 auto;position:relative}
.tag{display:inline-flex;align-items:center;gap:14px;font-weight:700;font-size:.85rem;letter-spacing:.24em;text-transform:uppercase;color:var(--mut)}
.tag::before{content:"";width:46px;height:3px;background:var(--red)}
.tag b{font-family:var(--kr);font-weight:900;letter-spacing:.1em;color:var(--red)}
.hero h1{margin-top:22px;font-family:var(--impact);font-weight:400;text-transform:uppercase;font-size:clamp(3.3rem,11.5vw,9.6rem);line-height:.92;letter-spacing:.005em}
.hero h1 span{display:block}
.glitch{position:relative;display:inline-block;color:var(--red)}
.glitch::before,.glitch::after{content:attr(data-t);position:absolute;inset:0;opacity:0}
.glitch::before{color:#fff;animation:g1 4.5s infinite steps(1)}
.glitch::after{color:var(--red-d);animation:g2 4.5s infinite steps(1)}
@keyframes g1{0%,91%,100%{opacity:0}92%{opacity:.95;transform:translate(-5px,2px);clip-path:inset(8% 0 58% 0)}95%{opacity:.95;transform:translate(4px,-2px);clip-path:inset(62% 0 6% 0)}}
@keyframes g2{0%,92%,100%{opacity:0}93%{opacity:.95;transform:translate(5px,-2px);clip-path:inset(50% 0 20% 0)}96%{opacity:.95;transform:translate(-4px,3px);clip-path:inset(12% 0 60% 0)}}
.caption{margin-top:30px;max-width:520px;padding:16px 20px;background:rgba(239,236,228,.94);color:var(--ink);font-weight:600;font-size:1.05rem;border-left:6px solid var(--red);box-shadow:8px 8px 0 var(--red-d)}
.cta{display:flex;flex-wrap:wrap;gap:16px;margin-top:40px}
.stamp{position:absolute;right:clamp(18px,5vw,72px);bottom:90px;font-family:var(--kr);font-weight:900;font-size:clamp(2.6rem,8vw,6.5rem);line-height:1;color:transparent;-webkit-text-stroke:2px rgba(239,236,228,.28);writing-mode:vertical-rl;letter-spacing:.1em;user-select:none}
@media(max-width:760px){.stamp{display:none}}
.hero > *{opacity:0;transform:translateY(22px);animation:in .8s cubic-bezier(.2,.7,.2,1) forwards}
.hero > *:nth-child(1){animation-delay:.1s}
.hero > *:nth-child(2){animation-delay:.25s}
.hero > *:nth-child(3){animation-delay:.45s}
.hero > *:nth-child(4){animation-delay:.6s}
.hero > .stamp{animation-delay:.9s}
@keyframes in{to{opacity:1;transform:none}}

/* ---------- Slash ticker ---------- */
.slash{margin:20px 0;transform:rotate(-2deg);background:var(--red);color:var(--ink);overflow:hidden;white-space:nowrap;border-block:4px solid var(--ink);box-shadow:0 0 0 2px var(--red-d)}
.slash div{display:inline-flex;animation:run 30s linear infinite;padding:12px 0}
.slash span{font-family:var(--impact);font-size:1.6rem;letter-spacing:.06em;text-transform:uppercase;padding-right:34px}
.slash span::after{content:"✕";padding-left:34px;color:var(--paper)}
@keyframes run{to{transform:translateX(-50%)}}

/* ---------- Sections ---------- */
section{padding:clamp(70px,10vw,130px) clamp(18px,5vw,72px)}
.wrap{max-width:1180px;margin:0 auto}
.kicker{font-weight:700;font-size:.82rem;letter-spacing:.26em;text-transform:uppercase;color:var(--red)}
h2{margin-top:10px;font-family:var(--impact);font-weight:400;text-transform:uppercase;font-size:clamp(2.4rem,6vw,4.8rem);line-height:1;max-width:14ch}
.sub{margin-top:14px;color:var(--mut);max-width:52ch}

.rv{}
.js .rv{opacity:0;transform:translateY(28px);transition:opacity .7s ease,transform .7s cubic-bezier(.2,.7,.2,1)}
.js .rv.in{opacity:1;transform:none}

/* Panels */
.panels{display:grid;grid-template-columns:repeat(6,1fr);gap:18px;margin-top:48px}
.panel{position:relative;display:flex;flex-direction:column;justify-content:flex-end;min-height:230px;padding:28px;background:rgba(21,22,26,.86);backdrop-filter:blur(8px);border-left:5px solid var(--red);
  clip-path:polygon(0 0,calc(100% - 26px) 0,100% 26px,100% 100%,26px 100%,0 calc(100% - 26px));transition:transform .2s,background .2s}
.panel:hover{transform:translate(-4px,-4px);background:rgba(36,14,17,.92)}
.panel .n{position:absolute;top:6px;right:18px;font-family:var(--impact);font-size:5.5rem;line-height:1;color:rgba(239,236,228,.09);transition:color .2s}
.panel:hover .n{color:rgba(227,38,46,.5)}
.panel h3{font-family:var(--impact);font-weight:400;font-size:1.9rem;text-transform:uppercase;letter-spacing:.02em}
.panel p{margin-top:6px;color:var(--mut);font-size:.98rem}
.panel .go{margin-top:16px;font-weight:700;font-size:.8rem;letter-spacing:.2em;text-transform:uppercase;color:var(--red)}
.p1{grid-column:span 4;min-height:300px}
.p1 h3{font-size:3rem;line-height:1}
.p2{grid-column:span 2}
.p3{grid-column:span 3}
.p4{grid-column:span 3}
@media(max-width:800px){.p1,.p2,.p3,.p4{grid-column:span 6;min-height:210px}}

/* Red band: steps */
.band{background:var(--red);color:var(--ink);clip-path:polygon(0 5vw,100% 0,100% calc(100% - 5vw),0 100%);padding-block:calc(5vw + 60px)}
.band .kicker{color:var(--ink)}
.band h2{color:var(--ink)}
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:30px;margin-top:44px}
.step b{display:block;font-family:var(--impact);font-weight:400;font-size:5.5rem;line-height:.9;color:var(--ink);-webkit-text-stroke:0}
.step h3{margin-top:8px;font-family:var(--impact);font-weight:400;font-size:1.7rem;text-transform:uppercase}
.step p{margin-top:4px;font-weight:600}

/* Hero character */
.hero2{display:grid;grid-template-columns:1.1fr 1fr;gap:40px;align-items:center}
@media(max-width:860px){.hero2{grid-template-columns:1fr}}
.ghostkr{position:relative;min-height:300px;display:grid;place-items:center;border:2px solid var(--line);background:rgba(21,22,26,.7);backdrop-filter:blur(8px);overflow:hidden;
  clip-path:polygon(0 0,calc(100% - 40px) 0,100% 40px,100% 100%,40px 100%,0 calc(100% - 40px))}
.ghostkr strong{font-family:var(--kr);font-weight:900;font-size:clamp(3rem,9vw,6.5rem);line-height:1.05;letter-spacing:.08em;color:transparent;-webkit-text-stroke:2px var(--red);text-align:center}
.ghostkr em{position:absolute;bottom:14px;left:20px;font-style:normal;font-weight:700;font-size:.75rem;letter-spacing:.3em;text-transform:uppercase;color:var(--mut)}
.name{font-family:var(--impact);font-weight:400;text-transform:uppercase;font-size:clamp(2.6rem,6vw,4.6rem);line-height:1}
.name span{color:var(--red)}
.hero2 p{margin-top:16px;color:var(--mut);max-width:46ch}

/* Owner */
.owner{display:grid;grid-template-columns:1.1fr 1fr;gap:34px;align-items:center;padding:clamp(26px,5vw,54px);background:rgba(21,22,26,.88);backdrop-filter:blur(10px);border:2px solid var(--line);border-top:6px solid var(--red)}
@media(max-width:820px){.owner{grid-template-columns:1fr}}
.owner h2{font-size:clamp(1.7rem,3.8vw,2.6rem);max-width:none;line-height:1.25;font-family:var(--body);font-weight:700;text-transform:none;word-break:break-word}
.owner .role{margin-top:12px;color:var(--mut)}
.links{display:flex;flex-direction:column;gap:12px}
.lnk{display:flex;align-items:center;justify-content:space-between;gap:14px;padding:16px 20px;background:rgba(11,11,13,.7);border:1px solid var(--line);transition:border-color .2s,transform .2s,background .2s}
.lnk:hover{border-color:var(--red);transform:translateX(6px);background:rgba(227,38,46,.12)}
.lnk small{display:block;color:var(--mut);font-size:.74rem;letter-spacing:.2em;text-transform:uppercase}
.lnk strong{font-family:var(--impact);font-weight:400;font-size:1.3rem;letter-spacing:.04em}
.lnk > span:last-child{color:var(--red);font-size:1.4rem}

footer{padding:30px 20px 120px;text-align:center;color:var(--mut);font-size:.9rem;border-top:1px solid var(--line);background:rgba(11,11,13,.88)}
footer strong{font-family:var(--impact);font-weight:400;letter-spacing:.06em;color:var(--paper);font-size:1.1rem}
footer small{display:block;margin-top:6px;opacity:.6;font-size:.78rem}

/* ---------- Sound ---------- */
.sound{position:fixed;left:50%;bottom:20px;transform:translateX(-50%);z-index:50;display:flex;align-items:center;gap:12px;padding:12px 28px 12px 20px;border:0;cursor:pointer;
  background:var(--paper);color:var(--ink);font:700 .9rem var(--body);letter-spacing:.14em;text-transform:uppercase;
  clip-path:polygon(12px 0,100% 0,calc(100% - 12px) 100%,0 100%);transition:background .2s,color .2s,transform .15s}
.sound:hover{transform:translateX(-50%) translateY(-3px)}
.sound[aria-pressed="true"]{background:var(--red);color:#fff}
.eq{display:flex;align-items:flex-end;gap:3px;width:22px;height:18px}
.eq i{flex:1;height:28%;background:currentColor}
.sound[aria-pressed="true"] .eq i{animation:eq .9s ease-in-out infinite}
.sound[aria-pressed="true"] .eq i:nth-child(2){animation-delay:.2s}
.sound[aria-pressed="true"] .eq i:nth-child(3){animation-delay:.4s}
.sound[aria-pressed="true"] .eq i:nth-child(4){animation-delay:.1s}
@keyframes eq{0%,100%{height:25%}50%{height:100%}}

@media(prefers-reduced-motion:reduce){
  *{animation:none!important;transition:none!important}
  .hero > *{opacity:1;transform:none}
  .js .rv{opacity:1;transform:none}
  html{scroll-behavior:auto}
}
</style>
</head>
<body>

<div class="bg">
  <video id="bgb" muted loop playsinline preload="auto" aria-hidden="true" src="{{VIDEO}}"></video>
  <video id="bgf" autoplay muted loop playsinline preload="auto" src="{{VIDEO}}"></video>
</div>
<div class="shade"></div>
<div class="dots"></div>

<header class="top">
  <a class="logo" href="#top">Seong<i>Era</i>Study</a>
  <nav class="menu">
    <a href="#learn">Learn</a>
    <a href="#steps">Steps</a>
    <a href="#hero">The Hero</a>
    <a href="#owner">Owner</a>
  </nav>
  <a class="btn red sm" href="{{PORTAL}}" target="_blank" rel="noopener">Open Portal</a>
</header>

<main id="top">
  <div class="hero">
    <div class="tag">SeongEraStudy <b>약한영웅</b></div>
    <h1><span>Education</span><span>is <b class="glitch" data-t="FREE">FREE</b></span><span>for everyone.</span></h1>
    <div class="caption">Weak or strong, every student deserves to learn. Real power starts with knowledge.</div>
    <div class="cta">
      <a class="btn red" href="{{PORTAL}}" target="_blank" rel="noopener">
        Start learning
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
      </a>
      <a class="btn dark" href="{{CHANNEL}}" target="_blank" rel="noopener">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.9 4.3 18.7 19.4c-.2 1-.9 1.3-1.7.8l-4.7-3.5-2.3 2.2c-.3.3-.5.5-1 .5l.3-4.8 8.7-7.9c.4-.3-.1-.5-.6-.2L6.6 13 2 11.6c-1-.3-1-1 .2-1.5L20.2 3.2c.8-.3 1.6.2 1.7 1.1Z"/></svg>
        Join Channel
      </a>
    </div>
    <div class="stamp" aria-hidden="true">약한영웅</div>
  </div>

  <div class="slash" aria-hidden="true">
    <div>
      <span>Education is free for everyone</span><span>Study smart</span><span>Stay sharp</span><span>No student left behind</span><span>Knowledge is power</span>
      <span>Education is free for everyone</span><span>Study smart</span><span>Stay sharp</span><span>No student left behind</span><span>Knowledge is power</span>
    </div>
  </div>

  <section id="learn">
    <div class="wrap">
      <div class="kicker rv">What you get</div>
      <h2 class="rv">Everything you need. Zero cost.</h2>
      <p class="sub rv">One portal for your whole study game. Open it on any phone or laptop.</p>
      <div class="panels">
        <a class="panel p1 rv" href="{{PORTAL}}" target="_blank" rel="noopener"><span class="n">01</span><h3>Video lectures</h3><p>Watch classes in a clean player that keeps you focused from start to end.</p><span class="go">Enter portal →</span></a>
        <a class="panel p2 rv" href="{{PORTAL}}" target="_blank" rel="noopener"><span class="n">02</span><h3>Notes and PDFs</h3><p>Clear material, ready any time.</p><span class="go">Open →</span></a>
        <a class="panel p3 rv" href="{{PORTAL}}" target="_blank" rel="noopener"><span class="n">03</span><h3>Practice and tests</h3><p>Test yourself and keep levelling up.</p><span class="go">Open →</span></a>
        <a class="panel p4 rv" href="{{CHANNEL}}" target="_blank" rel="noopener"><span class="n">04</span><h3>Telegram community</h3><p>Updates and doubt support in the channel.</p><span class="go">Join →</span></a>
      </div>
    </div>
  </section>

  <section id="steps" class="band">
    <div class="wrap">
      <div class="kicker rv">How it works</div>
      <h2 class="rv">Three steps. Start now.</h2>
      <div class="steps">
        <div class="step rv"><b>01</b><h3>Open the portal</h3><p>Tap Open Portal. No setup needed.</p></div>
        <div class="step rv"><b>02</b><h3>Pick your class</h3><p>Choose the subject you want to study.</p></div>
        <div class="step rv"><b>03</b><h3>Study every day</h3><p>Watch, read, practice and follow the channel.</p></div>
      </div>
    </div>
  </section>

  <section id="hero">
    <div class="wrap hero2">
      <div class="ghostkr rv"><strong>약한<br>영웅</strong><em>Weak Hero</em></div>
      <div class="rv">
        <div class="kicker">The hero of our portal</div>
        <div class="name" style="margin-top:12px">Seong <span>Jee</span> Gium</div>
        <p>A character from Weak Hero. Not the loudest in the room, but never someone to underestimate. Learn like him: stay calm, stay sharp, keep growing.</p>
      </div>
    </div>
  </section>

  <section id="owner">
    <div class="wrap">
      <div class="owner rv">
        <div>
          <div class="kicker">Owner</div>
          <h2>夔🌑 𝑺𝒆𝒐𝒏𝒈-𝒋𝒆 ⋆ 𝑂𝑓𝑓𝑙𝑖𝑛𝑒</h2>
          <p class="role">Founder of SeongEraStudy. Made by Seong Gium Jee.</p>
        </div>
        <div class="links">
          <a class="lnk" href="{{OWNER}}" target="_blank" rel="noopener"><span><small>Owner on Telegram</small><strong>@SeongEra</strong></span><span>→</span></a>
          <a class="lnk" href="{{CHANNEL}}" target="_blank" rel="noopener"><span><small>Telegram channel</small><strong>@SeongEraStudy</strong></span><span>→</span></a>
          <a class="lnk" href="{{PORTAL}}" target="_blank" rel="noopener"><span><small>Study portal</small><strong>Open the portal</strong></span><span>→</span></a>
        </div>
      </div>
    </div>
  </section>
</main>

<footer>
  <strong>SeongEraStudy</strong> · Made by Seong Gium Jee · © <span id="yr"></span>
  <small>Weak Hero fan-inspired design. Not affiliated with the original creators.</small>
</footer>

<button class="sound" id="snd" type="button" aria-pressed="false" aria-label="Turn music on">
  <span class="eq" aria-hidden="true"><i></i><i></i><i></i><i></i></span>
  <span id="sndl">Music off</span>
</button>

<script>
(function(){
  var v=document.getElementById('bgf'),
      w=document.getElementById('bgb'),
      b=document.getElementById('snd'),
      l=document.getElementById('sndl');

  function safe(p){ if(p&&p.catch)p.catch(function(){}); }
  function play(){ safe(v.play()); safe(w.play()); }
  function stop(){ v.pause(); w.pause(); }

  try{ v.currentTime=0; w.currentTime=0; }catch(e){}
  play();

  v.addEventListener('timeupdate',function(){
    if(Math.abs(w.currentTime-v.currentTime)>.4){ w.currentTime=v.currentTime; }
  });

  document.addEventListener('visibilitychange',function(){
    if(document.hidden){ stop(); } else { play(); }
  });
  window.addEventListener('pagehide',stop);
  window.addEventListener('pageshow',function(){ if(!document.hidden){ play(); } });

  b.addEventListener('click',function(){
    var on=v.muted;
    v.muted=!on;
    if(on){ v.volume=.8; }
    play();
    b.setAttribute('aria-pressed',on);
    b.setAttribute('aria-label',on?'Turn music off':'Turn music on');
    l.textContent=on?'Music on':'Music off';
  });

  var items=document.querySelectorAll('.rv');
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){
      es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
    },{threshold:.12});
    items.forEach(function(el,i){ el.style.transitionDelay=((i%4)*70)+'ms'; io.observe(el); });
  } else {
    items.forEach(function(el){ el.classList.add('in'); });
  }

  document.getElementById('yr').textContent=new Date().getFullYear();
})();
</script>
</body>
</html>
"""

PAGE = (
    HTML.replace("{{PORTAL}}", PORTAL_LINK)
        .replace("{{VIDEO}}", VIDEO_URL)
        .replace("{{CHANNEL}}", CHANNEL_LINK)
        .replace("{{OWNER}}", OWNER_LINK)
)


@app.route("/")
def home():
    return Response(PAGE, mimetype="text/html; charset=utf-8")


@app.route("/<path:_>")
def fallback(_):
    return Response(PAGE, mimetype="text/html; charset=utf-8")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
