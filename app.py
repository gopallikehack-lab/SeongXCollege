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
<meta name="theme-color" content="#07050b">
<meta property="og:title" content="SeongEraStudy">
<meta property="og:description" content="Education is free for everyone.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=DM+Sans:wght@400;500;600;700&family=Noto+Sans+KR:wght@800&display=swap" rel="stylesheet">
<script>document.documentElement.classList.add('js')</script>
<style>
:root{
  --bg:#07050b;
  --ink:#fbf6ff;
  --mut:rgba(251,246,255,.72);
  --a1:#ffa23d;
  --a2:#ff3f86;
  --a3:#7a5cff;
  --grad:linear-gradient(120deg,var(--a1),var(--a2) 55%,var(--a3));
  --glass:rgba(255,255,255,.07);
  --edge:rgba(255,255,255,.15);
  --head:"Sora",system-ui,sans-serif;
  --body:"DM Sans",system-ui,sans-serif;
  --kr:"Noto Sans KR",sans-serif;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--ink);font-family:var(--body);line-height:1.6;-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:inherit;text-decoration:none}
:focus-visible{outline:2px solid var(--a1);outline-offset:3px;border-radius:8px}
::selection{background:var(--a2);color:#fff}

/* ---------- Backdrop ---------- */
.bg{position:fixed;inset:0;z-index:-3;background:radial-gradient(90% 70% at 80% 10%,#3a1450 0%,var(--bg) 70%)}
.bg video{position:absolute;inset:0;width:100%;height:100%}
.bg #bgb{object-fit:cover;filter:blur(34px) brightness(.55) saturate(1.2);transform:scale(1.18);z-index:1}
.bg #bgf{object-fit:contain;z-index:2}
.shade{position:fixed;inset:0;z-index:-2;pointer-events:none;
  background:
    radial-gradient(70% 60% at 50% 40%,rgba(7,5,11,.2),rgba(7,5,11,.72) 100%),
    linear-gradient(180deg,rgba(7,5,11,.5),rgba(7,5,11,.15) 35%,rgba(7,5,11,.92) 100%)}
.orb{position:fixed;z-index:-1;pointer-events:none;border-radius:50%;filter:blur(90px);opacity:.32;mix-blend-mode:screen}
.o1{width:46vmax;height:46vmax;left:-14vmax;top:-10vmax;background:var(--a2);animation:d1 22s ease-in-out infinite alternate}
.o2{width:40vmax;height:40vmax;right:-12vmax;top:30vh;background:var(--a3);animation:d2 26s ease-in-out infinite alternate}
.o3{width:34vmax;height:34vmax;left:25vw;bottom:-16vmax;background:var(--a1);opacity:.2;animation:d1 30s ease-in-out infinite alternate-reverse}
@keyframes d1{to{transform:translate(8vmax,6vmax) scale(1.15)}}
@keyframes d2{to{transform:translate(-9vmax,-5vmax) scale(.9)}}
.prog{position:fixed;top:0;left:0;height:3px;width:0;z-index:60;background:var(--grad);box-shadow:0 0 14px rgba(255,63,134,.7)}

/* ---------- Nav ---------- */
.nav{position:fixed;top:16px;left:50%;transform:translateX(-50%);z-index:40;width:min(960px,calc(100% - 28px));
  display:flex;align-items:center;justify-content:space-between;gap:14px;padding:10px 10px 10px 22px;border-radius:999px;
  background:rgba(14,9,22,.62);border:1px solid var(--edge);backdrop-filter:blur(18px)}
.logo{font-family:var(--head);font-weight:800;font-size:1.05rem;letter-spacing:-.01em}
.logo b{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.links{display:flex;gap:26px;font-size:.9rem;font-weight:500;color:var(--mut)}
.links a{position:relative;padding:4px 0}
.links a::after{content:"";position:absolute;left:0;bottom:-2px;height:2px;width:0;background:var(--grad);transition:width .25s}
.links a:hover{color:var(--ink)}
.links a:hover::after{width:100%}
@media(max-width:720px){.links{display:none}}

.pill{position:relative;overflow:hidden;display:inline-flex;align-items:center;gap:8px;padding:11px 22px;border-radius:999px;font-weight:700;font-size:.9rem;background:var(--grad);color:#1a0a10;transition:transform .2s,box-shadow .2s;font-family:var(--body);border:0;cursor:pointer}
.pill::after{content:"";position:absolute;top:0;left:-60%;width:40%;height:100%;background:linear-gradient(100deg,transparent,rgba(255,255,255,.55),transparent);transform:skewX(-20deg);animation:shine 3.6s ease-in-out infinite}
@keyframes shine{0%,55%{left:-60%}100%{left:130%}}
.pill:hover{transform:translateY(-2px);box-shadow:0 14px 34px -8px rgba(255,63,134,.75)}
.pill.big{padding:17px 34px;font-size:1rem}
.ghost{display:inline-flex;align-items:center;gap:10px;padding:16px 30px;border-radius:999px;border:1px solid var(--edge);background:var(--glass);backdrop-filter:blur(12px);font-weight:600;transition:background .2s,border-color .2s,transform .2s}
.ghost:hover{background:rgba(255,255,255,.13);border-color:rgba(255,255,255,.34);transform:translateY(-2px)}
.pill svg,.ghost svg{width:18px;height:18px}

/* ---------- Hero ---------- */
.hero{min-height:100svh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:130px 22px 100px}
.badge{position:relative;display:inline-flex;align-items:center;gap:10px;padding:9px 20px;border-radius:999px;background:rgba(14,9,22,.6);backdrop-filter:blur(10px);font-size:.85rem;font-weight:600;color:var(--mut);isolation:isolate}
.badge::before{content:"";position:absolute;inset:0;border-radius:inherit;padding:1.5px;background:conic-gradient(from var(--ang,0deg),var(--a1),var(--a2),var(--a3),var(--a1));-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;animation:spin 5s linear infinite;z-index:-1}
@property --ang{syntax:"<angle>";initial-value:0deg;inherits:false}
@keyframes spin{to{--ang:360deg}}
.badge i{width:8px;height:8px;border-radius:50%;background:#3ddc97;box-shadow:0 0 0 4px rgba(61,220,151,.2);animation:pulse 2s infinite}
@keyframes pulse{50%{box-shadow:0 0 0 8px rgba(61,220,151,0)}}
.hero h1{margin-top:26px;font-family:var(--head);font-weight:800;font-size:clamp(2.8rem,8.6vw,7rem);line-height:1;letter-spacing:-.04em;max-width:14ch;text-shadow:0 6px 40px rgba(0,0,0,.5)}
.hero h1 em{font-style:normal;background:linear-gradient(120deg,var(--a1),var(--a2),var(--a3),var(--a1));background-size:250% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:flow 6s linear infinite;text-shadow:none}
@keyframes flow{to{background-position:250% 0}}
.hero p{margin-top:24px;max-width:48ch;font-size:clamp(1rem,1.7vw,1.2rem);color:var(--mut);text-shadow:0 2px 20px rgba(0,0,0,.6)}
.row{display:flex;flex-wrap:wrap;justify-content:center;gap:14px;margin-top:36px}
.tri{margin-top:50px;display:flex;flex-wrap:wrap;justify-content:center;gap:10px 34px;font-family:var(--head);font-weight:600;font-size:.95rem;color:var(--mut)}
.tri span::before{content:"";display:inline-block;width:7px;height:7px;margin-right:10px;border-radius:50%;background:var(--grad)}
.hero > *{opacity:0;transform:translateY(20px);animation:up .9s cubic-bezier(.2,.7,.2,1) forwards}
.hero > *:nth-child(1){animation-delay:.1s}
.hero > *:nth-child(2){animation-delay:.25s}
.hero > *:nth-child(3){animation-delay:.45s}
.hero > *:nth-child(4){animation-delay:.65s}
.hero > *:nth-child(5){animation-delay:.85s}
@keyframes up{to{opacity:1;transform:none}}

/* ---------- Ticker ---------- */
.ticker{overflow:hidden;white-space:nowrap;border-block:1px solid var(--edge);background:rgba(7,5,11,.62);backdrop-filter:blur(10px)}
.ticker div{display:inline-flex;animation:scroll 38s linear infinite;padding:20px 0}
.ticker span{font-family:var(--head);font-weight:700;font-size:1.35rem;padding-right:48px;color:rgba(251,246,255,.92)}
.ticker span::after{content:"•";padding-left:48px;color:var(--a2)}
@keyframes scroll{to{transform:translateX(-50%)}}

/* ---------- Sections ---------- */
section{padding:clamp(70px,10vw,130px) 22px}
.wrap{max-width:1120px;margin:0 auto}
.eyebrow{font-weight:700;font-size:.8rem;letter-spacing:.16em;text-transform:uppercase;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent;display:inline-block}
h2{margin-top:12px;font-family:var(--head);font-weight:800;font-size:clamp(2rem,4.8vw,3.6rem);line-height:1.05;letter-spacing:-.03em;max-width:18ch}
.lead{margin-top:16px;color:var(--mut);max-width:52ch}
.js .rv{opacity:0;transform:translateY(26px);transition:opacity .7s ease,transform .7s cubic-bezier(.2,.7,.2,1)}
.js .rv.in{opacity:1;transform:none}

/* Bento */
.bento{display:grid;grid-template-columns:repeat(6,1fr);gap:16px;margin-top:50px}
.card{position:relative;display:flex;flex-direction:column;justify-content:space-between;gap:30px;padding:30px;border-radius:28px;background:var(--glass);border:1px solid var(--edge);backdrop-filter:blur(16px);overflow:hidden;transition:transform .3s,border-color .3s}
.card::before{content:"";position:absolute;inset:auto -20% -60% auto;width:260px;height:260px;border-radius:50%;background:var(--grad);opacity:0;filter:blur(70px);transition:opacity .4s}
.card::after{content:"";position:absolute;inset:0;pointer-events:none;opacity:0;transition:opacity .3s;background:radial-gradient(380px circle at var(--x,50%) var(--y,0%),rgba(255,255,255,.13),transparent 60%)}
.card:hover{transform:translateY(-5px);border-color:rgba(255,255,255,.34)}
.card:hover::before{opacity:.45}
.card:hover::after{opacity:1}
.card .no{font-family:var(--head);font-weight:800;font-size:.95rem;color:var(--a1)}
.card h3{font-family:var(--head);font-weight:700;font-size:1.5rem;letter-spacing:-.02em;margin-bottom:8px}
.card p{color:var(--mut);font-size:.97rem}
.card .arrow{align-self:flex-start;display:grid;place-items:center;width:42px;height:42px;border-radius:50%;border:1px solid var(--edge);transition:background .25s,transform .25s,color .25s}
.card:hover .arrow{background:var(--grad);color:#1a0a10;transform:rotate(-45deg)}
.c1{grid-column:span 3;grid-row:span 2;min-height:340px}
.c1 h3{font-size:2.3rem;line-height:1.08}
.c2,.c3{grid-column:span 3}
.c4{grid-column:span 6;flex-direction:row;align-items:center;flex-wrap:wrap}
@media(max-width:760px){.c1,.c2,.c3,.c4{grid-column:span 6;grid-row:auto;min-height:0}}

/* Steps */
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:0;margin-top:50px;border-top:1px solid var(--edge)}
.step{position:relative;padding:34px 28px 10px 0}
.step b{font-family:var(--head);font-size:3.6rem;font-weight:800;line-height:1;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.step h3{margin-top:14px;font-family:var(--head);font-size:1.3rem;font-weight:700}
.step p{margin-top:6px;color:var(--mut);font-size:.96rem}

/* Character */
.hero2{display:grid;grid-template-columns:1fr 1.1fr;gap:34px;align-items:center}
@media(max-width:820px){.hero2{grid-template-columns:1fr}}
.kr{position:relative;display:grid;place-items:center;min-height:300px;border-radius:34px;border:1px solid var(--edge);background:linear-gradient(135deg,rgba(255,162,61,.14),rgba(255,63,134,.1) 45%,rgba(122,92,255,.18));backdrop-filter:blur(16px);overflow:hidden}
.kr strong{font-family:var(--kr);font-weight:800;font-size:clamp(3rem,9vw,6rem);line-height:1.05;text-align:center;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.kr em{position:absolute;left:22px;bottom:16px;font-style:normal;font-size:.75rem;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--mut)}
.nm{margin-top:12px;font-family:var(--head);font-weight:800;font-size:clamp(2.2rem,5vw,3.8rem);line-height:1.05;letter-spacing:-.03em}
.nm span{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.hero2 p{margin-top:16px;color:var(--mut);max-width:46ch}

/* FAQ */
.faq{margin-top:44px;max-width:820px}
.faq details{border-bottom:1px solid var(--edge);padding:6px 0}
.faq summary{list-style:none;display:flex;align-items:center;justify-content:space-between;gap:16px;cursor:pointer;padding:18px 0;font-family:var(--head);font-weight:700;font-size:1.1rem}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";display:grid;place-items:center;flex:none;width:34px;height:34px;border-radius:50%;border:1px solid var(--edge);font-size:1.3rem;font-weight:400;transition:transform .3s,background .3s}
.faq details[open] summary::after{transform:rotate(45deg);background:var(--grad);color:#1a0a10;border-color:transparent}
.faq p{padding:0 0 20px;color:var(--mut);max-width:60ch}

/* Quote */
.quote{text-align:center}
.quote blockquote{font-family:var(--head);font-weight:800;font-size:clamp(2rem,6vw,4.6rem);line-height:1.05;letter-spacing:-.035em;max-width:16ch;margin:0 auto}
.quote blockquote em{font-style:normal;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}

/* Owner */
.owner{display:grid;grid-template-columns:1.1fr 1fr;gap:34px;align-items:center;padding:clamp(28px,5vw,56px);border-radius:34px;background:linear-gradient(135deg,rgba(255,162,61,.16),rgba(255,63,134,.12) 45%,rgba(122,92,255,.18));border:1px solid var(--edge);backdrop-filter:blur(18px)}
@media(max-width:800px){.owner{grid-template-columns:1fr}}
.owner h2{font-size:clamp(1.7rem,3.8vw,2.7rem);max-width:none;line-height:1.2;letter-spacing:-.01em;word-break:break-word}
.owner .role{margin-top:14px;color:var(--mut)}
.links2{display:flex;flex-direction:column;gap:12px}
.lnk{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:18px 22px;border-radius:20px;background:rgba(7,5,11,.55);border:1px solid var(--edge);transition:border-color .2s,transform .2s}
.lnk:hover{border-color:var(--a1);transform:translateX(4px)}
.lnk small{display:block;color:var(--mut);font-size:.78rem;letter-spacing:.08em;text-transform:uppercase}
.lnk strong{font-family:var(--head);font-size:1.1rem}

footer{padding:34px 22px 120px;text-align:center;color:var(--mut);font-size:.9rem;border-top:1px solid var(--edge);background:rgba(7,5,11,.85)}
footer strong{color:var(--ink);font-family:var(--head)}
footer small{display:block;margin-top:6px;opacity:.6;font-size:.78rem}

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
  .js .rv{opacity:1;transform:none}
  html{scroll-behavior:auto}
}
</style>
</head>
<body>

<div class="prog" id="prog"></div>
<div class="bg">
  <video id="bgb" muted loop playsinline preload="auto" aria-hidden="true" src="{{VIDEO}}"></video>
  <video id="bgf" autoplay muted loop playsinline preload="auto" src="{{VIDEO}}"></video>
</div>
<div class="shade"></div>
<div class="orb o1"></div><div class="orb o2"></div><div class="orb o3"></div>

<nav class="nav">
  <a class="logo" href="#top">Seong<b>Era</b>Study</a>
  <div class="links">
    <a href="#learn">Learn</a>
    <a href="#how">How it works</a>
    <a href="#hero">The Hero</a>
    <a href="#faq">FAQ</a>
    <a href="#owner">Owner</a>
  </div>
  <a class="pill" href="{{PORTAL}}" target="_blank" rel="noopener">Open Portal</a>
</nav>

<main id="top">
  <div class="hero">
    <div class="badge"><i></i> Free study portal · 약한영웅</div>
    <h1>Education is <em>free</em> for everyone.</h1>
    <p>SeongEraStudy brings lectures, notes and practice to every student, in one simple portal. Open it and start learning today.</p>
    <div class="row">
      <a class="pill big" href="{{PORTAL}}" target="_blank" rel="noopener">
        Start learning
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
      </a>
      <a class="ghost" href="{{CHANNEL}}" target="_blank" rel="noopener">
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
      <div class="eyebrow rv">What you get</div>
      <h2 class="rv">One portal. Everything to study.</h2>
      <p class="lead rv">Learn at your own pace from any phone or laptop.</p>
      <div class="bento">
        <a class="card c1 rv" href="{{PORTAL}}" target="_blank" rel="noopener">
          <div><span class="no">01</span><h3 style="margin-top:14px">Video lectures that keep you focused.</h3><p>Watch classes in a clean, smooth player built for learning.</p></div>
          <span class="arrow">→</span>
        </a>
        <a class="card c2 rv" href="{{PORTAL}}" target="_blank" rel="noopener">
          <div><span class="no">02</span><h3 style="margin-top:12px">Notes and PDFs</h3><p>Clear study material, ready whenever you are.</p></div>
          <span class="arrow">→</span>
        </a>
        <a class="card c3 rv" href="{{PORTAL}}" target="_blank" rel="noopener">
          <div><span class="no">03</span><h3 style="margin-top:12px">Practice and tests</h3><p>Check what you learned and keep getting better.</p></div>
          <span class="arrow">→</span>
        </a>
        <a class="card c4 rv" href="{{CHANNEL}}" target="_blank" rel="noopener">
          <div style="flex:1;min-width:240px"><span class="no">04</span><h3 style="margin-top:12px">Join the Telegram community</h3><p>Get every update and ask your doubts in the channel.</p></div>
          <span class="arrow">→</span>
        </a>
      </div>
    </div>
  </section>

  <section id="how">
    <div class="wrap">
      <div class="eyebrow rv">How it works</div>
      <h2 class="rv">Start in three simple steps.</h2>
      <div class="steps">
        <div class="step rv"><b>1</b><h3>Open the portal</h3><p>Tap Open Portal. No complicated setup.</p></div>
        <div class="step rv"><b>2</b><h3>Pick your class</h3><p>Choose the subject or batch you want to study.</p></div>
        <div class="step rv"><b>3</b><h3>Learn every day</h3><p>Watch, read, practice, and follow the channel for updates.</p></div>
      </div>
    </div>
  </section>

  <section id="hero">
    <div class="wrap hero2">
      <div class="kr rv"><strong>약한<br>영웅</strong><em>Weak Hero</em></div>
      <div class="rv">
        <div class="eyebrow">The hero of our portal</div>
        <div class="nm">Seong <span>Jee</span> Gium</div>
        <p>A character from Weak Hero. Not the loudest in the room, but never someone to underestimate. Learn like him: stay calm, stay sharp, keep growing.</p>
      </div>
    </div>
  </section>

  <section class="quote">
    <div class="wrap">
      <blockquote class="rv">Knowledge should never have a <em>price tag.</em></blockquote>
    </div>
  </section>

  <section id="faq">
    <div class="wrap">
      <div class="eyebrow rv">Questions</div>
      <h2 class="rv">Quick answers.</h2>
      <div class="faq">
        <details class="rv"><summary>Is it really free?</summary><p>Yes. Our promise is simple: education is free for everyone.</p></details>
        <details class="rv"><summary>Which devices can I use?</summary><p>Any phone, tablet or laptop with a browser.</p></details>
        <details class="rv"><summary>How do I get updates?</summary><p>Join the Telegram channel @SeongEraStudy. Every new update is posted there.</p></details>
        <details class="rv"><summary>I have a doubt or a problem. Who do I contact?</summary><p>Message the owner @SeongEra on Telegram.</p></details>
      </div>
    </div>
  </section>

  <section id="owner">
    <div class="wrap">
      <div class="owner rv">
        <div>
          <div class="eyebrow">Owner</div>
          <h2>夔🌑 𝑺𝒆𝒐𝒏𝒈-𝒋𝒆 ⋆ 𝑂𝑓𝑓𝑙𝑖𝑛𝑒</h2>
          <p class="role">Founder of SeongEraStudy. Made by Seong Gium Jee.</p>
        </div>
        <div class="links2">
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
  <small>Weak Hero fan-inspired. Not affiliated with the original creators.</small>
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

  /* scroll reveal */
  var items=document.querySelectorAll('.rv');
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){
      es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
    },{threshold:.12});
    items.forEach(function(el,i){ el.style.transitionDelay=((i%4)*70)+'ms'; io.observe(el); });
  } else {
    items.forEach(function(el){ el.classList.add('in'); });
  }

  /* card spotlight follows the pointer */
  document.querySelectorAll('.card').forEach(function(c){
    c.addEventListener('pointermove',function(e){
      var r=c.getBoundingClientRect();
      c.style.setProperty('--x',(e.clientX-r.left)+'px');
      c.style.setProperty('--y',(e.clientY-r.top)+'px');
    });
  });

  /* scroll progress bar */
  var bar=document.getElementById('prog');
  function onScroll(){
    var h=document.documentElement.scrollHeight-window.innerHeight;
    bar.style.width=(h>0?(window.scrollY/h)*100:0)+'%';
  }
  window.addEventListener('scroll',onScroll,{passive:true}); onScroll();

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
