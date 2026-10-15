"""All HTML templates as strings."""


MAIN_PAGE = r"""<!DOCTYPE html>
<html lang="en" data-theme="default">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>𝐒𝐞𝐨𝐧𝐠𝐒𝐭𝐮𝐝𝐲𝐄𝐫𝐚</title>
<link rel="icon" href="https://i.ibb.co/GQvZNJ5x/file-00000000a2d082088bb8b30c95b7d8b9.png">
<style>
:root{--bg:#07090c;--panel:#0e1218;--panel2:#141a22;--line:#1e2630;--txt:#e6e9ee;--muted:#7c8697;--accent:#5c8dff;--accent2:#7c5cff;--good:#2ecc71;--warn:#f6b73c;--tap:44px}
[data-theme="rose"]{--accent:#ff5c8d;--accent2:#c45cff;--bg:#0c070b;--panel:#160d13;--panel2:#221420}
[data-theme="green"]{--accent:#2ecc71;--accent2:#13b6a3;--bg:#060d09;--panel:#0d1a12;--panel2:#152622}
[data-theme="amber"]{--accent:#f6b73c;--accent2:#ff8a4c;--bg:#0d0a06;--panel:#1a140a;--panel2:#2a2010}
[data-theme="crimson"]{--accent:#ff5c5c;--accent2:#b35cff;--bg:#0c0606;--panel:#1a0d0d;--panel2:#2a1414}
[data-theme="cyber"]{--accent:#00d4ff;--accent2:#7c5cff;--bg:#05080d;--panel:#0b1219;--panel2:#122030}
[data-theme="mono"]{--accent:#e6e9ee;--accent2:#9fb8ff;--bg:#050505;--panel:#101010;--panel2:#1a1a1a}
[data-theme="sunset"]{--accent:#ff7c5c;--accent2:#ff5cbd;--bg:#0d0608;--panel:#1a0f13;--panel2:#2a1820}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html,body{margin:0;height:100%;background:var(--bg);color:var(--txt);font:14px/1.5 -apple-system,"SF Mono",ui-monospace,monospace;overflow:hidden}
button,select,input{font-family:inherit;-webkit-appearance:none;appearance:none}
a{color:var(--accent);text-decoration:none}
.brand-gradient{background:linear-gradient(90deg,var(--accent),var(--accent2) 60%,#b35cff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.topnav{display:flex;align-items:center;gap:10px;padding:10px 16px;background:linear-gradient(180deg,rgba(20,26,34,.6),rgba(10,14,20,.9));border-bottom:1px solid var(--line);flex-shrink:0}
.menu-btn{padding:8px 12px;background:var(--panel2);border:1px solid var(--line);color:var(--txt);border-radius:9px;cursor:pointer;font-size:18px;min-width:44px;min-height:44px;display:inline-flex;align-items:center;justify-content:center}
.brand{flex:1;min-width:0;display:flex;align-items:center;gap:10px}
.brand-logo{width:34px;height:34px;border-radius:9px;object-fit:cover;border:1px solid var(--line);background:#000;flex-shrink:0}
.brand-text{min-width:0;display:flex;flex-direction:column;justify-content:center}
.brand-title{margin:0;font-size:15px;font-weight:800;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;letter-spacing:.3px;line-height:1.15}
.brand-sub{font-size:10px;color:var(--muted);display:block;margin-top:1px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-weight:600}
.brand-sub a{color:var(--accent);font-weight:700}
.brand-sub a:hover{text-decoration:underline}
.theme-btn{padding:8px 12px;background:var(--panel2);border:1px solid var(--line);color:var(--txt);border-radius:9px;cursor:pointer;font-size:16px;min-width:44px;min-height:44px}
.drawer-bg{position:fixed;inset:0;background:rgba(0,0,0,.65);backdrop-filter:blur(4px);z-index:200;opacity:0;pointer-events:none;transition:opacity .22s}
.drawer-bg.open{opacity:1;pointer-events:auto}
.drawer{position:fixed;top:0;left:0;bottom:0;width:280px;max-width:85vw;background:var(--panel);border-right:1px solid var(--line);z-index:201;transform:translateX(-100%);transition:transform .22s;display:flex;flex-direction:column;overflow-y:auto}
.drawer.open{transform:translateX(0)}
.drawer-head{padding:18px 18px;border-bottom:1px solid var(--line);background:linear-gradient(180deg,rgba(92,141,255,.08),transparent);display:flex;align-items:center;gap:12px}
.drawer-head img{width:44px;height:44px;border-radius:11px;border:1px solid var(--line);background:#000}
.drawer-head .info{min-width:0;flex:1}
.drawer-head h2{margin:0;font-size:15px;font-weight:800;letter-spacing:.3px;line-height:1.15;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.drawer-head .tg{font-size:11px;color:var(--muted);display:block;margin-top:3px}
.drawer-head .tg a{color:var(--accent);font-weight:700}
.drawer-item{display:flex;align-items:center;gap:12px;padding:14px 18px;cursor:pointer;color:var(--txt);border-left:3px solid transparent;font-weight:600;font-size:13.5px;text-decoration:none}
.drawer-item.active{background:linear-gradient(90deg,rgba(92,141,255,.12),transparent);border-left-color:var(--accent);color:var(--accent)}
.drawer-item .ico{font-size:18px;width:24px;text-align:center}
.drawer-foot{margin-top:auto;padding:16px 18px;font-size:10.5px;color:var(--muted);border-top:1px solid var(--line);line-height:1.6}
.drawer-foot a{color:var(--accent)}
.content{flex:1;display:flex;flex-direction:column;overflow:hidden;min-height:0;position:relative}
.page{display:none;flex:1;overflow-y:auto;padding:16px}
.page.active{display:block}
.hero{display:flex;align-items:center;gap:14px;padding:16px;margin:4px 0 6px;background:linear-gradient(135deg,rgba(92,141,255,.12),rgba(124,92,255,.06) 60%,transparent);border:1px solid var(--line);border-radius:16px;position:relative;overflow:hidden}
.hero::after{content:"";position:absolute;inset:0;background:radial-gradient(circle at 90% 10%,rgba(124,92,255,.25),transparent 55%);pointer-events:none}
.hero img{width:52px;height:52px;border-radius:12px;background:#fff;border:1px solid var(--line);object-fit:contain;flex-shrink:0}
.hero .h-text{min-width:0;flex:1}
.hero .h-title{font-size:16px;font-weight:800;letter-spacing:.4px;line-height:1.2}
.hero .h-sub{font-size:11.5px;color:var(--muted);margin-top:2px}
.hero .h-sub a{color:var(--accent);font-weight:700}
.search-wrap{padding:10px 0;position:sticky;top:0;background:var(--bg);z-index:5}
.search-wrap input{width:100%;padding:12px 14px;background:var(--panel);border:1px solid var(--line);color:var(--txt);font:inherit;border-radius:10px;min-height:46px;font-size:14px}
.batch-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:14px;padding-bottom:40px}
@media (min-width:700px){.batch-grid{grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:16px}}
.batch-card{background:var(--panel);border:1px solid var(--line);border-radius:14px;overflow:hidden;transition:all .15s;display:flex;flex-direction:column}
.batch-card:hover{border-color:var(--accent);transform:translateY(-2px)}
.batch-card .thumb{aspect-ratio:16/9;background:var(--panel2);position:relative;overflow:hidden;cursor:pointer}
.batch-card .thumb img{width:100%;height:100%;object-fit:cover;display:block}
.batch-card .thumb .pattern{position:absolute;inset:0;background-image:radial-gradient(circle at 20% 20%,rgba(255,255,255,.15) 0,transparent 40%),radial-gradient(circle at 80% 80%,rgba(255,255,255,.1) 0,transparent 40%)}
.batch-card .thumb .mono{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:52px;font-weight:800;color:#fff;text-shadow:0 3px 12px rgba(0,0,0,.35);letter-spacing:2px}
.batch-card .meta{padding:12px 14px 10px;flex:1;display:flex;flex-direction:column;gap:3px;min-width:0}
.batch-card .meta .t{color:#dfe6f0;font-weight:600;font-size:13.5px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.batch-card .meta .s{color:var(--muted);font-size:11px}
.batch-card .study-btn{margin:0 12px 12px;padding:10px;border-radius:9px;border:0;background:linear-gradient(90deg,var(--accent),var(--accent2));color:#fff;font:inherit;font-weight:700;font-size:13px;cursor:pointer;min-height:42px}
.batch-card .study-btn:hover{filter:brightness(1.1)}

.viewer{display:flex;flex-direction:column;height:100%;min-height:0}
.viewer-head{display:flex;align-items:center;gap:10px;padding:10px 16px;background:var(--panel);border-bottom:1px solid var(--line);flex-shrink:0}
.viewer-head .back{padding:8px 12px;background:var(--panel2);border:1px solid var(--line);color:var(--txt);border-radius:8px;cursor:pointer;font-size:14px;min-height:40px;min-width:40px}
.viewer-head .title{font-size:14px;font-weight:600;color:#dfe6f0;flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.player-main{flex:1;display:flex;flex-direction:column;overflow:hidden;min-height:0;position:relative}
.player-wrap{flex:1;background:#000;display:flex;align-items:center;justify-content:center;position:relative;min-height:0;overflow:hidden;cursor:pointer}
.player-empty{color:var(--muted);text-align:center;padding:32px;max-width:560px;line-height:1.8}
.player-empty h2{font-size:26px;margin:0 0 16px;font-weight:800}
.player-wrap video{width:100%;height:100%;background:#000;object-fit:contain}
.player-wrap iframe{width:100%;height:100%;border:0;background:#fff}
.controls{background:var(--panel);border-top:1px solid var(--line);padding:10px 14px;flex-shrink:0}
.bottombar{padding:8px 14px;background:var(--panel);border-top:1px solid var(--line);flex-shrink:0;font-size:11.5px;color:var(--muted);display:flex;justify-content:space-between;gap:10px}
.status{padding:3px 10px;background:var(--panel2);border-radius:12px;color:var(--accent);font-weight:600;font-size:11px}
.status.ok{color:var(--good)}
.status.err{color:#ff7a7a}

/* ===== YouTube-style player (beast mode) ===== */
.yt{position:absolute;inset:0;background:#000;overflow:hidden;color:#fff;font-family:-apple-system,"Segoe UI",Roboto,sans-serif;-webkit-user-select:none;user-select:none;-webkit-touch-callout:none}
.yt:not(.show){cursor:none}
.yt video{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;background:#000}
.yt button{background:none;border:0;color:#fff;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;padding:0;border-radius:50%;font:inherit;transition:background .18s ease,transform .12s cubic-bezier(.34,1.56,.64,1),opacity .22s ease}
.yt button:active{transform:scale(.9)}
.yt button[disabled]{opacity:.3;pointer-events:none!important}
.yt-gl{position:absolute;inset:0;z-index:2;touch-action:manipulation}
.yt-logo{position:absolute;right:14px;top:12px;z-index:3;font-weight:800;font-size:13px;letter-spacing:.5px;opacity:.7;pointer-events:none;transition:opacity .3s ease}
.yt.show .yt-logo{opacity:.9}
.yt-top{position:absolute;left:0;right:0;top:0;z-index:4;padding:14px 100px 40px 16px;background:linear-gradient(180deg,rgba(0,0,0,.82),rgba(0,0,0,.35) 55%,transparent);opacity:0;transform:translateY(-8px);transition:opacity .3s cubic-bezier(.22,.9,.28,1),transform .3s cubic-bezier(.22,.9,.28,1);pointer-events:none}
.yt.show .yt-top{opacity:1;transform:translateY(0)}
.yt-title{font-size:14px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;text-shadow:0 1px 3px rgba(0,0,0,.7)}
.yt-center{position:absolute;inset:0;z-index:4;display:flex;align-items:center;justify-content:center;gap:clamp(20px,10vw,72px);opacity:0;transition:opacity .3s cubic-bezier(.22,.9,.28,1);pointer-events:none}
.yt-center button{pointer-events:none;background:rgba(0,0,0,.5);backdrop-filter:blur(3px);box-shadow:0 6px 24px rgba(0,0,0,.4)}
.yt.show .yt-center{opacity:1}
.yt.show .yt-center button{pointer-events:auto}
.yt-sb{width:48px;height:48px}
.yt-sb:hover{background:rgba(0,0,0,.72);transform:scale(1.08)}
.yt-big{width:70px;height:70px;transition:transform .18s cubic-bezier(.34,1.56,.64,1),background .18s ease,box-shadow .18s ease}
.yt-big:hover{transform:scale(1.1);background:rgba(0,0,0,.72)}
.yt-paused .yt-big{animation:yt-pulse 1.8s ease-in-out infinite}
@keyframes yt-pulse{0%,100%{box-shadow:0 6px 24px rgba(0,0,0,.4),0 0 0 0 rgba(255,255,255,.28)}50%{box-shadow:0 6px 24px rgba(0,0,0,.4),0 0 0 16px rgba(255,255,255,0)}}
.yt-bottom{position:absolute;left:0;right:0;bottom:0;z-index:4;padding:40px 10px 8px;background:linear-gradient(0deg,rgba(0,0,0,.9),rgba(0,0,0,.4) 55%,transparent);opacity:0;transform:translateY(8px);transition:opacity .3s cubic-bezier(.22,.9,.28,1),transform .3s cubic-bezier(.22,.9,.28,1);pointer-events:none}
.yt.show .yt-bottom{opacity:1;transform:translateY(0);pointer-events:auto}
.yt.buf .yt-big{opacity:0}
.yt-pb{position:relative;height:28px;margin:0 4px;display:flex;align-items:center;cursor:pointer;touch-action:none}
.yt-track{position:relative;width:100%;height:4px;background:rgba(255,255,255,.28);border-radius:3px;transition:height .18s cubic-bezier(.22,.9,.28,1)}
.yt-pb:hover .yt-track,.yt-pb.drag .yt-track{height:6px}
.yt-buf{position:absolute;left:0;top:0;bottom:0;width:0;background:rgba(255,255,255,.42);border-radius:3px;transition:width .2s linear}
.yt-fill{position:absolute;left:0;top:0;bottom:0;width:0;background:linear-gradient(90deg,var(--accent),var(--accent2));border-radius:3px;box-shadow:0 0 12px rgba(92,141,255,.6)}
.yt-knob{position:absolute;top:50%;left:0;width:14px;height:14px;border-radius:50%;background:#fff;transform:translate(-50%,-50%);box-shadow:0 0 0 3px rgba(255,255,255,.15);transition:width .18s cubic-bezier(.34,1.56,.64,1),height .18s cubic-bezier(.34,1.56,.64,1),box-shadow .18s ease}
.yt-pb:hover .yt-knob,.yt-pb.drag .yt-knob{width:18px;height:18px;box-shadow:0 0 0 5px rgba(92,141,255,.32)}
.yt-tip{position:absolute;bottom:32px;left:0;transform:translateX(-50%);background:rgba(0,0,0,.88);padding:4px 10px;border-radius:7px;font-size:12px;opacity:0;pointer-events:none;white-space:nowrap;transition:opacity .18s ease;font-variant-numeric:tabular-nums}
.yt-pb:hover .yt-tip,.yt-pb.drag .yt-tip{opacity:1}
.yt-row{display:flex;align-items:center;justify-content:space-between;gap:4px}
.yt-l,.yt-r{display:flex;align-items:center;gap:2px}
.yb{width:40px;height:40px}
.yb:hover{background:rgba(255,255,255,.14)}
.yt-time{font-size:12.5px;margin-left:6px;white-space:nowrap;text-shadow:0 1px 2px #000;font-variant-numeric:tabular-nums}
.yt-volwrap{display:inline-flex;align-items:center}
.yt-vol{-webkit-appearance:none;appearance:none;width:0;opacity:0;height:4px;border-radius:2px;background:rgba(255,255,255,.3);outline:0;padding:0;margin:0;transition:width .22s cubic-bezier(.22,.9,.28,1),opacity .22s ease}
.yt-volwrap:hover .yt-vol,.yt-vol:focus{width:70px;opacity:1;margin:0 8px 0 2px}
.yt-vol::-webkit-slider-thumb{-webkit-appearance:none;width:12px;height:12px;border-radius:50%;background:#fff;border:0;box-shadow:0 0 0 2px rgba(0,0,0,.3)}
.yt-vol::-moz-range-thumb{width:12px;height:12px;border-radius:50%;background:#fff;border:0;box-shadow:0 0 0 2px rgba(0,0,0,.3)}
@media (hover:none){.yt-vol{display:none}}
@media (max-width:520px){.yt-hide-sm{display:none!important}.yb{width:38px;height:38px}.yt-sb{width:46px;height:46px}.yt-big{width:64px;height:64px}}
.yt-rip{position:absolute;top:0;bottom:0;width:38%;z-index:3;display:flex;align-items:center;justify-content:center;opacity:0;pointer-events:none;transition:opacity .25s cubic-bezier(.22,.9,.28,1);background:radial-gradient(circle at 50% 50%,rgba(255,255,255,.22),rgba(255,255,255,.04) 70%);font-size:13px;font-weight:700;text-align:center}
.yt-rip.l{left:0;border-radius:0 100% 100% 0/0 50% 50% 0}
.yt-rip.r{right:0;border-radius:100% 0 0 100%/50% 0 0 50%}
.yt-rip.on{opacity:1;animation:rip-pop .35s cubic-bezier(.34,1.56,.64,1)}
@keyframes rip-pop{0%{transform:scale(.92);opacity:0}100%{transform:scale(1);opacity:1}}
.yt-rip .in{display:flex;flex-direction:column;align-items:center;gap:4px}
.yt-rip .flip svg{transform:scaleX(-1)}
.yt-2x{position:absolute;top:14px;left:50%;transform:translateX(-50%);z-index:5;background:rgba(0,0,0,.75);padding:7px 16px;border-radius:20px;font-size:13px;font-weight:700;opacity:0;pointer-events:none;transition:opacity .2s ease;white-space:nowrap;backdrop-filter:blur(6px);border:1px solid rgba(255,255,255,.1)}
.yt-2x.on{opacity:1;animation:yt-2x-pop .32s cubic-bezier(.34,1.56,.64,1)}
@keyframes yt-2x-pop{from{transform:translateX(-50%) scale(.85);opacity:0}to{transform:translateX(-50%) scale(1);opacity:1}}
.yt-spin{position:absolute;top:50%;left:50%;width:48px;height:48px;margin:-24px 0 0 -24px;border:4px solid rgba(255,255,255,.22);border-top-color:var(--accent);border-radius:50%;z-index:3;display:none;pointer-events:none;animation:ytspin .85s linear infinite}
.yt-spin.on{display:block}
.yt-spin::after{content:"";position:absolute;inset:-18px;border-radius:50%;background:radial-gradient(circle,rgba(0,0,0,.4),transparent 70%)}
@keyframes ytspin{to{transform:rotate(360deg)}}
.yt-menu{position:absolute;right:10px;bottom:76px;z-index:6;min-width:230px;max-width:88%;max-height:70%;overflow-y:auto;background:rgba(16,20,28,.98);border:1px solid var(--line);border-radius:14px;padding:6px;display:none;box-shadow:0 24px 60px rgba(0,0,0,.7);backdrop-filter:blur(10px)}
.yt-menu.open{display:block;animation:yt-menu-in .22s cubic-bezier(.22,.9,.28,1)}
@keyframes yt-menu-in{from{opacity:0;transform:translateY(8px) scale(.97)}to{opacity:1;transform:translateY(0) scale(1)}}
.yt-menu .mi,.yt-menu .mh{display:flex;justify-content:space-between;align-items:center;gap:16px;padding:11px 13px;border-radius:9px;cursor:pointer;font-size:13px;min-height:44px;transition:background .15s ease}
.yt-menu .mi:hover{background:rgba(255,255,255,.1)}
.yt-menu .mh{font-weight:700;border-bottom:1px solid var(--line);border-radius:0;margin-bottom:4px}
.yt-menu .mi .v{color:var(--muted);font-size:12px}
.yt-menu .mi.sel{color:var(--accent);font-weight:700}
/* ===== end player ===== */

/* ===== assessment UI ===== */
.as-wrap{position:absolute;inset:0;background:var(--bg);overflow-y:auto;color:var(--txt);font-family:-apple-system,"Segoe UI",Roboto,sans-serif}
.as-inner{max-width:820px;margin:0 auto;padding:24px 18px 96px}
.as-head{display:flex;justify-content:space-between;align-items:flex-start;gap:14px;margin-bottom:22px;padding-bottom:18px;border-bottom:1px solid var(--line);flex-wrap:wrap}
.as-head h1{margin:0 0 6px;font-size:22px;font-weight:800;line-height:1.3}
.as-head .as-sub{color:var(--muted);font-size:12.5px}
.as-progress{margin-top:14px;width:100%;height:6px;background:var(--panel2);border-radius:3px;overflow:hidden}
.as-progress > div{height:100%;background:linear-gradient(90deg,var(--accent),var(--accent2));width:0;transition:width .3s ease}
.as-timer{padding:6px 12px;background:var(--panel2);border:1px solid var(--line);border-radius:8px;font-weight:700;font-size:13px;font-variant-numeric:tabular-nums}
.as-q{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:22px;margin-bottom:18px;animation:as-q-in .3s cubic-bezier(.22,.9,.28,1)}
@keyframes as-q-in{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:translateY(0)}}
.as-q .as-q-num{color:var(--muted);font-size:11.5px;text-transform:uppercase;letter-spacing:.7px;font-weight:700;margin-bottom:10px}
.as-q .as-q-text{font-size:15.5px;line-height:1.75;color:#dfe6f0;margin-bottom:18px}
.as-q .as-q-text p{margin:0 0 12px}
.as-q .as-q-text p:last-child{margin-bottom:0}
.as-q .as-q-text sup{font-size:.7em;vertical-align:super}
.as-opts{display:flex;flex-direction:column;gap:10px}
.as-opt{display:flex;align-items:flex-start;gap:12px;padding:14px 16px;background:var(--panel2);border:1px solid var(--line);border-radius:11px;cursor:pointer;transition:all .15s ease;min-height:52px}
.as-opt:hover{border-color:var(--accent);background:rgba(92,141,255,.06)}
.as-opt.sel{border-color:var(--accent);background:linear-gradient(90deg,rgba(92,141,255,.14),rgba(124,92,255,.05));box-shadow:0 0 0 1px rgba(92,141,255,.35) inset}
.as-opt .as-radio{width:22px;height:22px;border-radius:50%;border:2px solid var(--muted);flex-shrink:0;display:flex;align-items:center;justify-content:center;margin-top:1px;transition:all .15s ease}
.as-opt.sel .as-radio{border-color:var(--accent);background:var(--accent)}
.as-opt.sel .as-radio::after{content:"";width:8px;height:8px;background:#fff;border-radius:50%}
.as-opt .as-opt-body{flex:1;line-height:1.6;font-size:14.5px}
.as-opt .as-opt-body p{margin:0}
.as-opt input[type=text]{width:100%;margin-top:10px;padding:10px 12px;background:var(--bg);border:1px solid var(--line);color:var(--txt);border-radius:8px;font:inherit;font-size:14px}
.as-actions{position:sticky;bottom:0;display:flex;justify-content:space-between;gap:10px;padding:14px 18px;background:linear-gradient(0deg,var(--bg) 60%,transparent);margin:0 -18px;flex-wrap:wrap}
.as-btn{padding:13px 22px;border-radius:10px;font:inherit;font-weight:700;font-size:14px;cursor:pointer;border:1px solid var(--line);background:var(--panel2);color:var(--txt);min-height:48px;transition:all .15s ease}
.as-btn:hover:not(:disabled){border-color:var(--accent);transform:translateY(-1px)}
.as-btn:disabled{opacity:.4;cursor:not-allowed}
.as-btn.primary{background:linear-gradient(90deg,var(--accent),var(--accent2));color:#fff;border:0}
.as-btn.primary:hover:not(:disabled){filter:brightness(1.1)}
.as-btn.danger{background:linear-gradient(90deg,#ff5c5c,#b35cff);color:#fff;border:0}
.as-review{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:22px;margin-bottom:16px}
.as-review .as-q-text{font-size:14.5px;line-height:1.7;color:#dfe6f0;margin-bottom:14px}
.as-review .as-opt{cursor:default}
.as-review .as-opt.correct{border-color:var(--good);background:rgba(46,204,113,.08)}
.as-review .as-opt.correct .as-radio{border-color:var(--good);background:var(--good)}
.as-review .as-opt.wrong{border-color:#ff5c5c;background:rgba(255,92,92,.08)}
.as-review .as-opt.wrong .as-radio{border-color:#ff5c5c;background:#ff5c5c}
.as-review .as-tag{padding:3px 9px;border-radius:8px;font-size:10.5px;font-weight:700;text-transform:uppercase;letter-spacing:.5px;align-self:flex-start;margin-left:auto}
.as-review .as-tag.ok{background:rgba(46,204,113,.15);color:var(--good)}
.as-review .as-tag.no{background:rgba(255,92,92,.15);color:#ff5c5c}
.as-score-card{background:linear-gradient(135deg,rgba(92,141,255,.14),rgba(124,92,255,.05) 60%,transparent);border:1px solid var(--line);border-radius:14px;padding:22px;margin-bottom:20px;text-align:center}
.as-score-card .num{font-size:44px;font-weight:800;line-height:1;background:linear-gradient(90deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.as-score-card .lbl{color:var(--muted);font-size:12px;text-transform:uppercase;letter-spacing:.8px;margin-top:8px;font-weight:700}
.as-loading{display:flex;align-items:center;justify-content:center;height:100%;color:var(--muted);flex-direction:column;gap:16px}
.as-loading .sp{width:40px;height:40px;border:3px solid var(--panel2);border-top-color:var(--accent);border-radius:50%;animation:ytspin .85s linear infinite}
.as-err{color:#ff7a7a;text-align:center;padding:32px}
/* ===== end assessment ===== */

.sections-overlay{position:fixed;top:0;left:0;bottom:0;width:340px;max-width:85vw;background:var(--panel);border-right:1px solid var(--line);z-index:250;transform:translateX(-100%);transition:transform .28s cubic-bezier(.22,.9,.28,1);display:flex;flex-direction:column;box-shadow:16px 0 40px rgba(0,0,0,.5)}
.sections-overlay.open{transform:translateX(0)}
.sections-overlay .sections-head{padding:14px 16px;border-bottom:1px solid var(--line);display:flex;justify-content:space-between;align-items:center;flex-shrink:0;gap:10px}
.sections-overlay .sections-head img{width:28px;height:28px;border-radius:8px;background:#000;border:1px solid var(--line)}
.sections-overlay .sections-head h3{margin:0;font-size:14px;color:#dfe6f0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;flex:1}
.sections-overlay .close-sec{background:transparent;border:0;color:var(--muted);font-size:22px;cursor:pointer;padding:0 6px;min-width:40px;min-height:40px;transition:color .15s ease}
.sections-overlay .close-sec:hover{color:var(--accent)}
.sections-overlay .search2{padding:10px 12px;border-bottom:1px solid var(--line);flex-shrink:0}
.sections-overlay .search2 input{width:100%;padding:10px 12px;background:var(--bg);border:1px solid var(--line);color:var(--txt);font:inherit;border-radius:9px;min-height:42px;font-size:13.5px}
.toc{flex:1;overflow-y:auto;padding-bottom:40px}
.sec{border-bottom:1px solid var(--line)}
.sec-head{padding:13px 16px;cursor:pointer;display:flex;justify-content:space-between;gap:10px;align-items:center;font-weight:600;font-size:13px;color:#c8d0dd;min-height:44px;transition:background .15s ease,color .15s ease}
.sec-head:hover{background:rgba(255,255,255,.03)}
.sec-head.open{background:var(--panel2);color:var(--accent)}
.sec-head .left{flex:1;display:flex;gap:10px;align-items:center;overflow:hidden}
.sec-head .t{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sec-head .cnt{color:var(--muted);font-size:11px;background:var(--panel2);padding:2px 8px;border-radius:10px}
.sec-body{display:none;background:rgba(0,0,0,.15)}
.sec-body.open{display:block;animation:sec-in .24s cubic-bezier(.22,.9,.28,1)}
@keyframes sec-in{from{opacity:0;transform:translateY(-6px)}to{opacity:1;transform:translateY(0)}}
.unit{padding:11px 16px 11px 24px;cursor:pointer;font-size:13px;color:#a8b3c2;border-left:3px solid transparent;display:flex;justify-content:space-between;gap:10px;align-items:center;min-height:44px;transition:background .18s ease,color .18s ease,border-color .18s ease}
.unit:hover{background:rgba(255,255,255,.04)}
.unit.active{background:linear-gradient(90deg,rgba(92,141,255,.14),transparent);color:var(--accent);border-left-color:var(--accent)}
.unit .u-left{flex:1;display:flex;gap:8px;align-items:center;overflow:hidden}
.unit .u-left .t{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.unit .type{padding:2px 8px;border-radius:8px;font-size:10px;background:var(--panel2);color:var(--muted);font-weight:600;text-transform:uppercase;flex-shrink:0}
.unit .type.assessmentV2{background:rgba(92,141,255,.15);color:var(--accent)}
.pdf-viewer{width:100%;height:100%;display:flex;flex-direction:column;background:#0a0a0a}
.pdf-toolbar{padding:10px 14px;background:var(--panel2);border-bottom:1px solid var(--line);display:flex;justify-content:space-between;gap:10px;align-items:center;flex-wrap:wrap}
.pdf-toolbar .name{color:#dfe6f0;font-weight:600;font-size:12.5px;flex:1;min-width:100px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.pdf-actions{display:flex;gap:6px;flex-wrap:wrap}
.pdf-actions a,.pdf-actions button{padding:8px 12px;background:var(--panel2);color:var(--txt);border:1px solid var(--line);border-radius:8px;font:inherit;font-weight:600;font-size:12px;cursor:pointer;min-height:38px;display:inline-flex;align-items:center;gap:5px;text-decoration:none}
.pdf-actions .primary{background:linear-gradient(90deg,var(--accent),var(--accent2));color:#fff;border-color:transparent}
.pdf-frame{flex:1;border:0;background:#fff}
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:22px;margin-bottom:14px}
.card h2{margin:0 0 12px;font-size:16px;font-weight:700;color:#dfe6f0}
.card p{color:#c8d0dd;line-height:1.7;margin:8px 0;font-size:13.5px}
.card p b{color:#dfe6f0}
.card .btn-row{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px}
.btn-link{display:inline-flex;align-items:center;gap:8px;padding:11px 18px;background:linear-gradient(90deg,var(--accent),var(--accent2));color:#fff;border-radius:10px;font-weight:600;font-size:13px;text-decoration:none;min-height:46px;transition:filter .15s ease,transform .12s ease}
.btn-link:hover{filter:brightness(1.12);transform:translateY(-1px)}
.btn-ghost{display:inline-flex;align-items:center;gap:8px;padding:11px 18px;background:var(--panel2);color:var(--txt);border:1px solid var(--line);border-radius:10px;font-weight:600;font-size:13px;text-decoration:none;min-height:46px;transition:border-color .15s ease,transform .12s ease}
.btn-ghost:hover{border-color:var(--accent);transform:translateY(-1px)}
.qr-img{width:min(100%,320px);border-radius:14px;border:1px solid var(--line);margin:14px auto 0;display:block;background:#fff;padding:12px}
.upi-box{background:var(--bg);border:1px solid var(--line);border-radius:10px;padding:14px;display:flex;justify-content:space-between;gap:10px;align-items:center;margin-top:14px;flex-wrap:wrap}
.upi-box .id{font:13px monospace;color:var(--accent);word-break:break-all;flex:1;min-width:120px}
.upi-box button{padding:10px 16px;background:linear-gradient(90deg,var(--accent),var(--accent2));color:#fff;border:0;border-radius:9px;font:inherit;font-weight:600;font-size:12.5px;cursor:pointer;min-height:40px}
.dev-hero{text-align:center;padding:20px;background:linear-gradient(180deg,rgba(92,141,255,.1),transparent);border-radius:14px;margin-bottom:14px}
.dev-hero .avatar{width:96px;height:96px;border-radius:50%;background:linear-gradient(135deg,var(--accent),var(--accent2));display:inline-flex;align-items:center;justify-content:center;font-size:42px;font-weight:800;color:#fff;margin-bottom:14px;box-shadow:0 12px 40px rgba(92,141,255,.35)}
.dev-hero h2{margin:0 0 6px;font-size:20px}
.dev-hero .tag{color:var(--muted);font-size:12.5px}
.modal{position:fixed;inset:0;background:rgba(0,0,0,.82);backdrop-filter:blur(8px);display:none;align-items:center;justify-content:center;z-index:999;padding:16px}
.modal.open{display:flex;animation:fade-in .22s cubic-bezier(.22,.9,.28,1)}
@keyframes fade-in{from{opacity:0}to{opacity:1}}
.modal .box{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:22px;max-width:600px;width:100%;max-height:90vh;overflow-y:auto;animation:box-in .26s cubic-bezier(.22,.9,.28,1)}
@keyframes box-in{from{opacity:0;transform:translateY(14px) scale(.96)}to{opacity:1;transform:translateY(0) scale(1)}}
.modal h2{margin:0 0 6px;font-size:17px}
.modal .sub{color:var(--muted);font-size:12px;margin-bottom:16px}
.modal input{width:100%;padding:12px 14px;background:var(--bg);border:1px solid var(--line);color:var(--accent);font:12px monospace;border-radius:10px;margin-bottom:10px;box-sizing:border-box}
.modal .variant{padding:12px 14px;background:var(--bg);border:1px solid var(--line);border-radius:10px;margin-bottom:8px}
.modal .variant .name{font-weight:600;font-size:13px}
.modal .variant button{padding:10px 16px;background:var(--panel2);border:1px solid var(--line);color:var(--txt);border-radius:8px;cursor:pointer;font:inherit;font-size:12.5px;font-weight:600;min-height:40px}
.modal .close{float:right;background:transparent;border:0;color:var(--muted);font-size:26px;cursor:pointer;min-width:44px;min-height:44px;transition:color .15s ease}
.modal .close:hover{color:#ff5c5c}
@media (max-width:900px){
  .sections-overlay{width:88vw}
}
/* fullscreen: overlay stacks inside fullscreen element */
.player-wrap:fullscreen .sections-overlay,
.player-wrap:-webkit-full-screen .sections-overlay{position:absolute;width:min(380px,42vw);max-width:88vw;z-index:60;transform:translateX(-100%)}
.player-wrap:fullscreen .sections-overlay.open,
.player-wrap:-webkit-full-screen .sections-overlay.open{transform:translateX(0)}
.player-wrap:fullscreen .bottombar,
.player-wrap:-webkit-full-screen .bottombar{display:none}
</style>
</head>
<body>
<div style="height:100vh;height:100dvh;display:flex;flex-direction:column">
  <div class="topnav">
    <button class="menu-btn" onclick="openDrawer()">☰</button>
    <div class="brand">
      <img class="brand-logo" src="https://i.ibb.co/GQvZNJ5x/file-00000000a2d082088bb8b30c95b7d8b9.png" alt="logo">
      <div class="brand-text">
        <h1 class="brand-title brand-gradient">𝐒𝐞𝐨𝐧𝐠𝐒𝐭𝐮𝐝𝐲𝐄𝐫𝐚</h1>
        <span class="brand-sub">📚 Free Study · <a href="https://t.me/SeongEraStudy" target="_blank">t.me/SeongEraStudy</a></span>
      </div>
    </div>
    <button class="theme-btn" onclick="cycleTheme()">🎨</button>
  </div>

  <div class="drawer-bg" id="drawer-bg" onclick="closeDrawer()"></div>
  <div class="drawer" id="drawer">
    <div class="drawer-head">
      <img src="https://i.ibb.co/GQvZNJ5x/file-00000000a2d082088bb8b30c95b7d8b9.png" alt="logo">
      <div class="info">
        <h2 class="brand-gradient">𝐒𝐞𝐨𝐧𝐠𝐒𝐭𝐮𝐝𝐲𝐄𝐫𝐚</h2>
        <span class="tg">📚 Free study · Made By <a href="https://t.me/Seong_Era" target="_blank">@Seong_Era</a></span>
      </div>
    </div>
    <div class="drawer-item active" data-page="batches" onclick="goPage('batches')"><span class="ico">📚</span><span>All Batches</span></div>
    <div class="drawer-item" data-page="request" onclick="goPage('request')"><span class="ico">➕</span><span>Request a Batch</span></div>
    <a class="drawer-item" href="https://t.me/SeongEraStudy" target="_blank"><span class="ico">💬</span><span>Join Telegram</span></a>
    <div class="drawer-item" data-page="contact" onclick="goPage('contact')"><span class="ico">📩</span><span>Contact Us</span></div>
    <div class="drawer-item" data-page="donate" onclick="goPage('donate')"><span class="ico">❤️</span><span>Donate</span></div>
    <div class="drawer-item" data-page="developer" onclick="goPage('developer')"><span class="ico">👨‍💻</span><span>Developer Info</span></div>
    <div class="drawer-foot">Made By <a href="https://t.me/Seong_Era" target="_blank">@Seong_Era</a><br>Channel: <a href="https://t.me/SeongEraStudy" target="_blank">t.me/SeongEraStudy</a></div>
  </div>

  <div class="content">
    <div class="page active" id="page-batches">
      <div class="hero">
        <img src="https://i.ibb.co/7d6VkR0g/apna-college-icon-filled-256.png" alt="Apna College">
        <div class="h-text">
          <div class="h-title brand-gradient">𝐀𝐩𝐧𝐚 𝐂𝐨𝐥𝐥𝐞𝐠𝐞</div>
          <div class="h-sub">All batches · Free forever · <a href="https://t.me/SeongEraStudy" target="_blank">t.me/SeongEraStudy</a></div>
        </div>
      </div>
      <div class="search-wrap">
        <input id="batch-search" placeholder="🔍 Search batches…">
      </div>
      <div class="batch-grid" id="batch-grid">
        <div style="padding:24px;color:var(--muted);text-align:center;grid-column:1/-1">loading…</div>
      </div>
    </div>

    <div class="page" id="page-viewer">
      <div class="viewer">
        <div class="viewer-head">
          <button class="back" onclick="closeBatch()">←</button>
          <button class="back" onclick="toggleSections()" title="playlist">☰</button>
          <div class="title" id="viewer-title">Batch</div>
        </div>
        <div class="player-main">
          <div class="player-wrap" id="player-wrap">
            <div class="player-empty">
              <h2 class="brand-gradient">Pick a lecture</h2>
              <p>Open the playlist panel with ☰ to browse lectures.</p>
            </div>
          </div>
          <div class="controls" id="controls" style="display:none"></div>
          <div class="bottombar">
            <span class="status" id="status">ready</span>
            <span id="nowplaying"></span>
          </div>
        </div>
      </div>
    </div>

    <div class="page" id="page-request">
      <div class="card">
        <h2>➕ Request a Batch</h2>
        <p>Want a new batch added? Message me on Telegram with the batch name or link.</p>
        <div class="btn-row">
          <a class="btn-link" href="https://t.me/Seong_Era" target="_blank">💬 Message @Seong_Era</a>
          <a class="btn-ghost" href="https://t.me/SeongEraStudy" target="_blank">📢 Join Channel</a>
        </div>
      </div>
    </div>

    <div class="page" id="page-contact">
      <div class="card">
        <h2>📩 Contact Us</h2>
        <p>Any issue or feedback — reach out on Telegram.</p>
        <div class="btn-row">
          <a class="btn-link" href="https://t.me/Seong_Era" target="_blank">💬 @Seong_Era (Personal)</a>
          <a class="btn-ghost" href="https://t.me/SeongEraStudy" target="_blank">📢 Study Channel</a>
        </div>
      </div>
      <div class="card">
        <h2>Common stuff</h2>
        <p><b>Video won't load:</b> reload. Still broken? Message me the batch + lecture name.</p>
        <p><b>Wrong quality or lag:</b> pick a lower resolution.</p>
        <p><b>Download:</b> hit ⬇ in the player. Saves a .ts file — VLC plays it fine.</p>
        <p><b>New batch:</b> use the Request page.</p>
      </div>
    </div>

    <div class="page" id="page-donate">
      <div class="card">
        <h2>❤️ Support 𝐒𝐞𝐨𝐧𝐠𝐒𝐭𝐮𝐝𝐲𝐄𝐫𝐚</h2>
        <p>If this helped you, even a small amount keeps it alive for everyone.</p>
        <p><b>Thank you for the support — it means a lot. 🙏</b></p>
        <img class="qr-img" src="__QR_IMAGE__" alt="UPI QR">
        <div class="upi-box">
          <span class="id" id="upi-id">__UPI_ID__</span>
          <button onclick="copyUpi(this)">📋 copy UPI ID</button>
        </div>
        <p style="margin-top:16px;color:#f6b73c;font-weight:600">📸 After donation, kindly send the payment screenshot to the owner on Telegram — this helps confirm your support and keeps the records clean.</p>
        <div class="btn-row">
          <a class="btn-link" href="https://t.me/SeongEra" target="_blank">💬 Send Screenshot to @SeongEra</a>
        </div>
      </div>
      <div class="card">
        <h2>Where it goes</h2>
        <p>• Server + domain costs</p>
        <p>• New batches, more lectures</p>
        <p>• Keeping it free for everyone</p>
      </div>
    </div>

    <div class="page" id="page-developer">
      <div class="dev-hero">
        <div class="avatar">GP</div>
        <h2 class="brand-gradient">Gopal Parmar</h2>
        <div class="tag">Reverse Engineer · Developer · Bug Bounty Hunter</div>
      </div>
      <div class="card">
        <h2>👨‍💻 Developer Info</h2>
        <p><b>Name:</b> Gopal Parmar</p>
        <p><b>Skills:</b> Reverse Engineering · Coding · Exploiting · Bug Bounty</p>
        <p><b>Age:</b> Why?? you want to know 🥹🥸🥲</p>
        <p><b>State:</b> Rajasthan 🫶❤️‍🩹</p>
        <p><b>Telegram:</b> <a href="https://t.me/SeongEra" target="_blank" style="color:var(--accent)">@SeongEra</a></p>
        <div class="btn-row">
          <a class="btn-link" href="https://t.me/SeongEra" target="_blank">💬 Message @SeongEra</a>
          <a class="btn-ghost" href="https://t.me/SeongEraStudy" target="_blank">📢 Study Channel</a>
        </div>
      </div>
      <div class="card">
        <h2>About the project</h2>
        <p>𝐒𝐞𝐨𝐧𝐠𝐒𝐭𝐮𝐝𝐲𝐄𝐫𝐚 is a free study platform built for students. No ads, no paywall, no signup. Just pick a batch and start learning.</p>
        <p style="color:var(--muted);font-size:12px;margin-top:14px">Made with care in Rajasthan.</p>
      </div>
    </div>
  </div>
</div>

<div class="sections-overlay" id="sections-overlay">
  <div class="sections-head">
    <img src="https://i.ibb.co/GQvZNJ5x/file-00000000a2d082088bb8b30c95b7d8b9.png" alt="logo">
    <h3 id="sections-title">Sections</h3>
    <button class="close-sec" onclick="toggleSections()">✕</button>
  </div>
  <div class="search2"><input id="search" placeholder="search units…"></div>
  <div class="toc" id="toc"></div>
</div>

<div class="modal" id="modal-dl"><div class="box"><button class="close" onclick="closeModal('modal-dl')">×</button><h2>Download</h2><div class="sub">Downloads directly to your device</div><div class="variants" id="dl-variants"></div></div></div>
<div class="modal" id="modal-link"><div class="box"><button class="close" onclick="closeModal('modal-link')">×</button><h2>Direct m3u8 links</h2><div class="sub">Paste into VLC, mpv, yt-dlp</div><input id="link-master" readonly onclick="this.select()"><button onclick="copyField('link-master',this)" style="padding:12px 18px;background:linear-gradient(90deg,var(--accent),var(--accent2));color:#fff;border:0;border-radius:10px;font:inherit;font-weight:600;cursor:pointer;margin-bottom:16px;width:100%">copy master</button><div class="variants" id="link-variants"></div></div></div>

<script src="https://cdn.jsdelivr.net/npm/hls.js@1"></script>
<script>
(function(){
'use strict';
var BATCHES=[],ACTIVE=null,FLAT=[],CURRENT=null,CURRENT_INFO=null,HLS=null,VIDEO=null,CURRENT_VARIANTS={};
var UI_T=null,LP_T=null,TAP_T=null,seekReset=null,seekSide=null,seekAcc=0,ripT=null,lastTapT=0,lastTapSide=null,lastPtr='mouse';
var CUR_SPEED=1,VOL=1,MUTED=false,QSEL=-1,QPREF=0,MENU_VIEW=null,SCRUB=false,HOLDING=false;
var DT_STEP=10;
var SPEEDS=[0.5,0.75,1,1.25,1.5,2];
var THEMES=["default","rose","green","amber","crimson","cyber","mono","sunset"];
var curTheme=localStorage.getItem("theme")||"default";
document.documentElement.setAttribute("data-theme",curTheme);
var PALETTES=[['#5c8dff','#7c5cff'],['#ff5c8d','#c45cff'],['#2ecc71','#13b6a3'],['#f6b73c','#ff8a4c'],['#ff5c5c','#b35cff'],['#00d4ff','#7c5cff'],['#ff7c5c','#ff5cbd'],['#9d5cff','#5c8dff'],['#00b894','#00cec9'],['#fdcb6e','#e17055'],['#e84393','#fd79a8'],['#6c5ce7','#a29bfe']];
window.cycleTheme=function(){var i=THEMES.indexOf(curTheme);i=(i+1)%THEMES.length;curTheme=THEMES[i];document.documentElement.setAttribute("data-theme",curTheme);localStorage.setItem("theme",curTheme);};
function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
function g(id){return document.getElementById(id);}
function hashCode(s){var h=0;for(var i=0;i<s.length;i++){h=((h<<5)-h)+s.charCodeAt(i);h|=0;}return Math.abs(h);}
function pickGradient(l){return PALETTES[hashCode(l||'?')%PALETTES.length];}
function initials(l){var p=(l||'?').trim().split(/\s+/);if(p.length===1)return p[0].slice(0,2).toUpperCase();return (p[0].charAt(0)+p[1].charAt(0)).toUpperCase();}
function showPage(name){var pages=document.querySelectorAll('.page');for(var i=0;i<pages.length;i++)pages[i].classList.remove('active');var el=document.getElementById('page-'+name);if(el)el.classList.add('active');var items=document.querySelectorAll('.drawer-item[data-page]');for(var j=0;j<items.length;j++)items[j].classList.remove('active');var act=document.querySelector('.drawer-item[data-page="'+name+'"]');if(act)act.classList.add('active');}
window.goPage=function(name){showPage(name);closeDrawer();};
window.openDrawer=function(){document.getElementById('drawer').classList.add('open');document.getElementById('drawer-bg').classList.add('open');};
window.closeDrawer=function(){document.getElementById('drawer').classList.remove('open');document.getElementById('drawer-bg').classList.remove('open');};

function renderBatches(){
  var grid=document.getElementById('batch-grid');
  var q=(document.getElementById('batch-search').value||'').toLowerCase();
  grid.innerHTML='';
  var filtered=BATCHES.filter(function(b){return !q||(b.label||'').toLowerCase().indexOf(q)!==-1;});
  if(!filtered.length){grid.innerHTML='<div style="padding:24px;color:var(--muted);text-align:center;grid-column:1/-1">'+(BATCHES.length?'No batches match.':'No batches available.')+'</div>';return;}
  for(var i=0;i<filtered.length;i++){
    (function(b){
      var card=document.createElement('div');card.className='batch-card';
      var hasImg=b.image&&b.image.indexOf('course-default-img')===-1;
      var gr=pickGradient(b.label),ini=initials(b.label);
      var thumb,thumbStyle;
      if(hasImg){thumb='<img src="'+esc(b.image)+'" alt="">';thumbStyle='';}
      else{thumb='<div class="pattern"></div><div class="mono">'+esc(ini)+'</div>';thumbStyle=' style="background:linear-gradient(135deg,'+gr[0]+','+gr[1]+')"';}
      card.innerHTML=
        '<div class="thumb"'+thumbStyle+' data-tid="'+esc(b.titleId)+'" data-label="'+esc(b.label)+'">'+thumb+'</div>'+
        '<div class="meta"><span class="t">'+esc(b.label)+'</span><span class="s">tap to open</span></div>'+
        '<button class="study-btn" data-tid="'+esc(b.titleId)+'" data-label="'+esc(b.label)+'">▶ Study</button>';
      grid.appendChild(card);
    })(filtered[i]);
  }
}
document.addEventListener('click',function(e){
  var t=e.target;
  if(t.dataset&&t.dataset.tid){openBatch(t.dataset.tid,t.dataset.label);}
});

window.openBatch=function(titleId,label){
  ACTIVE=titleId;
  document.getElementById('viewer-title').textContent=label;
  document.getElementById('sections-title').textContent=label;
  document.getElementById('search').value='';
  document.getElementById('toc').innerHTML='<div style="padding:20px;color:var(--muted)">loading sections…</div>';
  document.getElementById('player-wrap').innerHTML='<div class="player-empty"><h2 class="brand-gradient">Pick a lecture</h2><p>Open playlist panel with ☰</p></div>';
  document.getElementById('controls').style.display='none';
  document.getElementById('nowplaying').textContent='';
  destroyPlayer();
  showPage('viewer');
  fetch('/api/sections/'+encodeURIComponent(titleId)).then(function(r){return r.json();}).then(function(j){
    if(!j||!j.sections){document.getElementById('toc').innerHTML='<div style="padding:20px;color:#ff7a7a">'+esc((j&&j.error)||'failed')+'</div>';return;}
    window._sections=j.sections;
    renderTOC();
    if(window.innerWidth>900)document.getElementById('sections-overlay').classList.add('open');
  }).catch(function(e){document.getElementById('toc').innerHTML='<div style="padding:20px;color:#ff7a7a">error: '+esc(e.message||e)+'</div>';});
};
window.closeBatch=function(){destroyPlayer();ACTIVE=null;document.getElementById('sections-overlay').classList.remove('open');showPage('batches');};
window.toggleSections=function(){document.getElementById('sections-overlay').classList.toggle('open');};

function renderTOC(){
  var toc=document.getElementById('toc');toc.innerHTML='';FLAT=[];
  var q=(document.getElementById('search').value||'').toLowerCase();
  var sections=window._sections||[];
  for(var si=0;si<sections.length;si++){
    var sec=sections[si];
    var units=sec.units.filter(function(u){return !q||((u.title||'').toLowerCase().indexOf(q)!==-1);});
    if(q&&units.length===0)continue;
    var secDiv=document.createElement('div');secDiv.className='sec';
    var head=document.createElement('div');head.className='sec-head'+(q?' open':'');
    head.innerHTML='<div class="left"><span class="t">'+esc(sec.title)+'</span></div><span class="cnt">'+sec.units.length+'</span>';
    var body=document.createElement('div');body.className='sec-body'+(q?' open':'');
    head.onclick=(function(h,b){return function(){h.classList.toggle('open');b.classList.toggle('open');};})(head,body);
    for(var ui=0;ui<units.length;ui++){
      var u=units[ui];var idx=FLAT.length;
      FLAT.push({unit:u,sectionTitle:sec.title});
      var uDiv=document.createElement('div');uDiv.className='unit';uDiv.dataset.idx=idx;
      uDiv.innerHTML='<div class="u-left"><span class="t">'+esc(u.title||u.id)+'</span></div><span class="type '+esc(u.type||'')+'">'+esc(u.type||'')+'</span>';
      (function(i){uDiv.onclick=function(){playUnit(i);};})(idx);
      body.appendChild(uDiv);
    }
    secDiv.appendChild(head);secDiv.appendChild(body);toc.appendChild(secDiv);
  }
}

function playUnit(idx){
  if(idx<0||idx>=FLAT.length)return;
  CURRENT=idx;var item=FLAT[idx];var u=item.unit;
  var units=document.querySelectorAll('.unit.active');
  for(var i=0;i<units.length;i++)units[i].classList.remove('active');
  var el=document.querySelector('.unit[data-idx="'+idx+'"]');
  if(el){el.classList.add('active');el.scrollIntoView({block:'nearest',behavior:'smooth'});}
  document.getElementById('nowplaying').textContent=u.title||'';
  document.getElementById('status').textContent='loading…';
  document.getElementById('status').className='status';
  document.getElementById('controls').style.display='none';
  destroyPlayer();
  fetch('/api/video/'+encodeURIComponent(ACTIVE)+'/'+encodeURIComponent(u.id)).then(function(r){return r.json();}).then(function(j){
    CURRENT_INFO=j;
    if(j.error){document.getElementById('player-wrap').innerHTML='<div class="player-empty"><p>error: '+esc(j.error)+'</p></div>';document.getElementById('status').textContent='error';document.getElementById('status').className='status err';return;}
    if(j.type==='wistia'&&j.sourceid){playWistia(j.sourceid);}
    else if(j.type==='pdf'){playPdf(ACTIVE,u.id);}
    else if(j.type==='assessment'){playAssessment(ACTIVE,u.id,j);}
    else{document.getElementById('player-wrap').innerHTML='<div class="player-empty"><p>unsupported: '+esc(j.type||'?')+'</p></div>';}
    if(window.innerWidth<=900)document.getElementById('sections-overlay').classList.remove('open');
  }).catch(function(e){document.getElementById('player-wrap').innerHTML='<div class="player-empty"><p>error: '+esc(e.message||e)+'</p></div>';});
}
function destroyPlayer(){
  clearTimeout(UI_T);clearTimeout(LP_T);clearTimeout(TAP_T);clearTimeout(seekReset);clearTimeout(ripT);
  seekSide=null;seekAcc=0;MENU_VIEW=null;SCRUB=false;HOLDING=false;
  if(HLS){try{HLS.destroy();}catch(e){}HLS=null;}
  if(VIDEO){try{VIDEO.pause();}catch(e){}VIDEO=null;}
  if(window._asTimer){clearInterval(window._asTimer);window._asTimer=null;}
}
/* ================= YouTube-style player ================= */
var IC={
  play:'M8 5v14l11-7z',
  pause:'M6 19h4V5H6v14zm8-14v14h4V5h-4z',
  replay:'M12 5V1L7 6l5 5V7c3.31 0 6 2.69 6 6s-2.69 6-6 6-6-2.69-6-6H4c0 4.42 3.58 8 8 8s8-3.58 8-8-3.58-8-8-8z',
  prev:'M6 6h2v12H6zm3.5 6l8.5 6V6z',
  next:'M6 18l8.5-6L6 6v12zM16 6v12h2V6h-2z',
  vol:'M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02z',
  mute:'M16.5 12c0-1.77-1.02-3.29-2.5-4.03v2.21l2.45 2.45c.03-.2.05-.41.05-.63zm2.5 0c0 .94-.2 1.82-.54 2.64l1.51 1.51C20.63 14.91 21 13.5 21 12c0-4.28-2.99-7.86-7-8.77v2.06c2.89.86 5 3.54 5 6.71zM4.27 3L3 4.27 7.73 9H3v6h4l5 5v-6.73l4.25 4.25c-.67.52-1.42.93-2.25 1.18v2.06c1.38-.31 2.63-.95 3.69-1.81L19.73 21 21 19.73l-9-9L4.27 3zM12 4L9.91 6.09 12 8.18V4z',
  gear:'M19.14 12.94c.04-.3.06-.61.06-.94 0-.32-.02-.64-.07-.94l2.03-1.58a.49.49 0 0 0 .12-.61l-1.92-3.32a.488.488 0 0 0-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54a.484.484 0 0 0-.48-.41h-3.84c-.24 0-.43.17-.47.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96c-.22-.08-.47 0-.59.22L2.74 8.87c-.12.21-.08.47.12.61l2.03 1.58c-.05.3-.09.63-.09.94s.02.64.07.94l-2.03 1.58a.49.49 0 0 0-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z',
  fs:'M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z',
  exitfs:'M5 16h3v3h2v-5H5v2zm3-8H5v2h5V5H8v3zm6 11h2v-3h3v-2h-5v5zm2-11V5h-2v5h5V8h-3z',
  list:'M3 13h2v-2H3v2zm0 4h2v-2H3v2zm0-8h2V7H3v2zm4 4h14v-2H7v2zm0 4h14v-2H7v2zM7 7v2h14V7H7z',
  dl:'M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z',
  link:'M3.9 12c0-1.71 1.39-3.1 3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 5 5 5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 3.1s-1.39 3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 5-5s-2.24-5-5-5z'
};
function ic(n,s){s=s||24;return '<svg viewBox="0 0 24 24" width="'+s+'" height="'+s+'" fill="currentColor"><path d="'+IC[n]+'"/></svg>';}
function setStatus(t,c){var s=g('status');if(!s)return;s.textContent=t;s.className=c||'status';}

function buildPlayerUI(){
  var title=(CURRENT!=null&&FLAT[CURRENT])?(FLAT[CURRENT].unit.title||''):'';
  g('player-wrap').innerHTML=
  '<div class="yt show" id="yt">'+
    '<video id="v" playsinline webkit-playsinline preload="metadata"></video>'+
    '<div class="yt-gl" id="yt-gl"></div>'+
    '<div class="yt-logo brand-gradient">SeongEra</div>'+
    '<div class="yt-rip l" id="yt-rl"><div class="in"><span class="ar">'+ic('replay',30)+'</span><span id="yt-rlt">10 seconds</span></div></div>'+
    '<div class="yt-rip r" id="yt-rr"><div class="in"><span class="ar flip">'+ic('replay',30)+'</span><span id="yt-rrt">10 seconds</span></div></div>'+
    '<div class="yt-2x" id="yt-2x">▶▶ 2× speed</div>'+
    '<div class="yt-spin" id="yt-spin"></div>'+
    '<div class="yt-top" id="yt-top"><div class="yt-title" id="yt-title">'+esc(title)+'</div></div>'+
    '<div class="yt-center" id="yt-center">'+
      '<button class="yt-sb" id="yt-prev" title="Previous lecture">'+ic('prev',28)+'</button>'+
      '<button class="yt-big" id="yt-big" title="Play / Pause">'+ic('play',40)+'</button>'+
      '<button class="yt-sb" id="yt-next" title="Next lecture">'+ic('next',28)+'</button>'+
    '</div>'+
    '<div class="yt-bottom" id="yt-bottom">'+
      '<div class="yt-pb" id="yt-pb"><div class="yt-track"><div class="yt-buf" id="yt-buf"></div><div class="yt-fill" id="yt-fill"></div><div class="yt-knob" id="yt-knob"></div></div><div class="yt-tip" id="yt-tip">0:00</div></div>'+
      '<div class="yt-row">'+
        '<div class="yt-l">'+
          '<button class="yb yt-hide-sm" id="yt-pp" title="Play / Pause">'+ic('play')+'</button>'+
          '<span class="yt-volwrap"><button class="yb yt-hide-sm" id="yt-mute" title="Mute">'+ic('vol')+'</button><input class="yt-vol" id="yt-vol" type="range" min="0" max="1" step="0.05" value="1"></span>'+
          '<span class="yt-time" id="yt-time">0:00 / 0:00</span>'+
        '</div>'+
        '<div class="yt-r">'+
          '<button class="yb" id="yt-list" title="Playlist">'+ic('list')+'</button>'+
          '<button class="yb" id="yt-dl" title="Download">'+ic('dl')+'</button>'+
          '<button class="yb" id="yt-lk" title="Get m3u8 link">'+ic('link')+'</button>'+
          '<button class="yb" id="yt-set" title="Settings">'+ic('gear')+'</button>'+
          '<button class="yb" id="yt-fs" title="Fullscreen">'+ic(fsEl()?'exitfs':'fs')+'</button>'+
        '</div>'+
      '</div>'+
    '</div>'+
    '<div class="yt-menu" id="yt-menu"></div>'+
  '</div>';
  bindUI();
  syncNav();
}

function on(id,fn){var el=g(id);if(el)el.addEventListener('click',fn);}
function bindUI(){
  var y=g('yt');
  y.addEventListener('mousemove',showUI);
  var zones=['yt-top','yt-bottom','yt-center'];
  for(var i=0;i<zones.length;i++){g(zones[i]).addEventListener('pointerdown',function(e){e.stopPropagation();showUI();});}
  on('yt-big',function(e){e.stopPropagation();window.togglePlay();});
  on('yt-pp',function(e){e.stopPropagation();window.togglePlay();});
  on('yt-prev',function(e){e.stopPropagation();window.playPrev();});
  on('yt-next',function(e){e.stopPropagation();window.playNext();});
  on('yt-mute',function(e){e.stopPropagation();window.toggleMute();});
  on('yt-list',function(e){e.stopPropagation();leaveFS();window.toggleSections();});
  on('yt-dl',function(e){e.stopPropagation();leaveFS();window.openDownload();});
  on('yt-lk',function(e){e.stopPropagation();leaveFS();window.openLink();});
  on('yt-set',function(e){e.stopPropagation();if(MENU_VIEW)closeMenu();else openMenu('main');});
  on('yt-fs',function(e){e.stopPropagation();window.toggleFS();});
  g('yt-vol').addEventListener('input',function(e){e.stopPropagation();if(!VIDEO)return;var v=parseFloat(this.value);VIDEO.volume=v;VIDEO.muted=(v===0);});
  g('yt-menu').addEventListener('click',function(e){
    e.stopPropagation();
    var t=e.target;
    while(t&&t!==this&&!(t.dataset&&(t.dataset.go||t.dataset.q!==undefined||t.dataset.s!==undefined)))t=t.parentNode;
    if(!t||t===this)return;
    if(t.dataset.go){MENU_VIEW=t.dataset.go;renderMenu();return;}
    if(t.dataset.q!==undefined){setQuality(t.dataset.q);closeMenu();return;}
    if(t.dataset.s!==undefined){window.setSpeed(t.dataset.s);closeMenu();}
  });
  bindProgress();
  bindGestures();
}

function bindVideo(){
  var v=VIDEO;
  v.addEventListener('timeupdate',updateTime);
  v.addEventListener('progress',updateTime);
  v.addEventListener('durationchange',updateTime);
  v.addEventListener('loadedmetadata',function(){if(!HOLDING)v.playbackRate=CUR_SPEED;updateTime();});
  v.addEventListener('play',function(){syncPlay();showUI();});
  v.addEventListener('pause',function(){if(!VIDEO)return;syncPlay();showUI();setStatus('paused','status');});
  v.addEventListener('playing',function(){if(!VIDEO)return;setBuf(false);syncPlay();setStatus(playingLabel(),'status ok');showUI();});
  v.addEventListener('waiting',function(){if(!VIDEO)return;setBuf(true);setStatus('buffering…','status');});
  v.addEventListener('canplay',function(){setBuf(false);});
  v.addEventListener('seeked',function(){setBuf(false);});
  v.addEventListener('ended',function(){syncPlay();showUI();});
  v.addEventListener('volumechange',syncVol);
  v.addEventListener('error',function(){if(!VIDEO)return;setBuf(false);setStatus('video error','status err');});
}
function playingLabel(){
  if(HLS&&HLS.levels&&HLS.currentLevel>=0&&HLS.levels[HLS.currentLevel]&&HLS.levels[HLS.currentLevel].height)return 'playing · '+HLS.levels[HLS.currentLevel].height+'p';
  return 'playing';
}
function setBuf(on){var y=g('yt'),s=g('yt-spin');if(!y||!s)return;y.classList.toggle('buf',on);s.classList.toggle('on',on);}
function syncPlay(){
  if(!VIDEO||!g('yt-big'))return;
  var playing=!VIDEO.paused&&!VIDEO.ended;
  var n=VIDEO.ended?'replay':(playing?'pause':'play');
  g('yt-big').innerHTML=ic(n,40);
  g('yt-pp').innerHTML=ic(n);
  var y=g('yt');
  if(y)y.classList.toggle('yt-paused',!playing);
}
function syncNav(){
  var p=g('yt-prev'),n=g('yt-next');if(!p||!n)return;
  p.disabled=!(CURRENT!=null&&CURRENT>0);
  n.disabled=!(CURRENT!=null&&CURRENT<FLAT.length-1);
}
function syncVol(){
  if(!VIDEO||!g('yt-mute'))return;
  MUTED=VIDEO.muted;
  if(!VIDEO.muted&&VIDEO.volume>0)VOL=VIDEO.volume;
  var eff=VIDEO.muted?0:VIDEO.volume;
  g('yt-mute').innerHTML=ic(eff===0?'mute':'vol');
  var s=g('yt-vol');s.value=eff;
  var p=Math.round(eff*100);
  s.style.background='linear-gradient(90deg,#fff '+p+'%,rgba(255,255,255,.3) '+p+'%)';
}
function showUI(){
  var y=g('yt');if(!y)return;
  y.classList.add('show');
  clearTimeout(UI_T);
  if(VIDEO&&!VIDEO.paused&&!SCRUB&&!MENU_VIEW&&!HOLDING){UI_T=setTimeout(hideUI,3200);}
}
function hideUI(){
  var y=g('yt');
  if(!y||!VIDEO||VIDEO.paused||SCRUB||MENU_VIEW)return;
  y.classList.remove('show');
}
function toggleUI(){
  var y=g('yt');if(!y)return;
  if(y.classList.contains('show')){y.classList.remove('show');clearTimeout(UI_T);}
  else showUI();
}
function dur(){var d=VIDEO&&VIDEO.duration;return (d&&isFinite(d))?d:0;}
function setProg(pct){var f=g('yt-fill'),k=g('yt-knob');if(!f)return;f.style.width=pct+'%';k.style.left=pct+'%';}
function updateTime(){
  if(!VIDEO||!g('yt-time'))return;
  var cur=VIDEO.currentTime||0,d=dur();
  if(!SCRUB){
    g('yt-time').textContent=fmt(cur)+' / '+fmt(d);
    setProg(d?Math.min(100,cur/d*100):0);
  }
  var b=VIDEO.buffered;
  if(d&&b&&b.length){
    var end=b.end(b.length-1);
    for(var i=0;i<b.length;i++){if(b.start(i)<=cur+0.5&&b.end(i)>=cur){end=b.end(i);break;}}
    g('yt-buf').style.width=Math.min(100,end/d*100)+'%';
  }
}
function fmt(s){s=Math.floor(s||0);if(!isFinite(s))s=0;var h=Math.floor(s/3600),m=Math.floor((s%3600)/60),r=s%60;if(h)return h+':'+(m<10?'0':'')+m+':'+(r<10?'0':'')+r;return m+':'+(r<10?'0':'')+r;}
function bindProgress(){
  var pb=g('yt-pb'),tip=g('yt-tip');
  function pos(e){var r=pb.getBoundingClientRect();return Math.max(0,Math.min(1,(e.clientX-r.left)/r.width));}
  function showTip(p){
    var w=pb.getBoundingClientRect().width;
    var x=Math.max(26,Math.min(w-26,p*w));
    tip.style.left=x+'px';tip.textContent=fmt(p*dur());tip.style.opacity='1';
  }
  function scrub(e){
    var p=pos(e),d=dur();
    setProg(p*100);
    g('yt-time').textContent=fmt(p*d)+' / '+fmt(d);
    showTip(p);
  }
  pb.addEventListener('pointerdown',function(e){
    if(!VIDEO||!dur())return;
    e.stopPropagation();
    SCRUB=true;pb.classList.add('drag');
    try{pb.setPointerCapture(e.pointerId);}catch(x){}
    scrub(e);showUI();
  });
  pb.addEventListener('pointermove',function(e){
    if(!dur())return;
    if(SCRUB)scrub(e);else showTip(pos(e));
  });
  function finish(e,apply){
    if(!SCRUB)return;
    SCRUB=false;pb.classList.remove('drag');tip.style.opacity='0';
    if(apply&&VIDEO&&dur()){VIDEO.currentTime=pos(e)*dur();}
    updateTime();showUI();
  }
  pb.addEventListener('pointerup',function(e){finish(e,true);});
  pb.addEventListener('pointercancel',function(e){finish(e,false);});
  pb.addEventListener('pointerleave',function(){if(!SCRUB)tip.style.opacity='0';});
}

function qualityLabel(){
  if(!HLS||!HLS.levels||!HLS.levels.length)return 'Auto';
  if(QSEL===-1){var l=HLS.levels[HLS.currentLevel];return 'Auto'+(l&&l.height?' ('+l.height+'p)':'');}
  var l2=HLS.levels[QSEL];return l2&&l2.height?l2.height+'p':'L'+QSEL;
}
function openMenu(view){MENU_VIEW=view;renderMenu();g('yt-menu').classList.add('open');showUI();}
function closeMenu(){MENU_VIEW=null;var m=g('yt-menu');if(m)m.classList.remove('open');showUI();}
function renderMenu(){
  var m=g('yt-menu');if(!m)return;
  var h='';
  if(MENU_VIEW==='main'){
    h+='<div class="mi" data-go="quality"><span>Quality</span><span class="v">'+esc(qualityLabel())+' ›</span></div>';
    h+='<div class="mi" data-go="speed"><span>Playback speed</span><span class="v">'+(CUR_SPEED===1?'Normal':CUR_SPEED+'×')+' ›</span></div>';
  }else if(MENU_VIEW==='quality'){
    h+='<div class="mh" data-go="main">‹ Quality</div>';
    var lv=[];
    if(HLS&&HLS.levels){for(var i=0;i<HLS.levels.length;i++){lv.push({i:i,h:HLS.levels[i].height||0});}}
    lv.sort(function(a,b){return b.h-a.h;});
    for(var j=0;j<lv.length;j++){
      h+='<div class="mi'+(QSEL===lv[j].i?' sel':'')+'" data-q="'+lv[j].i+'"><span>'+(QSEL===lv[j].i?'✓ ':'')+(lv[j].h?lv[j].h+'p':'L'+lv[j].i)+'</span></div>';
    }
    h+='<div class="mi'+(QSEL===-1?' sel':'')+'" data-q="auto"><span>'+(QSEL===-1?'✓ ':'')+'Auto</span></div>';
  }else if(MENU_VIEW==='speed'){
    h+='<div class="mh" data-go="main">‹ Playback speed</div>';
    for(var k=0;k<SPEEDS.length;k++){
      var sp=SPEEDS[k];
      h+='<div class="mi'+(CUR_SPEED===sp?' sel':'')+'" data-s="'+sp+'"><span>'+(CUR_SPEED===sp?'✓ ':'')+(sp===1?'Normal':sp+'×')+'</span></div>';
    }
  }
  m.innerHTML=h;
}
function setQuality(v){
  if(v==='auto'){QSEL=-1;QPREF=0;}
  else{QSEL=parseInt(v,10);var l=HLS&&HLS.levels&&HLS.levels[QSEL];QPREF=l?(l.height||0):0;}
  if(HLS)HLS.currentLevel=QSEL;
}
window.onQualityChange=function(v){setQuality(v);};
window.setSpeed=function(v){CUR_SPEED=parseFloat(v)||1;if(VIDEO&&!HOLDING)VIDEO.playbackRate=CUR_SPEED;};

function bindGestures(){
  var gl=g('yt-gl'),down=false,holding=false,moved=false,sx=0,sy=0;
  var isTouch=false;
  function sideOf(e){var r=gl.getBoundingClientRect();var x=(e.clientX-r.left)/r.width;return x<0.35?'l':(x>0.65?'r':'c');}
  gl.addEventListener('contextmenu',function(e){e.preventDefault();});
  gl.addEventListener('pointerdown',function(e){
    if(e.pointerType==='mouse'&&e.button!==0)return;
    lastPtr=e.pointerType||'mouse';
    isTouch=(e.pointerType==='touch'||e.pointerType==='pen');
    down=true;holding=false;moved=false;sx=e.clientX;sy=e.clientY;
    clearTimeout(LP_T);
    if(isTouch){
      LP_T=setTimeout(function(){
        if(!down||moved||!VIDEO||VIDEO.paused||MENU_VIEW)return;
        holding=true;startHold();
      },450);
    }
  });
  gl.addEventListener('pointermove',function(e){
    if(e.pointerType==='mouse')showUI();
    if(down&&!holding&&(Math.abs(e.clientX-sx)>12||Math.abs(e.clientY-sy)>12)){moved=true;clearTimeout(LP_T);}
  });
  function end(e,cancel){
    if(!down)return;
    down=false;clearTimeout(LP_T);
    if(holding){holding=false;stopHold();return;}
    if(cancel||moved)return;
    onTap(sideOf(e),isTouch);
  }
  gl.addEventListener('pointerup',function(e){end(e,false);});
  gl.addEventListener('pointercancel',function(e){end(e,true);});
  gl.addEventListener('pointerleave',function(e){if(down&&holding)end(e,true);});
}
function startHold(){
  if(!VIDEO)return;
  HOLDING=true;VIDEO.playbackRate=2;
  var b=g('yt-2x');if(b)b.classList.add('on');
  var y=g('yt');if(y)y.classList.remove('show');
  clearTimeout(UI_T);
  try{if(navigator.vibrate)navigator.vibrate(15);}catch(e){}
}
function stopHold(){
  HOLDING=false;
  if(VIDEO)VIDEO.playbackRate=CUR_SPEED;
  var b=g('yt-2x');if(b)b.classList.remove('on');
}
function onTap(side,isTouch){
  if(MENU_VIEW){closeMenu();return;}
  var now=Date.now();
  if(seekSide&&side===seekSide&&side!=='c'){doSeek(side);return;}
  if(now-lastTapT<280&&lastTapSide===side){
    clearTimeout(TAP_T);lastTapT=0;
    if(side==='c'){
      if(isTouch){showUI();}else{window.toggleFS();}
    }else{doSeek(side);}
    return;
  }
  lastTapT=now;lastTapSide=side;
  clearTimeout(TAP_T);
  TAP_T=setTimeout(function(){singleTap(isTouch);},280);
}
function singleTap(isTouch){
  if(isTouch){
    var y=g('yt');
    if(!y)return;
    if(!y.classList.contains('show')){
      showUI();
    }else{
      clearTimeout(UI_T);
      if(VIDEO&&!VIDEO.paused)UI_T=setTimeout(hideUI,3200);
    }
    return;
  }
  window.togglePlay();
  showUI();
}
function doSeek(side){
  if(!VIDEO||!dur())return;
  var dir=side==='l'?-1:1;
  if(seekSide!==side)seekAcc=0;
  seekSide=side;seekAcc+=DT_STEP;
  VIDEO.currentTime=Math.max(0,Math.min(dur(),(VIDEO.currentTime||0)+dir*DT_STEP));
  showRipple(side,seekAcc);
  clearTimeout(seekReset);
  seekReset=setTimeout(function(){seekSide=null;seekAcc=0;},700);
  updateTime();
}
function showRipple(side,acc){
  var l=g('yt-rl'),r=g('yt-rr');if(!l||!r)return;
  var el=side==='l'?l:r,other=side==='l'?r:l;
  other.classList.remove('on');
  g(side==='l'?'yt-rlt':'yt-rrt').textContent=acc+' seconds';
  el.classList.add('on');
  clearTimeout(ripT);
  ripT=setTimeout(function(){el.classList.remove('on');},650);
}

/* ================= video loading ================= */
function playWistia(sourceid){
  var master='https://fast.wistia.com/embed/medias/'+sourceid+'.m3u8';
  buildPlayerUI();
  VIDEO=g('v');
  VIDEO.volume=VOL;VIDEO.muted=MUTED;VIDEO.playbackRate=CUR_SPEED;
  QSEL=-1;
  bindVideo();
  syncVol();syncPlay();
  setBuf(true);
  fetch('/api/variants/'+encodeURIComponent(sourceid)).then(function(r){return r.json();}).then(function(j){CURRENT_VARIANTS=(j&&j.variants)||{};}).catch(function(){CURRENT_VARIANTS={};});
  if(window.Hls&&Hls.isSupported()){
    HLS=new Hls({capLevelToPlayerSize:false,startLevel:-1,autoStartLoad:true,maxBufferLength:60});
    HLS.loadSource(master);HLS.attachMedia(VIDEO);
    HLS.on(Hls.Events.MANIFEST_PARSED,function(e,data){
      if(QPREF){
        for(var i=0;i<data.levels.length;i++){if(data.levels[i].height===QPREF){QSEL=i;HLS.currentLevel=i;break;}}
      }
      if(MENU_VIEW)renderMenu();
      VIDEO.play().catch(function(){});
    });
    HLS.on(Hls.Events.LEVEL_SWITCHED,function(e,data){
      var lvl=HLS.levels[data.level];
      if(lvl){setStatus('playing · '+(lvl.height||'?')+'p','status ok');}
      if(MENU_VIEW)renderMenu();
    });
    HLS.on(Hls.Events.ERROR,function(e,d){
      if(!d||!d.fatal)return;
      if(d.type===Hls.ErrorTypes.NETWORK_ERROR){setStatus('network error · retrying','status err');try{HLS.startLoad();}catch(x){}}
      else if(d.type===Hls.ErrorTypes.MEDIA_ERROR){try{HLS.recoverMediaError();}catch(x){}}
      else{setBuf(false);setStatus('playback error','status err');}
    });
  }else if(VIDEO.canPlayType('application/vnd.apple.mpegurl')){VIDEO.src=master;VIDEO.play().catch(function(){});}
  document.getElementById('status').textContent='playing';
  attachAutoNext();
}

function attachAutoNext(){
  if(!VIDEO) return;
  VIDEO.addEventListener('ended', function(){
    if(CURRENT != null && CURRENT < FLAT.length - 1){
      document.getElementById('status').textContent='auto-playing next…';
      playUnit(CURRENT + 1);
    }
  });
}

/* ================= assessment player ================= */
var AS = { state:null, titleId:null, unitId:null, submissionId:null,
           answers:{}, order:[], blockMap:{}, curIdx:0, total:0, submitted:false,
           submissionsById:{} };

function asWidgetHtml(widgets){
  if(!widgets)return '';
  var parts=[];
  for(var i=0;i<widgets.length;i++){
    var w=widgets[i];
    if(!w)continue;
    if(w.type==='text'&&w.properties&&w.properties.html){parts.push(w.properties.html);}
    else if(w.type==='spacer'){parts.push('<div style="height:'+((w.properties&&w.properties.height)||12)+'px"></div>');}
    else if(w.type==='image'&&w.properties&&w.properties.url){parts.push('<img src="'+esc(w.properties.url)+'" style="max-width:100%;border-radius:8px">');}
    else if(w.type==='button'&&w.properties&&w.properties.buttonLabel){parts.push('<button class="as-btn">'+w.properties.buttonLabel+'</button>');}
  }
  return parts.join('');
}

function playAssessment(titleId,unitId,info){
  AS.state=null;AS.titleId=titleId;AS.unitId=unitId;AS.answers={};
  AS.order=[];AS.blockMap={};AS.curIdx=0;AS.total=0;AS.submitted=false;
  g('player-wrap').innerHTML='<div class="as-loading"><div class="sp"></div><div>loading assessment…</div></div>';
  setStatus('assessment','status');
  fetch('/api/assessment/'+encodeURIComponent(titleId)+'/'+encodeURIComponent(unitId))
    .then(function(r){return r.json();})
    .then(function(j){
      if(j.error){g('player-wrap').innerHTML='<div class="as-err">'+esc(j.error)+'</div>';setStatus('error','status err');return;}
      AS.state=j;
      var a=j.assessment||{};
      var sub=j.latestSubmission||{};
      AS.submissionId=sub.id||null;
      // pre-fill answers from latestSubmission
      var pre=(sub.answers||[]);
      for(var i=0;i<pre.length;i++){
        var e=pre[i];
        var id=e.answer&&e.answer.id;
        if(id)AS.answers[e.blockId]=id;
      }
      var secs=a.sections||[];
      for(var si=0;si<secs.length;si++){
        var blocks=secs[si].blocks||[];
        for(var bi=0;bi<blocks.length;bi++){
          var b=blocks[bi];
          AS.blockMap[b.id]=b;
          AS.order.push(b.id);
        }
      }
      AS.total=AS.order.length;
      if(sub.status==='submitted'){AS.submitted=true;renderAssessmentReview();}
      else{renderAssessment();}
    })
    .catch(function(e){g('player-wrap').innerHTML='<div class="as-err">'+esc(e.message||e)+'</div>';});
}

function asAnsweredCount(){var n=0;for(var k in AS.answers)if(AS.answers[k])n++;return n;}

function renderAssessment(){
  var a=AS.state.assessment||{};
  var title=a.title||'Assessment';
  var curIdx=AS.curIdx;
  var blockId=AS.order[curIdx];
  var block=AS.blockMap[blockId];
  if(!block){renderAssessmentReview();return;}
  var bd=block.blockData||{};
  var qHtml=asWidgetHtml(bd.description&&bd.description.widgets);
  var opts=bd.options||[];
  var optsHtml='';
  var curAns=AS.answers[blockId];
  for(var i=0;i<opts.length;i++){
    var o=opts[i];
    var oHtml=asWidgetHtml(o.description&&o.description.widgets);
    var sel=curAns===o.id?' sel':'';
    optsHtml+='<div class="as-opt'+sel+'" data-opt="'+esc(o.id)+'"><div class="as-radio"></div><div class="as-opt-body">'+oHtml+'</div></div>';
  }
  if(bd.hasOptionOther){
    var otherSel=curAns&&curAns.indexOf('other:')===0?' sel':'';
    optsHtml+='<div class="as-opt'+otherSel+'" data-opt="other"><div class="as-radio"></div><div class="as-opt-body"><span>Other</span><input type="text" placeholder="your answer…" id="as-other-input" value="'+(otherSel?esc(curAns.slice(6)):'')+'"></div></div>';
  }
  var answered=asAnsweredCount();
  var pct=AS.total?Math.round(answered/AS.total*100):0;
  var html=
    '<div class="as-wrap"><div class="as-inner">'+
      '<div class="as-head">'+
        '<div><h1>'+esc(title)+'</h1>'+
          '<div class="as-sub">Question '+(curIdx+1)+' of '+AS.total+' · '+answered+' answered</div>'+
          '<div class="as-progress"><div style="width:'+pct+'%"></div></div>'+
        '</div>'+
      '</div>'+
      '<div class="as-q">'+
        '<div class="as-q-num">Question '+(curIdx+1)+' / '+AS.total+'</div>'+
        '<div class="as-q-text">'+qHtml+'</div>'+
        '<div class="as-opts">'+optsHtml+'</div>'+
      '</div>'+
      '<div class="as-actions">'+
        '<button class="as-btn" id="as-prev" '+(curIdx===0?'disabled':'')+'>← Prev</button>'+
        '<div style="display:flex;gap:10px">'+
          '<button class="as-btn primary" id="as-save">Save</button>'+
          (curIdx<AS.total-1
            ? '<button class="as-btn primary" id="as-next">Next →</button>'
            : '<button class="as-btn danger" id="as-submit">Submit</button>')+
        '</div>'+
      '</div>'+
    '</div></div>';
  g('player-wrap').innerHTML=html;
  setStatus('assessment · Q'+(curIdx+1),'status ok');
  // bind option clicks
  var optEls=g('player-wrap').querySelectorAll('.as-opt');
  for(var k=0;k<optEls.length;k++){
    (function(el){
      el.addEventListener('click',function(e){
        if(e.target&&e.target.tagName==='INPUT')return;
        var val=el.dataset.opt;
        if(val==='other'){
          var inp=g('as-other-input');
          AS.answers[blockId]='other:'+(inp?inp.value:'');
        }else{
          AS.answers[blockId]=val;
        }
        // rerender this question only — cheaper than full re-render? full is simpler
        renderAssessment();
      });
    })(optEls[k]);
  }
  // other input
  var oi=g('as-other-input');
  if(oi){
    oi.addEventListener('input',function(){AS.answers[blockId]='other:'+this.value;});
    oi.addEventListener('click',function(e){e.stopPropagation();});
  }
  on('as-prev',function(){AS.curIdx=Math.max(0,AS.curIdx-1);renderAssessment();});
  var nx=g('as-next');if(nx)nx.addEventListener('click',function(){autosave();AS.curIdx=Math.min(AS.total-1,AS.curIdx+1);renderAssessment();});
  var sv=g('as-save');if(sv)sv.addEventListener('click',function(){autosave();});
  var sb=g('as-submit');if(sb)sb.addEventListener('click',submitAssessment);
}

function asAnswersArray(){
  var arr=[];
  for(var bid in AS.answers){
    var v=AS.answers[bid];
    if(!v)continue;
    if(v.indexOf('other:')===0){
      arr.push({blockId:bid, answer:{text:v.slice(6)}});
    }else{
      arr.push({blockId:bid, answer:{id:v}});
    }
  }
  return arr;
}

function autosave(){
  if(!AS.submissionId||AS.submitted)return;
  var body={submission_id:AS.submissionId, answers:asAnswersArray()};
  fetch('/api/assessment/save/'+encodeURIComponent(AS.titleId)+'/'+encodeURIComponent(AS.unitId),
    {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)})
    .then(function(r){return r.json();})
    .then(function(j){if(j.success||j.updated)setStatus('saved ✓','status ok');})
    .catch(function(){});
}

function submitAssessment(){
  if(!AS.submissionId)return;
  var unanswered=AS.total-asAnsweredCount();
  if(unanswered>0){
    if(!confirm('You have '+unanswered+' unanswered question'+(unanswered>1?'s':'')+'. Submit anyway?'))return;
  }
  setStatus('submitting…','status');
  var body={submission_id:AS.submissionId, answers:asAnswersArray()};
  fetch('/api/assessment/submit/'+encodeURIComponent(AS.titleId)+'/'+encodeURIComponent(AS.unitId),
    {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)})
    .then(function(r){return r.json();})
    .then(function(j){
      if(j.error){setStatus('submit failed: '+j.error,'status err');return;}
      AS.submitted=true;
      // stash submission for review
      if(j.submission){AS.lastSubmission=j.submission;}
      // refetch state so feedback populates
      return fetch('/api/assessment/'+encodeURIComponent(AS.titleId)+'/'+encodeURIComponent(AS.unitId))
        .then(function(r){return r.json();})
        .then(function(fresh){
          AS.state=fresh;
          renderAssessmentReview();
        });
    })
    .catch(function(e){setStatus('submit error','status err');});
}

function renderAssessmentReview(){
  var a=AS.state.assessment||{};
  var sub=AS.state.latestSubmission||{};
  var feedback=AS.state.feedback||[];
  var title=a.title||'Assessment';
  // build blockId -> correctness map from submission.answers
  var grades={};
  var correctCount=0, gradedCount=0;
  var subAnswers=sub.answers||[];
  for(var i=0;i<subAnswers.length;i++){
    var e=subAnswers[i];
    grades[e.blockId]=e;
    if(e.graded){gradedCount++; if(e.correct)correctCount++;}
  }
  // build blockId -> feedback block (contains correct answer highlight info)
  var fbMap={};
  for(var fi=0;fi<feedback.length;fi++){
    var fsec=feedback[fi];
    var fblocks=fsec.blocks||[];
    for(var fbi=0;fbi<fblocks.length;fbi++){
      var fb=fblocks[fbi];
      fbMap[fb.id]=fb;
    }
  }
  var html='<div class="as-wrap"><div class="as-inner">';
  html+='<div class="as-head"><div><h1>'+esc(title)+'</h1><div class="as-sub">✓ Submitted · reviewed</div></div></div>';
  if(gradedCount>0){
    var pct=Math.round(correctCount/gradedCount*100);
    html+='<div class="as-score-card"><div class="num">'+correctCount+' / '+gradedCount+'</div><div class="lbl">'+pct+'% correct</div></div>';
  }else{
    html+='<div class="as-score-card"><div class="num">✓</div><div class="lbl">Submitted</div></div>';
  }
  for(var qi=0;qi<AS.order.length;qi++){
    var bid=AS.order[qi];
    var block=AS.blockMap[bid];
    if(!block)continue;
    var bd=block.blockData||{};
    var qHtml=asWidgetHtml(bd.description&&bd.description.widgets);
    var opts=bd.options||[];
    var userAns=AS.answers[bid];
    var grade=grades[bid];
    var fb=fbMap[bid];
    // try to find correct option id from feedback if present
    var correctOptId=null;
    if(fb&&fb.correctAnswer&&fb.correctAnswer.id)correctOptId=fb.correctAnswer.id;
    else if(fb&&fb.answer&&fb.answer.id&&grade&&grade.correct)correctOptId=fb.answer.id;
    var optsHtml='';
    for(var oi=0;oi<opts.length;oi++){
      var o=opts[oi];
      var oHtml=asWidgetHtml(o.description&&o.description.widgets);
      var cls='as-opt';
      var tag='';
      if(userAns===o.id){
        if(grade&&grade.correct){cls+=' correct';tag='<span class="as-tag ok">✓ correct</span>';}
        else if(grade&&!grade.correct){cls+=' wrong';tag='<span class="as-tag no">✗ wrong</span>';}
      }else if(correctOptId&&o.id===correctOptId){
        cls+=' correct';tag='<span class="as-tag ok">✓ answer</span>';
      }
      optsHtml+='<div class="'+cls+'"><div class="as-radio"></div><div class="as-opt-body">'+oHtml+'</div>'+tag+'</div>';
    }
    html+='<div class="as-review"><div class="as-q-num">Question '+(qi+1)+' / '+AS.total+'</div><div class="as-q-text">'+qHtml+'</div><div class="as-opts">'+optsHtml+'</div></div>';
  }
  html+='<div class="as-actions"><button class="as-btn" id="as-back">← Back</button><button class="as-btn primary" id="as-retake">Retake</button></div>';
  html+='</div></div>';
  g('player-wrap').innerHTML=html;
  setStatus('assessment · submitted','status ok');
  on('as-back',function(){toggleSections();});
  on('as-retake',function(){playAssessment(AS.titleId,AS.unitId);});
}
/* ================= end assessment ================= */

function playPdf(titleId,unitId){
  document.getElementById('player-wrap').innerHTML='<div class="player-empty">loading PDF…</div>';
  fetch('/api/pdf/'+encodeURIComponent(titleId)+'/'+encodeURIComponent(unitId)).then(function(r){return r.json();}).then(function(info){
    if(info.error){document.getElementById('player-wrap').innerHTML='<div class="player-empty"><p>PDF error: '+esc(info.error)+'</p></div>';return;}
    window._pdfInfo=info;
    document.getElementById('player-wrap').innerHTML='<div class="pdf-viewer"><div class="pdf-toolbar"><span class="name">📄 '+esc(info.display||info.filename)+'</span><div class="pdf-actions"><a href="'+esc(info.redirectUrl)+'" download="'+esc(info.filename)+'" target="_blank" class="primary">⬇ download</a><button onclick="pdfCopyUrl(this)">🔗 copy</button><button onclick="pdfNewTab()">↗ new tab</button></div></div><iframe class="pdf-frame" src="'+esc(info.redirectUrl)+'"></iframe></div>';
    document.getElementById('status').textContent='pdf';document.getElementById('status').className='status ok';
  });
}
window.pdfNewTab=function(){if(window._pdfInfo&&window._pdfInfo.redirectUrl)window.open(window._pdfInfo.redirectUrl,'_blank');};
window.pdfCopyUrl=function(btn){var item=FLAT[CURRENT];fetch('/api/pdf/'+encodeURIComponent(ACTIVE)+'/'+encodeURIComponent(item.unit.id)).then(function(r){return r.json();}).then(function(info){if(info.redirectUrl){navigator.clipboard.writeText(info.redirectUrl);var o=btn.textContent;btn.textContent='✓';setTimeout(function(){btn.textContent=o;},1200);}});};

window.togglePlay=function(){
  if(!VIDEO)return;
  if(VIDEO.paused||VIDEO.ended){var p=VIDEO.play();if(p&&p.catch)p.catch(function(){});}
  else VIDEO.pause();
};
window.toggleMute=function(){if(VIDEO){VIDEO.muted=!VIDEO.muted;if(!VIDEO.muted&&VIDEO.volume===0)VIDEO.volume=VOL||1;}};
window.skip=function(n){if(VIDEO)VIDEO.currentTime+=n;};
window.seekClick=function(e){if(!VIDEO)return;var r=e.currentTarget.getBoundingClientRect();VIDEO.currentTime=((e.clientX-r.left)/r.width)*(VIDEO.duration||0);};
window.playNext=function(){if(CURRENT!=null&&CURRENT<FLAT.length-1)playUnit(CURRENT+1);};
window.playPrev=function(){if(CURRENT!=null&&CURRENT>0)playUnit(CURRENT-1);};

function fsEl(){return document.fullscreenElement||document.webkitFullscreenElement;}
function leaveFS(){
  if(fsEl()){
    if(document.exitFullscreen)document.exitFullscreen();
    else if(document.webkitExitFullscreen)document.webkitExitFullscreen();
  }
}
window.toggleFS=function(){
  var w=document.getElementById('player-wrap');
  if(!fsEl()){
    var p=null;
    if(w.requestFullscreen)p=w.requestFullscreen();
    else if(w.webkitRequestFullscreen)p=w.webkitRequestFullscreen();
    else if(w.msRequestFullscreen)p=w.msRequestFullscreen();
    else if(VIDEO&&VIDEO.webkitEnterFullscreen){VIDEO.webkitEnterFullscreen();return;}
    if(p&&p.then){
      p.then(function(){
        try{if(window.innerWidth<=900&&screen.orientation&&screen.orientation.lock){screen.orientation.lock('landscape').catch(function(){});}}catch(e){}
      }).catch(function(){});
    }
  }else{
    leaveFS();
  }
};
function onFsChange(){
  var b=g('yt-fs');if(b)b.innerHTML=ic(fsEl()?'exitfs':'fs');
  if(!fsEl()){try{if(screen.orientation&&screen.orientation.unlock)screen.orientation.unlock();}catch(e){}}
}
document.addEventListener('fullscreenchange',onFsChange);
document.addEventListener('webkitfullscreenchange',onFsChange);

window.openDownload=function(){
  if(!CURRENT_INFO)return;
  if(CURRENT_INFO.type==='pdf'){var a=document.querySelector('.pdf-actions a.primary');if(a)a.click();return;}
  if(CURRENT_INFO.type==='assessment'){alert('assessment has no download');return;}
  var box=document.getElementById('dl-variants');box.innerHTML='';
  var items=Object.entries(CURRENT_VARIANTS).sort(function(a,b){return parseInt(b[0])-parseInt(a[0]);});
  if(!items.length){box.innerHTML='<p style="color:var(--muted)">no variants</p>';document.getElementById('modal-dl').classList.add('open');return;}
  for(var i=0;i<items.length;i++){
    var q=items[i][0],url=items[i][1];
    var el=document.createElement('div');el.className='variant';
    el.innerHTML='<div style="display:flex;justify-content:space-between;align-items:center;gap:10px"><span class="name">'+esc(q)+'</span><button data-url="'+esc(url)+'" data-q="'+esc(q)+'" class="dlbtn">download</button></div>';
    box.appendChild(el);
  }
  var btns=box.querySelectorAll('.dlbtn');
  for(var j=0;j<btns.length;j++){(function(b){b.onclick=function(){browserHlsDownload(b.dataset.url,(CURRENT_INFO.title||'video'),b.dataset.q);};})(btns[j]);}
  document.getElementById('modal-dl').classList.add('open');
};
function browserHlsDownload(masterUrl,title,quality){
  closeModal('modal-dl');
  var status=document.getElementById('status');status.textContent='download starting…';
  fetch(masterUrl).then(function(r){return r.text();}).then(function(m){
    var lines=m.split(/\r?\n/);var base=masterUrl.substring(0,masterUrl.lastIndexOf('/')+1);var segs=[];
    for(var i=0;i<lines.length;i++){var t=lines[i].trim();if(!t||t.charAt(0)==='#')continue;var abs=t;if(t.indexOf('http')!==0){if(t.charAt(0)==='/')abs=(new URL(masterUrl)).origin+t;else abs=base+t;}segs.push(abs);}
    if(!segs.length)throw new Error('no segments');
    var buffers=[];var done=0;var cursor=0;
    function worker(){var i=cursor++;if(i>=segs.length)return Promise.resolve();return fetch(segs[i]).then(function(r){return r.arrayBuffer();}).then(function(buf){buffers[i]=buf;}).catch(function(){buffers[i]=new Uint8Array(0);}).then(function(){done++;status.textContent='fetching '+done+'/'+segs.length;return worker();});}
    var workers=[];for(var w=0;w<6;w++)workers.push(worker());
    return Promise.all(workers).then(function(){
      status.textContent='assembling…';
      var total=0;for(var i=0;i<buffers.length;i++)total+=buffers[i].byteLength;
      var out=new Uint8Array(total);var off=0;
      for(var i=0;i<buffers.length;i++){out.set(new Uint8Array(buffers[i]),off);off+=buffers[i].byteLength;}
      var blob=new Blob([out],{type:'video/mp2t'});var url=URL.createObjectURL(blob);
      var a=document.createElement('a');a.href=url;a.download=(title.replace(/[\\/:*?"<>|]/g,'_').slice(0,80))+'_'+quality+'.ts';
      document.body.appendChild(a);a.click();document.body.removeChild(a);
      setTimeout(function(){URL.revokeObjectURL(url);},60000);
      status.textContent='✓ downloaded';status.className='status ok';
    });
  }).catch(function(e){status.textContent='error: '+e.message;status.className='status err';});
}
window.openLink=function(){
  if(!CURRENT_INFO||!CURRENT_INFO.sourceid){alert('no video loaded');return;}
  var master='https://fast.wistia.com/embed/medias/'+CURRENT_INFO.sourceid+'.m3u8';
  document.getElementById('link-master').value=master;
  var box=document.getElementById('link-variants');box.innerHTML='<p style="color:var(--muted);font-size:12px">loading…</p>';
  fetch('/api/variants/'+encodeURIComponent(CURRENT_INFO.sourceid)).then(function(r){return r.json();}).then(function(j){
    CURRENT_VARIANTS=(j&&j.variants)||{};
    var items=Object.entries(CURRENT_VARIANTS).sort(function(a,b){return parseInt(b[0])-parseInt(a[0]);});
    if(!items.length){box.innerHTML='<p style="color:var(--muted);font-size:12px">no variants</p>';}
    else{box.innerHTML='';for(var i=0;i<items.length;i++){var q=items[i][0],url=items[i][1];var el=document.createElement('div');el.className='variant';el.innerHTML='<div style="display:flex;justify-content:space-between;align-items:center;gap:10px;margin-bottom:8px"><span class="name">'+esc(q)+'</span><button data-url="'+esc(url)+'" class="copybtn">copy</button></div><input value="'+esc(url)+'" readonly onclick="this.select()" style="font:11px monospace">';box.appendChild(el);}
      var btns=box.querySelectorAll('.copybtn');for(var j=0;j<btns.length;j++){(function(b){b.onclick=function(){copyText(b.dataset.url,b);};})(btns[j]);}}
    document.getElementById('modal-link').classList.add('open');
  });
};
function copyText(t,btn){navigator.clipboard.writeText(t).then(function(){var o=btn.textContent;btn.textContent='✓';setTimeout(function(){btn.textContent=o;},1200);}).catch(function(){var ta=document.createElement('textarea');ta.value=t;document.body.appendChild(ta);ta.select();document.execCommand('copy');document.body.removeChild(ta);var o=btn.textContent;btn.textContent='✓';setTimeout(function(){btn.textContent=o;},1200);});}
window.closeModal=function(id){document.getElementById(id).classList.remove('open');};
window.copyField=function(id,btn){var el=document.getElementById(id);el.select();el.setSelectionRange(0,99999);navigator.clipboard.writeText(el.value).then(function(){var o=btn.textContent;btn.textContent='copied!';setTimeout(function(){btn.textContent=o;},1200);});};
window.copyUpi=function(btn){var id=document.getElementById('upi-id').textContent.trim();navigator.clipboard.writeText(id).then(function(){var o=btn.textContent;btn.textContent='✓ copied';setTimeout(function(){btn.textContent=o;},1200);});};
var modals=document.querySelectorAll('.modal');for(var mi=0;mi<modals.length;mi++){(function(m){m.addEventListener('click',function(e){if(e.target===m)m.classList.remove('open');});})(modals[mi]);}
document.addEventListener('keydown',function(e){
  if(e.target.tagName==='INPUT'||e.target.tagName==='SELECT'||e.target.tagName==='TEXTAREA')return;
  var k=e.key;
  if(k==='/'){e.preventDefault();if(document.getElementById('page-viewer').classList.contains('active'))document.getElementById('search').focus();else document.getElementById('batch-search').focus();return;}
  if(!VIDEO)return;
  if(k===' '||k==='k'||k==='K'){e.preventDefault();togglePlay();showUI();}
  else if(k==='ArrowRight'||k==='l'||k==='L'){e.preventDefault();doSeek('r');showUI();}
  else if(k==='ArrowLeft'||k==='j'||k==='J'){e.preventDefault();doSeek('l');showUI();}
  else if(k==='ArrowUp'){e.preventDefault();VIDEO.muted=false;VIDEO.volume=Math.min(1,VIDEO.volume+0.05);showUI();}
  else if(k==='ArrowDown'){e.preventDefault();VIDEO.volume=Math.max(0,VIDEO.volume-0.05);showUI();}
  else if(k==='f'||k==='F')toggleFS();
  else if(k==='n'||k==='N')playNext();
  else if(k==='p'||k==='P')playPrev();
  else if(k==='m'||k==='M'){VIDEO.muted=!VIDEO.muted;showUI();}
  else if(k==='Escape'&&document.getElementById('sections-overlay').classList.contains('open')){document.getElementById('sections-overlay').classList.remove('open');}
});
document.getElementById('search').addEventListener('input',renderTOC);
document.getElementById('batch-search').addEventListener('input',renderBatches);
function loadAll(){
  var grid=document.getElementById('batch-grid');
  grid.innerHTML='<div style="padding:24px;color:var(--muted);text-align:center;grid-column:1/-1">loading…</div>';
  fetch('/api/batches').then(function(r){return r.json();}).then(function(j){
    BATCHES=(j&&j.batches)||[];renderBatches();
  }).catch(function(e){grid.innerHTML='<div style="padding:24px;color:#ff7a7a;text-align:center;grid-column:1/-1">error: '+esc(e.message||e)+'</div>';});
}
if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',loadAll);}else{loadAll();}
})();
</script>
</body></html>"""


