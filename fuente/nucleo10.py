# Décima tanda (20 de noviembre de 2026): Suiza, Reino Unido, Francia, España, Italia, Países Bajos, Hungría y Turquía.
# ACTORES: id, nombre, área, sede, bloque, autonomía, 17 puntajes (orden de entrada), certeza, depende de, poder formal, fase.
W = "https://en.wikipedia.org/wiki/"
F_ = "01020001222001002"   # financiera
X_ = "11110001121101012"   # gran empresa
M_ = "01120002121101012"   # farmacéutica
D_ = "02220002111101011"   # armamento

ACTORES = [
 ("nestle", "Nestlé", "Empresa industrial", "Vevey, Suiza", "X", 2, "21110001221201012", "D", "", 1, "C"),
 ("roche", "Roche (familias Hoffmann y Oeri)", "Farmacéutica y agroquímica", "Basilea, Suiza", "X", 2, M_, "D", "", 1, "C"),
 ("novartis", "Novartis", "Farmacéutica y agroquímica", "Basilea, Suiza", "X", 2, M_, "D", "", 1, "C"),
 ("mercuria", "Mercuria Energy", "Recursos primarios", "Ginebra, Suiza", "X", 2, "11110001121101012", "D", "", 1, "C"),
 ("astrazeneca", "AstraZeneca", "Farmacéutica y agroquímica", "Cambridge, Reino Unido", "T", 2, M_, "D", "", 1, "C"),
 ("amundi", "Amundi (Crédit Agricole)", "Empresa financiera", "París, Francia", "T", 2, F_, "D", "", 1, "C"),
 ("socgen", "Société Générale", "Empresa financiera", "París, Francia", "T", 2, F_, "D", "", 1, "C"),
 ("afp", "AFP (Agence France-Presse)", "Medio de comunicación", "París, Francia", "T", 2, "00002000021001001", "D", "", 1, "C"),
 ("indra", "Indra", "Empresa de armamento", "Madrid, España", "T", 2, D_, "D", "", 1, "E"),
 ("acs", "ACS (Florentino Pérez)", "Empresa industrial", "Madrid, España", "T", 2, X_, "D", "", 1, "C"),
 ("generali", "Generali", "Empresa financiera", "Trieste, Italia", "T", 2, F_, "D", "", 1, "C"),
 ("aise", "AISE (inteligencia exterior de Italia)", "Servicio de inteligencia", "Roma, Italia", "T", 3, "00000211011022001", "D", "meloni", 1, "C"),
 ("nexperia", "Nexperia", "Empresa tecnológica", "Nimega, Países Bajos", "X", 1, "01110001111101001", "D", "", 1, "D"),
 ("otp", "OTP Bank (Sándor Csányi)", "Empresa financiera", "Budapest, Hungría", "X", 2, F_, "D", "", 1, "C"),
 ("chp", "CHP (Partido Republicano del Pueblo)", "Partido en sistema competitivo", "Ankara, Turquía", "X", 2, "00101010010000100", "D", "", 2, "E"),
 ("diyanet", "Diyanet (Presidencia de Asuntos Religiosos de Turquía)", "Organización religiosa", "Ankara, Turquía", "P", 3, "00121010030001101", "D", "erdogan", 2, "E"),
 ("aselsan", "Aselsan", "Empresa de armamento", "Ankara, Turquía", "P", 3, D_, "D", "", 1, "E"),
 ("tai", "TUSAŞ (Turkish Aerospace)", "Empresa de armamento", "Ankara, Turquía", "P", 3, D_, "D", "", 1, "E"),
]

ALC_G = {"nestle", "roche", "novartis", "mercuria", "astrazeneca", "amundi", "afp", "acs", "generali"}
ALC_R = {"socgen", "indra", "aise", "nexperia", "otp", "diyanet", "aselsan", "tai"}
COH = {"chp": 2}
APO = {"chp": 3, "diyanet": 2}
PRI = {"aise": 2, "diyanet": 1}

