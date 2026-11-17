# Datos base del Mapa del Poder Global: organizaciones, puntajes y relaciones.
# Puntajes editoriales iniciales (2026-11-16), a revisar ficha por ficha.

EJES = [
    ("rec", "Recursos naturales", "Materia", "Posesión o control directo de tierra, energía, minerales, agua o alimentos."),
    ("cap", "Capital físico", "Materia", "Propiedad de infraestructura, plantas, equipos, flotas, centros de datos."),
    ("prd", "Producción material", "Materia", "Volumen y peso estratégico de lo que fabrica o extrae."),
    ("mov", "Movilidad y transporte", "Materia", "Capacidad de mover bienes, personas o fuerzas a escala."),
    ("gan", "Generación de ganancia", "Dinero", "Flujo anual de excedente económico propio."),
    ("din", "Dinero neto", "Dinero", "Stock de riqueza, activos administrados o capacidad de emitir."),
    ("coe", "Coerción violenta", "Fuerza", "Capacidad propia de usar o amenazar con violencia organizada."),
    ("ter", "Dominio territorial", "Fuerza", "Control efectivo de un territorio y su población."),
    ("adq", "Adquisición de información", "Información", "Capacidad de obtener datos, secretos o vigilancia."),
    ("pro", "Procesamiento de información", "Información", "Capacidad de analizar y convertir datos en decisiones."),
    ("mod", "Moderación de información", "Información", "Poder de decidir qué circula, qué se amplifica y qué se calla."),
    ("con", "Conocimiento", "Información", "Saber experto acumulado, técnico o institucional."),
    ("inn", "Innovación", "Información", "Capacidad de crear tecnología, métodos o productos nuevos."),
    ("mie", "Miembros humanos", "Personas", "Cantidad de personas que integran, obedecen o siguen a la organización."),
    ("cul", "Influencia cultural", "Personas", "Capacidad de moldear ideas, creencias, gustos o identidades."),
    ("red", "Contactos y relaciones", "Personas", "Densidad y altura de su red con otros centros de poder."),
    ("reg", "Regulación normativa", "Norma", "Capacidad de dictar o imponer reglas que otros deben cumplir."),
]
# Orden en que vienen los 17 dígitos de cada organización (orden de la propuesta original):
ORDEN_ENTRADA = ["rec", "cap", "mie", "con", "cul", "coe", "mod", "inn", "gan", "red", "pro", "prd", "ter", "adq", "reg", "mov", "din"]

AREA_TIPO = {
    "Gobierno": "Estado", "Ejército": "Estado", "Fuerza de seguridad": "Estado", "Servicio de inteligencia": "Estado",
    "Banco central": "Estado", "Justicia": "Estado", "Partido político": "Estado",
    "Institución mundial": "Supranacional", "Estandarización e infraestructura técnica": "Supranacional",
    "Empresa financiera": "Capital", "Empresa tecnológica": "Capital", "Recursos primarios": "Capital",
    "Empresa de armamento": "Capital", "Empresa industrial": "Capital", "Logística y transporte": "Capital",
    "Familia y oficina patrimonial": "Capital",
    "Red social": "Información", "Medio de comunicación": "Información", "Institución de conocimiento": "Información",
    "ONG, fundación o think tank": "Influencia", "Organización religiosa": "Influencia", "Organización deportiva": "Influencia",
    "Organización reservada": "Sombra", "Organización criminal": "Sombra", "Paramilitar": "Sombra",
}

BLOQUES = {
    "T": "Transoceánico", "E": "Euroasiático", "I": "Independiente", "P": "Pendular", "X": "Transnacional",
}
AUTONOMIA = {1: "Decide solo", 2: "Aliado con criterio propio", 3: "Subordinado", 4: "Fachada"}
CERTEZA = {"D": "Documentado", "E": "Estimado", "S": "Especulativo"}

# id, nombre, área, sede, bloque, autonomía, puntajes (orden de entrada), certeza, depende de (ids)
ORGS = [
    # Gobiernos
    ("casablanca", "Casa Blanca (Poder Ejecutivo de EE.UU.)", "Gobierno", "Washington, EE.UU.", "T", 1, "22223221032032312", "D", ""),
    ("kremlin", "Kremlin (Administración Presidencial de Rusia)", "Gobierno", "Moscú, Rusia", "E", 1, "21111220021032211", "D", ""),
    ("consejoestado", "Consejo de Estado de China", "Gobierno", "Pekín, China", "E", 3, "23321122122222222", "D", "pcch"),
    ("lider_iran", "Oficina del Líder Supremo de Irán", "Gobierno", "Teherán, Irán", "E", 1, "11212220121121211", "E", ""),
    ("pm_israel", "Oficina del Primer Ministro de Israel", "Gobierno", "Jerusalén, Israel", "T", 2, "01122121021012211", "D", ""),
    ("comisioneu", "Comisión Europea", "Gobierno", "Bruselas, Bélgica", "T", 2, "01122021031011311", "D", ""),
    ("gob_india", "Gobierno de la India (Oficina del Primer Ministro)", "Gobierno", "Nueva Delhi, India", "I", 1, "22212221021122221", "D", ""),
    # Ejércitos
    ("pentagono", "Pentágono (Departamento de Guerra de EE.UU.)", "Ejército", "Arlington, EE.UU.", "T", 2, "13332313033123131", "D", "casablanca"),
    ("epl", "Ejército Popular de Liberación", "Ejército", "Pekín, China", "E", 3, "03321312112122021", "D", "pcch"),
    ("ffaa_rusia", "Fuerzas Armadas de Rusia", "Ejército", "Moscú, Rusia", "E", 3, "02311311011122020", "D", "kremlin"),
    ("fdi", "Fuerzas de Defensa de Israel", "Ejército", "Tel Aviv, Israel", "T", 2, "02221222022122120", "D", "pm_israel"),
    ("ejercito_pak", "Ejército de Pakistán", "Ejército", "Rawalpindi, Pakistán", "P", 2, "12211220121122211", "D", ""),
    # Fuerzas de seguridad
    ("cgri", "Cuerpo de la Guardia Revolucionaria Islámica", "Fuerza de seguridad", "Teherán, Irán", "E", 2, "12212221121122111", "D", "lider_iran"),
    ("fsb", "FSB (Servicio Federal de Seguridad de Rusia)", "Fuerza de seguridad", "Moscú, Rusia", "E", 2, "01221221122022211", "D", "kremlin"),
    ("mps_china", "Ministerio de Seguridad Pública de China", "Fuerza de seguridad", "Pekín, China", "E", 3, "02321332013023211", "D", "pcch"),
    ("dhs", "Departamento de Seguridad Nacional de EE.UU.", "Fuerza de seguridad", "Washington, EE.UU.", "T", 3, "02311221012023220", "D", "casablanca"),
    # Inteligencia
    ("cia", "CIA (Agencia Central de Inteligencia)", "Servicio de inteligencia", "Langley, EE.UU.", "T", 2, "01232222033013011", "D", "casablanca"),
    ("nsa", "NSA (Agencia de Seguridad Nacional)", "Servicio de inteligencia", "Fort Meade, EE.UU.", "T", 2, "02230023023003000", "D", "pentagono"),
    ("mss", "MSS (Ministerio de Seguridad del Estado de China)", "Servicio de inteligencia", "Pekín, China", "E", 3, "01221222022023000", "D", "pcch"),
    ("gru", "GRU (inteligencia militar rusa)", "Servicio de inteligencia", "Moscú, Rusia", "E", 3, "01120221012012000", "E", "ffaa_rusia"),
    ("mossad", "Mossad", "Servicio de inteligencia", "Tel Aviv, Israel", "T", 2, "00121212022002010", "E", "pm_israel"),
    ("isi", "ISI (Inteligencia Interservicios de Pakistán)", "Servicio de inteligencia", "Islamabad, Pakistán", "P", 3, "01121220021012000", "E", "ejercito_pak"),
    # Bancos centrales
    ("fed", "Reserva Federal de EE.UU.", "Banco central", "Washington, EE.UU.", "T", 2, "00131011132002303", "D", ""),
    ("bce", "Banco Central Europeo", "Banco central", "Fráncfort, Alemania", "T", 2, "00121011121002303", "D", ""),
    ("pboc", "Banco Popular de China", "Banco central", "Pekín, China", "E", 3, "00120011121002303", "D", "pcch"),
    ("boj", "Banco de Japón", "Banco central", "Tokio, Japón", "T", 2, "00120001111001203", "D", ""),
    ("bpi", "Banco de Pagos Internacionales", "Banco central", "Basilea, Suiza", "X", 2, "00030011131002202", "D", ""),
    # Justicia
    ("scotus", "Corte Suprema de EE.UU.", "Justicia", "Washington, EE.UU.", "T", 1, "00022010010000300", "D", ""),
    ("doj", "Departamento de Justicia de EE.UU. (con el FBI)", "Justicia", "Washington, EE.UU.", "T", 3, "01221221022013210", "D", "casablanca"),
    ("tjue", "Tribunal de Justicia de la Unión Europea", "Justicia", "Luxemburgo", "T", 2, "00021010010000300", "D", ""),
    ("cpi", "Corte Penal Internacional", "Justicia", "La Haya, Países Bajos", "X", 3, "00011000010001100", "D", ""),
    # Partidos
    ("pcch", "Partido Comunista de China", "Partido político", "Pekín, China", "E", 1, "12322231032133311", "D", ""),
    ("gop", "Partido Republicano de EE.UU.", "Partido político", "Washington, EE.UU.", "T", 2, "00212010031001101", "D", ""),
    ("dem", "Partido Demócrata de EE.UU.", "Partido político", "Washington, EE.UU.", "T", 2, "00212010031001101", "D", ""),
    ("bjp", "BJP (Partido Popular Indio) y RSS", "Partido político", "Nueva Delhi, India", "I", 1, "00313120021002101", "D", ""),
    # Instituciones mundiales
    ("csonu", "Consejo de Seguridad de la ONU", "Institución mundial", "Nueva York, EE.UU.", "X", 3, "00012100031001200", "D", "casablanca,kremlin,pcch"),
    ("fmi", "Fondo Monetario Internacional", "Institución mundial", "Washington, EE.UU.", "T", 3, "00031010132002302", "D", "casablanca"),
    ("bm", "Banco Mundial", "Institución mundial", "Washington, EE.UU.", "T", 3, "00131011132002202", "D", "casablanca"),
    ("otan", "OTAN", "Institución mundial", "Bruselas, Bélgica", "T", 3, "02222312032012120", "D", "pentagono"),
    ("oms", "Organización Mundial de la Salud", "Institución mundial", "Ginebra, Suiza", "X", 3, "00122021031002200", "D", "gates"),
    ("brics", "BRICS y Nuevo Banco de Desarrollo", "Institución mundial", "Shanghái, China", "P", 2, "00011000020000101", "D", ""),
    # Estandarización e infraestructura técnica
    ("icann", "ICANN", "Estandarización e infraestructura técnica", "Los Ángeles, EE.UU.", "T", 2, "00020021022001300", "D", ""),
    ("iso", "ISO (Organización Internacional de Normalización)", "Estandarización e infraestructura técnica", "Ginebra, Suiza", "X", 2, "00131001030001300", "D", ""),
    ("swift", "SWIFT", "Estandarización e infraestructura técnica", "La Hulpe, Bélgica", "T", 3, "00010020133003200", "D", "casablanca,comisioneu"),
    ("cips", "CIPS (Sistema de Pagos Interbancarios Transfronterizos)", "Estandarización e infraestructura técnica", "Shanghái, China", "E", 3, "00010010012002100", "D", "pboc"),
    # Financieras
    ("blackrock", "BlackRock", "Empresa financiera", "Nueva York, EE.UU.", "T", 2, "12131002333003103", "D", ""),
    ("vanguard", "Vanguard", "Empresa financiera", "Malvern, EE.UU.", "T", 2, "12120001221001003", "D", ""),
    ("jpmorgan", "JPMorgan Chase", "Empresa financiera", "Nueva York, EE.UU.", "T", 2, "01231012333003103", "D", ""),
    ("icbc", "ICBC (Banco Industrial y Comercial de China)", "Empresa financiera", "Pekín, China", "E", 3, "02310011322002003", "D", "pcch"),
    ("nbim", "Fondo soberano de Noruega (NBIM)", "Empresa financiera", "Oslo, Noruega", "T", 2, "01020000221001003", "D", ""),
    ("pif", "PIF (Fondo de Inversión Pública saudí)", "Empresa financiera", "Riad, Arabia Saudita", "P", 3, "12111001230101013", "D", "saud"),
    # Tecnológicas
    ("alphabet", "Alphabet (Google)", "Empresa tecnológica", "Mountain View, EE.UU.", "T", 2, "03233033333103113", "D", ""),
    ("microsoft", "Microsoft", "Empresa tecnológica", "Redmond, EE.UU.", "T", 2, "03232023333103103", "D", ""),
    ("amazon", "Amazon", "Empresa tecnológica", "Seattle, EE.UU.", "T", 2, "03332023333203133", "D", ""),
    ("nvidia", "Nvidia", "Empresa tecnológica", "Santa Clara, EE.UU.", "T", 2, "02131003332201103", "D", ""),
    ("tsmc", "TSMC", "Empresa tecnológica", "Hsinchu, Taiwán", "T", 2, "03230003321301103", "D", ""),
    ("asml", "ASML", "Empresa tecnológica", "Veldhoven, Países Bajos", "T", 3, "02130003221201102", "D", "casablanca"),
    ("huawei", "Huawei", "Empresa tecnológica", "Shenzhen, China", "E", 3, "02331013222202102", "E", "pcch"),
    ("palantir", "Palantir", "Empresa tecnológica", "Denver, EE.UU.", "T", 2, "01131023233003002", "D", ""),
    # Redes sociales
    ("meta", "Meta (Facebook, Instagram, WhatsApp)", "Red social", "Menlo Park, EE.UU.", "T", 2, "02233033333003103", "D", ""),
    ("x", "X (de SpaceX y xAI)", "Red social", "Bastrop, EE.UU.", "T", 3, "02123032132002002", "D", "spacex"),
    ("bytedance", "ByteDance (TikTok y Douyin)", "Red social", "Pekín, China", "E", 3, "02233033323003003", "D", "pcch"),
    ("tencent", "Tencent (WeChat)", "Red social", "Shenzhen, China", "E", 3, "02233033323003103", "D", "pcch"),
    # Medios
    ("reuters", "Thomson Reuters", "Medio de comunicación", "Toronto, Canadá", "T", 2, "01132021232003002", "D", ""),
    ("newscorp", "News Corp y Fox (familia Murdoch)", "Medio de comunicación", "Nueva York, EE.UU.", "T", 2, "01113020231002002", "D", ""),
    ("bbc", "BBC", "Medio de comunicación", "Londres, Reino Unido", "T", 2, "01123021121002001", "D", ""),
    ("xinhua", "Xinhua", "Medio de comunicación", "Pekín, China", "E", 3, "01122030021002000", "D", "pcch"),
    ("aljazeera", "Al Jazeera", "Medio de comunicación", "Doha, Catar", "P", 3, "01122020021002001", "D", ""),
    # Recursos primarios
    ("aramco", "Saudi Aramco", "Recursos primarios", "Dhahran, Arabia Saudita", "P", 3, "33220001321311013", "D", "saud"),
    ("gazprom", "Gazprom", "Recursos primarios", "San Petersburgo, Rusia", "E", 3, "33211100221311022", "D", "kremlin"),
    ("exxon", "ExxonMobil", "Recursos primarios", "Houston, EE.UU.", "T", 2, "33121002331311023", "D", ""),
    ("glencore", "Glencore", "Recursos primarios", "Baar, Suiza", "X", 2, "22210001231212032", "D", ""),
    ("cargill", "Cargill", "Recursos primarios", "Minnetonka, EE.UU.", "T", 2, "22210001221311032", "D", ""),
    # Armamento
    ("lockheed", "Lockheed Martin", "Empresa de armamento", "Bethesda, EE.UU.", "T", 2, "02231103231301012", "D", ""),
    ("rtx", "RTX (Raytheon)", "Empresa de armamento", "Arlington, EE.UU.", "T", 2, "02230103221301012", "D", ""),
    ("bae", "BAE Systems", "Empresa de armamento", "Londres, Reino Unido", "T", 2, "02220102221201011", "D", ""),
    ("rostec", "Rostec", "Empresa de armamento", "Moscú, Rusia", "E", 3, "12320101121301011", "D", "kremlin"),
    ("norinco", "NORINCO", "Empresa de armamento", "Pekín, China", "E", 3, "12320102121301011", "E", "consejoestado"),
    # Industriales
    ("samsung", "Grupo Samsung", "Empresa industrial", "Seúl, Corea del Sur", "T", 2, "03232003322302013", "D", ""),
    ("toyota", "Toyota", "Empresa industrial", "Toyota, Japón", "T", 2, "03321002321301033", "D", ""),
    ("siemens", "Siemens", "Empresa industrial", "Múnich, Alemania", "T", 2, "02330002222301012", "D", ""),
    ("catl", "CATL", "Empresa industrial", "Ningde, China", "E", 3, "13230003221301022", "D", "pcch"),
    ("spacex", "SpaceX (con xAI y Starlink)", "Empresa industrial", "Starbase, EE.UU.", "T", 2, "02132023232203033", "D", ""),
    # Logística
    ("msc", "MSC (Mediterranean Shipping Company)", "Logística y transporte", "Ginebra, Suiza", "X", 2, "03210001321001032", "D", ""),
    ("maersk", "Maersk", "Logística y transporte", "Copenhague, Dinamarca", "T", 2, "03220001221001032", "D", ""),
    ("cosco", "COSCO Shipping", "Logística y transporte", "Shanghái, China", "E", 3, "03210001221111032", "D", "consejoestado"),
    # ONG, fundaciones, think tanks
    ("gates", "Fundación Gates", "ONG, fundación o think tank", "Seattle, EE.UU.", "T", 2, "00122011031001103", "D", ""),
    ("osf", "Open Society Foundations", "ONG, fundación o think tank", "Nueva York, EE.UU.", "T", 2, "00122010031001102", "D", ""),
    ("wef", "Foro Económico Mundial (Davos)", "ONG, fundación o think tank", "Cologny, Suiza", "X", 2, "00122011031001101", "D", ""),
    ("cfr", "Council on Foreign Relations", "ONG, fundación o think tank", "Nueva York, EE.UU.", "T", 2, "00132010031001101", "D", ""),
    ("heritage", "Heritage Foundation", "ONG, fundación o think tank", "Washington, EE.UU.", "T", 2, "00122010031001201", "D", ""),
    ("rand", "RAND Corporation", "ONG, fundación o think tank", "Santa Mónica, EE.UU.", "T", 3, "00131002022002101", "D", "pentagono"),
    # Reservadas
    ("bilderberg", "Grupo Bilderberg", "Organización reservada", "Sin sede fija (secretaría en Leiden, Países Bajos)", "T", 2, "00020010030001000", "S", ""),
    ("trilateral", "Comisión Trilateral", "Organización reservada", "Washington, EE.UU.", "T", 2, "00020000030001000", "E", ""),
    ("ugle", "Gran Logia Unida de Inglaterra (masonería)", "Organización reservada", "Londres, Reino Unido", "T", 2, "11211000020000001", "S", ""),
    # Religiosas
    ("santasede", "Santa Sede", "Organización religiosa", "Ciudad del Vaticano", "X", 1, "12323010031121002", "D", ""),
    ("patriarcado", "Iglesia Ortodoxa Rusa (Patriarcado de Moscú)", "Organización religiosa", "Moscú, Rusia", "E", 3, "11312010020001001", "D", "kremlin"),
    ("opusdei", "Opus Dei", "Organización religiosa", "Roma, Italia", "X", 2, "01121000030001001", "E", "santasede"),
    ("lmm", "Liga Musulmana Mundial", "Organización religiosa", "La Meca, Arabia Saudita", "P", 3, "01112010020000002", "D", "saud"),
    ("hermandad", "Hermandad Musulmana", "Organización religiosa", "Sin sede central (origen en Egipto)", "X", 2, "00212100020000001", "E", ""),
    # Criminales
    ("sinaloa", "Cártel de Sinaloa", "Organización criminal", "Culiacán, México", "X", 1, "01111211211221021", "E", ""),
    ("cjng", "Cártel de Jalisco Nueva Generación", "Organización criminal", "Guadalajara, México", "X", 1, "01111211211101021", "E", ""),
    ("ndrangheta", "'Ndrangheta", "Organización criminal", "Calabria, Italia", "X", 1, "01110101221011022", "E", ""),
    ("pcc", "Primeiro Comando da Capital", "Organización criminal", "São Paulo, Brasil", "X", 1, "01211200220021121", "E", ""),
    ("yamaguchi", "Yamaguchi-gumi", "Organización criminal", "Kobe, Japón", "X", 1, "01101100120011001", "E", ""),
    # Paramilitares
    ("africacorps", "Africa Corps (ex Grupo Wagner)", "Paramilitar", "Bamako, Malí (operación principal)", "E", 3, "21110210120021010", "E", "ffaa_rusia"),
    ("hezbola", "Hezbolá", "Paramilitar", "Beirut, Líbano", "E", 3, "01212211121122111", "D", "cgri"),
    ("hutis", "Ansar Allah (hutíes)", "Paramilitar", "Saná, Yemen", "E", 2, "11201211010121120", "D", "cgri"),
    ("far_sudan", "Fuerzas de Apoyo Rápido (Sudán)", "Paramilitar", "Darfur, Sudán", "P", 2, "21200200110120111", "E", "alnahyan"),
    ("hamas", "Hamás", "Paramilitar", "Gaza, Palestina", "E", 2, "00102110010011100", "D", "cgri"),
    # Deportivas
    ("fifa", "FIFA", "Organización deportiva", "Zúrich, Suiza", "X", 1, "01113010231001202", "D", ""),
    ("coi", "Comité Olímpico Internacional", "Organización deportiva", "Lausana, Suiza", "X", 1, "01113010130001202", "D", ""),
    # Conocimiento
    ("harvard", "Universidad de Harvard", "Institución de conocimiento", "Cambridge, EE.UU.", "T", 2, "12133013132002002", "D", ""),
    ("mit", "MIT (Instituto Tecnológico de Massachusetts)", "Institución de conocimiento", "Cambridge, EE.UU.", "T", 2, "02132003133002002", "D", ""),
    ("tsinghua", "Universidad Tsinghua", "Institución de conocimiento", "Pekín, China", "E", 3, "02131013122002001", "D", "pcch"),
    ("cas", "Academia China de Ciencias", "Institución de conocimiento", "Pekín, China", "E", 3, "02231003023002101", "D", "consejoestado"),
    # Familias
    ("saud", "Casa de Saud (familia real saudí)", "Familia y oficina patrimonial", "Riad, Arabia Saudita", "P", 2, "32112220231122213", "D", ""),
    ("alnahyan", "Familia Al Nahyan (Abu Dabi: ADIA, Mubadala, ADQ)", "Familia y oficina patrimonial", "Abu Dabi, Emiratos Árabes Unidos", "P", 2, "22111211231112113", "D", ""),
    ("rothschild", "Familia Rothschild (Rothschild & Co)", "Familia y oficina patrimonial", "París, Francia", "T", 2, "00021000130001001", "D", ""),
    ("walton", "Familia Walton (Walmart)", "Familia y oficina patrimonial", "Bentonville, EE.UU.", "T", 2, "02311001321102023", "D", ""),
]

