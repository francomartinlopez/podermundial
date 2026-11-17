# Cuarta tanda (17 de noviembre de 2026): 22 actores no estatales en países que tenían un solo actor,
# priorizados por su peso real (energía y tránsito ruso en Europa, puertos, 5G, bancos expuestos a Rusia,
# grupos armados de Siria y Yemen, iglesias y organizaciones sociales de masas).
W = "https://en.wikipedia.org/wiki/"

NUCLEO4 = [
 ("vingroup", "Vingroup (Phạm Nhật Vượng)", "Empresa industrial", "Hanói, Vietnam", "P", 2, "12111001120200012", "D", "", 2, "E"),
 ("ayala", "Ayala Corporation (familia Zobel de Ayala)", "Empresa industrial", "Makati, Filipinas", "T", 2, "02111001120200012", "D", "", 2, "C"),
 ("mol", "MOL (petróleo y gas de Hungría)", "Recursos primarios", "Budapest, Hungría", "T", 2, "22110001121200011", "D", "", 2, "C"),
 ("eph", "EPH (Daniel Křetínský)", "Recursos primarios", "Praga, Chequia", "T", 2, "21110001121200012", "D", "", 2, "E"),
 ("nokia", "Nokia", "Empresa tecnológica", "Espoo, Finlandia", "T", 2, "01120002221002002", "D", "", 2, "C"),
 ("brac", "BRAC", "ONG, fundación o think tank", "Daca, Bangladés", "X", 2, "01213010010000001", "D", "", 2, "C"),
 ("eotc", "Iglesia Ortodoxa Etíope Tewahedo", "Organización religiosa", "Adís Abeba, Etiopía", "P", 2, "00312010020000000", "D", "", 2, "C"),
 ("abl", "Asociación de Bancos del Líbano", "Federación empresaria", "Beirut, Líbano", "P", 2, "02010000110000001", "D", "", 2, "D"),
 ("sdf", "Fuerzas Democráticas Sirias (FDS)", "Paramilitar", "Al Hasaka, Siria", "T", 2, "10201210110021000", "D", "", 1, "C"),
 ("unrwa", "UNRWA (agencia de la ONU para los refugiados palestinos)", "Institución mundial", "Gaza, Palestina", "X", 2, "01111010010010000", "D", "", 3, "D"),
 ("stc", "Consejo de Transición del Sur (Yemen)", "Paramilitar", "Adén, Yemen", "P", 3, "10201210110021010", "D", "alnahyan", 1, "E"),
 ("ckh", "CK Hutchison (familia Li Ka-shing)", "Logística y transporte", "Hong Kong", "P", 2, "12111001221210022", "D", "", 2, "C"),
 ("arcelormittal", "ArcelorMittal (familia Mittal)", "Empresa industrial", "Luxemburgo", "T", 2, "22111001121200012", "D", "", 2, "C"),
 ("raiffeisen", "Raiffeisen Bank International", "Empresa financiera", "Viena, Austria", "T", 2, "02110000221000002", "D", "", 2, "C"),
 ("cenco", "CENCO (Conferencia Episcopal del Congo)", "Organización religiosa", "Kinsasa, República Democrática del Congo", "X", 3, "00213010020000000", "D", "santasede", 2, "C"),
 ("nis", "NIS (Industria Petrolera de Serbia)", "Recursos primarios", "Novi Sad, Serbia", "E", 3, "21110000111200011", "D", "gazprom", 2, "C"),
 ("ryanair", "Ryanair", "Logística y transporte", "Dublín, Irlanda", "T", 2, "01110001120100012", "D", "", 2, "C"),
 ("radiomaryja", "Radio Maryja (Tadeusz Rydzyk)", "Medio de comunicación", "Toruń, Polonia", "T", 2, "00012020010000000", "D", "", 2, "C"),
 ("edp", "EDP (Energías de Portugal)", "Recursos primarios", "Lisboa, Portugal", "T", 2, "21110001121200012", "D", "", 2, "C"),
 ("ugtt", "UGTT (Unión General Tunecina del Trabajo)", "Sindicato", "Túnez, Túnez", "P", 2, "01211010120000111", "D", "", 2, "C"),
 ("inc", "Iglesia ni Cristo", "Organización religiosa", "Ciudad Quezón, Filipinas", "T", 2, "00312010020000000", "D", "", 2, "E"),
 ("fredriksen", "John Fredriksen (Seatankers)", "Empresario", "Limasol, Chipre", "T", 2, "12010000120000032", "D", "", 2, "C"),
]
assert all(len(n[6]) == 17 for n in NUCLEO4), [n[0] for n in NUCLEO4 if len(n[6]) != 17]

