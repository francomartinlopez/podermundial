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
from fichas import FICHAS
from locales import MANDA
from poder_duro import PESOS, EXT, AUTONOMIA_REAL
from ejes_nuevos import COH, COH_AREA, APO, APO_AREA, PRI, PRI_AREA
from alcance import VALOR as ALC_V, NOMBRE as ALC_N, GLOBAL as ALC_G, REGIONAL as ALC_R, alcance
from cambios import CAMBIOS
from friccion import FRICCION
from paises_juego import PJ, EXTRA
from paises_datos import DATOS as PDATOS
from categorias import ESTIRAR, TEORICO, PESO_FINAL, PESO_REL, MONARCAS, NOTA_MONARCA
import math

CORTE = "2026-11-17"
PROXIMA = "2027-02-16"
TERRITORIOS_D = {"Siachen Glacier"}
RU, EU, FR, PB, AU, NZ = "Reino Unido", "Estados Unidos", "Francia", "Países Bajos", "Australia", "Nueva Zelanda"
TERR_ES = {  # nombre en español y país del que dependen
    "N. Mariana Is.": ("Islas Marianas del Norte", EU), "U.S. Virgin Is.": ("Islas Vírgenes de EE.UU.", EU), "Guam": ("Guam", EU),
    "American Samoa": ("Samoa Americana", EU), "S. Geo. and the Is.": ("Georgias del Sur y Sandwich del Sur", RU),
    "Br. Indian Ocean Ter.": ("Territorio Británico del Océano Índico (Diego García)", RU), "Saint Helena": ("Santa Elena", RU),
    "Pitcairn Is.": ("Islas Pitcairn", RU), "Anguilla": ("Anguila", RU), "Falkland Is.": ("Islas Malvinas", RU), "Bermuda": ("Bermudas", RU),
    "British Virgin Is.": ("Islas Vírgenes Británicas", RU), "Turks and Caicos Is.": ("Islas Turcas y Caicos", RU), "Montserrat": ("Montserrat", RU),
    "Guernsey": ("Guernsey", RU), "Isle of Man": ("Isla de Man", RU), "Jersey": ("Jersey", RU), "Cayman Is.": ("Islas Caimán", RU),
    "Niue": ("Niue", NZ), "Cook Is.": ("Islas Cook", NZ), "Aruba": ("Aruba", PB), "Curaçao": ("Curazao", PB), "Sint Maarten": ("San Martín (Países Bajos)", PB),
    "St. Pierre and Miquelon": ("San Pedro y Miquelón", FR), "Wallis and Futuna Is.": ("Wallis y Futuna", FR), "St-Martin": ("San Martín (Francia)", FR),
    "St-Barthélemy": ("San Bartolomé", FR), "Fr. Polynesia": ("Polinesia Francesa", FR), "New Caledonia": ("Nueva Caledonia", FR),
    "Fr. S. Antarctic Lands": ("Tierras Australes y Antárticas Francesas", FR), "Åland": ("Åland", "Finlandia"), "Faeroe Is.": ("Islas Feroe", "Dinamarca"),
    "Indian Ocean Ter.": ("Islas Christmas y Cocos", AU), "Heard I. and McDonald Is.": ("Islas Heard y McDonald", AU), "Norfolk Island": ("Isla Norfolk", AU),
    "Ashmore and Cartier Is.": ("Islas Ashmore y Cartier", AU), "Siachen Glacier": ("Glaciar de Siachen", None),
}  # el resto de los territorios dependientes hereda el bloque transoceánico

def js(nombre, valor, comentario):
    return f"// {comentario}\n// Generado por scripts/generar_datos.py: no editar a mano.\nwindow.{nombre} = " + json.dumps(valor, ensure_ascii=False, separators=(",", ":")) + ";\n"