# origen, destino, tipo, descripción
RELACIONES = [
    ("kremlin", "pcch", "Alianza", "Asociación estratégica \"sin límites\" declarada en febrero de 2022, con energía, armas y coordinación en la ONU."),
    ("kremlin", "lider_iran", "Alianza", "Tratado de asociación estratégica integral firmado en enero de 2025; Irán aporta drones a Rusia."),
    ("ejercito_pak", "pcch", "Alianza", "China es el principal proveedor de armas de Pakistán y financia el Corredor Económico China-Pakistán."),
    ("cia", "mossad", "Alianza", "Cooperación estrecha en inteligencia y contraterrorismo desde los años cincuenta."),
    ("hezbola", "hamas", "Alianza", "Integran el llamado Eje de la Resistencia que coordina Irán."),
    ("pcc", "ndrangheta", "Alianza", "Sociedad documentada en el envío de cocaína desde puertos brasileños hacia Europa."),
    ("nvidia", "tsmc", "Alianza", "TSMC fabrica los chips de inteligencia artificial que diseña Nvidia."),
    ("pentagono", "epl", "Enfrentamiento", "Rivalidad estratégica central en el Pacífico occidental y el estrecho de Taiwán."),
    ("otan", "ffaa_rusia", "Enfrentamiento", "Choque indirecto por la guerra en Ucrania desde febrero de 2022."),
    ("fdi", "cgri", "Enfrentamiento", "Guerra abierta en junio de 2025 tras años de guerra en las sombras."),
    ("fdi", "hezbola", "Enfrentamiento", "Guerra en el Líbano en 2024 y ataques posteriores al alto el fuego."),
    ("fdi", "hamas", "Enfrentamiento", "Guerra en Gaza desde el ataque del 7 de octubre de 2023."),
    ("gob_india", "ejercito_pak", "Enfrentamiento", "Enfrentamiento militar en mayo de 2025 tras el atentado de Pahalgam."),
    ("sinaloa", "cjng", "Enfrentamiento", "Disputa por rutas y plazas en México y por el mercado de fentanilo."),
    ("casablanca", "huawei", "Enfrentamiento", "Sanciones y restricciones de exportación de EE.UU. desde 2019."),
    ("casablanca", "bytedance", "Enfrentamiento", "Ley de 2024 que obligó a desinvertir TikTok en EE.UU."),
    ("cgri", "hezbola", "Financiamiento", "Irán financia, arma y entrena a Hezbolá a través de la Fuerza Quds."),
    ("cgri", "hutis", "Financiamiento", "Provisión de misiles, drones y asesoramiento documentada por paneles de la ONU."),
    ("alnahyan", "far_sudan", "Financiamiento", "Paneles de expertos de la ONU señalaron envíos de armas desde Emiratos; Emiratos lo niega."),
    ("pentagono", "lockheed", "Financiamiento", "Principal contratista de defensa de EE.UU. (F-35, misiles)."),
    ("pentagono", "rtx", "Financiamiento", "Contratos de misiles y defensa aérea (Patriot, motores)."),
    ("pentagono", "palantir", "Financiamiento", "Contratos de análisis de datos e inteligencia artificial militar (Maven)."),
    ("pentagono", "spacex", "Financiamiento", "Lanzamientos militares y red satelital Starshield."),
    ("cia", "palantir", "Financiamiento", "In-Q-Tel, el fondo de capital de riesgo de la CIA, invirtió en Palantir en sus inicios."),
    ("gates", "oms", "Financiamiento", "Uno de los mayores donantes de la OMS."),
    ("rostec", "ffaa_rusia", "Abastecimiento", "Principal conglomerado de armamento del Estado ruso."),
    ("norinco", "epl", "Abastecimiento", "Uno de los principales proveedores de armas terrestres del EPL."),
    ("ffaa_rusia", "gob_india", "Abastecimiento", "Rusia sigue siendo gran proveedor de armas de la India (S-400)."),
    ("blackrock", "exxon", "Propiedad", "Entre los mayores accionistas institucionales."),
    ("vanguard", "microsoft", "Propiedad", "Mayor accionista institucional."),
    ("vanguard", "nvidia", "Propiedad", "Mayor accionista institucional."),
    ("spacex", "x", "Propiedad", "SpaceX absorbió a xAI, dueña de X, en febrero de 2026."),
    ("nsa", "microsoft", "Acceso a datos", "Programa PRISM revelado en 2013: acceso a datos de usuarios."),
    ("nsa", "alphabet", "Acceso a datos", "Programa PRISM revelado en 2013."),
    ("nsa", "meta", "Acceso a datos", "Programa PRISM revelado en 2013."),
    ("heritage", "casablanca", "Puerta giratoria", "Autores del Proyecto 2025 ocupan cargos en el gobierno."),
    ("cfr", "casablanca", "Puerta giratoria", "Fuente histórica de secretarios de Estado y asesores de seguridad."),
    ("jpmorgan", "fed", "Puerta giratoria", "Directivos del banco integraron el directorio de la Reserva Federal de Nueva York."),
    ("blackrock", "fed", "Contrato", "La Reserva Federal contrató a BlackRock en 2020 para administrar compras de bonos."),
]

# ---------- Ampliación a 200 (2026-11-16) ----------
AREA_TIPO.update({"Consultoría y auditoría": "Capital", "Farmacéutica y agroquímica": "Capital"})

