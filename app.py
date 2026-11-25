# =====================================================
#  CONFIG  -  change links / media ONLY here, nowhere else
# =====================================================
PORTAL_LINK     = "http://seongxcollege.duckdns.org"
CHANNEL_LINK    = "https://t.me/SeongEraStudy"
OWNER_LINK      = "https://t.me/SeongEra"
OWNER_NAME      = "夔🌑 𝑺𝒆𝒐𝒏𝒈-𝒋𝒆 ⋆ 𝑂𝑓𝑓𝑙𝑖𝑛𝑒"

VIDEO_URL       = "https://huggingface.co/datasets/gopallikehack/Seong_Study/resolve/main/n-261124-kcctgu.mp4"
OWNER_VIDEO_URL = "https://huggingface.co/datasets/gopallikehack/Seong_Study/resolve/main/a-261025-y6jc8x.mp4"

LOGO_URL        = "https://i.ibb.co/XxtXNBCW/file-00000000649482079925d320aeb3e88b.png"
TREE_URL        = "https://i.ibb.co/nsrmkCn9/file-0000000077c48207807f7e09f0f8d150.png"
GIFTS_URL       = "https://i.ibb.co/Z0LjjGw/file-00000000cfe0820799c102c961ea1c5b.png"
SNOWMAN_URL     = "https://i.ibb.co/20kfKnLj/file-00000000755882079d6cb681905d59cb.png"
HAT_URL         = "https://i.ibb.co/gMfnHdn4/Note-GPT-Image-20261125084956.png"
SANTA_URL       = "https://i.ibb.co/206Z4PZK/1795566285922.png"
SNOWBG_URL      = "https://i.ibb.co/4gJQNThb/download.jpg"

# Leave empty to auto-detect your domain. Change the number to force
# WhatsApp / Telegram to refresh the link preview picture.
SITE_URL        = ""
ASSET_VERSION   = "1"
# =====================================================

import io
import urllib.request

from flask import Flask, Response, redirect, request

try:
    from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont
except Exception:          # Pillow missing: site still works, images load from original links
    Image = None