fac = {1: 1, 2: .75, 3: .5, 4: .25}
ids = {o[0] for o in ORGS}
for k in EXT: assert k in ids, k
for k in list(COH) + list(APO) + list(PRI): assert k in ids, k
masters = {o[0]: [d for d in o[8].split(",") if d] for o in ORGS}
ejes = [e[0] for e in EJES]
peso = {k: PESOS.get(k, 1) for k in ejes}
CAPMAX = 3 * len(ejes)
norma = CAPMAX / sum(3 * w for w in peso.values())
SC = {}
for o in ORGS:
    sc = dict(zip(ORDEN_ENTRADA, map(int, o[6]))); sc["ext"] = EXT.get(o[0], (0,))[0]
    sc["coh"] = COH.get(o[0], COH_AREA[o[2]]); sc["apo"] = APO.get(o[0], APO_AREA[o[2]]); sc["pri"] = PRI.get(o[0], PRI_AREA[o[2]]); SC[o[0]] = sc
cap = {i: round(sum(SC[i][k] * peso[k] for k in ejes) * norma, 2) for i in ids}
# autonomía real: armas, secretos, acción fuera de la ley y contactos dan margen propio frente al jefe formal
dur = {i: min(1, (SC[i]["coe"] + SC[i]["adq"] + SC[i]["ext"] + SC[i]["red"]) / 12) for i in ids}
aut = {o[0]: o[5] for o in ORGS}
freal = {i: fac[aut[i]] + (1 - fac[aut[i]]) * dur[i] * AUTONOMIA_REAL for i in ids}
pe = {i: cap[i] * freal[i] for i in ids}
memo = {}
def red(i, pila=()):
    if i in memo: return memo[i]
    if i in pila: raise SystemExit(f"Ciclo de dependencias en {i}")
    v = pe[i] + 0.5 * sum(red(j, pila + (i,)) * (1 - AUTONOMIA_REAL * dur[j]) / len(masters[j]) for j in ids if i in masters[j])
    memo[i] = v; return v

orgs = []
for o in ORGS:
    sc = SC[o[0]]; f = FORMAL[o[0]]
    orgs.append({"id": o[0], "n": o[1], "area": o[2], "tipo": AREA_TIPO[o[2]], "bloque": o[4], "aut": o[5],
                 "sc": [sc[k] for k in ejes], "cap": cap[o[0]], "fr": round(freal[o[0]], 3), "pe": round(pe[o[0]], 2), "red": round(red(o[0]), 2),
                 "formal": f, "brecha": round((3 - f) / 3, 4), "oculto": round(pe[o[0]] * (3 - f) / 3, 2),
                 "fase": FASE[o[0]], "cert": o[7], "sede": o[3], "ll": C[o[3]], "dep": masters[o[0]],
                 **({"ext": list(EXT[o[0]][1:])} if o[0] in EXT else {})})

# Puntaje de categoría real: sale del relevamiento cargado (autonomía, mando sobre otros, dependientes, desafío al jefe formal)
for o in orgs: assert o["area"] in TEORICO, o["area"]
for m in MONARCAS: assert m in ids, m
for m in ALC_G | ALC_R: assert m in ids, m
byid = {o["id"]: o for o in orgs}
# Una sola relación por par de actores: si el par aparece dos veces (en cualquier sentido), se queda la primera,
# con la mayor intensidad y la descripción más completa.
_rel = {}
for a, b, t, x, n in RELACIONES:
    k = frozenset((a, b))
    if k not in _rel: _rel[k] = [a, b, t, x, n]; continue
    r = _rel[k]; r[4] = max(r[4], n)
    if len(x) > len(r[3]): r[3] = x
RELACIONES = [tuple(r) for r in _rel.values()]
sale = {i: 0.0 for i in ids}; entra = {i: 0.0 for i in ids}; desafia = {i: 0 for i in ids}; ndep = {i: 0 for i in ids}
for a, b, t, x, n in RELACIONES:
    w = PESO_REL.get(t)
    if w: sale[a] += w; entra[b] += w
    if t in ("Enfrentamiento", "Ambigua"):
        if b in masters[a]: desafia[a] = 1
        if a in masters[b]: desafia[b] = 1
