# Arma la hoja de puntuación (.xlsx) a partir de data/*.js y fuente/fichas.py.
# Uso: python3 scripts/exportar_hoja.py salida.xlsx  (luego se importa en la hoja de Claude)
import json, sys, os
from openpyxl import Workbook
from openpyxl.styles import Font
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, R + "/fuente")
from fichas import FICHAS
from paises import BLOQ, POS, GRADO, ASP
def load(f, var):
    t = open(f"{R}/data/{f}").read()
    return json.loads(t[t.index("=") + 1:].strip().rstrip(";"))
O = load("organizaciones.js", "ORGS"); REL = load("relaciones.js", "R"); P = load("paises.js", "P"); M = load("meta.js", "M")
name = {o["id"]: o["n"] for o in O}
BL = {"T": "Transoceánico", "E": "Euroasiático", "I": "Independiente", "P": "Pendular", "X": "Transnacional"}
FA = {"E": "Expansión", "C": "Captura", "D": "Distorsión"}; CE = {"D": "Documentado", "E": "Estimado", "S": "Especulativo"}
old_src = json.load(open("/tmp/fuentes_rel.json")) if os.path.exists("/tmp/fuentes_rel.json") else {}
wb = Workbook(); ws = wb.active; ws.title = "Organizaciones"
ejes = [x["n"] for x in M["ejes"]]
head = ["Organización", "Área", "Bloque", "Autonomía", "Capacidad", "Poder efectivo", "Poder en red", "Poder formal", "Brecha", "Poder oculto",
        "Fase de Quigley", "Tipo", "Certeza", "Sede", "Depende de"] + ejes + ["Datos que justifican", "Fuentes", "ID", "Puntaje de poder (0-100)", "Alcance efectivo"]
ws.append(head)
from openpyxl.utils import get_column_letter as L_
keys = [x["k"] for x in M["ejes"]]
COL = {k: L_(16 + n) for n, k in enumerate(keys)}; U = COL[keys[-1]]
PES = ",".join(str(M["pesos"][k]) for k in keys)
NORMA = round(M["capmax"] / sum(3 * M["pesos"][k] for k in keys), 6)
for i, o in enumerate(O, start=2):
    f = FICHAS.get(o["id"], {})
    just = " ".join(f.get("res", []))
    src = "\n".join(u for _, u in f.get("fuentes", []))
    fa = f"CHOOSE(D{i},1,0.75,0.5,0.25)"
    if o.get("ext"): just = (just + " Acción fuera de la ley: " + o["ext"][0]).strip(); src = (src + "\n" + o["ext"][1]).strip()
    ws.append([o["n"], o["area"], BL[o["bloque"]], o["aut"], f"=SUMPRODUCT(P{i}:{U}{i},{{{PES}}})*{NORMA}",
               f"=E{i}*({fa}+(1-{fa})*MIN(1,({COL['coe']}{i}+{COL['adq']}{i}+{COL['ext']}{i}+{COL['red']}{i})/12)*{M['autreal']})", o["red"], o["formal"],
               f"=(3-H{i})/3", f"=F{i}*I{i}", FA[o["fase"]], o["tipo"], CE[o["cert"]], o["sede"],
               ", ".join(name[d] for d in o["dep"]) or None] + o["sc"] + [just or None, src or None, o["id"], o["pt"], {"G": "Global", "R": "Regional", "N": "Nacional"}[o["alc"]]])
for c in ws[1]: c.font = Font(bold=True)
ws.freeze_panes = "B2"
for col in ("E", "F", "G", "J"):
    for c in ws[col][1:]: c.number_format = "0.0"
for c in ws["I"][1:]: c.number_format = "0%"
r = wb.create_sheet("Relaciones"); r.append(["Origen", "Destino", "Tipo", "Intensidad", "Descripción", "Fuente"])
for x in sorted(REL, key=lambda x: (x["t"], -x["i"], name[x["a"]])):
    r.append([name[x["a"]], name[x["b"]], x["t"], x["i"], x["x"], old_src.get(name[x["a"]] + "|" + name[x["b"]])])
for c in r[1]: c.font = Font(bold=True)
r.freeze_panes = "A2"
p = wb.create_sheet("Países"); p.append(["País", "Bloque", "Posición", "Zona liberada", "Aspectos", "Nota", "Nombre en el mapa"])
for k, v in sorted(P.items(), key=lambda kv: kv[1]["n"]):
    p.append([v["n"], BLOQ[v["b"]], POS[v["p"]], GRADO[v["z"]] or None, ", ".join(ASP[a] for a in v["asp"]) or None, v["x"] or None, k])
for c in p[1]: c.font = Font(bold=True)
p.freeze_panes = "A2"
for s, w in ((ws, {"A": 42, "B": 24, "N": 26, "O": 30, L_(16 + len(keys)): 80, L_(17 + len(keys)): 50}), (r, {"A": 40, "B": 40, "C": 16, "E": 90, "F": 50}), (p, {"A": 28, "F": 70})):
    for col, wd in w.items(): s.column_dimensions[col].width = wd
wb.save(sys.argv[1] if len(sys.argv) > 1 else "hoja_poder.xlsx"); print(len(O), len(REL), len(P))
