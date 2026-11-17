// El mapa del poder global · interfaz
(function () {
  "use strict";
  const M = window.META, ORGS = window.ORGS, REL = window.RELACIONES, PA = window.PAISES, WORLD = window.WORLD, FI = window.FICHAS || {};
  const byId = Object.fromEntries(ORGS.map(o => [o.id, o]));
  const app = document.getElementById("app");
  const tip = document.getElementById("tip");
  const BL = M.bloques;
  const BORDER = ["T", "I", "P", "X", "E"]; // izquierda a derecha en Quién manda

  // ---------- utilidades ----------
  const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const num = (v, d = 1) => Number(v).toLocaleString("es-AR", { minimumFractionDigits: d, maximumFractionDigits: d });
  const pct = v => Math.round(v * 100) + " %";
  const MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"];
  const fecha = iso => { const [y, m, d] = iso.split("-").map(Number); return `${d} de ${MESES[m - 1]} de ${y}`; };
  const corto = n => n.replace(/\s*\((?:[^()]*)\)\s*$/, "");
  const bcol = b => (BL[b] || BL.D).c;
  const relsOf = id => REL.filter(r => r.a === id || r.b === id);
  const dependents = id => ORGS.filter(o => o.dep.includes(id));

  // Forma por tipo de organización (SVG dentro de un <g> o de un <svg>)
  function shape(tipo, x, y, r, fill, extra = "") {
    const f = `fill="${fill}"`;
    switch (tipo) {
      case "Capital": return `<rect x="${x - r * .88}" y="${y - r * .88}" width="${r * 1.76}" height="${r * 1.76}" ${f} ${extra}/>`;
      case "Información": return `<path d="M${x} ${y - r * 1.15}L${x + r * 1.15} ${y}L${x} ${y + r * 1.15}L${x - r * 1.15} ${y}Z" ${f} ${extra}/>`;
      case "Supranacional": return `<path d="M${x - r * .55} ${y - r}H${x + r * .55}L${x + r * 1.1} ${y}L${x + r * .55} ${y + r}H${x - r * .55}L${x - r * 1.1} ${y}Z" ${f} ${extra}/>`;
      case "Influencia": return `<path d="M${x} ${y - r * 1.15}L${x + r * 1.1} ${y + r * .85}H${x - r * 1.1}Z" ${f} ${extra}/>`;
      case "Sombra": return `<circle cx="${x}" cy="${y}" r="${Math.max(r - 1.2, 2)}" fill="none" stroke="${fill}" stroke-width="2.4" ${extra}/>`;
      case "Persona": { const R = r * 1.25, q = R * .45, p = []; for (let i = 0; i < 10; i++) { const a = -Math.PI / 2 + i * Math.PI / 5, d = i % 2 ? q : R; p.push(`${(x + d * Math.cos(a)).toFixed(2)} ${(y + d * Math.sin(a)).toFixed(2)}`); } return `<path d="M${p.join("L")}Z" ${f} ${extra}/>`; }
      default: return `<circle cx="${x}" cy="${y}" r="${r}" ${f} ${extra}/>`;
    }
  }
  const icon = (o, s = 16) => `<svg width="${s}" height="${s}" viewBox="0 0 16 16" aria-hidden="true">${shape(o.tipo, 8, 8, 6.4, bcol(o.bloque))}</svg>`;
  const lineIcon = t => {
    const st = { "Enfrentamiento": 'stroke="#FF3B30" stroke-dasharray="5 3"', "Puerta giratoria": 'stroke="#9A8F8C" stroke-dasharray="2 3"', "Acceso a datos": 'stroke="#9A8F8C" stroke-dasharray="2 3"', "Ambigua": 'stroke="#F2A93B" stroke-dasharray="4 3"' }[t] || 'stroke="#EDE6E3"';
    return `<svg width="26" height="6" aria-hidden="true"><line x1="0" y1="3" x2="26" y2="3" ${st} stroke-width="2"/></svg>`;
  };
  function bindTip(root, sel, html) {
    root.querySelectorAll(sel).forEach(el => {
      el.addEventListener("mousemove", e => { tip.innerHTML = html(el); tip.style.display = "block"; const w = tip.offsetWidth; tip.style.left = Math.min(e.clientX + 14, innerWidth - w - 8) + "px"; tip.style.top = (e.clientY + 14) + "px"; });
      el.addEventListener("mouseleave", () => { tip.style.display = "none"; });
    });
  }
  function activate(root, sel, fn) {
    root.querySelectorAll(sel).forEach(el => {
      el.addEventListener("click", () => fn(el));
      el.addEventListener("keydown", e => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); fn(el); } });
    });
  }

  // ---------- mapa ----------
  const FEAT = topojson.feature(WORLD, WORLD.objects.countries).features.filter(f => f.properties.name !== "Antarctica");
  const MW = 960, MH = 500;
  const proj = d3.geoNaturalEarth1().fitExtent([[6, 6], [MW - 6, MH + 64]], { type: "Sphere" });
  const gpath = d3.geoPath(proj);
  const SPHERE = gpath({ type: "Sphere" }), GRAT = gpath(d3.geoGraticule().step([20, 20])());
  const CPATH = FEAT.map(f => ({ name: f.properties.name, d: gpath(f) }));
  // país de cada sede
  // primero por el nombre del país en la sede (más fiable en costas e islas); si no, por coordenadas
  const norm = t => t.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase().trim();
  const ALIAS = { "ee.uu.": "Estados Unidos" };
  const porNombre = {}; Object.entries(PA).forEach(([k, p]) => { if (!p.terr || !porNombre[norm(p.n)]) porNombre[norm(p.n)] = k; });
  ORGS.forEach(o => {
    o.pais = null;
    const suf = (o.sede || "").replace(/\s*\(.*\)\s*$/, "").split(",").pop();
    const k = porNombre[norm(ALIAS[norm(suf)] || suf)];
    if (k) { o.pais = k; return; }
    if (!o.ll) return; const hit = FEAT.find(F => d3.geoContains(F, o.ll)); o.pais = hit ? hit.properties.name : null;
  });
  const POSOP = { C: 1, A: .9, G: .7, R: .7, U: 1, P: .45, IT: .32, IE: .38, S: 0 };
  const ZONA = { T: "#E10600", X: "#A3150C", P: "#5E1410" };
  function fillFor(name, layer) {
    const p = PA[name]; if (!p) return "#101010";
    if (layer === "zonas") return p.z ? ZONA[p.z] : "#232323";
    if (layer === "organizaciones") return p.b === "D" ? "#1D1D1D" : bcol(p.b) + "40";
    if (layer === "posicion") {
      if (p.p === "R") return `url(#hatch-${p.b})`;
      if (p.p === "K") return `url(#col-${p.b})`;
      if (p.b === "D") { const c = p.p === "IT" ? BL.T.c : p.p === "IE" ? BL.E.c : p.p === "P" ? BL.P.c : null; if (!c) return "#232323"; return c + Math.round(POSOP[p.p] * 255).toString(16).padStart(2, "0"); }
      return bcol(p.b) + Math.round((POSOP[p.p] || 1) * 255).toString(16).padStart(2, "0");
    }
    return p.b === "D" ? "#232323" : bcol(p.b);
  }
  const FULL = [0, 0, MW, MH];
  function fitBox([[x0, y0], [x1, y1]], minW = 150) {
    let w = Math.max(x1 - x0, minW) * 1.6, h = Math.max(y1 - y0, minW * MH / MW) * 1.6;
    if (w / h > MW / MH) h = w * MH / MW; else w = h * MW / MH;
    if (w > MW) { w = MW; h = MH; }
    const x = Math.max(0, Math.min(MW - w, (x0 + x1) / 2 - w / 2)), y = Math.max(0, Math.min(MH - h, (y0 + y1) / 2 - h / 2));
    return [x, y, w, h];
  }
  function selBox(sel) {
    if (!sel) return FULL;
    if (sel.k === "c") { const F = FEAT.find(f => f.properties.name === sel.v); return F ? fitBox(gpath.bounds(F)) : FULL; }
    const ll = sel.k === "o" ? byId[sel.v].ll : M.friccion.find(f => f.n === +sel.v).ll;
    const [x, y] = proj(ll); return fitBox([[x - 70, y - 40], [x + 70, y + 40]]);
  }
  function mapSVG(layer, sel, z = 1, vb = FULL) {
    const zs = 1 / Math.pow(z, .75);
    const defs = `<defs>${["T", "E", "I", "D"].map(b => `<pattern id="hatch-${b}" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="6" height="6" fill="#141414"/><rect width="3" height="6" fill="${b === "D" ? "#5A5150" : bcol(b)}"/></pattern><pattern id="col-${b}" width="5" height="5" patternUnits="userSpaceOnUse"><rect width="5" height="5" fill="${b === "D" ? "#5A5150" : bcol(b)}"/><circle cx="2.5" cy="2.5" r="1.1" fill="#141414"/></pattern>`).join("")}</defs>`;
    const cs = CPATH.map(c => `<path class="m-c${sel && sel.k === "c" && sel.v === c.name ? " sel" : ""}" data-c="${esc(c.name)}" d="${c.d}" fill="${fillFor(c.name, layer)}"/>`).join("");
    let extra = "";
    if (layer === "bloques" || layer === "posicion") extra = `<g class="m-fr">${M.friccion.map(f => { const [x, y] = proj(f.ll); return `<g data-fr="${f.n}" tabindex="0" role="button" aria-label="Punto de fricción ${f.n}: ${esc(f.x)}"><circle cx="${x}" cy="${y}" r="${9 * zs}"/><text x="${x}" y="${y}" style="font-size:${10 * zs}px">${f.n}</text></g>`; }).join("")}</g>`;
    if (layer === "organizaciones") extra = ORGS.filter(o => o.ll).slice().sort((a, b) => b.pe - a.pe).map(o => { const [x, y] = proj(o.ll); const r = (2 + Math.sqrt(o.pe) * .9) * zs; return shape(o.tipo, x, y, r, bcol(o.bloque), `class="m-o${sel && sel.k === "o" && sel.v === o.id ? " sel" : ""}" data-o="${o.id}" tabindex="0" role="button" aria-label="${esc(o.n)}"`); }).join("");
    return `<svg viewBox="${vb.join(" ")}" role="img" aria-label="Mapa mundial: ${esc(LAYERS[layer])}">${defs}<path class="m-sphere" d="${SPHERE}"/><path class="m-grat" d="${GRAT}"/>${cs}${extra}</svg>`;
  }
  const LAYERS = { bloques: "Bloques", posicion: "Posición", zonas: "Zonas liberadas", organizaciones: "Organizaciones" };
  function legendFor(layer) {
    const sq = (c, t, extra = "") => `<div><span class="sq" style="background:${c};${extra}"></span>${t}</div>`;
    if (layer === "zonas") return sq(ZONA.T, "Total") + sq(ZONA.X, "Extendida") + sq(ZONA.P, "Parcial") + sq("#232323", "Sin zona liberada", "border:1px solid #2A1414");
    if (layer === "organizaciones") return M.tipos.map(t => `<div><svg width="16" height="16" aria-hidden="true">${shape(t, 8, 8, 6.4, "#EDE6E3")}</svg>${t}</div>`).join("") + `<p class="note">Color: bloque de la organización. Tamaño: poder efectivo.</p>`;
    const base = sq(BL.T.c, "Imperio transoceánico") + sq(BL.E.c, "Alianza euroasiática") + sq(BL.I.c, "Independientes") + sq("#232323", "Terreno disputado", "border:1px solid #2A1414");
    if (layer === "posicion") return base + sq("repeating-linear-gradient(45deg,#2F6BFF 0 3px,#141414 3px 6px)", "Protectorado") + sq("radial-gradient(circle,#141414 1.1px,#2F6BFF 1.3px) 0 0/5px 5px", "Colonia de hecho") + `<p class="note">Intensidad: centro y aliados, plenos; integrados, medios. En el terreno disputado, el tinte indica hacia qué bloque se inclina.</p>`;
    return base + `<div><span class="sq" style="border:1.6px solid #FF3B30;border-radius:50%"></span>Punto de fricción</div>`;
  }
  function countryPanel(name) {
    const p = PA[name]; if (!p) return "";
    const orgs = ORGS.filter(o => o.pais === name || (p.m && p.m[0] === o.id && !p.m[1])).sort((a, b) => b.pt - a.pt);
    const def = p.m ? byId[p.m[0]] : orgs[0];
    const quien = def ? `<div class="define"><div class="lbl">Quién define aquí</div><a href="#o-${def.id}">${icon(def, 22)}<span><b>${esc(corto(def.n))}</b><small>${esc(def.area)} · puntaje ${num(def.pt)}</small></span></a>${p.m && p.m[1] ? `<p class="side-x">${esc(p.m[1])}</p>` : ""}</div>` : "";
    return `<div class="lbl">${esc(BL[p.b].n)}</div><h3>${esc(p.n)}</h3>
      <p class="side-x"><b>Posición:</b> ${esc(M.posiciones[p.p])}${p.z ? `<br><b>Zona liberada:</b> ${esc(M.grados[p.z])} · ${esc(p.asp.map(a => M.aspectos[a]).join(", "))}` : ""}</p>
      ${p.x ? `<p class="side-x">${esc(p.x)}</p>` : ""}${quien}
      ${(o2 => o2.length ? `<div class="lbl" style="margin-top:6px">${def ? "Otros actores" : "Actores"} con sede aquí (${o2.length})</div><div>${o2.map(o => `<a class="rk" style="grid-template-columns:18px minmax(0,1fr) 46px" href="#o-${o.id}">${icon(o)}<span class="nm">${esc(corto(o.n))}</span><span class="v">${num(o.pt)}</span></a>`).join("")}</div>` : "")(orgs.filter(o => o !== def))}`;
  }
  function orgPanel(o) {
    return `<div class="lbl">${esc(o.area)} · ${esc(BL[o.bloque].n)}</div><h3>${esc(o.n)}</h3>
      <div class="nums"><div><small>Puntaje</small><b>${num(o.pt)}</b></div><div><small>En red</small><b>${num(o.red)}</b></div><div class="o"><small>Oculto</small><b>${num(o.oculto)}</b></div></div>
      <p class="side-x"><b>Sede:</b> ${esc(o.sede)}<br><b>Autonomía:</b> ${o.aut} · ${esc(M.autonomia[o.aut])}</p>
      <a class="btn" href="#o-${o.id}">Abrir la ficha</a>`;
  }
  function frPanel(n) { const f = M.friccion.find(x => x.n === +n); return `<div class="lbl">Punto de fricción ${f.n} de ${M.friccion.length}</div><h3>${esc(f.x)}</h3><p class="side-x">${esc(f.d)}</p><p class="note">Los puntos de fricción son los frentes donde chocan los bloques.</p>`; }
  function mountMap(el, opts = {}) {
    let layer = opts.layer || "bloques", sel = null;
    const layers = opts.layers || Object.keys(LAYERS);
    el.innerHTML = `<div class="panel"><div class="panel-bar"><div class="chips" role="group" aria-label="Capas del mapa">${layers.map(k => `<button type="button" class="chip" data-l="${k}">${LAYERS[k]}</button>`).join("")}</div><span class="note" style="margin:0">Tocá un país o una organización</span></div>
      <div class="split"><div class="stage map"><div class="map-svg"></div><div class="map-ctl"><button type="button" data-z="in" aria-label="Acercar">+</button><button type="button" data-z="out" aria-label="Alejar">−</button><button type="button" data-z="all" class="all">Vista completa</button></div></div><aside></aside></div></div>`;
    const holder = el.querySelector(".map-svg"), side = el.querySelector("aside");
    const stage = holder;
    let vb = FULL.slice(), goal = FULL.slice(), anim = 0;
    const still = matchMedia("(prefers-reduced-motion: reduce)").matches;
    const zoomTo = t => {
      goal = t.slice(); cancelAnimationFrame(anim);
      const from = vb.slice(), t0 = performance.now(), svg = holder.querySelector("svg");
      const step = now => { const p = still ? 1 : Math.min(1, (now - t0) / 480), e = 1 - Math.pow(1 - p, 3);
        vb = from.map((v, i) => v + (t[i] - v) * e); if (svg) svg.setAttribute("viewBox", vb.join(" ")); if (p < 1) anim = requestAnimationFrame(step); };
      anim = requestAnimationFrame(step);
    };
    const pick = s => { sel = s; const t = selBox(s); draw(t); zoomTo(t); };
    const zoomBy = f => { const [x, y, w, h] = goal, nw = Math.min(MW, Math.max(MW / 12, w * f)), nh = nw * MH / MW;
      const t = [Math.max(0, Math.min(MW - nw, x + w / 2 - nw / 2)), Math.max(0, Math.min(MH - nh, y + h / 2 - nh / 2)), nw, nh]; draw(t); zoomTo(t); };
    el.querySelector('[data-z="in"]').onclick = () => zoomBy(1 / 1.7);
    el.querySelector('[data-z="out"]').onclick = () => zoomBy(1.7);
    el.querySelector('[data-z="all"]').onclick = () => { draw(FULL); zoomTo(FULL); };
    // arrastre con mouse cuando está acercado (en pantallas táctiles no, para no trabar el scroll)
    let drag = null;
    holder.addEventListener("pointerdown", e => { if (e.pointerType !== "mouse" || goal[2] >= MW) return; drag = { x: e.clientX, y: e.clientY, v: goal.slice(), moved: false }; });
    addEventListener("pointermove", e => { if (!drag) return; const k = drag.v[2] / holder.clientWidth, dx = (e.clientX - drag.x) * k, dy = (e.clientY - drag.y) * k;
      if (Math.abs(dx) + Math.abs(dy) > 2) drag.moved = true; if (!drag.moved) return;
      const [x, y, w, h] = drag.v; goal = vb = [Math.max(0, Math.min(MW - w, x - dx)), Math.max(0, Math.min(MH - h, y - dy)), w, h];
      const svg = holder.querySelector("svg"); if (svg) svg.setAttribute("viewBox", vb.join(" ")); });
    addEventListener("pointerup", () => { if (drag && drag.moved) holder.addEventListener("click", e => e.stopPropagation(), { capture: true, once: true }); drag = null; });
    const draw = (t = goal) => {
      el.querySelector(".map-ctl .all").classList.toggle("on", t[2] < MW);
      el.querySelectorAll("[data-l]").forEach(b => { b.classList.toggle("on", b.dataset.l === layer); b.setAttribute("aria-pressed", b.dataset.l === layer); });
      holder.innerHTML = mapSVG(layer, sel, MW / t[2], vb);
      side.innerHTML = !sel ? `<div class="lbl">Cómo leerlo</div><div class="legend">${legendFor(layer)}</div>`
        : sel.k === "c" ? countryPanel(sel.v) : sel.k === "o" ? orgPanel(byId[sel.v]) : frPanel(sel.v);
      if (sel) side.insertAdjacentHTML("beforeend", `<button type="button" class="chip" data-clear style="align-self:flex-start">Volver a la leyenda</button>`);
      const clear = side.querySelector("[data-clear]"); if (clear) clear.onclick = () => { sel = null; draw(FULL); zoomTo(FULL); };
      stage.querySelectorAll(".m-c").forEach(p => p.addEventListener("click", () => pick({ k: "c", v: p.dataset.c })));
      activate(stage, ".m-o", g => pick({ k: "o", v: g.dataset.o }));
      activate(stage, "[data-fr]", g => pick({ k: "f", v: g.dataset.fr }));
      bindTip(stage, ".m-c", p => { const c = PA[p.dataset.c]; return c ? `<b>${esc(c.n)}</b><span>${esc(BL[c.b].n)} · ${esc(M.posiciones[c.p])}${c.z ? " · zona liberada " + esc(M.grados[c.z]).toLowerCase() : ""}</span>` : esc(p.dataset.c); });
      bindTip(stage, ".m-o", g => { const o = byId[g.dataset.o]; return `<b>${esc(o.n)}</b><span>${esc(o.area)} · puntaje ${num(o.pt)}</span>`; });
    };
    el.querySelectorAll("[data-l]").forEach(b => b.addEventListener("click", () => { layer = b.dataset.l; if (sel && sel.k === "o" && layer !== "organizaciones") sel = null; draw(); }));
    side.addEventListener("click", e => { const a = e.target.closest("[data-pick]"); if (!a) return; e.preventDefault(); if (layer !== "organizaciones") layer = "organizaciones"; pick({ k: "o", v: a.dataset.pick }); });
    draw();
  }

  // ---------- listas ----------
  const METRIC = { pt: "Puntaje de poder", red: "Poder en red", pe: "Poder efectivo", oculto: "Poder oculto", cap: "Capacidad" };
  function rankRows(list, key, max, color) {
    return list.map((o, i) => `<a class="rk" href="#o-${o.id}"><span class="n">${String(i + 1).padStart(2, "0")}</span>${icon(o)}<span class="nm">${esc(corto(o.n))}<small>${esc(o.area)}${FI[o.id] ? "" : " · ficha en preparación"}</small></span><span class="bar"><i style="width:${Math.max(2, o[key] / max * 100)}%;background:${color || bcol(o.bloque)}"></i></span><span class="v">${num(o[key], key === "cap" ? 0 : 1)}</span></a>`).join("");
  }
  const sortBy = k => ORGS.slice().sort((a, b) => b[k] - a[k] || b.pt - a.pt);

  // ---------- vistas ----------
  const V = {};
  V.inicio = () => {
    const red = sortBy("pt").slice(0, 10), oc = sortBy("oculto").slice(0, 10);
    app.innerHTML = `<div class="wrap">
      <div class="hero"><div style="display:flex;flex-direction:column;gap:18px"><div class="kick">El mundo real, sin máscaras</div><h1>El mapa del<br>poder global</h1></div>
      <p class="read">Quién tiene el poder real en el mundo y quién solo lo aparenta. ${ORGS.length} organizaciones y personas medidas en ${M.ejes.length} ejes, su jerarquía y cuánto de su poder escapa al control público.</p></div>
      <section class="block" id="mapa-inicio"></section>
      <section class="block two">
        <div><div class="sec-title"><h2>Puntaje de poder</h2><a href="#organizaciones">Ver los ${ORGS.length}</a></div>${rankRows(red, "pt", 100)}</div>
        <div><div class="sec-title"><h2>Poder oculto</h2><a href="#organizaciones-oculto">Ver el índice</a></div>${rankRows(oc, "oculto", oc[0].oculto, "#E10600")}</div>
        <p class="note scale-note"><b>Cómo leer los números.</b> El <b>puntaje de poder</b> va de 0 a 100: el actor más poderoso vale 100 y la escala está estirada para que las distancias se parezcan a las reales, que entre el primero y los últimos son de varios órdenes de magnitud. Combina cinco cosas: lo que suele pesar su categoría de actor (40 %), su capacidad propia en ${M.ejes.length} ejes (30 %), su <b>alcance efectivo</b> —si puede actuar en cualquier parte del mundo, en un grupo de países o solo en el suyo— (20 %), su autonomía real (5 %) y la red de quienes dependen de él (5 %). Se multiplican, no se suman: para estar arriba hay que tener puntaje en todo. El <b>poder oculto</b> es la parte de su poder que escapa a la ley, las elecciones, los tribunales y la auditoría. <a href="#marco">Ver el método</a>.</p>
      </section>
      <section class="block cards">
        <a class="card" href="#quien-manda"><span class="kick">Esquema</span><b>Quién manda</b><span>La jerarquía real: quién decide solo, quién obedece y quién aparenta.</span></a>
        <a class="card" href="#organizaciones"><span class="kick">Fichas</span><b>Organizaciones</b><span>Perfil de poder, dependencias y relaciones de cada una.</span></a>
        <a class="card" href="#paises"><span class="kick">Mapa</span><b>Países</b><span>Bloques, protectorados, zonas liberadas y puntos de fricción.</span></a>
        <a class="card" href="#marco"><span class="kick">Método</span><b>Marco</b><span>La teoría detrás del mapa y cómo se mide el poder.</span></a>
      </section></div>`;
    mountMap(document.getElementById("mapa-inicio"), { layer: "bloques" });
  };

  V.paises = () => {
    const rows = Object.entries(PA).filter(([, p]) => !p.terr).sort((a, b) => a[1].n.localeCompare(b[1].n, "es"));
    app.innerHTML = `<div class="wrap"><div class="page-head"><div style="display:flex;flex-direction:column;gap:12px"><div class="kick">Mapa</div><h1>Países</h1></div>
      <p class="read">El orden mundial real: imperios con un país centro, aliados, protectorados que obedecen cuando el centro ordena, colonias de hecho que figuran como países, y zonas liberadas donde el Estado no manda y cada actor hace lo que su poder le permite. <a href="#marco">Cómo se clasifica</a>.</p></div>
      <section class="block" id="mapa-paises"></section>
      <section class="block"><div class="sec-title"><h2>Clasificación</h2><span class="note" style="margin:0">${rows.length} países y territorios</span></div>
      <div class="filters"><label>Bloque<select id="fB"><option value="">Todos</option>${["T", "E", "I", "D"].map(k => `<option value="${k}">${esc(BL[k].n)}</option>`).join("")}</select></label>
      <label>Posición<select id="fP"><option value="">Todas</option>${Object.entries(M.posiciones).filter(([k]) => rows.some(([, p]) => p.p === k)).map(([k, n]) => `<option value="${k}">${esc(n)}</option>`).join("")}</select></label>
      <label>Zona liberada<select id="fZ"><option value="">Todas</option><option value="si">Con zona liberada</option></select></label></div>
      <div class="tbl-wrap"><table><thead><tr><th>País</th><th>Bloque</th><th>Posición</th><th>Zona liberada</th><th>Nota</th></tr></thead><tbody id="tb"></tbody></table></div></section></div>`;
    mountMap(document.getElementById("mapa-paises"), { layer: "posicion" });
    const tb = document.getElementById("tb"), fB = document.getElementById("fB"), fZ = document.getElementById("fZ"), fP = document.getElementById("fP");
    const fill = () => { tb.innerHTML = rows.filter(([, p]) => (!fB.value || p.b === fB.value) && (!fP.value || p.p === fP.value) && (!fZ.value || p.z)).map(([, p]) => `<tr><td>${esc(p.n)}</td><td><span class="sq" style="background:${p.b === "D" ? "#232323" : bcol(p.b)};border:1px solid #2A1414;vertical-align:-2px"></span> ${esc(BL[p.b].n)}</td><td>${esc(M.posiciones[p.p])}</td><td>${p.z ? esc(M.grados[p.z]) + " · " + esc(p.asp.map(a => M.aspectos[a]).join(", ")) : "—"}</td><td class="muted">${esc(p.x)}</td></tr>`).join(""); };
    fB.onchange = fZ.onchange = fP.onchange = fill; fill();
  };

  V.organizaciones = (arg) => {
    const areas = [...new Set(ORGS.map(o => o.area))].sort((a, b) => a.localeCompare(b, "es"));
    app.innerHTML = `<div class="wrap"><div class="page-head"><div style="display:flex;flex-direction:column;gap:12px"><div class="kick">Fichas</div><h1>Organizaciones</h1></div>
      <p class="read">${ORGS.length} organizaciones y personas con nombre propio, ordenadas por su puntaje de poder real. Filtrá por tipo, categoría, alcance o bloque, y tocá una para ver su ficha: quién la manda, de dónde saca el dinero, con quién se alía y cuánto de su poder escapa al control público.</p></div>
      <div class="filters">
        <label>Ordenar por<select id="fM">${Object.entries(METRIC).map(([k, n]) => `<option value="${k}"${k === (arg || "pt") ? " selected" : ""}>${n}</option>`).join("")}</select></label>
        <label>Tipo<select id="fT"><option value="">Todos</option>${M.tipos.map(t => `<option>${t}</option>`).join("")}</select></label>
        <label>Área<select id="fA"><option value="">Todas</option>${areas.map(a => `<option>${esc(a)}</option>`).join("")}</select></label>
        <label>Alcance<select id="fL"><option value="">Todos</option>${Object.entries(M.alcance).map(([k, a]) => `<option value="${k}">${esc(a.n)}</option>`).join("")}</select></label>
        <label>Bloque<select id="fB"><option value="">Todos</option>${["T", "E", "I", "P", "X"].map(k => `<option value="${k}">${esc(BL[k].n)}</option>`).join("")}</select></label>
      </div><div id="lst" style="padding-bottom:56px"></div></div>`;
    const g = id => document.getElementById(id);
    const fill = () => {
      const k = g("fM").value;
      const l = sortBy(k).filter(o => (!g("fT").value || o.tipo === g("fT").value) && (!g("fA").value || o.area === g("fA").value) && (!g("fB").value || o.bloque === g("fB").value) && (!g("fL").value || o.alc === g("fL").value));
      const max = sortBy(k)[0][k];
      g("lst").innerHTML = l.length ? rankRows(l, k, max, k === "oculto" ? "#E10600" : null) : `<p class="note">Ninguna organización con esos filtros.</p>`;
    };
    ["fM", "fT", "fA", "fB", "fL"].forEach(id => g(id).onchange = fill); fill();
  };

  function radar(o) {
    const cx = 130, cy = 120, R = 92, n = M.familias.length;
    const pt = (i, f) => { const a = -Math.PI / 2 + i * 2 * Math.PI / n; return [cx + Math.cos(a) * R * f, cy + Math.sin(a) * R * f]; };
    const famVal = M.familias.map(F => { const ks = F.ejes.map(k => M.ejes.findIndex(e => e.k === k)); return ks.reduce((s, i) => s + o.sc[i], 0) / (ks.length * 3); });
    const ring = f => M.familias.map((_, i) => pt(i, f).join(",")).join(" ");
    return `<svg viewBox="0 0 260 250" width="100%" role="img" aria-label="Radar por familias de ejes: ${M.familias.map((F, i) => F.n + " " + Math.round(famVal[i] * 100) + " %").join(", ")}">
      <g fill="none" stroke="#2A1414">${[1, .66, .33].map(f => `<polygon points="${ring(f)}"/>`).join("")}</g>
      <polygon points="${famVal.map((v, i) => pt(i, Math.max(v, .03)).join(",")).join(" ")}" fill="#E10600" fill-opacity=".28" stroke="#FF3B30" stroke-width="2"/>
      <g font-family="JetBrains Mono, monospace" font-size="10" fill="#9A8F8C" text-anchor="middle">${M.familias.map((F, i) => { const [x, y] = pt(i, 1.2); return `<text x="${x}" y="${y + 3}">${F.n.toUpperCase()}</text>`; }).join("")}</g></svg>`;
  }

  V.org = (id) => {
    const o = byId[id]; if (!o) return V.organizaciones();
    const deps = o.dep.map(d => byId[d]), subs = dependents(id), rels = relsOf(id), F = FI[id];
    const rank = sortBy("pt").indexOf(o) + 1;
    const CAT = M.categorias[o.area];
    const ejeIdx = Object.fromEntries(M.ejes.map((e, i) => [e.k, i]));
    const perfil = M.familias.map(F => `<div class="fam">${esc(F.n)}</div>` + F.ejes.map(k => { const e = M.ejes[ejeIdx[k]], v = o.sc[ejeIdx[k]]; return `<div class="eje"><span>${esc(e.n)}</span><span class="segs" role="img" aria-label="${v} de 3">${[0, 1, 2].map(i => `<i class="${i < v ? "on" : ""}"></i>`).join("")}</span><span class="an">${v ? esc(e.a[3 - v]) : "Sin capacidad relevante"}</span></div>`; }).join("")).join("");
    const relHtml = rels.length ? rels.sort((a, b) => b.i - a.i).map(r => { const other = byId[r.a === id ? r.b : r.a]; return `<div class="rel">${lineIcon(r.t)}<div><a href="#o-${other.id}">${esc(corto(other.n))}</a> · ${esc(r.t.toLowerCase())}${r.i === 3 ? " fuerte" : r.i === 1 ? " débil" : ""}<small>${esc(r.x)}</small></div></div>`; }).join("") : `<p class="side-x">Sin relaciones cargadas todavía.</p>`;
    app.innerHTML = `<div class="wrap">
      <div class="org-head"><div class="crumb"><a href="#organizaciones">Organizaciones</a> / ${esc(o.area)}</div>
        <div style="display:flex;flex-wrap:wrap;align-items:center;gap:18px">${icon(o, 44)}<h1>${esc(o.n)}</h1></div>
        <div class="pills"><span style="border-color:${bcol(o.bloque)}">${esc(BL[o.bloque].n)}</span><span>Autonomía ${o.aut} · ${esc(M.autonomia[o.aut])} · factor real ${num(o.fr, 2)}</span><span>Alcance: ${esc(M.alcance[o.alc].n).toLowerCase()}</span><span>Fase: ${esc(M.fases[o.fase]).toLowerCase()}</span><span>Certeza: ${esc(M.certeza[o.cert]).toLowerCase()}</span><span>${esc(o.tipo)}</span><span>Sede: ${esc(o.sede)}</span><span style="border-color:transparent;color:#9A8F8C">Puesto ${rank} de ${ORGS.length}</span></div></div>
      <div class="nums" style="margin-top:22px"><div><small>Puntaje de poder</small><b>${num(o.pt)}<span class="muted" style="font-size:15px"> /100</span></b></div><div><small>Capacidad</small><b>${num(o.cap)}<span class="muted" style="font-size:15px"> /${M.capmax}</span></b></div><div><small>Poder efectivo</small><b>${num(o.pe)}</b></div><div><small>Poder en red</small><b>${num(o.red)}</b></div><div><small>Brecha</small><b>${pct(o.brecha)}</b></div><div class="o"><small>Poder oculto</small><b>${num(o.oculto)}</b></div></div>
      <div class="org-body"><div class="org-main">
        ${M.monarcas.includes(o.id) ? `<p class="note" style="margin:0;border-left:2px solid #E10600;padding-left:12px">${esc(M.nota_monarca)}</p>` : ""}
        <div><h2>Su categoría</h2><p class="read" style="font-size:17px">${esc(o.area)} (${esc(o.tipo)}). Puntaje teórico de la categoría: ${num(CAT.t, 0)} de 10; puntaje real, según los datos del mapa (informativo): ${num(CAT.r, 1)} de 10. <a href="#marco">Cómo se calcula</a>.</p></div>
        <div><h2>Cómo se calcula su puntaje</h2>${(() => { const N = { ct: "Categoría teórica", cap: "Capacidad", alc: "Alcance efectivo", aut: "Autonomía real", red: "Red de dependientes" }; return `<div class="tbl-wrap" style="margin:0"><table><thead><tr><th>Componente</th><th>Peso</th><th>Valor (0 a 1)</th></tr></thead><tbody>${Object.keys(M.peso_final).map((k, i) => `<tr><td>${N[k]}${k === "alc" ? ` · ${esc(M.alcance[o.alc].n).toLowerCase()}` : ""}</td><td>${pct(M.peso_final[k])}</td><td>${num(o.cp[i], 2)}</td></tr>`).join("")}</tbody></table></div><p class="note" style="margin-top:8px">Los cinco valores se multiplican, cada uno elevado a su peso; el resultado se eleva al cubo y se compara con el del actor más poderoso, que vale 100. <a href="#marco">Ver el método</a>.</p>`; })()}</div>
        <div><h2>Poder formal y poder real</h2>
          <div class="note" style="display:flex;justify-content:space-between;margin:0"><span>Reconocido y sujeto a control</span><span style="color:#FF3B30">Fuera de control público</span></div>
          <div class="gapbar" role="img" aria-label="Brecha de ${pct(o.brecha)}"><i style="width:${(1 - o.brecha) * 100}%"></i><i style="width:${o.brecha * 100}%"></i></div>
          <p class="read" style="font-size:17px">Poder formal ${o.formal} de 3: ${pct(1 - o.brecha)} de su poder está reconocido públicamente y sujeto a control; el resto escapa a ese control.</p></div>
        ${o.ext ? `<div><h2>Acción fuera de la ley</h2><p class="read" style="font-size:17px;margin:0">${o.sc[M.ejes.findIndex(e => e.k === "ext")]} de 3. ${esc(o.ext[0])} <a href="${esc(o.ext[1])}" rel="noopener" target="_blank">Fuente</a>.</p></div>` : ""}
        
        ${F ? `<div><h2>Resumen</h2>${F.res.map(p => `<p class="read" style="margin:0 0 14px">${esc(p)}</p>`).join("")}</div>
        <div><h2>Quién manda adentro</h2><ul class="mlist">${F.manda.map(x => `<li>${esc(x)}</li>`).join("")}</ul></div>
        <div><h2>Dinero</h2><p class="read">${esc(F.dinero)}</p></div>
        <div><h2>Cronología</h2><div class="crono">${F.crono.map(([d, x]) => `<div><span class="mono">${esc(d)}</span><p>${esc(x)}</p></div>`).join("")}</div></div>
        <div><h2>Fuentes</h2><ol class="fuentes">${F.fuentes.map(([t, u]) => `<li><a href="${esc(u)}" rel="noopener" target="_blank">${esc(t)}</a></li>`).join("")}</ol><p class="note">Ficha revisada el ${fecha(F.rev)}.</p></div><div><h2>Perfil de poder</h2>${perfil}</div>`
        : `<div><h2>Resumen y contexto</h2><div class="pending">Ficha en preparación: el resumen, quién manda adentro, el dinero, la cronología y las fuentes se cargan por tandas, con un dato verificable para cada puntaje.</div></div><div><h2>Perfil de poder</h2>${perfil}</div>`}
      </div>
      <aside class="org-side">
        <div class="box"><span class="lbl">Por familia</span>${radar(o)}</div>
        <div class="box"><span class="lbl">Dependencias</span>
          <div class="side-x"><b>Depende de:</b> ${deps.length ? deps.map(d => `<a href="#o-${d.id}">${esc(corto(d.n))}</a>`).join(", ") : "nadie en el mapa"}</div>
          <div class="side-x"><b>Dependen de ella:</b> ${subs.length ? subs.map(d => `<a href="#o-${d.id}">${esc(corto(d.n))}</a>`).join(", ") : "ninguna del mapa"}</div></div>
        <div class="box"><span class="lbl">Aliados y enemigos</span>${relHtml}</div>
        <div class="box"><span class="lbl">Fase de Quigley</span><div class="phase">${["E", "C", "D"].map(f => `<span class="${o.fase === f ? "on" : ""}">${M.fases[f]}</span>`).join("")}</div></div>
      </aside></div></div>`;
  };

  V.quien = () => {
    let mode = "pe", cur = null, showRel = true, view = "grafico", topN = 60, fB = "", fT = "";
    const norm = t => t.normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase();
    app.innerHTML = `<div class="wrap"><div class="page-head"><div style="display:flex;flex-direction:column;gap:12px"><div class="kick">Esquema</div><h1>Quién manda</h1></div>
      <p class="read">La jerarquía real, no la del organigrama: quién decide solo, quién tiene criterio propio dentro de un bloque, quién obedece y quién es fachada de otro. La fila indica la autonomía; el tamaño, el poder; el color, el bloque; la forma, el tipo. Buscá un actor o filtrá para ver menos a la vez.</p></div>
      <div class="qm-tools">
        <label class="qm-search">Buscar<input id="qS" type="search" list="qL" placeholder="Nombre de un actor" autocomplete="off"><datalist id="qL">${ORGS.slice().sort((a, b) => corto(a.n).localeCompare(corto(b.n), "es")).map(o => `<option value="${esc(corto(o.n))}"></option>`).join("")}</datalist></label>
        <label>Mostrar<select id="qN"><option value="30">Los 30 con más poder</option><option value="60" selected>Los 60 con más poder</option><option value="120">Los 120 con más poder</option><option value="0">Todos (${ORGS.length})</option></select></label>
        <label>Bloque<select id="qB"><option value="">Todos</option>${["T", "E", "I", "P", "X"].map(k => `<option value="${k}">${esc(BL[k].n)}</option>`).join("")}</select></label>
        <label>Tipo<select id="qT"><option value="">Todos</option>${M.tipos.map(t => `<option>${t}</option>`).join("")}</select></label>
      </div>
      <div class="chips" style="margin-bottom:14px"><button type="button" class="chip" data-v="grafico">Gráfico</button><button type="button" class="chip" data-v="lista">Lista por nivel</button><span class="chip-sep" aria-hidden="true"></span><button type="button" class="chip" data-m="pe">Poder efectivo</button><button type="button" class="chip" data-m="oculto">Poder oculto</button><span class="chip-sep" aria-hidden="true"></span><button type="button" class="chip" data-r>Relaciones</button></div>
      <section class="block"><div class="panel"><div class="split"><div class="stage" id="qstage"></div><aside id="qside"></aside></div></div></section></div>`;
    const stage = document.getElementById("qstage"), side = document.getElementById("qside");
    const linked = id => new Set([id, ...byId[id].dep, ...dependents(id).map(d => d.id), ...relsOf(id).map(r => r.a === id ? r.b : r.a)]);
    const visible = () => {
      let l = sortBy(mode).filter(o => (!fB || o.bloque === fB) && (!fT || o.tipo === fT));
      if (topN) l = l.slice(0, topN);
      const set = new Set(l.map(o => o.id));
      if (cur) linked(cur).forEach(i => set.add(i));
      return ORGS.filter(o => set.has(o.id));
    };
    const near = id => !cur || linked(cur).has(id);
    const rad = o => 3 + Math.sqrt(Math.max(o[mode], 0)) * (mode === "pe" ? 1.9 : 2.2);
    function graph(vis) {
      const VW = 1200, top = 24, labelAll = vis.length <= 130, PER = labelAll ? 14 : 30, SUBH = labelAll ? 84 : 62;
      const rows = [1, 2, 3, 4].map(a => vis.filter(o => o.aut === a));
      const yBase = {}; let acc = top;
      [1, 2, 3, 4].forEach(a => { const n = rows[a - 1].length; yBase[a] = acc; acc += n ? 40 + Math.ceil(n / PER) * SUBH : 0; });
      const VH = acc + 10, pos = {}, below = {};
      rows.forEach((list, ri) => {
        const a = ri + 1; if (!list.length) return;
        const sorted = list.slice().sort((x, y) => BORDER.indexOf(x.bloque) - BORDER.indexOf(y.bloque) || y[mode] - x[mode]);
        const nsub = Math.ceil(sorted.length / PER), per = Math.ceil(sorted.length / nsub);
        sorted.forEach((o, i) => { const s = Math.floor(i / per), k = i % per, cnt = Math.min(per, sorted.length - s * per);
          const x = 70 + (cnt === 1 ? (VW - 140) / 2 : k * (VW - 140) / (cnt - 1));
          const y = yBase[a] + 40 + s * SUBH + SUBH / 2 - 4 + (labelAll ? 0 : ((k % 2) ? 7 : -7));
          pos[o.id] = [x, y]; below[o.id] = k % 2 === 0; });
      });
      const lv = [1, 2, 3, 4].filter(a => rows[a - 1].length).map((a, i) => `<g class="qm-row">${i ? `<line x1="16" x2="${VW - 16}" y1="${yBase[a] - 4}" y2="${yBase[a] - 4}"/>` : ""}<text class="qm-lv" x="16" y="${yBase[a] + 14}">${a} · ${esc(M.autonomia[a]).toUpperCase()} (${rows[a - 1].length})</text></g>`).join("");
      const deps = vis.flatMap(o => o.dep.filter(d => pos[d]).map(d => { const [x1, y1] = pos[o.id], [x2, y2] = pos[d], on = !cur || cur === o.id || cur === d;
        return `<path class="qm-dep" d="M${x1},${y1} C${x1},${(y1 + y2) / 2} ${x2},${(y1 + y2) / 2} ${x2},${y2}" opacity="${on ? (cur ? .9 : .3) : .04}"/>`; })).join("");
      const rels = showRel ? REL.filter(r => pos[r.a] && pos[r.b] && (cur ? (r.a === cur || r.b === cur) : r.i === 3)).map(r => { const [x1, y1] = pos[r.a], [x2, y2] = pos[r.b], mx = (x1 + x2) / 2, my = Math.min(y1, y2) - 30 - Math.abs(x1 - x2) * .1;
        const st = r.t === "Enfrentamiento" ? 'stroke="#FF3B30" stroke-dasharray="6 4"' : (r.t === "Ambigua" ? 'stroke="#F2A93B" stroke-dasharray="4 3"' : (r.t === "Puerta giratoria" || r.t === "Acceso a datos") ? 'stroke="#9A8F8C" stroke-dasharray="2 4"' : 'stroke="#EDE6E3"');
        return `<path class="qm-rel" d="M${x1},${y1} Q${mx},${my} ${x2},${y2}" ${st} opacity="${cur ? .9 : .3}"/>`; }).join("") : "";
      const nodes = vis.slice().sort((a, b) => rad(b) - rad(a)).map(o => { const [x, y] = pos[o.id], r = Math.min(rad(o), 30), dim = !near(o.id), lab = cur ? near(o.id) : (labelAll || r > 13.5);
        const ty = below[o.id] || !labelAll ? y + r + 13 : y - r - 6, nm = corto(o.n), t = nm.length > 22 ? nm.slice(0, 21) + "…" : nm;
        return `<g class="qm-n" data-id="${o.id}" tabindex="0" role="button" aria-label="${esc(o.n)}" opacity="${dim ? .12 : 1}"><circle cx="${x}" cy="${y}" r="${Math.max(r, 12)}" fill="transparent"/>${shape(o.tipo, x, y, r, bcol(o.bloque), `fill-opacity="${o.tipo === "Sombra" ? 1 : .9}"`)}${cur === o.id ? `<circle cx="${x}" cy="${y}" r="${r + 6}" fill="none" stroke="#FF3B30" stroke-width="2"/>` : ""}${lab ? `<text x="${x}" y="${ty}"${cur === o.id ? ' class="cur"' : ""}>${esc(t)}</text>` : ""}</g>`; }).join("");
      stage.innerHTML = `<div class="qm-scroll"><svg id="qm" viewBox="0 0 ${VW} ${VH}" role="img" aria-label="Gráfico de jerarquía entre organizaciones">${lv + deps + rels + nodes}</svg></div><p class="note" style="padding:0 14px 12px">${vis.length} actores a la vista. En el teléfono el gráfico se desliza de costado.</p>`;
      return pos;
    }
    function list(vis) {
      stage.innerHTML = `<div class="qm-list">${[1, 2, 3, 4].map(a => { const l = vis.filter(o => o.aut === a).sort((x, y) => y[mode] - x[mode]); if (!l.length) return "";
        return `<div><div class="lbl" style="padding:0 0 8px;border-bottom:1px solid var(--line)">${a} · ${esc(M.autonomia[a])} (${l.length})</div>${l.map(o => `<button type="button" class="qm-it${cur === o.id ? " on" : ""}" data-id="${o.id}" style="opacity:${near(o.id) ? 1 : .3}">${icon(o)}<span>${esc(corto(o.n))}<small>${o.dep.length ? "depende de " + esc(o.dep.map(d => corto(byId[d].n)).join(", ")) : esc(o.area)}</small></span><b>${num(o[mode])}</b></button>`).join("")}</div>`; }).join("")}</div><p class="note" style="padding:0 16px 14px">${vis.length} actores a la vista, ordenados por ${mode === "pe" ? "poder efectivo" : "poder oculto"}.</p>`;
    }
    const draw = (focus = false) => {
      app.querySelectorAll("[data-m]").forEach(b => { b.classList.toggle("on", b.dataset.m === mode); b.setAttribute("aria-pressed", b.dataset.m === mode); });
      app.querySelectorAll("[data-v]").forEach(b => { b.classList.toggle("on", b.dataset.v === view); b.setAttribute("aria-pressed", b.dataset.v === view); });
      const rb = app.querySelector("[data-r]"); rb.classList.toggle("on", showRel); rb.setAttribute("aria-pressed", showRel); rb.hidden = view !== "grafico";
      const vis = visible();
      const pos = view === "grafico" ? graph(vis) : (list(vis), null);
      side.innerHTML = cur ? orgPanel(byId[cur]) + `<div class="box" style="padding:12px"><span class="lbl">Por familia</span>${radar(byId[cur])}</div>` + `<div class="side-x"><b>Depende de:</b> ${byId[cur].dep.map(d => `<a href="#" data-go="${d}">${esc(corto(byId[d].n))}</a>`).join(", ") || "nadie en el mapa"}<br><b>Dependen de él:</b> ${dependents(cur).map(d => `<a href="#" data-go="${d.id}">${esc(corto(d.n))}</a>`).join(", ") || "ninguno"}</div><button type="button" class="chip" data-clear style="align-self:flex-start">Ver todo</button>`
        : `<div class="lbl">Cómo leerlo</div>${[1, 2, 3, 4].map(a => `<p class="side-x"><b>${a} · ${esc(M.autonomia[a])}.</b> ${["Sin superior en lo estratégico.", "Decide su estrategia dentro de un bloque o jurisdicción que puede limitarla.", "Ejecuta lo que decide otro.", "Aparenta una independencia que no tiene."][a - 1]}</p>`).join("")}
          <div class="legend">${["T", "E", "I", "P", "X"].map(k => `<div><span class="sq" style="background:${BL[k].c}"></span>${esc(BL[k].n)}</div>`).join("")}</div>
          <div class="legend">${M.tipos.map(t => `<div><svg width="16" height="16" aria-hidden="true">${shape(t, 8, 8, 6.4, "#EDE6E3")}</svg>${t}</div>`).join("")}</div>
          <p class="note">Las líneas grises marcan de quién depende cada uno. Sin selección se muestran solo las relaciones fuertes; tocá un actor para ver todas las suyas y a quiénes está ligado.</p>`;
      const clr = side.querySelector("[data-clear]"); if (clr) clr.onclick = () => { cur = null; document.getElementById("qS").value = ""; draw(); };
      side.querySelectorAll("[data-go]").forEach(a => a.onclick = e => { e.preventDefault(); select(a.dataset.go, true); });
      activate(stage, "[data-id]", g => { cur = cur === g.dataset.id ? null : g.dataset.id; draw(true); });
      bindTip(stage, ".qm-n", g => { const o = byId[g.dataset.id]; return `<b>${esc(o.n)}</b><span>${esc(o.area)} · ${esc(BL[o.bloque].n)}</span><span>Efectivo ${num(o.pe)} · en red ${num(o.red)} · oculto ${num(o.oculto)}</span>`; });
      if (focus && cur) {
        if (pos && pos[cur]) { const sc = stage.querySelector(".qm-scroll"), svg = sc.querySelector("svg"); sc.scrollLeft = pos[cur][0] / 1200 * svg.clientWidth - sc.clientWidth / 2; }
        if (innerWidth < 980) side.scrollIntoView({ block: "start" });
      }
    };
    const select = (id, focus) => { cur = id; document.getElementById("qS").value = corto(byId[id].n); draw(focus); };
    const qS = document.getElementById("qS");
    const find = () => { const q = norm(qS.value.trim()); if (!q) return null;
      return ORGS.find(o => norm(corto(o.n)) === q) || ORGS.find(o => norm(o.n).startsWith(q)) || sortBy("pt").find(o => norm(o.n).includes(q)); };
    qS.addEventListener("change", () => { const o = find(); if (o) select(o.id, true); });
    qS.addEventListener("keydown", e => { if (e.key === "Enter") { e.preventDefault(); const o = find(); if (o) select(o.id, true); } });
    qS.addEventListener("search", () => { if (!qS.value) { cur = null; draw(); } });
    document.getElementById("qN").onchange = e => { topN = +e.target.value; draw(); };
    document.getElementById("qB").onchange = e => { fB = e.target.value; draw(); };
    document.getElementById("qT").onchange = e => { fT = e.target.value; draw(); };
    app.querySelectorAll("[data-m]").forEach(b => b.onclick = () => { mode = b.dataset.m; draw(); });
    app.querySelectorAll("[data-v]").forEach(b => b.onclick = () => { view = b.dataset.v; draw(); });
    app.querySelector("[data-r]").onclick = () => { showRel = !showRel; draw(); };
    draw();
  };

  V.marco = () => {
    app.innerHTML = `<div class="wrap"><div class="page-head"><div style="display:flex;flex-direction:column;gap:12px"><div class="kick">Método</div><h1>Marco</h1></div></div>
      <div class="prose" style="padding-bottom:40px">
        <p>El sitio responde una sola pregunta: quién tiene el poder real en el mundo y quién solo lo aparenta. La unidad de análisis es la organización con nombre propio, no el país: un gobierno, un ejército, una agencia de inteligencia, una empresa, una familia, un partido, una red criminal o una persona.</p>
        <h2>La tesis</h2>
        <p>El mapa toma su marco del libro <i>Cryptocracy. A Human Guide for an Age of Institutional Collapse</i> (Franco Martín López, 2026). Su punto de partida es una tesis sobre la naturaleza humana: las personas no son, en el fondo, buenas. No son malvadas, pero tienden al menor esfuerzo, ponen su interés y el de los suyos por delante del de los demás y razonan peor de lo que suponen las teorías que las imaginan racionales. Las instituciones diseñadas para personas mejores que las reales fracasan; las que funcionan son las que cuentan con esa naturaleza y no confían en la benevolencia de quien manda.</p>
        <p>De ahí el diagnóstico: la civilización que produjo las mejores teorías de la libertad individual y del gobierno limitado se está degradando desde adentro, no por conquista sino por acumulación de fallas institucionales. Sus democracias conservan la forma —elecciones, tribunales, prensa, constitución— mientras crece por debajo una arquitectura paralela de poder que no responde a ninguna de ellas. A esa deformación el libro la llama <b>criptocracia</b>, del griego <i>kryptós</i>, oculto, y <i>krátos</i>, poder: el gobierno oculto.</p>
        <p>Para el libro, el punto de inflexión es el asesinato de John F. Kennedy, el 22 de noviembre de 1963: el momento en que el Estado operativo se impuso al constitucional y quitó del medio a un presidente en ejercicio que intentaba controlarlo, y demostró que podía sobrevivir a las consecuencias. El libro no lo presenta como un hecho probado; sostiene que el registro institucional alcanza para considerar insuficiente la versión oficial, y que todo lo que vino después —vigilancia masiva, persecución de quienes revelan secretos, emergencia legal permanente— se apoya en esa demostración de impunidad.</p>
        <p>La criptocracia no es una conspiración sino una estructura: el resultado previsible de fuerzas que operan en toda sociedad grande y compleja. Los instrumentos con que una civilización crece se convierten en instituciones que se defienden a sí mismas; una clase de gerentes y burócratas toma el control de las organizaciones sin ser dueña ni electa; las minorías organizadas capturan a las mayorías dispersas; el dinero barato fabrica auges artificiales que después hay que pagar. Para el libro, Occidente está en su fase de contracción, y la presión de civilizaciones rivales que no comparten sus premisas agrava ese proceso.</p>
        <h2>Sistemas de gobierno</h2>
        <ul>
          <li><b>Autocracia.</b> Lo que la distingue es la <b>transparencia de la dominación</b>: la población sabe, en algún nivel, cómo es el arreglo, y el poder no necesita esconderse. Adopta muchas formas: monarquía absoluta, dictadura personal, junta militar, partido único, teocracia o régimen personalista con elecciones decorativas. El libro distingue tres modelos principales: la <b>tecnocracia de resultados</b>, que pide obediencia a cambio de prosperidad y orgullo nacional, como en China; el <b>régimen nacionalista e imperial</b>, que vació la fachada democrática hasta volverla ornamental y necesita un enemigo exterior, como en Rusia; y el <b>híbrido teocrático</b>, en el que las elecciones funcionan como filtro y no como competencia, como en Irán. En el extremo quedan los regímenes residuales, sostenidos por la inercia dinástica o la dependencia de recursos, que ya ni siquiera buscan legitimarse.</li>
          <li><b>Criptocracia.</b> La etapa más baja de las democracias republicanas constitucionales. Mantiene elecciones, tribunales, prensa libre y constitución, y al mismo tiempo sostiene un Estado operativo que no responde a ninguno de ellos: inteligencia clandestina, asesinatos selectivos, vigilancia encubierta, chantaje institucionalizado, control oligopólico de la información y represión violenta selectiva. Una casta chica que se reproduce a sí misma opera por encima de la constitución y por debajo del escrutinio público, protegida por excepciones legales, el secreto oficial y la deferencia habitual de las instituciones ante la «seguridad». Lo que la define es la distancia entre el Estado visible y el operativo, y por eso depende de la ficción de su propia legitimidad. Castiga la exposición más que el delito: quien revela un abuso recibe más castigo que quien lo cometió. Los ciudadanos votan, debaten y protestan dentro de límites que no pueden ver. En el mapa, el <b>poder oculto</b> de cada organización es su índice criptocrático.</li>
          <li><b>Democracia republicana constitucional: la teoría y la fachada.</b> Es el modelo que todos invocan y ninguno cumple: la teoría que se enseña y la fachada detrás de la cual operan las criptocracias. En teoría tiene soberanía popular con elecciones libres, limpias y competitivas; una constitución que limita al poder y no puede cambiarse a gusto de quien gobierna; división de poderes —ejecutivo, legislativo y judicial independientes— con frenos y contrapesos reales; Estado de derecho, en el que nadie está por encima de la ley, ni siquiera los servicios secretos; derechos civiles y políticos garantizados: libertad de expresión, de prensa, de reunión y de culto, debido proceso, propiedad e igualdad ante la ley; control civil efectivo de las fuerzas armadas y de inteligencia; transparencia y rendición de cuentas personal de quienes deciden. En la práctica, esas instituciones siguen en pie como decorado: se vota, se legisla y se juzga, pero las decisiones de fondo se toman en otro lado.</li>
        </ul>
        <p>En el mundo actual no hay ninguna democracia republicana constitucional real. Lo que existe son autocracias, que dominan a la vista, y criptocracias, que dominan detrás de la fachada democrática. Los países que se presentan como democracias funcionan, en distinto grado, como criptocracias. Por eso el sitio no clasifica países por su régimen formal: mide, organización por organización, cuánto poder real tiene cada una y cuánto de ese poder escapa al control público.</p>
        <h2>El orden mundial: imperios, protectorados, colonias y zonas liberadas</h2>
        <p>Debajo del mapa de los Estados soberanos, todos iguales en la ONU, hay otro mapa: el de los imperios. Cada imperio tiene un <b>país centro</b> y a su alrededor una gradación de dependencia, que el libro describe como la dependencia administrada de Estados clientes respecto de un hegemón cuyas decisiones no se espera que discutan. Hoy hay un imperio transoceánico, con centro en Estados Unidos, y una alianza euroasiática, con centros en China y Rusia. Fuera de ellos quedan unas pocas potencias independientes, como la India y Brasil, y un terreno disputado donde los bloques compiten.</p>
        <ul>
          <li><b>Centro.</b> Decide la estrategia del bloque y tiene la última palabra en guerra, moneda y alianzas.</li>
          <li><b>Aliado con autonomía.</b> Pertenece al bloque, pero conserva criterio estratégico propio y capacidad de decir que no; por ejemplo, el Reino Unido, Francia o Israel, al que el libro ubica en una categoría especial: más que un protectorado, un socio estratégico con acceso excepcional a la política estadounidense.</li>
          <li><b>Integrado.</b> Forma parte del bloque y rara vez se aparta de su línea, aunque gestione sus asuntos internos. Es el lugar de buena parte de Europa occidental, que durante la Guerra Fría fue, para el libro, un protectorado en sentido estricto: dependiente militarmente, integrada económicamente y limitada para tener una política exterior propia.</li>
          <li><b>Protectorado.</b> Tiene un grado de independencia y gobierno propio, pero cuando el centro da una orden la cumple: su seguridad, su economía o la supervivencia de sus gobernantes dependen de él. Ejemplos: Taiwán, Ucrania o Jordania; Bielorrusia, del lado euroasiático.</li>
          <li><b>Colonia de hecho.</b> Figura como otro país, con bandera, asiento en la ONU y gobierno, pero la potencia ejerce el control como si fuera parte de su territorio: decide su defensa, su moneda o su presupuesto, y su gobierno no puede contradecirla. A esto se suman los territorios que son formalmente dependientes, como Puerto Rico, Guam o Groenlandia.</li>
          <li><b>Pendular, inclinado o sin alinear.</b> Países que negocian con más de un bloque, que se inclinan hacia uno sin pertenecer del todo o que se mantienen fuera de ambos.</li>
        </ul>
        <p>Además están las <b>zonas liberadas</b>: territorios, a veces dentro de países que figuran como soberanos y estables, donde el Estado no manda y cada actor hace lo que su poder real le permite. Un cártel cobra impuestos y administra justicia en una región de México; una milicia controla una frontera; una facción criminal gobierna cárceles y barrios en Brasil; una potencia extranjera mantiene tropas que nadie invitó. Son, también, la frontera en el sentido del libro: los espacios fuera del alcance de un poder único. El mapa las marca por grado (parcial, extendida o total) y por aspecto: territorial, crimen organizado, fronteras, fiscal y económico, o presencia extranjera. Todo esto se ve en las capas «Posición» y «Zonas liberadas» del mapa de <a href="#paises">Países</a>.</p>
        <h2>Marco teórico</h2>
        <p><b>Geopolítica y realismo</b></p>
        <ul>
          <li><b>John Mearsheimer y el realismo ofensivo</b> (<i>La tragedia de la política de las grandes potencias</i>, 2001; <i>The Great Delusion</i>, 2018). Es el eje del análisis geopolítico del sitio. El sistema internacional es anárquico: no hay autoridad por encima de los Estados y ninguno puede estar seguro de las intenciones de los otros. La respuesta racional de una gran potencia es maximizar su poder relativo, buscar la hegemonía en su región e impedir que otra la consiga en la suya. Por eso el ascenso de China empuja a sacar a EE.UU. del Pacífico occidental, como EE.UU. sacó a Europa de América con la doctrina Monroe, y Rusia trata la frontera ucraniana como EE.UU. trató los misiles en Cuba. La «hegemonía liberal» —exportar la democracia y rehacer a otros países a imagen propia— fracasa porque el nacionalismo pesa más que el liberalismo y la seguridad más que las instituciones; la alternativa es el equilibrio a distancia (<i>offshore balancing</i>). Mearsheimer explica también el «poder de contención del agua»: los océanos frenan a los ejércitos, y por eso el imperio transoceánico domina desde afuera.</li>
          <li><b>El realismo clásico y la <i>realpolitik</i>.</b> Tucídides y el miedo que el ascenso de una potencia provoca en la establecida; Maquiavelo, que separa la política de la moral declarada; Hobbes y el estado de naturaleza; Hans Morgenthau y el interés definido como poder; E. H. Carr y la crítica del idealismo; Kenneth Waltz y la estructura del sistema internacional; Henry Kissinger y el equilibrio de poder. Todos parten de que el poder se mide por lo que se puede hacer, no por lo que se declara.</li>
          <li><b>Las fallas de las civilizaciones</b> (Samuel Huntington, <i>El choque de civilizaciones</i>, 1996) y <b>la adaptación de los rivales</b> (David Kilcullen, <i>The Dragons and the Snakes</i>, 2020). Los conflictos del siglo XXI corren entre civilizaciones que no comparten las premisas occidentales, y los adversarios aprendieron a competir sin hacerlo en los términos de Occidente: guerra en la zona gris, desinformación, fuerzas interpuestas y presión económica y tecnológica.</li>
        </ul>
        <p><b>Civilización, frontera y decadencia</b></p>
        <ul>
          <li><b>La evolución de las civilizaciones</b> (Carroll Quigley, 1961). Una civilización nace como sociedad productora y crece mediante un «instrumento de expansión» —militar, comercial, religioso o tecnológico—. Con el tiempo, quienes controlan ese instrumento desarrollan intereses propios y lo convierten en una institución que se defiende a sí misma: el paso de la expansión a la conservación es el primer paso de la decadencia. Quigley describe fases que van de la gestación y la expansión a la era de conflictos, el imperio universal, la decadencia y la invasión. El sitio aplica esa lógica a cada organización: expansión, captura o distorsión.</li>
          <li><b>La teoría de la frontera</b> (Frederick Jackson Turner, 1893). Las civilizaciones no nacen en el centro sino en el borde: la frontera, el límite móvil entre lo ordenado y lo que nadie gobierna, obliga a resolver problemas sin instituciones heredadas y forja el individualismo, el pragmatismo y la tolerancia al riesgo. Cuando la frontera se cierra, la sociedad se vuelve sobre sí misma. La frontera no es solo geográfica: también es institucional, tecnológica e intelectual. Hoy son el espacio, el ciberespacio, el Ártico, los fondos marinos y la inteligencia artificial.</li>
          <li><b>La destrucción creativa</b> (Joseph Schumpeter). El capitalismo avanza porque lo nuevo desplaza a lo viejo; su figura central es el emprendedor, no el gerente ni el burócrata. Cuando las organizaciones establecidas logran frenar esa destrucción, la civilización deja de expandirse.</li>
          <li><b>La clase ociosa</b> (Thorstein Veblen, <i>Teoría de la clase ociosa</i>, 1899). Las clases dominantes muestran su dominio con el consumo y el ocio ostentosos, la exhibición de la capacidad de derrochar lo que otros necesitan. Es la señal de que una élite completó el paso de instrumento a institución: su actividad principal ya no es crear valor sino representar estatus. Cuando esa clase ociosa se funde con la clase gerencial, las organizaciones que debían impulsar la expansión quedan en manos de quienes más interés tienen en impedirla.</li>
          <li><b>El ciclo económico austríaco</b> (Ludwig von Mises y Friedrich Hayek). Cuando los bancos centrales bajan artificialmente la tasa de interés, envían una señal falsa de ahorro abundante que produce inversiones insostenibles, un auge artificial y una crisis posterior. Los sectores que viven del auge presionan para prolongarlo, y cada intervención genera la demanda de la siguiente. Ray Dalio describe un ciclo largo similar para los imperios y sus monedas de reserva.</li>
        </ul>
        <p><b>Poder, élites y democracia</b></p>
        <ul>
          <li><b>La revolución gerencial</b> (James Burnham, 1941) y <b>los maquiavelistas</b> (Burnham, 1943, sobre Gaetano Mosca, Vilfredo Pareto y Robert Michels). Siempre gobierna una minoría organizada, y toda organización termina en manos de quienes la administran. En el siglo XX el poder real pasó a una clase de gerentes, técnicos y burócratas que no necesitan ser dueños del Estado ni de los medios de producción: les basta controlar la información, el personal y la maquinaria. En la criptocracia, el aparato de inteligencia y seguridad es exactamente ese estrato.</li>
          <li><b>La poliarquía y el costo de reprimir</b> (Robert Dahl, 1971). Un gobierno tolera la oposición cuando reprimirla le cuesta más que tolerarla. La criptocracia invierte esa ecuación sin abolir las instituciones democráticas: una parte del Estado aprende a reprimir a bajo costo visible, mediante el secreto, la vigilancia, la persecución legal y las operaciones encubiertas.</li>
          <li><b>La elección pública</b> (Kenneth Arrow, James Buchanan y Gordon Tullock, Anthony Downs, William Niskanen, Mancur Olson). Votantes, políticos y burócratas persiguen su propio interés: el votante elige no informarse, el político prioriza la reelección, el burócrata busca agrandar su presupuesto y los grupos organizados le ganan a las mayorías dispersas. El resultado es la búsqueda de rentas: usar la política para capturar valor en vez de crearlo. Hans-Hermann Hoppe extiende la crítica a la lógica de corto plazo de la democracia de masas, y Karl Popper aporta la defensa de la sociedad abierta frente a quienes se creen dueños de la verdad.</li>
        </ul>
        <p><b>Naturaleza humana y poder</b></p>
        <ul>
          <li><b>La naturaleza humana sin consuelo.</b> El libro parte de que las personas tienden al menor esfuerzo, al interés propio y a razonar peor de lo que creen, y de que quienes ocupan el poder no son la excepción. Las instituciones tienen que diseñarse para esa naturaleza y no para otra.</li>
          <li><b>Robert Greene</b> (<i>Las 48 leyes del poder</i>, <i>Las leyes de la naturaleza humana</i>). Las organizaciones las dirigen personas, y las personas buscan poder, ocultan sus intenciones, cultivan apariencias, se alían por interés y temen perder posición. Entender esas pulsiones explica por qué el poder real se esconde detrás del formal y por qué la apariencia de debilidad o de virtud es, muchas veces, una estrategia.</li>
        </ul>
        <h2>Cómo se mide</h2>
        <p>Cada organización recibe de 0 a 3 en ${M.ejes.length} ejes agrupados en seis familias. El 3 se reserva a quienes están entre los pocos primeros del mundo en ese eje. El sitio mide el poder real y no la jerarquía oficial, así que el poder duro pesa más: la coerción violenta, la obtención de información y la acción fuera de la ley valen doble, y los contactos y el privilegio legal una vez y media. Los pesos son fijos.</p>
        <p>Además de los ejes de recursos, dinero, fuerza, información y normas, tres ejes miden rasgos que la jerarquía formal no muestra: la <b>cohesión interna</b> (3 si hay un mando único sin pujas; 0 si el actor está partido en facciones enfrentadas), el <b>apoyo popular</b> (votos, aprobación, fieles o usuarios) y el <b>privilegio legal</b> (inmunidad, veto, indulto, secreto sin control, monopolio legal de un mercado o permiso para hacer lo que para otros sería delito). La <b>acción fuera de la ley</b> incluye la violencia encubierta y el crimen organizado, pero también la corrupción: sobornos, tráfico de influencias, desvío de fondos, robo y fraude.</p>
        <p>En cohesión, apoyo popular y privilegio, cada categoría tiene un valor de partida y los casos que se apartan se corrigen uno por uno. Los 521 actores se revisaron uno por uno el 17 de noviembre de 2026, también en alcance efectivo.</p>
      </div>
      <div class="tbl-wrap"><table><thead><tr><th>Familia</th><th>Eje</th><th>3 · Dominante</th><th>2 · Alto</th><th>1 · Relevante</th></tr></thead><tbody>${M.ejes.map(e => `<tr><td class="muted">${esc(e.fam)}</td><td><b>${esc(e.n)}</b><br><span class="muted">${esc(e.x)}</span></td>${e.a.map(a => `<td>${esc(a)}</td>`).join("")}</tr>`).join("")}</tbody></table></div>
      <div class="prose" style="padding:40px 0 64px">
        <h2>Fórmulas</h2>
        <ul>
          <li><b>Puntaje de poder (0 a 100):</b> media geométrica ponderada de cinco componentes, cada uno llevado a una escala de 0 a 1: puntaje teórico de su categoría, ${pct(M.peso_final.ct)}; capacidad, ${pct(M.peso_final.cap)}; alcance efectivo, ${pct(M.peso_final.alc)}; autonomía real, ${pct(M.peso_final.aut)}; red de dependientes, ${pct(M.peso_final.red)}. Los componentes se multiplican, cada uno elevado a su peso, así que un actor débil en uno no lo compensa del todo con los demás. Al final el resultado se eleva a la potencia ${M.estirar}, para que la escala refleje distancias de poder de varios órdenes de magnitud sin cambiar el orden, y se reescala: el actor más poderoso vale 100.</li>
          <li><b>Alcance efectivo:</b> dónde puede actuar de verdad, no lo que la ley le permite. ${Object.values(M.alcance).map(a => `${esc(a.n)}: ${num(a.v, 2)}`).join("; ")}. Se asigna actor por actor: global si puede actuar de verdad en cualquier parte del mundo (por armas, redes, mercados o inteligencia), regional si llega a un grupo de países, nacional si no sale del suyo. Pesa sobre todo a favor de las agencias de inteligencia, los ejércitos con armas de alcance mundial, las grandes empresas y las redes criminales transnacionales.</li>
          <li><b>Red de dependientes:</b> el poder que hereda de quienes dependen de él (poder en red menos poder efectivo), en escala logarítmica para que no domine a los demás componentes.</li>
          <li><b>Capacidad:</b> suma ponderada de los ${M.ejes.length} ejes, llevada a una escala de 0 a ${M.capmax}. Pesos: coerción, adquisición de información y acción fuera de la ley, 2; contactos y privilegio legal, 1,5; el resto, 1.</li>
          <li><b>Autonomía real:</b> el factor formal (1 decide solo: 1; 2 aliado con criterio propio: 0,75; 3 subordinado: 0,5; 4 fachada: 0,25) sube hacia 1 según su poder duro: coerción, información, acción fuera de la ley y contactos. Una agencia de inteligencia que depende de un gobierno conserva así buena parte de su poder, porque puede resistirlo.</li>
          <li><b>Poder efectivo:</b> capacidad por el factor de autonomía real.</li>
          <li><b>Poder en red:</b> poder efectivo más la mitad del poder en red de quienes dependen de él, descontada la parte que esos dependientes pueden sustraerle por su propio poder duro; en cadena.</li>
          <li><b>Poder formal:</b> de 0 a 3, cuánto de su poder está reconocido públicamente y sujeto a control: ley, elecciones, tribunales, auditoría, transparencia.</li>
          <li><b>Brecha:</b> la parte de su poder que escapa a ese control. <b>Poder oculto:</b> poder efectivo por brecha.</li>
        </ul>
        <h2>Tipos y categorías de actores</h2>
        <p>Cada actor pertenece a una de ${Object.keys(M.categorias).length} categorías, agrupadas en ${M.tipos.length} tipos. Cada categoría tiene dos puntajes de 0 a 10. El <b>teórico</b> es un criterio editorial: cuánto poder real suele tener ese tipo de actor, con más peso para quien tiene armas, secretos o margen para actuar fuera de la ley. El <b>real</b> sale de los datos cargados en el mapa: es el promedio, entre los actores de la categoría, de su autonomía (50 %), de cuánto manda, financia o abastece a otros frente a cuánto depende de otros (30 %), de cuántos actores dependen de él (20 %) y de si enfrentó a su propio jefe formal (15 % adicional, con tope en 10). El puntaje real es informativo: no entra en el puntaje de poder, para no contar dos veces la autonomía y las relaciones, que ya están en la fórmula.</p>
        <p>Los partidos se dividen en dos categorías: el <b>partido único o hegemónico</b>, que controla el Estado sin alternancia real (como el PCCh), y el <b>partido en sistema competitivo</b>, que puede perder el gobierno en elecciones.</p>
        <p>Solo figuran monarcas con poder real: los que gobiernan o conservan poder de veto o de decisión. Las monarquías ceremoniales, como las de Reino Unido, España, Japón, los países nórdicos, Países Bajos y Bélgica, no entran.</p>
      </div>
      <div class="tbl-wrap"><table><thead><tr><th>Tipo</th><th>Categoría</th><th>Actores</th><th>Teórico</th><th>Real</th></tr></thead><tbody>${M.tipos.flatMap(t => Object.entries(M.categorias).filter(([, c]) => c.tipo === t).sort((a, b) => b[1].t - a[1].t || a[0].localeCompare(b[0], "es")).map(([n, c], i) => `<tr><td class="muted">${i ? "" : esc(t)}</td><td>${esc(n)}</td><td>${c.k}</td><td>${num(c.t, 0)}</td><td>${num(c.r, 1)}</td></tr>`)).join("")}</tbody></table></div>
      <div class="prose" style="padding:40px 0 64px">
        <h2>Cambios recientes</h2>
        <ul>${M.cambios.map(([f, x]) => `<li><b>${fecha(f)}.</b> ${esc(x)}</li>`).join("")}</ul>
        <h2>Resguardos</h2>
        <ul>
          <li>Cada organización lleva un nivel de certeza: documentado, estimado o especulativo.</li>
          <li>Toda afirmación que califique a una organización de fachada o protectorado, o la vincule con delitos o con grupos armados, lleva fuente. El eje «acción fuera de la ley» solo se puntúa con un hecho documentado, y en personas vivas solo con lo establecido por un tribunal o un organismo oficial.</li>
          <li>Nada especulativo se publica sobre personas vivas.</li>
          <li>El sitio se actualiza cada tres meses. Corte actual: ${fecha(M.corte)}. Próxima revisión: ${fecha(M.proxima)}.</li>
        </ul>
      </div></div>`;
  };

  // ---------- rutas ----------
  const NAV = { inicio: "", "quien-manda": "quien", organizaciones: "organizaciones", paises: "paises", marco: "marco" };
  function route() {
    const h = decodeURIComponent(location.hash.slice(1));
    tip.style.display = "none";
    let navKey = "inicio";
    if (h.startsWith("o-")) { V.org(h.slice(2)); navKey = "organizaciones"; }
    else if (h === "quien-manda") { V.quien(); navKey = h; }
    else if (h === "organizaciones" || h === "organizaciones-oculto") { V.organizaciones(h.endsWith("oculto") ? "oculto" : "pt"); navKey = "organizaciones"; }
    else if (h === "paises") { V.paises(); navKey = h; }
    else if (h === "marco") { V.marco(); navKey = h; }
    else V.inicio();
    document.querySelectorAll(".mainnav a").forEach(a => a.classList.toggle("on", a.dataset.k === navKey));
    const titles = { inicio: "", "quien-manda": "Quién manda", organizaciones: "Organizaciones", paises: "Países", marco: "Marco" };
    const t = h.startsWith("o-") && byId[h.slice(2)] ? corto(byId[h.slice(2)].n) : titles[navKey];
    document.title = (t ? t + " · " : "") + "El mapa del poder global";
    window.scrollTo({ top: 0, left: 0, behavior: "instant" });
  }
  if ("scrollRestoration" in history) history.scrollRestoration = "manual";
  document.getElementById("stamp").innerHTML = `Corte <b>${fecha(M.corte)}</b><br>Próxima revisión ${fecha(M.proxima)}`;
  document.getElementById("foot-date").textContent = `Corte del ${fecha(M.corte)} · próxima revisión el ${fecha(M.proxima)}`;
  window.addEventListener("hashchange", route);
  route();
})();