ORGS += [
    ("planalto", "Presidencia de Brasil (Palacio del Planalto)", "Gobierno", "Brasilia, Brasil", "I", 1, "21211110021021211", "D", ""),
    ("turquia", "Presidencia de Turquía", "Gobierno", "Ankara, Turquía", "P", 1, "11211221021122211", "D", ""),
    ("downing", "Gobierno del Reino Unido (Downing Street)", "Gobierno", "Londres, Reino Unido", "T", 2, "01122121031012211", "D", ""),
    ("eliseo", "Presidencia de Francia (Elíseo)", "Gobierno", "París, Francia", "T", 2, "11122220021012211", "D", ""),
    ("kanzleramt", "Cancillería Federal de Alemania", "Gobierno", "Berlín, Alemania", "T", 2, "01121110021011211", "D", ""),
    ("kantei", "Gobierno de Japón (Kantei)", "Gobierno", "Tokio, Japón", "T", 2, "01121110021011211", "D", ""),
    ("taiwan", "Oficina Presidencial de Taiwán", "Gobierno", "Taipéi, Taiwán", "T", 3, "01111110010011100", "D", "casablanca"),
    ("ucrania", "Presidencia de Ucrania", "Gobierno", "Kiev, Ucrania", "T", 3, "11111220021021110", "D", "casablanca,comisioneu"),
    ("ffaa_ucrania", "Fuerzas Armadas de Ucrania", "Ejército", "Kiev, Ucrania", "T", 3, "01210212011121010", "D", "ucrania"),
    ("ffaa_egipto", "Fuerzas Armadas de Egipto", "Ejército", "El Cairo, Egipto", "P", 1, "12211220221221211", "D", ""),
    ("epc", "Ejército Popular de Corea", "Ejército", "Pionyang, Corea del Norte", "E", 3, "01210211101121010", "E", "ptk"),
    ("rosgvardia", "Rosgvardia (Guardia Nacional de Rusia)", "Fuerza de seguridad", "Moscú, Rusia", "E", 3, "01200210010011010", "D", "kremlin"),
    ("cac", "Administración del Ciberespacio de China", "Fuerza de seguridad", "Pekín, China", "E", 3, "00122031012002300", "D", "pcch"),
    ("mi6", "MI6 (Servicio Secreto de Inteligencia)", "Servicio de inteligencia", "Londres, Reino Unido", "T", 2, "00121111022002000", "D", "downing"),
    ("gchq", "GCHQ", "Servicio de inteligencia", "Cheltenham, Reino Unido", "T", 2, "01120012022003000", "D", "downing"),
    ("dgse", "DGSE (inteligencia exterior francesa)", "Servicio de inteligencia", "París, Francia", "T", 2, "00120111021002000", "D", "eliseo"),
    ("mit_tr", "MIT (Organización Nacional de Inteligencia de Turquía)", "Servicio de inteligencia", "Ankara, Turquía", "P", 3, "00110110021002000", "E", "turquia"),
    ("boe", "Banco de Inglaterra", "Banco central", "Londres, Reino Unido", "T", 2, "00120011121001202", "D", ""),
    ("stf", "Supremo Tribunal Federal de Brasil", "Justicia", "Brasilia, Brasil", "I", 1, "00011020010001200", "D", ""),
    ("ptk", "Partido del Trabajo de Corea", "Partido político", "Pionyang, Corea del Norte", "E", 1, "11211220011122211", "E", ""),
    ("pt_br", "Partido de los Trabajadores (Brasil)", "Partido político", "São Paulo, Brasil", "I", 2, "00211010020001101", "D", ""),
    ("morena", "Morena (México)", "Partido político", "Ciudad de México, México", "P", 2, "00211010020001101", "D", ""),
    ("ufwd", "Departamento de Trabajo del Frente Unido", "Partido político", "Pekín, China", "E", 3, "00112020031002000", "E", "pcch"),
    ("opep", "OPEP+", "Institución mundial", "Viena, Austria", "X", 3, "20010000020100200", "D", "saud,kremlin"),
    ("omc", "Organización Mundial del Comercio", "Institución mundial", "Ginebra, Suiza", "X", 3, "00020000020000200", "D", ""),
    ("ocs", "Organización de Cooperación de Shanghái", "Institución mundial", "Pekín, China", "E", 3, "00010100020001100", "D", "pcch,kremlin"),
    ("visa", "Visa", "Estandarización e infraestructura técnica", "San Francisco, EE.UU.", "T", 2, "01121022333003202", "D", ""),
    ("mastercard", "Mastercard", "Estandarización e infraestructura técnica", "Purchase, EE.UU.", "T", 2, "01121022233003202", "D", ""),
    ("euroclear", "Euroclear", "Estandarización e infraestructura técnica", "Bruselas, Bélgica", "T", 3, "00010010122002103", "D", "comisioneu"),
    ("goldman", "Goldman Sachs", "Empresa financiera", "Nueva York, EE.UU.", "T", 2, "00131012332003103", "D", ""),
    ("statestreet", "State Street", "Empresa financiera", "Boston, EE.UU.", "T", 2, "01120001221001003", "D", ""),
    ("qia", "Autoridad de Inversiones de Catar (QIA)", "Empresa financiera", "Doha, Catar", "P", 3, "01110000220001003", "D", "althani"),
    ("cic", "China Investment Corporation", "Empresa financiera", "Pekín, China", "E", 3, "01110000220001003", "D", "consejoestado"),
    ("spglobal", "S&P Global (calificadora)", "Empresa financiera", "Nueva York, EE.UU.", "T", 2, "00131021222002201", "D", ""),
    ("moodys", "Moody's", "Empresa financiera", "Nueva York, EE.UU.", "T", 2, "00121021222002201", "D", ""),
    ("berkshire", "Berkshire Hathaway", "Empresa financiera", "Omaha, EE.UU.", "T", 2, "13211000321200023", "D", ""),
    ("apple", "Apple", "Empresa tecnológica", "Cupertino, EE.UU.", "T", 2, "02233023332102103", "D", ""),
    ("openai", "OpenAI", "Empresa tecnológica", "San Francisco, EE.UU.", "T", 2, "02132023033002102", "D", ""),
    ("alibaba", "Alibaba", "Empresa tecnológica", "Hangzhou, China", "E", 3, "02232023223003122", "D", "pcch"),
    ("smic", "SMIC (Semiconductor Manufacturing International)", "Empresa tecnológica", "Shanghái, China", "E", 3, "02220002111200001", "D", "pcch"),
    ("anduril", "Anduril", "Empresa tecnológica", "Costa Mesa, EE.UU.", "T", 2, "01121103122102001", "D", ""),
    ("telegram", "Telegram", "Red social", "Dubái, Emiratos Árabes Unidos", "X", 1, "01112021111001001", "D", ""),
    ("rt", "RT", "Medio de comunicación", "Moscú, Rusia", "E", 3, "00111020010001000", "D", "kremlin"),
    ("nyt", "The New York Times", "Medio de comunicación", "Nueva York, EE.UU.", "T", 2, "01123021131002001", "D", ""),
    ("globo", "Grupo Globo", "Medio de comunicación", "Río de Janeiro, Brasil", "I", 2, "01112020120001001", "D", ""),
    ("petrobras", "Petrobras", "Recursos primarios", "Río de Janeiro, Brasil", "I", 3, "22220002221200012", "D", "planalto"),
    ("rosneft", "Rosneft", "Recursos primarios", "Moscú, Rusia", "E", 3, "32210100221201012", "D", "kremlin"),
    ("sinopec", "Sinopec", "Recursos primarios", "Pekín, China", "E", 3, "13320001221300022", "D", "consejoestado"),
    ("vitol", "Vitol", "Recursos primarios", "Ginebra, Suiza", "X", 2, "11120000232002032", "D", ""),
    ("trafigura", "Trafigura", "Recursos primarios", "Singapur", "X", 2, "11120000222002032", "D", ""),
    ("stategrid", "State Grid de China", "Recursos primarios", "Pekín, China", "E", 3, "13320002212311112", "D", "consejoestado"),
    ("gendyn", "General Dynamics", "Empresa de armamento", "Reston, EE.UU.", "T", 2, "02220102221301011", "D", ""),
    ("elbit", "Elbit Systems", "Empresa de armamento", "Haifa, Israel", "T", 2, "01120102121202001", "D", ""),
    ("hanwha", "Hanwha Aerospace", "Empresa de armamento", "Changwon, Corea del Sur", "T", 2, "01220002111200011", "D", ""),
    ("byd", "BYD", "Empresa industrial", "Shenzhen, China", "E", 3, "13321003211301022", "D", "pcch"),
    ("boeing", "Boeing", "Empresa industrial", "Arlington, EE.UU.", "T", 2, "02231002031301130", "D", ""),
    ("airbus", "Airbus", "Empresa industrial", "Leiden, Países Bajos", "T", 2, "02231002231301131", "D", ""),
    ("mckinsey", "McKinsey & Company", "Consultoría y auditoría", "Nueva York, EE.UU.", "T", 2, "00132011233002101", "D", ""),
    ("deloitte", "Deloitte", "Consultoría y auditoría", "Londres, Reino Unido", "T", 2, "01331011233003201", "D", ""),
    ("bayer", "Bayer (con Monsanto)", "Farmacéutica y agroquímica", "Leverkusen, Alemania", "T", 2, "12230002121201101", "D", ""),
    ("pfizer", "Pfizer", "Farmacéutica y agroquímica", "Nueva York, EE.UU.", "T", 2, "02231013232202102", "D", ""),
    ("dpworld", "DP World", "Logística y transporte", "Dubái, Emiratos Árabes Unidos", "P", 3, "03210001221011032", "D", "maktoum"),
    ("cmport", "China Merchants Port", "Logística y transporte", "Shenzhen, China", "E", 3, "03110001121011031", "D", "consejoestado"),
    ("aipac", "AIPAC (Comité de Asuntos Públicos Estadounidense-Israelí)", "ONG, fundación o think tank", "Washington, EE.UU.", "T", 2, "00111010031001102", "D", ""),
    ("brookings", "Brookings Institution", "ONG, fundación o think tank", "Washington, EE.UU.", "T", 2, "00122010031001101", "D", ""),
    ("chatham", "Chatham House", "ONG, fundación o think tank", "Londres, Reino Unido", "T", 2, "00122010021001100", "D", ""),
    ("alazhar", "Al-Azhar", "Organización religiosa", "El Cairo, Egipto", "P", 3, "01222010020000101", "D", ""),
    ("sud", "Iglesia de Jesucristo de los Santos de los Últimos Días", "Organización religiosa", "Salt Lake City, EE.UU.", "T", 1, "12212000121001003", "D", ""),
    ("trenaragua", "Tren de Aragua", "Organización criminal", "Origen en Aragua, Venezuela", "X", 1, "01111110110011020", "E", ""),
    ("cv", "Comando Vermelho", "Organización criminal", "Río de Janeiro, Brasil", "X", 1, "01211210110021111", "E", ""),
    ("sunyeeon", "Sun Yee On (tríada)", "Organización criminal", "Hong Kong", "X", 1, "01110100120011011", "E", ""),
    ("prince", "Prince Group (Camboya)", "Organización criminal", "Nom Pen, Camboya", "X", 1, "01110111221012012", "E", ""),
    ("pmf", "Fuerzas de Movilización Popular (Irak)", "Paramilitar", "Bagdad, Irak", "E", 3, "11201210120021111", "D", "cgri"),
    ("talibanes", "Emirato Islámico de Afganistán (talibanes)", "Paramilitar", "Kabul, Afganistán", "X", 1, "10201220010021200", "D", ""),
    ("jnim", "JNIM (Al Qaeda en el Sahel)", "Paramilitar", "Sahel central (Malí)", "X", 1, "10101210110021110", "E", ""),
    ("isis", "Estado Islámico y sus provincias", "Paramilitar", "Sin sede fija", "X", 1, "00111211110011011", "E", ""),
    ("stanford", "Universidad de Stanford", "Institución de conocimiento", "Stanford, EE.UU.", "T", 2, "12132013132002002", "D", ""),
    ("oxford", "Universidad de Oxford", "Institución de conocimiento", "Oxford, Reino Unido", "T", 2, "11132012031001001", "D", ""),
    ("althani", "Casa de Al Thani (Catar)", "Familia y oficina patrimonial", "Doha, Catar", "P", 2, "32112120231111113", "D", ""),
    ("maktoum", "Familia Al Maktoum (Dubái)", "Familia y oficina patrimonial", "Dubái, Emiratos Árabes Unidos", "P", 2, "02111011231011122", "D", ""),
]

# Al Jazeera pasa a depender de la Casa de Al Thani
ORGS = [(o[:8] + ("althani",)) if o[0] == "aljazeera" else o for o in ORGS]

# Ajustes por las anclas de la escala (miembros, ganancia y dinero neto)
_FIX = {  # id: {eje: valor}
 "icbc": {"mie": 2}, "sinopec": {"mie": 2, "gan": 1}, "deloitte": {"mie": 2, "gan": 1}, "siemens": {"mie": 2}, "toyota": {"mie": 2, "din": 2},
 "huawei": {"mie": 2, "gan": 1}, "rostec": {"mie": 2}, "norinco": {"mie": 2},
 "blackrock": {"gan": 1}, "vanguard": {"gan": 1}, "nbim": {"gan": 2}, "tsmc": {"gan": 2}, "exxon": {"gan": 2, "din": 2},
 "gazprom": {"gan": 1, "din": 1}, "glencore": {"gan": 1}, "cargill": {"gan": 1, "din": 1}, "samsung": {"gan": 2, "din": 2},
 "tencent": {"gan": 2, "din": 2}, "bytedance": {"gan": 2, "din": 2}, "reuters": {"gan": 1}, "newscorp": {"gan": 1},
 "lockheed": {"gan": 1}, "rtx": {"gan": 1}, "bae": {"gan": 1}, "maersk": {"gan": 1, "din": 1}, "cosco": {"gan": 1, "din": 1},
 "fifa": {"gan": 1}, "palantir": {"gan": 1}, "asml": {"gan": 1}, "byd": {"gan": 1}, "catl": {"gan": 1}, "pfizer": {"gan": 1},
 "airbus": {"gan": 1}, "gendyn": {"gan": 1}, "mckinsey": {"gan": 1}, "spglobal": {"gan": 1}, "moodys": {"gan": 1},
 "statestreet": {"gan": 1}, "dpworld": {"gan": 1}, "vitol": {"gan": 1}, "trafigura": {"gan": 1},
 "gates": {"din": 1}, "harvard": {"din": 1}, "stanford": {"din": 1}, "walton": {"din": 2}, "althani": {"din": 2},
 "qia": {"din": 2}, "santasede": {"din": 1}, "sud": {"din": 2}, "statestreet_": {},
}
def _apply(o):
    f = _FIX.get(o[0])
    if not f: return o
    sc = dict(zip(ORDEN_ENTRADA, o[6]))
    for k, v in f.items(): sc[k] = str(v)
    return o[:6] + ("".join(sc[k] for k in ORDEN_ENTRADA),) + o[7:]
ORGS = [_apply(o) for o in ORGS]

