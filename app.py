# =====================================================
#  CONFIG  -  change links ONLY here, nowhere else
# =====================================================
PORTAL_LINK  = "http://seongxcollege.duckdns.org"
BACKUP_LINK  = "https://teaching-responded-pond-payday.trycloudflare.com"
VIDEO_URL    = "https://huggingface.co/datasets/gopallikehack/Seong_Study/resolve/main/a-261025-y6jc8x.mp4"
CHANNEL_LINK = "https://t.me/SeongEraStudy"
OWNER_LINK   = "https://t.me/SeongEra"
# =====================================================
#  How the portal buttons work:
#  Every "Open Portal" button goes to /go. The server checks
#  PORTAL_LINK first. If it gives an error (404, 500, timeout,
#  down) the visitor is sent to BACKUP_LINK automatically.
# =====================================================

import time
import urllib.request

from flask import Flask, Response, jsonify, redirect

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
  --mut:rgba(251,246,255,.74);
  --a1:#ffa23d;
  --a2:#ff3f86;
  --a3:#7a5cff;
  --ok:#3ddc97;
  --grad:linear-gradient(120deg,var(--a1),var(--a2) 55%,var(--a3));
  --glass:rgba(16,10,26,.58);
  --edge:rgba(255,255,255,.15);
  --head:"Sora",system-ui,sans-serif;
  --body:"DM Sans",system-ui,sans-serif;
  --kr:"Noto Sans KR",sans-serif;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;scroll-padding-top:90px}