COORDS = {
 "Vevey, Suiza": (6.84, 46.46), "Basilea, Suiza": (7.59, 47.56), "Ginebra, Suiza": (6.14, 46.2), "Cambridge, Reino Unido": (0.12, 52.2),
 "París, Francia": (2.35, 48.86), "Madrid, España": (-3.7, 40.42), "Trieste, Italia": (13.78, 45.65), "Roma, Italia": (12.5, 41.9),
 "Nimega, Países Bajos": (5.86, 51.84), "Budapest, Hungría": (19.04, 47.5), "Ankara, Turquía": (32.85, 39.93),
}

EXT = {
 "socgen": (1, "Acordó en 2018 con el Departamento de Justicia de EE.UU. pagar unos 860 millones de dólares por sobornos en Libia y la manipulación de la tasa Libor.", W + "Soci%C3%A9t%C3%A9_G%C3%A9n%C3%A9rale"),
}
MANDA = {}

def _f(res, manda, dinero, crono, fuentes):
    return dict(res=res, manda=manda, dinero=dinero, crono=crono, fuentes=fuentes)

FICHAS = {
"nestle": _f(["La mayor empresa de alimentos del mundo, presente en casi todos los países; pesa en el agua embotellada, el café y la nutrición infantil."], ["Sus accionistas y su directorio; Philipp Navratil es director ejecutivo desde septiembre de 2025."], "Venta de alimentos y bebidas.",
    [("1866", "Fundación."), ("2025-09", "Despide a su director ejecutivo, Laurent Freixe, por una relación no informada con una subordinada.")], [("Nestlé (Wikipedia)", W + "Nestl%C3%A9")]),
"roche": _f(["Una de las mayores farmacéuticas del mundo y líder en diagnóstico; las familias fundadoras controlan la mayoría de los votos."], ["Las familias Hoffmann y Oeri, con la mayoría de las acciones con voto."], "Medicamentos oncológicos y diagnóstico.",
    [("1896", "Fundación."), ("2009", "Compra el total de Genentech.")], [("Roche (Wikipedia)", W + "Roche_Holding")]),
"novartis": _f(["Una de las mayores farmacéuticas del mundo, nacida de la fusión de Ciba-Geigy y Sandoz."], ["Sus accionistas y su directorio."], "Medicamentos innovadores.",
    [("1996", "Fusión de Ciba-Geigy y Sandoz."), ("2023-10", "Separa su negocio de genéricos, Sandoz.")], [("Novartis (Wikipedia)", W + "Novartis")]),
"mercuria": _f(["Una de las grandes comercializadoras de energía y materias primas, con sede en Ginebra, el principal centro mundial de ese comercio."], ["Sus fundadores, Marco Dunand y Daniel Jaeggi, y sus socios."], "Comercio de petróleo, gas, electricidad y metales.",
    [("2004", "Fundación.")], [("Mercuria Energy Group (Wikipedia)", W + "Mercuria_Energy_Group")]),
"astrazeneca": _f(["Farmacéutica anglo-sueca; produjo con la Universidad de Oxford una de las vacunas contra el COVID-19 más usadas en el mundo."], ["Sus accionistas y su director, Pascal Soriot."], "Medicamentos oncológicos, cardiovasculares y respiratorios.",
    [("1999", "Fusión de Astra y Zeneca."), ("2020-12", "El Reino Unido aprueba su vacuna."), ("2025-07", "Anuncia una inversión de 50.000 millones de dólares en EE.UU. ante la amenaza de aranceles.")], [("AstraZeneca (Wikipedia)", W + "AstraZeneca")]),
"amundi": _f(["La mayor gestora de fondos de Europa, controlada por el banco Crédit Agricole."], ["Crédit Agricole, su accionista mayoritario."], "Comisiones sobre fondos.",
    [("2010", "Fundación.")], [("Amundi (Wikipedia)", W + "Amundi")]),
"socgen": _f(["Uno de los grandes bancos de Francia y de la zona euro."], ["Sus accionistas y su director, Slawomir Krupa."], "Banca minorista, de inversión y financiamiento.",
    [("1864", "Fundación."), ("2008-01", "Pierde casi 5.000 millones de euros por las operaciones de Jérôme Kerviel."), ("2018-06", "Acuerdo con la justicia de EE.UU. por sobornos en Libia y la tasa Libor.")], [("Société Générale (Wikipedia)", W + "Soci%C3%A9t%C3%A9_G%C3%A9n%C3%A9rale")]),
"afp": _f(["Una de las tres grandes agencias de noticias del mundo, junto con AP y Reuters; financiada en parte por el Estado francés."], ["Su presidente, elegido por un consejo con representantes del Estado y de la prensa."], "Venta de servicios informativos y aporte estatal.",
    [("1944", "Fundación.")], [("Agence France-Presse (Wikipedia)", W + "Agence_France-Presse")]),
"indra": _f(["Principal empresa española de electrónica de defensa y control del tráfico aéreo; el Estado es su mayor accionista y la usa para concentrar la industria de defensa."], ["La SEPI, accionista estatal, y su presidente, Ángel Escribano."], "Contratos de defensa y tecnología.",
    [("1993", "Fundación."), ("2025", "Gana gran parte de los programas del plan español de gasto en defensa.")], [("Indra Sistemas (Wikipedia)", W + "Indra_Sistemas")]),
"acs": _f(["Una de las mayores constructoras del mundo; controla la alemana Hochtief y la estadounidense Turner."], ["Florentino Pérez, presidente y principal accionista."], "Construcción e infraestructura.",
    [("1997", "Fusión de OCP y Ginés Navarro."), ("2011", "Toma el control de Hochtief.")], [("ACS Group (Wikipedia)", W + "ACS_Group")]),
"generali": _f(["La mayor aseguradora de Italia y una de las mayores de Europa; gran tenedora de deuda pública italiana."], ["Sus accionistas: Mediobanca, Delfin y el grupo Caltagirone pesan en su control."], "Seguros y gestión de activos.",
    [("1831", "Fundación en Trieste.")], [("Assicurazioni Generali (Wikipedia)", W + "Assicurazioni_Generali")]),
"aise": _f(["Servicio de inteligencia exterior de Italia."], ["Su director, que responde al presidente del Consejo de Ministros."], "Presupuesto de inteligencia.",
    [("2007", "Creación por la reforma de los servicios italianos.")], [("AISE (Wikipedia)", W + "Agenzia_Informazioni_e_Sicurezza_Esterna")]),
"nexperia": _f(["Fabricante de chips básicos para autos, con sede en Nimega y dueña china (Wingtech). En 2025 el gobierno neerlandés tomó el control y China frenó sus exportaciones, lo que paralizó parte de la industria automotriz europea."], ["La conducción europea designada por el tribunal; Wingtech conserva la propiedad y reclama el control."], "Venta de semiconductores.",
    [("2017", "Se separa de NXP."), ("2019", "Wingtech completa su compra."), ("2024-12", "EE.UU. incluye a Wingtech en su lista de entidades."), ("2025-09-30", "El gobierno neerlandés interviene la empresa."),
     ("2025-10", "China bloquea las exportaciones de sus chips desde China."), ("2025-11", "Países Bajos suspende la intervención como gesto hacia China; la disputa judicial sigue.")],
    [("Nexperia (Wikipedia)", W + "Nexperia"), ("Dutch government takes control of Nexperia (AP)", "https://www.mbtmag.com/global/news/22952379/dutch-government-takes-control-of-chineseowned-chipmaker-nexperia-over-governance-shortcomings")]),
"otp": _f(["El mayor banco de Hungría, con filiales en Europa central y oriental y en Rusia."], ["Sándor Csányi, presidente desde 1992."], "Banca minorista.",
    [("1949", "Fundación como caja de ahorro estatal."), ("2023-05", "Ucrania lo incluye en su lista de patrocinadores de la guerra por seguir en Rusia; lo retira en septiembre.")], [("OTP Bank (Wikipedia)", W + "OTP_Bank")]),
"chp": _f(["Principal partido opositor de Turquía, fundado por Atatürk. Ganó las elecciones municipales de 2024; su candidato presidencial, Ekrem İmamoğlu, está preso desde 2025 y es juzgado con más de 400 acusados en una causa por corrupción que el partido y organismos de derechos humanos consideran política."], ["Özgür Özel, presidente del partido."], "Aportes estatales y de afiliados.",
    [("1923", "Fundación."), ("2024-03-31", "Primer partido en las elecciones municipales."), ("2025-03-23", "Prisión preventiva de İmamoğlu."), ("2026-03-09", "Empieza el juicio a İmamoğlu y otros 401 acusados.")],
    [("Republican People's Party (Wikipedia)", W + "Republican_People%27s_Party"), ("Türkiye: Leading Opponent of Erdoğan on Trial (Human Rights Watch)", "https://www.hrw.org/news/2026/03/03/turkiye-leading-opponent-of-erdogan-on-trial")]),
"diyanet": _f(["Administra las mezquitas de Turquía, designa a los imanes y redacta los sermones del viernes; a través de su red en el exterior llega a la diáspora turca en Europa."], ["Su presidente, designado por el presidente de la República."], "Presupuesto público, mayor que el de varios ministerios.",
    [("1924", "Creación.")], [("Diyanet (Wikipedia)", W + "Presidency_of_Religious_Affairs")]),
"aselsan": _f(["Mayor empresa de electrónica de defensa de Turquía: radares, defensa aérea y comunicaciones."], ["La Fundación de Fortalecimiento de las Fuerzas Armadas, su accionista mayoritario."], "Contratos de defensa y exportaciones.",
    [("1975", "Fundación.")], [("Aselsan (Wikipedia)", W + "Aselsan")]),
"tai": _f(["Fabricante turco de aviones y helicópteros militares; desarrolla el caza KAAN y el dron Anka."], ["El Estado turco, a través de la fundación de las Fuerzas Armadas y la Presidencia de Industrias de Defensa."], "Contratos de defensa.",
    [("1973", "Fundación."), ("2024-02-21", "Primer vuelo del caza KAAN."), ("2024-10-23", "Ataque armado contra su sede en Ankara.")], [("Turkish Aerospace (Wikipedia)", W + "Turkish_Aerospace")]),
}