# Poder formal 0-3: cuánto de su poder real está reconocido públicamente y sujeto a control
FORMAL = dict(
 casablanca=2, kremlin=1, consejoestado=1, lider_iran=1, pm_israel=2, comisioneu=2, gob_india=2, planalto=2, turquia=1, downing=2,
 eliseo=2, kanzleramt=3, kantei=3, taiwan=2, ucrania=2,
 pentagono=2, epl=1, ffaa_rusia=1, fdi=2, ejercito_pak=0, ffaa_ucrania=2, ffaa_egipto=0, epc=1,
 cgri=1, fsb=0, mps_china=1, dhs=2, rosgvardia=1, cac=1,
 cia=1, nsa=0, mss=0, gru=0, mossad=0, isi=0, mi6=1, gchq=1, dgse=1, mit_tr=0,
 fed=2, bce=2, pboc=1, boj=2, bpi=1, boe=2,
 scotus=3, doj=2, tjue=3, cpi=3, stf=2,
 pcch=1, gop=2, dem=2, bjp=1, ptk=0, pt_br=2, morena=2, ufwd=0,
 csonu=3, fmi=2, bm=2, otan=2, oms=2, brics=2, opep=2, omc=3, ocs=2,
 icann=2, iso=2, swift=1, cips=1, visa=2, mastercard=2, euroclear=1,
 blackrock=1, vanguard=1, jpmorgan=2, icbc=1, nbim=3, pif=1, goldman=1, statestreet=1, qia=0, cic=1, spglobal=1, moodys=1, berkshire=2,
 alphabet=1, microsoft=1, amazon=1, nvidia=2, tsmc=2, asml=2, huawei=0, palantir=0, apple=1, openai=1, alibaba=1, smic=1, anduril=1,
 meta=1, x=0, bytedance=0, tencent=0, telegram=0,
 reuters=2, newscorp=1, bbc=2, xinhua=1, aljazeera=1, rt=0, nyt=2, globo=1,
 aramco=1, gazprom=1, exxon=2, glencore=1, cargill=0, petrobras=2, rosneft=0, sinopec=1, vitol=0, trafigura=0, stategrid=1,
 lockheed=2, rtx=2, bae=2, rostec=0, norinco=0, gendyn=2, elbit=1, hanwha=2,
 samsung=1, toyota=2, siemens=2, catl=1, spacex=1, byd=1, boeing=2, airbus=2,
 msc=0, maersk=2, cosco=1, dpworld=1, cmport=1, mckinsey=0, deloitte=1, bayer=2, pfizer=2,
 gates=1, osf=1, wef=1, cfr=1, heritage=1, rand=1, aipac=1, brookings=2, chatham=1,
 bilderberg=0, trilateral=1, ugle=0,
 santasede=1, patriarcado=1, opusdei=0, lmm=1, hermandad=0, alazhar=2, sud=1,
 sinaloa=0, cjng=0, ndrangheta=0, pcc=0, yamaguchi=0, trenaragua=0, cv=0, sunyeeon=0, prince=0,
 africacorps=0, hezbola=1, hutis=1, far_sudan=0, hamas=0, pmf=1, talibanes=1, jnim=0, isis=0,
 fifa=1, coi=1, harvard=2, mit=2, tsinghua=1, cas=2, stanford=2, oxford=3,
 saud=1, alnahyan=1, rothschild=1, walton=1, althani=1, maktoum=1,
)

# Fase de Quigley: E expansión, C captura, D distorsión (por defecto C)
_E = "pcch consejoestado epl mss mps_china cac ufwd huawei bytedance tencent alibaba smic byd catl cosco cmport cips stategrid cic tsinghua cas norinco openai anduril spacex nvidia palantir tsmc telegram gob_india bjp turquia pif althani alnahyan maktoum dpworld africacorps jnim prince trenaragua cjng pcc cv hanwha ocs brics".split()
_D = "casablanca cia nsa doj dhs gop dem csonu oms cpi bbc nyt newscorp boeing bilderberg trilateral ugle wef cfr lider_iran cgri hezbola hamas ptk epc gazprom rt isis yamaguchi sunyeeon hermandad eliseo downing".split()
FASE = {o[0]: ("E" if o[0] in _E else "D" if o[0] in _D else "C") for o in ORGS}
FASES = {"E": "Expansión", "C": "Captura", "D": "Distorsión"}

# Intensidad de las relaciones originales (1 a 3; por defecto 2)
_INT = {("kremlin","pcch"):3, ("cgri","hezbola"):3, ("pentagono","lockheed"):3, ("pentagono","epl"):3, ("otan","ffaa_rusia"):3,
        ("fdi","cgri"):3, ("fdi","hamas"):3, ("fdi","hezbola"):3, ("sinaloa","cjng"):3, ("cia","mossad"):3, ("nvidia","tsmc"):3,
        ("spacex","x"):3, ("gates","oms"):1, ("cfr","casablanca"):1, ("jpmorgan","fed"):1, ("blackrock","fed"):1}
RELACIONES = [r + (_INT.get((r[0], r[1]), 2),) for r in RELACIONES]
RELACIONES += [(a, b, t, x, i) for a, b, t, i, x in [
 ("casablanca","pm_israel","Alianza",3,"Respaldo político, diplomático y militar permanente de EE.UU. a Israel."),
 ("pentagono","fdi","Abastecimiento",3,"Ayuda militar de unos 3.800 millones de dólares anuales según el memorando 2019-2028."),
 ("casablanca","downing","Alianza",3,"La relación especial: defensa, inteligencia y armas nucleares compartidas."),
 ("nsa","gchq","Alianza",3,"Núcleo de los Cinco Ojos desde el acuerdo UKUSA de 1946."),
 ("cia","mi6","Alianza",3,"Cooperación estrecha en inteligencia humana desde la Segunda Guerra Mundial."),
 ("otan","ffaa_ucrania","Abastecimiento",3,"Armas, entrenamiento e inteligencia para Ucrania desde 2022."),
 ("comisioneu","ucrania","Financiamiento",3,"Mecanismo para Ucrania de 50.000 millones de euros y préstamos ligados a activos rusos congelados."),
 ("casablanca","ucrania","Abastecimiento",2,"Armas y apoyo de EE.UU.; desde 2025, en buena parte vendidas a través de aliados europeos."),
 ("euroclear","kremlin","Enfrentamiento",2,"Custodia la mayor parte de las reservas del banco central ruso congeladas desde 2022."),
 ("ffaa_rusia","ffaa_ucrania","Enfrentamiento",3,"Guerra a gran escala desde febrero de 2022."),
 ("kremlin","ptk","Alianza",3,"Tratado de asociación estratégica integral de junio de 2024, con defensa mutua."),
 ("epc","ffaa_rusia","Alianza",3,"Tropas norcoreanas combatieron junto a Rusia en Kursk en 2024 y 2025."),
 ("pcch","ptk","Alianza",2,"Tratado de amistad y defensa de 1961; China es el principal sostén económico de Corea del Norte."),
 ("cgri","pmf","Financiamiento",3,"La Fuerza Quds organiza y arma a las principales milicias de las Fuerzas de Movilización Popular."),
 ("cgri","hamas","Financiamiento",2,"Financiamiento y entrenamiento militar documentados."),
 ("consejoestado","lider_iran","Alianza",1,"China es el principal comprador del petróleo iraní pese a las sanciones."),
 ("epl","ejercito_pak","Abastecimiento",3,"Cazas J-10C, misiles y fragatas chinas; usados en el choque con India de mayo de 2025."),
 ("turquia","otan","Alianza",2,"Miembro de la OTAN con el segundo ejército de la alianza y política exterior propia."),
 ("ffaa_rusia","turquia","Abastecimiento",1,"Turquía compró el sistema antiaéreo ruso S-400 en 2019."),
 ("saud","casablanca","Alianza",2,"Seguridad a cambio de petróleo e inversión; acuerdo de defensa estratégica en 2025."),
 ("saud","hutis","Enfrentamiento",2,"Guerra en Yemen desde 2015, con tregua de hecho desde 2022."),
 ("fdi","hutis","Enfrentamiento",2,"Ataques cruzados desde 2023 por los misiles hutíes contra Israel."),
 ("pentagono","hutis","Enfrentamiento",2,"Campaña aérea de EE.UU. en 2025 por los ataques al tráfico en el mar Rojo."),
 ("althani","hamas","Financiamiento",1,"Catar albergó la oficina política de Hamás y canalizó fondos a Gaza."),
 ("althani","casablanca","Alianza",2,"Base aérea de Al Udeid, la mayor de EE.UU. en Medio Oriente."),
 ("althani","hermandad","Alianza",1,"Apoyo político y mediático de Catar a movimientos de la Hermandad Musulmana."),
 ("saud","hermandad","Enfrentamiento",2,"Arabia Saudita la declaró organización terrorista en 2014."),
 ("alnahyan","hermandad","Enfrentamiento",2,"Emiratos la persigue y la declaró organización terrorista en 2014."),
 ("ffaa_egipto","hermandad","Enfrentamiento",3,"El ejército derrocó al gobierno de la Hermandad en 2013 y la ilegalizó."),
 ("pentagono","ffaa_egipto","Abastecimiento",2,"Ayuda militar anual de unos 1.300 millones de dólares."),
 ("talibanes","isis","Enfrentamiento",2,"Guerra contra la rama afgana del Estado Islámico (ISIS-K)."),
 ("talibanes","ejercito_pak","Enfrentamiento",2,"Choques fronterizos en octubre de 2025 por los refugios del TTP."),
 ("jnim","africacorps","Enfrentamiento",3,"Combate directo en Malí desde la llegada de Wagner en 2021."),
 ("isi","talibanes","Financiamiento",2,"Apoyo histórico del ISI a los talibanes desde los años noventa."),
 ("gob_india","pcch","Enfrentamiento",1,"Disputa fronteriza en el Himalaya; choque de Galwan en 2020 y deshielo parcial desde 2024."),
 ("gob_india","casablanca","Ambigua",1,"Socios en el Quad, con fricción por aranceles y compras de petróleo ruso en 2025."),
 ("planalto","casablanca","Ambigua",1,"Aranceles de EE.UU. a Brasil en 2025 y choque por el juicio a Bolsonaro."),
 ("stf","x","Enfrentamiento",2,"El tribunal suspendió X en Brasil en 2024 hasta que acató sus órdenes."),
 ("casablanca","stf","Enfrentamiento",1,"EE.UU. sancionó en 2025 al juez Alexandre de Moraes."),
 ("pt_br","planalto","Gobierna",2,"El PT encabeza el gobierno desde 2023."),
 ("gop","casablanca","Gobierna",2,"El Partido Republicano controla el Ejecutivo desde enero de 2025."),
 ("bjp","gob_india","Gobierna",3,"El BJP gobierna la India desde 2014."),
 ("morena","planalto","Ambigua",1,"Afinidad política entre los gobiernos de izquierda de México y Brasil."),
 ("comisioneu","alphabet","Enfrentamiento",2,"Multas antimonopolio de la UE por varios miles de millones de euros."),
 ("comisioneu","meta","Enfrentamiento",1,"Sanciones bajo la Ley de Mercados Digitales y de protección de datos."),
 ("comisioneu","apple","Enfrentamiento",1,"Multas y obligaciones bajo la Ley de Mercados Digitales."),
 ("comisioneu","x","Enfrentamiento",1,"Investigación y sanción bajo la Ley de Servicios Digitales."),
 ("doj","alphabet","Enfrentamiento",2,"Juicio que declaró monopolio ilegal al buscador de Google en 2024."),
 ("casablanca","harvard","Enfrentamiento",2,"Congelamiento de fondos federales a Harvard en 2025."),
 ("casablanca","fed","Ambigua",2,"Presión pública sobre las tasas de interés y sobre miembros de la junta."),
 ("casablanca","cpi","Enfrentamiento",2,"Sanciones de EE.UU. a jueces y fiscales de la Corte en 2025."),
 ("casablanca","oms","Enfrentamiento",2,"Retiro de EE.UU. de la OMS anunciado en enero de 2025."),
 ("casablanca","nvidia","Ambigua",1,"Controles de exportación de chips a China y acuerdos sobre ventas autorizadas."),
 ("casablanca","tsmc","Ambigua",1,"Presión arancelaria e inversión forzada en fábricas en Arizona."),
 ("pentagono","anduril","Financiamiento",2,"Contratos de drones, defensa antiaérea y sistemas autónomos."),
 ("pentagono","openai","Financiamiento",1,"Contrato de 2025 para inteligencia artificial de defensa."),
 ("pentagono","microsoft","Financiamiento",2,"Nube militar conjunta (JWCC)."),
 ("pentagono","amazon","Financiamiento",2,"Nube militar conjunta (JWCC)."),
 ("pentagono","boeing","Financiamiento",3,"Aviones, misiles y satélites; uno de los mayores contratistas."),
 ("pentagono","gendyn","Financiamiento",3,"Submarinos nucleares, tanques y sistemas de información."),
 ("cia","amazon","Financiamiento",2,"Contratos de nube para la comunidad de inteligencia desde 2013."),
 ("nsa","apple","Acceso a datos",1,"Apple figuraba entre las empresas del programa PRISM revelado en 2013."),
 ("swift","kremlin","Enfrentamiento",2,"Desconexión de los principales bancos rusos en 2022."),
 ("visa","kremlin","Enfrentamiento",1,"Salida de Rusia en 2022."),
 ("mastercard","kremlin","Enfrentamiento",1,"Salida de Rusia en 2022."),
 ("blackrock","apple","Propiedad",2,"Entre los mayores accionistas institucionales."),
 ("vanguard","apple","Propiedad",2,"Mayor accionista institucional."),
 ("vanguard","exxon","Propiedad",2,"Mayor accionista institucional."),
 ("microsoft","openai","Propiedad",2,"Participación de alrededor del 27 % tras la reestructuración de 2025."),
 ("nvidia","openai","Financiamiento",2,"Acuerdo de inversión de hasta 100.000 millones de dólares anunciado en 2025."),
 ("tsmc","apple","Abastecimiento",3,"Fabrica todos los procesadores de Apple."),
 ("asml","tsmc","Abastecimiento",3,"Única proveedora de las máquinas de litografía ultravioleta extrema."),
 ("asml","smic","Abastecimiento",1,"Ventas limitadas por los controles de exportación neerlandeses y de EE.UU."),
 ("casablanca","smic","Enfrentamiento",2,"SMIC está en la lista de entidades restringidas de EE.UU."),
 ("huawei","smic","Alianza",2,"SMIC fabrica los chips avanzados de Huawei."),
 ("gazprom","pcch","Abastecimiento",2,"Gas a China por el gasoducto Fuerza de Siberia."),
 ("rosneft","gob_india","Abastecimiento",2,"Rusia pasó a ser el principal proveedor de crudo de la India desde 2022."),
 ("lockheed","fdi","Abastecimiento",3,"Cazas F-35I y otros sistemas."),
 ("elbit","fdi","Abastecimiento",3,"Principal proveedor local de drones y electrónica militar."),
 ("rtx","saud","Abastecimiento",2,"Misiles y defensa antiaérea Patriot."),
 ("cjng","casablanca","Enfrentamiento",2,"Designado organización terrorista extranjera por EE.UU. en 2025."),
 ("sinaloa","casablanca","Enfrentamiento",2,"Designado organización terrorista extranjera por EE.UU. en 2025."),
 ("trenaragua","casablanca","Enfrentamiento",2,"Designado organización terrorista en 2025 y blanco de operaciones de EE.UU."),
 ("pcc","cv","Enfrentamiento",2,"Rivalidad por el control de cárceles y rutas en Brasil."),
 ("prince","casablanca","Enfrentamiento",2,"Sancionado por EE.UU. y Reino Unido en 2025 por estafas a escala industrial."),
 ("hezbola","pmf","Alianza",2,"Ambos integran el Eje de la Resistencia que coordina Irán."),
 ("hutis","hamas","Alianza",1,"Ataques hutíes declarados en apoyo a Hamás desde 2023."),
 ("fifa","saud","Contrato",2,"Arabia Saudita organizará el Mundial 2034."),
 ("saud","opep","Gobierna",3,"Arabia Saudita lidera las decisiones de producción de la OPEP+."),
 ("aipac","pm_israel","Alianza",3,"Principal lobby proisraelí en EE.UU."),
 ("aipac","gop","Financiamiento",2,"Gasto electoral a través de su comité de acción política."),
 ("aipac","dem","Financiamiento",2,"Gasto electoral a través de su comité de acción política, incluidas primarias."),
 ("brookings","dem","Puerta giratoria",1,"Fuente frecuente de funcionarios de gobiernos demócratas."),
 ("mckinsey","pif","Contrato",2,"Asesor central de la estrategia saudí Visión 2030."),
 ("mit","pentagono","Financiamiento",2,"El Laboratorio Lincoln del MIT es financiado por el Pentágono."),
 ("santasede","pcch","Ambigua",1,"Acuerdo provisorio de 2018 sobre nombramiento de obispos, renovado."),
 ("eliseo","africacorps","Enfrentamiento",1,"Rusia reemplazó a Francia como socio de seguridad en el Sahel."),
 ("turquia","hermandad","Alianza",1,"Turquía dio refugio y apoyo a dirigentes de la Hermandad."),
 ("epl","taiwan","Enfrentamiento",3,"Maniobras militares regulares alrededor de Taiwán."),
 ("pentagono","taiwan","Abastecimiento",2,"Ventas de armas bajo la Ley de Relaciones con Taiwán."),
 ("epl","kantei","Enfrentamiento",1,"Rivalidad en el mar de China Oriental y por Taiwán."),
 ("pentagono","kantei","Alianza",3,"Tratado de seguridad de 1960 y bases de EE.UU. en Japón."),
 ("casablanca","kanzleramt","Alianza",2,"Alianza atlántica, con fricciones comerciales."),
 ("kremlin","alnahyan","Ambigua",1,"Emiratos mantiene comercio y finanzas con Rusia pese a las sanciones."),
 ("alnahyan","casablanca","Alianza",2,"Socio de seguridad e inversor estratégico en inteligencia artificial."),
 ("dpworld","maktoum","Propiedad",3,"Controlada por el gobierno de Dubái a través de Dubai World."),
 ("telegram","eliseo","Enfrentamiento",1,"Su fundador fue detenido e imputado en Francia en 2024."),
]]

