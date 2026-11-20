# Ejes 19 y 20 (17 de noviembre de 2026): cohesión interna y apoyo popular.
# Puntaje editorial de 0 a 3: un valor por categoría y excepciones actor por actor.

EJES = [
    ("coh", "Cohesión interna", "Personas",
     "Unidad de mando frente a la fragmentación: cuánto lo traban las facciones, las pujas internas o las disputas de sucesión.",
     ("Mando único sin pujas visibles; nadie disputa la conducción",
      "Pujas internas contenidas que no frenan sus decisiones",
      "Facciones o rivalidades abiertas que traban o dividen sus decisiones")),
    ("apo", "Apoyo popular", "Personas",
     "Respaldo o legitimidad pública que tiene entre la población: votos, aprobación, fieles, usuarios o prestigio.",
     ("Respaldo de cientos de millones de personas o clara mayoría en una gran potencia",
      "Mayoría o fuerte legitimidad en su país o en su ámbito",
      "Apoyo relevante pero minoritario o limitado")),
    ("pri", "Privilegio legal", "Norma",
     "Lo que la ley le permite y a otros no: actuar sin supervisión, inmunidad (aunque sea mientras dura el cargo), vetos o indultos, cuotas o el monopolio legal de un mercado, o hacer legalmente lo que para otros sería delito.",
     ("Privilegios con efecto mundial: veto en el Consejo de Seguridad, emisión de la moneda de reserva, operaciones encubiertas en el exterior autorizadas por ley o inmunidad soberana total",
      "Privilegios en su país: inmunidad, veto o indulto, secreto legal sin control externo, monopolio legal de un mercado nacional o uso legal de la fuerza, escuchas o detenciones",
      "Privilegios parciales: concesiones o cuotas exclusivas, patentes, exenciones especiales o inmunidad limitada a algunos actos")),
]
# Eje tras el que va cada eje nuevo
DESPUES = {"coh": "red", "apo": "red", "pri": "reg"}

COH_AREA = {
    "Partido único o hegemónico": 3, "Ejército": 2, "Servicio de inteligencia": 2, "Organización criminal": 1, "Gobierno": 2,
    "Familia y oficina patrimonial": 2, "Líder político": 3, "Fuerza de seguridad": 2, "Empresa tecnológica": 2, "Paramilitar": 2,
    "Empresario": 3, "Empresa financiera": 2, "Red social": 2, "Recursos primarios": 2, "Empresa industrial": 2,
    "Empresa de armamento": 2, "Banco central": 2, "Farmacéutica y agroquímica": 2, "Justicia": 1, "Organización religiosa": 2,
    "Partido en sistema competitivo": 1, "Organismo de gobierno": 2, "Organización deportiva": 2, "Consultoría y auditoría": 2,
    "Estandarización e infraestructura técnica": 2, "Medio de comunicación": 2, "Institución mundial": 1, "Federación empresaria": 1,
    "ONG, fundación o think tank": 2, "Logística y transporte": 2, "Sindicato": 1, "Institución de conocimiento": 1,
    "Organización reservada": 1,
}
COH = {
    # Partidos únicos con fracturas
    "psuv": 1, "zanupf": 1, "prosperidad": 2, "mpla": 2, "frelimo": 2, "ccm": 2, "pcc_cuba": 2, "cndd_fdd": 2, "prpl": 2,
    # Ejércitos y mandos
    "epl": 1, "cmc": 1, "ejercito_pak": 3, "ffaa_egipto": 3, "epc": 3, "saf": 1, "tatmadaw": 1, "fanb": 1, "ffaa_gbissau": 1,
    # Inteligencia
    "mossad": 3, "isi": 3, "svr": 3, "mi6": 3, "u8200": 3, "rgb": 3, "cia": 1, "shinbet": 1, "mois": 1,
    # Crimen organizado
    "sinaloa": 0, "cjng": 2, "pcc": 3, "ndrangheta": 2, "prince": 2, "clan_golfo": 2, "sunyeeon": 2,
    # Gobiernos
    "kremlin": 3, "gob_india": 3, "consejoestado": 3, "majzen": 3, "hachemita": 3, "lider_iran": 1, "comisioneu": 1,
    "gob_groenlandia": 1, "coprincipes": 1,
    # Familias
    "saud": 3, "alnahyan": 3, "althani": 3, "maktoum": 3, "bollore": 3, "wallenberg": 3, "rotenberg": 3, "liechtenstein": 3,
    "grimaldi": 3, "wangchuck": 3, "porsche_se": 1, "al_sabah": 1,
    # Líderes con coaliciones o sucesiones en disputa
    "lula": 1, "netanyahu": 1, "rodrigo_paz": 1, "kiir": 1, "sharaa": 1, "delcy": 1, "biya": 1, "zelenski": 2, "milei": 2,
    "prabowo": 2, "kadyrov": 2, "ortega_murillo": 2, "deby": 2, "vilanova": 2,
    # Fuerzas de seguridad
    "dhs": 1,
    # Tecnológicas y redes
    "openai": 1, "x": 3, "telegram": 3, "meta": 3, "spacex": 3, "reliance": 3, "adani": 3, "lvmh": 3, "vw": 1, "boeing": 1,
    # Paramilitares
    "hutis": 3, "lna": 3, "isis": 1, "talibanes": 1, "pmf": 1, "eln": 1, "hamas": 1,
    # Finanzas y recursos
    "setad": 3, "pif": 3, "pdvsa": 1, "nnpc": 1, "petrobras": 1,
    # Bancos centrales y justicia
    "fed": 1, "doj": 1, "scotus": 2, "stf": 2, "sc_india": 2, "tjue": 2, "cpi": 1,
    # Religión
    "sud": 3, "aqr": 3, "patriarcado": 3, "opusdei": 3, "hermandad": 1,
    # Partidos en sistemas competitivos
    "bjp": 3, "sns": 3, "sueno_georgiano": 3, "akp": 3, "ps_albania": 3, "gop": 2, "morena": 2, "pt_br": 2, "fpa": 2, "smer": 2,
    "dem": 0, "marco_coord": 0,
    # Organismos
    "congreso_eeuu": 1, "congreso_br": 1, "ccdi": 3, "oficina39": 3, "ufwd": 3, "consejo_seg_rusia": 3,
    # Instituciones mundiales
    "csonu": 0, "brics": 0, "omc": 0, "bm": 2, "fmi": 2, "aes": 2, "ohr": 2,
    # Otros
    "ugle": 2, "aflcio": 2, "cut_br": 2, "igmetall": 2, "rt": 3, "xinhua": 3, "wef": 1, "aipac": 3,
}