ALC_G = {"ckh", "arcelormittal", "nokia", "fredriksen"}
ALC_R = {"brac", "unrwa", "raiffeisen", "eph", "mol", "edp", "nis", "ryanair", "vingroup"}
COH = {"stc": 1, "sdf": 2, "eotc": 1, "abl": 2}
APO = {"brac": 2, "eotc": 2, "inc": 2, "ugtt": 2, "radiomaryja": 1, "abl": 0, "sdf": 1}
PRI = {"unrwa": 1}

COORDS = {
 "Hanói, Vietnam": (105.85, 21.03), "Makati, Filipinas": (121.02, 14.55), "Budapest, Hungría": (19.04, 47.5),
 "Praga, Chequia": (14.42, 50.08), "Espoo, Finlandia": (24.66, 60.21), "Daca, Bangladés": (90.41, 23.81),
 "Adís Abeba, Etiopía": (38.75, 9.03), "Al Hasaka, Siria": (40.75, 36.5), "Gaza, Palestina": (34.47, 31.5),
 "Adén, Yemen": (45.03, 12.79), "Kinsasa, República Democrática del Congo": (15.27, -4.32), "Novi Sad, Serbia": (19.83, 45.27),
 "Dublín, Irlanda": (-6.26, 53.35), "Toruń, Polonia": (18.6, 53.01), "Lisboa, Portugal": (-9.14, 38.72),
 "Túnez, Túnez": (10.18, 36.81), "Ciudad Quezón, Filipinas": (121.04, 14.68), "Limasol, Chipre": (33.04, 34.68),
 # actores sin sede fija: se ubican en el mapa en su lugar de origen o de reunión, sin asignarles país
 "Sin sede fija (secretaría en Leiden, Países Bajos)": (4.49, 52.16), "Sin sede central (origen en Egipto)": (31.24, 30.04),
 "Sin sede fija": (40.1, 35.3),
}

EXT = {}