# Anclas de la escala: (3 dominante, 2 alto, 1 relevante)
ANCLAS = {
 "rec": ("Controla más del 5 % de las reservas o la producción mundial de un recurso estratégico, o un territorio continental", "Más del 1 %, o los recursos de un país grande", "Recursos relevantes en lo local"),
 "cap": ("Más de 300.000 M USD en activos físicos o infraestructura crítica global", "Más de 50.000 M USD", "Más de 5.000 M USD"),
 "prd": ("Líder mundial en un bien estratégico (más del 15 % del mercado)", "Entre los diez primeros del mundo en su rubro", "Productor relevante"),
 "mov": ("Red logística o proyección de fuerza global", "Alcance regional o multinacional", "Alcance nacional"),
 "gan": ("Más de 50.000 M USD de ganancia anual", "Más de 10.000 M USD", "Más de 1.000 M USD"),
 "din": ("Más de 1 billón USD en activos, capitalización o fondos administrados, o emisión de moneda de reserva", "Más de 100.000 M USD", "Más de 10.000 M USD"),
 "coe": ("Arsenal nuclear con alcance global o proyección militar mundial", "Fuerza capaz de librar una guerra regional", "Capacidad armada local"),
 "ter": ("Gobierna más de 5 M de km² o más de 500 M de personas", "Un país mediano o grande", "Una región o enclaves"),
 "adq": ("Vigila u obtiene datos de cientos de millones de personas en todo el mundo", "Alcance nacional o sectorial amplio", "Alcance limitado"),
 "pro": ("Capacidad analítica o de cómputo de primer nivel mundial", "Capacidad alta", "Capacidad relevante"),
 "mod": ("Decide qué ven más de 1.000 M de personas", "Más de 100 M de personas o un país grande", "Más de 10 M de personas"),
 "con": ("Referencia mundial en su campo", "Referencia regional o sectorial", "Saber especializado"),
 "inn": ("Produce avances de frontera mundial", "Innova dentro de su sector", "Adopta y adapta"),
 "mie": ("Más de 1 M de integrantes o más de 100 M de fieles o seguidores", "Más de 100.000 integrantes", "Más de 10.000 integrantes"),
 "cul": ("Moldea ideas o gustos a escala mundial", "En una región o civilización", "En un país"),
 "red": ("Acceso directo a jefes de Estado y a la cúpula de las mayores organizaciones del mundo", "Red de alto nivel regional o sectorial", "Red nacional"),
 "reg": ("Sus reglas obligan de hecho fuera de su jurisdicción", "Regula un país grande o un sector entero", "Normas propias o locales"),
}

# ---------- Ajustes del 2026-11-16 por la guerra con Irán y otros cambios verificados ----------
# Irán: según Reuters, desde marzo de 2026 la Guardia Revolucionaria decide y el líder supremo legitima.
def _set(oid, aut=None, dep=None):
    global ORGS
    ORGS = [(o[:5] + ((aut if aut is not None else o[5]),) + o[6:8] + ((dep if dep is not None else o[8]),)) if o[0] == oid else o for o in ORGS]
_set("cgri", aut=1, dep="")
_set("lider_iran", aut=3, dep="cgri")

def _rel_text(a, b, t=None, x=None, i=None):
    global RELACIONES
    RELACIONES = [((a, b, t or r[2], x or r[3], i or r[4]) if (r[0], r[1]) == (a, b) else r) for r in RELACIONES]
_rel_text("fdi", "cgri", x="Guerra de doce días en junio de 2025 y nueva guerra desde el 28 de febrero de 2026, junto con EE.UU.", i=3)
_rel_text("sinaloa", "cjng", t="Enfrentamiento", x="Disputa histórica por rutas; en 2026 el CJNG apoyó con combatientes y dinero a Los Chapitos contra Los Mayos, según reconoció el gobierno mexicano.")
RELACIONES += [
 ("casablanca", "lider_iran", "Enfrentamiento", "Guerra iniciada el 28 de febrero de 2026, en la que murió Ali Jamenei; bloqueo naval a los puertos iraníes vigente desde julio.", 3),
 ("pentagono", "cgri", "Enfrentamiento", "Operación Furia Épica desde febrero de 2026 y ataques posteriores contra objetivos de la Guardia.", 3),
 ("ejercito_pak", "casablanca", "Ambigua", "Pakistán medió y fue sede de las negociaciones entre EE.UU. e Irán en 2026.", 1),
 ("hutis", "pentagono", "Enfrentamiento", "Los hutíes se sumaron a la guerra de 2026 con ataques con misiles.", 2),
]

# ---------- Ampliación del 2026-11-16: 50 organizaciones para cubrir regiones sin presencia ----------
# Orden de los 17 dígitos: rec cap mie con cul coe mod inn gan red pro prd ter adq reg mov din
_NUEVAS = [
 # América Latina
 ("casarosada", "Casa Rosada (Gobierno de Argentina)", "Gobierno", "Buenos Aires, Argentina", "T", 2, "21211110021121211", "D", "", 2, "C"),
 ("gob_colombia", "Casa de Nariño (Gobierno de Colombia)", "Gobierno", "Bogotá, Colombia", "T", 2, "21211210021121211", "D", "", 2, "C"),
 ("miraflores", "Palacio de Miraflores (Gobierno interino de Venezuela)", "Gobierno", "Caracas, Venezuela", "T", 3, "21201120010021110", "D", "casablanca", 1, "D"),
 ("pdvsa", "PDVSA (Petróleos de Venezuela)", "Recursos primarios", "Caracas, Venezuela", "T", 3, "32110000110100011", "D", "miraflores", 1, "D"),
 ("pcc_cuba", "Partido Comunista de Cuba", "Partido político", "La Habana, Cuba", "E", 2, "00111120010012100", "D", "", 1, "D"),
 ("gob_chile", "Palacio de La Moneda (Gobierno de Chile)", "Gobierno", "Santiago, Chile", "T", 2, "21111110021121211", "D", "", 2, "C"),
 ("codelco", "Codelco", "Recursos primarios", "Santiago, Chile", "T", 3, "22120001111200011", "D", "gob_chile", 2, "C"),
 ("gob_ecuador", "Palacio de Carondelet (Gobierno de Ecuador)", "Gobierno", "Quito, Ecuador", "T", 2, "11111110010121110", "D", "", 2, "C"),
 ("eln", "Ejército de Liberación Nacional (ELN)", "Paramilitar", "Frontera colombo-venezolana", "X", 1, "10100100110011100", "E", "", 0, "D"),
 ("clan_golfo", "Clan del Golfo (EGC)", "Organización criminal", "Urabá, Colombia", "X", 1, "11100100110111111", "E", "", 0, "E"),
 ("los_lobos", "Los Lobos (Ecuador)", "Organización criminal", "Guayaquil, Ecuador", "X", 2, "10100100110010110", "E", "", 0, "E"),
 # África
 ("gob_nigeria", "Villa Aso Rock (Gobierno de Nigeria)", "Gobierno", "Abuya, Nigeria", "P", 1, "21211110020121211", "D", "", 2, "C"),
 ("dangote", "Grupo Dangote", "Empresa industrial", "Lagos, Nigeria", "P", 2, "12111001120200011", "D", "", 1, "E"),
 ("gob_sudafrica", "Union Buildings (Gobierno de Sudáfrica)", "Gobierno", "Pretoria, Sudáfrica", "P", 1, "21211110021121211", "D", "", 2, "C"),
 ("gob_etiopia", "Gobierno de Etiopía", "Gobierno", "Adís Abeba, Etiopía", "P", 1, "11211210020121210", "D", "", 1, "C"),
 ("gob_kenia", "State House (Gobierno de Kenia)", "Gobierno", "Nairobi, Kenia", "T", 2, "11111110021121110", "D", "", 2, "C"),
 ("gob_ruanda", "Gobierno de Ruanda", "Gobierno", "Kigali, Ruanda", "P", 1, "10111210021011110", "D", "", 1, "E"),
 ("m23", "AFC/M23", "Paramilitar", "Goma, RD Congo", "X", 2, "10100100110010100", "E", "gob_ruanda", 0, "E"),
 ("saf", "Fuerzas Armadas de Sudán", "Ejército", "Puerto Sudán, Sudán", "P", 1, "11210210110021110", "D", "", 1, "D"),
 ("majzen", "Palacio Real de Marruecos (Majzén)", "Gobierno", "Rabat, Marruecos", "T", 2, "11111111021121111", "D", "", 1, "C"),
 ("ocp", "OCP (fosfatos de Marruecos)", "Recursos primarios", "Casablanca, Marruecos", "T", 3, "31120001111300111", "D", "majzen", 1, "C"),
 ("sonatrach", "Sonatrach", "Recursos primarios", "Argel, Argelia", "P", 2, "22110000210200111", "D", "", 1, "C"),
 ("lna", "Ejército Nacional Libio (Haftar)", "Paramilitar", "Bengasi, Libia", "P", 2, "21100110120121111", "D", "", 0, "D"),
 ("alshabaab", "Al Shabaab", "Paramilitar", "Sur de Somalia", "X", 1, "10101100100011100", "D", "", 0, "E"),
 ("aes", "Alianza de Estados del Sahel", "Institución mundial", "Bamako, Malí", "E", 2, "10101110010021100", "D", "", 1, "E"),
 # Europa
 ("chigi", "Palazzo Chigi (Gobierno de Italia)", "Gobierno", "Roma, Italia", "T", 2, "12222111021221212", "D", "", 2, "C"),
 ("moncloa", "La Moncloa (Gobierno de España)", "Gobierno", "Madrid, España", "T", 2, "12222111021221212", "D", "", 2, "C"),
 ("gob_polonia", "Gobierno de Polonia", "Gobierno", "Varsovia, Polonia", "T", 2, "11211210021121211", "D", "", 2, "E"),
 ("gob_hungria", "Gobierno de Hungría", "Gobierno", "Budapest, Hungría", "T", 2, "01111110020111111", "D", "", 2, "C"),
 ("shell", "Shell", "Recursos primarios", "Londres, Reino Unido", "T", 2, "23121002222201122", "D", "", 2, "C"),
 ("totalenergies", "TotalEnergies", "Recursos primarios", "París, Francia", "T", 2, "22121002222201122", "D", "", 2, "C"),
 ("lvmh", "LVMH (familia Arnault)", "Empresa industrial", "París, Francia", "T", 2, "02212011221201012", "D", "", 2, "C"),
 ("rheinmetall", "Rheinmetall", "Empresa de armamento", "Düsseldorf, Alemania", "T", 2, "02120102121200011", "D", "", 2, "E"),
 # Asia y Pacífico
 ("gob_indonesia", "Gobierno de Indonesia", "Gobierno", "Yakarta, Indonesia", "P", 1, "22211220021221211", "D", "", 2, "E"),
 ("pcv", "Partido Comunista de Vietnam", "Partido político", "Hanói, Vietnam", "P", 1, "11211110021121211", "D", "", 1, "E"),
 ("gob_filipinas", "Palacio de Malacañang (Gobierno de Filipinas)", "Gobierno", "Manila, Filipinas", "T", 2, "11211110010121110", "D", "", 2, "C"),
 ("ejercito_tai", "Ejército Real Tailandés", "Ejército", "Bangkok, Tailandia", "P", 2, "11211210120012111", "D", "", 1, "C"),
 ("tatmadaw", "Tatmadaw (Fuerzas Armadas de Myanmar)", "Ejército", "Naipyidó, Myanmar", "E", 2, "21200220110111110", "D", "", 0, "D"),
 ("gob_corea", "Gobierno de Corea del Sur", "Gobierno", "Seúl, Corea del Sur", "T", 2, "02222212022222212", "D", "", 2, "C"),
 ("gob_australia", "Gobierno de Australia", "Gobierno", "Canberra, Australia", "T", 2, "32222111022232212", "D", "", 3, "C"),
 ("bhp", "BHP", "Recursos primarios", "Melbourne, Australia", "T", 2, "32120001211310022", "D", "", 2, "C"),
 ("reliance", "Reliance Industries (familia Ambani)", "Empresa industrial", "Bombay, India", "I", 2, "22211021221202012", "D", "", 1, "E"),
 ("adani", "Grupo Adani", "Empresa industrial", "Ahmedabad, India", "I", 2, "22110011121200022", "D", "", 1, "E"),
 ("kazatomprom", "Kazatomprom", "Recursos primarios", "Astaná, Kazajistán", "P", 2, "31110000110300001", "D", "", 1, "E"),
 ("temasek", "Temasek", "Empresa financiera", "Singapur", "T", 2, "01020001222001002", "D", "", 2, "C"),
 ("petronas", "Petronas", "Recursos primarios", "Kuala Lumpur, Malasia", "P", 2, "22110001211200112", "D", "", 1, "C"),
 ("gob_bangladesh", "Gobierno de Bangladés", "Gobierno", "Daca, Bangladés", "P", 1, "11211110010221110", "D", "", 2, "C"),
 # Medio Oriente y Norteamérica
 ("gob_siria", "Presidencia de Siria", "Gobierno", "Damasco, Siria", "P", 2, "10211110020021110", "D", "", 1, "E"),
 ("gob_irak", "Gobierno de Irak", "Gobierno", "Bagdad, Irak", "P", 2, "21211110120221111", "D", "", 2, "C"),
 ("gob_canada", "Gobierno de Canadá", "Gobierno", "Ottawa, Canadá", "T", 2, "32222111022231212", "D", "", 3, "C"),
]
assert all(len(n[6]) == 17 for n in _NUEVAS) and len(_NUEVAS) == 50
ORGS += [n[:9] for n in _NUEVAS]
FORMAL.update({n[0]: n[9] for n in _NUEVAS})
FASE.update({n[0]: n[10] for n in _NUEVAS})

