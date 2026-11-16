#!/usr/bin/env node
// Controla los datos del sitio: ids, dependencias, relaciones, puntajes y vencimiento del corte.
// Uso: node scripts/validate.js
const fs = require("fs"), path = require("path");
global.window = {};
const raiz = path.join(__dirname, "..");
["meta", "organizaciones", "relaciones", "paises"].forEach(f => require(path.join(raiz, "data", f + ".js")));
const { META, ORGS, RELACIONES, PAISES } = window;
const err = [], ids = new Set();
for (const o of ORGS) {
  if (ids.has(o.id)) err.push(`id repetido: ${o.id}`); ids.add(o.id);
  if (o.sc.length !== META.ejes.length || o.sc.some(v => ![0, 1, 2, 3].includes(v))) err.push(`puntajes inválidos: ${o.id}`);
  if (![1, 2, 3, 4].includes(o.aut)) err.push(`autonomía inválida: ${o.id}`);
  if (![0, 1, 2, 3].includes(o.formal)) err.push(`poder formal inválido: ${o.id}`);
  if (!META.bloques[o.bloque]) err.push(`bloque desconocido: ${o.id}`);
  if (o.sample) err.push(`dato de prueba publicado: ${o.id}`);
}
for (const o of ORGS) for (const d of o.dep) if (!ids.has(d)) err.push(`dependencia inexistente: ${o.id} → ${d}`);
for (const r of RELACIONES) {
  if (!ids.has(r.a) || !ids.has(r.b)) err.push(`relación con id inexistente: ${r.a} → ${r.b}`);
  if (![1, 2, 3].includes(r.i)) err.push(`intensidad inválida: ${r.a} → ${r.b}`);
  if (!r.x) err.push(`relación sin explicación: ${r.a} → ${r.b}`);
}
for (const [k, p] of Object.entries(PAISES)) if (!META.bloques[p.b] || !META.posiciones[p.p]) err.push(`país mal clasificado: ${k}`);
const dias = (Date.now() - Date.parse(META.corte)) / 864e5;
const avisos = dias > 92 ? [`el corte tiene ${Math.round(dias)} días: toca la revisión trimestral`] : [];
avisos.forEach(a => console.log("Aviso: " + a));
if (err.length) { console.error(err.join("\n")); process.exit(1); }
console.log(`OK: ${ORGS.length} organizaciones, ${RELACIONES.length} relaciones, ${Object.keys(PAISES).length} países y territorios.`);