RELACIONES = [
 ("goldman", "tesoro_eeuu", "Puerta giratoria", "Henry Paulson y Steven Mnuchin pasaron de Goldman Sachs a secretarios del Tesoro.", 2),
 ("sap", "microsoft", "Alianza", "Acuerdo para llevar los sistemas de gestión de SAP a la nube de Microsoft.", 1),
 ("doj", "glencore", "Enfrentamiento", "Glencore se declaró culpable en 2022 de sobornos y manipulación de mercados ante la justicia de EE.UU.", 2),
 ("doj", "vitol", "Enfrentamiento", "Vitol pagó 135 millones de dólares en 2020 para cerrar causas por sobornos en Ecuador, México y Brasil.", 2),
 ("doj", "trafigura", "Enfrentamiento", "Trafigura se declaró culpable en 2024 de sobornar a funcionarios de Petrobras.", 2),
 ("spglobal", "moodys", "Ambigua", "Comparten con Fitch el oligopolio de las calificaciones de deuda.", 1),
 ("comisioneu", "pfizer", "Contrato", "Contratos de vacunas contra el COVID-19 con la Unión Europea.", 2),
 ("bae", "ffaa_reinounido", "Abastecimiento", "Principal proveedor de las fuerzas armadas británicas.", 3),
 ("bae", "saud", "Contrato", "Contratos de aviones de combate desde el acuerdo Al Yamamah de 1985.", 2),
 ("fed", "bpi", "Propiedad", "Los bancos centrales son los accionistas del Banco de Pagos Internacionales y forman su consejo.", 2),
 ("bce", "bpi", "Propiedad", "Los bancos centrales son los accionistas del Banco de Pagos Internacionales y forman su consejo.", 2),
 ("lilly", "novo_fundacion", "Enfrentamiento", "Compiten por el mercado mundial de los medicamentos contra la obesidad y la diabetes.", 2),
 ("statestreet", "blackrock", "Ambigua", "Junto con Vanguard, los tres grandes fondos indexados que votan en casi todas las grandes empresas.", 1),
 ("pcv", "vingroup", "Ambigua", "El mayor grupo privado de Vietnam creció bajo el sistema de partido único.", 1),
 ("lukoil", "mol", "Abastecimiento", "Crudo ruso por el oleoducto Druzhba; desde 2024 MOL toma la propiedad en la frontera por las sanciones ucranianas a Lukoil.", 2),
 ("gazprom", "eph", "Contrato", "EPH controla Eustream, por donde pasó el gas ruso hacia Europa hasta que Ucrania cortó el tránsito en 2025.", 1),
 ("nokia", "huawei", "Enfrentamiento", "Compiten por las redes 5G; Europa reemplaza equipos de Huawei por Nokia y Ericsson.", 2),
 ("nvidia", "nokia", "Financiamiento", "Nvidia invirtió 1.000 millones de dólares en Nokia en 2025 para redes con inteligencia artificial.", 2),
 ("gates", "brac", "Financiamiento", "La Fundación Gates financia programas de BRAC.", 1),
 ("eotc", "prosperidad", "Ambigua", "Choque con el gobierno en 2023 por el sínodo cismático de Oromía.", 2),
 ("abl", "fmi", "Enfrentamiento", "Los bancos resistieron el plan de reestructuración que exigía el FMI tras el colapso de 2019.", 1),
 ("pentagono", "sdf", "Alianza", "Aliadas de EE.UU. contra el Estado Islámico desde 2015.", 3),
 ("tsk", "sdf", "Enfrentamiento", "Turquía las considera una extensión del PKK y las combate en el norte de Siria.", 3),
 ("sharaa", "sdf", "Ambigua", "Acuerdo de marzo de 2025 para integrarlas a las instituciones del Estado sirio.", 2),
 ("sdf", "isis", "Enfrentamiento", "Lo derrotaron en Raqqa y Baghuz y custodian a miles de sus presos.", 3),
 ("fdi", "unrwa", "Enfrentamiento", "Israel prohibió sus operaciones por ley desde enero de 2025.", 3),
 ("alnahyan", "stc", "Financiamiento", "Emiratos arma y financia al Consejo de Transición del Sur.", 3),
 ("stc", "hutis", "Enfrentamiento", "Guerra en Yemen.", 2),
 ("saud", "stc", "Ambigua", "Integra el Consejo de Liderazgo Presidencial que Riad armó en 2022, pero busca la independencia del sur.", 2),
 ("ckh", "blackrock", "Contrato", "Acordó en 2025 venderle sus puertos fuera de China a un consorcio de BlackRock y MSC.", 2),
 ("pcch", "ckh", "Ambigua", "Pekín cuestionó la venta de los puertos a un consorcio estadounidense.", 2),
 ("bce", "raiffeisen", "Enfrentamiento", "El BCE le exigió reducir su negocio en Rusia, donde es el mayor banco occidental que sigue operando.", 2),
 ("cenco", "m23", "Ambigua", "Las iglesias se reunieron con el M23 en 2025 en su iniciativa de pacto social por la paz.", 1),
 ("tesoro_eeuu", "nis", "Enfrentamiento", "Sanciones de EE.UU. por su propiedad rusa, vigentes desde octubre de 2025.", 2),
 ("sns", "nis", "Ambigua", "El gobierno serbio negocia para que los dueños rusos vendan y la refinería vuelva a operar.", 2),
 ("pcch", "edp", "Propiedad", "China Three Gorges, estatal china, es su mayor accionista desde la privatización de 2011.", 2),
 ("saied", "ugtt", "Enfrentamiento", "El sindicato se opone al gobierno por decreto de Saied.", 2),
]

