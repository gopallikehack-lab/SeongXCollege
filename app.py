from flask import Flask, Response

app = Flask(__name__)

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SeongEraStudy · Education is Free for Everyone</title>
<meta name="description" content="SeongEraStudy is a free study portal for every student. Made by Seong Gium Jee.">
<meta name="theme-color" content="#07050b">
<meta property="og:title" content="SeongEraStudy">
<meta property="og:description" content="Education is free for everyone.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=DM+Sans:wght@400;500;600;700&family=Hind:wght@500&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#07050b;
  --ink:#fbf6ff;
  --mut:rgba(251,246,255,.7);
  --a1:#ffa23d;
  --a2:#ff3f86;
  --a3:#7a5cff;
  --grad:linear-gradient(120deg,var(--a1),var(--a2) 55%,var(--a3));
  --glass:rgba(255,255,255,.06);
  --edge:rgba(255,255,255,.14);
  --head:"Sora",system-ui,sans-serif;
  --body:"DM Sans",system-ui,sans-serif;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--ink);font-family:var(--body);line-height:1.6;-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:inherit;text-decoration:none}
:focus-visible{outline:2px solid var(--a1);outline-offset:3px;border-radius:8px}

/* ---------- Backdrop ---------- */
.bg{position:fixed;inset:0;z-index:-2;background:radial-gradient(90% 70% at 80% 10%,#3a1450 0%,var(--bg) 70%)}
.bg video{position:absolute;inset:0;width:100%;height:100%}
.bg #bgb{object-fit:cover;filter:blur(34px) brightness(.55) saturate(1.2);transform:scale(1.18);z-index:1}
.bg #bgf{object-fit:contain;z-index:2}
.shade{position:fixed;inset:0;z-index:-1;pointer-events:none;
  background:
    radial-gradient(70% 60% at 50% 40%,rgba(7,5,11,.18),rgba(7,5,11,.7) 100%),
    linear-gradient(180deg,rgba(7,5,11,.5),rgba(7,5,11,.2) 35%,rgba(7,5,11,.92) 100%)}

/* ---------- Floating nav ---------- */
.nav{position:fixed;top:16px;left:50%;transform:translateX(-50%);z-index:40;width:min(940px,calc(100% - 28px));
  display:flex;align-items:center;justify-content:space-between;gap:14px;padding:10px 10px 10px 22px;border-radius:999px;
  background:rgba(14,9,22,.62);border:1px solid var(--edge);backdrop-filter:blur(18px)}
.logo{font-family:var(--head);font-weight:800;font-size:1.05rem;letter-spacing:-.01em}
.logo b{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.links{display:flex;gap:26px;font-size:.9rem;font-weight:500;color:var(--mut)}
.links a:hover{color:var(--ink)}
.pill{display:inline-flex;align-items:center;gap:8px;padding:11px 22px;border-radius:999px;font-weight:700;font-size:.9rem;background:var(--grad);color:#1a0a10;transition:transform .2s,box-shadow .2s;font-family:var(--body);border:0;cursor:pointer}
.pill:hover{transform:translateY(-2px);box-shadow:0 12px 30px -8px rgba(255,63,134,.7)}
@media(max-width:700px){.links{display:none}}

/* ---------- Hero ---------- */
.hero{min-height:100svh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:130px 22px 90px}
.badge{display:inline-flex;align-items:center;gap:10px;padding:8px 18px;border-radius:999px;background:var(--glass);border:1px solid var(--edge);backdrop-filter:blur(10px);font-size:.85rem;font-weight:600;color:var(--mut)}
.badge i{width:8px;height:8px;border-radius:50%;background:#3ddc97;box-shadow:0 0 0 4px rgba(61,220,151,.2)}
.hero h1{margin-top:26px;font-family:var(--head);font-weight:800;font-size:clamp(2.8rem,8.6vw,7rem);line-height:1;letter-spacing:-.04em;max-width:14ch}
.hero h1 em{font-style:normal;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.hero p{margin-top:24px;max-width:48ch;font-size:clamp(1rem,1.7vw,1.2rem);color:var(--mut)}
.row{display:flex;flex-wrap:wrap;justify-content:center;gap:14px;margin-top:36px}
.pill.big{padding:17px 34px;font-size:1rem}
.ghost{display:inline-flex;align-items:center;gap:10px;padding:16px 30px;border-radius:999px;border:1px solid var(--edge);background:var(--glass);backdrop-filter:blur(12px);font-weight:600;transition:background .2s,border-color .2s,transform .2s}
.ghost:hover{background:rgba(255,255,255,.12);border-color:rgba(255,255,255,.3);transform:translateY(-2px)}
.pill svg,.ghost svg{width:18px;height:18px}
.hero > *{opacity:0;transform:translateY(20px);animation:up .9s cubic-bezier(.2,.7,.2,1) forwards}
.hero > *:nth-child(1){animation-delay:.1s}
.hero > *:nth-child(2){animation-delay:.25s}
.hero > *:nth-child(3){animation-delay:.45s}
.hero > *:nth-child(4){animation-delay:.65s}
.hero > *:nth-child(5){animation-delay:.85s}
@keyframes up{to{opacity:1;transform:none}}
.tri{margin-top:54px;display:flex;flex-wrap:wrap;justify-content:center;gap:10px 34px;font-family:var(--head);font-weight:600;font-size:.95rem;color:var(--mut)}
.tri span::before{content:"";display:inline-block;width:7px;height:7px;margin-right:10px;border-radius:50%;background:var(--grad)}

/* ---------- Ticker ---------- */
.ticker{overflow:hidden;white-space:nowrap;border-block:1px solid var(--edge);background:rgba(7,5,11,.6);backdrop-filter:blur(10px)}
.ticker div{display:inline-flex;animation:scroll 38s linear infinite;padding:20px 0}
.ticker span{font-family:var(--head);font-weight:700;font-size:1.35rem;padding-right:48px;color:rgba(251,246,255,.9)}
.ticker span::after{content:"•";padding-left:48px;color:var(--a2)}
@keyframes scroll{to{transform:translateX(-50%)}}

/* ---------- Sections ---------- */
section{padding:clamp(70px,10vw,130px) 22px}
.wrap{max-width:1120px;margin:0 auto}
.eyebrow{font-weight:700;font-size:.8rem;letter-spacing:.16em;text-transform:uppercase;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
h2{margin-top:12px;font-family:var(--head);font-weight:800;font-size:clamp(2rem,4.8vw,3.6rem);line-height:1.05;letter-spacing:-.03em;max-width:18ch}
.lead{margin-top:16px;color:var(--mut);max-width:52ch}

/* Bento */
.bento{display:grid;grid-template-columns:repeat(6,1fr);gap:16px;margin-top:50px}
.card{position:relative;display:flex;flex-direction:column;justify-content:space-between;gap:30px;padding:30px;border-radius:28px;background:var(--glass);border:1px solid var(--edge);backdrop-filter:blur(16px);overflow:hidden;transition:transform .3s,border-color .3s}
.card::before{content:"";position:absolute;inset:auto -20% -60% auto;width:260px;height:260px;border-radius:50%;background:var(--grad);opacity:.0;filter:blur(70px);transition:opacity .4s}
.card:hover{transform:translateY(-5px);border-color:rgba(255,255,255,.32)}
.card:hover::before{opacity:.45}
.card .no{font-family:var(--head);font-weight:800;font-size:.95rem;color:var(--a1)}
.card h3{font-family:var(--head);font-weight:700;font-size:1.5rem;letter-spacing:-.02em;margin-bottom:8px}
.card p{color:var(--mut);font-size:.97rem}
.card .arrow{align-self:flex-start;display:grid;place-items:center;width:42px;height:42px;border-radius:50%;border:1px solid var(--edge);transition:background .25s,transform .25s}
.card:hover .arrow{background:var(--grad);color:#1a0a10;transform:rotate(-45deg)}
.c1{grid-column:span 3;grid-row:span 2;min-height:340px}
.c1 h3{font-size:2.3rem;line-height:1.08}
.c2,.c3{grid-column:span 3}
.c4{grid-column:span 6;flex-direction:row;align-items:center;flex-wrap:wrap}
@media(max-width:760px){.c1,.c2,.c3,.c4{grid-column:span 6;grid-row:auto;min-height:0}}

/* Steps */
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:0;margin-top:50px;border-top:1px solid var(--edge)}
.step{padding:34px 28px 10px 0}
.step b{font-family:var(--head);font-size:3.6rem;font-weight:800;line-height:1;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.step h3{margin-top:14px;font-family:var(--head);font-size:1.3rem;font-weight:700}
.step p{margin-top:6px;color:var(--mut);font-size:.96rem}

/* Quote */
.quote{text-align:center}
.quote blockquote{font-family:var(--head);font-weight:800;font-size:clamp(2rem,6vw,4.6rem);line-height:1.05;letter-spacing:-.035em;max-width:16ch;margin:0 auto}
.quote blockquote em{font-style:normal;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.quote small{display:block;margin-top:30px;font-family:"Hind",sans-serif;font-size:1.15rem;color:var(--mut)}
.quote small span{display:block;margin-top:4px;font-family:var(--body);font-size:.85rem}

/* Owner */
.owner{display:grid;grid-template-columns:1.1fr 1fr;gap:34px;align-items:center;padding:clamp(28px,5vw,56px);border-radius:34px;background:linear-gradient(135deg,rgba(255,162,61,.16),rgba(255,63,134,.12) 45%,rgba(122,92,255,.18));border:1px solid var(--edge);backdrop-filter:blur(18px)}
@media(max-width:800px){.owner{grid-template-columns:1fr}}
.owner h2{font-size:clamp(1.7rem,3.8vw,2.7rem);max-width:none;line-height:1.2;letter-spacing:-.01em;word-break:break-word}
.owner .role{margin-top:14px;color:var(--mut)}
.owner .links2{display:flex;flex-direction:column;gap:12px}
.lnk{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:18px 22px;border-radius:20px;background:rgba(7,5,11,.55);border:1px solid var(--edge);transition:border-color .2s,transform .2s}
.lnk:hover{border-color:var(--a1);transform:translateX(4px)}
.lnk small{display:block;color:var(--mut);font-size:.78rem;letter-spacing:.08em;text-transform:uppercase}
.lnk strong{font-family:var(--head);font-size:1.1rem}

footer{padding:34px 22px 120px;text-align:center;color:var(--mut);font-size:.9rem;border-top:1px solid var(--edge);background:rgba(7,5,11,.85)}
footer strong{color:var(--ink);font-family:var(--head)}

/* ---------- Sound ---------- */
.sound{position:fixed;left:50%;bottom:20px;transform:translateX(-50%);z-index:50;display:flex;align-items:center;gap:12px;padding:12px 22px 12px 16px;border-radius:999px;
  background:rgba(14,9,22,.72);border:1px solid var(--edge);backdrop-filter:blur(18px);color:var(--ink);font:600 .88rem var(--body);cursor:pointer;transition:border-color .2s,transform .2s,background .2s}
.sound:hover{border-color:rgba(255,255,255,.36);transform:translateX(-50%) translateY(-2px)}
.sound[aria-pressed="true"]{border-color:var(--a2);background:rgba(255,63,134,.2)}
.eq{display:flex;align-items:flex-end;gap:3px;width:22px;height:18px}
.eq i{flex:1;height:28%;border-radius:2px;background:var(--grad)}
.sound[aria-pressed="true"] .eq i{animation:eq 1s ease-in-out infinite}
.sound[aria-pressed="true"] .eq i:nth-child(2){animation-delay:.2s}
.sound[aria-pressed="true"] .eq i:nth-child(3){animation-delay:.4s}
.sound[aria-pressed="true"] .eq i:nth-child(4){animation-delay:.1s}
@keyframes eq{0%,100%{height:25%}50%{height:100%}}

@media(prefers-reduced-motion:reduce){
  *{animation:none!important;transition:none!important}
  .hero > *{opacity:1;transform:none}
  html{scroll-behavior:auto}
}
</style>
</head>
<body>

<div class="bg">
  <video id="bgb" muted loop playsinline preload="auto" aria-hidden="true"
    src="https://huggingface.co/datasets/gopallikehack/Seong_Study/resolve/main/n-261027-9rgev0.mp4"></video>
  <video id="bgf" autoplay muted loop playsinline preload="auto"
    src="https://huggingface.co/datasets/gopallikehack/Seong_Study/resolve/main/n-261027-9rgev0.mp4"></video>
</div>
<div class="shade"></div>

<nav class="nav">
  <a class="logo" href="#top">Seong<b>Era</b>Study</a>
  <div class="links">
    <a href="#learn">Learn</a>
    <a href="#how">How it works</a>
    <a href="#owner">Owner</a>
  </div>
  <a class="pill" href="https://clocks-protective-missed-record.trycloudflare.com/" target="_blank" rel="noopener">Open Portal</a>
</nav>

<main id="top">
  <div class="hero">
    <div class="badge"><i></i> Free study portal · जय श्री कृष्ण</div>
    <h1>Education is <em>free</em> for everyone.</h1>
    <p>SeongEraStudy brings lectures, notes and practice to every student, in one simple portal. Open it and start learning today.</p>
    <div class="row">
      <a class="pill big" href="https://clocks-protective-missed-record.trycloudflare.com/" target="_blank" rel="noopener">
        Start learning
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
      </a>
      <a class="ghost" href="https://t.me/SeongEraStudy" target="_blank" rel="noopener">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.9 4.3 18.7 19.4c-.2 1-.9 1.3-1.7.8l-4.7-3.5-2.3 2.2c-.3.3-.5.5-1 .5l.3-4.8 8.7-7.9c.4-.3-.1-.5-.6-.2L6.6 13 2 11.6c-1-.3-1-1 .2-1.5L20.2 3.2c.8-.3 1.6.2 1.7 1.1Z"/></svg>
        @SeongEraStudy
      </a>
    </div>
    <div class="tri"><span>Free for all</span><span>Simple to use</span><span>Made for students</span></div>
  </div>

  <div class="ticker" aria-hidden="true">
    <div>
      <span>Education is free for everyone</span><span>Learn without limits</span><span>Every student deserves a fair start</span><span>Knowledge grows when shared</span><span>Study today, shape tomorrow</span>
      <span>Education is free for everyone</span><span>Learn without limits</span><span>Every student deserves a fair start</span><span>Knowledge grows when shared</span><span>Study today, shape tomorrow</span>
    </div>
  </div>

  <section id="learn">
    <div class="wrap">
      <div class="eyebrow">What you get</div>
      <h2>One portal. Everything to study.</h2>
      <p class="lead">Learn at your own pace from any phone or laptop.</p>
      <div class="bento">
        <a class="card c1" href="https://clocks-protective-missed-record.trycloudflare.com/" target="_blank" rel="noopener">
          <div><span class="no">01</span><h3 style="margin-top:14px">Video lectures that keep you focused.</h3><p>Watch classes in a clean, smooth player built for learning.</p></div>
          <span class="arrow">→</span>
        </a>
        <a class="card c2" href="https://clocks-protective-missed-record.trycloudflare.com/" target="_blank" rel="noopener">
          <div><span class="no">02</span><h3 style="margin-top:12px">Notes and PDFs</h3><p>Clear study material, ready whenever you are.</p></div>
          <span class="arrow">→</span>
        </a>
        <a class="card c3" href="https://clocks-protective-missed-record.trycloudflare.com/" target="_blank" rel="noopener">
          <div><span class="no">03</span><h3 style="margin-top:12px">Practice and tests</h3><p>Check what you learned and keep getting better.</p></div>
          <span class="arrow">→</span>
        </a>
        <a class="card c4" href="https://t.me/SeongEraStudy" target="_blank" rel="noopener">
          <div style="flex:1;min-width:240px"><span class="no">04</span><h3 style="margin-top:12px">Join the Telegram community</h3><p>Get every update and ask your doubts in the channel.</p></div>
          <span class="arrow">→</span>
        </a>
      </div>
    </div>
  </section>

  <section id="how">
    <div class="wrap">
      <div class="eyebrow">How it works</div>
      <h2>Start in three simple steps.</h2>
      <div class="steps">
        <div class="step"><b>1</b><h3>Open the portal</h3><p>Tap Open Portal. No complicated setup.</p></div>
        <div class="step"><b>2</b><h3>Pick your class</h3><p>Choose the subject or batch you want to study.</p></div>
        <div class="step"><b>3</b><h3>Learn every day</h3><p>Watch, read, practice, and follow the channel for updates.</p></div>
      </div>
    </div>
  </section>

  <section class="quote">
    <div class="wrap">
      <blockquote>Knowledge should never have a <em>price tag.</em></blockquote>
      <small>न हि ज्ञानेन सदृशं पवित्रमिह विद्यते<span>Nothing in this world purifies like knowledge · Bhagavad Gita 4.38</span></small>
    </div>
  </section>

  <section id="owner">
    <div class="wrap">
      <div class="owner">
        <div>
          <div class="eyebrow">Owner</div>
          <h2>夔🌑 𝑺𝒆𝒐𝒏𝒈-𝒋𝒆 ⋆ 𝑂𝑓𝑓𝑙𝑖𝑛𝑒</h2>
          <p class="role">Founder of SeongEraStudy. Made by Seong Gium Jee.</p>
        </div>
        <div class="links2">
          <a class="lnk" href="https://t.me/SeongEra" target="_blank" rel="noopener"><span><small>Owner on Telegram</small><strong>@SeongEra</strong></span><span>→</span></a>
          <a class="lnk" href="https://t.me/SeongEraStudy" target="_blank" rel="noopener"><span><small>Telegram channel</small><strong>@SeongEraStudy</strong></span><span>→</span></a>
          <a class="lnk" href="https://clocks-protective-missed-record.trycloudflare.com/" target="_blank" rel="noopener"><span><small>Study portal</small><strong>Open the portal</strong></span><span>→</span></a>
        </div>
      </div>
    </div>
  </section>
</main>

<footer>
  <strong>SeongEraStudy</strong> · Made by Seong Gium Jee · © <span id="yr"></span>
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

  /* start from the very first frame */
  try{ v.currentTime=0; w.currentTime=0; }catch(e){}
  play();

  /* keep the blurred filler in sync with the main video */
  v.addEventListener('timeupdate',function(){
    if(Math.abs(w.currentTime-v.currentTime)>.4){ w.currentTime=v.currentTime; }
  });

  /* user leaves the tab/site: stop video and music. Back again: continue */
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

  document.getElementById('yr').textContent=new Date().getFullYear();
})();
</script>
</body>
</html>
"""


@app.route("/")
def home():
    return Response(HTML, mimetype="text/html; charset=utf-8")


@app.route("/<path:_>")
def fallback(_):
    return Response(HTML, mimetype="text/html; charset=utf-8")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