for i in ids:
    for d in masters[i]: sale[d] += 1; entra[i] += 1; ndep[d] += 1
real_actor = {i: min(1, .5 * (4 - aut[i]) / 3 + .3 * (sale[i] + 1) / (sale[i] + entra[i] + 2) + .2 * min(1, ndep[i] / 3) + .15 * desafia[i]) for i in ids}
REAL = {}
for o in orgs: REAL.setdefault(o["area"], []).append(real_actor[o["id"]])
REAL = {a: round(10 * sum(v) / len(v), 1) for a, v in REAL.items()}

# Puntaje final: media geométrica ponderada, llevada a 0-100 con el mayor en 100
heredado = {o["id"]: o["red"] - o["pe"] for o in orgs}
hmax = max(heredado.values())
def comp(o):
    return {"ct": TEORICO[o["area"]] / 10, "cr": REAL[o["area"]] / 10, "cap": max(o["cap"], .5) / CAPMAX, "aut": o["fr"],
            "red": .5 + .5 * math.log1p(heredado[o["id"]]) / math.log1p(hmax), "alc": ALC_V[alcance(o["id"])] / ALC_V["G"]}
bruto = {o["id"]: math.prod(v ** PESO_FINAL[k] for k, v in comp(o).items() if k in PESO_FINAL) for o in orgs}
bmax = max(bruto.values())
for o in orgs: o["pt"] = round(100 * (bruto[o["id"]] / bmax) ** ESTIRAR, 1)
for o in orgs: o["alc"] = alcance(o["id"])
# Poder oculto de 0 a 100: puntaje de poder (ya estirado) por la brecha, y el mayor vale 100
_omax = max(o["pt"] * o["brecha"] for o in orgs)
for o in orgs: o["oculto"] = round(100 * o["pt"] * o["brecha"] / _omax, 1)
for o in orgs: o["cp"] = [round(comp(o)[k], 3) for k in PESO_FINAL]
orgs.sort(key=lambda x: (-x["pt"], -x["red"], x["n"]))

fam = []
for e in EJES:
    if not fam or fam[-1]["n"] != e[2]: fam.append({"n": e[2], "ejes": []})
    fam[-1]["ejes"].append(e[0])
meta = {"corte": CORTE, "proxima": PROXIMA, "skeleton": False, "pesos": peso, "capmax": CAPMAX, "autreal": AUTONOMIA_REAL,
        "peso_final": PESO_FINAL, "estirar": ESTIRAR, "cambios": CAMBIOS, "alcance": {k: {"n": ALC_N[k], "v": ALC_V[k]} for k in ALC_V}, "monarcas": sorted(MONARCAS), "nota_monarca": NOTA_MONARCA, "categorias": {a: {"t": TEORICO[a], "r": REAL[a], "tipo": AREA_TIPO[a], "k": sum(1 for o in orgs if o["area"] == a)} for a in TEORICO},
        "ejes": [{"k": e[0], "n": e[1], "fam": e[2], "x": e[3], "a": list(ANCLAS[e[0]])} for e in EJES], "familias": fam,
        "bloques": {"T": {"n": "Transoceánico", "c": "#2F6BFF"}, "E": {"n": "Euroasiático", "c": "#9E1B32"},
                    "I": {"n": "Independiente", "c": "#BDBDBD"}, "P": {"n": "Pendular", "c": "#F2A93B"},
                    "X": {"n": "Transnacional", "c": "#F5F0E6"}, "D": {"n": "Terreno disputado", "c": "#141414"}},
        "autonomia": {str(k): v for k, v in AUTONOMIA.items()}, "certeza": CERTEZA, "fases": FASES,
        "tipos": ["Estado", "Capital", "Información", "Supranacional", "Influencia", "Sombra", "Persona"],
        "posiciones": POS, "grados": GRADO, "aspectos": ASP,
        "friccion": [dict(f, actores=[{"id": a, "r": r} for a, r in f["actores"]]) for f in FRICCION]}