RELACIONES += [
 ("casarosada", "casablanca", "Alianza", "Milei alineó a la Argentina con EE.UU.; en octubre de 2025 el Tesoro estadounidense firmó un canje de monedas de 20.000 millones de dólares con el Banco Central.", 2),
 ("fmi", "casarosada", "Financiamiento", "Acuerdo de 20.000 millones de dólares en abril de 2025; la Argentina es el mayor deudor del FMI.", 3),
 ("gob_colombia", "casablanca", "Alianza", "Abelardo de la Espriella, presidente desde el 7 de agosto de 2026, opositor de Petro y cercano a Trump.", 2),
 ("gob_colombia", "eln", "Enfrentamiento", "Guerra con la guerrilla en el Catatumbo, Arauca y la frontera con Venezuela.", 2),
 ("gob_colombia", "clan_golfo", "Enfrentamiento", "Principal estructura narcotraficante del país, con control de territorios en el Caribe colombiano.", 2),
 ("casablanca", "miraflores", "Gobierna", "Tras la captura de Maduro, Washington tutela al gobierno interino de Delcy Rodríguez y fija la hoja de ruta de la transición.", 3),
 ("miraflores", "pdvsa", "Propiedad", "Empresa estatal; la reforma de la ley de hidrocarburos de 2026 abrió el sector a inversores extranjeros.", 3),
 ("casablanca", "pcc_cuba", "Enfrentamiento", "Bloqueo petrolero de hecho desde enero de 2026 y presión para un cambio de régimen.", 3),
 ("kremlin", "pcc_cuba", "Alianza", "Aliado histórico; cooperación militar y energética limitada.", 1),
 ("gob_chile", "codelco", "Propiedad", "Empresa estatal; aporta una parte central de la renta del cobre chileno.", 3),
 ("codelco", "consejoestado", "Contrato", "China es el principal comprador del cobre chileno.", 2),
 ("los_lobos", "cjng", "Alianza", "El Tesoro de EE.UU. documentó en 2024 sus vínculos con el CJNG para el tráfico de cocaína.", 2),
 ("gob_ecuador", "los_lobos", "Enfrentamiento", "Guerra interna declarada por Noboa contra las bandas en 2024.", 2),
 ("gob_ecuador", "casablanca", "Alianza", "Cooperación militar y antinarcóticos con EE.UU.; los votantes rechazaron bases extranjeras en el referéndum de noviembre de 2025.", 2),
 ("gob_nigeria", "isis", "Enfrentamiento", "Guerra contra la provincia de África Occidental del Estado Islámico y Boko Haram en el noreste.", 2),
 ("casablanca", "gob_nigeria", "Ambigua", "Trump amenazó en noviembre de 2025 con intervenir por la violencia contra cristianos.", 1),
 ("dangote", "gob_nigeria", "Alianza", "La refinería Dangote, la mayor de África, es central para la política energética nigeriana.", 2),
 ("gob_sudafrica", "brics", "Alianza", "Miembro fundador ampliado de los BRICS.", 3),
 ("casablanca", "gob_sudafrica", "Enfrentamiento", "Aranceles, recortes de ayuda y boicot de EE.UU. a la cumbre del G20 en Johannesburgo en 2025.", 1),
 ("gob_etiopia", "ffaa_egipto", "Enfrentamiento", "Disputa por la Gran Represa del Renacimiento sobre el Nilo, inaugurada en 2025.", 1),
 ("gob_ruanda", "m23", "Abastecimiento", "Expertos de la ONU documentaron apoyo militar ruandés al M23; Ruanda lo niega.", 3),
 ("althani", "m23", "Ambigua", "Catar media entre el gobierno congoleño y el M23 desde 2025 (marco de Doha).", 1),
 ("saf", "far_sudan", "Enfrentamiento", "Guerra civil desde abril de 2023.", 3),
 ("ffaa_egipto", "saf", "Alianza", "Egipto respalda al ejército sudanés.", 2),
 ("majzen", "casablanca", "Alianza", "EE.UU. reconoció en 2020 la soberanía marroquí sobre el Sáhara Occidental a cambio de la normalización con Israel.", 2),
 ("majzen", "ocp", "Propiedad", "El Estado marroquí controla la empresa que administra las mayores reservas de fosfato del mundo.", 3),
 ("sonatrach", "chigi", "Contrato", "Argelia es el principal proveedor de gas de Italia por gasoducto desde 2022.", 2),
 ("lna", "africacorps", "Alianza", "Presencia militar rusa en bases bajo control de Haftar.", 2),
 ("alnahyan", "lna", "Abastecimiento", "Paneles de la ONU documentaron apoyo militar emiratí a Haftar.", 2),
 ("pentagono", "alshabaab", "Enfrentamiento", "Bombardeos de EE.UU. en Somalia contra Al Shabaab y el Estado Islámico.", 2),
 ("aes", "africacorps", "Alianza", "Las juntas de Malí, Burkina Faso y Níger dependen de la protección militar rusa.", 3),
 ("aes", "jnim", "Enfrentamiento", "Guerra contra el JNIM y el Estado Islámico en el Sahel central.", 3),
 ("aes", "eliseo", "Enfrentamiento", "Expulsión de las tropas francesas de los tres países entre 2022 y 2025.", 2),
 ("chigi", "casablanca", "Alianza", "Meloni, aliada cercana de Trump dentro de la Unión Europea.", 2),
 ("moncloa", "otan", "Ambigua", "España rechazó en 2025 la meta de gasto militar del 5 %.", 1),
 ("gob_polonia", "otan", "Alianza", "El país de la OTAN que más gasta en defensa en proporción a su PBI.", 3),
 ("hanwha", "gob_polonia", "Abastecimiento", "Contratos de obuses K9 y tanques K2 desde 2022.", 2),
 ("gob_hungria", "comisioneu", "Alianza", "Magyar prometió reconstruir la relación con la UE tras su victoria de abril de 2026.", 2),
 ("shell", "gob_nigeria", "Contrato", "Décadas de operación en el delta del Níger, con litigios por derrames.", 2),
 ("totalenergies", "eliseo", "Alianza", "Principal empresa energética francesa y brazo de la diplomacia económica de París.", 2),
 ("rheinmetall", "kanzleramt", "Abastecimiento", "Principal beneficiaria del rearme alemán.", 3),
 ("rheinmetall", "ffaa_ucrania", "Abastecimiento", "Munición de artillería y vehículos para Ucrania.", 2),
 ("gob_indonesia", "brics", "Alianza", "Miembro pleno desde enero de 2025.", 2),
 ("consejoestado", "gob_indonesia", "Financiamiento", "Inversión china en el procesamiento de níquel indonesio.", 2),
 ("pcv", "pcch", "Alianza", "Partidos hermanos con cooperación económica estrecha.", 2),
 ("epl", "pcv", "Enfrentamiento", "Disputa por islas del mar de China Meridional.", 1),
 ("gob_filipinas", "casablanca", "Alianza", "Tratado de defensa mutua y acceso militar de EE.UU. a nueve bases.", 3),
 ("epl", "gob_filipinas", "Enfrentamiento", "Choques en el mar de China Meridional, en especial en torno al banco Scarborough.", 2),
 ("ejercito_tai", "casablanca", "Alianza", "Aliado formal de EE.UU. desde 1954.", 1),
 ("consejoestado", "tatmadaw", "Alianza", "China es el principal sostén diplomático y económico de la junta.", 2),
 ("ffaa_rusia", "tatmadaw", "Abastecimiento", "Rusia es su principal proveedor de aviones de combate.", 2),
 ("gob_corea", "casablanca", "Alianza", "Tratado de defensa y unos 28.500 soldados de EE.UU. en el país.", 3),
 ("gob_corea", "ptk", "Enfrentamiento", "Guerra no terminada desde el armisticio de 1953.", 2),
 ("gob_australia", "casablanca", "Alianza", "Pacto AUKUS para submarinos nucleares con EE.UU. y Reino Unido.", 3),
 ("bhp", "consejoestado", "Contrato", "China compra la mayor parte del mineral de hierro australiano.", 2),
 ("reliance", "rosneft", "Contrato", "Acuerdo de suministro de crudo ruso de 2024; India es el mayor comprador marítimo de petróleo ruso.", 2),
 ("reliance", "gob_india", "Alianza", "Mukesh Ambani, cercano al gobierno de Modi.", 2),
 ("adani", "gob_india", "Alianza", "Puertos, aeropuertos y energía otorgados en concesión bajo el gobierno de Modi.", 2),
 ("doj", "adani", "Enfrentamiento", "Acusación en Nueva York en 2024 por presuntos sobornos; el grupo la niega.", 1),
 ("kazatomprom", "consejoestado", "Contrato", "China es destino principal del uranio kazajo.", 2),
 ("gob_bangladesh", "gob_india", "Enfrentamiento", "India alberga a Sheikh Hasina, condenada en Bangladés.", 1),
 ("gob_siria", "turquia", "Alianza", "Turquía es el principal sostén militar y político del nuevo gobierno.", 3),
 ("gob_siria", "casablanca", "Alianza", "EE.UU. levantó las sanciones en 2025 y respaldó la integración de las fuerzas kurdas al ejército sirio.", 2),
 ("fdi", "gob_siria", "Enfrentamiento", "Bombardeos y ocupación de una zona de amortiguación en el sur de Siria desde diciembre de 2024.", 1),
 ("gob_irak", "pmf", "Ambigua", "Las milicias dependen formalmente del primer ministro pero responden a sus propios mandos.", 2),
 ("casablanca", "gob_irak", "Alianza", "Washington respaldó la designación de Ali al-Zaidi en 2026.", 1),
 ("gob_canada", "casablanca", "Ambigua", "Socio histórico enfrentado por aranceles y las amenazas de anexión de Trump.", 2),
 ("gob_canada", "otan", "Alianza", "Miembro fundador.", 2),
]

# ---------- Revisión del 2026-11-16: menos Estados formales, más actores con poder real ----------
# Se quitan los gobiernos de países que no son centros del orden mundial y se reemplazan
# por quienes ejercen el poder: personas, partidos, sindicatos, organismos internos, ejércitos y empresas.
AREA_TIPO.update({"Persona": "Persona", "Sindicato": "Influencia", "Organismo de gobierno": "Estado", "Federación empresaria": "Influencia"})

_QUITAR = ("pm_israel downing turquia gob_indonesia planalto gob_australia gob_canada gob_corea gob_sudafrica eliseo "
           "gob_nigeria moncloa chigi gob_etiopia gob_chile gob_ruanda gob_bangladesh gob_colombia casarosada gob_irak "
           "gob_polonia ucrania kanzleramt kantei gob_kenia gob_filipinas gob_hungria gob_ecuador gob_siria miraflores taiwan").split()

