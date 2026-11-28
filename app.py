# =====================================================
#  CONFIG  -  change links / media ONLY here, nowhere else
# =====================================================
PORTAL_LINK     = "http://seongxcollege.duckdns.org"
CHANNEL_LINK    = "https://t.me/SeongEraStudy"
WHATSAPP_CHANNEL_LINK = "https://whatsapp.com/channel/0029VbE8De8B4hdWhdsUoH0z"
OWNER_LINK      = "https://t.me/SeongEra"
OWNER_NAME      = "夔🌑 𝑺𝒆𝒐𝒏𝒈-𝒋𝒆 ⋆ 𝑂𝑓𝑓𝑙𝑖𝑛𝑒"

VIDEO_URL       = "https://huggingface.co/datasets/gopallikehack/Seong_Study/resolve/main/yzx-261128-l3dmrl.mp4"
OWNER_VIDEO_URL = "https://huggingface.co/datasets/gopallikehack/Seong_Study/resolve/main/a-261025-y6jc8x.mp4"

DEFAULT_LOGO_URL = "https://i.ibb.co/XxtXNBCW/file-00000000649482079925d320aeb3e88b.png"
LOGO_URL        = DEFAULT_LOGO_URL  # Change this value to use a different logo.
TREE_URL        = "https://i.ibb.co/nsrmkCn9/file-0000000077c48207807f7e09f0f8d150.png"
GIFTS_URL       = "https://i.ibb.co/Z0LjjGw/file-00000000cfe0820799c102c961ea1c5b.png"
SNOWMAN_URL     = "https://i.ibb.co/20kfKnLj/file-00000000755882079d6cb681905d59cb.png"
HAT_URL         = "https://i.ibb.co/gMfnHdn4/Note-GPT-Image-20261125084956.png"
SANTA_URL       = "https://i.ibb.co/svYsBz3H/file-000000002bbc81fa8962f73f04e212a8.png"
SNOWBG_URL      = "https://i.ibb.co/4gJQNThb/download.jpg"

# Set your public HTTPS homepage here or in the SITE_URL environment variable.
# Leave empty to use the origin of the incoming request.
SITE_URL        = ""
ASSET_VERSION   = "2"
SHARE_TITLE     = "SeongEraStudy | Free Study Portal"
SHARE_DESCRIPTION = "Open SeongEraStudy for free video lectures, notes, and practice. Education is free for everyone."
SHARE_IMAGE_ALT = "The SeongEraStudy logo on a snowy background with the words Education is free for everyone."
# Increase this when updating the preview image to give it a new URL.
SHARE_IMAGE_VERSION = "3"
# =====================================================

import base64
import io
import os
import html
import threading
import urllib.request
from urllib.parse import urlsplit

from flask import Flask, Response, redirect, request

try:
    from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont
except Exception:          # Pillow missing: site still works, images load from original links
    Image = None

app = Flask(__name__)