body{background:var(--bg);color:var(--ink);font-family:var(--body);line-height:1.6;-webkit-font-smoothing:antialiased;overflow-x:hidden}
body.open{overflow:hidden}
a{color:inherit;text-decoration:none}
:focus-visible{outline:2px solid var(--a1);outline-offset:3px;border-radius:8px}
::selection{background:var(--a2);color:#fff}

/* ---------- Loader ---------- */
#loader{display:none}
.js #loader{position:fixed;inset:0;z-index:200;display:grid;place-items:center;align-content:center;gap:22px;background:var(--bg);transition:opacity .6s ease,visibility .6s}
#loader.done{opacity:0;visibility:hidden}
#loader b{font-family:var(--head);font-weight:800;font-size:1.3rem;letter-spacing:-.01em}
#loader b i{font-style:normal;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.ring{width:54px;height:54px;border-radius:50%;border:3px solid rgba(255,255,255,.1);border-top-color:var(--a2);border-right-color:var(--a1);animation:rot .9s linear infinite}
@keyframes rot{to{transform:rotate(360deg)}}

/* ---------- Backdrop (one video + tiny canvas that fills the page) ---------- */
.bg{position:fixed;inset:0;z-index:-3;background:radial-gradient(90% 70% at 80% 10%,#3a1450 0%,var(--bg) 70%);overflow:hidden}
.bg canvas{position:absolute;inset:0;width:100%;height:100%;z-index:1;opacity:.7}
.bg video{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;z-index:2;transform:translateZ(0);will-change:transform;backface-visibility:hidden}
.shade{position:fixed;inset:0;z-index:-2;pointer-events:none;
  background:
    radial-gradient(70% 60% at 50% 40%,rgba(7,5,11,.2),rgba(7,5,11,.72) 100%),
    linear-gradient(180deg,rgba(7,5,11,.5),rgba(7,5,11,.15) 35%,rgba(7,5,11,.92) 100%)}
.glow{position:fixed;left:0;top:0;width:520px;height:520px;margin:-260px 0 0 -260px;z-index:-1;pointer-events:none;border-radius:50%;
  background:radial-gradient(circle,rgba(255,63,134,.16),rgba(122,92,255,.08) 45%,transparent 70%);opacity:0;transition:opacity .4s;will-change:transform}
.prog{position:fixed;top:0;left:0;height:3px;width:0;z-index:150;background:var(--grad);box-shadow:0 0 14px rgba(255,63,134,.7)}

/* ---------- Nav ---------- */
.nav{position:fixed;top:16px;left:50%;transform:translateX(-50%);z-index:60;width:min(980px,calc(100% - 28px));
  display:flex;align-items:center;justify-content:space-between;gap:14px;padding:10px 10px 10px 22px;border-radius:999px;
  background:rgba(14,9,22,.78);border:1px solid var(--edge)}
.logo{font-family:var(--head);font-weight:800;font-size:1.05rem;letter-spacing:-.01em}
.logo b{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.links{display:flex;gap:24px;font-size:.9rem;font-weight:500;color:var(--mut)}
.links a{position:relative;padding:4px 0;transition:color .2s}
.links a::after{content:"";position:absolute;left:0;bottom:-2px;height:2px;width:0;background:var(--grad);transition:width .25s}
.links a:hover,.links a.active{color:var(--ink)}
.links a:hover::after,.links a.active::after{width:100%}
.nr{display:flex;align-items:center;gap:10px}
.burger{display:none;width:44px;height:44px;border-radius:50%;border:1px solid var(--edge);background:var(--glass);cursor:pointer;place-items:center;position:relative}
.burger span{position:absolute;left:13px;right:13px;height:2px;border-radius:2px;background:var(--ink);transition:transform .3s,top .3s,opacity .3s}
.burger span:nth-child(1){top:16px}
.burger span:nth-child(2){top:21px}
.burger span:nth-child(3){top:26px}
body.open .burger span:nth-child(1){top:21px;transform:rotate(45deg)}
body.open .burger span:nth-child(2){opacity:0}
body.open .burger span:nth-child(3){top:21px;transform:rotate(-45deg)}
@media(max-width:820px){.links{display:none}.burger{display:grid}}
.drawer{position:fixed;inset:0;z-index:55;background:rgba(7,5,11,.96);display:flex;flex-direction:column;justify-content:center;gap:6px;padding:90px 9vw 40px;transform:translateY(-102%);transition:transform .5s cubic-bezier(.7,0,.2,1)}
body.open .drawer{transform:none}
.drawer a{font-family:var(--head);font-weight:800;font-size:clamp(2rem,9vw,3rem);letter-spacing:-.03em;padding:6px 0;border-bottom:1px solid var(--edge);transition:padding-left .25s,color .25s}
.drawer a:hover{padding-left:12px;color:var(--a1)}
.drawer small{margin-top:18px;color:var(--mut)}

.pill{position:relative;overflow:hidden;display:inline-flex;align-items:center;gap:8px;padding:11px 22px;border-radius:999px;font-weight:700;font-size:.9rem;background:var(--grad);color:#1a0a10;transition:transform .2s,box-shadow .2s;font-family:var(--body);border:0;cursor:pointer}
.pill::after{content:"";position:absolute;top:0;left:-60%;width:40%;height:100%;background:linear-gradient(100deg,transparent,rgba(255,255,255,.55),transparent);transform:skewX(-20deg);animation:shine 3.6s ease-in-out infinite}
@keyframes shine{0%,55%{left:-60%}100%{left:130%}}
.pill:hover{transform:translateY(-2px);box-shadow:0 14px 34px -8px rgba(255,63,134,.75)}
.pill.big{padding:17px 34px;font-size:1rem}
.ghost{display:inline-flex;align-items:center;gap:10px;padding:16px 30px;border-radius:999px;border:1px solid var(--edge);background:var(--glass);font-weight:600;transition:background .2s,border-color .2s,transform .2s}
.ghost:hover{background:rgba(255,255,255,.14);border-color:rgba(255,255,255,.34);transform:translateY(-2px)}
.pill svg,.ghost svg{width:18px;height:18px}

/* ---------- Hero ---------- */
.hero{min-height:100svh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:130px 22px 110px}
.badge{position:relative;display:inline-flex;align-items:center;gap:10px;padding:9px 20px;border-radius:999px;background:rgba(14,9,22,.7);font-size:.85rem;font-weight:600;color:var(--mut);isolation:isolate}
.badge::before{content:"";position:absolute;inset:0;border-radius:inherit;padding:1.5px;background:conic-gradient(from var(--ang,0deg),var(--a1),var(--a2),var(--a3),var(--a1));-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;animation:spin 5s linear infinite;z-index:-1}
@property --ang{syntax:"<angle>";initial-value:0deg;inherits:false}
@keyframes spin{to{--ang:360deg}}
.badge i{width:8px;height:8px;border-radius:50%;background:var(--ok);box-shadow:0 0 0 4px rgba(61,220,151,.2);animation:pulse 2s infinite}
@keyframes pulse{50%{box-shadow:0 0 0 8px rgba(61,220,151,0)}}
.hero h1{margin-top:26px;font-family:var(--head);font-weight:800;font-size:clamp(2.8rem,8.6vw,7rem);line-height:1;letter-spacing:-.04em;max-width:14ch;text-shadow:0 6px 40px rgba(0,0,0,.55)}
.hero h1 em{font-style:normal;background:linear-gradient(120deg,var(--a1),var(--a2),var(--a3),var(--a1));background-size:250% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:flow 6s linear infinite;text-shadow:none}
@keyframes flow{to{background-position:250% 0}}
.hero p{margin-top:24px;max-width:50ch;font-size:clamp(1rem,1.7vw,1.2rem);color:var(--mut);text-shadow:0 2px 20px rgba(0,0,0,.7)}
.rot{display:inline-block;min-width:5.4em;font-weight:700;color:var(--ink);border-bottom:2px solid var(--a2);transition:opacity .3s,transform .3s}
.rot.out{opacity:0;transform:translateY(6px)}
.row{display:flex;flex-wrap:wrap;justify-content:center;gap:14px;margin-top:36px}
.status{margin-top:26px;display:inline-flex;align-items:center;gap:10px;padding:8px 16px;border-radius:999px;background:rgba(14,9,22,.7);border:1px solid var(--edge);font-size:.82rem;font-weight:600;color:var(--mut)}
.status i{width:8px;height:8px;border-radius:50%;background:#888}
.status.ok i{background:var(--ok);box-shadow:0 0 0 4px rgba(61,220,151,.2)}
.status.bk i{background:var(--a1);box-shadow:0 0 0 4px rgba(255,162,61,.2)}
.tri{margin-top:34px;display:flex;flex-wrap:wrap;justify-content:center;gap:10px 34px;font-family:var(--head);font-weight:600;font-size:.95rem;color:var(--mut)}
.tri span::before{content:"";display:inline-block;width:7px;height:7px;margin-right:10px;border-radius:50%;background:var(--grad)}
.hero > *{opacity:0;transform:translateY(20px);animation:up .9s cubic-bezier(.2,.7,.2,1) forwards}
.hero > *:nth-child(1){animation-delay:.1s}
.hero > *:nth-child(2){animation-delay:.25s}
.hero > *:nth-child(3){animation-delay:.45s}
.hero > *:nth-child(4){animation-delay:.65s}
.hero > *:nth-child(5){animation-delay:.8s}
.hero > *:nth-child(6){animation-delay:.95s}
@keyframes up{to{opacity:1;transform:none}}
.scroll{position:absolute;bottom:84px;left:50%;margin-left:-13px;width:26px;height:42px;border:2px solid var(--edge);border-radius:14px}
.scroll::after{content:"";position:absolute;left:50%;top:8px;width:4px;height:8px;margin-left:-2px;border-radius:2px;background:var(--ink);animation:wheel 1.8s infinite}
@keyframes wheel{0%{opacity:1;transform:none}80%,100%{opacity:0;transform:translateY(14px)}}
@media(max-height:700px){.scroll{display:none}}

/* ---------- Ticker ---------- */
.ticker{overflow:hidden;white-space:nowrap;border-block:1px solid var(--edge);background:rgba(7,5,11,.72)}
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
.card{position:relative;display:flex;flex-direction:column;justify-content:space-between;gap:30px;padding:30px;border-radius:28px;background:var(--glass);border:1px solid var(--edge);overflow:hidden;transform-style:preserve-3d;transition:border-color .3s,opacity .7s ease,transform .15s ease-out}
.card::before{content:"";position:absolute;inset:auto -20% -60% auto;width:260px;height:260px;border-radius:50%;background:var(--grad);opacity:0;filter:blur(70px);transition:opacity .4s}
.card::after{content:"";position:absolute;inset:0;pointer-events:none;opacity:0;transition:opacity .3s;background:radial-gradient(380px circle at var(--x,50%) var(--y,0%),rgba(255,255,255,.13),transparent 60%)}
.card:hover{border-color:rgba(255,255,255,.34)}
.card:hover::before{opacity:.4}
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
.step{padding:34px 28px 10px 0}
.step b{font-family:var(--head);font-size:3.6rem;font-weight:800;line-height:1;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.step h3{margin-top:14px;font-family:var(--head);font-size:1.3rem;font-weight:700}
.step p{margin-top:6px;color:var(--mut);font-size:.96rem}

/* Character */
.hero2{display:grid;grid-template-columns:1fr 1.1fr;gap:34px;align-items:center}
@media(max-width:820px){.hero2{grid-template-columns:1fr}}
.kr{position:relative;display:grid;place-items:center;min-height:300px;border-radius:34px;border:1px solid var(--edge);background:linear-gradient(135deg,rgba(255,162,61,.16),rgba(255,63,134,.12) 45%,rgba(122,92,255,.2));overflow:hidden}
.kr strong{font-family:var(--kr);font-weight:800;font-size:clamp(3rem,9vw,6rem);line-height:1.05;text-align:center;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.kr em{position:absolute;left:22px;bottom:16px;font-style:normal;font-size:.75rem;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--mut)}
.nm{margin-top:12px;font-family:var(--head);font-weight:800;font-size:clamp(2.2rem,5vw,3.8rem);line-height:1.05;letter-spacing:-.03em}
.nm span{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.hero2 p{margin-top:16px;color:var(--mut);max-width:46ch}

/* Quote */
.quote{text-align:center}
.quote blockquote{font-family:var(--head);font-weight:800;font-size:clamp(2rem,6vw,4.6rem);line-height:1.05;letter-spacing:-.035em;max-width:16ch;margin:0 auto}
.quote blockquote em{font-style:normal;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}

/* FAQ */
.faq{margin-top:44px;max-width:820px}
.faq details{border-bottom:1px solid var(--edge);padding:6px 0}
.faq summary{list-style:none;display:flex;align-items:center;justify-content:space-between;gap:16px;cursor:pointer;padding:18px 0;font-family:var(--head);font-weight:700;font-size:1.1rem}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";display:grid;place-items:center;flex:none;width:34px;height:34px;border-radius:50%;border:1px solid var(--edge);font-size:1.3rem;font-weight:400;transition:transform .3s,background .3s}
.faq details[open] summary::after{transform:rotate(45deg);background:var(--grad);color:#1a0a10;border-color:transparent}
.faq p{padding:0 0 20px;color:var(--mut);max-width:60ch}

/* Owner */
.owner{display:grid;grid-template-columns:1.1fr 1fr;gap:34px;align-items:center;padding:clamp(28px,5vw,56px);border-radius:34px;background:linear-gradient(135deg,rgba(255,162,61,.18),rgba(255,63,134,.14) 45%,rgba(122,92,255,.2));border:1px solid var(--edge)}
@media(max-width:800px){.owner{grid-template-columns:1fr}}
.owner h2{font-size:clamp(1.7rem,3.8vw,2.7rem);max-width:none;line-height:1.2;letter-spacing:-.01em;word-break:break-word}
.owner .role{margin-top:14px;color:var(--mut)}
.links2{display:flex;flex-direction:column;gap:12px}
.lnk{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:18px 22px;border-radius:20px;background:rgba(7,5,11,.62);border:1px solid var(--edge);transition:border-color .2s,transform .2s}
.lnk:hover{border-color:var(--a1);transform:translateX(4px)}
.lnk small{display:block;color:var(--mut);font-size:.78rem;letter-spacing:.08em;text-transform:uppercase}
.lnk strong{font-family:var(--head);font-size:1.1rem}

footer{padding:34px 22px 120px;text-align:center;color:var(--mut);font-size:.9rem;border-top:1px solid var(--edge);background:rgba(7,5,11,.88)}
footer strong{color:var(--ink);font-family:var(--head)}
footer small{display:block;margin-top:6px;opacity:.6;font-size:.78rem}

/* ---------- Sound ---------- */
.sound{position:fixed;left:50%;bottom:20px;transform:translateX(-50%);z-index:50;display:flex;align-items:center;gap:12px;padding:12px 22px 12px 16px;border-radius:999px;
  background:rgba(14,9,22,.82);border:1px solid var(--edge);color:var(--ink);font:600 .88rem var(--body);cursor:pointer;transition:border-color .2s,transform .2s,background .2s}
.sound:hover{border-color:rgba(255,255,255,.36);transform:translateX(-50%) translateY(-2px)}
.sound[aria-pressed="true"]{border-color:var(--a2);background:rgba(255,63,134,.24)}
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

<div id="loader"><div class="ring"></div><b>Seong<i>Era</i>Study</b></div>
<div class="prog" id="prog"></div>

<div class="bg">
  <canvas id="fill" width="96" height="54" aria-hidden="true"></canvas>
  <video id="bgf" autoplay muted loop playsinline preload="auto" disablepictureinpicture src="{{VIDEO}}"></video>
</div>
<div class="shade"></div>
<div class="glow" id="glow"></div>

<nav class="nav">
  <a class="logo" href="#top">Seong<b>Era</b>Study</a>
  <div class="links" id="links">
    <a href="#learn">Learn</a>
    <a href="#how">How it works</a>
    <a href="#hero">The Hero</a>
    <a href="#faq">FAQ</a>
    <a href="#owner">Owner</a>
  </div>
  <div class="nr">
    <a class="pill" href="{{PORTAL}}" target="_blank" rel="noopener">Open Portal</a>
    <button class="burger" id="burger" type="button" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
</nav>

<div class="drawer" id="drawer">
  <a href="#learn">Learn</a>
  <a href="#how">How it works</a>
  <a href="#hero">The Hero</a>
  <a href="#faq">FAQ</a>
  <a href="#owner">Owner</a>
  <small>Education is free for everyone.</small>
</div>

<main id="top">
  <div class="hero">
    <div class="badge"><i></i> Free study portal · 약한영웅</div>
    <h1>Education is <em>free</em> for everyone.</h1>
    <p>Watch, read and practice <span class="rot" id="rot">anywhere</span>, all in one simple portal. Open it and start learning today.</p>
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
    <div class="status" id="status"><i></i><span>Checking portal…</span></div>
    <div class="tri"><span>Free for all</span><span>Simple to use</span><span>Made for students</span></div>
    <div class="scroll" aria-hidden="true"></div>
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
        <details class="rv"><summary>The portal shows an error. What now?</summary><p>No problem. If the main server has an error, the Open Portal buttons switch to our backup server by themselves. If a problem stays, message @SeongEra on Telegram.</p></details>
        <details class="rv"><summary>How do I get updates?</summary><p>Join the Telegram channel @SeongEraStudy. Every new update is posted there.</p></details>
        <details class="rv"><summary>Who do I contact for help?</summary><p>Message the owner @SeongEra on Telegram.</p></details>
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
  var $=function(id){return document.getElementById(id)};
  var v=$('bgf'), cv=$('fill'), cx=cv.getContext('2d'),
      b=$('snd'), l=$('sndl'), timer=null;

  function safe(p){ if(p&&p.catch)p.catch(function(){}); }

  /* tiny canvas copy of the video: stretches to fill the whole page, very cheap */
  function paint(){ try{ cx.drawImage(v,0,0,cv.width,cv.height); }catch(e){} }
  function startFill(){ if(!timer){ timer=setInterval(paint,110); } }
  function stopFill(){ clearInterval(timer); timer=null; }

  function play(){ safe(v.play()); startFill(); }
  function stop(){ v.pause(); stopFill(); }

  try{ v.currentTime=0; }catch(e){}
  play();
  v.addEventListener('loadeddata',paint);

  /* leave the tab = stop video + music, come back = continue */
  document.addEventListener('visibilitychange',function(){ if(document.hidden){ stop(); } else { play(); } });
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

  /* loader */
  var ld=$('loader');
  function hideLoader(){ if(ld){ ld.classList.add('done'); setTimeout(function(){ ld.remove(); ld=null; },700); } }
  window.addEventListener('load',function(){ setTimeout(hideLoader,250); });
  setTimeout(hideLoader,2200);

  /* mobile menu */
  var burger=$('burger'), drawer=$('drawer');
  function toggle(open){
    document.body.classList.toggle('open',open);
    burger.setAttribute('aria-expanded',open);
  }
  burger.addEventListener('click',function(){ toggle(!document.body.classList.contains('open')); });
  drawer.querySelectorAll('a').forEach(function(a){ a.addEventListener('click',function(){ toggle(false); }); });
  document.addEventListener('keydown',function(e){ if(e.key==='Escape'){ toggle(false); } });

  /* rotating word */
  var words=['anywhere','anytime','on any device','at your pace','for free'], wi=0, rot=$('rot');
  setInterval(function(){
    rot.classList.add('out');
    setTimeout(function(){ wi=(wi+1)%words.length; rot.textContent=words[wi]; rot.classList.remove('out'); },320);
  },2400);

  /* scroll reveal */
  var items=document.querySelectorAll('.rv');
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){
      es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
    },{threshold:.12});
    items.forEach(function(el,i){ el.style.transitionDelay=((i%4)*70)+'ms'; io.observe(el); });
  } else { items.forEach(function(el){ el.classList.add('in'); }); }

  /* active menu link while scrolling */
  var links=document.querySelectorAll('#links a'), map={};
  links.forEach(function(a){ map[a.getAttribute('href').slice(1)]=a; });
  if('IntersectionObserver' in window){
    var so=new IntersectionObserver(function(es){
      es.forEach(function(e){
        if(e.isIntersecting && map[e.target.id]){
          links.forEach(function(a){ a.classList.remove('active'); });
          map[e.target.id].classList.add('active');
        }
      });
    },{rootMargin:'-45% 0px -50% 0px'});
    Object.keys(map).forEach(function(id){ var s=$(id); if(s){ so.observe(s); } });
  }

  /* desktop only: card spotlight + tilt, cursor glow */
  if(window.matchMedia('(hover:hover) and (pointer:fine)').matches){
    document.querySelectorAll('.card').forEach(function(c){
      c.addEventListener('pointermove',function(e){
        var r=c.getBoundingClientRect(), x=e.clientX-r.left, y=e.clientY-r.top;
        c.style.setProperty('--x',x+'px'); c.style.setProperty('--y',y+'px');
        var rx=((y/r.height)-.5)*-6, ry=((x/r.width)-.5)*6;
        c.style.transform='perspective(900px) rotateX('+rx+'deg) rotateY('+ry+'deg) translateY(-4px)';
      });
      c.addEventListener('pointerleave',function(){ c.style.transform=''; });
    });
    var g=$('glow');
    window.addEventListener('pointermove',function(e){
      g.style.opacity=1; g.style.transform='translate('+e.clientX+'px,'+e.clientY+'px)';
    },{passive:true});
  }

  /* scroll progress */
  var bar=$('prog');
  function onScroll(){
    var h=document.documentElement.scrollHeight-window.innerHeight;
    bar.style.width=(h>0?(window.scrollY/h)*100:0)+'%';
  }
  window.addEventListener('scroll',onScroll,{passive:true}); onScroll();

  /* portal status (server checks main link, switches to backup on 404/500) */
  var st=$('status'), stt=st.querySelector('span');
  function check(){
    fetch('/status',{cache:'no-store'}).then(function(r){return r.json()}).then(function(d){
      st.classList.remove('ok','bk');
      if(d.online){ st.classList.add('ok'); stt.textContent='Portal online'; }
      else { st.classList.add('bk'); stt.textContent='Main server busy · using backup'; }
    }).catch(function(){ stt.textContent='Portal ready'; });
  }
  check(); setInterval(check,60000);

  $('yr').textContent=new Date().getFullYear();
})();
</script>
</body>
</html>
"""

PAGE = (
    HTML.replace("{{PORTAL}}", "/go")
        .replace("{{VIDEO}}", VIDEO_URL)
        .replace("{{CHANNEL}}", CHANNEL_LINK)
        .replace("{{OWNER}}", OWNER_LINK)
)

_cache = {"t": 0.0, "ok": True}


def primary_ok():
    """True if PORTAL_LINK answers with a normal page (status below 400)."""
    now = time.time()
    if now - _cache["t"] < 20:          # re-check at most every 20 seconds
        return _cache["ok"]
    ok = False
    try:
        req = urllib.request.Request(
            PORTAL_LINK,
            headers={"User-Agent": "Mozilla/5.0 (SeongEraStudy link check)"},
        )
        with urllib.request.urlopen(req, timeout=3) as r:
            ok = r.status < 400
    except Exception:                    # 404, 500, timeout, DNS error...
        ok = False
    _cache["t"], _cache["ok"] = now, ok
    return ok


def no_store(resp):
    resp.headers["Cache-Control"] = "no-store"
    return resp


@app.route("/go")
def go():
    return no_store(redirect(PORTAL_LINK if primary_ok() else BACKUP_LINK, code=302))


@app.route("/status")
def status():
    ok = primary_ok()
    return no_store(jsonify(online=ok, using="primary" if ok else "backup"))


@app.route("/")
def home():
    return Response(PAGE, mimetype="text/html; charset=utf-8")


@app.route("/<path:_>")
def fallback(_):
    return Response(PAGE, mimetype="text/html; charset=utf-8")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
