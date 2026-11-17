# Poder duro: pesos de los ejes, eje 18 «Acción fuera de la ley» y autonomía real (noviembre de 2026).
# Criterio: el poder real pesa más que la jerarquía formal. Quien tiene armas, secretos, contactos y capacidad
# de actuar fuera de la ley conserva poder propio aunque dependa formalmente de otro.
W = "https://en.wikipedia.org/wiki/"

# Pesos fijos por eje (el resto vale 1). El sitio no ofrece controles para cambiarlos.
PESOS = {"coe": 2, "adq": 2, "ext": 2, "red": 1.5}

# Autonomía real: d = (coerción + adquisición de información + acción fuera de la ley + contactos) / 12, tope 1.
# El factor de autonomía sube hacia 1 en proporción a d (AUTONOMIA_REAL) y el jefe formal hereda menos de ese actor.
AUTONOMIA_REAL = 0.6

EJE = ("ext", "Acción fuera de la ley", "Fuerza",
       "Capacidad de operar por fuera de la ley o de forma encubierta: operaciones secretas, asesinatos selectivos, sabotaje, chantaje, soborno sistemático o crimen organizado.")
ANCLA = ("Operaciones encubiertas, asesinatos, sabotaje o crimen a escala mundial, con impunidad de hecho",
         "Opera fuera de la ley en una región o en varios países, documentado por tribunales u organismos oficiales",
         "Prácticas ilegales o encubiertas documentadas, de alcance limitado")