# id, nombre, área, sede, bloque, autonomía, puntajes, certeza, depende de, poder formal, fase
_REAL = [
 # Personas
 ("musk", "Elon Musk", "Persona", "Starbase, EE.UU.", "T", 1, "01113022131001113", "D", "", 0, "E"),
 ("thiel", "Peter Thiel", "Persona", "San Francisco, EE.UU.", "T", 1, "01022012132002102", "D", "", 0, "E"),
 ("ellison", "Larry y David Ellison", "Persona", "Austin, EE.UU.", "T", 1, "02122032233102003", "D", "", 0, "E"),
 ("bezos", "Jeff Bezos", "Persona", "Miami, EE.UU.", "T", 1, "01112021131101013", "D", "", 0, "C"),
 ("zuckerberg", "Mark Zuckerberg", "Persona", "Menlo Park, EE.UU.", "T", 1, "01112011131001103", "D", "", 0, "C"),
 ("m_ambani", "Mukesh Ambani", "Persona", "Bombay, India", "I", 1, "01011011131001003", "D", "", 0, "E"),
 ("arnault", "Bernard Arnault", "Persona", "París, Francia", "T", 1, "01012010131000003", "D", "", 0, "C"),
 ("milei", "Javier Milei", "Persona", "Buenos Aires, Argentina", "T", 2, "11112120021021211", "D", "", 2, "C"),
 ("erdogan", "Recep Tayyip Erdoğan", "Persona", "Ankara, Turquía", "P", 1, "11212220021121211", "D", "", 1, "E"),
 ("netanyahu", "Benjamín Netanyahu", "Persona", "Jerusalén, Israel", "T", 2, "01111111021011111", "D", "", 2, "D"),
 ("lula", "Luiz Inácio Lula da Silva", "Persona", "Brasilia, Brasil", "I", 1, "11111110021121211", "D", "", 2, "C"),
 ("prabowo", "Prabowo Subianto", "Persona", "Yakarta, Indonesia", "P", 1, "11111110021111211", "D", "", 2, "E"),
 ("zelenski", "Volodímir Zelenski", "Persona", "Kiev, Ucrania", "T", 2, "00112210021021110", "D", "", 2, "C"),
 ("sharaa", "Ahmed al-Sharaa", "Persona", "Damasco, Siria", "P", 2, "10211110020021110", "D", "", 1, "E"),
 ("delcy", "Delcy Rodríguez", "Persona", "Caracas, Venezuela", "T", 3, "21201120010021110", "D", "casablanca", 1, "D"),
 ("kagame", "Paul Kagame", "Persona", "Kigali, Ruanda", "P", 1, "10111110011011110", "D", "", 1, "E"),
 # Sindicatos
 ("cgt_arg", "CGT (Confederación General del Trabajo, Argentina)", "Sindicato", "Buenos Aires, Argentina", "P", 1, "01211010120000111", "D", "", 2, "D"),
 ("cosatu", "COSATU (Sudáfrica)", "Sindicato", "Johannesburgo, Sudáfrica", "P", 2, "01211010020000110", "D", "", 2, "D"),
 ("aflcio", "AFL-CIO", "Sindicato", "Washington, EE.UU.", "T", 2, "01311010120000101", "D", "", 2, "D"),
 ("igmetall", "IG Metall", "Sindicato", "Fráncfort, Alemania", "T", 2, "01321010120000201", "D", "", 2, "C"),
 ("cut_br", "CUT (Central Única dos Trabalhadores, Brasil)", "Sindicato", "São Paulo, Brasil", "I", 2, "01311010020000110", "D", "", 2, "C"),
 # Organismos internos
 ("tesoro_eeuu", "Tesoro de EE.UU. (con la OFAC)", "Organismo de gobierno", "Washington, EE.UU.", "T", 3, "01131011033003303", "D", "casablanca", 2, "C"),
 ("bis", "Oficina de Industria y Seguridad (controles de exportación de EE.UU.)", "Organismo de gobierno", "Washington, EE.UU.", "T", 3, "00020010022002300", "D", "casablanca", 2, "E"),
 ("ccdi", "Comisión Central de Inspección Disciplinaria del PCCh", "Organismo de gobierno", "Pekín, China", "E", 3, "00121110032003300", "D", "pcch", 1, "C"),
 ("consejo_seg_rusia", "Consejo de Seguridad de Rusia", "Organismo de gobierno", "Moscú, Rusia", "E", 3, "00020110032002200", "D", "kremlin", 1, "C"),
 ("city_londres", "City de Londres (City of London Corporation)", "Organismo de gobierno", "Londres, Reino Unido", "T", 2, "02021011132011202", "D", "", 1, "C"),
 # Inteligencia
 ("shinbet", "Shin Bet (seguridad interior de Israel)", "Servicio de inteligencia", "Tel Aviv, Israel", "T", 3, "00120111022012100", "D", "netanyahu", 0, "D"),
 ("bnd", "BND (inteligencia exterior de Alemania)", "Servicio de inteligencia", "Berlín, Alemania", "T", 2, "00120001022002000", "D", "", 1, "C"),
 ("nis_corea", "NIS (inteligencia de Corea del Sur)", "Servicio de inteligencia", "Seúl, Corea del Sur", "T", 2, "00120011022002000", "D", "", 1, "C"),
 ("gur", "GUR (inteligencia militar de Ucrania)", "Servicio de inteligencia", "Kiev, Ucrania", "T", 3, "00120212022002010", "D", "zelenski", 0, "E"),
 # Partidos
 ("ldp", "Partido Liberal Democrático de Japón", "Partido político", "Tokio, Japón", "T", 2, "01211010021021201", "D", "", 2, "C"),
 ("anc", "ANC (Congreso Nacional Africano)", "Partido político", "Johannesburgo, Sudáfrica", "P", 1, "01212010020020200", "D", "", 2, "D"),
 ("bnp", "BNP (Partido Nacionalista de Bangladés)", "Partido político", "Daca, Bangladés", "P", 1, "01211010020020200", "D", "", 2, "C"),
 ("tisza", "Tisza (partido de Péter Magyar)", "Partido político", "Budapest, Hungría", "T", 2, "00101010020010100", "D", "", 2, "E"),
 ("prosperidad", "Partido de la Prosperidad (Etiopía)", "Partido político", "Adís Abeba, Etiopía", "P", 1, "11211110020021200", "D", "", 1, "C"),
 ("fpr", "Frente Patriótico Ruandés", "Partido político", "Kigali, Ruanda", "P", 3, "01111110120011101", "D", "kagame", 1, "E"),
 ("psuv", "PSUV (Partido Socialista Unido de Venezuela)", "Partido político", "Caracas, Venezuela", "T", 2, "00201110010012100", "D", "", 1, "D"),
 ("fpa", "Frente Parlamentaria Agropecuaria (bancada ruralista de Brasil)", "Partido político", "Brasilia, Brasil", "I", 1, "10111010020000200", "D", "", 2, "C"),
 ("marco_coord", "Marco de Coordinación (alianza chiita de Irak)", "Partido político", "Bagdad, Irak", "P", 1, "20101110120021201", "D", "", 1, "C"),
 # Empresas y grupos familiares
 ("softbank", "SoftBank (Masayoshi Son)", "Empresa financiera", "Tokio, Japón", "T", 1, "01121012132001003", "D", "", 2, "E"),
 ("brookfield", "Brookfield", "Empresa financiera", "Toronto, Canadá", "T", 2, "13120001122100013", "D", "", 2, "C"),
 ("techint", "Techint (familia Rocca)", "Empresa industrial", "Buenos Aires, Argentina", "T", 2, "12120001121200011", "D", "", 1, "C"),
 ("inditex", "Inditex (familia Ortega)", "Empresa industrial", "Arteixo, España", "T", 2, "02212011121201022", "D", "", 2, "C"),
 ("santander", "Banco Santander (familia Botín)", "Empresa financiera", "Madrid, España", "T", 2, "01221011222002003", "D", "", 2, "C"),
 ("exor", "Exor (familia Agnelli-Elkann)", "Familia y oficina patrimonial", "Ámsterdam, Países Bajos", "T", 2, "02112011121100012", "D", "", 1, "C"),
 ("eni", "ENI", "Recursos primarios", "Roma, Italia", "T", 2, "22120001121200012", "D", "", 2, "C"),
 ("hyundai", "Grupo Hyundai Motor", "Empresa industrial", "Seúl, Corea del Sur", "T", 2, "02221002121200022", "D", "", 2, "C"),
 ("foxconn", "Foxconn (Hon Hai)", "Empresa tecnológica", "Nuevo Taipéi, Taiwán", "T", 2, "02220002121300012", "D", "", 2, "C"),
 ("baykar", "Baykar (familia Bayraktar)", "Empresa de armamento", "Estambul, Turquía", "P", 2, "01121102121201011", "D", "", 1, "E"),
 ("nnpc", "NNPC (petrolera estatal de Nigeria)", "Recursos primarios", "Abuya, Nigeria", "P", 2, "22110000110200111", "D", "", 1, "C"),
 ("aval", "Grupo Aval (familia Sarmiento)", "Empresa financiera", "Bogotá, Colombia", "T", 2, "01111010121001002", "D", "", 2, "C"),
 ("luksic", "Grupo Luksic", "Familia y oficina patrimonial", "Santiago, Chile", "T", 2, "22110010121100012", "D", "", 1, "C"),
 ("hancock", "Hancock Prospecting (Gina Rinehart)", "Recursos primarios", "Perth, Australia", "T", 2, "21011010120100012", "D", "", 0, "C"),
 ("porsche_se", "Porsche SE (familias Porsche y Piëch)", "Familia y oficina patrimonial", "Stuttgart, Alemania", "T", 2, "02221002121200022", "D", "", 2, "C"),
 ("bollore", "Grupo Bolloré", "Familia y oficina patrimonial", "París, Francia", "T", 2, "01112020121001022", "D", "", 1, "E"),
 ("dassault", "Grupo Dassault", "Empresa de armamento", "París, Francia", "T", 2, "01121112121200012", "D", "", 2, "C"),
 ("safaricom", "Safaricom (M-Pesa)", "Empresa tecnológica", "Nairobi, Kenia", "T", 2, "01011011111002101", "D", "", 2, "C"),
 ("noboa_grupo", "Grupo Noboa", "Familia y oficina patrimonial", "Guayaquil, Ecuador", "T", 2, "11100000120100011", "D", "", 1, "C"),
 ("danantara", "Danantara (fondo soberano de Indonesia)", "Empresa financiera", "Yakarta, Indonesia", "P", 3, "12110000121100002", "D", "prabowo", 1, "E"),
 ("keidanren", "Keidanren (federación empresaria de Japón)", "Federación empresaria", "Tokio, Japón", "T", 2, "00121010031000201", "D", "", 2, "C"),
 # Fuerzas armadas
 ("ffaa_reinounido", "Fuerzas Armadas del Reino Unido", "Ejército", "Londres, Reino Unido", "T", 2, "02221302022102021", "D", "", 2, "C"),
 ("ffaa_francia", "Fuerzas Armadas de Francia", "Ejército", "París, Francia", "T", 2, "02221302022102021", "D", "", 2, "C"),
 ("bundeswehr", "Bundeswehr (Fuerzas Armadas de Alemania)", "Ejército", "Berlín, Alemania", "T", 2, "02220201021001011", "D", "", 3, "E"),
 ("jsdf", "Fuerzas de Autodefensa de Japón", "Ejército", "Tokio, Japón", "T", 2, "02220201022101011", "D", "", 2, "E"),
 ("ffaa_taiwan", "Fuerzas Armadas de Taiwán", "Ejército", "Taipéi, Taiwán", "T", 2, "01210201021011010", "D", "", 2, "C"),
 ("ffaa_filipinas", "Fuerzas Armadas de Filipinas", "Ejército", "Manila, Filipinas", "T", 2, "01210100010011010", "D", "", 2, "C"),
 ("ffaa_corea", "Fuerzas Armadas de Corea del Sur", "Ejército", "Seúl, Corea del Sur", "T", 2, "02220202022102011", "D", "", 2, "C"),
 ("adf", "Fuerzas de Defensa de Australia", "Ejército", "Canberra, Australia", "T", 2, "01120201022001021", "D", "", 3, "E"),
 ("ffaa_polonia", "Fuerzas Armadas de Polonia", "Ejército", "Varsovia, Polonia", "T", 2, "01210200021001011", "D", "", 2, "E"),
 ("ffmm_colombia", "Fuerzas Militares de Colombia", "Ejército", "Bogotá, Colombia", "T", 2, "01210200021012010", "D", "", 2, "C"),
 ("fanb", "FANB (Fuerza Armada de Venezuela)", "Ejército", "Caracas, Venezuela", "T", 3, "11200110110021110", "D", "delcy", 1, "D"),
 ("tni", "TNI (Fuerzas Armadas de Indonesia)", "Ejército", "Yakarta, Indonesia", "P", 3, "11210210120021110", "D", "prabowo", 1, "E"),
 # Religión
 ("hawza_najaf", "Hawza de Nayaf (gran ayatolá Sistani)", "Organización religiosa", "Nayaf, Irak", "X", 1, "01222010120000201", "D", "", 1, "D"),
]
assert all(len(n[6]) == 17 for n in _REAL) and len(_REAL) == 73

_MAPA = {"pm_israel": "netanyahu", "turquia": "erdogan", "planalto": "lula", "gob_indonesia": "prabowo", "ucrania": "zelenski",
         "gob_siria": "sharaa", "miraflores": "delcy", "gob_ruanda": "kagame", "casarosada": "milei", "gob_bangladesh": "bnp",
         "gob_hungria": "tisza", "gob_etiopia": "prosperidad", "kantei": "jsdf", "kanzleramt": "bundeswehr", "eliseo": "ffaa_francia",
         "downing": "ffaa_reinounido", "taiwan": "ffaa_taiwan", "gob_filipinas": "ffaa_filipinas", "gob_corea": "ffaa_corea",
         "gob_australia": "adf", "gob_polonia": "ffaa_polonia", "gob_colombia": "ffmm_colombia", "gob_irak": "marco_coord",
         "gob_nigeria": "nnpc", "chigi": "eni"}
_SIN_PAR = {("telegram", "eliseo"), ("totalenergies", "eliseo"), ("gob_nigeria", "isis"), ("casablanca", "gob_nigeria"),
            ("dangote", "gob_nigeria"), ("casablanca", "gob_sudafrica"), ("gob_sudafrica", "brics"), ("chigi", "casablanca"),
            ("casablanca", "kanzleramt"), ("pt_br", "planalto")}
_TEXTO = {("gob_colombia", "casablanca"): "Principal socio militar de EE.UU. en Sudamérica; cooperación antinarcóticos desde el Plan Colombia.",
          ("gob_irak", "pmf"): "La alianza chiita que designa al primer ministro tiene sus propias milicias dentro de las Fuerzas de Movilización Popular.",
          ("turquia", "otan"): "Erdoğan conduce el segundo ejército de la OTAN con política exterior propia.",
          ("gob_polonia", "otan"): "Las fuerzas armadas del país de la OTAN que más gasta en defensa en proporción a su PBI.",
          ("gob_australia", "casablanca"): "Pacto AUKUS para submarinos nucleares con EE.UU. y Reino Unido.",
          ("casablanca", "gob_irak"): "Washington vetó a Nuri al-Maliki y respaldó en 2026 a Ali al-Zaidi, candidato de consenso de la alianza."}

def _remap(i): return _MAPA.get(i, i)
_nuevas_rel = []
for r in RELACIONES:
    a, b = r[0], r[1]
    if (a, b) in _SIN_PAR: continue
    if (a in _QUITAR and a not in _MAPA) or (b in _QUITAR and b not in _MAPA): continue
    x = _TEXTO.get((a, b), r[3])
    _nuevas_rel.append((_remap(a), _remap(b), r[2], x, r[4]))
RELACIONES = _nuevas_rel

ORGS = [o for o in ORGS if o[0] not in _QUITAR]
_DEP = {"fdi": "netanyahu", "mossad": "netanyahu", "ffaa_ucrania": "zelenski", "mi6": "", "gchq": "", "dgse": "", "mit_tr": "erdogan",
        "petrobras": "lula", "pdvsa": "delcy", "codelco": "", "m23": "kagame", "spacex": "musk", "meta": "zuckerberg",
        "reliance": "m_ambani", "lvmh": "arnault"}
_AUT = {"codelco": 2, "spacex": 3, "meta": 3, "reliance": 3, "lvmh": 3}
ORGS = [(o[:5] + (_AUT.get(o[0], o[5]),) + o[6:8] + (_DEP[o[0]],)) if o[0] in _DEP else o for o in ORGS]
ORGS += [n[:9] for n in _REAL]
FORMAL.update({n[0]: n[9] for n in _REAL})
FASE.update({n[0]: n[10] for n in _REAL})