APO_AREA = {
    "Partido único o hegemónico": 1, "Ejército": 2, "Servicio de inteligencia": 1, "Organización criminal": 1, "Gobierno": 1,
    "Familia y oficina patrimonial": 1, "Líder político": 1, "Fuerza de seguridad": 1, "Empresa tecnológica": 2, "Paramilitar": 1,
    "Empresario": 1, "Empresa financiera": 1, "Red social": 2, "Recursos primarios": 1, "Empresa industrial": 2,
    "Empresa de armamento": 1, "Banco central": 1, "Farmacéutica y agroquímica": 1, "Justicia": 1, "Organización religiosa": 2,
    "Partido en sistema competitivo": 2, "Organismo de gobierno": 1, "Organización deportiva": 2, "Consultoría y auditoría": 0,
    "Estandarización e infraestructura técnica": 1, "Medio de comunicación": 1, "Institución mundial": 1, "Federación empresaria": 0,
    "ONG, fundación o think tank": 1, "Logística y transporte": 1, "Sindicato": 1, "Institución de conocimiento": 2,
    "Organización reservada": 0,
}
APO = {
    # Partidos únicos
    "pcch": 2, "pcv": 2, "fpr": 2, "ccm": 2, "psuv": 0,
    # Ejércitos
    "ffaa_india": 3, "tatmadaw": 0, "fanb": 0, "saf": 1, "epc": 1, "ffaa_br": 1, "bundeswehr": 1,
    # Gobiernos
    "gob_india": 3, "kremlin": 2, "consejoestado": 2, "majzen": 2, "hachemita": 2, "lider_iran": 0,
    # Familias
    "saud": 2, "alnahyan": 2, "althani": 2, "maktoum": 2, "wangchuck": 2, "liechtenstein": 2,
    "koch": 0, "bollore": 0, "rothschild": 0, "rotenberg": 0,
    # Líderes
    "prabowo": 3, "erdogan": 2, "lula": 2, "milei": 2, "zelenski": 2, "bukele": 2, "delcy": 0, "kadyrov": 0,
    # Fuerzas de seguridad y paramilitares
    "cgri": 0, "basij": 0, "hezbola": 2, "isis": 0, "jnim": 0, "far_sudan": 0, "africacorps": 0, "m23": 0, "alshabaab": 0,
    # Tecnológicas, redes e industria
    "apple": 3, "alphabet": 3, "amazon": 3, "openai": 3, "nvidia": 1, "palantir": 0, "anduril": 0, "nso": 0, "tsmc": 1,
    "foxconn": 1, "asml": 1, "smic": 1, "meta": 3, "tencent": 3, "bytedance": 3, "toyota": 3, "samsung": 3,
    # Personas
    "ellison": 0, "thiel": 0, "kovalchuk": 0, "timchenko": 0,
    # Finanzas y recursos
    "setad": 0, "berkshire": 2, "petrobras": 2, "pdvsa": 0,
    # Justicia
    "sc_india": 2,
    # Religión
    "santasede": 3, "hawza_najaf": 2, "alazhar": 2, "opusdei": 1, "lmm": 1,
    # Partidos
    "bjp": 3, "ldp": 1, "anc": 1, "marco_coord": 1, "fpa": 1, "fuerza_popular": 1,
    # Organismos
    "congreso_eeuu": 0, "congreso_br": 0,
    # Deporte, medios, instituciones
    "fifa": 3, "bbc": 2, "globo": 2, "aljazeera": 2, "otan": 2, "cas": 1,
    # Influencia
    "gates": 1, "wef": 0, "osf": 0, "cfr": 0, "cut_br": 2, "aflcio": 2, "igmetall": 2, "uschamber": 1, "keidanren": 1,
}


