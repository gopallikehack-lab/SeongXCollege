# =====================================================
#  CONFIG  -  change links ONLY here, nowhere else
# =====================================================
PORTAL_LINK  = "http://seongxcollege.duckdns.org"
VIDEO_URL    = "https://huggingface.co/datasets/gopallikehack/Seong_Study/resolve/main/n-261124-kcctgu.mp4"
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
<title>SeongEraStudy · Merry Christmas &amp; Happy New Year 2027</title>
<meta name="description" content="SeongEraStudy is a free study portal for every student. Education is free for everyone. Merry Christmas and Happy New Year 2027! Made by Seong Gium Jee.">
<meta name="theme-color" content="#050b1c">
<meta property="og:title" content="SeongEraStudy · Education is free for everyone">
<meta property="og:description" content="Merry Christmas and Happy New Year 2027 from SeongEraStudy.">
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
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;scroll-padding-top:100px}
body{background:var(--night);color:var(--ink);font-family:var(--body);font-size:17px;line-height:1.6;-webkit-font-smoothing:antialiased;overflow-x:hidden}
body.open{overflow:hidden}
a{color:inherit;text-decoration:none}
:focus-visible{outline:2px solid var(--gold);outline-offset:3px;border-radius:8px}
::selection{background:var(--red);color:#fff}

/* ---------- Loader ---------- */
#loader{display:none}
.js #loader{position:fixed;inset:0;z-index:300;display:grid;place-items:center;align-content:center;gap:20px;background:radial-gradient(80% 60% at 50% 40%,#10234d,var(--night));transition:opacity .7s ease,visibility .7s}
#loader.done{opacity:0;visibility:hidden}
#loader .flake{font-size:3.4rem;animation:rot 3s linear infinite;filter:drop-shadow(0 0 14px rgba(191,233,255,.8))}
#loader b{font-family:var(--head);font-weight:900;font-size:1.4rem}
#loader small{color:var(--mut);font-size:.9rem;letter-spacing:.12em;text-transform:uppercase}
@keyframes rot{to{transform:rotate(360deg)}}

/* ---------- Backdrop ---------- */
.bg{position:fixed;inset:0;z-index:-3;background:radial-gradient(90% 70% at 70% 10%,#14306a 0%,var(--night) 70%);overflow:hidden}
.bg canvas{position:absolute;inset:0;width:100%;height:100%;z-index:1;opacity:.72}
.bg video{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;z-index:2;transform:translateZ(0);will-change:transform;backface-visibility:hidden}
.shade{position:fixed;inset:0;z-index:-2;pointer-events:none;
  background:
    radial-gradient(75% 65% at 50% 42%,rgba(5,11,28,.12),rgba(5,11,28,.66) 100%),
    linear-gradient(180deg,rgba(5,11,28,.55),rgba(5,11,28,.08) 32%,rgba(5,11,28,.9) 100%)}
#snow{position:fixed;inset:0;width:100%;height:100%;z-index:90;pointer-events:none}
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

/* ---------- Santa flyby ---------- */
.sleigh{position:fixed;top:15%;left:0;z-index:80;font-size:2.2rem;pointer-events:none;white-space:nowrap;animation:fly 70s linear infinite;animation-delay:6s;transform:translateX(-30vw);filter:drop-shadow(0 4px 10px rgba(0,0,0,.5))}
@keyframes fly{0%{transform:translate(-30vw,0)}6%{transform:translate(55vw,-28px)}12%,100%{transform:translate(125vw,10px)}}

/* ---------- Nav ---------- */
.nav{position:fixed;top:42px;left:50%;transform:translateX(-50%);z-index:100;width:min(1000px,calc(100% - 28px));
  display:flex;align-items:center;justify-content:space-between;gap:14px;padding:10px 10px 10px 22px;border-radius:999px;
  background:rgba(7,16,38,.82);border:1px solid var(--edge)}
.logo{font-family:var(--head);font-weight:900;font-size:1.1rem;letter-spacing:-.01em}
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
.sound{position:fixed;left:50%;bottom:20px;transform:translateX(-50%);z-index:110;display:flex;align-items:center;gap:12px;padding:12px 22px 12px 16px;border-radius:999px;
  background:rgba(7,16,38,.86);border:1px solid var(--edge);color:var(--ink);font:600 .88rem var(--body);cursor:pointer;transition:border-color .2s,transform .2s,background .2s}
.sound:hover{border-color:rgba(255,255,255,.4);transform:translateX(-50%) translateY(-2px)}
.sound[aria-pressed="true"]{border-color:var(--red);background:rgba(232,40,63,.3)}
.eq{display:flex;align-items:flex-end;gap:3px;width:22px;height:18px}
.eq i{flex:1;height:28%;border-radius:2px;background:var(--grad)}
.sound[aria-pressed="true"] .eq i{animation:eq 1s ease-in-out infinite}
.sound[aria-pressed="true"] .eq i:nth-child(2){animation-delay:.2s}
.sound[aria-pressed="true"] .eq i:nth-child(3){animation-delay:.4s}
.sound[aria-pressed="true"] .eq i:nth-child(4){animation-delay:.1s}
@keyframes eq{0%,100%{height:25%}50%{height:100%}}
.celeb{position:fixed;right:18px;bottom:18px;z-index:110;width:54px;height:54px;border-radius:50%;border:1px solid var(--edge);background:rgba(7,16,38,.86);font-size:1.5rem;cursor:pointer;transition:transform .2s,background .2s}
.celeb:hover{transform:scale(1.1) rotate(-8deg);background:rgba(232,40,63,.35)}
.toast{position:fixed;top:112px;left:50%;z-index:130;transform:translate(-50%,-20px);opacity:0;pointer-events:none;padding:12px 24px;border-radius:999px;background:linear-gradient(120deg,var(--red),var(--red2));font-weight:700;box-shadow:0 14px 40px -10px rgba(232,40,63,.9);transition:opacity .35s,transform .35s;white-space:nowrap}
.toast.show{opacity:1;transform:translate(-50%,0)}

@media(prefers-reduced-motion:reduce){
  *{animation:none!important;transition:none!important}
  .hero > *{opacity:1;transform:none}
  .js .rv{opacity:1;transform:none}
  .sleigh{display:none}
  html{scroll-behavior:auto}
}
</style>
</head>
<body>

<div id="loader"><div class="flake">❄</div><b>SeongEraStudy</b><small>Loading Christmas magic…</small></div>
<div class="prog" id="prog"></div>
<div class="lights" id="lights" aria-hidden="true"></div>

<div class="bg">
  <canvas id="fill" width="96" height="54" aria-hidden="true"></canvas>
  <video id="bgf" autoplay muted loop playsinline preload="auto" disablepictureinpicture src="{{VIDEO}}"></video>
</div>
<div class="shade"></div>
<canvas id="snow" aria-hidden="true"></canvas>
<div class="sleigh" aria-hidden="true">🦌🦌🛷🎅</div>
<div class="toast" id="toast" role="status"></div>

<nav class="nav">
  <a class="logo" href="#top">Seong<b>Era</b>Study</a>
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
  <span class="sc">Merry Christmas &amp; Happy New Year 2027</span>
  <strong>SeongEraStudy</strong> · Made by Seong Gium Jee · © <span id="yr"></span>
  <small>Weak Hero fan-inspired. Not affiliated with the original creators. Background edit uses the song "Snowman" by Sia.</small>
</footer>

<button class="celeb" id="celebrate" type="button" aria-label="Celebrate with fireworks" title="Celebrate!">🎆</button>
<button class="sound" id="snd" type="button" aria-pressed="false" aria-label="Turn music on">
  <span class="eq" aria-hidden="true"><i></i><i></i><i></i><i></i></span>
  <span id="sndl">Music off</span>
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
  function play(){ safe(v.play()); startFill(); startSnow(); }
  function stop(){ v.pause(); stopFill(); stopSnow(); }
  try{ v.currentTime=0; }catch(e){}
  play();
  v.addEventListener('loadeddata',paint);
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

  /* ================= LOADER ================= */
  var ld=$('loader');
  function hideLoader(){ if(ld){ ld.classList.add('done'); var x=ld; ld=null; setTimeout(function(){ x.remove(); },800); } }
  window.addEventListener('load',function(){ setTimeout(hideLoader,300); });
  setTimeout(hideLoader,2400);

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