LOGIN_PAGE = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Admin · 𝐒𝐞𝐨𝐧𝐠𝐒𝐭𝐮𝐝𝐲𝐄𝐫𝐚</title>
<link rel="icon" href="https://i.ibb.co/GQvZNJ5x/file-00000000a2d082088bb8b30c95b7d8b9.png">
<style>
body{margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;background:#07090c;color:#e6e9ee;font:14px -apple-system,monospace;padding:20px}
.card{background:#0e1218;border:1px solid #1e2630;border-radius:16px;padding:32px 28px;width:100%;max-width:420px;box-shadow:0 24px 60px rgba(0,0,0,.55)}
.logo{width:64px;height:64px;border-radius:14px;display:block;margin:0 auto 14px;background:#000;border:1px solid #1e2630}
h1{margin:0 0 6px;font-size:22px;text-align:center;background:linear-gradient(90deg,#5c8dff,#7c5cff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.sub{color:#7c8697;font-size:11.5px;text-align:center;margin-bottom:26px}
.sub a{color:#5c8dff;text-decoration:none}
label{display:block;font-size:11px;color:#7c8697;text-transform:uppercase;letter-spacing:.6px;margin:16px 0 6px;font-weight:600}
input{width:100%;padding:13px 14px;background:#07090c;border:1px solid #1e2630;color:#e6e9ee;font:inherit;border-radius:10px;min-height:48px;font-size:15px;letter-spacing:3px;text-align:center;box-sizing:border-box}
input:focus{outline:none;border-color:#5c8dff}
button{margin-top:22px;width:100%;padding:15px;background:linear-gradient(90deg,#5c8dff,#7c5cff);color:#fff;border:0;border-radius:10px;font:inherit;font-weight:700;cursor:pointer;min-height:50px;font-size:15px}
.err{margin-top:16px;padding:12px 14px;background:rgba(255,92,92,.1);border:1px solid rgba(255,92,92,.3);border-radius:8px;color:#ff8b8b;font-size:12.5px}
.foot{margin-top:22px;text-align:center;color:#7c8697;font-size:11px}
</style></head><body>
<form class="card" method="POST" action="/admin">
  <img class="logo" src="https://i.ibb.co/GQvZNJ5x/file-00000000a2d082088bb8b30c95b7d8b9.png" alt="logo">
  <h1>𝐒𝐞𝐨𝐧𝐠𝐒𝐭𝐮𝐝𝐲𝐄𝐫𝐚</h1>
  <p class="sub">Admin · <a href="https://t.me/SeongEraStudy" target="_blank">t.me/SeongEraStudy</a></p>
  <label>Admin Code</label>
  <input type="password" name="code" required autofocus autocomplete="off" inputmode="numeric" maxlength="8" pattern="[0-9]{8}" placeholder="••••••••">
  {% if error %}<div class="err">{{ error }}</div>{% endif %}
  <button type="submit">Unlock</button>
</form></body></html>"""


ADMIN_PAGE = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Admin · 𝐒𝐞𝐨𝐧𝐠𝐒𝐭𝐮𝐝𝐲𝐄𝐫𝐚</title>
<link rel="icon" href="https://i.ibb.co/GQvZNJ5x/file-00000000a2d082088bb8b30c95b7d8b9.png">
<style>
body{margin:0;min-height:100vh;background:#07090c;color:#e6e9ee;font:14px -apple-system,monospace}
.header{padding:20px 24px;background:linear-gradient(180deg,#141a22,#0a0e14);border-bottom:1px solid #1e2630;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px}
.header .hd{display:flex;align-items:center;gap:12px}
.header img{width:40px;height:40px;border-radius:10px;background:#000;border:1px solid #1e2630}
h1{margin:0;font-size:18px;background:linear-gradient(90deg,#5c8dff,#7c5cff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.nav{display:flex;gap:8px}
.btn{padding:10px 16px;background:#141a22;border:1px solid #1e2630;color:#e6e9ee;border-radius:9px;font:inherit;font-weight:600;font-size:12.5px;cursor:pointer;min-height:40px;display:inline-flex;align-items:center;text-decoration:none}
.btn:hover{border-color:#5c8dff;color:#5c8dff}
.btn.danger:hover{border-color:#ff5c5c;color:#ff5c5c}
.wrap{max-width:900px;margin:0 auto;padding:24px 20px 60px}
.card{background:#0e1218;border:1px solid #1e2630;border-radius:14px;padding:24px;margin-bottom:20px}
.card h2{margin:0 0 16px;font-size:16px}
label{display:block;font-size:11px;color:#7c8697;text-transform:uppercase;letter-spacing:.6px;margin:12px 0 6px;font-weight:600}
input,textarea{width:100%;padding:12px 14px;background:#07090c;border:1px solid #1e2630;color:#e6e9ee;font:inherit;border-radius:10px;min-height:46px;box-sizing:border-box}
textarea{font:12px monospace;min-height:80px}
input:focus,textarea:focus{outline:none;border-color:#5c8dff}
.btn-primary{margin-top:14px;padding:12px 22px;background:linear-gradient(90deg,#5c8dff,#7c5cff);color:#fff;border:0;border-radius:10px;font:inherit;font-weight:700;cursor:pointer;min-height:46px;font-size:14px}
.row{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:14px;background:#07090c;border:1px solid #1e2630;border-radius:10px;margin-bottom:10px;flex-wrap:wrap}
.info{display:flex;flex-direction:column;gap:4px;min-width:0;flex:1}
.em{color:#dfe6f0;font-weight:600;word-break:break-all;font-size:13px}
.lb{color:#7c8697;font-size:11.5px}
.tk{color:#9fb8ff;font:11px monospace;word-break:break-all}
.token-status{padding:4px 10px;border-radius:12px;font-size:11px;font-weight:600}
.token-ok{background:rgba(46,204,113,.1);color:#2ecc71;border:1px solid rgba(46,204,113,.3)}
.token-warn{background:rgba(246,183,60,.1);color:#f6b73c;border:1px solid rgba(246,183,60,.3)}
.token-bad{background:rgba(255,92,92,.1);color:#ff5c5c;border:1px solid rgba(255,92,92,.3)}
.msg{margin-top:12px;padding:11px 14px;border-radius:8px;font-size:12.5px;display:none}
.msg.show{display:block}
.msg.ok{background:rgba(46,204,113,.1);color:#2ecc71}
.msg.err{background:rgba(255,92,92,.1);color:#ff8b8b}
.help{padding:14px;background:#07090c;border-radius:10px;font-size:12px;color:#7c8697;line-height:1.7;margin-top:12px}
.help code{background:#141a22;padding:2px 6px;border-radius:4px;color:#9fb8ff;font-size:11px}
</style></head><body>
<div class="header">
  <div class="hd">
    <img src="https://i.ibb.co/GQvZNJ5x/file-00000000a2d082088bb8b30c95b7d8b9.png" alt="logo">
    <h1>𝐒𝐞𝐨𝐧𝐠𝐒𝐭𝐮𝐝𝐲𝐄𝐫𝐚 · Admin</h1>
  </div>
  <div class="nav">
    <a href="/" class="btn">← Site</a>
    <a href="https://t.me/SeongEraStudy" target="_blank" class="btn">📢 Channel</a>
    <button class="btn danger" onclick="logout()">Logout</button>
  </div>
</div>
<div class="wrap">
  <div class="card">
    <h2>Add Account</h2>
    <form id="add-form">
      <label>Email</label>
      <input name="email" type="email" required>
      <label>Access Token</label>
      <textarea name="token" required placeholder="paste access_token here"></textarea>
      <label>Label (optional)</label>
      <input name="label" type="text" placeholder="e.g. Main">
      <button type="submit" class="btn-primary">Add Account</button>
      <div id="add-msg" class="msg"></div>
    </form>
    <div class="help">
      <b>How to get the token:</b><br>
      1. Log in to <code>apnacollege.in</code><br>
      2. DevTools → Application → Cookies → <code>www.apnacollege.in</code><br>
      3. Copy <code>lw_tokens</code> → extract only <code>access_token</code> value<br>
      4. Paste. Valid <b>7 days</b>.
    </div>
  </div>
  <div class="card">
    <h2>Accounts (<span id="count">0</span>)</h2>
    <div id="list"></div>
    <div style="margin-top:14px;display:flex;gap:10px;flex-wrap:wrap">
      <button class="btn" onclick="testAll()">Test All</button>
      <button class="btn" onclick="reload()">Refresh</button>
      <button class="btn" onclick="clearCache()">Clear Batch Cache</button>
    </div>
    <div id="test-msg" class="msg"></div>
  </div>
</div>
<script>
async function reload(){
  const r=await fetch('/api/admin/accounts');
  const j=await r.json();
  const list=document.getElementById('list');
  const accts=j.accounts||[];
  document.getElementById('count').textContent=accts.length;
  if(!accts.length){list.innerHTML='<p style="color:#7c8697">No accounts.</p>';return;}
  list.innerHTML=accts.map(a=>`
    <div class="row">
      <div class="info">
        <span class="em">${a.display}</span>
        <span class="lb">${a.label||''} · ${a.added_ago||''}</span>
        <span class="tk">${a.token_prefix||''}…</span>
      </div>
      <span class="token-status ${a.status_class}">${a.status_text}</span>
      <button class="btn danger" onclick="removeAcct('${a.email}')">Remove</button>
    </div>`).join('');
}
async function addAcct(e){
  e.preventDefault();
  const f=e.target;
  const r=await fetch('/api/admin/accounts',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({email:f.email.value,token:f.token.value,label:f.label.value})});
  const j=await r.json();
  const msg=document.getElementById('add-msg');
  msg.textContent=j.error||(j.ok?'added ✓':'');
  msg.className='msg show '+(j.ok?'ok':'err');
  if(j.ok){f.reset();reload();}
}
async function removeAcct(email){
  if(!confirm('Remove '+email+'?'))return;
  await fetch('/api/admin/accounts',{method:'DELETE',headers:{'Content-Type':'application/json'},body:JSON.stringify({email})});
  reload();
}
async function testAll(){
  const msg=document.getElementById('test-msg');
  msg.textContent='testing…';msg.className='msg show';
  const r=await fetch('/api/admin/test');
  const j=await r.json();
  msg.textContent=(j.results||[]).map(x=>`${x.email}: ${x.ok?'✓':'✗ '+x.error}`).join(' · ');
  msg.className='msg show '+(j.results&&j.results.every(x=>x.ok)?'ok':'err');
}
async function clearCache(){await fetch('/api/admin/clear_batch_cache');alert('cache cleared');}
async function logout(){await fetch('/logout',{method:'POST'});location.href='/';}
document.getElementById('add-form').addEventListener('submit',addAcct);
reload();
</script></body></html>"""

