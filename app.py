from flask import Flask, Response

app = Flask(__name__)

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SeongEraStudy · Education is Free for Everyone</title>
<meta name="description" content="SeongEraStudy is a free study portal. Lectures, notes and practice for every student. Made by Seong Gium Jee.">
<meta name="theme-color" content="#070b1a">
<meta property="og:title" content="SeongEraStudy">
<meta property="og:description" content="Education is free for everyone.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Manrope:wght@400;500;600;700&family=Tiro+Devanagari+Sanskrit:ital@0;1&display=swap" rel="stylesheet">
<style>
:root{
  --night:#070b1a;
  --deep:#0a1630;
  --peacock:#12a3a8;
  --gold:#e4b45c;
  --gold-soft:#f3d79a;
  --ivory:#f6f0e2;
  --mist:rgba(246,240,226,.72);
  --line:rgba(228,180,92,.28);
  --serif:"Cormorant Garamond",Georgia,serif;
  --sans:"Manrope",system-ui,sans-serif;
  --deva:"Tiro Devanagari Sanskrit","Cormorant Garamond",serif;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--night);color:var(--ivory);font-family:var(--sans);line-height:1.6;-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:inherit;text-decoration:none}
:focus-visible{outline:2px solid var(--gold);outline-offset:3px;border-radius:4px}