HTML = r"""<!DOCTYPE html>
<html lang="en" prefix="og: https://ogp.me/ns#">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SeongEraStudy · Merry Christmas &amp; Happy New Year 2027</title>
<meta name="description" content="{{SHARE_DESCRIPTION}}">
<meta name="theme-color" content="#050b1c">
<link rel="canonical" href="{{SHARE_URL}}">
<meta property="og:title" content="{{SHARE_TITLE}}">
<meta property="og:description" content="{{SHARE_DESCRIPTION}}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="SeongEraStudy">
<meta property="og:url" content="{{SHARE_URL}}">
<meta property="og:image" content="{{SHARE_IMAGE}}">
{{SHARE_SECURE_IMAGE}}
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{{SHARE_ALT}}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{{SHARE_TITLE}}">
<meta name="twitter:description" content="{{SHARE_DESCRIPTION}}">
<meta name="twitter:image" content="{{SHARE_IMAGE}}">
<meta name="twitter:image:alt" content="{{SHARE_ALT}}">
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
.sleigh{position:fixed;top:11%;left:0;z-index:-1;pointer-events:none;will-change:transform;transform:translate(-45vw,0);animation:fly 64s linear infinite;animation-delay:.5s}
.sleigh img{display:block;height:clamp(92px,17vw,180px);width:auto;transform:scaleX(var(--santa-flip,1));filter:drop-shadow(0 12px 18px rgba(0,0,0,.55)) drop-shadow(0 0 20px rgba(255,207,107,.4));animation:sbob 1.5s ease-in-out infinite}
@keyframes sbob{0%,100%{transform:translateY(0) scaleX(var(--santa-flip,1))}50%{transform:translateY(-9px) scaleX(var(--santa-flip,1))}}
@keyframes fly{0%{transform:translate(-45vw,0)}9%{transform:translate(140vw,-26px)}100%{transform:translate(140vw,-26px)}}

/* ---------- Nav ---------- */
.nav{position:fixed;top:42px;left:50%;transform:translateX(-50%);z-index:100;width:min(1000px,calc(100% - 28px));
  display:flex;align-items:center;justify-content:space-between;gap:14px;padding:10px 10px 10px 22px;border-radius:999px;
  background:rgba(7,16,38,.82);border:1px solid var(--edge)}
.logo{display:flex;align-items:center;gap:10px;font-family:var(--head);font-weight:900;font-size:1.1rem;letter-spacing:-.01em}
.lg{position:relative;flex:none;width:38px;height:38px;
  --hat-anchor-x:70%;--hat-anchor-y:12%;--hat-width:60%;--hat-tilt:10deg}
.lg img.mark{width:100%;height:100%;object-fit:contain;border-radius:11px;display:block}
/* The brim of HAT_URL is lower than the center of its transparent canvas. */
.santa-hat{
  --hat-brim-x:43%;--hat-brim-y:73%;
  position:absolute;z-index:1;display:block;left:var(--hat-anchor-x);top:var(--hat-anchor-y);
  width:var(--hat-width);height:auto;pointer-events:none;
  transform-origin:var(--hat-brim-x) var(--hat-brim-y);
  transform:translate(calc(0% - var(--hat-brim-x)),calc(0% - var(--hat-brim-y))) rotate(var(--hat-tilt));
  filter:drop-shadow(0 2px 3px rgba(0,0,0,.5))
}
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
.pill.hearth{
  color:#261916;background:linear-gradient(120deg,#fff0c9,#ffd28e 49%,#f7a875);
  border:1px solid #ffebc1;box-shadow:0 10px 30px -10px #f09b6aa6,inset 0 1px #fff7
}
.pill.hearth:hover{box-shadow:0 12px 36px -8px #ffb874b0,inset 0 1px #fff8}
.pill.hearth::after{animation-duration:6.4s}
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
.hero h1 em{font-style:normal;background:linear-gradient(120deg,#f0fcff,#9ce5ff,#c5bdff,#f0fcff);background-size:260% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:flow 8s linear infinite;text-shadow:none}
@keyframes flow{to{background-position:260% 0}}
.hero p.lead{margin-top:22px;max-width:50ch;font-size:clamp(1rem,1.7vw,1.2rem);color:var(--mut);text-shadow:0 2px 20px rgba(0,0,0,.8)}
.rot{display:inline-block;min-width:5.4em;font-weight:700;color:var(--ink);border-bottom:2px solid var(--red);transition:opacity .3s,transform .3s}
.rot.out{opacity:0;transform:translateY(6px)}
.row{display:flex;flex-wrap:wrap;justify-content:center;gap:14px;margin-top:34px}
.community-links{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;max-width:100%}
.community-links .ghost{white-space:nowrap}
.community-links svg{flex:none}
.ghost.whatsapp-link{border-color:#6cdeab66;color:#e0fff1}
.ghost.whatsapp-link svg{color:#75e5b0}
.ghost.whatsapp-link:hover{background:#184436;border-color:#75e5b0}

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
.faq p a{color:var(--ice);text-decoration:underline;text-underline-offset:.2em}

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

/* ---------- Winter landscape and welcome ---------- */
.gate{display:none}
.js .gate{
  position:fixed;inset:0;z-index:105;display:grid;place-items:center;padding:clamp(14px,4vw,28px);
  overflow:hidden auto;overscroll-behavior:contain;background:#060e21;
  transition:opacity .65s ease,visibility .65s,transform .65s cubic-bezier(.25,.7,.25,1)
}
.gate.out{opacity:0;visibility:hidden;transform:scale(1.08);pointer-events:none}
.winter-symbols{position:absolute;width:0;height:0;overflow:hidden;pointer-events:none}
.winter-sky,.winter-land{position:fixed;left:0;width:100%;pointer-events:none}
.winter-sky{top:0;height:100%}
.winter-land{bottom:0;height:clamp(195px,48vh,500px)}
.gate .sleigh{z-index:0}
.gate.out .sleigh{visibility:hidden}
.aurora{transform-box:fill-box;transform-origin:center;animation:aurora-drift 17s ease-in-out infinite alternate}
.aurora.secondary{animation-duration:23s;animation-direction:alternate-reverse}
@keyframes aurora-drift{
  from{opacity:.58;transform:translate(-25px,4px) rotate(-4deg) scaleY(.88)}
  to{opacity:.98;transform:translate(28px,-13px) rotate(4deg) scaleY(1.07)}
}
.winter-stars use{animation:starlight 4.8s ease-in-out infinite alternate}
.winter-stars use:nth-child(3n+1){animation-delay:-1.6s}
.winter-stars use:nth-child(3n+2){animation-delay:-3.2s}
@keyframes starlight{from{opacity:.25}to{opacity:.9}}
.lodge-light{animation:lodge-glow 5.5s ease-in-out infinite alternate}
@keyframes lodge-glow{from{opacity:.68}to{opacity:1}}
.chimney-smoke{transform-box:fill-box;transform-origin:center;animation:smoke-rise 6s linear infinite}
@keyframes smoke-rise{
  0%{opacity:0;transform:translate(0,5px) scale(.65)}
  22%{opacity:.36}
  100%{opacity:0;transform:translate(36px,-54px) scale(1.9)}
}
.intro-inner{
  position:relative;z-index:1;width:100%;max-width:482px;margin:auto;text-align:center;
  padding:clamp(22px,4.4vw,39px) clamp(18px,4.8vw,38px) clamp(18px,3.4vw,30px);
  border:1px solid #bbecff4a;border-radius:30px;
  background:radial-gradient(90% 65% at 50% 0%,#31678165,transparent 78%),linear-gradient(160deg,#152c46ee,#070f22f5 73%);
  box-shadow:0 28px 85px #020710ad,inset 0 1px 0 #e6faff33,0 0 58px #62cde616;
  transition:transform .6s cubic-bezier(.25,.7,.25,1),opacity .45s ease
}
.intro-inner::before{
  content:"";position:absolute;inset:0 12% auto;height:1px;pointer-events:none;
  background:linear-gradient(90deg,transparent,#d6f8ffbb,transparent)
}
.gate.out .intro-inner{transform:translateY(-10px) scale(.95);opacity:0}
.logo-wrap{position:relative;width:104px;height:104px;margin:0 auto 22px;animation:pop .85s cubic-bezier(.2,.9,.3,1.2) both}
@keyframes pop{from{opacity:0;transform:scale(.8) translateY(16px)}}
.logo-wrap::before{content:"";position:absolute;inset:-23px;border-radius:50%;background:radial-gradient(circle,#70dafa52,transparent 70%)}
.logo-wrap .lw{
  position:absolute;inset:0;border:1px solid #a2e4f89c;border-radius:25%;
  background:radial-gradient(circle at 50% 15%,#263c58,#0a152a 74%);display:grid;place-items:center;
  box-shadow:inset 0 1px 5px #c7f3ff40,0 6px 25px #0008
}
.logo-wrap img{width:86%;height:86%;object-fit:contain}
.frost-orbit{position:absolute;inset:-19%;width:138%;height:138%;overflow:visible;pointer-events:none}
.frost-orbit .orbit-trace{animation:orbit-trace 9s linear infinite}
.frost-orbit .orbit-stars{transform-origin:center;animation:rot 28s linear infinite}
@keyframes orbit-trace{to{stroke-dashoffset:-56}}
.i-script{font-family:var(--script);font-weight:700;font-size:clamp(1.35rem,4.4vw,1.95rem);color:#ffdda2;line-height:1.14;text-shadow:0 0 22px #ffb66452}
.i-title{margin-top:8px;font-family:var(--head);font-weight:900;font-size:clamp(1.7rem,8vw,3.05rem);line-height:1.06;letter-spacing:-.045em}
.i-title b{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.i-sub{margin-top:9px;color:var(--mut)}
.i-load{margin:17px auto 4px;max-width:245px}
.i-load .bar{height:3px;border-radius:5px;background:#dff6ff26;overflow:hidden}
.i-load .bar i{display:block;height:100%;width:6%;border-radius:5px;background:linear-gradient(90deg,#8fbdff,#ace9f7,#ffe1a8);transition:width .35s ease}
.i-load small{display:block;margin-top:7px;font-size:.65rem;letter-spacing:.13em;text-transform:uppercase;color:var(--mut)}
.i-btns{margin-top:17px}
.i-btns .pill{width:100%;max-width:340px;justify-content:center}
.skip{display:block;margin:10px auto 0;background:none;border:0;color:var(--mut);font:500 .92rem var(--body);cursor:pointer;text-decoration:underline;text-underline-offset:3px;padding:6px 10px}
.skip:hover{color:var(--ink)}
.tip{margin-top:12px;font-size:.78rem;color:#bfd6e9}
@keyframes iup{from{opacity:0;transform:translateY(14px)}}
.intro-inner > *:not(.logo-wrap){animation:iup .6s cubic-bezier(.2,.7,.2,1) both}
.intro-inner > :nth-child(2){animation-delay:.1s}
.intro-inner > :nth-child(3){animation-delay:.18s}
.intro-inner > :nth-child(4){animation-delay:.26s}
.intro-inner > :nth-child(5){animation-delay:.34s}
.intro-inner > :nth-child(6){animation-delay:.42s}
.intro-inner > :nth-child(7){animation-delay:.5s}
@media(max-height:560px),(max-width:400px) and (max-height:620px){
  .js .gate{padding:16px}
  .intro-inner{padding-block:17px}
  .logo-wrap{width:65px;height:65px;margin-bottom:14px}
  .i-script{font-size:clamp(1.25rem,4vw,1.6rem)}
  .i-title{font-size:clamp(1.9rem,7vw,2.6rem);line-height:1.1}
  .i-sub{margin-top:5px}
  .i-load,.i-btns{margin-top:10px}
  .i-btns .pill{padding-block:12px}
  .skip,.tip{margin-top:8px}
}
@media(max-height:415px) and (orientation:landscape){
  .intro-inner{display:grid;grid-template-columns:90px minmax(0,1fr);column-gap:16px;max-width:538px}
  .logo-wrap{grid-row:1 / span 5;place-self:center;margin:0}
  .intro-inner > :not(.logo-wrap){grid-column:2}
  .i-load{width:min(100%,245px)}
}
body.gated .nav,body.gated .music,body.gated .celeb,body.gated .bubble{opacity:0;pointer-events:none}
body.gated .hero > *{animation-play-state:paused}
.hint{margin-top:10px;font-size:.8rem;opacity:.65}

/* Ice at the outer edges leaves the video and portal controls visible. */
.hero > .hero-frost{position:absolute;inset:0;z-index:-1;overflow:hidden;pointer-events:none;opacity:1;transform:none;animation:none}
.hero-frost svg{position:absolute;width:clamp(68px,16vw,245px);color:#b1ebfa;opacity:.23;animation:drift-crystal 13s ease-in-out infinite alternate}
.hero-frost .frost-left{left:clamp(-58px,-2.8vw,-14px);top:19%}
.hero-frost .frost-right{right:clamp(-48px,-2vw,-10px);top:27%;width:clamp(65px,12vw,180px);opacity:.16;animation-delay:-5s}
@keyframes drift-crystal{from{transform:translateY(0) rotate(-12deg)}to{transform:translateY(28px) rotate(14deg)}}

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
.ocol .eyebrow{margin-bottom:clamp(50px,17vw,68px)}
.circle{position:relative;display:block;width:min(100%,300px,70vw);aspect-ratio:1;margin:0 auto;
  background:none;border:0;color:inherit;font:inherit;cursor:pointer;-webkit-tap-highlight-color:transparent;
  --hat-anchor-x:70%;--hat-anchor-y:9%;--hat-width:34%;--hat-tilt:14deg}
.circle:focus-visible{outline-offset:12px;border-radius:50%}
.circle::before{content:"";position:absolute;inset:-8px;border-radius:50%;background:conic-gradient(#ff3b52,#ffcf6b,#35d69a,#6fd0ff,#ff3b52);animation:rot 7s linear infinite}
.circle .disc{position:absolute;inset:0;border-radius:50%;overflow:hidden;background:#0a1228;border:4px solid var(--night);transition:transform .3s}
.circle video{width:100%;height:100%;object-fit:cover;display:block}
.circle .santa-hat{filter:drop-shadow(0 6px 8px rgba(0,0,0,.5))}
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

/* Winter edition 2: responsive editorial layout and accessible controls */
:root{--glass:rgba(12,26,49,.88);--edge:rgba(199,225,255,.22);--santa-flip:-1}
body{background:#050b1c} .bg{background:radial-gradient(ellipse at 75% 15%,#234c71,transparent 55%),#050b1c}
.nav{max-width:1180px;width:calc(100% - 32px);box-shadow:0 12px 40px #0005;backdrop-filter:blur(16px)}
.hero{isolation:isolate;overflow:hidden;padding-bottom:100px}.hero h1{max-width:13ch}.hero .lead{max-width:52ch}
.hero::before{content:"";position:absolute;inset:0;z-index:-1;background:radial-gradient(ellipse at center,#050b1c77,transparent 75%);pointer-events:none}
.treewrap{right:2vw;bottom:4vh;opacity:.8}.treewrap img{height:min(48vh,420px)}
.cd{box-shadow:0 12px 32px #0003;min-width:0}.cd div span{min-width:48px}.cds{gap:12px}
.card{background:linear-gradient(145deg,#172d49e8,#09162ce8);box-shadow:0 12px 30px #0002}.c1{background:radial-gradient(ellipse at top right,#235b56,transparent 65%),#10283d}.c2{background:linear-gradient(145deg,#34304b,#111d34)}.c3{background:linear-gradient(145deg,#48303e,#121e34)}
.gift{padding-right: min(36%,390px)}.gift .boxes{bottom:0;right:0}.steps{gap:16px;border:0}.step{padding:24px;border:1px solid var(--edge);border-radius:24px;background:var(--glass)}
.drawer{visibility:hidden}.open .drawer{visibility:visible}.toast{max-width:calc(100% - 24px);white-space:normal;text-align:center}.music{bottom:calc(16px + env(safe-area-inset-bottom));max-width:calc(100% - 90px)}
.tools{position:fixed;right:16px;bottom:88px;z-index:112;display:grid;gap:8px}.tools button{width:44px;height:44px;border-radius:50%;background:#101f38;color:white;border:1px solid var(--edge);cursor:pointer;font-size:18px}.tools button[aria-pressed=true]{border-color:var(--gold)}
body.gated .tools{display:none}.calm #snow,.calm .sleigh,.calm .lights,.calm .bg video,.calm .bg canvas{display:none}.calm *, .calm *::before,.calm *::after{animation:none!important;transition:none!important}.calm .hero>* , .calm .rv{opacity:1!important;transform:none!important}
.goaltrack{height:8px;background:#ffffff19;border-radius:20px;overflow:hidden;margin:12px 0}.goaltrack i{display:block;height:100%;width:0;background:var(--grad);transition:width .3s}.goalcount{font-size:.85rem;color:var(--ice)}
.skiplink{position:fixed;top:-100px;left:12px;z-index:300;background:#fff;color:#09162c;padding:12px}.skiplink:focus{top:12px}
@media(max-width:760px){.hero{padding:140px 16px 75px}.hero h1{font-size:clamp(2.6rem,10vw,4rem)}.nav{padding:8px 9px 8px 12px;gap:5px}.logo{font-size:.95rem;gap:6px}.nr{gap:5px}.nr .pill{padding:10px 12px;font-size:.75rem;white-space:nowrap}.lg{width:32px;height:32px}.cds{width:100%}.cd{width:min(100%,300px)}.gift{padding:30px 22px 30px 72px}.gift .boxes{width:100%}.tools{bottom:154px;right:12px}.card{padding:24px}.owner{padding:24px 18px}.lnk{padding:14px}.hero .row{gap:10px}.hero .row a{padding:14px 20px}.fsnow{max-height:125px}}
@media(max-width:560px){
  .hero .row{flex-direction:column;align-items:center;width:100%}
  .community-links{gap:8px}
  .hero .row .community-links .ghost{min-height:44px;gap:6px;padding:10px 12px;font-size:.86rem}
  .community-links .ghost svg{width:16px;height:16px}
}
@media(max-width:370px){
  .nav{width:calc(100% - 20px);padding-inline:8px}
  .logo{min-width:0;gap:5px;font-size:.8rem;letter-spacing:-.02em}
  .logo > span:last-child{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .nr{flex:none}
  .nr .pill{padding-inline:8px;font-size:.72rem}
  .cd div{gap:5px}.cd div span{min-width:43px}
}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important}.bg video,.bg canvas{display:none}}

</style>
</head>
<body>
<a class="skiplink" href="#top">Skip to content</a>

<svg class="winter-symbols" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">
  <defs>
    <path id="winter-flake-axis" d="M24 3v42M17 9l7 7 7-7M17 39l7-7 7 7"/>
    <symbol id="winter-flake" viewBox="0 0 48 48">
      <g fill="none" stroke="currentColor" stroke-width="1.25" stroke-linecap="round" stroke-linejoin="round">
        <use href="#winter-flake-axis"/>
        <use href="#winter-flake-axis" transform="rotate(60 24 24)"/>
        <use href="#winter-flake-axis" transform="rotate(120 24 24)"/>
        <path d="m24 19 4.3 2.5v5L24 29l-4.3-2.5v-5Z"/>
      </g>
    </symbol>
    <symbol id="winter-star" viewBox="0 0 20 20">
      <path fill="currentColor" d="M10 0Q11 9 20 10Q11 11 10 20Q9 11 0 10Q9 9 10 0Z"/>
    </symbol>
    <symbol id="winter-pine" viewBox="0 0 64 96">
      <path fill="currentColor" d="M32 2 11 32h10L5 52h12L0 76h29v18h6V76h29L47 52h12L43 32h10Z"/>
      <path fill="#a6cddd" opacity=".39" d="m32 2-17 24 9-3 8-14 10 16 7 2Zm-11 30L9 48l12-5 11 2 12-2 10 5-11-16-11 6ZM17 52 4 71l16-5 12 2 12-2 16 5-13-19-15 8Z"/>
    </symbol>
  </defs>
</svg>

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
  <svg class="winter-sky" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">
    <defs>
      <linearGradient id="winter-night" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0" stop-color="#060c20"/>
        <stop offset=".56" stop-color="#152848"/>
        <stop offset="1" stop-color="#2d5063"/>
      </linearGradient>
      <radialGradient id="winter-moon-halo">
        <stop offset="0" stop-color="#c4f5ff" stop-opacity=".39"/>
        <stop offset=".26" stop-color="#9bdcfd" stop-opacity=".23"/>
        <stop offset="1" stop-color="#6883dc" stop-opacity="0"/>
      </radialGradient>
      <linearGradient id="winter-aurora-mint" x1=".12" x2=".8" y1="0" y2="1">
        <stop offset="0" stop-color="#7887d8" stop-opacity="0"/>
        <stop offset=".55" stop-color="#709ce9" stop-opacity=".17"/>
        <stop offset=".83" stop-color="#9afde5" stop-opacity=".62"/>
        <stop offset="1" stop-color="#5ce7eb" stop-opacity="0"/>
      </linearGradient>
      <linearGradient id="winter-aurora-violet" x1="0" y1="0" x2=".62" y2="1">
        <stop offset="0" stop-color="#9893f8" stop-opacity="0"/>
        <stop offset=".67" stop-color="#9e93ed" stop-opacity=".46"/>
        <stop offset="1" stop-color="#52bbdf" stop-opacity="0"/>
      </linearGradient>
    </defs>
    <rect width="1600" height="900" fill="url(#winter-night)"/>
    <g class="aurora secondary">
      <path d="M-96 242C164 168 335 100 591 177S965 372 1205 218s306-203 509-198L1674 125c-232 9-330 180-520 210-236 39-444-95-635-107-218-15-371 71-615 115Z" fill="url(#winter-aurora-violet)"/>
    </g>
    <g class="aurora">
      <path d="M-86 148C177 260 306 267 501 209S810 78 1017 159s375 63 664-66l30 83c-274 178-501 193-714 103S718 184 511 281 98 359-109 289Z" fill="url(#winter-aurora-mint)"/>
      <path d="M-50 275C188 352 343 340 524 257S797 152 991 238s429 123 671-53" fill="none" stroke="#88e4e8" stroke-opacity=".19" stroke-width="2"/>
      <path d="M-21 283C206 341 333 341 501 272S765 167 958 235s319 138 683-21" fill="none" stroke="#a7dde9" stroke-opacity=".13"/>
    </g>
    <circle cx="1034" cy="136" r="169" fill="url(#winter-moon-halo)"/>
    <path fill="#dff6ff" d="M1048 107a28 28 0 1 0 19 43 26 26 0 0 1-19-43Z"/>
    <g class="winter-stars" color="#e3f9ff">
      <use href="#winter-star" x="154" y="122" width="8" height="8"/>
      <use href="#winter-star" x="305" y="86" width="15" height="15"/>
      <use href="#winter-star" x="432" y="145" width="9" height="9"/>
      <use href="#winter-star" x="532" y="61" width="6" height="6"/>
      <use href="#winter-star" x="650" y="132" width="11" height="11"/>
      <use href="#winter-star" x="741" y="79" width="8" height="8"/>
      <use href="#winter-star" x="897" y="102" width="13" height="13"/>
      <use href="#winter-star" x="978" y="62" width="7" height="7"/>
      <use href="#winter-star" x="1138" y="118" width="9" height="9"/>
      <use href="#winter-star" x="1221" y="85" width="5" height="5"/>
      <use href="#winter-star" x="1317" y="157" width="16" height="16"/>
      <use href="#winter-star" x="1497" y="74" width="8" height="8"/>
    </g>
  </svg>

  <svg class="winter-land" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 520" preserveAspectRatio="xMinYMax slice" aria-hidden="true" focusable="false">
    <defs>
      <linearGradient id="winter-ridge" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0" stop-color="#567192"/>
        <stop offset="1" stop-color="#213853"/>
      </linearGradient>
      <linearGradient id="winter-snowbank" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0" stop-color="#81a6c0"/>
        <stop offset="1" stop-color="#2d4b64"/>
      </linearGradient>
      <radialGradient id="winter-hearth-glow">
        <stop offset="0" stop-color="#ffd193" stop-opacity=".46"/>
        <stop offset="1" stop-color="#ffb671" stop-opacity="0"/>
      </radialGradient>
    </defs>
    <path d="M0 356 157 245 237 273 422 124 568 250 676 182 779 308 926 208 1041 312 1188 139 1323 265 1438 204 1600 323v197H0Z" fill="url(#winter-ridge)"/>
    <path d="m157 245-57 40 55-13 29 14 18-18Zm265-121L295 226l90-32 38 19 35-30 44 10Zm254 58-62 40 48-9 26 17 27-7Zm250 26-61 41 48-9 23 12 30-8Zm262-69-96 113 64-40 32 19 30-36 43 12Zm250 65-63 34 44-3 38 12 28-11Z" fill="#c1ddec" opacity=".61"/>
    <path d="M0 382 108 340 211 369 366 273 487 329 591 306 797 378 959 292 1042 327 1194 285 1304 363 1470 313 1600 365v155H0Z" fill="#223c56"/>
    <path d="M0 439c150-35 287-17 470-49s359 5 529 9 371-28 601-11v132H0Z" fill="#314e65"/>
    <g color="#29475c" opacity=".84">
      <use href="#winter-pine" x="75" y="350" width="49" height="74"/>
      <use href="#winter-pine" x="134" y="336" width="57" height="86"/>
      <use href="#winter-pine" x="184" y="356" width="44" height="66"/>
      <use href="#winter-pine" x="470" y="340" width="51" height="77"/>
      <use href="#winter-pine" x="535" y="320" width="61" height="92"/>
      <use href="#winter-pine" x="1102" y="314" width="65" height="98"/>
      <use href="#winter-pine" x="1160" y="345" width="48" height="72"/>
      <use href="#winter-pine" x="1350" y="312" width="65" height="98"/>
      <use href="#winter-pine" x="1423" y="308" width="74" height="111"/>
      <use href="#winter-pine" x="1501" y="348" width="52" height="78"/>
    </g>
    <path d="M0 462c211-22 300-42 488-32 211 12 320 36 495 16 124-14 236-49 355-40 103 7 180 28 262 22v92H0Z" fill="url(#winter-snowbank)"/>
    <g transform="translate(243 343)">
      <ellipse class="lodge-light" cx="97" cy="141" rx="124" ry="46" fill="url(#winter-hearth-glow)"/>
      <g fill="#cfdfed" opacity=".55">
        <ellipse class="chimney-smoke" cx="139" cy="10" rx="11" ry="5"/>
        <ellipse class="chimney-smoke" cx="139" cy="8" rx="9" ry="4" style="animation-delay:-2s"/>
        <ellipse class="chimney-smoke" cx="141" cy="6" rx="8" ry="4" style="animation-delay:-4s"/>
      </g>
      <path d="M128 17h21v51h-21Z" fill="#304759"/>
      <path d="M125 17h27" stroke="#cce3ee" stroke-width="6" stroke-linecap="round"/>
      <path d="M26 79 97 37l72 42v66H26Z" fill="#27394a" stroke="#14273a" stroke-width="2"/>
      <path d="M29 96h137M29 110h137M29 124h137M29 138h137" stroke="#758798" stroke-opacity=".24" stroke-width="2"/>
      <path d="m18 84 79-48 80 48" fill="none" stroke="#142537" stroke-width="15" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="m18 76 79-48 80 48" fill="none" stroke="#e0f1f5" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M82 145v-38q0-4 4-4h22q4 0 4 4v38Z" fill="#162637"/>
      <g class="lodge-light" fill="#ffd58f">
        <rect x="42" y="94" width="28" height="25" rx="2"/>
        <rect x="124" y="94" width="28" height="25" rx="2"/>
        <circle cx="97" cy="71" r="9"/>
        <path d="M96 122h3v3h-3Z"/>
      </g>
      <path d="M56 94v25m-14-13h28m68-12v25m-14-13h28M97 63v16m-8-8h16" fill="none" stroke="#926752" stroke-width="2"/>
      <path d="M23 147q28-9 60-4t90 1" fill="none" stroke="#c8e1ed" stroke-width="5" stroke-linecap="round" opacity=".7"/>
    </g>
    <g color="#183446">
      <use href="#winter-pine" x="-35" y="273" width="139" height="209"/>
      <use href="#winter-pine" x="64" y="353" width="86" height="129"/>
      <use href="#winter-pine" x="437" y="343" width="91" height="137"/>
      <use href="#winter-pine" x="1495" y="271" width="147" height="220"/>
    </g>
    <path d="M0 508c204-34 313-1 529 0 197 1 354-25 520-28s340 24 551 5v35H0Z" fill="#53768d"/>
  </svg>

  <div class="sleigh" aria-hidden="true"><img src="{{SANTA}}" alt="" width="260" height="170" decoding="async"></div>

  <div class="intro-inner">
    <div class="logo-wrap">
      <div class="lw"><img src="{{LOGO}}" alt="" width="90" height="90"></div>
      <svg class="frost-orbit" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" aria-hidden="true" focusable="false">
        <circle cx="80" cy="80" r="73" fill="none" stroke="#7fd6f5" stroke-opacity=".32"/>
        <circle class="orbit-trace" cx="80" cy="80" r="73" fill="none" stroke="#c1f1ff" stroke-width="1.35" stroke-dasharray="8 48" stroke-linecap="round"/>
        <g class="orbit-stars" color="#deeffd">
          <use href="#winter-flake" x="18" y="11" width="24" height="24"/>
          <use href="#winter-star" x="127" y="118" width="14" height="14"/>
          <use href="#winter-star" x="134" y="35" width="7" height="7"/>
        </g>
      </svg>
    </div>
    <div class="i-script">Merry Christmas &amp; Happy New Year 2027</div>
    <div class="i-title">Seong<b>Era</b>Study</div>
    <p class="i-sub">Education is free for everyone.</p>
    <div class="i-load"><div class="bar"><i id="ibar"></i></div><small id="istat">Preparing the magic…</small></div>
    <div class="i-btns">
      <button class="pill big hearth" id="gOn" type="button">🎶 Enter with music</button>
      <button class="skip" id="gOff" type="button">Enter without sound</button>
    </div>
    <div class="tip">Tip: double-tap anywhere to turn the music on or off.</div>
  </div>
</div>

<nav class="nav">
  <a class="logo" href="#top" aria-label="SeongEraStudy home">
    <span class="lg">
      <img class="mark" src="{{LOGO}}" alt="" width="38" height="38">
      <img class="santa-hat" src="{{HAT}}" alt="" width="360" height="640" decoding="async">
    </span>
    <span>Seong<b>Era</b>Study</span>
  </a>
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
      <a class="pill big hearth" href="{{PORTAL}}" target="_blank" rel="noopener">
        Open the portal
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
      </a>
      <div class="community-links">
        <a class="ghost" href="{{CHANNEL}}" target="_blank" rel="noopener" aria-label="@SeongEraStudy on Telegram">
          <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false"><path d="M21.9 4.3 18.7 19.4c-.2 1-.9 1.3-1.7.8l-4.7-3.5-2.3 2.2c-.3.3-.5.5-1 .5l.3-4.8 8.7-7.9c.4-.3-.1-.5-.6-.2L6.6 13 2 11.6c-1-.3-1-1 .2-1.5L20.2 3.2c.8-.3 1.6.2 1.7 1.1Z"/></svg>
          @SeongEraStudy
        </a>
        <a class="ghost whatsapp-link" href="{{WHATSAPP}}" target="_blank" rel="noopener" aria-label="WhatsApp channel for Seong Era Study">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">
            <path d="M20.5 11.5a8.5 8.5 0 0 1-12.4 7.55L3 20.5l1.4-5.07A8.5 8.5 0 1 1 20.5 11.5Z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/>
            <path d="M9 7.6c.3-.3.7-.2.9.2l1 1.8c.13.3.08.59-.14.82l-.66.63c.66 1.22 1.6 2.15 2.82 2.79l.62-.65c.23-.22.57-.27.84-.1l1.78.99c.4.2.49.6.2.91-.65.79-1.66 1.18-2.63.92-2.58-.67-5.03-3.05-5.65-5.63-.27-.99.08-1.98.92-2.68Z" fill="currentColor"/>
          </svg>
          WhatsApp
        </a>
      </div>
    </div>
    <div class="cds">
      <div class="cd"><h4>Christmas in</h4><div id="cdx"></div></div>
      <div class="cd"><h4>New Year 2027 in</h4><div id="cdn"></div></div>
    </div>
    <div class="scroll" aria-hidden="true"></div>
    <div class="treewrap" aria-hidden="true"><img src="{{TREE}}" alt="" width="480" height="480" decoding="async"></div>
    <div class="hero-frost" aria-hidden="true">
      <svg class="frost-left" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" focusable="false">
        <use href="#winter-flake" x="4" y="4" width="92" height="92"/>
        <use href="#winter-star" x="82" y="12" width="10" height="10"/>
      </svg>
      <svg class="frost-right" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" focusable="false">
        <use href="#winter-flake" x="16" y="10" width="80" height="80"/>
        <use href="#winter-star" x="9" y="72" width="12" height="12"/>
      </svg>
    </div>
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
        <p class="s">Tick them off. Finish all four for a surprise.</p><div class="goalcount" id="goalcount" role="status"></div><div class="goaltrack" aria-hidden="true"><i id="goalbar"></i></div>
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
        <details class="rv">
          <summary>How do I get updates?</summary>
          <p>Follow Seong Era Study on <a href="{{WHATSAPP}}" target="_blank" rel="noopener">WhatsApp</a> or <a href="{{CHANNEL}}" target="_blank" rel="noopener">Telegram</a>.</p>
        </details>
        <details class="rv"><summary>Who do I contact for help?</summary><p>Message the owner @SeongEra on Telegram.</p></details>
      </div>
    </div>
  </section>

  <section id="owner">
    <div class="wrap">
      <div class="owner rv">
        <div class="ocol">
          <div class="eyebrow">Owner</div>
          <button class="circle" id="circle" type="button" aria-label="Owner video sound" aria-pressed="false">
            <span class="disc"><video id="ov" muted loop playsinline preload="none" data-src="{{OVIDEO}}"></video></span>
            <img class="santa-hat" src="{{HAT}}" alt="" width="360" height="640" loading="lazy" decoding="async">
            <span class="cbtn"><span class="eq" aria-hidden="true"><i></i><i></i><i></i><i></i></span><b id="cl">Tap for sound</b></span>
          </button>
          <h2>{{OWNER_NAME}}</h2>
          <p class="role">Founder of SeongEraStudy. Made by Seong Gium Jee.</p>
          <p class="hint">Every video has its own sound. Playing one stops the other.</p>
        </div>
        <div class="links2">
          <a class="lnk" href="{{OWNER}}" target="_blank" rel="noopener"><span><small>Owner on Telegram</small><strong>@SeongEra</strong></span><span>→</span></a>
          <a class="lnk" href="{{CHANNEL}}" target="_blank" rel="noopener"><span><small>Telegram channel</small><strong>@SeongEraStudy</strong></span><span>→</span></a>
          <a class="lnk" href="{{WHATSAPP}}" target="_blank" rel="noopener">
            <span><small>WhatsApp channel</small><strong>Seong Era Study</strong></span><span aria-hidden="true">→</span>
          </a>
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

<div class="tools"><button id="calm" type="button" aria-label="Reduce visual effects" aria-pressed="false" title="Reduce effects">❄</button><button id="share" type="button" aria-label="Share website" title="Share website">↗</button><button id="backtop" type="button" aria-label="Back to top" title="Back to top">↑</button></div>
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
  var motion=window.matchMedia('(prefers-reduced-motion: reduce)'), reduce=motion.matches;
  var fine=window.matchMedia('(hover:hover) and (pointer:fine)').matches;
  function safe(p){ if(p&&p.catch)p.catch(function(){}); }

  /* ================= VIDEO + FILL ================= */
  var v=$('bgf'), fl=$('fill'), fx=fl.getContext('2d'), b=$('snd'), l=$('sndl'), fillTimer=null;
  function paint(){ try{ fx.drawImage(v,0,0,fl.width,fl.height); }catch(e){} }
  function startFill(){ if(!fillTimer && !document.body.classList.contains("calm")){ fillTimer=setInterval(paint,110); } }
  function stopFill(){ clearInterval(fillTimer); fillTimer=null; }

  /* ================= SNOW + FIREWORKS ================= */
  var sc=$('snow'), sx=sc.getContext('2d'), W=0,H=0, flakes=[], sparks=[];
  var wind=0, windGoal=0, tw=0, raf=0, lastFrame=0, running=false;

  // One soft sprite gives nearby flakes depth without blurring the whole canvas.
  var softFlake=document.createElement('canvas');
  softFlake.width=softFlake.height=40;
  var sf=softFlake.getContext('2d'), snowFade=sf.createRadialGradient(20,20,0,20,20,20);
  snowFade.addColorStop(0,'rgba(243,253,255,.94)');
  snowFade.addColorStop(.32,'rgba(218,243,255,.73)');
  snowFade.addColorStop(.66,'rgba(182,222,249,.24)');
  snowFade.addColorStop(1,'rgba(182,222,249,0)');
  sf.fillStyle=snowFade;
  sf.fillRect(0,0,40,40);

  function mk(init){
    var depth=Math.random(), near=depth>.82;
    return {
      x:Math.random()*W,y:init?Math.random()*H:-12,depth:depth,near:near,
      r:near?4+depth*4:.65+depth*2.2,vy:.26+depth*1.6,
      ph:Math.random()*2*Math.PI,a:.38+depth*.44
    };
  }
  function size(){
    var dpr=Math.min(window.devicePixelRatio||1,1.5);
    W=window.innerWidth; H=window.innerHeight;
    sc.width=W*dpr; sc.height=H*dpr; sx.setTransform(dpr,0,0,dpr,0,0);
    var n=Math.round(Math.min(W*H/8200,fine?155:72));
    while(flakes.length<n){ flakes.push(mk(true)); }
    flakes.length=n;
  }
  function frame(now){
    raf=requestAnimationFrame(frame);
    var step=lastFrame?Math.min(2.5,(now-lastFrame)/(1000/60)):1;
    lastFrame=now;
    sx.clearRect(0,0,W,H);
    tw+=.017*step;
    wind+=(windGoal-wind)*.04*step;
    sx.fillStyle='#e1f4ff';
    for(var i=0;i<flakes.length;i++){
      var f=flakes[i];
      f.y+=f.vy*step;
      f.x+=(Math.sin(tw+f.ph)*(.16+f.depth*.62)+wind*f.depth*.8+.14)*step;
      if(f.y>H+12){ f.y=-12; f.x=Math.random()*W; }
      if(f.x>W+12){ f.x=-12; } else if(f.x<-12){ f.x=W+12; }
      sx.globalAlpha=f.a;
      if(f.near){
        sx.drawImage(softFlake,f.x-f.r,f.y-f.r,2*f.r,2*f.r);
      } else {
        sx.beginPath(); sx.arc(f.x,f.y,f.r,0,2*Math.PI); sx.fill();
      }
    }
    var drag=Math.pow(.985,step);
    for(var j=sparks.length-1;j>=0;j--){
      var p=sparks[j];
      p.vx*=drag; p.vy=p.vy*drag+p.g*step; p.x+=p.vx*step; p.y+=p.vy*step; p.life-=step;
      if(p.life<=0){ sparks[j]=sparks[sparks.length-1]; sparks.pop(); continue; }
      sx.globalAlpha=Math.min(1,p.life/p.max*1.4);
      sx.fillStyle=p.c;
      sx.beginPath(); sx.arc(p.x,p.y,p.s,0,6.283); sx.fill();
    }
    sx.globalAlpha=1;
  }
  function startSnow(){ if(!running && !reduce && !document.body.classList.contains("calm")){ running=true; raf=requestAnimationFrame(frame); } }
  function stopSnow(){
    running=false;
    cancelAnimationFrame(raf);
    lastFrame=0;
    sparks.length=0;
    sx.clearRect(0,0,W,H);
  }
  size(); window.addEventListener('resize',size);

  var cols=['#ffcf6b','#ff5468','#bfe9ff','#ffffff','#5cf2b0'];
  function burst(x,y,n,color){
    if(!running||sparks.length>520){ return; }
    var c=color||cols[(Math.random()*cols.length)|0];
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
    if(reduce||document.body.classList.contains("calm")){toast("Happy New Year 2027!");return;}
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
    if(!fine||reduce||document.body.classList.contains("calm")){ return; }
    windGoal=((e.clientX/W)-.5)*1.4;
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
  var sub=$('sndsub'), circle=$('circle'), cl=$('cl'), bub=$('bubble'), bubN=0, bubT=0;
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
    circle.setAttribute('aria-pressed',owOn);
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
  circle.addEventListener('click',flipOwner);
  setTimeout(showBubble,4500); setInterval(showBubble,35000);

  /* gestures: double-tap / double-click anywhere, or press M (background music) */
  function inter(t){ return t&&t.closest&&t.closest('a,button,input,label,summary,details,.gate'); }
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
      if(ovVis){ ovReady(); }
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
  var glogo=document.querySelector('#gate .lw img');
  if(!glogo||glogo.complete){ step(); } else { glogo.addEventListener('load',step); glogo.addEventListener('error',step); }
  if(document.readyState==='complete'){ step(); } else { window.addEventListener('load',step); }
  setTimeout(function(){ if(ibar){ ibar.style.width='100%'; } if(istat){ istat.textContent='Ready'; } },2600);

  var gate=$('gate');
  function closeGate(){
    if(!gate){ return; }
    var g=gate; gate=null;
    if(running){
      var emblem=g.querySelector('.logo-wrap').getBoundingClientRect();
      burst(emblem.left+emblem.width/2,emblem.top+emblem.height/2,36,'#b6eaff');
    }
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
    if(reduce||document.body.classList.contains('calm')){ return; }
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

  /* Additional controls and saved preferences */
  var calm=$('calm'), quiet=false;
  try { quiet=localStorage.getItem('sx-calm')==='1'; } catch(e){}
  function applyCalm(){
    var effectsOff=reduce||quiet;
    document.body.classList.toggle('calm',effectsOff);
    calm.setAttribute('aria-pressed',String(effectsOff));
    if(effectsOff){ stopSnow(); stopFill(); } else if(!document.hidden){ startSnow(); startFill(); }
  }
  calm.addEventListener('click',function(){
    if(reduce){ toast('Reduced motion is on in your device settings'); return; }
    quiet=!quiet;
    try{localStorage.setItem('sx-calm',quiet?'1':'0');}catch(e){}
    applyCalm();
    toast(quiet?'Reduced effects enabled':'Festive effects enabled');
  });
  if(motion.addEventListener){
    motion.addEventListener('change',function(e){ reduce=e.matches; applyCalm(); });
  }
  applyCalm();
  $('backtop').addEventListener('click',function(){window.scrollTo({top:0,behavior:(reduce||quiet)?'auto':'smooth'});});
  $('share').addEventListener('click',async function(){
    var url=document.querySelector('link[rel="canonical"]').href;
    var title=document.querySelector('meta[property="og:title"]').content;
    if(navigator.share){
      try{ await navigator.share({title:title,url:url}); return; }
      catch(e){ if(e.name==='AbortError'){ return; } }
    }
    if(navigator.clipboard){
      try{ await navigator.clipboard.writeText(url); toast('Link copied'); return; }
      catch(e){}
    }
    window.prompt('Copy this link',url);
  });
  function goalProgress(){var n=Array.from(rs).filter(function(x){return x.checked;}).length;$('goalcount').textContent=n+' of '+rs.length+' goals completed';$('goalbar').style.width=(n/rs.length*100)+'%';}
  rs.forEach(function(x){x.addEventListener('change',goalProgress);});goalProgress();
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
        .replace("{{WHATSAPP}}", html.escape(WHATSAPP_CHANNEL_LINK, quote=True))
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
        .replace("{{SHARE_TITLE}}", html.escape(SHARE_TITLE, quote=True))
        .replace("{{SHARE_DESCRIPTION}}", html.escape(SHARE_DESCRIPTION, quote=True))
        .replace("{{SHARE_ALT}}", html.escape(SHARE_IMAGE_ALT, quote=True))
)

# ---------------------------------------------------------------
#  Image helper: resizes big pictures (faster site), removes a
#  white / checkerboard background if one is baked in. Results
#  are cached, including share previews generated for custom logos.
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
_locks = {key: threading.Lock() for key in ASSETS}
_og_lock = threading.Lock()


def fetch(url, timeout=9):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (SeongEraStudy asset loader)"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = r.read(16 * 1024 * 1024 + 1)
        if len(data) > 16 * 1024 * 1024:
            raise ValueError("Asset exceeds size limit")
        return data


def remove_bg(im, limit=640):
    """Make a light (white / checkerboard) outer background transparent.
    Only touches pixels connected to the picture edge, so white fur, snow
    and highlights inside the artwork stay. Already-transparent images are untouched."""
    im = im.convert("RGBA")
    w, h = im.size
    corners = [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]
    alpha = im.getchannel("A")
    if alpha.getextrema()[0] < 16:
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
    with _locks[key]:
        if key not in _cache:
            _cache[key] = build_asset(key)
        return _cache[key]


def build_og():
    """Build a 1200×630 preview when the site uses a custom logo."""
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
    return out.getvalue()


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


@app.after_request
def security_headers(response):
    response.headers.setdefault("X-Content-Type-Options", "nosniff")
    response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
    response.headers.setdefault("X-Frame-Options", "DENY")
    return response


@app.get("/healthz")
def health():
    return {"status": "ok", "version": ASSET_VERSION}


def base_url():
    configured = (os.environ.get("SITE_URL") or SITE_URL).strip().rstrip("/")
    if configured:
        try:
            public_url = urlsplit(configured)
            if (public_url.scheme in ("http", "https") and public_url.hostname
                    and public_url.username is None and not (public_url.query or public_url.fragment)):
                return configured
        except ValueError:
            pass
    # Only the scheme comes from the proxy. The host comes from this request.
    forwarded = request.headers.get("X-Forwarded-Proto", "").rsplit(",", 1)[-1].strip().lower()
    scheme = "https" if request.is_secure or forwarded == "https" else "http"
    return f"{scheme}://{request.host}{request.script_root}"


@app.route("/a/<name>")
def asset(name):
    key = name.rsplit(".", 1)[0]
    if key not in ASSETS:
        return Response("Not found", status=404)
    return image_response(lambda: get_asset(key), ASSETS[key]["url"])


@app.route("/og.jpg")
def og():
    picture = _DEFAULT_SHARE_JPEG
    max_age = 86400
    if Image is not None and LOGO_URL != DEFAULT_LOGO_URL:
        try:
            with _og_lock:
                if "og" not in _cache:
                    _cache["og"] = build_og()
                picture = _cache["og"]
        except Exception:
            # Keep serving a usable card if the custom logo host is unavailable.
            max_age = 60
    response = Response(picture, mimetype="image/jpeg")
    response.cache_control.public = True
    response.cache_control.max_age = max_age
    response.add_etag()
    return response.make_conditional(request)


@app.route("/")
def home():
    canonical = base_url() + "/"
    image_url = html.escape(f"{canonical}og.jpg?v={SHARE_IMAGE_VERSION}", quote=True)
    secure_tag = ""
    if canonical.startswith("https://"):
        secure_tag = f'<meta property="og:image:secure_url" content="{image_url}">'
    page = (PAGE.replace("{{SHARE_URL}}", html.escape(canonical, quote=True))
            .replace("{{SHARE_IMAGE}}", image_url)
            .replace("{{SHARE_SECURE_IMAGE}}", secure_tag))
    response = Response(page, mimetype="text/html")
    response.vary.add("X-Forwarded-Proto")
    return response


@app.route("/<path:_>")
def fallback(_):
    return Response("Page not found", status=404, mimetype="text/plain")


# Embedded 1200×630 JPEG for the default logo. The crawler can fetch it even
# when Pillow or the remote logo host is unavailable.
_DEFAULT_SHARE_JPEG = base64.b64decode(b"""
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
""")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))