# id: (valor, justificación, fuente). Toda calificación lleva un hecho documentado y una fuente.
# En personas vivas solo se puntúa lo establecido por un tribunal u organismo oficial.
EXT = {
 # Servicios de inteligencia y fuerzas de seguridad
 "cia": (3, "Acción encubierta en el exterior por mandato legal: golpes, programas de drones y prisiones secretas documentados.", W + "CIA_black_sites"),
 "mossad": (3, "Asesinatos selectivos y sabotajes en el exterior documentados durante décadas.", W + "Mossad"),
 "fsb": (3, "La UE sancionó a agentes del FSB por el envenenamiento de Alexéi Navalni en 2020.", W + "Poisoning_of_Alexei_Navalny"),
 "gru": (3, "El Reino Unido atribuyó al GRU el envenenamiento de Serguéi Skripal en 2018; EE.UU. acusó a sus agentes por ciberataques.", W + "Poisoning_of_Sergei_and_Yulia_Skripal"),
 "mss": (3, "EE.UU. acusó a agentes y contratistas del MSS por campañas globales de ciberespionaje.", W + "Ministry_of_State_Security_(China)"),
 "cgri": (3, "Su Fuerza Quds opera milicias en Medio Oriente; EE.UU. la designó organización terrorista en 2019.", W + "Quds_Force"),
 "nsa": (2, "Vigilancia masiva revelada en 2013, que tribunales de EE.UU. y Europa declararon ilegal en parte.", W + "Global_surveillance_disclosures_(2013%E2%80%93present)"),
 "gchq": (2, "El Tribunal Europeo de Derechos Humanos declaró ilegal su intercepción masiva en 2021.", W + "Big_Brother_Watch_v_United_Kingdom"),
 "mi6": (2, "Operaciones encubiertas en el exterior por mandato legal.", W + "Secret_Intelligence_Service"),
 "dgse": (2, "Hundió el Rainbow Warrior de Greenpeace en Nueva Zelanda en 1985.", W + "Sinking_of_the_Rainbow_Warrior"),
 "isi": (2, "Apoyo documentado a los talibanes y a la red Haqqani.", W + "Inter-Services_Intelligence"),
 "mit_tr": (2, "Secuestros y traslados forzados de opositores desde el exterior, reconocidos por el gobierno turco.", W + "National_Intelligence_Organization_(Turkey)"),
 "gur": (2, "Sabotajes y asesinatos dentro de Rusia durante la guerra.", W + "Main_Directorate_of_Intelligence_(Ukraine)"),
 "mps_china": (2, "En 2023 EE.UU. acusó a agentes por una «comisaría» china encubierta en Nueva York.", W + "Chinese_police_overseas_service_stations"),
 "bnd": (1, "Vigilancia de aliados revelada en 2015.", W + "Federal_Intelligence_Service"),
 "shinbet": (1, "Uso de presión física en interrogatorios bajo la doctrina de «necesidad», que la Corte Suprema admitió en 1999.", W + "Shin_Bet"),
 "nis_corea": (1, "Condenas por intervención en las elecciones de 2012.", W + "National_Intelligence_Service_(South_Korea)"),
 "sri": (1, "Protocolos secretos con la fiscalía declarados inconstitucionales.", W + "Romanian_Intelligence_Service"),
 "ccdi": (1, "Detiene sin proceso judicial a funcionarios bajo el régimen de liuzhi.", W + "Liuzhi"),
 # Ejércitos
 "africacorps": (3, "La ONU documentó ejecuciones masivas con participación de Wagner en Moura (Malí) en 2022.", W + "Moura_massacre"),
 "far_sudan": (3, "EE.UU. determinó en enero de 2025 que cometieron genocidio en Darfur.", W + "Rapid_Support_Forces"),
 "ffaa_rusia": (2, "La comisión de la ONU documentó crímenes de guerra en Ucrania.", W + "War_crimes_in_the_Russian_invasion_of_Ukraine"),
 "fdi": (2, "La Corte Penal Internacional emitió en 2024 órdenes de arresto contra Netanyahu y Gallant por la conducción de la guerra de Gaza.", W + "International_Criminal_Court_investigation_in_Palestine"),
 "tatmadaw": (2, "La misión de la ONU recomendó juzgar a sus jefes por genocidio contra los rohinyá.", W + "Rohingya_genocide"),
 "saf": (2, "EE.UU. determinó en 2025 que usó armas químicas.", W + "Sudanese_Armed_Forces"),
 "epc": (2, "Ciberataques y venta de armas en violación de sanciones de la ONU.", W + "Korean_People%27s_Army"),
 "ejercito_pak": (1, "Golpes de Estado y manipulación electoral documentados.", W + "Pakistan_Army"),
 "ffaa_egipto": (1, "Golpe de 2013 y represión de Rabaa documentada por Human Rights Watch.", W + "Rabaa_massacre"),
 "ejercito_tai": (1, "Doce golpes de Estado exitosos desde 1932.", W + "Coups_d%27%C3%A9tat_in_Thailand"),
 "pentagono": (1, "Ataques letales contra lanchas en el Caribe desde 2025, de legalidad cuestionada.", "https://en.wikipedia.org/wiki/Special:Search?search=2025+United+States+strikes+on+alleged+drug+vessels"),
 "fanb": (1, "Represión de protestas documentada por la misión de la ONU.", W + "Bolivarian_National_Armed_Forces_of_Venezuela"),
 "capsat": (1, "Golpes de 2009 y 2025.", W + "Michael_Randrianirina"),
 "ffaa_gbissau": (1, "Golpe de noviembre de 2025.", "https://www.trtworld.com/article/2a2c7f70c2b2"),
 "rfmf": (1, "Golpes de 1987 y 2006.", W + "Republic_of_Fiji_Military_Forces"),
 # Paramilitares y crimen organizado (su actividad es ilegal por definición; ver sus fichas)
 "isis": (3, "Atentados en varios continentes.", W + "Islamic_State"),
 "sinaloa": (3, "Tráfico de fentanilo y cocaína a escala mundial; organización terrorista para EE.UU. desde 2025.", W + "Sinaloa_Cartel"),
 "cjng": (3, "Tráfico de drogas en varios continentes; organización terrorista para EE.UU. desde 2025.", W + "Jalisco_New_Generation_Cartel"),
 "ndrangheta": (3, "Controla buena parte de la cocaína que entra a Europa.", W + "%27Ndrangheta"),
 "talibanes": (2, "Toma del poder por las armas y represión documentada por la ONU.", W + "Taliban"),
 "jnim": (2, "Insurgencia armada en el Sahel.", W + "Jama%27at_Nasr_al-Islam_wal_Muslimin"),
 "hutis": (2, "Ataques contra el tráfico marítimo en el mar Rojo.", W + "Houthis"),
 "lna": (2, "Crímenes documentados por la misión de la ONU en Libia.", W + "Libyan_National_Army"),
 "hezbola": (2, "Organización armada designada terrorista por EE.UU. y la UE (su brazo armado).", W + "Hezbollah"),
 "pmf": (2, "Milicias con ataques contra fuerzas de EE.UU. documentados.", W + "Popular_Mobilization_Forces"),
 "alshabaab": (2, "Insurgencia y atentados en Somalia y Kenia.", W + "Al-Shabaab_(militant_group)"),
 "eln": (2, "Guerrilla y narcotráfico en Colombia y Venezuela.", W + "National_Liberation_Army_(Colombia)"),
 "hamas": (2, "Ataque del 7 de octubre de 2023.", W + "Hamas"),
 "m23": (2, "La ONU documentó ejecuciones de civiles en el este del Congo.", W + "March_23_Movement"),
 "pcc": (2, "Narcotráfico transnacional; organización terrorista para EE.UU. desde 2026.", W + "Primeiro_Comando_da_Capital"),
 "cv": (2, "Narcotráfico; organización terrorista para EE.UU. desde 2026.", W + "Comando_Vermelho"),
 "clan_golfo": (2, "Narcotráfico transnacional.", W + "Clan_del_Golfo"),
 "trenaragua": (2, "Crimen organizado en varios países; organización terrorista para EE.UU. desde 2025.", W + "Tren_de_Aragua"),
 "sunyeeon": (2, "Tríada con presencia en varios países.", W + "Sun_Yee_On"),
 "yamaguchi": (2, "Mayor sindicato yakuza.", W + "Yamaguchi-gumi"),
 "prince": (2, "EE.UU. y el Reino Unido lo sancionaron en 2025 por centros de estafa con trabajo forzado.", W + "Prince_Group"),
 "los_lobos": (2, "Narcotráfico y minería ilegal; organización terrorista para EE.UU. desde 2025.", W + "Los_Lobos_(Ecuador)"),
 "viv_ansanm": (2, "Organización terrorista para EE.UU. desde 2025.", W + "Viv_Ansanm"),
 # Gobiernos y personas (solo hechos establecidos por tribunales u organismos oficiales)
 "kremlin": (3, "La investigación pública británica concluyó en 2016 que Putin probablemente aprobó el asesinato de Litvinenko.", W + "Poisoning_of_Alexander_Litvinenko"),
 "ptk": (3, "Asesinato de Kim Jong-nam en 2017 y robos informáticos del grupo Lazarus, según EE.UU. y la ONU.", W + "Lazarus_Group"),
 "saud": (2, "La inteligencia de EE.UU. concluyó en 2021 que el príncipe heredero aprobó la operación contra Jamal Khashoggi.", W + "Assassination_of_Jamal_Khashoggi"),
 "pcch": (2, "Presión sobre disidentes en el exterior documentada por gobiernos occidentales.", "https://en.wikipedia.org/wiki/Special:Search?search=transnational+repression+China"),
 "lider_iran": (2, "EE.UU. acusó en 2024 a agentes iraníes de complots de asesinato en su territorio.", "https://en.wikipedia.org/wiki/Special:Search?search=Iranian+assassination+plots+United+States+2024"),
 "gob_india": (1, "EE.UU. acusó en 2023 a un funcionario indio de planear un asesinato en Nueva York.", "https://en.wikipedia.org/wiki/Special:Search?search=Gurpatwant+Singh+Pannun+assassination+plot"),
 "alnahyan": (1, "El panel de la ONU documentó envíos de armas a las Fuerzas de Apoyo Rápido de Sudán.", W + "Rapid_Support_Forces"),
 "ufwd": (1, "Operaciones de influencia en el exterior documentadas por gobiernos occidentales.", W + "United_Front_Work_Department"),
 "ortega_murillo": (2, "El grupo de expertos de la ONU concluyó en 2023 que su gobierno cometió crímenes de lesa humanidad.", "https://en.wikipedia.org/wiki/Special:Search?search=Group+of+Human+Rights+Experts+on+Nicaragua"),
 "lukashenko": (2, "La OACI concluyó que el desvío del vuelo de Ryanair en 2021 fue deliberado.", W + "Ryanair_Flight_4978"),
 "bukele": (1, "El Tesoro de EE.UU. sancionó en 2021 a funcionarios de su gobierno por negociar con pandillas.", W + "Nayib_Bukele"),
 "hermandad": (1, "EE.UU. designó a tres de sus ramas como terroristas en enero de 2026.", W + "Muslim_Brotherhood"),
 "rt": (1, "Prohibida en la UE desde 2022 por desinformación.", W + "RT_(TV_network)"),
 # Empresas con causas documentadas
 "glencore": (2, "Se declaró culpable en 2022 de sobornos y manipulación de mercado en EE.UU., el Reino Unido y Brasil.", W + "Glencore"),
 "trafigura": (1, "Se declaró culpable en 2024 de sobornos en Brasil ante la justicia de EE.UU.", W + "Trafigura"),
 "vitol": (1, "Acuerdo con EE.UU. en 2020 por sobornos en Ecuador, México y Brasil.", W + "Vitol"),
 "airbus": (1, "Acuerdo de 2020 por 3.600 millones de euros por sobornos en varios países.", W + "Airbus"),
 "huawei": (1, "Acusada por EE.UU. de fraude bancario para evadir sanciones a Irán.", W + "Huawei"),
 "goldman": (1, "Su filial de Malasia se declaró culpable por el caso 1MDB en 2020.", W + "1Malaysia_Development_Berhad_scandal"),
 "mckinsey": (1, "Acuerdo con EE.UU. en 2024 por sobornos en Sudáfrica.", W + "McKinsey_%26_Company"),
 "petrobras": (1, "Acuerdo con EE.UU. en 2018 por la corrupción del caso Lava Jato.", W + "Operation_Car_Wash"),
 "pdvsa": (1, "Causas de corrupción y sanciones de EE.UU.", W + "PDVSA"),
 "adani": (1, "La justicia de EE.UU. acusó en 2024 a directivos por sobornos en la India, lo que el grupo niega.", W + "Adani_Group"),
 "bollore": (1, "Causa en Francia por presuntos sobornos en Togo.", W + "Bollor%C3%A9"),
 "samherji": (1, "Investigada en Islandia y Namibia por el caso Fishrot, lo que niega.", W + "Fishrot_Files"),
}

# Revisión de autonomía caso por caso (de la jerarquía formal al poder real)
AUT = {
 "shinbet": 2,   # enfrentó al gobierno en 2025 por el despido de su director, que frenó la Corte Suprema
 "spacex": 2, "meta": 2, "reliance": 2, "lvmh": 2, "x": 2,  # empresas con aparato propio, más que instrumentos de su dueño
 "mss": 2,       # aparato de inteligencia con agenda propia en el exterior
 "isi": 2,       # opera con margen propio dentro del ejército
 "mossad": 1,    # responde por ley al primer ministro, pero en los hechos fija su propia agenda
}

# Dependencias formales que no reflejan el poder real ("" = no depende de nadie en el mapa)
DEP = {"mossad": ""}

# Altas de los países núcleo
from nucleo import EXT as _EXT_N, AUT as _AUT_N, DEP as _DEP_N
EXT.update(_EXT_N); AUT.update(_AUT_N); DEP.update(_DEP_N)