/* ---------- Video backdrop ---------- */
.backdrop{position:fixed;inset:0;z-index:-2;background:radial-gradient(120% 80% at 70% 20%,#0f3a52 0%,var(--deep) 45%,var(--night) 100%)}
.backdrop video{width:100%;height:100%;object-fit:cover;opacity:0;transition:opacity 1.6s ease}
.backdrop video.ready{opacity:1}
.veil{position:fixed;inset:0;z-index:-1;pointer-events:none;
  background:
    linear-gradient(90deg,rgba(7,11,26,.88) 0%,rgba(7,11,26,.55) 48%,rgba(7,11,26,.25) 100%),
    linear-gradient(180deg,rgba(7,11,26,.55) 0%,rgba(7,11,26,0) 30%,rgba(7,11,26,.9) 100%)}

/* ---------- Nav ---------- */
header{position:fixed;top:0;left:0;right:0;z-index:20;display:flex;align-items:center;justify-content:space-between;padding:18px clamp(20px,5vw,64px);
  background:linear-gradient(180deg,rgba(7,11,26,.85),rgba(7,11,26,0));backdrop-filter:blur(2px)}
.brand{display:flex;align-items:center;gap:12px;font-family:var(--serif);font-size:1.5rem;font-weight:700;letter-spacing:.01em}
.brand i{display:grid;place-items:center;width:38px;height:38px;border-radius:50%;border:1px solid var(--gold);color:var(--gold);font-style:normal;font-size:1.1rem;background:rgba(228,180,92,.08)}
nav{display:flex;gap:28px;font-size:.92rem;font-weight:500;color:var(--mist)}
nav a{padding:6px 0;border-bottom:1px solid transparent;transition:color .2s,border-color .2s}
nav a:hover{color:var(--gold-soft);border-color:var(--gold)}
@media(max-width:720px){nav{display:none}}

/* ---------- Hero ---------- */
.hero{min-height:100svh;display:flex;flex-direction:column;justify-content:center;padding:130px clamp(20px,5vw,64px) 90px;max-width:1280px;margin:0 auto}
.hero .om{font-family:var(--deva);font-size:1.35rem;color:var(--gold);margin-bottom:22px}
.hero h1{font-family:var(--serif);font-weight:600;font-size:clamp(3rem,9vw,7.4rem);line-height:.98;letter-spacing:-.015em;max-width:11ch;
  background:linear-gradient(180deg,#fff6df 10%,var(--gold) 95%);-webkit-background-clip:text;background-clip:text;color:transparent}
.hero p.lead{margin-top:26px;max-width:46ch;font-size:clamp(1.02rem,1.6vw,1.2rem);color:var(--mist)}
.cta-row{display:flex;flex-wrap:wrap;gap:14px;margin-top:38px}
.btn{display:inline-flex;align-items:center;gap:10px;padding:15px 28px;border-radius:999px;font-weight:700;font-size:.98rem;transition:transform .2s,box-shadow .2s,background .2s,border-color .2s;cursor:pointer;border:1px solid transparent;font-family:var(--sans)}
.btn.gold{background:linear-gradient(135deg,#f3d79a,#e4b45c 55%,#c98f2e);color:#1b1304;box-shadow:0 10px 34px -8px rgba(228,180,92,.55)}
.btn.gold:hover{transform:translateY(-2px);box-shadow:0 16px 40px -8px rgba(228,180,92,.75)}
.btn.ghost{border-color:var(--line);color:var(--ivory);background:rgba(7,11,26,.35);backdrop-filter:blur(8px)}
.btn.ghost:hover{border-color:var(--gold);background:rgba(228,180,92,.1)}
.btn svg{width:18px;height:18px}
.scroll-hint{position:absolute;left:clamp(20px,5vw,64px);bottom:28px;font-size:.8rem;color:var(--mist);display:flex;align-items:center;gap:12px}
.scroll-hint::before{content:"";width:46px;height:1px;background:var(--gold)}

/* hero entrance: one orchestrated moment */
.hero > *{opacity:0;transform:translateY(18px);animation:rise .9s cubic-bezier(.2,.7,.2,1) forwards}
.hero > *:nth-child(1){animation-delay:.15s}
.hero > *:nth-child(2){animation-delay:.3s}
.hero > *:nth-child(3){animation-delay:.5s}
.hero > *:nth-child(4){animation-delay:.7s}
@keyframes rise{to{opacity:1;transform:none}}

/* ---------- Ribbon of lines ---------- */
.ribbon{border-block:1px solid var(--line);background:rgba(7,11,26,.62);backdrop-filter:blur(10px);overflow:hidden;white-space:nowrap}
.ribbon div{display:inline-flex;gap:56px;padding:18px 0;animation:tick 42s linear infinite;font-family:var(--serif);font-size:1.45rem;font-style:italic;color:var(--gold-soft)}
.ribbon span::after{content:"✦";margin-left:56px;color:var(--peacock);font-style:normal;font-size:.9rem}
@keyframes tick{to{transform:translateX(-50%)}}

/* ---------- Sections ---------- */
section{padding:clamp(70px,11vw,140px) clamp(20px,5vw,64px)}
.wrap{max-width:1180px;margin:0 auto}
h2{font-family:var(--serif);font-weight:600;font-size:clamp(2.2rem,5vw,4rem);line-height:1.05;letter-spacing:-.01em;max-width:16ch}
.sub{margin-top:16px;color:var(--mist);max-width:50ch}

/* Learn list */
.learn{display:grid;grid-template-columns:1fr 1.25fr;gap:clamp(30px,6vw,90px);align-items:start}
@media(max-width:860px){.learn{grid-template-columns:1fr}}
.rows{border-top:1px solid var(--line)}
.row{display:grid;grid-template-columns:auto 1fr auto;gap:20px;align-items:center;padding:26px 6px;border-bottom:1px solid var(--line);transition:background .25s,padding .25s}
.row:hover{background:linear-gradient(90deg,rgba(18,163,168,.12),transparent);padding-left:18px}
.row .ic{width:46px;height:46px;border-radius:14px;display:grid;place-items:center;background:rgba(18,163,168,.14);color:var(--peacock);border:1px solid rgba(18,163,168,.35)}
.row .ic svg{width:22px;height:22px}
.row h3{font-family:var(--serif);font-size:1.6rem;font-weight:600}
.row p{color:var(--mist);font-size:.95rem}
.row .go{color:var(--gold);font-size:1.3rem;transition:transform .25s}
.row:hover .go{transform:translateX(6px)}

/* Shloka */
.shloka{text-align:center;background:linear-gradient(180deg,rgba(7,11,26,0),rgba(10,22,48,.78) 30%,rgba(10,22,48,.78) 70%,rgba(7,11,26,0))}
.shloka .deva{font-family:var(--deva);font-size:clamp(1.7rem,4.2vw,3.1rem);line-height:1.5;color:var(--gold-soft);max-width:22ch;margin:0 auto}
.shloka .mean{margin:26px auto 0;font-family:var(--serif);font-style:italic;font-size:clamp(1.2rem,2.2vw,1.6rem);color:var(--ivory);max-width:34ch}
.shloka small{display:block;margin-top:14px;color:var(--mist);font-size:.85rem}

/* Promise */
.promise{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:0;margin-top:50px;border:1px solid var(--line);border-radius:26px;overflow:hidden;background:rgba(7,11,26,.55);backdrop-filter:blur(12px)}
.promise div{padding:34px 30px;border-right:1px solid var(--line)}
.promise div:last-child{border-right:0}
@media(max-width:700px){.promise div{border-right:0;border-bottom:1px solid var(--line)}.promise div:last-child{border-bottom:0}}
.promise b{display:block;font-family:var(--serif);font-size:1.7rem;font-weight:600;color:var(--gold-soft);margin-bottom:6px}
.promise span{color:var(--mist);font-size:.95rem}

/* Join */
.join{text-align:center}
.join h2{margin:0 auto}
.join .sub{margin-inline:auto}
.join .cta-row{justify-content:center}
.owner{margin-top:34px;font-size:.95rem;color:var(--mist)}
.owner a{color:var(--gold-soft);border-bottom:1px solid var(--line)}
.owner a:hover{border-color:var(--gold)}

footer{border-top:1px solid var(--line);padding:30px clamp(20px,5vw,64px) 110px;text-align:center;color:var(--mist);font-size:.9rem;background:rgba(7,11,26,.8)}
footer strong{font-family:var(--serif);font-size:1.15rem;color:var(--gold-soft);font-weight:600}

/* ---------- Sound control ---------- */
.sound{position:fixed;right:clamp(16px,3vw,34px);bottom:clamp(16px,3vw,30px);z-index:30;display:flex;align-items:center;gap:12px;padding:12px 20px 12px 14px;border-radius:999px;
  background:rgba(7,11,26,.72);border:1px solid var(--line);backdrop-filter:blur(14px);color:var(--ivory);font:600 .88rem var(--sans);cursor:pointer;transition:border-color .2s,background .2s,transform .2s}
.sound:hover{border-color:var(--gold);transform:translateY(-2px)}
.sound[aria-pressed="true"]{background:rgba(18,163,168,.22);border-color:var(--peacock)}
.eq{display:flex;align-items:flex-end;gap:3px;width:22px;height:20px}
.eq i{flex:1;background:var(--gold);border-radius:2px;height:30%}
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

<div class="backdrop">
  <video id="bg" autoplay muted loop playsinline preload="auto"
    src="https://huggingface.co/datasets/gopallikehack/Seong_Study/resolve/main/n-261027-9rgev0.mp4"></video>
</div>
<div class="veil"></div>

<header>
  <a class="brand" href="#top" aria-label="SeongEraStudy home"><i>॥</i>SeongEraStudy</a>
  <nav>
    <a href="#learn">Learn</a>
    <a href="#promise">Our promise</a>
    <a href="#join">Join</a>
  </nav>
</header>

<main id="top">
  <div class="hero">
    <div class="om">॥ श्री कृष्णाय नमः ॥</div>
    <h1>Education is free for everyone.</h1>
    <p class="lead">SeongEraStudy is a free study portal for every student. Open it, pick a class and start learning today. No fees, no gates.</p>
    <div class="cta-row">
      <a class="btn gold" href="https://devel-novelty-cayman-clearance.trycloudflare.com/" target="_blank" rel="noopener">
        Start learning
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
      </a>
      <a class="btn ghost" href="https://t.me/SeongEraStudy" target="_blank" rel="noopener">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.9 4.3 18.7 19.4c-.2 1-.9 1.3-1.7.8l-4.7-3.5-2.3 2.2c-.3.3-.5.5-1 .5l.3-4.8 8.7-7.9c.4-.3-.1-.5-.6-.2L6.6 13 2 11.6c-1-.3-1-1 .2-1.5L20.2 3.2c.8-.3 1.6.2 1.7 1.1Z"/></svg>
        Join on Telegram
      </a>
    </div>
    <div class="scroll-hint">Scroll to explore</div>
  </div>

  <div class="ribbon" aria-hidden="true">
    <div>
      <span>Education is free for everyone</span><span>Learn without limits</span><span>Knowledge grows when it is shared</span><span>Every student deserves a fair start</span><span>Study today, shape tomorrow</span>
      <span>Education is free for everyone</span><span>Learn without limits</span><span>Knowledge grows when it is shared</span><span>Every student deserves a fair start</span><span>Study today, shape tomorrow</span>
    </div>
  </div>

  <section id="learn">
    <div class="wrap learn">
      <div>
        <h2>Everything you need to study, in one portal.</h2>
        <p class="sub">Open the portal and learn at your own pace, from any phone or laptop.</p>
      </div>
      <div class="rows">
        <a class="row" href="https://devel-novelty-cayman-clearance.trycloudflare.com/" target="_blank" rel="noopener">
          <span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="3"/><path d="m10 9.5 5 2.5-5 2.5z" fill="currentColor"/></svg></span>
          <span><h3>Video lectures</h3><p>Watch classes with a smooth, easy player.</p></span>
          <span class="go">→</span>
        </a>
        <a class="row" href="https://devel-novelty-cayman-clearance.trycloudflare.com/" target="_blank" rel="noopener">
          <span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h9l4 4v14H6z"/><path d="M14 3v5h5M9 13h7M9 17h7"/></svg></span>
          <span><h3>Notes and PDFs</h3><p>Clear study material you can open any time.</p></span>
          <span class="go">→</span>
        </a>
        <a class="row" href="https://devel-novelty-cayman-clearance.trycloudflare.com/" target="_blank" rel="noopener">
          <span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 11l3 3 8-8"/><path d="M20 12v7a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h9"/></svg></span>
          <span><h3>Practice and tests</h3><p>Check what you learned and keep improving.</p></span>
          <span class="go">→</span>
        </a>
        <a class="row" href="https://t.me/SeongEraStudy" target="_blank" rel="noopener">
          <span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a8 8 0 0 1-11.5 7.2L4 20l1-4.6A8 8 0 1 1 21 12z"/></svg></span>
          <span><h3>Community on Telegram</h3><p>Get updates and ask your doubts in the channel.</p></span>
          <span class="go">→</span>
        </a>
      </div>
    </div>
  </section>

  <section class="shloka">
    <div class="wrap">
      <p class="deva">न हि ज्ञानेन सदृशं पवित्रमिह विद्यते</p>
      <p class="mean">In this world, nothing purifies like knowledge.</p>
      <small>Bhagavad Gita 4.38</small>
    </div>
  </section>

  <section id="promise">
    <div class="wrap">
      <h2>Our promise to every student.</h2>
      <div class="promise">
        <div><b>Free, always</b><span>Learning should never depend on what you can pay.</span></div>
        <div><b>Open to all</b><span>Every student is welcome, from any city or background.</span></div>
        <div><b>Made with care</b><span>Built to be simple, fast and easy on any device.</span></div>
      </div>
    </div>
  </section>

  <section id="join" class="join">
    <div class="wrap">
      <h2>Your next class starts here.</h2>
      <p class="sub">Open the portal to begin, and follow the Telegram channel for every new update.</p>
      <div class="cta-row">
        <a class="btn gold" href="https://devel-novelty-cayman-clearance.trycloudflare.com/" target="_blank" rel="noopener">Open the portal</a>
        <a class="btn ghost" href="https://t.me/SeongEraStudy" target="_blank" rel="noopener">@SeongEraStudy</a>
      </div>
      <p class="owner">Questions? Message the owner <a href="https://t.me/SeongEra" target="_blank" rel="noopener">@SeongEra</a> on Telegram.</p>
    </div>
  </section>
</main>

<footer>
  <strong>SeongEraStudy</strong><br>
  Made by Seong Gium Jee · © <span id="yr"></span>
</footer>

<button class="sound" id="sound" type="button" aria-pressed="false" aria-label="Turn music on">
  <span class="eq" aria-hidden="true"><i></i><i></i><i></i><i></i></span>
  <span id="soundLabel">Music off</span>
</button>

<script>
(function(){
  var v=document.getElementById('bg'),
      b=document.getElementById('sound'),
      l=document.getElementById('soundLabel');

  v.addEventListener('canplay',function(){v.classList.add('ready')});
  v.addEventListener('loadeddata',function(){v.classList.add('ready')});
  var p=v.play(); if(p&&p.catch)p.catch(function(){});

  b.addEventListener('click',function(){
    var turnOn=v.muted;
    v.muted=!turnOn;
    if(turnOn){v.volume=.8;var q=v.play();if(q&&q.catch)q.catch(function(){})}
    b.setAttribute('aria-pressed',turnOn);
    b.setAttribute('aria-label',turnOn?'Turn music off':'Turn music on');
    l.textContent=turnOn?'Music on':'Music off';
  });

  document.getElementById('yr').textContent=new Date().getFullYear();
})();
</script>
</body>
</html>
"""


@app.route("/")
def home():
    return Response(HTML, mimetype="text/html")


@app.route("/<path:_>")
def fallback(_):
    return Response(HTML, mimetype="text/html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
