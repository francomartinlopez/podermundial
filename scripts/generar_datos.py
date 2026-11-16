#!/usr/bin/env python3
"""Genera data/*.js a partir de fuente/ (datos.py, paises.py, coords.py).
La hoja de puntuación es la fuente editorial; fuente/ es su copia en el repositorio.
Uso: python3 scripts/generar_datos.py"""
import json, os, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "fuente"))
from datos import ORGS, EJES, ORDEN_ENTRADA, AREA_TIPO, BLOQUES, AUTONOMIA, CERTEZA, RELACIONES, FORMAL, FASE, FASES, ANCLAS
from paises import PAISES, BLOQ, POS, GRADO, ASP
from coords import C

CORTE = "2026-11-16"
PROXIMA = "2027-02-16"
TERRITORIOS_D = {"Siachen Glacier"}  # el resto de los territorios dependientes hereda el bloque transoceánico

def js(nombre, valor, comentario):
    return f"// {comentario}\n// Generado por scripts/generar_datos.py: no editar a mano.\nwindow.{nombre} = " + json.dumps(valor, ensure_ascii=False, separators=(",", ":")) + ";\n"

fac = {1: 1, 2: .75, 3: .5, 4: .25}
ids = {o[0] for o in ORGS}
masters = {o[0]: [d for d in o[8].split(",") if d] for o in ORGS}
pe = {o[0]: sum(map(int, o[6])) * fac[o[5]] for o in ORGS}
memo = {}
def red(i, pila=()):
    if i in memo: return memo[i]
    if i in pila: raise SystemExit(f"Ciclo de dependencias en {i}")
    v = pe[i] + 0.5 * sum(red(j, pila + (i,)) / len(masters[j]) for j in ids if i in masters[j])
    memo[i] = v; return v

ejes = [e[0] for e in EJES]
orgs = []
for o in ORGS:
    sc = dict(zip(ORDEN_ENTRADA, map(int, o[6])))
    cap = sum(sc.values()); f = FORMAL[o[0]]
    orgs.append({"id": o[0], "n": o[1], "area": o[2], "tipo": AREA_TIPO[o[2]], "bloque": o[4], "aut": o[5],
                 "sc": [sc[k] for k in ejes], "cap": cap, "pe": round(pe[o[0]], 2), "red": round(red(o[0]), 2),
                 "formal": f, "brecha": round((3 - f) / 3, 4), "oculto": round(pe[o[0]] * (3 - f) / 3, 2),
                 "fase": FASE[o[0]], "cert": o[7], "sede": o[3], "ll": C[o[3]], "dep": masters[o[0]]})
orgs.sort(key=lambda x: (-x["red"], -x["pe"], x["n"]))

fam = []
for e in EJES:
    if not fam or fam[-1]["n"] != e[2]: fam.append({"n": e[2], "ejes": []})
    fam[-1]["ejes"].append(e[0])
meta = {"corte": CORTE, "proxima": PROXIMA, "skeleton": False,
        "ejes": [{"k": e[0], "n": e[1], "fam": e[2], "x": e[3], "a": list(ANCLAS[e[0]])} for e in EJES], "familias": fam,
        "bloques": {"T": {"n": "Transoceánico", "c": "#2F6BFF"}, "E": {"n": "Euroasiático", "c": "#9E1B32"},
                    "I": {"n": "Independiente", "c": "#BDBDBD"}, "P": {"n": "Pendular", "c": "#F2A93B"},
                    "X": {"n": "Transnacional", "c": "#F5F0E6"}, "D": {"n": "Terreno disputado", "c": "#141414"}},
        "autonomia": {str(k): v for k, v in AUTONOMIA.items()}, "certeza": CERTEZA, "fases": FASES,
        "tipos": ["Estado", "Capital", "Información", "Supranacional", "Influencia", "Sombra"],
        "posiciones": POS, "grados": GRADO, "aspectos": ASP,
        "friccion": [{"n": 1, "x": "Mar de China Oriental y estrecho de Taiwán", "ll": [123.5, 26.0]},
                     {"n": 2, "x": "Accesos del Pacífico suroccidental", "ll": [158.0, -12.0]},
                     {"n": 3, "x": "Frontera sur de Norteamérica", "ll": [-104.0, 29.5]},
                     {"n": 4, "x": "Litoral mediterráneo", "ll": [15.0, 35.5]},
                     {"n": 5, "x": "Mar Negro y Ucrania", "ll": [34.0, 46.0]},
                     {"n": 6, "x": "Levante y golfo Pérsico", "ll": [44.0, 30.0]}]}
rel = [{"a": a, "b": b, "t": t, "x": x, "i": i} for a, b, t, x, i in RELACIONES]
paises = {m: {"n": es, "b": b, "p": p, "z": z, "asp": a, "x": n} for m, es, b, p, z, a, n in PAISES}
nombres = json.load(open(os.path.join(RAIZ, "data", "nombres_mapa.json"))) if os.path.exists(os.path.join(RAIZ, "data", "nombres_mapa.json")) else []
for m in nombres:
    if m not in paises:
        paises[m] = {"n": m, "b": "D" if m in TERRITORIOS_D else "T", "p": "S" if m in TERRITORIOS_D else "G", "z": "", "asp": [], "x": "Territorio dependiente.", "terr": True}

# controles
for r in rel: assert r["a"] in ids and r["b"] in ids, r
for o in orgs:
    for d in o["dep"]: assert d in ids, (o["id"], d)

out = os.path.join(RAIZ, "data")
open(os.path.join(out, "meta.js"), "w").write(js("META", meta, "Metadatos: corte, ejes, anclas, bloques, tipos y escalas."))
open(os.path.join(out, "organizaciones.js"), "w").write(js("ORGS", orgs, "Las 200 organizaciones con puntajes y métricas, ordenadas por poder en red."))
open(os.path.join(out, "relaciones.js"), "w").write(js("RELACIONES", rel, "Vínculos entre organizaciones: tipo, intensidad (1 a 3) y explicación."))
open(os.path.join(out, "paises.js"), "w").write(js("PAISES", paises, "Bloque, posición y zona liberada de cada país, por nombre del mapa."))
print(f"{len(orgs)} organizaciones, {len(rel)} relaciones, {len(paises)} países y territorios")