app = Flask(__name__)

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SeongEraStudy · Merry Christmas &amp; Happy New Year 2027</title>
<meta name="description" content="SeongEraStudy is a free study portal for every student. Education is free for everyone. Merry Christmas and Happy New Year 2027! Made by Seong Gium Jee.">
<meta name="theme-color" content="#050b1c">
<meta property="og:title" content="SeongEraStudy · Education is free for everyone">
<meta property="og:description" content="Merry Christmas and Happy New Year 2027 from SeongEraStudy.">
<meta property="og:type" content="website">
<meta property="og:site_name" content="SeongEraStudy">
<meta property="og:url" content="{{BASE}}/">
<meta property="og:image" content="{{BASE}}/og.jpg?v={{V}}">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{{BASE}}/og.jpg?v={{V}}">
<link rel="icon" type="image/png" href="{{LOGO}}">
<link rel="apple-touch-icon" href="{{LOGO}}">
<link rel="preload" as="image" href="{{LOGO}}">
<link rel="preconnect" href="https://huggingface.co">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,700;9..144,900&family=Mountains+of+Christmas:wght@700&family=Noto+Sans+KR:wght@800&family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">
<script>document.documentElement.classList.add('js')</script>
<style>
:root{
  --night:#050b1c;
  --ink:#f4fbff;
  --mut:rgba(228,243,255,.8);
  --ice:#bfe9ff;
  --red:#e8283f;
  --red2:#ff6a57;
  --green:#17a36b;
  --gold:#ffcf6b;
  --grad:linear-gradient(120deg,#ff5468,var(--gold) 55%,var(--ice));
  --glass:rgba(8,20,44,.64);
  --edge:rgba(200,230,255,.24);
  --head:"Fraunces",Georgia,serif;
  --body:"Outfit",system-ui,sans-serif;
  --script:"Mountains of Christmas","Fraunces",cursive;
  --kr:"Noto Sans KR",sans-serif;
  /* Santa hat on the owner circle: change these 4 numbers to move it */
  --hat-x:8%;--hat-y:-27%;--hat-rot:18deg;--hat-size:44%;
  /* Santa + reindeer flies left to right. If he faces backwards set this to -1 */
  --santa-flip:1;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;scroll-padding-top:100px}
body{background:var(--night);color:var(--ink);font-family:var(--body);font-size:17px;line-height:1.6;-webkit-font-smoothing:antialiased;overflow-x:hidden}
body.open,body.gated{overflow:hidden}
body{touch-action:manipulation}
a{color:inherit;text-decoration:none}
:focus-visible{outline:2px solid var(--gold);outline-offset:3px;border-radius:8px}
::selection{background:var(--red);color:#fff}

/* ---------- Backdrop ---------- */
.bg{position:fixed;inset:0;z-index:-3;background:radial-gradient(90% 70% at 70% 10%,#14306a 0%,var(--night) 70%);overflow:hidden}
.bg canvas{position:absolute;inset:0;width:100%;height:100%;z-index:1;opacity:.72}
.bg video{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;z-index:2;transform:translateZ(0);will-change:transform;backface-visibility:hidden}
.shade{position:fixed;inset:0;z-index:-2;pointer-events:none;
  background:
    radial-gradient(75% 65% at 50% 42%,rgba(5,11,28,.12),rgba(5,11,28,.66) 100%),
    linear-gradient(180deg,rgba(5,11,28,.55),rgba(5,11,28,.08) 32%,rgba(5,11,28,.9) 100%)}
#snow{position:fixed;inset:0;width:100%;height:100%;z-index:90;pointer-events:none}
body.gated #snow{z-index:106}
.prog{position:fixed;top:0;left:0;height:3px;width:0;z-index:250;background:var(--grad);box-shadow:0 0 14px rgba(255,207,107,.8)}

/* ---------- Christmas lights ---------- */
.lights{position:fixed;top:0;left:0;right:0;height:34px;z-index:120;pointer-events:none;display:flex;justify-content:space-around;align-items:flex-start;padding-top:6px}
.lights::before{content:"";position:absolute;left:0;right:0;top:5px;height:2px;background:#0d2a1f;box-shadow:0 1px 0 rgba(255,255,255,.1)}
.lights i{position:relative;width:9px;height:15px;margin-top:2px;border-radius:50% 50% 45% 45%/40% 40% 60% 60%;background:var(--c)}
.lights i:nth-child(odd){margin-top:6px}
.lights i::before{content:"";position:absolute;left:2px;top:-4px;width:5px;height:5px;border-radius:1px;background:#0d2a1f}
.lights i::after{content:"";position:absolute;left:-9px;top:-5px;width:27px;height:27px;border-radius:50%;background:radial-gradient(circle,var(--c),transparent 68%);opacity:.15;animation:tw 2.4s ease-in-out infinite}
.lights i:nth-child(4n+1){--c:#ff3b52}
.lights i:nth-child(4n+2){--c:#ffcf6b}
.lights i:nth-child(4n+3){--c:#35d69a}
.lights i:nth-child(4n+4){--c:#6fd0ff}
.lights i:nth-child(3n)::after{animation-delay:.6s}
.lights i:nth-child(3n+1)::after{animation-delay:1.2s}
@keyframes tw{0%,100%{opacity:.12}50%{opacity:.9}}

/* ---------- Santa + reindeer flyby ---------- */
.sleigh{position:fixed;top:11%;left:0;z-index:107;pointer-events:none;will-change:transform;transform:translate(-45vw,0);animation:fly 64s linear infinite;animation-delay:.5s}
.sleigh img{display:block;height:clamp(92px,17vw,180px);width:auto;transform:scaleX(var(--santa-flip,1));filter:drop-shadow(0 12px 18px rgba(0,0,0,.55)) drop-shadow(0 0 20px rgba(255,207,107,.4));animation:sbob 1.5s ease-in-out infinite}
@keyframes sbob{0%,100%{transform:translateY(0) scaleX(var(--santa-flip,1))}50%{transform:translateY(-9px) scaleX(var(--santa-flip,1))}}
@keyframes fly{0%{transform:translate(-45vw,0)}9%{transform:translate(140vw,-26px)}100%{transform:translate(140vw,-26px)}}

/* ---------- Nav ---------- */
.nav{position:fixed;top:42px;left:50%;transform:translateX(-50%);z-index:100;width:min(1000px,calc(100% - 28px));
  display:flex;align-items:center;justify-content:space-between;gap:14px;padding:10px 10px 10px 22px;border-radius:999px;
  background:rgba(7,16,38,.82);border:1px solid var(--edge)}
.logo{display:flex;align-items:center;gap:10px;font-family:var(--head);font-weight:900;font-size:1.1rem;letter-spacing:-.01em}
.lg{position:relative;flex:none;width:38px;height:38px}
.lg img.mark{width:38px;height:38px;object-fit:contain;border-radius:11px;display:block}
.lg img.mini{position:absolute;top:-13px;right:-10px;width:27px;height:auto;transform:rotate(22deg);transform-origin:50% 85%;pointer-events:none;filter:drop-shadow(0 2px 3px rgba(0,0,0,.5))}
.logo b{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.links{display:flex;gap:24px;font-size:.92rem;font-weight:500;color:var(--mut)}
.links a{position:relative;padding:4px 0;transition:color .2s}
.links a::after{content:"";position:absolute;left:0;bottom:-2px;height:2px;width:0;background:var(--grad);transition:width .25s}
.links a:hover,.links a.active{color:var(--ink)}
.links a:hover::after,.links a.active::after{width:100%}
.nr{display:flex;align-items:center;gap:10px}
.burger{display:none;width:44px;height:44px;border-radius:50%;border:1px solid var(--edge);background:var(--glass);cursor:pointer;position:relative}
.burger span{position:absolute;left:13px;right:13px;height:2px;border-radius:2px;background:var(--ink);transition:transform .3s,top .3s,opacity .3s}
.burger span:nth-child(1){top:16px}
.burger span:nth-child(2){top:21px}
.burger span:nth-child(3){top:26px}
body.open .burger span:nth-child(1){top:21px;transform:rotate(45deg)}
body.open .burger span:nth-child(2){opacity:0}
body.open .burger span:nth-child(3){top:21px;transform:rotate(-45deg)}
@media(max-width:860px){.links{display:none}.burger{display:block}}
.drawer{position:fixed;inset:0;z-index:95;background:rgba(5,11,28,.97);display:flex;flex-direction:column;justify-content:center;gap:6px;padding:120px 9vw 40px;transform:translateY(-102%);transition:transform .5s cubic-bezier(.7,0,.2,1)}
body.open .drawer{transform:none}
.drawer a{font-family:var(--head);font-weight:900;font-size:clamp(2rem,9vw,3rem);letter-spacing:-.02em;padding:6px 0;border-bottom:1px solid var(--edge);transition:padding-left .25s,color .25s}
.drawer a:hover{padding-left:12px;color:var(--gold)}
.drawer small{margin-top:18px;color:var(--mut)}

.pill{position:relative;overflow:hidden;display:inline-flex;align-items:center;gap:8px;padding:11px 22px;border-radius:999px;font-weight:700;font-size:.92rem;background:linear-gradient(120deg,var(--red),var(--red2));color:#fff;transition:transform .2s,box-shadow .2s;font-family:var(--body);border:0;cursor:pointer;box-shadow:0 8px 26px -10px rgba(232,40,63,.9)}
.pill::after{content:"";position:absolute;top:0;left:-60%;width:40%;height:100%;background:linear-gradient(100deg,transparent,rgba(255,255,255,.6),transparent);transform:skewX(-20deg);animation:shine 3.6s ease-in-out infinite}
@keyframes shine{0%,55%{left:-60%}100%{left:130%}}
.pill:hover{transform:translateY(-2px);box-shadow:0 16px 36px -10px rgba(232,40,63,1)}
.pill.big{padding:18px 36px;font-size:1.02rem}
.ghost{display:inline-flex;align-items:center;gap:10px;padding:17px 30px;border-radius:999px;border:1px solid var(--edge);background:var(--glass);font-weight:600;transition:background .2s,border-color .2s,transform .2s}
.ghost:hover{background:rgba(190,230,255,.16);border-color:rgba(255,255,255,.4);transform:translateY(-2px)}
.pill svg,.ghost svg{width:18px;height:18px}

/* ---------- Hero ---------- */
.hero{position:relative;min-height:100svh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:150px 22px 120px}
.badge{position:relative;display:inline-flex;align-items:center;gap:10px;padding:9px 20px;border-radius:999px;background:rgba(7,16,38,.72);font-size:.86rem;font-weight:600;color:var(--mut);isolation:isolate}
.badge::before{content:"";position:absolute;inset:0;border-radius:inherit;padding:1.5px;background:conic-gradient(from var(--ang,0deg),#ff5468,var(--gold),var(--ice),#35d69a,#ff5468);-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;animation:spin 5s linear infinite;z-index:-1}
@property --ang{syntax:"<angle>";initial-value:0deg;inherits:false}
@keyframes spin{to{--ang:360deg}}
.script{margin-top:22px;font-family:var(--script);font-weight:700;font-size:clamp(2.2rem,6.4vw,4.6rem);line-height:1;color:var(--gold);text-shadow:0 0 28px rgba(255,207,107,.55),0 4px 24px rgba(0,0,0,.6)}
.hero h1{margin-top:8px;font-family:var(--head);font-weight:900;font-size:clamp(2.7rem,8.2vw,6.8rem);line-height:1;letter-spacing:-.035em;max-width:15ch;text-shadow:0 6px 40px rgba(0,0,0,.6)}
.hero h1 em{font-style:normal;background:linear-gradient(120deg,#ff5468,var(--gold),var(--ice),#ff5468);background-size:260% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:flow 6s linear infinite;text-shadow:none}
@keyframes flow{to{background-position:260% 0}}
.hero p.lead{margin-top:22px;max-width:50ch;font-size:clamp(1rem,1.7vw,1.2rem);color:var(--mut);text-shadow:0 2px 20px rgba(0,0,0,.8)}
.rot{display:inline-block;min-width:5.4em;font-weight:700;color:var(--ink);border-bottom:2px solid var(--red);transition:opacity .3s,transform .3s}
.rot.out{opacity:0;transform:translateY(6px)}
.row{display:flex;flex-wrap:wrap;justify-content:center;gap:14px;margin-top:34px}

.cds{display:flex;flex-wrap:wrap;justify-content:center;gap:14px;margin-top:38px}
.cd{padding:14px 20px 16px;border-radius:22px;background:rgba(7,16,38,.72);border:1px solid var(--edge);min-width:260px}
.cd h4{font-family:var(--script);font-size:1.5rem;color:var(--gold);line-height:1;margin-bottom:10px;font-weight:700}
.cd div{display:flex;justify-content:center;gap:10px}
.cd div span{display:grid;place-items:center;min-width:54px;padding:7px 6px;border-radius:12px;background:rgba(255,255,255,.07)}
.cd b{font-family:var(--head);font-weight:900;font-size:1.5rem;line-height:1}
.cd i{font-style:normal;font-size:.62rem;letter-spacing:.14em;text-transform:uppercase;color:var(--mut)}
.cd em{font-style:normal;font-family:var(--head);font-weight:900;font-size:1.2rem}

.hero > *{opacity:0;transform:translateY(20px);animation:up .9s cubic-bezier(.2,.7,.2,1) forwards}
.hero > *:nth-child(1){animation-delay:.1s}
.hero > *:nth-child(2){animation-delay:.22s}
.hero > *:nth-child(3){animation-delay:.34s}
.hero > *:nth-child(4){animation-delay:.5s}
.hero > *:nth-child(5){animation-delay:.66s}
.hero > *:nth-child(6){animation-delay:.82s}
@keyframes up{to{opacity:1;transform:none}}
.scroll{position:absolute;bottom:78px;left:50%;margin-left:-13px;width:26px;height:42px;border:2px solid var(--edge);border-radius:14px}
.scroll::after{content:"";position:absolute;left:50%;top:8px;width:4px;height:8px;margin-left:-2px;border-radius:2px;background:var(--ink);animation:wheel 1.8s infinite}
@keyframes wheel{0%{opacity:1;transform:none}80%,100%{opacity:0;transform:translateY(14px)}}
@media(max-height:760px){.scroll{display:none}}

/* ---------- Ticker + ice ---------- */
.ticker{overflow:hidden;white-space:nowrap;border-block:1px solid var(--edge);background:rgba(5,11,28,.78)}
.ticker div{display:inline-flex;animation:scroll 40s linear infinite;padding:20px 0}
.ticker span{font-family:var(--script);font-weight:700;font-size:1.9rem;padding-right:46px;color:var(--ink)}
.ticker span::after{content:"❄";padding-left:46px;color:var(--ice);font-family:var(--body);font-size:1.1rem}
.ticker span:nth-child(3n)::after{content:"🎄"}
@keyframes scroll{to{transform:translateX(-50%)}}
.ice{height:44px;pointer-events:none;background:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='80' height='44'><polygon points='0,0 80,0 80,8 70,8 64,38 58,8 44,8 38,26 32,8 18,8 12,32 6,8 0,8' fill='%23dff1ff' fill-opacity='.92'/></svg>") repeat-x top}

/* ---------- Sections ---------- */
section{padding:clamp(70px,10vw,130px) 22px}
.wrap{max-width:1140px;margin:0 auto}
.eyebrow{font-family:var(--script);font-weight:700;font-size:1.7rem;line-height:1;color:var(--gold);display:inline-block;text-shadow:0 0 18px rgba(255,207,107,.4)}
h2{margin-top:10px;font-family:var(--head);font-weight:900;font-size:clamp(2.1rem,5vw,3.8rem);line-height:1.04;letter-spacing:-.03em;max-width:18ch}
.lead2{margin-top:16px;color:var(--mut);max-width:52ch}
.js .rv{opacity:0;transform:translateY(26px);transition:opacity .7s ease,transform .7s cubic-bezier(.2,.7,.2,1)}
.js .rv.in{opacity:1;transform:none}

/* Bento gift cards */
.bento{display:grid;grid-template-columns:repeat(6,1fr);gap:16px;margin-top:50px}
.card{position:relative;display:flex;flex-direction:column;justify-content:space-between;gap:30px;padding:30px;border-radius:28px;background:var(--glass);border:1px solid var(--edge);overflow:hidden;transition:border-color .3s,opacity .7s ease,transform .15s ease-out}
.card::before{content:"";position:absolute;inset:auto -20% -60% auto;width:260px;height:260px;border-radius:50%;background:var(--grad);opacity:0;filter:blur(70px);transition:opacity .4s}
.card::after{content:"";position:absolute;inset:0;pointer-events:none;opacity:0;transition:opacity .3s;background:radial-gradient(380px circle at var(--x,50%) var(--y,0%),rgba(255,255,255,.14),transparent 60%)}
.card:hover{border-color:rgba(255,255,255,.45)}
.card:hover::before{opacity:.4}
.card:hover::after{opacity:1}
.card .no{font-family:var(--script);font-weight:700;font-size:1.6rem;color:var(--gold);line-height:1}
.card h3{font-family:var(--head);font-weight:900;font-size:1.5rem;letter-spacing:-.02em;margin-bottom:8px}
.card p{color:var(--mut);font-size:.98rem}
.card .arrow{align-self:flex-start;display:grid;place-items:center;width:42px;height:42px;border-radius:50%;border:1px solid var(--edge);transition:background .25s,transform .25s,color .25s}
.card:hover .arrow{background:var(--red);color:#fff;border-color:transparent;transform:rotate(-45deg)}
.c1{grid-column:span 3;grid-row:span 2;min-height:340px}
.c1 h3{font-size:2.3rem;line-height:1.06}
.c2,.c3{grid-column:span 3}
.c4{grid-column:span 6;flex-direction:row;align-items:center;flex-wrap:wrap}
.tag{position:absolute;top:22px;right:-44px;width:170px;text-align:center;padding:6px 0;background:linear-gradient(90deg,#c9172f,#ff4d63);color:#fff;font-weight:800;font-size:.78rem;letter-spacing:.2em;transform:rotate(40deg);box-shadow:0 4px 14px rgba(0,0,0,.4)}
@media(max-width:760px){.c1,.c2,.c3,.c4{grid-column:span 6;grid-row:auto;min-height:0}}

/* Gift section */
.gift{position:relative;border-radius:36px;padding:clamp(34px,6vw,70px) clamp(24px,5vw,60px) clamp(34px,6vw,64px) clamp(84px,12vw,150px);background:linear-gradient(135deg,#b3162b,#6d0d1b 70%);border:1px solid rgba(255,255,255,.22);overflow:hidden}
.gift::before{content:"";position:absolute;top:0;bottom:0;left:clamp(22px,4.4vw,52px);width:clamp(30px,4.4vw,46px);background:linear-gradient(90deg,#d6a032,#ffe493 50%,#d6a032);box-shadow:0 0 30px rgba(255,207,107,.35)}
.gift .bow{position:absolute;top:12px;left:clamp(10px,3.2vw,38px);font-size:clamp(2.6rem,6vw,4rem);filter:drop-shadow(0 4px 8px rgba(0,0,0,.5))}
.gift h2{max-width:16ch}
.gift p{margin-top:16px;color:rgba(255,236,236,.92);max-width:48ch}
.gift .row{justify-content:flex-start}
.gift .pill{background:linear-gradient(120deg,#ffe493,var(--gold));color:#4a0a14;box-shadow:0 10px 30px -10px rgba(255,207,107,.8)}

/* Steps (candy cane numbers) */
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:0;margin-top:50px;border-top:1px solid var(--edge)}
.step{padding:34px 28px 10px 0}
.step b{display:inline-block;font-family:var(--head);font-size:4.4rem;font-weight:900;line-height:1;background:repeating-linear-gradient(-45deg,#ff3b52 0 11px,#fff 11px 22px);-webkit-background-clip:text;background-clip:text;color:transparent}
.step h3{margin-top:12px;font-family:var(--head);font-size:1.4rem;font-weight:900}
.step p{margin-top:6px;color:var(--mut);font-size:.97rem}

/* Character */
.hero2{display:grid;grid-template-columns:1fr 1.1fr;gap:34px;align-items:center}
@media(max-width:820px){.hero2{grid-template-columns:1fr}}
.kr{position:relative;display:grid;place-items:center;min-height:300px;border-radius:34px;border:1px solid var(--edge);background:radial-gradient(80% 80% at 30% 20%,rgba(191,233,255,.28),rgba(23,163,107,.14) 55%,rgba(232,40,63,.2));overflow:hidden}
.kr::before{content:"";position:absolute;left:0;right:0;top:0;height:26px;background:radial-gradient(circle at 20px 0,#eaf6ff 17px,transparent 18px) repeat-x;background-size:40px 26px;opacity:.95}
.kr strong{font-family:var(--kr);font-weight:800;font-size:clamp(3rem,9vw,6rem);line-height:1.05;text-align:center;background:linear-gradient(160deg,#fff,var(--ice) 55%,#ff8b98);-webkit-background-clip:text;background-clip:text;color:transparent}
.kr em{position:absolute;left:22px;bottom:16px;font-style:normal;font-size:.75rem;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--mut)}
.nm{margin-top:12px;font-family:var(--head);font-weight:900;font-size:clamp(2.2rem,5vw,3.8rem);line-height:1.04;letter-spacing:-.03em}
.nm span{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.hero2 p{margin-top:16px;color:var(--mut);max-width:46ch}

/* New Year 2027 */
.ny{display:grid;grid-template-columns:1.05fr 1fr;gap:34px;align-items:center}
@media(max-width:860px){.ny{grid-template-columns:1fr}}
.big27{font-family:var(--head);font-weight:900;font-size:clamp(5.5rem,22vw,15rem);line-height:.9;letter-spacing:-.05em;background:linear-gradient(120deg,var(--gold),#ff5468,var(--ice),var(--gold));background-size:260% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:flow 7s linear infinite;filter:drop-shadow(0 8px 30px rgba(0,0,0,.5))}
.ny .hny{font-family:var(--script);font-weight:700;font-size:clamp(1.8rem,4vw,2.8rem);color:var(--ice);margin-top:4px}
.resbox{padding:clamp(24px,4vw,40px);border-radius:30px;background:var(--glass);border:1px solid var(--edge)}
.resbox h3{font-family:var(--head);font-weight:900;font-size:1.6rem;margin-bottom:4px}
.resbox p.s{color:var(--mut);font-size:.95rem;margin-bottom:16px}
.res{display:flex;align-items:center;gap:14px;padding:14px 0;border-top:1px solid var(--edge);cursor:pointer;font-weight:500}
.res input{appearance:none;-webkit-appearance:none;flex:none;width:26px;height:26px;border-radius:8px;border:2px solid var(--ice);background:transparent;display:grid;place-items:center;cursor:pointer;transition:background .2s,border-color .2s}
.res input::after{content:"✓";color:#fff;font-weight:900;font-size:.95rem;transform:scale(0);transition:transform .2s}
.res input:checked{background:var(--green);border-color:var(--green)}
.res input:checked::after{transform:scale(1)}
.res input:checked + span{text-decoration:line-through;opacity:.6}
.resbox .pill{margin-top:20px}

/* Quote */
.quote{text-align:center}
.quote blockquote{font-family:var(--head);font-weight:900;font-size:clamp(2rem,6vw,4.6rem);line-height:1.04;letter-spacing:-.035em;max-width:16ch;margin:0 auto}
.quote blockquote em{font-style:normal;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}

/* FAQ */
.faq{margin-top:44px;max-width:820px}
.faq details{border-bottom:1px solid var(--edge);padding:6px 0}
.faq summary{list-style:none;display:flex;align-items:center;justify-content:space-between;gap:16px;cursor:pointer;padding:18px 0;font-family:var(--head);font-weight:900;font-size:1.15rem}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";display:grid;place-items:center;flex:none;width:34px;height:34px;border-radius:50%;border:1px solid var(--edge);font-size:1.3rem;font-weight:400;transition:transform .3s,background .3s}
.faq details[open] summary::after{transform:rotate(45deg);background:var(--red);color:#fff;border-color:transparent}
.faq p{padding:0 0 20px;color:var(--mut);max-width:60ch}

/* Owner */
.owner{display:grid;grid-template-columns:1.1fr 1fr;gap:34px;align-items:center;padding:clamp(28px,5vw,56px);border-radius:34px;background:linear-gradient(135deg,rgba(232,40,63,.26),rgba(23,163,107,.18) 55%,rgba(191,233,255,.2));border:1px solid var(--edge)}
@media(max-width:800px){.owner{grid-template-columns:1fr}}
.owner h2{font-size:clamp(1.7rem,3.8vw,2.7rem);max-width:none;line-height:1.2;letter-spacing:-.01em;word-break:break-word;font-family:var(--body);font-weight:700}
.owner .role{margin-top:14px;color:var(--mut)}
.links2{display:flex;flex-direction:column;gap:12px}
.lnk{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:18px 22px;border-radius:20px;background:rgba(5,11,28,.66);border:1px solid var(--edge);transition:border-color .2s,transform .2s}
.lnk:hover{border-color:var(--gold);transform:translateX(4px)}
.lnk small{display:block;color:var(--mut);font-size:.78rem;letter-spacing:.08em;text-transform:uppercase}
.lnk strong{font-family:var(--head);font-weight:900;font-size:1.15rem}

footer{position:relative;margin-top:30px;padding:46px 22px 120px;text-align:center;color:var(--mut);font-size:.92rem;background:rgba(5,11,28,.92)}
footer::before{content:"";position:absolute;left:0;right:0;top:-20px;height:21px;background:radial-gradient(circle at 24px 22px,#eaf6ff 21px,transparent 22px) repeat-x;background-size:48px 21px}
footer strong{color:var(--ink);font-family:var(--head);font-weight:900}
footer .sc{display:block;font-family:var(--script);font-size:1.8rem;color:var(--gold);margin-bottom:6px}
footer small{display:block;margin-top:6px;opacity:.62;font-size:.78rem}

/* ---------- Floating controls ---------- */
/* ---------- Music button (vinyl + pulse ring) ---------- */
.eq{display:flex;align-items:flex-end;gap:3px;width:22px;height:18px}
.eq i{flex:1;height:28%;border-radius:2px;background:#fff}
body.music-on .music .eq i,body.owner-on .cbtn .eq i{animation:eq 1s ease-in-out infinite}
body.music-on .music .eq i:nth-child(2),body.owner-on .cbtn .eq i:nth-child(2){animation-delay:.2s}
body.music-on .music .eq i:nth-child(3),body.owner-on .cbtn .eq i:nth-child(3){animation-delay:.4s}
body.music-on .music .eq i:nth-child(4),body.owner-on .cbtn .eq i:nth-child(4){animation-delay:.1s}
@keyframes eq{0%,100%{height:25%}50%{height:100%}}
.music{position:fixed;left:50%;bottom:20px;transform:translateX(-50%);z-index:110;display:flex;align-items:center;gap:14px;padding:8px 22px 8px 8px;border-radius:999px;
  background:linear-gradient(120deg,#e8283f,#ff6a57);border:1px solid rgba(255,255,255,.38);color:#fff;cursor:pointer;text-align:left;font-family:var(--body);
  box-shadow:0 14px 40px -10px rgba(232,40,63,.95);transition:background .3s,box-shadow .3s}
.music::before{content:"";position:absolute;inset:-2px;border-radius:inherit;border:2px solid rgba(255,130,140,.95);animation:ping 1.8s ease-out infinite;pointer-events:none}
@keyframes ping{0%{transform:scale(1);opacity:.9}100%{transform:scale(1.28,1.75);opacity:0}}
body:not(.music-on) .music{animation:nudge 5s ease-in-out infinite}
@keyframes nudge{0%,84%,100%{transform:translateX(-50%)}88%{transform:translateX(-50%) translateY(-11px)}92%{transform:translateX(-50%)}95%{transform:translateX(-50%) translateY(-5px)}}
.music:hover{transform:translateX(-50%) translateY(-3px)}
.music .vinyl{position:relative;flex:none;width:48px;height:48px;border-radius:50%;
  background:radial-gradient(circle,#ffcf6b 0 12%,transparent 13%),repeating-radial-gradient(circle,#14141c 0 2px,#272735 2px 3px);box-shadow:0 0 0 2px rgba(255,255,255,.35)}
.music .vinyl::after{content:"";position:absolute;inset:0;border-radius:50%;background:conic-gradient(transparent 0 20%,rgba(255,255,255,.28) 25%,transparent 32% 70%,rgba(255,255,255,.2) 75%,transparent 82%)}
body.music-on .vinyl{animation:rot 2.4s linear infinite}
.music .mt b{display:block;font-weight:800;font-size:1rem;line-height:1.15}
.music .mt small{display:block;font-size:.74rem;opacity:.9}
.music .eq{display:none}
body.music-on .music{background:linear-gradient(120deg,#0f9d63,#35d69a);box-shadow:0 14px 40px -10px rgba(53,214,154,.85)}
body.music-on .music::before{display:none}
body.music-on .music .eq{display:flex}
.bubble{position:fixed;left:50%;bottom:94px;z-index:111;transform:translate(-50%,10px) scale(.95);opacity:0;pointer-events:none;background:#fff;color:#1a0a10;padding:10px 18px;border-radius:16px;font-weight:700;font-size:.9rem;white-space:nowrap;transition:opacity .3s,transform .3s;box-shadow:0 14px 34px -8px rgba(0,0,0,.65)}
.bubble::after{content:"";position:absolute;left:50%;bottom:-6px;margin-left:-7px;width:14px;height:14px;background:#fff;transform:rotate(45deg)}
.bubble.show{opacity:1;transform:translate(-50%,0) scale(1)}
.celeb{position:fixed;right:18px;bottom:18px;z-index:110;width:54px;height:54px;border-radius:50%;border:1px solid var(--edge);background:rgba(7,16,38,.86);font-size:1.5rem;cursor:pointer;transition:transform .2s,background .2s}
.celeb:hover{transform:scale(1.1) rotate(-8deg);background:rgba(232,40,63,.35)}
.toast{position:fixed;top:112px;left:50%;z-index:130;transform:translate(-50%,-20px);opacity:0;pointer-events:none;padding:12px 24px;border-radius:999px;background:linear-gradient(120deg,var(--red),var(--red2));font-weight:700;box-shadow:0 14px 40px -10px rgba(232,40,63,.9);transition:opacity .35s,transform .35s;white-space:nowrap}
.toast.show{opacity:1;transform:translate(-50%,0)}

/* ---------- Intro screen (instant, one tap to enter) ---------- */
.gate{display:none}
.js .gate{position:fixed;inset:0;z-index:105;display:grid;place-items:center;padding:22px;overflow:hidden;
  background:radial-gradient(75% 55% at 50% 28%,rgba(28,62,128,.9),rgba(5,11,28,.98) 72%),var(--night);
  transition:opacity .6s ease,visibility .6s,transform .6s}
.gate.out{opacity:0;visibility:hidden;transform:scale(1.05)}
.gate::before{content:"";position:absolute;left:-25%;right:-25%;top:-45%;bottom:-45%;will-change:transform;
  background:conic-gradient(from 0deg at 50% 50%,transparent 0 18%,rgba(255,207,107,.12) 22%,transparent 27% 52%,rgba(111,208,255,.12) 57%,transparent 62%);animation:rot 22s linear infinite}
.intro-inner{position:relative;max-width:520px;width:100%;text-align:center}
.logo-wrap{position:relative;width:138px;height:138px;margin:0 auto 20px;animation:pop .8s cubic-bezier(.2,.9,.3,1.2) both}
@keyframes pop{from{opacity:0;transform:scale(.8) translateY(16px)}}
.logo-wrap::before{content:"";position:absolute;inset:-5px;border-radius:36px;background:conic-gradient(#ff3b52,#ffcf6b,#35d69a,#6fd0ff,#ff3b52);animation:rot 6s linear infinite}
.logo-wrap::after{content:"";position:absolute;inset:-22px;border-radius:50%;background:radial-gradient(circle,rgba(255,207,107,.28),transparent 66%);z-index:-1}
.logo-wrap .lw{position:absolute;inset:0;border-radius:32px;background:#0a1630;display:grid;place-items:center;overflow:hidden}
.logo-wrap img{width:84%;height:84%;object-fit:contain}
.i-script{font-family:var(--script);font-weight:700;font-size:clamp(1.6rem,5vw,2.2rem);color:var(--gold);line-height:1.1;text-shadow:0 0 24px rgba(255,207,107,.5)}
.i-title{margin-top:6px;font-family:var(--head);font-weight:900;font-size:clamp(2.4rem,9vw,3.6rem);line-height:1;letter-spacing:-.035em}
.i-title b{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.i-sub{margin-top:10px;color:var(--mut)}
.i-load{margin:22px auto 4px;max-width:260px}
.i-load .bar{height:5px;border-radius:5px;background:rgba(255,255,255,.12);overflow:hidden}
.i-load .bar i{display:block;height:100%;width:6%;border-radius:5px;background:var(--grad);transition:width .35s ease}
.i-load small{display:block;margin-top:8px;font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;color:var(--mut)}
.i-btns{margin-top:20px}
.i-btns .pill{width:100%;max-width:340px;justify-content:center}
.skip{display:block;margin:14px auto 0;background:none;border:0;color:var(--mut);font:500 .92rem var(--body);cursor:pointer;text-decoration:underline;text-underline-offset:3px;padding:6px 10px}
.skip:hover{color:var(--ink)}
.tip{margin-top:16px;font-size:.78rem;opacity:.65}
@keyframes iup{from{opacity:0;transform:translateY(14px)}}
.intro-inner > *:not(.logo-wrap){animation:iup .6s cubic-bezier(.2,.7,.2,1) both}
.intro-inner > :nth-child(2){animation-delay:.1s}
.intro-inner > :nth-child(3){animation-delay:.18s}
.intro-inner > :nth-child(4){animation-delay:.26s}
.intro-inner > :nth-child(5){animation-delay:.34s}
.intro-inner > :nth-child(6){animation-delay:.42s}
.intro-inner > :nth-child(7){animation-delay:.5s}
body.gated .nav,body.gated .music,body.gated .celeb,body.gated .bubble{opacity:0;pointer-events:none}
body.gated .hero > *{animation-play-state:paused}
.hint{margin-top:10px;font-size:.8rem;opacity:.65}

/* ---------- Hero tree ---------- */
.treewrap{display:none;position:absolute;right:-1vw;bottom:6vh;z-index:-1}
.treewrap img{display:block;height:min(54vh,480px);width:auto;filter:drop-shadow(0 24px 40px rgba(0,0,0,.55));animation:bob 6s ease-in-out infinite}
@keyframes bob{50%{transform:translateY(-12px)}}
@media(min-width:1200px){.treewrap{display:block}}

/* ---------- Gift boxes in gift card ---------- */
.gift .boxes{position:absolute;right:-2%;bottom:-8%;width:min(38%,360px);height:auto;pointer-events:none;filter:drop-shadow(0 18px 24px rgba(0,0,0,.45))}
@media(max-width:760px){.gift .boxes{position:static;display:block;width:min(72%,300px);margin:26px auto -24px}}

/* ---------- Snowy banner section ---------- */
.banner{padding-block:clamp(110px,16vw,220px);background:
  linear-gradient(180deg,var(--night) 0%,rgba(5,11,28,0) 22%,rgba(5,11,28,0) 78%,var(--night) 100%),
  radial-gradient(55% 55% at 50% 50%,rgba(5,11,28,.74),rgba(5,11,28,.2)),
  url("{{SNOWBG}}") center/cover no-repeat}

/* ---------- Owner circle card ---------- */
.ocol{text-align:center}
.ocol .eyebrow{margin-bottom:34px}
.circle{position:relative;width:min(300px,70vw);aspect-ratio:1;margin:0 auto;cursor:pointer;-webkit-tap-highlight-color:transparent;outline-offset:14px}
.circle::before{content:"";position:absolute;inset:-8px;border-radius:50%;background:conic-gradient(#ff3b52,#ffcf6b,#35d69a,#6fd0ff,#ff3b52);animation:rot 7s linear infinite}
.circle .disc{position:absolute;inset:0;border-radius:50%;overflow:hidden;background:#0a1228;border:4px solid var(--night);transition:transform .3s}
.circle video{width:100%;height:100%;object-fit:cover;display:block}
.circle .hat{position:absolute;z-index:3;top:var(--hat-y);right:var(--hat-x);width:var(--hat-size);height:auto;transform:rotate(var(--hat-rot));transform-origin:50% 85%;pointer-events:none;filter:drop-shadow(0 8px 12px rgba(0,0,0,.55))}
.circle .cbtn{position:absolute;z-index:3;left:50%;bottom:-20px;transform:translateX(-50%);display:flex;align-items:center;gap:10px;padding:11px 20px;border-radius:999px;background:linear-gradient(120deg,var(--red),var(--red2));color:#fff;font-weight:700;font-size:.86rem;white-space:nowrap;box-shadow:0 10px 26px -8px rgba(232,40,63,.95);transition:transform .2s,background .3s}
.circle .cbtn::before{content:"▶";font-size:.8rem}
.circle .cbtn .eq{display:none;width:18px;height:14px}
.circle:hover .cbtn{transform:translateX(-50%) translateY(-3px)}
body.owner-on .circle .cbtn{background:linear-gradient(120deg,#0f9d63,#35d69a)}
body.owner-on .circle .cbtn::before{display:none}
body.owner-on .circle .cbtn .eq{display:flex}
body.owner-on .circle .disc{animation:beat 1.2s ease-in-out infinite}
@keyframes beat{50%{transform:scale(1.03)}}
.ocol h2{margin-top:50px}

/* ---------- Footer snowman ---------- */
footer .fsnow{position:absolute;left:clamp(8px,6vw,90px);bottom:calc(100% - 20px);height:clamp(120px,19vw,210px);width:auto;pointer-events:none;filter:drop-shadow(0 10px 18px rgba(0,0,0,.4))}

@media(max-width:640px){.celeb{bottom:96px;right:12px;width:48px;height:48px}}

@media(prefers-reduced-motion:reduce){
  .music::before{display:none}
  *{animation:none!important;transition:none!important}
  .hero > *{opacity:1;transform:none}
  .js .rv{opacity:1;transform:none}
  .sleigh{display:none}
  html{scroll-behavior:auto}
}
</style>
</head>
<body>

<div class="prog" id="prog"></div>
<div class="lights" id="lights" aria-hidden="true"></div>

<div class="bg">
  <canvas id="fill" width="96" height="54" aria-hidden="true"></canvas>
  <video id="bgf" autoplay muted loop playsinline preload="auto" disablepictureinpicture src="{{VIDEO}}"></video>
</div>
<div class="shade"></div>
<canvas id="snow" aria-hidden="true"></canvas>
<div class="sleigh" aria-hidden="true"><img src="{{SANTA}}" alt="" width="260" height="170" decoding="async"></div>
<div class="toast" id="toast" role="status"></div>

<div class="gate" id="gate" role="dialog" aria-modal="true" aria-label="Welcome to SeongEraStudy">
  <div class="intro-inner">
    <div class="logo-wrap"><div class="lw"><img src="{{LOGO}}" alt="SeongEraStudy" width="116" height="116"></div></div>
    <div class="i-script">Merry Christmas &amp; Happy New Year 2027</div>
    <div class="i-title">Seong<b>Era</b>Study</div>
    <p class="i-sub">Education is free for everyone.</p>
    <div class="i-load"><div class="bar"><i id="ibar"></i></div><small id="istat">Preparing the magic…</small></div>
    <div class="i-btns">
      <button class="pill big" id="gOn" type="button">🎶 Enter with music</button>
      <button class="skip" id="gOff" type="button">Enter without sound</button>
    </div>
    <div class="tip">Tip: double-tap anywhere to turn the music on or off.</div>
  </div>
</div>

<nav class="nav">
  <a class="logo" href="#top" aria-label="SeongEraStudy home"><span class="lg"><img class="mark" src="{{LOGO}}" alt="" width="38" height="38"><img class="mini" src="{{HAT}}" alt="" width="25" height="25" loading="lazy" decoding="async"></span><span>Seong<b>Era</b>Study</span></a>
  <div class="links" id="links">
    <a href="#learn">Learn</a>
    <a href="#how">How it works</a>
    <a href="#ny">2027</a>
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
  <a href="#ny">New Year 2027</a>
  <a href="#faq">FAQ</a>
  <a href="#owner">Owner</a>
  <small>Merry Christmas and Happy New Year 2027!</small>
</div>

<main id="top">
  <div class="hero">
    <div class="badge">❄ Merry Christmas &amp; Happy New Year 2027 🎄</div>
    <div class="script">Education is our gift</div>
    <h1>Education is <em>free</em> for everyone.</h1>
    <p class="lead">Watch, read and practice <span class="rot" id="rot">anywhere</span>, all in one simple portal. Open it and start learning today.</p>
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
    <div class="cds">
      <div class="cd"><h4>Christmas in</h4><div id="cdx"></div></div>
      <div class="cd"><h4>New Year 2027 in</h4><div id="cdn"></div></div>
    </div>
    <div class="scroll" aria-hidden="true"></div>
    <div class="treewrap" aria-hidden="true"><img src="{{TREE}}" alt="" width="480" height="480" decoding="async"></div>
  </div>

  <div class="ticker" aria-hidden="true">
    <div>
      <span>Merry Christmas</span><span>Education is free for everyone</span><span>Happy New Year 2027</span><span>Learn without limits</span><span>Let it snow</span><span>Study today, shape tomorrow</span>
      <span>Merry Christmas</span><span>Education is free for everyone</span><span>Happy New Year 2027</span><span>Learn without limits</span><span>Let it snow</span><span>Study today, shape tomorrow</span>
    </div>
  </div>

  <section id="learn">
    <div class="wrap">
      <div class="eyebrow rv">Unwrap your classes</div>
      <h2 class="rv">One portal. Everything to study.</h2>
      <p class="lead2 rv">Learn at your own pace from any phone or laptop.</p>
      <div class="bento">
        <a class="card c1 rv" href="{{PORTAL}}" target="_blank" rel="noopener">
          <span class="tag">FREE</span>
          <div><span class="no">Gift no. 1</span><h3 style="margin-top:14px">Video lectures that keep you focused.</h3><p>Watch classes in a clean, smooth player built for learning.</p></div>
          <span class="arrow">→</span>
        </a>
        <a class="card c2 rv" href="{{PORTAL}}" target="_blank" rel="noopener">
          <div><span class="no">Gift no. 2</span><h3 style="margin-top:10px">Notes and PDFs</h3><p>Clear study material, ready whenever you are.</p></div>
          <span class="arrow">→</span>
        </a>
        <a class="card c3 rv" href="{{PORTAL}}" target="_blank" rel="noopener">
          <div><span class="no">Gift no. 3</span><h3 style="margin-top:10px">Practice and tests</h3><p>Check what you learned and keep getting better.</p></div>
          <span class="arrow">→</span>
        </a>
        <a class="card c4 rv" href="{{CHANNEL}}" target="_blank" rel="noopener">
          <div style="flex:1;min-width:240px"><span class="no">Gift no. 4</span><h3 style="margin-top:10px">Join the Telegram community</h3><p>Get every update and ask your doubts in the channel.</p></div>
          <span class="arrow">→</span>
        </a>
      </div>
    </div>
  </section>

  <div class="ice" aria-hidden="true"></div>

  <section id="gift">
    <div class="wrap">
      <div class="gift rv">
        <img class="boxes" src="{{GIFTS}}" alt="" width="360" height="360" loading="lazy" decoding="async">
        <span class="bow" aria-hidden="true">🎀</span>
        <div class="eyebrow" style="color:#ffe9b0">Our Christmas gift</div>
        <h2>The best gift is knowledge. And it is free.</h2>
        <p>Whoever you are, wherever you study from, SeongEraStudy is open for you. No price tag, no gate. Just learning.</p>
        <div class="row">
          <a class="pill big" href="{{PORTAL}}" target="_blank" rel="noopener">Open your gift →</a>
        </div>
      </div>
    </div>
  </section>

  <section id="how">
    <div class="wrap">
      <div class="eyebrow rv">Easy as 1, 2, 3</div>
      <h2 class="rv">Start in three simple steps.</h2>
      <div class="steps">
        <div class="step rv"><b>1</b><h3>Open the portal</h3><p>Tap Open Portal. No complicated setup.</p></div>
        <div class="step rv"><b>2</b><h3>Pick your class</h3><p>Choose the subject or batch you want to study.</p></div>
        <div class="step rv"><b>3</b><h3>Learn every day</h3><p>Watch, read, practice, and follow the channel for updates.</p></div>
      </div>
    </div>
  </section>

  <section id="meet">
    <div class="wrap hero2">
      <div class="kr rv"><strong>약한<br>영웅</strong><em>Weak Hero</em></div>
      <div class="rv">
        <div class="eyebrow">The hero of our portal</div>
        <div class="nm">Seong <span>Jee</span> Gium</div>
        <p>A character from Weak Hero. Not the loudest in the room, but never someone to underestimate. Learn like him: stay calm, stay sharp, keep growing.</p>
      </div>
    </div>
  </section>

  <section id="ny">
    <div class="wrap ny">
      <div class="rv">
        <div class="eyebrow">New year, new goals</div>
        <div class="big27">2027</div>
        <div class="hny">Happy New Year!</div>
      </div>
      <div class="resbox rv">
        <h3>Your 2027 study goals</h3>
        <p class="s">Tick them off. Finish all four for a surprise.</p>
        <label class="res"><input type="checkbox"><span>Study a little, every single day</span></label>
        <label class="res"><input type="checkbox"><span>Finish one full subject</span></label>
        <label class="res"><input type="checkbox"><span>Help a friend learn something new</span></label>
        <label class="res"><input type="checkbox"><span>Share SeongEraStudy with 3 classmates</span></label>
        <button class="pill" id="celebrate2" type="button">Celebrate 🎆</button>
      </div>
    </div>
  </section>

  <section class="quote banner">
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
        <details class="rv"><summary>Who do I contact for help?</summary><p>Message the owner @SeongEra on Telegram.</p></details>
      </div>
    </div>
  </section>

  <section id="owner">
    <div class="wrap">
      <div class="owner rv">
        <div class="ocol">
          <div class="eyebrow">Owner</div>
          <div class="circle" id="circle" role="button" tabindex="0" aria-label="Owner video. Tap to turn its own sound on or off">
            <img class="hat" src="{{HAT}}" alt="" width="140" height="140" loading="lazy" decoding="async">
            <div class="disc"><video id="ov" muted loop playsinline preload="none" data-src="{{OVIDEO}}"></video></div>
            <span class="cbtn"><span class="eq" aria-hidden="true"><i></i><i></i><i></i><i></i></span><b id="cl">Tap for sound</b></span>
          </div>
          <h2>{{OWNER_NAME}}</h2>
          <p class="role">Founder of SeongEraStudy. Made by Seong Gium Jee.</p>
          <p class="hint">Every video has its own sound. Playing one stops the other.</p>
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
  <img class="fsnow" src="{{SNOWMAN}}" alt="" width="210" height="210" loading="lazy" decoding="async">
  <span class="sc">Merry Christmas &amp; Happy New Year 2027</span>
  <strong>SeongEraStudy</strong> · Made by Seong Gium Jee · © <span id="yr"></span>
  <small>Weak Hero fan-inspired. Not affiliated with the original creators. Background edit uses the song "Snowman" by Sia.</small>
  <small>Tip: double-tap anywhere to turn the music on or off.</small>
</footer>

<button class="celeb" id="celebrate" type="button" aria-label="Celebrate with fireworks" title="Celebrate!">🎆</button>
<div class="bubble" id="bubble" aria-hidden="true">Tap for Christmas music 🎶</div>
<button class="music" id="snd" type="button" aria-pressed="false" aria-label="Turn music on">
  <span class="vinyl" aria-hidden="true"></span>
  <span class="mt"><b id="sndl">Tap for music</b><small id="sndsub">Snowman · Sia</small></span>
  <span class="eq" aria-hidden="true"><i></i><i></i><i></i><i></i></span>
</button>

<script>
(function(){
  var $=function(id){return document.getElementById(id)};
  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine=window.matchMedia('(hover:hover) and (pointer:fine)').matches;
  function safe(p){ if(p&&p.catch)p.catch(function(){}); }

  /* ================= VIDEO + FILL ================= */
  var v=$('bgf'), fl=$('fill'), fx=fl.getContext('2d'), b=$('snd'), l=$('sndl'), fillTimer=null;
  function paint(){ try{ fx.drawImage(v,0,0,fl.width,fl.height); }catch(e){} }
  function startFill(){ if(!fillTimer){ fillTimer=setInterval(paint,110); } }
  function stopFill(){ clearInterval(fillTimer); fillTimer=null; }

  /* ================= SNOW + FIREWORKS ================= */
  var sc=$('snow'), sx=sc.getContext('2d'), W=0,H=0, flakes=[], sparks=[], wind=0, tw=0, raf=0, running=false;
  function mk(init){
    var r=Math.random()*2.6+.8;
    return {x:Math.random()*W,y:init?Math.random()*H:-8,r:r,vy:.35+r*.42,ph:Math.random()*6.283,a:.5+Math.random()*.5};
  }
  function size(){
    var dpr=Math.min(window.devicePixelRatio||1,1.5);
    W=window.innerWidth; H=window.innerHeight;
    sc.width=W*dpr; sc.height=H*dpr; sx.setTransform(dpr,0,0,dpr,0,0);
    var n=Math.round(Math.min(W*H/13000,fine?130:60));
    while(flakes.length<n){ flakes.push(mk(true)); }
    flakes.length=n;
  }
  function frame(){
    raf=requestAnimationFrame(frame);
    sx.clearRect(0,0,W,H);
    tw+=.01;
    sx.fillStyle='#fff';
    for(var i=0;i<flakes.length;i++){
      var f=flakes[i];
      f.y+=f.vy;
      f.x+=Math.sin(tw*2+f.ph)*.45+wind*f.r*.3;
      if(f.y>H+8){ f.y=-8; f.x=Math.random()*W; }
      if(f.x>W+8){ f.x=-8; } else if(f.x<-8){ f.x=W+8; }
      sx.globalAlpha=f.a;
      sx.beginPath(); sx.arc(f.x,f.y,f.r,0,6.283); sx.fill();
    }
    for(var j=sparks.length-1;j>=0;j--){
      var p=sparks[j];
      p.vx*=.985; p.vy=p.vy*.985+p.g; p.x+=p.vx; p.y+=p.vy; p.life--;
      if(p.life<=0){ sparks[j]=sparks[sparks.length-1]; sparks.pop(); continue; }
      sx.globalAlpha=Math.min(1,p.life/p.max*1.4);
      sx.fillStyle=p.c;
      sx.beginPath(); sx.arc(p.x,p.y,p.s,0,6.283); sx.fill();
    }
    sx.globalAlpha=1;
  }
  function startSnow(){ if(!running && !reduce){ running=true; raf=requestAnimationFrame(frame); } }
  function stopSnow(){ running=false; cancelAnimationFrame(raf); }
  size(); window.addEventListener('resize',size);

  var cols=['#ffcf6b','#ff5468','#bfe9ff','#ffffff','#5cf2b0'];
  function burst(x,y,n){
    if(sparks.length>520){ return; }
    var c=cols[(Math.random()*cols.length)|0];
    for(var i=0;i<n;i++){
      var a=Math.random()*6.283, s=Math.random()*4.4+1, life=70+((Math.random()*45)|0);
      sparks.push({x:x,y:y,vx:Math.cos(a)*s,vy:Math.sin(a)*s,life:life,max:life,c:Math.random()<.2?'#fff':c,s:Math.random()*1.4+1,g:.045});
    }
  }
  var tt=0;
  function toast(msg){
    var t=$('toast'); t.textContent=msg; t.classList.add('show');
    clearTimeout(tt); tt=setTimeout(function(){ t.classList.remove('show'); },2800);
  }
  function celebrate(){
    startSnow();
    for(var k=0;k<7;k++){
      (function(k){ setTimeout(function(){ burst(W*(.12+Math.random()*.76),H*(.1+Math.random()*.42),70); },k*240); })(k);
    }
    toast('Happy New Year 2027! 🎆');
  }
  $('celebrate').addEventListener('click',celebrate);
  $('celebrate2').addEventListener('click',celebrate);

  /* sparkle trail + wind (desktop) */
  var lastT=0;
  window.addEventListener('pointermove',function(e){
    wind=((e.clientX/W)-.5)*1.4;
    if(!fine||reduce){ return; }
    var n=Date.now(); if(n-lastT<45){ return; } lastT=n;
    if(sparks.length>300){ return; }
    for(var i=0;i<2;i++){
      sparks.push({x:e.clientX,y:e.clientY,vx:(Math.random()-.5)*.8,vy:Math.random()*.8+.1,life:26,max:26,c:i?'#ffcf6b':'#dff3ff',s:1.5,g:.02});
    }
  },{passive:true});

  /* ================= PLAY / PAUSE ================= */
  var ov=$('ov'), ovVis=false, who='';   /* who = which video has sound: '' | 'bg' | 'owner' */
  function ovReady(){ if(!ov.getAttribute('src')){ ov.src=ov.getAttribute('data-src'); } }
  function play(){ safe(v.play()); startFill(); startSnow(); if((ovVis||who==='owner')&&ov.getAttribute('src')){ safe(ov.play()); } }
  function stop(){ v.pause(); stopFill(); stopSnow(); ov.pause(); }
  try{ v.currentTime=0; }catch(e){}
  play();
  v.addEventListener('loadeddata',paint);
  document.addEventListener('visibilitychange',function(){ if(document.hidden){ stop(); } else { play(); } });
  window.addEventListener('pagehide',stop);
  window.addEventListener('pageshow',function(){ if(!document.hidden){ play(); } });

  /* ================= AUDIO: only one video makes sound at a time ================= */
  var sub=$('sndsub'), cl=$('cl'), bub=$('bubble'), bubN=0, bubT=0;
  function hideBubble(){ bub.classList.remove('show'); }
  function showBubble(){
    if(who||bubN>=3||document.hidden||document.body.classList.contains('gated')){ return; }
    bubN++; bub.classList.add('show'); clearTimeout(bubT); bubT=setTimeout(hideBubble,6500);
  }
  function setAudio(w){
    who=w;
    if(w==='owner'){ ovReady(); }
    v.muted=(w!=='bg'); ov.muted=(w!=='owner');
    if(w==='bg'){ v.volume=.85; }
    if(w==='owner'){ ov.volume=1; }
    play();
    var bgOn=(w==='bg'), owOn=(w==='owner');
    b.setAttribute('aria-pressed',bgOn);
    b.setAttribute('aria-label',bgOn?'Turn music off':'Turn music on');
    l.textContent=bgOn?'Music on':'Tap for music';
    sub.textContent=bgOn?'Tap to mute':(owOn?'Owner video sound is on':'Snowman \u00b7 Sia');
    cl.textContent=owOn?'Sound on \u00b7 tap to mute':'Tap for sound';
    document.body.classList.toggle('music-on',bgOn);
    document.body.classList.toggle('owner-on',owOn);
    hideBubble();
  }
  function flip(){
    var p=who; setAudio(p==='bg'?'':'bg');
    toast(who==='bg'?(p==='owner'?'Background music on \u00b7 owner sound stopped':'Music on \ud83c\udfb6'):'Music off');
  }
  function flipOwner(){
    var p=who; setAudio(p==='owner'?'':'owner');
    toast(who==='owner'?(p==='bg'?'Owner video sound on \u00b7 background music stopped':'Owner video sound on \ud83d\udd0a'):'Sound off');
  }
  b.addEventListener('click',flip);
  var circle=$('circle');
  circle.addEventListener('click',flipOwner);
  circle.addEventListener('keydown',function(e){ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); flipOwner(); } });
  setTimeout(showBubble,4500); setInterval(showBubble,35000);

  /* gestures: double-tap / double-click anywhere, or press M (background music) */
  function inter(t){ return t&&t.closest&&t.closest('a,button,input,label,summary,details,.circle,.gate'); }
  var lastTap=0,lx=0,ly=0;
  document.addEventListener('touchend',function(e){
    if(inter(e.target)){ return; }
    var t=e.changedTouches[0], n=Date.now();
    if(n-lastTap<320&&Math.abs(t.clientX-lx)<40&&Math.abs(t.clientY-ly)<40){ lastTap=0; flip(); }
    else{ lastTap=n; lx=t.clientX; ly=t.clientY; }
  },{passive:true});
  if(fine){ document.addEventListener('dblclick',function(e){ if(!inter(e.target)){ flip(); } }); }
  document.addEventListener('keydown',function(e){
    var tg=document.activeElement?document.activeElement.tagName:'';
    if((e.key==='m'||e.key==='M')&&tg!=='INPUT'&&tg!=='TEXTAREA'){ flip(); }
  });

  /* owner video: loads only when close, plays only while visible (or while its sound is on) */
  if('IntersectionObserver' in window){
    new IntersectionObserver(function(es){ if(es[0].isIntersecting){ ovReady(); } },{rootMargin:'500px 0px'}).observe(circle);
    new IntersectionObserver(function(es){
      ovVis=es[0].isIntersecting;
      if(!ov.getAttribute('src')){ return; }
      if((ovVis||who==='owner')&&!document.hidden){ safe(ov.play()); } else { ov.pause(); }
    },{threshold:.25}).observe(circle);
  } else { ovReady(); ovVis=true; }

  /* ================= INTRO: instant, real progress, one tap ================= */
  var ibar=$('ibar'), istat=$('istat'), steps=0, TOT=4;
  function step(){
    steps++;
    var pct=Math.min(100,Math.round(steps/TOT*100));
    if(ibar){ ibar.style.width=pct+'%'; }
    if(pct>=100&&istat){ istat.textContent='Ready'; }
  }
  step();
  var vdone=false; function vstep(){ if(!vdone){ vdone=true; step(); } }
  if(v.readyState>=2){ vstep(); } else { v.addEventListener('loadeddata',vstep); }
  var glogo=document.querySelector('#gate img');
  if(!glogo||glogo.complete){ step(); } else { glogo.addEventListener('load',step); glogo.addEventListener('error',step); }
  if(document.readyState==='complete'){ step(); } else { window.addEventListener('load',step); }
  setTimeout(function(){ if(ibar){ ibar.style.width='100%'; } if(istat){ istat.textContent='Ready'; } },2600);

  var gate=$('gate');
  function closeGate(){
    if(!gate){ return; }
    var g=gate; gate=null;
    g.classList.add('out'); document.body.classList.remove('gated');
    try{ sessionStorage.setItem('sxg','1'); }catch(e){}
    setTimeout(function(){ g.remove(); },700);
  }
  var seen=null; try{ seen=sessionStorage.getItem('sxg'); }catch(e){}
  if(seen){ gate.remove(); gate=null; }
  else {
    document.body.classList.add('gated');
    $('gOn').addEventListener('click',function(){ setAudio('bg'); closeGate(); toast('Music on \ud83c\udfb6'); });
    $('gOff').addEventListener('click',closeGate);
    document.addEventListener('keydown',function(e){ if(e.key==='Escape'){ closeGate(); } });
  }

  /* ================= LIGHTS ================= */
  var lights=$('lights');
  function buildLights(){
    var n=Math.max(12,Math.floor(window.innerWidth/38)), h='';
    for(var i=0;i<n;i++){ h+='<i></i>'; }
    lights.innerHTML=h;
  }
  buildLights(); window.addEventListener('resize',buildLights);

  /* ================= MENU ================= */
  var burger=$('burger'), drawer=$('drawer');
  function toggle(open){ document.body.classList.toggle('open',open); burger.setAttribute('aria-expanded',open); }
  burger.addEventListener('click',function(){ toggle(!document.body.classList.contains('open')); });
  drawer.querySelectorAll('a').forEach(function(a){ a.addEventListener('click',function(){ toggle(false); }); });
  document.addEventListener('keydown',function(e){ if(e.key==='Escape'){ toggle(false); } });

  /* ================= ROTATING WORD ================= */
  var words=['anywhere','anytime','on any device','at your pace','for free'], wi=0, rot=$('rot');
  setInterval(function(){
    rot.classList.add('out');
    setTimeout(function(){ wi=(wi+1)%words.length; rot.textContent=words[wi]; rot.classList.remove('out'); },320);
  },2400);

  /* ================= COUNTDOWNS ================= */
  var XM=new Date(2026,11,25,0,0,0).getTime(), NY=new Date(2027,0,1,0,0,0).getTime();
  function p2(n){ return n<10?'0'+n:''+n; }
  function fmt(ms){
    var s=Math.max(0,Math.floor(ms/1000)), d=Math.floor(s/86400), h=Math.floor(s%86400/3600), m=Math.floor(s%3600/60), c=s%60;
    return '<span><b>'+d+'</b><i>days</i></span><span><b>'+p2(h)+'</b><i>hrs</i></span><span><b>'+p2(m)+'</b><i>min</i></span><span><b>'+p2(c)+'</b><i>sec</i></span>';
  }
  function setCd(id,ms,done){ $(id).innerHTML=ms>0?fmt(ms):'<em>'+done+'</em>'; }
  function tick(){ var n=Date.now(); setCd('cdx',XM-n,'Merry Christmas! 🎄'); setCd('cdn',NY-n,'Happy New Year 2027! 🎆'); }
  tick(); setInterval(tick,1000);

  /* ================= 2027 GOALS ================= */
  var saved={}; try{ saved=JSON.parse(localStorage.getItem('sx27')||'{}'); }catch(e){}
  var rs=document.querySelectorAll('.res input');
  rs.forEach(function(i,idx){
    i.checked=!!saved[idx];
    i.addEventListener('change',function(){
      saved[idx]=i.checked;
      try{ localStorage.setItem('sx27',JSON.stringify(saved)); }catch(e){}
      var all=true; rs.forEach(function(x){ if(!x.checked){ all=false; } });
      if(all){ celebrate(); }
    });
  });

  /* ================= REVEAL + SCROLLSPY ================= */
  var items=document.querySelectorAll('.rv');
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){
      es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
    },{threshold:.12});
    items.forEach(function(el,i){ el.style.transitionDelay=((i%4)*70)+'ms'; io.observe(el); });

    var links=document.querySelectorAll('#links a'), map={};
    links.forEach(function(a){ map[a.getAttribute('href').slice(1)]=a; });
    var so=new IntersectionObserver(function(es){
      es.forEach(function(e){
        if(e.isIntersecting && map[e.target.id]){
          links.forEach(function(a){ a.classList.remove('active'); });
          map[e.target.id].classList.add('active');
        }
      });
    },{rootMargin:'-45% 0px -50% 0px'});
    Object.keys(map).forEach(function(id){ var s=$(id); if(s){ so.observe(s); } });
  } else { items.forEach(function(el){ el.classList.add('in'); }); }

  /* ================= CARD SPOTLIGHT + TILT ================= */
  if(fine){
    document.querySelectorAll('.card').forEach(function(c){
      c.addEventListener('pointermove',function(e){
        var r=c.getBoundingClientRect(), x=e.clientX-r.left, y=e.clientY-r.top;
        c.style.setProperty('--x',x+'px'); c.style.setProperty('--y',y+'px');
        var rx=((y/r.height)-.5)*-6, ry=((x/r.width)-.5)*6;
        c.style.transform='perspective(900px) rotateX('+rx+'deg) rotateY('+ry+'deg) translateY(-4px)';
      });
      c.addEventListener('pointerleave',function(){ c.style.transform=''; });
    });
  }

  /* ================= SCROLL PROGRESS ================= */
  var bar=$('prog');
  function onScroll(){
    var h=document.documentElement.scrollHeight-window.innerHeight;
    bar.style.width=(h>0?(window.scrollY/h)*100:0)+'%';
  }
  window.addEventListener('scroll',onScroll,{passive:true}); onScroll();

  $('yr').textContent=new Date().getFullYear();
})();
</script>
</body>
</html>
"""

V = ASSET_VERSION
PAGE = (
    HTML.replace("{{PORTAL}}", PORTAL_LINK)
        .replace("{{CHANNEL}}", CHANNEL_LINK)
        .replace("{{OWNER}}", OWNER_LINK)
        .replace("{{OWNER_NAME}}", OWNER_NAME)
        .replace("{{VIDEO}}", VIDEO_URL)
        .replace("{{OVIDEO}}", OWNER_VIDEO_URL)
        .replace("{{LOGO}}", "/a/logo.png?v=" + V)
        .replace("{{TREE}}", "/a/tree.webp?v=" + V)
        .replace("{{GIFTS}}", "/a/gifts.webp?v=" + V)
        .replace("{{SNOWMAN}}", "/a/snowman.webp?v=" + V)
        .replace("{{HAT}}", "/a/hat.webp?v=" + V)
        .replace("{{SANTA}}", "/a/santa.webp?v=" + V)
        .replace("{{SNOWBG}}", "/a/snowbg.jpg?v=" + V)
        .replace("{{V}}", V)
)

# ---------------------------------------------------------------
#  Image helper: resizes big pictures (faster site), removes a
#  white / checkerboard background if one is baked in, and builds
#  the WhatsApp / Telegram share picture. Results are cached.
# ---------------------------------------------------------------
ASSETS = {
    "logo":    dict(url=LOGO_URL,    max=360,  fmt="PNG"),
    "tree":    dict(url=TREE_URL,    max=900,  fmt="WEBP"),
    "gifts":   dict(url=GIFTS_URL,   max=720,  fmt="WEBP"),
    "snowman": dict(url=SNOWMAN_URL, max=560,  fmt="WEBP"),
    "hat":     dict(url=HAT_URL,     max=320,  fmt="WEBP"),
    "santa":   dict(url=SANTA_URL,   max=640,  fmt="WEBP"),
    "snowbg":  dict(url=SNOWBG_URL,  max=1920, fmt="JPEG"),
}
CACHE_HDR = "public, max-age=86400, s-maxage=2592000, stale-while-revalidate=86400"
_cache = {}


def fetch(url, timeout=9):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (SeongEraStudy asset loader)"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def remove_bg(im, limit=640):
    """Make a light (white / checkerboard) outer background transparent.
    Only touches pixels connected to the picture edge, so white fur, snow
    and highlights inside the artwork stay. Already-transparent images are untouched."""
    im = im.convert("RGBA")
    w, h = im.size
    corners = [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]
    alpha = im.getchannel("A")
    if all(alpha.getpixel(c) < 16 for c in corners):
        return im
    sc = min(1.0, limit / float(max(w, h)))
    if sc < 1.0:
        im = im.resize((max(1, int(w * sc)), max(1, int(h * sc))), Image.LANCZOS)
        w, h = im.size
        corners = [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]
    rgb = Image.new("RGB", im.size, (255, 255, 255))
    rgb.paste(im, mask=im.getchannel("A"))
    lo, hi = rgb.crop((0, 0, min(28, w), min(28, h))).convert("L").getextrema()
    thresh = 175 if (hi - lo) > 14 else 50          # checkerboard vs solid colour
    marker = (255, 0, 255)
    touched = False
    for c in corners:
        r, g, b = rgb.getpixel(c)
        if (r + g + b) / 3.0 >= 170:                 # only remove LIGHT backgrounds
            ImageDraw.floodfill(rgb, c, marker, thresh=thresh)
            touched = True
    if not touched:
        return im
    r, g, b = rgb.split()
    is_bg = ImageChops.multiply(
        ImageChops.multiply(r.point(lambda p: 255 if p == 255 else 0),
                            g.point(lambda p: 255 if p == 0 else 0)),
        b.point(lambda p: 255 if p == 255 else 0))
    keep = ImageChops.invert(is_bg).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.8))
    im.putalpha(ImageChops.multiply(keep, im.getchannel("A")))
    return im


def build_asset(key):
    cfg = ASSETS[key]
    im = Image.open(io.BytesIO(fetch(cfg["url"])))
    im.load()
    buf = io.BytesIO()
    if cfg["fmt"] == "JPEG":
        im = im.convert("RGB")
        sc = min(1.0, cfg["max"] / float(max(im.size)))
        if sc < 1.0:
            im = im.resize((int(im.width * sc), int(im.height * sc)), Image.LANCZOS)
        im.save(buf, "JPEG", quality=78, optimize=True, progressive=True)
        return buf.getvalue(), "image/jpeg"
    im = remove_bg(im)
    sc = min(1.0, cfg["max"] / float(max(im.size)))
    if sc < 1.0:
        im = im.resize((max(1, int(im.width * sc)), max(1, int(im.height * sc))), Image.LANCZOS)
    if cfg["fmt"] == "WEBP":
        im.save(buf, "WEBP", quality=86, method=4)
        return buf.getvalue(), "image/webp"
    im.save(buf, "PNG", optimize=True)
    return buf.getvalue(), "image/png"


def get_asset(key):
    if key not in _cache:
        _cache[key] = build_asset(key)
    return _cache[key]


def build_og():
    """1200x630 share picture: logo on a winter-night card with snow dots."""
    import random
    W, H = 1200, 630
    card = Image.new("RGB", (W, H), (5, 11, 28))
    d = ImageDraw.Draw(card)
    for y in range(H):
        t = y / float(H)
        d.line([(0, y), (W, y)], fill=(int(10 + 22 * t), int(22 + 10 * t), int(62 + 26 * (1 - t))))
    rnd = random.Random(27)
    for _ in range(110):
        x, y, r = rnd.randint(0, W), rnd.randint(0, H), rnd.choice((1, 1, 2, 2, 3))
        d.ellipse((x - r, y - r, x + r, y + r), fill=(232, 244, 255))
    logo = Image.open(io.BytesIO(get_asset("logo")[0])).convert("RGBA")
    lh = 330
    lw = max(1, int(logo.width * lh / float(logo.height)))
    if lw > 760:
        lw, lh = 760, max(1, int(logo.height * 760 / float(logo.width)))
    logo = logo.resize((lw, lh), Image.LANCZOS)
    card.paste(logo, ((W - lw) // 2, 60), logo)
    try:
        f1 = ImageFont.load_default(size=70)
        f2 = ImageFont.load_default(size=34)
        d.text((W // 2, 438), "SeongEraStudy", font=f1, fill=(255, 255, 255), anchor="ma")
        d.text((W // 2, 530), "Education is free for everyone", font=f2, fill=(255, 207, 107), anchor="ma")
        d.text((W // 2, 580), "Merry Christmas & Happy New Year 2027", font=f2, fill=(191, 233, 255), anchor="ma")
    except Exception:
        pass
    out = io.BytesIO()
    card.save(out, "JPEG", quality=84, optimize=True, progressive=True)
    return out.getvalue(), "image/jpeg"


def image_response(getter, fallback_url):
    try:
        if Image is None:
            raise RuntimeError("Pillow missing")
        data, mime = getter()
        resp = Response(data, mimetype=mime)
        resp.headers["Cache-Control"] = CACHE_HDR
        return resp
    except Exception:
        resp = redirect(fallback_url, code=302)
        resp.headers["Cache-Control"] = "no-store"
        return resp


def base_url():
    if SITE_URL:
        return SITE_URL.rstrip("/")
    proto = request.headers.get("X-Forwarded-Proto", request.scheme).split(",")[0].strip()
    host = request.headers.get("X-Forwarded-Host", request.host).split(",")[0].strip()
    return proto + "://" + host


@app.route("/a/<name>")
def asset(name):
    key = name.rsplit(".", 1)[0]
    if key not in ASSETS:
        return Response("Not found", status=404)
    return image_response(lambda: get_asset(key), ASSETS[key]["url"])


@app.route("/og.jpg")
def og():
    def getter():
        if "og" not in _cache:
            _cache["og"] = build_og()
        return _cache["og"]
    return image_response(getter, LOGO_URL)


@app.route("/")
def home():
    return Response(PAGE.replace("{{BASE}}", base_url()), mimetype="text/html; charset=utf-8")


@app.route("/<path:_>")
def fallback(_):
    return Response(PAGE.replace("{{BASE}}", base_url()), mimetype="text/html; charset=utf-8")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