RELACIONES = [
 ("nestle", "cargill", "Abastecimiento", "Compra granos y cacao a las grandes comercializadoras.", 1),
 ("roche", "novartis", "Enfrentamiento", "Las dos grandes farmacéuticas de Basilea compiten en oncología.", 1),
 ("novartis", "pfizer", "Enfrentamiento", "Compiten en el mercado farmacéutico mundial.", 1),
 ("mercuria", "vitol", "Enfrentamiento", "Compiten en el comercio de petróleo.", 1),
 ("mercuria", "trafigura", "Enfrentamiento", "Compiten en el comercio de energía y metales.", 1),
 ("astrazeneca", "casablanca", "Ambigua", "Anunció en 2025 inversiones en EE.UU. ante la amenaza de aranceles a los medicamentos.", 1),
 ("amundi", "blackrock", "Enfrentamiento", "La mayor gestora europea compite con la estadounidense.", 1),
 ("socgen", "doj", "Enfrentamiento", "Acuerdo de 2018 por sobornos en Libia y la tasa Libor.", 1),
 ("afp", "xinhua", "Enfrentamiento", "Compiten como agencias globales de noticias.", 1),
 ("indra", "sanchez", "Alianza", "El Estado es su mayor accionista y le adjudica los programas de defensa.", 2),
 ("acs", "sanchez", "Ambigua", "Gran contratista de obra pública en España.", 1),
 ("aise", "cia", "Alianza", "Cooperación de inteligencia en la OTAN.", 1),
 ("nexperia", "jetten", "Ambigua", "El gobierno neerlandés la intervino en 2025 y suspendió la intervención en noviembre.", 2),
 ("nexperia", "mofcom", "Enfrentamiento", "China bloqueó en 2025 las exportaciones de sus chips.", 2),
 ("otp", "tisza", "Ambigua", "El mayor banco del país ante el nuevo gobierno.", 1),
 ("chp", "erdogan", "Enfrentamiento", "Su candidato presidencial está preso y juzgado desde 2025.", 3),
 ("chp", "akp", "Enfrentamiento", "Principal oposición al partido de gobierno.", 2),
 ("diyanet", "akp", "Alianza", "Su agenda religiosa acompaña la del partido de gobierno.", 2),
 ("aselsan", "erdogan", "Alianza", "Pieza central de la industria de defensa que impulsa el gobierno.", 2),
 ("tai", "baykar", "Enfrentamiento", "Compiten en drones militares.", 1),
 ("tai", "erdogan", "Alianza", "Desarrolla el caza KAAN, proyecto estrella del gobierno.", 2),
]
