"""Player + assessment CSS (injected into MAIN_PAGE)."""

PLAYER_CSS = r"""
/* ===== youtube-style player ===== */
.yt{position:absolute;inset:0;background:#000;overflow:hidden;color:#fff;font-family:-apple-system,"Segoe UI",Roboto,sans-serif;-webkit-user-select:none;user-select:none;-webkit-touch-callout:none}
.yt:not(.show){cursor:none}
.yt video{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;background:#000}
.yt button{background:none;border:0;color:#fff;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;line-height:0;padding:0;border-radius:50%;font:inherit;transition:background .18s ease,transform .12s cubic-bezier(.34,1.56,.64,1)}
.yt button:active{transform:scale(.9)}
.yt button[disabled]{opacity:.3;pointer-events:none!important}
.yt button>svg{display:block;width:100%;height:100%;max-width:100%;max-height:100%;pointer-events:none;stroke:currentColor;fill:none}
.yt-gl{position:absolute;inset:0;z-index:2;touch-action:manipulation}
.yt-logo{position:absolute;right:14px;top:12px;z-index:3;font-weight:800;font-size:13px;letter-spacing:.5px;opacity:.7;pointer-events:none}
.yt.show .yt-logo{opacity:.9}
.yt-top{position:absolute;left:0;right:0;top:0;z-index:4;padding:14px 100px 40px 16px;background:linear-gradient(180deg,rgba(0,0,0,.82),rgba(0,0,0,.35) 55%,transparent);opacity:0;transform:translateY(-8px);transition:opacity .3s cubic-bezier(.22,.9,.28,1),transform .3s cubic-bezier(.22,.9,.28,1);pointer-events:none}
.yt.show .yt-top{opacity:1;transform:translateY(0)}
.yt-title{font-size:14px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;text-shadow:0 1px 3px rgba(0,0,0,.7);flex:1;min-width:0}
.yt-center{position:absolute;inset:0;z-index:4;display:flex;align-items:center;justify-content:center;gap:clamp(24px,12vw,90px);opacity:0;transition:opacity .3s cubic-bezier(.22,.9,.28,1);pointer-events:none}
.yt-center button{pointer-events:none;background:rgba(0,0,0,.5);backdrop-filter:blur(3px);box-shadow:0 6px 24px rgba(0,0,0,.4)}
.yt.show .yt-center{opacity:1}
.yt.show .yt-center button{pointer-events:auto}
.yt-sb{width:56px;height:56px;padding:0;display:inline-flex;align-items:center;justify-content:center}
.yt-sb>svg{width:30px!important;height:30px!important}
.yt-sb:hover{background:rgba(0,0,0,.72);transform:scale(1.08)}
.yt-big{width:82px;height:82px;padding:0;display:inline-flex;align-items:center;justify-content:center}
.yt-big>svg{width:44px!important;height:44px!important}
.yt-big:hover{transform:scale(1.1);background:rgba(0,0,0,.72)}
.yt-paused .yt-big{animation:yt-pulse 1.8s ease-in-out infinite}
@keyframes yt-pulse{0%,100%{box-shadow:0 6px 24px rgba(0,0,0,.4),0 0 0 0 rgba(255,255,255,.28)}50%{box-shadow:0 6px 24px rgba(0,0,0,.4),0 0 0 18px rgba(255,255,255,0)}}
.yt-bottom{position:absolute;left:0;right:0;bottom:0;z-index:4;padding:40px 12px 10px;background:linear-gradient(0deg,rgba(0,0,0,.9),rgba(0,0,0,.4) 55%,transparent);opacity:0;transform:translateY(8px);transition:opacity .3s cubic-bezier(.22,.9,.28,1),transform .3s cubic-bezier(.22,.9,.28,1);pointer-events:none}
.yt.show .yt-bottom{opacity:1;transform:translateY(0);pointer-events:auto}
.yt.buf .yt-big{opacity:0}
.yt-pb{position:relative;height:28px;margin:0 4px;display:flex;align-items:center;cursor:pointer;touch-action:none}
.yt-track{position:relative;width:100%;height:4px;background:rgba(255,255,255,.28);border-radius:3px;transition:height .18s cubic-bezier(.22,.9,.28,1)}
.yt-pb:hover .yt-track,.yt-pb.drag .yt-track{height:6px}
.yt-buf{position:absolute;left:0;top:0;bottom:0;width:0;background:rgba(255,255,255,.42);border-radius:3px}
.yt-fill{position:absolute;left:0;top:0;bottom:0;width:0;background:linear-gradient(90deg,var(--accent),var(--accent2));border-radius:3px;box-shadow:0 0 12px rgba(92,141,255,.6)}
.yt-knob{position:absolute;top:50%;left:0;width:14px;height:14px;border-radius:50%;background:#fff;transform:translate(-50%,-50%);box-shadow:0 0 0 3px rgba(255,255,255,.15);transition:width .18s,height .18s}
.yt-pb:hover .yt-knob,.yt-pb.drag .yt-knob{width:18px;height:18px;box-shadow:0 0 0 5px rgba(92,141,255,.32)}
.yt-tip{position:absolute;bottom:32px;left:0;transform:translateX(-50%);background:rgba(0,0,0,.88);padding:4px 10px;border-radius:7px;font-size:12px;opacity:0;pointer-events:none;white-space:nowrap;font-variant-numeric:tabular-nums}
.yt-pb:hover .yt-tip,.yt-pb.drag .yt-tip{opacity:1}
.yt-row{display:flex;align-items:center;justify-content:space-between;gap:8px;min-height:52px}
.yt-l,.yt-r{display:flex;align-items:center;gap:6px}
.yb{width:46px;height:46px;padding:0;display:inline-flex;align-items:center;justify-content:center}
.yb>svg{width:26px!important;height:26px!important}
.yb:hover{background:rgba(255,255,255,.14)}
.yt-time{font-size:13px;margin-left:10px;white-space:nowrap;text-shadow:0 1px 2px #000;font-variant-numeric:tabular-nums}
.yt-volwrap{display:inline-flex;align-items:center;height:46px}
.yt-vol{-webkit-appearance:none;appearance:none;width:0;opacity:0;height:4px;border-radius:2px;background:rgba(255,255,255,.3);outline:0;padding:0;margin:0;transition:width .22s,opacity .22s;align-self:center}
.yt-volwrap:hover .yt-vol{width:80px;opacity:1;margin:0 10px 0 4px}
.yt-vol::-webkit-slider-thumb{-webkit-appearance:none;width:14px;height:14px;border-radius:50%;background:#fff;border:0;box-shadow:0 0 0 2px rgba(0,0,0,.3)}
.yt-vol::-moz-range-thumb{width:14px;height:14px;border-radius:50%;background:#fff;border:0;box-shadow:0 0 0 2px rgba(0,0,0,.3)}
@media (hover:none){.yt-vol{display:none}}
@media (max-width:520px){
  .yt-hide-sm{display:none!important}
  .yb{width:42px;height:42px}
  .yb>svg{width:24px!important;height:24px!important}
  .yt-sb{width:50px;height:50px}
  .yt-sb>svg{width:26px!important;height:26px!important}
  .yt-big{width:72px;height:72px}
  .yt-big>svg{width:38px!important;height:38px!important}
}
.yt-rip{position:absolute;top:0;bottom:0;width:38%;z-index:3;display:flex;align-items:center;justify-content:center;opacity:0;pointer-events:none;transition:opacity .25s;background:radial-gradient(circle at 50% 50%,rgba(255,255,255,.22),rgba(255,255,255,.04) 70%);font-size:13px;font-weight:700;text-align:center}
.yt-rip.l{left:0;border-radius:0 100% 100% 0/0 50% 50% 0}
.yt-rip.r{right:0;border-radius:100% 0 0 100%/50% 0 0 50%}
.yt-rip.on{opacity:1}
.yt-rip .in{display:flex;flex-direction:column;align-items:center;gap:4px}
.yt-rip .flip svg{transform:scaleX(-1)}
.yt-2x{position:absolute;top:14px;left:50%;transform:translateX(-50%);z-index:5;background:rgba(0,0,0,.75);padding:7px 16px;border-radius:20px;font-size:13px;font-weight:700;opacity:0;pointer-events:none;white-space:nowrap;backdrop-filter:blur(6px);border:1px solid rgba(255,255,255,.1)}
.yt-2x.on{opacity:1}
.yt-spin{position:absolute;top:50%;left:50%;width:48px;height:48px;margin:-24px 0 0 -24px;border:4px solid rgba(255,255,255,.22);border-top-color:var(--accent);border-radius:50%;z-index:3;display:none;pointer-events:none;animation:ytspin .85s linear infinite}
.yt-spin.on{display:block}
@keyframes ytspin{to{transform:rotate(360deg)}}
.yt-menu{position:absolute;right:10px;bottom:80px;z-index:6;min-width:230px;max-width:88%;max-height:70%;overflow-y:auto;background:rgba(16,20,28,.98);border:1px solid var(--line);border-radius:14px;padding:6px;display:none;box-shadow:0 24px 60px rgba(0,0,0,.7);backdrop-filter:blur(10px)}
.yt-menu.open{display:block}
.yt-menu .mi,.yt-menu .mh{display:flex;justify-content:space-between;align-items:center;gap:16px;padding:11px 13px;border-radius:9px;cursor:pointer;font-size:13px;min-height:44px}
.yt-menu .mi:hover{background:rgba(255,255,255,.1)}
.yt-menu .mh{font-weight:700;border-bottom:1px solid var(--line);border-radius:0;margin-bottom:4px}
.yt-menu .mi .v{color:var(--muted);font-size:12px}
.yt-menu .mi.sel{color:var(--accent);font-weight:700}

/* ===== assessment ===== */
.as-wrap{position:absolute;inset:0;background:var(--bg);overflow-y:auto;color:var(--txt);font-family:-apple-system,"Segoe UI",Roboto,sans-serif}
.as-inner{max-width:820px;margin:0 auto;padding:24px 18px 96px}
.as-head{margin-bottom:22px;padding-bottom:18px;border-bottom:1px solid var(--line)}
.as-head h1{margin:0 0 6px;font-size:22px;font-weight:800;line-height:1.3}
.as-head .as-sub{color:var(--muted);font-size:12.5px}
.as-progress{margin-top:14px;width:100%;height:6px;background:var(--panel2);border-radius:3px;overflow:hidden}
.as-progress > div{height:100%;background:linear-gradient(90deg,var(--accent),var(--accent2));width:0;transition:width .3s}
.as-q{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:22px;margin-bottom:18px}
.as-q .as-q-num{color:var(--muted);font-size:11.5px;text-transform:uppercase;letter-spacing:.7px;font-weight:700;margin-bottom:10px}
.as-q .as-q-text{font-size:15.5px;line-height:1.75;color:#dfe6f0;margin-bottom:18px}
.as-q .as-q-text p{margin:0 0 12px}
.as-q .as-q-text sup{font-size:.7em;vertical-align:super}
.as-opts{display:flex;flex-direction:column;gap:10px}
.as-opt{display:flex;align-items:flex-start;gap:12px;padding:14px 16px;background:var(--panel2);border:1px solid var(--line);border-radius:11px;cursor:pointer;min-height:52px}
.as-opt:hover{border-color:var(--accent);background:rgba(92,141,255,.06)}
.as-opt.sel{border-color:var(--accent);background:linear-gradient(90deg,rgba(92,141,255,.14),rgba(124,92,255,.05))}
.as-opt.correct{border-color:var(--good);background:rgba(46,204,113,.1)}
.as-opt.correct .as-radio{border-color:var(--good);background:var(--good)}
.as-opt.wrong{border-color:#ff5c5c;background:rgba(255,92,92,.1)}
.as-opt.wrong .as-radio{border-color:#ff5c5c;background:#ff5c5c}
.as-radio{width:22px;height:22px;border-radius:50%;border:2px solid var(--muted);flex-shrink:0;display:flex;align-items:center;justify-content:center;margin-top:1px}
.as-opt.sel .as-radio{border-color:var(--accent);background:var(--accent)}
.as-opt.sel .as-radio::after{content:"";width:8px;height:8px;background:#fff;border-radius:50%}
.as-opt-body{flex:1;line-height:1.6;font-size:14.5px;color:#dfe6f0}
.as-tag{padding:3px 9px;border-radius:8px;font-size:10.5px;font-weight:700;text-transform:uppercase;letter-spacing:.5px;align-self:flex-start;margin-left:auto}
.as-tag.ok{background:rgba(46,204,113,.2);color:var(--good)}
.as-tag.no{background:rgba(255,92,92,.2);color:#ff5c5c}
.as-actions{position:sticky;bottom:0;display:flex;justify-content:space-between;gap:10px;padding:14px 18px;background:linear-gradient(0deg,var(--bg) 60%,transparent);margin:0 -18px;flex-wrap:wrap;z-index:5}
.as-btn{padding:13px 22px;border-radius:10px;font:inherit;font-weight:700;font-size:14px;cursor:pointer;border:1px solid var(--line);background:var(--panel2);color:var(--txt);min-height:48px;display:inline-flex;align-items:center;gap:8px}
.as-btn>svg{width:18px;height:18px;stroke:currentColor;fill:none;stroke-width:2}
.as-btn:hover:not(:disabled){border-color:var(--accent)}
.as-btn:disabled{opacity:.4;cursor:not-allowed}
.as-btn.primary{background:linear-gradient(90deg,var(--accent),var(--accent2));color:#fff;border:0}
.as-btn.danger{background:linear-gradient(90deg,#ff5c5c,#b35cff);color:#fff;border:0}
.as-review{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:22px;margin-bottom:16px}
.as-score-card{background:linear-gradient(135deg,rgba(92,141,255,.14),rgba(124,92,255,.05) 60%,transparent);border:1px solid var(--line);border-radius:16px;padding:24px;margin-bottom:20px;display:flex;align-items:center;gap:24px;flex-wrap:wrap;justify-content:center}
.as-pie{position:relative;width:120px;height:120px;flex-shrink:0}
.as-pie svg{transform:rotate(-90deg)}
.as-pie .c{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center}
.as-pie .c .pct{font-size:26px;font-weight:800;background:linear-gradient(90deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.as-pie .c .lbl{font-size:9px;color:var(--muted);text-transform:uppercase;letter-spacing:.8px;margin-top:3px;font-weight:700}
.as-score-info{text-align:center;min-width:180px}
.as-score-info .big{font-size:34px;font-weight:800;background:linear-gradient(90deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.as-score-info .sub{color:var(--muted);font-size:12px;text-transform:uppercase;letter-spacing:.8px;margin-top:6px;font-weight:700}
.as-score-info .legend{margin-top:14px;display:flex;flex-direction:column;gap:6px;align-items:flex-start}
.as-score-info .legend .row{display:flex;align-items:center;gap:8px;font-size:12.5px}
.as-score-info .legend .dot{width:10px;height:10px;border-radius:50%}
.as-score-info .legend .dot.ok{background:var(--good)}
.as-score-info .legend .dot.no{background:#ff5c5c}
.as-score-info .legend .dot.neutral{background:var(--muted)}
.as-coming{display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;padding:60px 24px;color:var(--muted);text-align:center;gap:16px}
.as-coming .as-icon{width:72px;height:72px;border-radius:18px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;color:#fff}
.as-coming .as-icon svg{width:36px;height:36px;stroke:currentColor;fill:none;stroke-width:2}
.as-coming h2{margin:0;font-size:22px;color:#dfe6f0}
.as-coming p{margin:0;font-size:13.5px;max-width:420px;line-height:1.7}
.as-loading{display:flex;align-items:center;justify-content:center;height:100%;color:var(--muted);flex-direction:column;gap:16px}
.as-loading .sp{width:40px;height:40px;border:3px solid var(--panel2);border-top-color:var(--accent);border-radius:50%;animation:ytspin .85s linear infinite}
.as-err{color:#ff7a7a;text-align:center;padding:32px;font-family:monospace}

/* ===== sections overlay ===== */
.sections-overlay{position:fixed;top:0;left:0;bottom:0;width:420px;max-width:92vw;background:var(--panel);border-right:1px solid var(--line);z-index:250;transform:translateX(-100%);transition:transform .28s cubic-bezier(.22,.9,.28,1);display:flex;flex-direction:column;box-shadow:16px 0 40px rgba(0,0,0,.55)}
.sections-overlay.open{transform:translateX(0)}
.sections-overlay .sections-head{padding:14px 16px;border-bottom:1px solid var(--line);display:flex;align-items:center;gap:12px;flex-shrink:0}
.sections-overlay .sections-head .logo{width:32px;height:32px;border-radius:8px;background:#000;border:1px solid var(--line);flex-shrink:0}
.sections-overlay .sections-head h3{margin:0;font-size:14.5px;color:#dfe6f0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;flex:1;font-weight:700}
.sections-overlay .close-sec{background:transparent;border:1px solid var(--line);color:var(--muted);cursor:pointer;width:40px;height:40px;border-radius:9px;display:inline-flex;align-items:center;justify-content:center;flex-shrink:0}
.sections-overlay .close-sec:hover{color:var(--accent);border-color:var(--accent)}
.sections-overlay .close-sec svg{width:20px;height:20px;stroke:currentColor;fill:none;stroke-width:2}
.sections-overlay .search2{padding:10px 14px;border-bottom:1px solid var(--line);flex-shrink:0}
.sections-overlay .search2 input{width:100%;padding:10px 12px;background:var(--bg);border:1px solid var(--line);color:var(--txt);font:inherit;border-radius:9px;min-height:42px;font-size:13.5px;outline:none}
.sections-overlay .search2 input:focus{border-color:var(--accent)}
.toc{flex:1;overflow-y:auto}
.toc-sec{border-bottom:1px solid var(--line)}
.toc-head{padding:13px 14px;display:flex;align-items:center;gap:12px;cursor:pointer;user-select:none}
.toc-head:hover{background:rgba(255,255,255,.025)}
.toc-head.open{background:linear-gradient(90deg,rgba(92,141,255,.08),transparent)}
.toc-num{width:36px;height:36px;border-radius:10px;background:var(--panel2);border:1px solid var(--line);display:flex;align-items:center;justify-content:center;font-weight:800;font-size:13px;color:var(--accent);flex-shrink:0}
.toc-head.open .toc-num{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border-color:transparent}
.toc-info{flex:1;min-width:0}
.toc-title{font-size:13.5px;font-weight:600;color:#dfe6f0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.toc-sub{font-size:11px;color:var(--muted);margin-top:2px}
.toc-arrow{color:var(--muted);flex-shrink:0;display:flex;align-items:center;transition:transform .2s}
.toc-head.open .toc-arrow{transform:rotate(90deg);color:var(--accent)}
.toc-arrow svg{width:16px;height:16px;stroke:currentColor;fill:none;stroke-width:2}
.toc-body{display:none}
.toc-body.open{display:block;background:rgba(0,0,0,.15)}
.toc-unit{padding:11px 14px 11px 62px;display:flex;align-items:center;gap:10px;cursor:pointer;border-top:1px solid rgba(255,255,255,.03);min-height:46px}
.toc-unit:hover{background:rgba(255,255,255,.04)}
.toc-unit.active{background:linear-gradient(90deg,rgba(92,141,255,.16),transparent)}
.toc-unit .t{flex:1;font-size:13px;color:#b0bccb;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.toc-unit.active .t{color:var(--accent);font-weight:600}
.toc-unit .type{padding:3px 8px;border-radius:6px;font-size:9.5px;font-weight:700;text-transform:uppercase;letter-spacing:.4px;flex-shrink:0;display:inline-flex;align-items:center;gap:4px}
.toc-unit .type svg{width:12px;height:12px;stroke:currentColor;fill:none;stroke-width:2}
.toc-unit .type.ivideo{background:rgba(92,141,255,.15);color:#7ea8ff}
.toc-unit .type.pdf{background:rgba(46,204,113,.15);color:#4ddc8e}
.toc-unit .type.assessmentV2{background:rgba(179,92,255,.15);color:#c88cff}
.toc-unit .type.youtube{background:rgba(255,92,92,.15);color:#ff8b8b}
.toc-unit .type.scorm{background:rgba(246,183,60,.15);color:#f6c46b}
.toc-unit .type.embed,.toc-unit .type.url{background:rgba(124,134,151,.18);color:#a8b3c2}
.toc-unit .type.quizFormal,.toc-unit .type.selfAssessment{background:rgba(179,92,255,.15);color:#c88cff}
.player-wrap:fullscreen .sections-overlay,
.player-wrap:-webkit-full-screen .sections-overlay{position:absolute;width:min(420px,50vw);max-width:88vw;z-index:60;transform:translateX(-100%)}
.player-wrap:fullscreen .sections-overlay.open,
.player-wrap:-webkit-full-screen .sections-overlay.open{transform:translateX(0)}

/* ===== pdf viewer ===== */
.pdf-viewer{width:100%;height:100%;display:flex;flex-direction:column;background:#0a0a0a}
.pdf-toolbar{padding:10px 14px;background:var(--panel2);border-bottom:1px solid var(--line);display:flex;justify-content:space-between;gap:10px;align-items:center;flex-wrap:wrap}
.pdf-toolbar .name{color:var(--txt);font-weight:600;font-size:12.5px;flex:1;min-width:100px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;display:inline-flex;align-items:center;gap:6px}
.pdf-toolbar .name svg{width:18px;height:18px;stroke:currentColor;fill:none;stroke-width:2}
.pdf-actions{display:flex;gap:6px;flex-wrap:wrap}
.pdf-actions a,.pdf-actions button{padding:8px 12px;background:var(--panel2);color:var(--txt);border:1px solid var(--line);border-radius:8px;font:inherit;font-weight:600;font-size:12px;cursor:pointer;min-height:38px;display:inline-flex;align-items:center;gap:5px;text-decoration:none}
.pdf-actions svg{width:16px;height:16px;stroke:currentColor;fill:none;stroke-width:2}
.pdf-actions .primary{background:linear-gradient(90deg,var(--accent),var(--accent2));color:#fff;border-color:transparent}
.pdf-frame{flex:1;border:0;background:#fff}

/* ===== theme picker ===== */
.theme-picker{position:fixed;top:64px;right:14px;z-index:300;background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:12px;box-shadow:0 24px 60px rgba(0,0,0,.7);display:none;min-width:280px;max-width:92vw}
.theme-picker.open{display:block}
.theme-picker h4{margin:0 0 10px;font-size:12px;text-transform:uppercase;letter-spacing:.8px;color:var(--muted);font-weight:700}
.theme-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:8px}
.theme-swatch{display:flex;align-items:center;gap:10px;padding:10px 12px;background:var(--panel2);border:1px solid var(--line);border-radius:10px;cursor:pointer;font-size:12.5px;font-weight:600;color:var(--txt)}
.theme-swatch:hover{border-color:var(--accent)}
.theme-swatch.cur{border-color:var(--accent);background:rgba(92,141,255,.08)}
.theme-swatch .dot{width:20px;height:20px;border-radius:50%;flex-shrink:0;border:1px solid rgba(255,255,255,.15)}
/* ===== end ===== */
"""
