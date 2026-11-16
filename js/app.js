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
  const pct = v => Math.round(v * 100) + " %";
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
  ORGS.forEach(o => { o.pais = null; if (!o.ll) return; const hit = FEAT.find(F => d3.geoContains(F, o.ll)); o.pais = hit ? hit.properties.name : null; });
  const POSOP = { C: 1, A: .9, G: .7, R: .7, U: 1, P: .45, IT: .32, IE: .38, S: 0 };
  const ZONA = { T: "#E10600", X: "#A3150C", P: "#5E1410" };
  function fillFor(name, layer) {
    const p = PA[name]; if (!p) return "#101010";
    if (layer === "zonas") return p.z ? ZONA[p.z] : "#161616";
    if (layer === "organizaciones") return p.b === "D" ? "#121212" : bcol(p.b) + "40";
    if (layer === "posicion") {
      if (p.p === "R") return `url(#hatch-${p.b})`;
      if (p.b === "D") { const c = p.p === "IT" ? BL.T.c : p.p === "IE" ? BL.E.c : p.p === "P" ? BL.P.c : null; if (!c) return "#161616"; return c + Math.round(POSOP[p.p] * 255).toString(16).padStart(2, "0"); }
      return bcol(p.b) + Math.round((POSOP[p.p] || 1) * 255).toString(16).padStart(2, "0");
    }
    return p.b === "D" ? "#161616" : bcol(p.b);
  }
  function mapSVG(layer, sel) {
    const defs = `<defs>${["T", "E", "I", "D"].map(b => `<pattern id="hatch-${b}" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="6" height="6" fill="#141414"/><rect width="3" height="6" fill="${b === "D" ? "#5A5150" : bcol(b)}"/></pattern>`).join("")}</defs>`;
    const cs = CPATH.map(c => `<path class="m-c${sel && sel.k === "c" && sel.v === c.name ? " sel" : ""}" data-c="${esc(c.name)}" d="${c.d}" fill="${fillFor(c.name, layer)}"/>`).join("");
    let extra = "";
    if (layer === "bloques" || layer === "posicion") extra = `<g class="m-fr">${M.friccion.map(f => { const [x, y] = proj(f.ll); return `<g data-fr="${f.n}"><circle cx="${x}" cy="${y}" r="9"/><text x="${x}" y="${y}">${f.n}</text></g>`; }).join("")}</g>`;
    if (layer === "organizaciones") extra = ORGS.filter(o => o.ll).slice().sort((a, b) => b.pe - a.pe).map(o => { const [x, y] = proj(o.ll); const r = 2 + Math.sqrt(o.pe) * .9; return shape(o.tipo, x, y, r, bcol(o.bloque), `class="m-o${sel && sel.k === "o" && sel.v === o.id ? " sel" : ""}" data-o="${o.id}" tabindex="0" role="button" aria-label="${esc(o.n)}"`); }).join("");
    return `<svg viewBox="0 0 ${MW} ${MH}" role="img" aria-label="Mapa mundial: ${esc(LAYERS[layer])}">${defs}<path class="m-sphere" d="${SPHERE}"/><path class="m-grat" d="${GRAT}"/>${cs}${extra}</svg>`;
  }
  const LAYERS = { bloques: "Bloques", posicion: "Posición", zonas: "Zonas liberadas", organizaciones: "Organizaciones" };
  function legendFor(layer) {
    const sq = (c, t, extra = "") => `<div><span class="sq" style="background:${c};${extra}"></span>${t}</div>`;
    if (layer === "zonas") return sq(ZONA.T, "Total") + sq(ZONA.X, "Extendida") + sq(ZONA.P, "Parcial") + sq("#161616", "Sin zona liberada", "border:1px solid #2A1414");
    if (layer === "organizaciones") return M.tipos.map(t => `<div><svg width="16" height="16" aria-hidden="true">${shape(t, 8, 8, 6.4, "#EDE6E3")}</svg>${t}</div>`).join("") + `<p class="note">Color: bloque de la organización. Tamaño: poder efectivo.</p>`;
    const base = sq(BL.T.c, "Imperio transoceánico") + sq(BL.E.c, "Alianza euroasiática") + sq(BL.I.c, "Independientes") + sq("#161616", "Terreno disputado", "border:1px solid #2A1414");
    if (layer === "posicion") return base + sq("repeating-linear-gradient(45deg,#2F6BFF 0 3px,#141414 3px 6px)", "Protectorado") + `<p class="note">Intensidad: centro y aliados, plenos; integrados, medios. En el terreno disputado, el tinte indica hacia qué bloque se inclina.</p>`;
    return base + `<div><span class="sq" style="border:1.6px solid #FF3B30;border-radius:50%"></span>Punto de fricción</div>`;
  }
  function countryPanel(name) {
    const p = PA[name]; if (!p) return "";
    const orgs = ORGS.filter(o => o.pais === name);
    return `<div class="lbl">${esc(BL[p.b].n)}</div><h3>${esc(p.n)}</h3>
      <p class="side-x"><b>Posición:</b> ${esc(M.posiciones[p.p])}${p.z ? `<br><b>Zona liberada:</b> ${esc(M.grados[p.z])} · ${esc(p.asp.map(a => M.aspectos[a]).join(", "))}` : ""}</p>
      ${p.x ? `<p class="side-x">${esc(p.x)}</p>` : ""}
      ${orgs.length ? `<div class="lbl" style="margin-top:6px">Organizaciones con sede aquí (${orgs.length})</div><div>${orgs.map(o => `<a class="rk" style="grid-template-columns:18px minmax(0,1fr) 46px" href="#o-${o.id}">${icon(o)}<span class="nm">${esc(corto(o.n))}</span><span class="v">${num(o.red)}</span></a>`).join("")}</div>` : ""}`;
  }
  function orgPanel(o) {
    return `<div class="lbl">${esc(o.area)} · ${esc(BL[o.bloque].n)}</div><h3>${esc(o.n)}</h3>
      <div class="nums"><div><small>Efectivo</small><b>${num(o.pe)}</b></div><div><small>En red</small><b>${num(o.red)}</b></div><div class="o"><small>Oculto</small><b>${num(o.oculto)}</b></div></div>
      <p class="side-x"><b>Sede:</b> ${esc(o.sede)}<br><b>Autonomía:</b> ${o.aut} · ${esc(M.autonomia[o.aut])}</p>
      <a class="btn" href="#o-${o.id}">Abrir la ficha</a>`;
  }
  function frPanel(n) { const f = M.friccion.find(x => x.n === +n); return `<div class="lbl">Punto de fricción ${f.n}</div><h3>${esc(f.x)}</h3><p class="side-x">Uno de los seis frentes donde chocan los bloques, según el marco del sitio.</p>`; }
  function mountMap(el, opts = {}) {
    let layer = opts.layer || "bloques", sel = null;
    const layers = opts.layers || Object.keys(LAYERS);
    el.innerHTML = `<div class="panel"><div class="panel-bar"><div class="chips" role="group" aria-label="Capas del mapa">${layers.map(k => `<button type="button" class="chip" data-l="${k}">${LAYERS[k]}</button>`).join("")}</div><span class="note" style="margin:0">Tocá un país o una organización</span></div>
      <div class="split"><div class="stage map"></div><aside></aside></div></div>`;
    const stage = el.querySelector(".stage"), side = el.querySelector("aside");
    const draw = () => {
      el.querySelectorAll("[data-l]").forEach(b => { b.classList.toggle("on", b.dataset.l === layer); b.setAttribute("aria-pressed", b.dataset.l === layer); });
      stage.innerHTML = mapSVG(layer, sel);
      side.innerHTML = !sel ? `<div class="lbl">Cómo leerlo</div><div class="legend">${legendFor(layer)}</div>`
        : sel.k === "c" ? countryPanel(sel.v) : sel.k === "o" ? orgPanel(byId[sel.v]) : frPanel(sel.v);
      if (sel) side.insertAdjacentHTML("beforeend", `<button type="button" class="chip" data-clear style="align-self:flex-start">Volver a la leyenda</button>`);
      const clear = side.querySelector("[data-clear]"); if (clear) clear.onclick = () => { sel = null; draw(); };
      stage.querySelectorAll(".m-c").forEach(p => p.addEventListener("click", () => { sel = { k: "c", v: p.dataset.c }; draw(); }));
      activate(stage, ".m-o", g => { sel = { k: "o", v: g.dataset.o }; draw(); });
      stage.querySelectorAll("[data-fr]").forEach(g => g.addEventListener("click", () => { sel = { k: "f", v: g.dataset.fr }; draw(); }));
      bindTip(stage, ".m-c", p => { const c = PA[p.dataset.c]; return c ? `<b>${esc(c.n)}</b><span>${esc(BL[c.b].n)} · ${esc(M.posiciones[c.p])}${c.z ? " · zona liberada " + esc(M.grados[c.z]).toLowerCase() : ""}</span>` : esc(p.dataset.c); });
      bindTip(stage, ".m-o", g => { const o = byId[g.dataset.o]; return `<b>${esc(o.n)}</b><span>${esc(o.area)} · poder en red ${num(o.red)}</span>`; });
    };
    el.querySelectorAll("[data-l]").forEach(b => b.addEventListener("click", () => { layer = b.dataset.l; if (sel && sel.k === "o" && layer !== "organizaciones") sel = null; draw(); }));
    draw();
  }

  // ---------- listas ----------
  const METRIC = { red: "Poder en red", pe: "Poder efectivo", oculto: "Poder oculto", cap: "Capacidad" };
  function rankRows(list, key, max, color) {
    return list.map((o, i) => `<a class="rk" href="#o-${o.id}"><span class="n">${String(i + 1).padStart(2, "0")}</span>${icon(o)}<span class="nm">${esc(corto(o.n))}<small>${esc(o.area)}${FI[o.id] ? "" : " · ficha en preparación"}</small></span><span class="bar"><i style="width:${Math.max(2, o[key] / max * 100)}%;background:${color || bcol(o.bloque)}"></i></span><span class="v">${num(o[key], key === "cap" ? 0 : 1)}</span></a>`).join("");
  }
  const sortBy = k => ORGS.slice().sort((a, b) => b[k] - a[k] || b.red - a.red);

  // ---------- vistas ----------
  const V = {};
  V.inicio = () => {
    const red = sortBy("red").slice(0, 10), oc = sortBy("oculto").slice(0, 10);
    app.innerHTML = `<div class="wrap">
      <div class="hero"><div style="display:flex;flex-direction:column;gap:18px"><div class="kick">El mundo real, sin máscaras</div><h1>El mapa del<br>poder global</h1></div>
      <p class="read">Quién tiene el poder real en el mundo y quién solo lo aparenta. ${ORGS.length} organizaciones medidas en ${M.ejes.length} ejes, su jerarquía y cuánto de su poder escapa al control público.</p></div>
      <section class="block" id="mapa-inicio"></section>
      <section class="block two">
        <div><div class="sec-title"><h2>Poder en red</h2><a href="#organizaciones">Ver los ${ORGS.length}</a></div>${rankRows(red, "red", red[0].red)}</div>
        <div><div class="sec-title"><h2>Poder oculto</h2><a href="#organizaciones-oculto">Ver el índice</a></div>${rankRows(oc, "oculto", oc[0].oculto, "#E10600")}</div>
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
      <p class="read">El orden mundial como bloques con centros, aliados, protectorados con fachada de independencia y zonas que ningún Estado controla del todo.</p></div>
      <section class="block" id="mapa-paises"></section>
      <section class="block"><div class="sec-title"><h2>Clasificación</h2><span class="note" style="margin:0">${rows.length} países y territorios</span></div>
      <div class="filters"><label>Bloque<select id="fB"><option value="">Todos</option>${Object.entries(BL).map(([k, b]) => `<option value="${k}">${esc(b.n)}</option>`).join("")}</select></label>
      <label>Zona liberada<select id="fZ"><option value="">Todas</option><option value="si">Con zona liberada</option></select></label></div>
      <div class="tbl-wrap"><table><thead><tr><th>País</th><th>Bloque</th><th>Posición</th><th>Zona liberada</th><th>Nota</th></tr></thead><tbody id="tb"></tbody></table></div></section></div>`;
    mountMap(document.getElementById("mapa-paises"), { layer: "posicion" });
    const tb = document.getElementById("tb"), fB = document.getElementById("fB"), fZ = document.getElementById("fZ");
    const fill = () => { tb.innerHTML = rows.filter(([, p]) => (!fB.value || p.b === fB.value) && (!fZ.value || p.z)).map(([, p]) => `<tr><td>${esc(p.n)}</td><td><span class="sq" style="background:${p.b === "D" ? "#161616" : bcol(p.b)};border:1px solid #2A1414;vertical-align:-2px"></span> ${esc(BL[p.b].n)}</td><td>${esc(M.posiciones[p.p])}</td><td>${p.z ? esc(M.grados[p.z]) + " · " + esc(p.asp.map(a => M.aspectos[a]).join(", ")) : "—"}</td><td class="muted">${esc(p.x)}</td></tr>`).join(""); };
    fB.onchange = fZ.onchange = fill; fill();
  };

  V.organizaciones = (arg) => {
    const areas = [...new Set(ORGS.map(o => o.area))].sort((a, b) => a.localeCompare(b, "es"));
    app.innerHTML = `<div class="wrap"><div class="page-head"><div style="display:flex;flex-direction:column;gap:12px"><div class="kick">Fichas</div><h1>Organizaciones</h1></div>
      <p class="read">${ORGS.length} organizaciones con nombre propio. Tocá una para abrir su ficha.</p></div>
      <div class="filters">
        <label>Ordenar por<select id="fM">${Object.entries(METRIC).map(([k, n]) => `<option value="${k}"${k === (arg || "red") ? " selected" : ""}>${n}</option>`).join("")}</select></label>
        <label>Tipo<select id="fT"><option value="">Todos</option>${M.tipos.map(t => `<option>${t}</option>`).join("")}</select></label>
        <label>Área<select id="fA"><option value="">Todas</option>${areas.map(a => `<option>${esc(a)}</option>`).join("")}</select></label>
        <label>Bloque<select id="fB"><option value="">Todos</option>${["T", "E", "I", "P", "X"].map(k => `<option value="${k}">${esc(BL[k].n)}</option>`).join("")}</select></label>
      </div><div id="lst" style="padding-bottom:56px"></div></div>`;
    const g = id => document.getElementById(id);
    const fill = () => {
      const k = g("fM").value;
      const l = sortBy(k).filter(o => (!g("fT").value || o.tipo === g("fT").value) && (!g("fA").value || o.area === g("fA").value) && (!g("fB").value || o.bloque === g("fB").value));
      const max = sortBy(k)[0][k];
      g("lst").innerHTML = l.length ? rankRows(l, k, max, k === "oculto" ? "#E10600" : null) : `<p class="note">Ninguna organización con esos filtros.</p>`;
    };
    ["fM", "fT", "fA", "fB"].forEach(id => g(id).onchange = fill); fill();
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
    const rank = sortBy("red").indexOf(o) + 1;
    const ejeIdx = Object.fromEntries(M.ejes.map((e, i) => [e.k, i]));
    const perfil = M.familias.map(F => `<div class="fam">${esc(F.n)}</div>` + F.ejes.map(k => { const e = M.ejes[ejeIdx[k]], v = o.sc[ejeIdx[k]]; return `<div class="eje"><span>${esc(e.n)}</span><span class="segs" role="img" aria-label="${v} de 3">${[0, 1, 2].map(i => `<i class="${i < v ? "on" : ""}"></i>`).join("")}</span><span class="an">${v ? esc(e.a[3 - v]) : "Sin capacidad relevante"}</span></div>`; }).join("")).join("");
    const relHtml = rels.length ? rels.sort((a, b) => b.i - a.i).map(r => { const other = byId[r.a === id ? r.b : r.a]; return `<div class="rel">${lineIcon(r.t)}<div><a href="#o-${other.id}">${esc(corto(other.n))}</a> · ${esc(r.t.toLowerCase())}${r.i === 3 ? " fuerte" : r.i === 1 ? " débil" : ""}<small>${esc(r.x)}</small></div></div>`; }).join("") : `<p class="side-x">Sin relaciones cargadas todavía.</p>`;
    app.innerHTML = `<div class="wrap">
      <div class="org-head"><div class="crumb"><a href="#organizaciones">Organizaciones</a> / ${esc(o.area)}</div>
        <div style="display:flex;flex-wrap:wrap;align-items:center;gap:18px">${icon(o, 44)}<h1>${esc(o.n)}</h1></div>
        <div class="pills"><span style="border-color:${bcol(o.bloque)}">${esc(BL[o.bloque].n)}</span><span>Autonomía ${o.aut} · ${esc(M.autonomia[o.aut])}</span><span>Fase: ${esc(M.fases[o.fase]).toLowerCase()}</span><span>Certeza: ${esc(M.certeza[o.cert]).toLowerCase()}</span><span>${esc(o.tipo)}</span><span>Sede: ${esc(o.sede)}</span><span style="border-color:transparent;color:#9A8F8C">Puesto ${rank} de ${ORGS.length}</span></div></div>
      <div class="nums" style="margin-top:22px"><div><small>Capacidad</small><b>${o.cap}<span class="muted" style="font-size:15px"> /51</span></b></div><div><small>Poder efectivo</small><b>${num(o.pe)}</b></div><div><small>Poder en red</small><b>${num(o.red)}</b></div><div><small>Brecha</small><b>${pct(o.brecha)}</b></div><div class="o"><small>Poder oculto</small><b>${num(o.oculto)}</b></div></div>
      <div class="org-body"><div class="org-main">
        <div><h2>Poder formal y poder real</h2>
          <div class="note" style="display:flex;justify-content:space-between;margin:0"><span>Reconocido y sujeto a control</span><span style="color:#FF3B30">Fuera de control público</span></div>
          <div class="gapbar" role="img" aria-label="Brecha de ${pct(o.brecha)}"><i style="width:${(1 - o.brecha) * 100}%"></i><i style="width:${o.brecha * 100}%"></i></div>
          <p class="read" style="font-size:17px">Poder formal ${o.formal} de 3: ${pct(1 - o.brecha)} de su poder está reconocido públicamente y sujeto a control; el resto escapa a ese control.</p></div>
        
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
    let mode = "pe", cur = null, showRel = true;
    app.innerHTML = `<div class="wrap"><div class="page-head"><div style="display:flex;flex-direction:column;gap:12px"><div class="kick">Esquema</div><h1>Quién manda</h1></div>
      <p class="read">La fila indica la autonomía; el tamaño, el poder; el color, el bloque; la forma, el tipo de organización. Las líneas grises marcan de quién depende cada una.</p></div>
      <div class="chips" style="margin-bottom:14px"><button type="button" class="chip" data-m="pe">Poder efectivo</button><button type="button" class="chip" data-m="oculto">Poder oculto</button><span class="chip-sep" aria-hidden="true"></span><button type="button" class="chip" data-r>Relaciones</button></div>
      <section class="block"><div class="panel"><div class="split"><div class="stage"><div class="qm-scroll"><svg id="qm" role="img" aria-label="Gráfico de jerarquía entre organizaciones"></svg></div><p class="note" style="padding:0 14px 12px">En el teléfono el gráfico se desliza de costado.</p></div><aside id="qside"></aside></div></div></section></div>`;
    const VW = 1200, top = 24, PER = 30, SUBH = 62;
    const rows = [1, 2, 3, 4].map(a => ORGS.filter(o => o.aut === a));
    const yBase = {}; let acc = top;
    [1, 2, 3, 4].forEach(a => { const n = rows[a - 1].length; yBase[a] = acc; acc += n ? 40 + Math.ceil(n / PER) * SUBH : 44; });
    const VH = acc + 10;
    const pos = {};
    rows.forEach((list, ri) => {
      const a = ri + 1; if (!list.length) return;
      const sorted = list.slice().sort((x, y) => BORDER.indexOf(x.bloque) - BORDER.indexOf(y.bloque) || y.pe - x.pe);
      const nsub = Math.ceil(sorted.length / PER), per = Math.ceil(sorted.length / nsub);
      sorted.forEach((o, i) => { const s = Math.floor(i / per), k = i % per, cnt = Math.min(per, sorted.length - s * per);
        const x = 60 + (cnt === 1 ? (VW - 120) / 2 : k * (VW - 120) / (cnt - 1));
        const y = yBase[a] + 40 + s * SUBH + SUBH / 2 - 6 + ((k % 2) ? 7 : -7);
        pos[o.id] = [x, y]; });
    });
    const svg = document.getElementById("qm"), side = document.getElementById("qside");
    svg.setAttribute("viewBox", `0 0 ${VW} ${VH}`);
    const rad = o => 3 + Math.sqrt(Math.max(o[mode], 0)) * (mode === "pe" ? 1.9 : 2.2);
    const near = id => !cur || id === cur || byId[cur].dep.includes(id) || byId[id].dep.includes(cur) || REL.some(r => (r.a === cur && r.b === id) || (r.b === cur && r.a === id));
    const draw = () => {
      app.querySelectorAll("[data-m]").forEach(b => { b.classList.toggle("on", b.dataset.m === mode); b.setAttribute("aria-pressed", b.dataset.m === mode); });
      const rb = app.querySelector("[data-r]"); rb.classList.toggle("on", showRel); rb.setAttribute("aria-pressed", showRel);
      const lv = [1, 2, 3, 4].map(a => `<g class="qm-row">${a > 1 ? `<line x1="16" x2="${VW - 16}" y1="${yBase[a] - 4}" y2="${yBase[a] - 4}"/>` : ""}<text class="qm-lv" x="16" y="${yBase[a] + 14}">${a} · ${esc(M.autonomia[a]).toUpperCase()} (${rows[a - 1].length})</text></g>`).join("");
      const deps = ORGS.flatMap(o => o.dep.filter(d => pos[d]).map(d => { const [x1, y1] = pos[o.id], [x2, y2] = pos[d], on = !cur || cur === o.id || cur === d;
        return `<path class="qm-dep" d="M${x1},${y1} C${x1},${(y1 + y2) / 2} ${x2},${(y1 + y2) / 2} ${x2},${y2}" opacity="${on ? (cur ? .9 : .35) : .05}"/>`; })).join("");
      const rels = showRel ? REL.filter(r => cur ? (r.a === cur || r.b === cur) : r.i === 3).map(r => { const [x1, y1] = pos[r.a], [x2, y2] = pos[r.b], mx = (x1 + x2) / 2, my = Math.min(y1, y2) - 30 - Math.abs(x1 - x2) * .1;
        const st = r.t === "Enfrentamiento" ? 'stroke="#FF3B30" stroke-dasharray="6 4"' : (r.t === "Ambigua" ? 'stroke="#F2A93B" stroke-dasharray="4 3"' : (r.t === "Puerta giratoria" || r.t === "Acceso a datos") ? 'stroke="#9A8F8C" stroke-dasharray="2 4"' : 'stroke="#EDE6E3"');
        return `<path class="qm-rel" d="M${x1},${y1} Q${mx},${my} ${x2},${y2}" ${st} opacity="${cur ? .9 : .4}"/>`; }).join("") : "";
      const ordered = ORGS.slice().sort((a, b) => rad(b) - rad(a));
      const nodes = ordered.map(o => { const [x, y] = pos[o.id], r = rad(o), dim = !near(o.id), lab = cur ? near(o.id) : r > 13.5;
        return `<g class="qm-n" data-id="${o.id}" tabindex="0" role="button" aria-label="${esc(o.n)}" opacity="${dim ? .15 : 1}">${shape(o.tipo, x, y, r, bcol(o.bloque), `fill-opacity="${o.tipo === "Sombra" ? 1 : .9}"`)}${cur === o.id ? `<circle cx="${x}" cy="${y}" r="${r + 6}" fill="none" stroke="#FF3B30" stroke-width="2"/>` : ""}${lab ? `<text x="${x}" y="${y + r + 13}">${esc(corto(o.n).slice(0, 26))}</text>` : ""}</g>`; }).join("");
      svg.innerHTML = lv + deps + rels + nodes;
      side.innerHTML = cur ? orgPanel(byId[cur]) + `<div class="box" style="padding:12px"><span class="lbl">Por familia</span>${radar(byId[cur])}</div>` + `<div class="side-x"><b>Depende de:</b> ${byId[cur].dep.map(d => esc(corto(byId[d].n))).join(", ") || "nadie en el mapa"}<br><b>Dependen de ella:</b> ${dependents(cur).map(d => esc(corto(d.n))).join(", ") || "ninguna"}</div><button type="button" class="chip" data-clear style="align-self:flex-start">Ver todo</button>`
        : `<div class="lbl">Cómo leerlo</div>${[1, 2, 3, 4].map(a => `<p class="side-x"><b>${a} · ${esc(M.autonomia[a])}.</b> ${["Sin superior en lo estratégico.", "Decide su estrategia dentro de un bloque o jurisdicción que puede limitarla.", "Ejecuta lo que decide otro.", "Aparenta una independencia que no tiene."][a - 1]}</p>`).join("")}
          <div class="legend">${["T", "E", "I", "P", "X"].map(k => `<div><span class="sq" style="background:${BL[k].c}"></span>${esc(BL[k].n)}</div>`).join("")}</div>
          <div class="legend">${M.tipos.map(t => `<div><svg width="16" height="16" aria-hidden="true">${shape(t, 8, 8, 6.4, "#EDE6E3")}</svg>${t}</div>`).join("")}</div>
          <p class="note">Sin selección se muestran solo las relaciones fuertes. Tocá un punto para ver todas las suyas.</p>`;
      const clr = side.querySelector("[data-clear]"); if (clr) clr.onclick = () => { cur = null; draw(); };
      activate(svg, ".qm-n", g => { cur = cur === g.dataset.id ? null : g.dataset.id; draw(); });
      bindTip(svg, ".qm-n", g => { const o = byId[g.dataset.id]; return `<b>${esc(o.n)}</b><span>${esc(o.area)} · ${esc(BL[o.bloque].n)}</span><span>Efectivo ${num(o.pe)} · en red ${num(o.red)} · oculto ${num(o.oculto)}</span>`; });
    };
    app.querySelectorAll("[data-m]").forEach(b => b.onclick = () => { mode = b.dataset.m; draw(); });
    app.querySelector("[data-r]").onclick = () => { showRel = !showRel; draw(); };
    draw();
  };

  V.marco = () => {
    app.innerHTML = `<div class="wrap"><div class="page-head"><div style="display:flex;flex-direction:column;gap:12px"><div class="kick">Método</div><h1>Marco</h1></div></div>
      <div class="prose" style="padding-bottom:40px">
        <p>El sitio responde una sola pregunta: quién tiene el poder real en el mundo y quién solo lo aparenta. La unidad de análisis es la organización con nombre propio, no el país.</p>
        <h2>Teoría</h2>
        <ul>
          <li><b>Fachada y poder operativo.</b> Toda organización tiene un poder formal, el que le dan la ley y su mandato, y un poder real. El sitio mide el real y la distancia entre ambos.</li>
          <li><b>La clase gerencial</b> (James Burnham). Manda quien controla la información, el personal y la maquinaria, aunque no sea dueño ni haya sido electo.</li>
          <li><b>El costo de reprimir</b> (Robert Dahl). Cuando una parte del Estado puede reprimir a bajo costo visible, la democracia conserva la forma y pierde el fondo.</li>
          <li><b>El ciclo de las instituciones</b> (Carroll Quigley). Los instrumentos de expansión se convierten en instituciones que se defienden a sí mismas: expansión, captura, distorsión.</li>
          <li><b>Realismo ofensivo</b> (John Mearsheimer). Un orden multipolar con un imperio transoceánico, una alianza euroasiática, potencias independientes y un terreno disputado.</li>
        </ul>
        <h2>Cómo se mide</h2>
        <p>Cada organización recibe de 0 a 3 en ${M.ejes.length} ejes agrupados en seis familias. El 3 se reserva a quienes están entre los pocos primeros del mundo en ese eje. Los pesos son fijos e iguales.</p>
      </div>
      <div class="tbl-wrap"><table><thead><tr><th>Familia</th><th>Eje</th><th>3 · Dominante</th><th>2 · Alto</th><th>1 · Relevante</th></tr></thead><tbody>${M.ejes.map(e => `<tr><td class="muted">${esc(e.fam)}</td><td><b>${esc(e.n)}</b><br><span class="muted">${esc(e.x)}</span></td>${e.a.map(a => `<td>${esc(a)}</td>`).join("")}</tr>`).join("")}</tbody></table></div>
      <div class="prose" style="padding:40px 0 64px">
        <h2>Fórmulas</h2>
        <ul>
          <li><b>Capacidad:</b> suma de los ${M.ejes.length} ejes, de 0 a 51.</li>
          <li><b>Poder efectivo:</b> capacidad por el factor de autonomía (1 decide solo: 1; 2 aliado con criterio propio: 0,75; 3 subordinado: 0,5; 4 fachada: 0,25).</li>
          <li><b>Poder en red:</b> poder efectivo más la mitad del poder en red de quienes dependen de ella, en cadena.</li>
          <li><b>Poder formal:</b> de 0 a 3, cuánto de su poder está reconocido públicamente y sujeto a control: ley, elecciones, tribunales, auditoría, transparencia.</li>
          <li><b>Brecha:</b> la parte de su poder que escapa a ese control. <b>Poder oculto:</b> poder efectivo por brecha.</li>
        </ul>
        <h2>Resguardos</h2>
        <ul>
          <li>Cada organización lleva un nivel de certeza: documentado, estimado o especulativo.</li>
          <li>Toda afirmación que califique a una organización de fachada o protectorado, o la vincule con delitos o con grupos armados, lleva fuente.</li>
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
    else if (h === "organizaciones" || h === "organizaciones-oculto") { V.organizaciones(h.endsWith("oculto") ? "oculto" : "red"); navKey = "organizaciones"; }
    else if (h === "paises") { V.paises(); navKey = h; }
    else if (h === "marco") { V.marco(); navKey = h; }
    else V.inicio();
    document.querySelectorAll(".mainnav a").forEach(a => a.classList.toggle("on", a.dataset.k === navKey));
    const titles = { inicio: "", "quien-manda": "Quién manda", organizaciones: "Organizaciones", paises: "Países", marco: "Marco" };
    const t = h.startsWith("o-") && byId[h.slice(2)] ? corto(byId[h.slice(2)].n) : titles[navKey];
    document.title = (t ? t + " · " : "") + "El mapa del poder global";
    window.scrollTo(0, 0);
  }
  document.getElementById("stamp").innerHTML = `Corte <b>${fecha(M.corte)}</b><br>Próxima revisión ${fecha(M.proxima)}`;
  document.getElementById("foot-date").textContent = `Corte del ${fecha(M.corte)} · próxima revisión el ${fecha(M.proxima)}`;
  window.addEventListener("hashchange", route);
  route();
})();
