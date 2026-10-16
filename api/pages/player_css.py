"""Player + assessment CSS (injected into MAIN_PAGE)."""

PLAYER_CSS = r"""
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
.as-q .as-q-text img{max-width:100%;border-radius:8px;margin:8px 0}
.as-opts{display:flex;flex-direction:column;gap:10px}
.as-opt{display:flex;align-items:flex-start;gap:12px;padding:14px 16px;background:var(--panel2);border:1px solid var(--line);border-radius:11px;cursor:pointer;transition:all .15s ease;min-height:52px}
.as-opt:hover{border-color:var(--accent);background:rgba(92,141,255,.06)}
.as-opt.sel{border-color:var(--accent);background:linear-gradient(90deg,rgba(92,141,255,.14),rgba(124,92,255,.05));box-shadow:0 0 0 1px rgba(92,141,255,.35) inset}
.as-opt .as-radio{width:22px;height:22px;border-radius:50%;border:2px solid var(--muted);flex-shrink:0;display:flex;align-items:center;justify-content:center;margin-top:1px;transition:all .15s ease}
.as-opt.sel .as-radio{border-color:var(--accent);background:var(--accent)}
.as-opt.sel .as-radio::after{content:"";width:8px;height:8px;background:#fff;border-radius:50%}
.as-opt .as-opt-body{flex:1;line-height:1.6;font-size:14.5px;color:#dfe6f0}
.as-opt .as-opt-body p{margin:0 0 6px}
.as-opt .as-opt-body p:last-child{margin-bottom:0}
.as-opt input[type=text]{width:100%;margin-top:10px;padding:10px 12px;background:var(--bg);border:1px solid var(--line);color:var(--txt);border-radius:8px;font:inherit;font-size:14px}
.as-actions{position:sticky;bottom:0;display:flex;justify-content:space-between;gap:10px;padding:14px 18px;background:linear-gradient(0deg,var(--bg) 60%,transparent);margin:0 -18px;flex-wrap:wrap;z-index:5}
.as-btn{padding:13px 22px;border-radius:10px;font:inherit;font-weight:700;font-size:14px;cursor:pointer;border:1px solid var(--line);background:var(--panel2);color:var(--txt);min-height:48px;transition:all .15s ease}
.as-btn:hover:not(:disabled){border-color:var(--accent);transform:translateY(-1px)}
.as-btn:disabled{opacity:.4;cursor:not-allowed}
.as-btn.primary{background:linear-gradient(90deg,var(--accent),var(--accent2));color:#fff;border:0}
.as-btn.primary:hover:not(:disabled){filter:brightness(1.1)}
.as-btn.danger{background:linear-gradient(90deg,#ff5c5c,#b35cff);color:#fff;border:0}

/* review */
.as-review{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:22px;margin-bottom:16px}
.as-review .as-q-text{font-size:14.5px;line-height:1.7;color:#dfe6f0;margin-bottom:14px}
.as-review .as-opt{cursor:default}
.as-review .as-opt.correct{border-color:var(--good);background:rgba(46,204,113,.08)}
.as-review .as-opt.correct .as-radio{border-color:var(--good);background:var(--good)}
.as-review .as-opt.wrong{border-color:#ff5c5c;background:rgba(255,92,92,.08)}
.as-review .as-opt.wrong .as-radio{border-color:#ff5c5c;background:#ff5c5c}
.as-review .as-opt.reveal-correct{border-color:var(--good);border-style:dashed;background:rgba(46,204,113,.03)}
.as-review .as-tag{padding:3px 9px;border-radius:8px;font-size:10.5px;font-weight:700;text-transform:uppercase;letter-spacing:.5px;align-self:flex-start;margin-left:auto}
.as-review .as-tag.ok{background:rgba(46,204,113,.15);color:var(--good)}
.as-review .as-tag.no{background:rgba(255,92,92,.15);color:#ff5c5c}

/* score card with pie */
.as-score-card{background:linear-gradient(135deg,rgba(92,141,255,.14),rgba(124,92,255,.05) 60%,transparent);border:1px solid var(--line);border-radius:16px;padding:24px;margin-bottom:20px;display:flex;align-items:center;gap:24px;flex-wrap:wrap;justify-content:center}
.as-pie{position:relative;width:120px;height:120px;flex-shrink:0}
.as-pie svg{transform:rotate(-90deg);overflow:visible}
.as-pie .as-pie-center{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;font-weight:800}
.as-pie .as-pie-center .pct{font-size:26px;line-height:1;background:linear-gradient(90deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.as-pie .as-pie-center .lbl{font-size:9px;color:var(--muted);text-transform:uppercase;letter-spacing:.8px;margin-top:3px;font-weight:700}
.as-score-info{text-align:center;min-width:180px}
.as-score-info .big{font-size:34px;font-weight:800;line-height:1;background:linear-gradient(90deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.as-score-info .sub{color:var(--muted);font-size:12px;text-transform:uppercase;letter-spacing:.8px;margin-top:6px;font-weight:700}
.as-score-info .legend{margin-top:14px;display:flex;flex-direction:column;gap:6px;align-items:flex-start}
.as-score-info .legend .row{display:flex;align-items:center;gap:8px;font-size:12.5px}
.as-score-info .legend .dot{width:10px;height:10px;border-radius:50%;flex-shrink:0}
.as-score-info .legend .dot.ok{background:var(--good)}
.as-score-info .legend .dot.no{background:#ff5c5c}
.as-score-info .legend .dot.neutral{background:var(--muted)}

.as-loading{display:flex;align-items:center;justify-content:center;height:100%;color:var(--muted);flex-direction:column;gap:16px}
.as-loading .sp{width:40px;height:40px;border:3px solid var(--panel2);border-top-color:var(--accent);border-radius:50%;animation:ytspin .85s linear infinite}
.as-err{color:#ff7a7a;text-align:center;padding:32px}
/* ===== end assessment ===== */
"""