FICHAS = {
"vingroup": dict(res=["El mayor grupo privado de Vietnam: inmuebles, autos eléctricos (VinFast), hoteles, salud y educación. Su fundador, Phạm Nhật Vượng, es el hombre más rico del país."], manda=["Phạm Nhật Vượng y su familia."], dinero="Desarrollo inmobiliario y crédito de la banca vietnamita.", crono=[("1993", "Nace en Ucrania como Technocom, una fábrica de fideos instantáneos."), ("2023-08", "VinFast empieza a cotizar en Nasdaq.")], fuentes=[("Vingroup (Wikipedia)", W + "Vingroup")]),
"ayala": dict(res=["El conglomerado más antiguo de Filipinas, de la familia Zobel de Ayala: bancos (BPI), telecomunicaciones (Globe), inmuebles (Ayala Land) y energía."], manda=["La familia Zobel de Ayala."], dinero="Inmuebles, banca y telecomunicaciones.", crono=[("1834", "Fundación.")], fuentes=[("Ayala Corporation (Wikipedia)", W + "Ayala_Corporation")]),
"mol": dict(res=["La mayor petrolera de Europa central: refina en Hungría y Eslovaquia crudo ruso que llega por el oleoducto Druzhba, exceptuado del embargo europeo de 2022."], manda=["Su directorio, con el Estado húngaro como accionista."], dinero="Refinación y estaciones de servicio en Europa central.", crono=[("1991", "Creación."), ("2022-06", "La UE exceptúa del embargo el crudo ruso por oleoducto.")], fuentes=[("MOL Group (Wikipedia)", W + "MOL_Group"), ("Druzhba pipeline (Wikipedia)", W + "Druzhba_pipeline")]),
"eph": dict(res=["Grupo energético de Daniel Křetínský: gasoductos de tránsito, centrales eléctricas en varios países europeos y participaciones en el acero de thyssenkrupp y en el correo británico."], manda=["Daniel Křetínský."], dinero="Transporte de gas y generación eléctrica.", crono=[("2009", "Fundación."), ("2025-01", "Termina el tránsito de gas ruso por Ucrania y Eslovaquia.")], fuentes=[("Energetický a průmyslový holding (Wikipedia)", W + "Energetick%C3%BD_a_pr%C5%AFmyslov%C3%BD_holding")]),
"nokia": dict(res=["Uno de los tres grandes fabricantes de redes 5G del mundo junto con Ericsson y Huawei; la alternativa occidental en infraestructura de telecomunicaciones."], manda=["Su directorio."], dinero="Equipos de redes móviles y de fibra.", crono=[("1865", "Fundación."), ("2025-10", "Nvidia compra el 2,9 % por 1.000 millones de dólares.")], fuentes=[("Nokia (Wikipedia)", W + "Nokia"), ("Nvidia invests $1 billion in Nokia (Broadband Breakfast)", "https://broadbandbreakfast.com/nvidia-invests-1-billion-in-nokia/")]),
"brac": dict(res=["La organización no gubernamental más grande del mundo por personal y beneficiarios: microcréditos, escuelas y salud en Bangladés y en países de Asia y África."], manda=["Su consejo directivo."], dinero="Microfinanzas, empresas sociales y donantes internacionales.", crono=[("1972", "La funda Fazle Hasan Abed tras la independencia de Bangladés.")], fuentes=[("BRAC (organisation) (Wikipedia)", W + "BRAC_(organisation)")]),
"eotc": dict(res=["La iglesia de cerca de la mitad de la población de Etiopía, con un peso social y político enorme; en 2023 enfrentó un cisma en Oromía y choques con el gobierno."], manda=["Su patriarca y el Santo Sínodo."], dinero="Tierras, templos y aportes de los fieles.", crono=[("2023-01", "Cisma del sínodo de Oromía.")], fuentes=[("Ethiopian Orthodox Tewahedo Church (Wikipedia)", W + "Ethiopian_Orthodox_Tewahedo_Church")]),
"abl": dict(res=["Agrupa a los bancos libaneses, que congelaron los depósitos en dólares tras el colapso financiero de 2019 y resistieron los planes de reestructuración que ponían las pérdidas a su cargo."], manda=["Los grandes bancos del país."], dinero="El sistema bancario libanés.", crono=[("2019-10", "Empieza la crisis financiera y se congelan los depósitos."), ("2020-03", "El Líbano entra en default.")], fuentes=[("Lebanese liquidity crisis (Wikipedia)", W + "Lebanese_liquidity_crisis")]),
"sdf": dict(res=["Alianza armada liderada por kurdos que controla el noreste de Siria, aliada de EE.UU. contra el Estado Islámico; en 2025 firmó un acuerdo para integrarse al nuevo Estado sirio."], manda=["Su comandante, Mazloum Abdi."], dinero="Petróleo del noreste sirio y apoyo de EE.UU.", crono=[("2015-10", "Fundación."), ("2019-03", "Toma Baghuz, el último bastión del Estado Islámico."), ("2025-03", "Acuerdo de integración con el gobierno de al-Sharaa.")], fuentes=[("Syrian Democratic Forces (Wikipedia)", W + "Syrian_Democratic_Forces")]),
"unrwa": dict(res=["Agencia de la ONU que desde 1949 da escuelas, salud y ayuda a unos seis millones de refugiados palestinos; en Gaza es la principal red de servicios. Israel prohibió sus operaciones por ley desde 2025, tras acusar a empleados de participar en el ataque del 7 de octubre; una investigación de la ONU concluyó que nueve podrían haber participado y fueron despedidos."], manda=["Su comisionado general, designado por el secretario general de la ONU."], dinero="Aportes voluntarios de los Estados.", crono=[("1949-12", "Creación."), ("2024-08", "La ONU despide a nueve empleados tras su investigación."), ("2025-01", "Entra en vigor la prohibición israelí.")], fuentes=[("UNRWA (Wikipedia)", W + "UNRWA"), ("UNRWA and Israel (Wikipedia)", W + "UNRWA_and_Israel")]),
"stc": dict(res=["Movimiento que busca la independencia del sur de Yemen y controla Adén con fuerzas armadas y financiadas por Emiratos; integra a la vez el consejo de gobierno que reconoce la ONU."], manda=["Aidarus al-Zoubaidi."], dinero="Apoyo emiratí y control del puerto de Adén.", crono=[("2017-05", "Fundación."), ("2022-04", "Entra al Consejo de Liderazgo Presidencial.")], fuentes=[("Southern Transitional Council (Wikipedia)", W + "Southern_Transitional_Council")]),
"ckh": dict(res=["Conglomerado de Hong Kong con uno de los mayores operadores portuarios del mundo, telecomunicaciones y comercio minorista en decenas de países; su venta de puertos en 2025, incluidos los de Panamá, enfrentó a Washington y Pekín."], manda=["La familia Li Ka-shing."], dinero="Puertos, telefonía, comercio e infraestructura.", crono=[("2015", "Reorganización del grupo de Li Ka-shing."), ("2025-03", "Acuerda vender sus puertos fuera de China a BlackRock y MSC.")], fuentes=[("CK Hutchison Holdings (Wikipedia)", W + "CK_Hutchison_Holdings")]),
"arcelormittal": dict(res=["Una de las mayores siderúrgicas del mundo, con plantas en Europa, América, India y Ucrania."], manda=["La familia Mittal."], dinero="Acero para autos, construcción e industria.", crono=[("2006", "Fusión de Mittal Steel y Arcelor.")], fuentes=[("ArcelorMittal (Wikipedia)", W + "ArcelorMittal")]),
"raiffeisen": dict(res=["Banco austríaco con fuerte presencia en Europa del Este; es el mayor banco occidental que sigue operando en Rusia, lo que le valió la presión del BCE y de EE.UU."], manda=["Los bancos regionales Raiffeisen de Austria, sus accionistas de control."], dinero="Banca en Europa central y oriental.", crono=[("2022-02", "Sigue en Rusia tras la invasión de Ucrania.")], fuentes=[("Raiffeisen Bank International (Wikipedia)", W + "Raiffeisen_Bank_International")]),
"cenco": dict(res=["La conferencia de obispos católicos del Congo, uno de los actores civiles más influyentes del país: medió el acuerdo político de 2016, observa las elecciones y en 2025 impulsó con las iglesias protestantes un pacto social por la paz."], manda=["Sus obispos."], dinero="Red de parroquias, escuelas y hospitales.", crono=[("2016-12", "Media el acuerdo de San Silvestre."), ("2025-02", "Se reúne con el M23 en Goma.")], fuentes=[("Catholic Church in the Democratic Republic of the Congo (Wikipedia)", W + "Catholic_Church_in_the_Democratic_Republic_of_the_Congo"), ("Catholic bishops in DR Congo meet rebel group (ACI Africa)", "https://aciafrica.org/news/14253/catholic-bishops-in-dr-congo-meet-rebel-group-to-push-for-peace-amid-political-opposition")]),
"nis": dict(res=["La petrolera de Serbia, controlada por Gazprom Neft y Gazprom; dueña de la única refinería del país, que quedó afectada por las sanciones de EE.UU. a sus dueños rusos."], manda=["Gazprom Neft, su accionista principal."], dinero="Refinación y estaciones de servicio en Serbia.", crono=[("2008", "Gazprom Neft compra la mayoría."), ("2025-01", "EE.UU. la incluye en su lista de sanciones."), ("2025-10-09", "Entran en vigor las sanciones; Croacia corta el envío de crudo."), ("2025-11-25", "Se suspende el procesamiento en la refinería de Pančevo.")], fuentes=[("Naftna Industrija Srbije (Wikipedia)", W + "Naftna_Industrija_Srbije"), ("US sanctions on Serbian oil company NIS take effect (bne IntelliNews)", "https://www.intellinews.com/us-sanctions-on-serbian-oil-company-nis-take-effect-405546/")]),
"ryanair": dict(res=["La aerolínea que más pasajeros transporta en Europa."], manda=["Michael O'Leary y su directorio."], dinero="Vuelos de bajo costo.", crono=[("1984", "Fundación.")], fuentes=[("Ryanair (Wikipedia)", W + "Ryanair")]),
"radiomaryja": dict(res=["Radio católica y nacionalista fundada por el sacerdote Tadeusz Rydzyk, con un público fiel que pesa en la política polaca de derecha."], manda=["Tadeusz Rydzyk."], dinero="Donaciones de su audiencia y fundaciones propias.", crono=[("1991-12", "Fundación en Toruń.")], fuentes=[("Radio Maryja (Wikipedia)", W + "Radio_Maryja")]),
"edp": dict(res=["La mayor eléctrica de Portugal y una de las grandes en energías renovables del mundo; la estatal China Three Gorges es su mayor accionista."], manda=["Su directorio y sus accionistas, con China Three Gorges a la cabeza."], dinero="Generación y distribución eléctrica.", crono=[("2011-12", "China Three Gorges compra la participación del Estado portugués.")], fuentes=[("EDP Group (Wikipedia)", W + "EDP_Group")]),
"ugtt": dict(res=["La central sindical de Túnez, el mayor actor organizado del país fuera del Estado; recibió el Nobel de la Paz en 2015 por mediar la transición y se enfrenta al gobierno de Kais Saied."], manda=["Su secretario general y su comisión ejecutiva."], dinero="Cuotas de cientos de miles de afiliados.", crono=[("1946", "Fundación."), ("2015-10", "Nobel de la Paz junto al cuarteto del diálogo nacional.")], fuentes=[("Tunisian General Labour Union (Wikipedia)", W + "Tunisian_General_Labour_Union")]),
"inc": dict(res=["Iglesia filipina con millones de fieles que vota en bloque según indica su liderazgo, lo que la vuelve codiciada en cada elección."], manda=["Su ministro ejecutivo, Eduardo Manalo."], dinero="Diezmos de sus fieles.", crono=[("1914", "Fundación por Felix Manalo.")], fuentes=[("Iglesia ni Cristo (Wikipedia)", W + "Iglesia_ni_Cristo")]),
"fredriksen": dict(res=["Armador de origen noruego con ciudadanía chipriota, dueño de una de las mayores flotas de petroleros y graneleros del mundo (Frontline, Golden Ocean) y de empresas de perforación."], manda=["John Fredriksen y su familia."], dinero="Transporte marítimo de petróleo y materias primas.", crono=[("1985", "Funda Frontline.")], fuentes=[("John Fredriksen (Wikipedia)", W + "John_Fredriksen")]),
}
assert set(FICHAS) == {n[0] for n in NUCLEO4}