def valor(tabla, area_tabla, i, area):
    return tabla.get(i, area_tabla[area])

PRI_AREA = {
    "Gobierno": 2, "Ejército": 2, "Servicio de inteligencia": 2, "Fuerza de seguridad": 2, "Banco central": 2, "Justicia": 2,
    "Partido único o hegemónico": 2, "Partido en sistema competitivo": 1, "Organismo de gobierno": 1, "Institución mundial": 1,
    "Estandarización e infraestructura técnica": 1, "Empresa financiera": 1, "Empresa tecnológica": 0, "Red social": 1,
    "Recursos primarios": 1, "Empresa de armamento": 1, "Empresa industrial": 0, "Logística y transporte": 0,
    "Farmacéutica y agroquímica": 1, "Consultoría y auditoría": 0, "Familia y oficina patrimonial": 0, "Líder político": 2,
    "Empresario": 0, "Organización criminal": 0, "Paramilitar": 0, "Organización reservada": 0, "Organización religiosa": 1,
    "Federación empresaria": 0, "ONG, fundación o think tank": 0, "Organización deportiva": 2, "Sindicato": 1,
    "Medio de comunicación": 0, "Institución de conocimiento": 0,
}
PRI = {
    # Alcance mundial
    "casablanca": 3, "pentagono": 3, "cia": 3, "nsa": 3, "fed": 3, "csonu": 3, "pcch": 3, "ptk": 3, "saud": 3, "lider_iran": 3,
    # Monarcas con poder real
    "alnahyan": 2, "althani": 2, "maktoum": 2, "al_sabah": 2, "al_khalifa": 2, "liechtenstein": 2, "grimaldi": 2, "wangchuck": 2, "tupou": 2,
    "santasede": 2, "aqr": 2,
    # Líderes sin inmunidad
    "netanyahu": 1,
    # Monopolios legales y empresas del Estado
    "aramco": 2, "gazprom": 2, "pdvsa": 2, "nnpc": 2, "sonatrach": 2, "ocp": 2, "stategrid": 2, "rosatom": 2, "cnnc": 2, "edf": 2,
    "kazatomprom": 2, "pif": 2, "setad": 2, "khatam": 2, "oficina39": 2, "cosco": 1, "cmport": 1, "dpworld": 1, "spacex": 1, "nso": 1,
    # Organismos
    "city_londres": 2, "acp": 2, "junta_pr": 2, "doe": 2, "tesoro_eeuu": 2, "bis": 2, "congreso_eeuu": 2, "congreso_br": 2, "sasac": 2,
    "ccdi": 2, "org_pcch": 2, "prop_pcch": 2,
    # Seguridad
    "pf_br": 1, "cac": 2,
    # Paramilitares con estatus legal
    "pmf": 2, "talibanes": 2, "hezbola": 1, "lna": 1,
    # Instituciones mundiales y técnicas
    "bm": 2, "fmi": 2, "cpi": 2, "icann": 2, "swift": 2,
    # Bancos centrales menores
    "eccb": 1,
    # Sindicatos, medios
    "cgt_arg": 2, "bbc": 2, "xinhua": 2, "rt": 1,
}

from nucleo2 import COH as _COH2, APO as _APO2
COH.update(_COH2); APO.update(_APO2)
from nucleo3 import COH as _COH3, APO as _APO3, PRI as _PRI3
COH.update(_COH3); APO.update(_APO3); PRI.update(_PRI3)
from nucleo4 import COH as _COH4, APO as _APO4, PRI as _PRI4
COH.update(_COH4); APO.update(_APO4); PRI.update(_PRI4)
import importlib as _il
for _t in ["nucleo5", "nucleo6", "nucleo7", "nucleo8"]:
    _m = _il.import_module(_t); COH.update(_m.COH); APO.update(_m.APO); PRI.update(_m.PRI)

from revision import COH as _COH_R, APO as _APO_R, PRI as _PRI_R
COH.update(_COH_R); APO.update(_APO_R); PRI.update(_PRI_R)