rel = [{"a": a, "b": b, "t": t, "x": x, "i": i} for a, b, t, x, i in RELACIONES]
paises = {m: {"n": es, "b": b, "p": p, "z": z, "asp": a, "x": n} for m, es, b, p, z, a, n in PAISES}
nombres = json.load(open(os.path.join(RAIZ, "data", "nombres_mapa.json"))) if os.path.exists(os.path.join(RAIZ, "data", "nombres_mapa.json")) else []
for m in nombres:
    if m not in paises:
        _t = TERR_ES.get(m, (m, None))
        paises[m] = {"n": _t[0], "b": "D" if m in TERRITORIOS_D else "T", "p": "S" if m in TERRITORIOS_D else "G", "z": "", "asp": [], "x": ("Bajo control británico desde 1833 y reclamadas por la Argentina; base militar británica en Mount Pleasant." if m == "Falkland Is." else "Base militar conjunta de EE.UU. y Reino Unido en Diego García; Mauricio reclama la soberanía y en 2025 se firmó su traspaso con arriendo de la base." if m == "Br. Indian Ocean Ter." else f"Territorio dependiente de {_t[1]}." if _t[1] else "Zona en disputa entre India y Pakistán." if m == "Siachen Glacier" else "Territorio dependiente."), "terr": True}

for f in FRICCION:
    for a, _ in f["actores"]: assert a in ids, (f["n"], a)
    for c in f["paises"]: assert c in paises, (f["n"], c)
for m, (i, nota) in MANDA.items():
    assert m in paises, m
    assert i in ids, (m, i)
    paises[m]["m"] = [i, nota]

# controles
for r in rel: assert r["a"] in ids and r["b"] in ids, r
for o in orgs:
    for d in o["dep"]: assert d in ids, (o["id"], d)

out = os.path.join(RAIZ, "data")
open(os.path.join(out, "meta.js"), "w").write(js("META", meta, "Metadatos: corte, ejes, anclas, bloques, tipos y escalas."))
open(os.path.join(out, "organizaciones.js"), "w").write(js("ORGS", orgs, "Las organizaciones con puntajes y métricas, ordenadas por poder en red."))
open(os.path.join(out, "relaciones.js"), "w").write(js("RELACIONES", rel, "Vínculos entre organizaciones: tipo, intensidad (1 a 3) y explicación."))
for k in FICHAS: assert k in ids, k
fichas = {k: {"res": v["res"], "manda": v["manda"], "dinero": v["dinero"], "crono": v["crono"], "fuentes": v["fuentes"], "rev": CORTE} for k, v in FICHAS.items()}
open(os.path.join(out, "fichas.js"), "w").write(js("FICHAS", fichas, "Contenido de las fichas cargadas: resumen, quién manda, dinero, cronología y fuentes."))
open(os.path.join(out, "paises.js"), "w").write(js("PAISES", paises, "Bloque, posición y zona liberada de cada país, por nombre del mapa."))
# ficha de cada país: qué está en juego, cronología y datos clave (cifras del CIA World Factbook)
for m in paises: assert m in PJ, ("falta en paises_juego.py", m)
for m in PJ: assert m in paises, ("sobra en paises_juego.py", m)
pfichas = {}
for m, v in PJ.items():
    d = dict(PDATOS.get(m, {})); d.update(EXTRA.get(m, {}))
    pfichas[m] = dict(v, crono=[[str(a), x] for a, x in v["crono"]], d={k: (list(x) if isinstance(x, tuple) else [list(y) for y in x] if isinstance(x, list) else x) for k, x in d.items()})
open(os.path.join(out, "paisfichas.js"), "w").write(js("PFICHAS", pfichas, "Ficha de cada país: qué está en juego, cronología, gobierno, sociedad, recursos, economía y cifras (CIA World Factbook)."))
print(f"{len(FICHAS)} fichas, {len(orgs)} organizaciones, {len(rel)} relaciones, {len(paises)} países y territorios")