RELACIONES += [
 ("musk", "casablanca", "Ambigua", "Dirigió el recorte del Estado (DOGE) en 2025 y luego rompió con Trump; SpaceX es contratista clave del Pentágono y la NASA.", 2),
 ("musk", "tesoro_eeuu", "Ambigua", "Sus empresas dependen de contratos y regulaciones federales.", 1),
 ("thiel", "palantir", "Propiedad", "Cofundador y presidente del directorio de Palantir.", 3),
 ("thiel", "casablanca", "Alianza", "Financió la carrera política del vicepresidente J. D. Vance.", 2),
 ("ellison", "bytedance", "Contrato", "Oracle es socio de seguridad y accionista del 15 % de TikTok USDS en EE.UU.", 2),
 ("ellison", "casablanca", "Alianza", "Cercanía con Trump; el gobierno aprobó la fusión de Paramount con Warner Bros. Discovery.", 2),
 ("ellison", "openai", "Contrato", "Oracle construye centros de datos para OpenAI en el proyecto Stargate.", 2),
 ("bezos", "amazon", "Propiedad", "Fundador, presidente ejecutivo y mayor accionista individual.", 3),
 ("zuckerberg", "casablanca", "Ambigua", "Acercamiento a Trump desde 2025 tras años de enfrentamiento.", 1),
 ("softbank", "openai", "Financiamiento", "Más de 60.000 millones de dólares comprometidos por cerca del 13 % de OpenAI.", 3),
 ("m_ambani", "lider_iran", "Ambigua", "", 1),
 ("arnault", "casablanca", "Alianza", "Relación personal con Trump; inversiones de LVMH en EE.UU.", 1),
 ("milei", "casablanca", "Alianza", "Alineamiento con Trump; canje de 20.000 millones de dólares del Tesoro de EE.UU. en 2025.", 3),
 ("tesoro_eeuu", "milei", "Financiamiento", "Canje de monedas de 20.000 millones de dólares con el Banco Central argentino en octubre de 2025.", 3),
 ("cgt_arg", "milei", "Enfrentamiento", "Paros generales y movilizaciones contra la reforma laboral.", 2),
 ("techint", "milei", "Ambigua", "Paolo Rocca, el empresario más poderoso de la Argentina, con relación cambiante con el gobierno.", 1),
 ("erdogan", "baykar", "Alianza", "Selçuk Bayraktar, accionista de Baykar, es yerno de Erdoğan.", 3),
 ("erdogan", "sharaa", "Alianza", "Turquía es el principal sostén militar del nuevo gobierno sirio.", 3),
 ("netanyahu", "casablanca", "Alianza", "Coordinación estrecha con Trump en la guerra contra Irán.", 3),
 ("shinbet", "hamas", "Enfrentamiento", "Inteligencia y operaciones contra Hamás en Gaza y Cisjordania.", 3),
 ("lula", "pt_br", "Alianza", "Líder histórico del PT.", 3),
 ("lula", "cut_br", "Alianza", "Lula surgió del sindicalismo metalúrgico que dio origen a la CUT.", 2),
 ("fpa", "lula", "Ambigua", "La bancada agropecuaria, la más grande del Congreso, condiciona al gobierno.", 2),
 ("delcy", "fanb", "Gobierna", "La Fuerza Armada juró lealtad a Rodríguez; en marzo de 2026 ella reemplazó al ministro de Defensa Padrino López.", 3),
 ("psuv", "delcy", "Ambigua", "Diosdado Cabello, vicepresidente del partido y ministro del Interior, es el otro polo de poder del chavismo.", 2),
 ("zelenski", "gur", "Gobierna", "El exjefe del GUR, Kirilo Budánov, dirige la Oficina del Presidente desde enero de 2026.", 3),
 ("prabowo", "danantara", "Gobierna", "Fondo soberano creado en 2025 bajo control presidencial.", 3),
 ("prabowo", "tni", "Gobierna", "Exgeneral; amplió el papel de los militares en el gobierno civil.", 3),
 ("kagame", "fpr", "Gobierna", "Lidera el partido que gobierna Ruanda desde 1994.", 3),
 ("anc", "cosatu", "Alianza", "Alianza tripartita con el Partido Comunista.", 2),
 ("ldp", "keidanren", "Alianza", "La federación empresaria es el principal apoyo del partido gobernante.", 2),
 ("ldp", "jsdf", "Gobierna", "El gobierno del LDP impulsa la expansión militar.", 2),
 ("igmetall", "porsche_se", "Ambigua", "Cogestión: el sindicato tiene la mitad de los asientos del consejo de vigilancia de Volkswagen.", 2),
 ("aflcio", "dem", "Alianza", "Principal aliado sindical del Partido Demócrata.", 2),
 ("bis", "huawei", "Enfrentamiento", "Lista negra de exportaciones desde 2019.", 3),
 ("bis", "smic", "Enfrentamiento", "Restricciones a la venta de equipos para chips avanzados.", 3),
 ("bis", "nvidia", "Ambigua", "Autoriza o prohíbe las ventas de chips de inteligencia artificial a China.", 3),
 ("tesoro_eeuu", "rosneft", "Enfrentamiento", "Sanciones de octubre de 2025.", 3),
 ("tesoro_eeuu", "prince", "Enfrentamiento", "Sanciones de octubre de 2025 a 146 personas y empresas del grupo.", 3),
 ("ccdi", "epl", "Enfrentamiento", "Purgas anticorrupción en la cúpula militar desde 2023.", 2),
 ("consejo_seg_rusia", "ffaa_rusia", "Gobierna", "Coordina la política de seguridad; Serguéi Shoigú es su secretario.", 2),
 ("city_londres", "jpmorgan", "Ambigua", "Sede europea de la banca de inversión estadounidense.", 1),
 ("brookfield", "blackrock", "Ambigua", "Competidores y socios en infraestructura global.", 1),
 ("exor", "ffaa_francia", "Ambigua", "", 1),
 ("bollore", "ffaa_francia", "Ambigua", "", 1),
 ("dassault", "ffaa_francia", "Abastecimiento", "Fabrica el Rafale, avión de combate de la aviación francesa con capacidad nuclear.", 3),
 ("dassault", "gob_india", "Contrato", "India compró aviones Rafale para su fuerza aérea y su marina.", 2),
 ("eni", "sonatrach", "Contrato", "Socia histórica en gas argelino.", 2),
 ("inditex", "santander", "Ambigua", "", 1),
 ("hyundai", "ffaa_corea", "Abastecimiento", "Hyundai Rotem fabrica los tanques K2.", 2),
 ("foxconn", "apple", "Contrato", "Ensambla la mayoría de los iPhone.", 3),
 ("nnpc", "dangote", "Propiedad", "NNPC es accionista minoritaria de la refinería Dangote.", 2),
 ("ffmm_colombia", "eln", "Enfrentamiento", "Combates en el Catatumbo y la frontera.", 2),
 ("aval", "ffmm_colombia", "Ambigua", "", 1),
 ("luksic", "codelco", "Ambigua", "", 1),
 ("hancock", "bhp", "Ambigua", "", 1),
 ("safaricom", "gob_india", "Ambigua", "", 1),
 ("noboa_grupo", "los_lobos", "Ambigua", "", 1),
 ("marco_coord", "pmf", "Alianza", "Las principales facciones de la alianza tienen milicias propias.", 3),
 ("hawza_najaf", "marco_coord", "Ambigua", "El gran ayatolá Sistani avala o veta de hecho a los gobiernos de Bagdad.", 2),
 ("hawza_najaf", "pmf", "Alianza", "Su fatwa de 2014 dio origen a la movilización contra el Estado Islámico.", 2),
 ("ffaa_reinounido", "otan", "Alianza", "Potencia nuclear de la OTAN.", 3),
 ("ffaa_francia", "otan", "Alianza", "Potencia nuclear de la OTAN.", 3),
 ("bundeswehr", "otan", "Alianza", "Rearme alemán con fondos especiales desde 2022 y 2025.", 2),
 ("pentagono", "bundeswehr", "Alianza", "Tropas y bases de EE.UU. en Alemania, como Ramstein.", 2),
 ("bnd", "cia", "Alianza", "Cooperación histórica en inteligencia.", 2),
 ("nis_corea", "ptk", "Enfrentamiento", "Inteligencia y contrainteligencia frente a Corea del Norte.", 2),
 ("tisza", "otan", "Alianza", "Magyar prometió reconstruir la relación con la OTAN.", 1),
 ("prosperidad", "ffaa_egipto", "Enfrentamiento", "Disputa por la Gran Represa del Renacimiento.", 1),
 ("bnp", "gob_india", "Enfrentamiento", "India alberga a Sheikh Hasina, condenada en Bangladés.", 1),
]
RELACIONES = [r for r in RELACIONES if r[3]]  # se descartan los vínculos sin explicación documentada

# ---------- Ampliación de relaciones y Fuerzas Armadas de la India (2026-11-16) ----------
ORGS += [("ffaa_india", "Fuerzas Armadas de la India", "Ejército", "Nueva Delhi, India", "I", 3, "12321201021111021", "D", "gob_india")]
FORMAL["ffaa_india"] = 2; FASE["ffaa_india"] = "E"
_MAS = [
 ("ffaa_india", "ejercito_pak", "Enfrentamiento", "Choque armado de mayo de 2025 tras el atentado de Pahalgam.", 3),
 ("epl", "ffaa_india", "Enfrentamiento", "Frontera en disputa en el Himalaya; enfrentamiento mortal en Galwan en 2020.", 2),
 ("ffaa_rusia", "ffaa_india", "Abastecimiento", "Sistemas antiaéreos S-400 y buena parte del arsenal indio de origen ruso.", 2),
 ("vanguard", "apple", "Propiedad", "Uno de los mayores accionistas institucionales.", 2),
 ("blackrock", "msc", "Alianza", "Consorcio para comprar los puertos de CK Hutchison anunciado en 2025.", 2),
 ("microsoft", "openai", "Propiedad", "Conserva cerca del 27 % de OpenAI tras la reestructuración de 2025.", 3),
 ("nvidia", "openai", "Financiamiento", "Acuerdo de 2025 para invertir hasta 100.000 millones de dólares en OpenAI.", 2),
 ("alnahyan", "openai", "Financiamiento", "El fondo emiratí MGX es socio de Stargate e inversor de OpenAI.", 2),
 ("alnahyan", "bytedance", "Propiedad", "MGX tiene el 15 % de TikTok USDS en EE.UU.", 2),
 ("thiel", "anduril", "Financiamiento", "Founders Fund, de Thiel, lideró rondas de inversión de Anduril.", 2),
 ("tesoro_eeuu", "kremlin", "Enfrentamiento", "Sanciones sobre bancos, energía y grandes fortunas rusas desde 2022.", 3),
 ("tesoro_eeuu", "lider_iran", "Enfrentamiento", "Sanciones sobre el petróleo y la banca de Irán.", 3),
 ("bis", "tsmc", "Ambigua", "Las reglas de exportación de EE.UU. limitan qué chips puede fabricar TSMC para clientes chinos.", 2),
 ("bis", "asml", "Ambigua", "EE.UU. presionó a los Países Bajos para restringir las ventas de ASML a China.", 2),
 ("bollore", "msc", "Contrato", "Vendió su red logística africana a MSC en 2022.", 2),
 ("foxconn", "nvidia", "Contrato", "Fabrica servidores de inteligencia artificial para Nvidia.", 2),
 ("foxconn", "consejoestado", "Ambigua", "Sus mayores plantas están en China continental.", 2),
 ("samsung", "nvidia", "Contrato", "Proveedor de memoria de alto rendimiento para chips de inteligencia artificial.", 2),
 ("tsmc", "apple", "Contrato", "Principal fabricante de los chips de Apple.", 3),
 ("hanwha", "ffaa_corea", "Abastecimiento", "Obuses K9 y sistemas espaciales para las fuerzas surcoreanas.", 2),
 ("baykar", "ffaa_ucrania", "Abastecimiento", "Drones Bayraktar TB2 usados por Ucrania desde 2022.", 2),
 ("lockheed", "ffaa_polonia", "Abastecimiento", "Aviones F-35 y lanzacohetes HIMARS.", 2),
 ("lockheed", "jsdf", "Abastecimiento", "Japón es uno de los mayores compradores del F-35.", 2),
 ("lockheed", "adf", "Abastecimiento", "Aviones F-35 para Australia.", 2),
 ("rtx", "ffaa_ucrania", "Abastecimiento", "Sistemas antiaéreos Patriot.", 2),
 ("dassault", "ffaa_egipto", "Abastecimiento", "Egipto compró aviones Rafale.", 2),
 ("totalenergies", "aramco", "Contrato", "Socias en la refinería SATORP de Jubail.", 2),
 ("pif", "softbank", "Financiamiento", "Mayor inversor externo del primer Vision Fund.", 2),
 ("brookfield", "microsoft", "Contrato", "Acuerdo de 2024 para abastecer de energía renovable a los centros de datos de Microsoft.", 2),
 ("blackrock", "microsoft", "Alianza", "Fondo conjunto de infraestructura para inteligencia artificial con MGX desde 2024.", 2),
 ("cut_br", "pt_br", "Alianza", "Base sindical histórica del PT.", 3),
 ("keidanren", "toyota", "Alianza", "Toyota es uno de los miembros dirigentes de la federación.", 2),
 ("hawza_najaf", "lider_iran", "Ambigua", "Rivalidad de autoridad religiosa entre Nayaf y el líder supremo iraní.", 2),
 ("psuv", "pcc_cuba", "Alianza", "Alianza histórica entre el chavismo y el castrismo.", 2),
 ("gur", "ffaa_rusia", "Enfrentamiento", "Sabotajes y ataques dentro de Rusia.", 3),
 ("consejo_seg_rusia", "fsb", "Gobierna", "Coordina a los servicios de seguridad bajo la autoridad de Putin.", 2),
 ("ellison", "dem", "Enfrentamiento", "Doce fiscales generales demócratas demandaron para frenar la compra de Warner Bros. Discovery.", 1),
]
_ya = {(r[0], r[1]) for r in RELACIONES} | {(r[1], r[0]) for r in RELACIONES}
RELACIONES += [r for r in _MAS if (r[0], r[1]) not in _ya]

# Actores locales: al menos un actor que define en cada país (ver fuente/locales.py)
from locales import LOCALES as _LOC, RELACIONES as _REL_LOC
ORGS += [n[:9] for n in _LOC]
FORMAL.update({n[0]: n[9] for n in _LOC})
FASE.update({n[0]: n[10] for n in _LOC})
_ya = {(r[0], r[1]) for r in RELACIONES} | {(r[1], r[0]) for r in RELACIONES}
RELACIONES += [r for r in _REL_LOC if (r[0], r[1]) not in _ya]

# Países núcleo: actores que faltaban en las potencias (ver fuente/nucleo.py)
from nucleo import NUCLEO as _NUC, RELACIONES as _REL_NUC
ORGS += [n[:9] for n in _NUC]
FORMAL.update({n[0]: n[9] for n in _NUC})
FASE.update({n[0]: n[10] for n in _NUC})
_ya = {(r[0], r[1]) for r in RELACIONES} | {(r[1], r[0]) for r in RELACIONES}
RELACIONES += [r for r in _REL_NUC if (r[0], r[1]) not in _ya]

# Poder duro: eje 18 «Acción fuera de la ley» y revisión de autonomía (ver fuente/poder_duro.py)
from poder_duro import EJE as _EJE, ANCLA as _ANCLA, AUT as _AUT_REAL, DEP as _DEP_REAL
EJES.insert([e[0] for e in EJES].index("ter") + 1, _EJE)
ANCLAS[_EJE[0]] = _ANCLA
ORGS = [o[:5] + (_AUT_REAL.get(o[0], o[5]),) + o[6:8] + (_DEP_REAL.get(o[0], o[8]),) + o[9:] for o in ORGS]

# Personas: empresarios y líderes políticos (jefes de Estado, de gobierno o de régimen)
AREA_TIPO.update({"Empresario": "Persona", "Líder político": "Persona"})
_EMPRESARIOS = {"musk", "ellison", "zuckerberg", "m_ambani", "bezos", "thiel", "arnault"}
ORGS = [o[:2] + (("Empresario" if o[0] in _EMPRESARIOS else "Líder político") if o[2] == "Persona" else o[2],) + o[3:] for o in ORGS]

# Partidos: único o hegemónico frente a sistema competitivo; el Frente Unido es un órgano del PCCh, no un partido.
from categorias import HEGEMONICOS as _HEG
AREA_TIPO.update({"Partido único o hegemónico": "Estado", "Partido en sistema competitivo": "Estado"})
del AREA_TIPO["Partido político"]
def _area(o):
    if o[0] == "ufwd": return "Organismo de gobierno"
    if o[2] == "Partido político": return "Partido único o hegemónico" if o[0] in _HEG else "Partido en sistema competitivo"
    return o[2]
ORGS = [o[:2] + (_area(o),) + o[3:] for o in ORGS]
assert {o[0] for o in ORGS if o[2] == "Partido único o hegemónico"} == _HEG

# Ejes 19 y 20: cohesión interna y apoyo popular (ver fuente/ejes_nuevos.py)
from ejes_nuevos import EJES as _EJN
for _e in _EJN:
    EJES.insert([e[0] for e in EJES].index("red") + 1, _e[:4]); ANCLAS[_e[0]] = _e[4]
