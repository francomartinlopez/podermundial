# Correcciones del 20 de noviembre de 2026: hechos de 2026 que faltaban, actores disueltos,
# errores en fichas de país y cronologías de los puntos de fricción.
# Solo datos: se aplican en datos.py, fichas.py, locales.py, paises_juego.py, paises_bloques.py,
# friccion.py y scripts/generar_datos.py.
W = "https://en.wikipedia.org/wiki/"

# ───────── Actores dados de baja: salen del mapa, los rankings y las relaciones; su ficha queda como histórica.
BAJAS = {
    "sdf": ("2026-08-25", "Se disolvió como fuerza independiente al completar su integración al ejército sirio."),
}

# ───────── Puntajes corregidos (17 ejes en el orden de entrada de datos.py)
ORG_SC = {
    "stc": "10201110110011010",  # perdió Adén y su conducción está dividida tras la disolución anunciada en Riad
}

# ───────── Fichas de actores: res (reemplaza), res_mas (agrega), manda (reemplaza), crono_mas, fuentes_mas
PARCHES = {
"stc": dict(
    res=["Movimiento separatista del sur de Yemen, armado y financiado por Emiratos. En diciembre de 2025 avanzó sobre el sur y el este del país y fue rechazado por la aviación saudí y fuerzas afines a Riad.",
         "El 9 de enero de 2026 una delegación suya anunció desde Riad la disolución del consejo; su vocero y parte de la conducción la rechazaron por considerarla dictada bajo presión, y hubo marchas en Adén en su contra."],
    manda=["Aidarus al-Zoubaidi, que huyó a Emiratos en enero de 2026; la conducción quedó dividida entre quienes aceptaron la disolución y quienes la rechazan."],
    crono_mas=[("2025-12", "Avanza sobre el sur y el este; lo repelen la aviación saudí y fuerzas afines a Riad."), ("2026-01-07", "Al-Zoubaidi huye a Emiratos."),
               ("2026-01-09", "Una delegación en Riad anuncia la disolución; el vocero la rechaza.")],
    fuentes_mas=[("Southern Yemen separatists call foul as STC announce dissolution (The New Arab)", "https://www.newarab.com/news/south-yemen-separatists-call-foul-stc-announce-dissolution"),
                 ("Yemeni separatists announce disputed 'dissolution' (Dawn, AFP)", "https://www.dawn.com/news/1966102")]),
"sdf": dict(
    res=["Alianza armada liderada por kurdos que controló el noreste de Siria y fue la aliada de EE.UU. contra el Estado Islámico.", "El 25 de agosto de 2026 su comandante, Mazloum Abdi, anunció en Damasco la disolución de las FDS y de la administración autónoma, tras integrar unos 10.000 combatientes a brigadas del ejército sirio según el acuerdo del 29 de enero. Abdi pasó a ser asesor del presidente al-Sharaa."],
    manda=["Mazloum Abdi, su comandante hasta la disolución."],
    crono_mas=[("2026-01", "Ofensiva del gobierno: Damasco toma Tabqa y la mayor parte del noreste."), ("2026-01-29", "Acuerdo de alto el fuego e integración."), ("2026-08-25", "Anuncia su disolución.")],
    fuentes_mas=[("Kurdish-led SDF announces dissolution after merging with Syria's military (Al Jazeera)", "https://aljazeera.com/news/2026/8/25/kurdish-led-forces-in-syria-dissolve-after-merging-with-the-army"),
                 ("Kurdish-led Syrian Democratic Forces announce its dissolution (FDD's Long War Journal)", "https://www.fdd.org/analysis/2026/08/26/kurdish-led-syrian-democratic-forces-announce-its-dissolution/")]),
"sharaa": dict(crono_mas=[("2026-01-29", "Acuerdo de integración con las FDS tras la ofensiva sobre el noreste.")],
    fuentes_mas=[("Kurdish-led SDF has dissolved, but has Syria really unified its military? (Al Jazeera)", "https://aljazeera.com/news/2026/8/26/kurdish-led-sdf-has-dissolved-but-has-syria-really-unified-its-military")]),
"opep": dict(
    res_mas=["Emiratos dejó la OPEP y la OPEP+ el 1 de mayo de 2026, en plena guerra con Irán y con relaciones cada vez más frías con Arabia Saudita, para producir sin cuotas."],
    crono_mas=[("2026-05-01", "Emiratos sale de la OPEP y la OPEP+.")],
    fuentes_mas=[("United Arab Emirates says it will leave OPEC effective May 1 (AP)", "https://abc7news.com/story/united-arab-emirates-says-will-leave-opec-effective-may-1/18986097/")]),
"alnahyan": dict(crono_mas=[("2026-04-28", "Anuncia que Emiratos deja la OPEP y la OPEP+ desde el 1 de mayo.")],
    fuentes_mas=[("UAE to leave OPEC, OPEC+ (Gulf News)", "https://gulfnews.com/amp/story/business%2Fenergy%2Fuae-announces-decision-to-exit-opec-opec-1.500522017")]),
"tatmadaw": dict(
    res=["Fuerzas armadas de Myanmar, en el poder desde el golpe de 2021 y en guerra con milicias étnicas y de la resistencia que controlan buena parte del territorio.",
         "Tras las elecciones por etapas que organizó sin la oposición disuelta, el Parlamento eligió presidente a su jefe, Min Aung Hlaing, el 3 de abril de 2026: el ejército sigue mandando detrás de una fachada civil."],
    manda=["Min Aung Hlaing, presidente desde abril de 2026; dejó la comandancia porque la Constitución impide ocupar los dos cargos.", "Ye Win Oo, exjefe de inteligencia y hombre de su confianza, comandante en jefe."],
    crono_mas=[("2026-03-30", "Ye Win Oo es designado sucesor al frente del ejército."), ("2026-04-03", "El Parlamento elige presidente a Min Aung Hlaing con 429 de 584 votos.")],
    fuentes_mas=[("Myanmar junta chief Min Aung Hlaing elected president by pro-military parliament (Reuters)", "https://chronicle.lu/category/international-news/60465-myanmar-junta-chief-min-aung-hlaing-elected-president-by-pro-military-parliament"),
                 ("Myanmar's former junta chief elected president by parliament (Anadolu)", "https://aa.com.tr/en/asia-pacific/myanmar-s-former-junta-chief-elected-president-by-parliament/3890153")]),
"colorado_py": dict(
    manda=["Santiago Peña, presidente de la República, y Horacio Cartes, expresidente, presidente del partido y jefe de la facción dominante.",
           "EE.UU. sancionó a Cartes por corrupción en 2023; la OFAC levantó las sanciones el 6 de octubre de 2025 y el Departamento de Estado dijo que ya no eran necesarias para incentivar un cambio de conducta."],
    crono_mas=[("2025-10-06", "La OFAC levanta las sanciones a Cartes.")],
    fuentes_mas=[("US lifts sanctions on Paraguay's Cartes (LatinNews)", "https://latinnews.com/component/k2/item/107570.html")]),
"ptr_mu": dict(
    res=["Partido que encabeza el gobierno de Mauricio tras arrasar en las elecciones de 2024.",
         "En mayo de 2025 Mauricio firmó con el Reino Unido el tratado que le traspasa la soberanía de las islas Chagos, con arriendo de la base de Diego García por 99 años. El tratado no entró en vigor: la ley británica de ratificación venció en la Cámara de los Lores en 2026 y EE.UU. retiró su apoyo."],
    crono_mas=[("2026-04", "Se frena la ratificación británica del tratado de Chagos.")],
    fuentes_mas=[("UK-Mauritius Chagos sovereignty deal stalls (Al Jazeera)", "https://www.aljazeera.com/news/2026/10/2/uk-mauritius-chagos-sovereignty-deal-stalls-amid-fears-of-further-delays")]),
"dpworld": dict(
    res_mas=["Sultan Ahmed bin Sulayem, su presidente y director ejecutivo durante dos décadas, renunció el 13 de febrero de 2026 después de que los archivos Epstein mostraran una relación de más de diez años con Epstein; no fue acusado de ningún delito."],
    manda=["El emirato de Dubái, su dueño a través de Dubai World.", "Essa Kazim, presidente, y Yuvraj Narayan, director ejecutivo, desde febrero de 2026."],
    crono_mas=[("2026-02-13", "Renuncia bin Sulayem; asumen Kazim y Narayan.")],
    fuentes_mas=[("Epstein files: DP World chief executive Bin Sulayem resigns (The Irish Times)", "https://www.irishtimes.com/world/us/2026/02/13/epstein-files-dp-world-chief-executive-bin-sulayem-resigns-over-links-to-disgraced-financier/")]),
"disney": dict(
    manda=["Josh D'Amaro, director ejecutivo desde el 18 de marzo de 2026; Dana Walden, presidenta y directora creativa.", "Su directorio, presidido por James Gorman."],
    crono_mas=[("2026-03-18", "Josh D'Amaro sucede a Bob Iger.")],
    fuentes_mas=[("Disney names Josh D'Amaro CEO (ABC News)", "https://abc7news.com/post/disney-names-josh-damaro-ceo-dana-walden-president-chief-creative-officer/18534139/")]),
"ckh": dict(
    res_mas=["En enero de 2026 la Corte Suprema de Panamá declaró inconstitucionales sus concesiones de Balboa y Cristóbal; en febrero Panamá tomó las terminales y CK Hutchison inició un arbitraje internacional. El fallo complica la venta de sus puertos a BlackRock y MSC."],
    crono_mas=[("2026-01-29", "La Corte Suprema de Panamá anula sus concesiones."), ("2026-02-23", "Panamá toma Balboa y Cristóbal; quedan a cargo de APM Terminals (Maersk) y TiL (MSC) por 18 meses.")],
    fuentes_mas=[("Hutchison pushed out as Maersk, MSC assume interim operations at Panama Canal ports (Riviera)", "https://www.rivieramm.com/news-content-hub/hutchison-pushed-out-as-maersk-msc-assume-interim-operations-at-panama-canal-ports-87902"),
                 ("Panama finalizes Supreme Court ruling scrapping Hutchison ports deal (Tico Times)", "https://ticotimes.net/2026/02/23/panama-finalizes-supreme-court-ruling-scrapping-hutchison-ports-deal")]),
"acp": dict(crono_mas=[("2026-02-23", "Los puertos de Balboa y Cristóbal, a ambos lados del canal, pasan a operadores interinos de Maersk y MSC.")],
    fuentes_mas=[("Panama occupies Hutchison's terminals after court publishes decision (The Maritime Executive)", "https://maritime-executive.com/article/panama-occupies-hutchison-s-terminals-after-court-publishes-decision")]),
"maersk": dict(crono_mas=[("2026-02-23", "APM Terminals toma de forma interina la terminal de Balboa, en Panamá.")],
    fuentes_mas=[("Maersk and MSC take over as Panama seizes key canal ports (Trans.info)", "https://trans.info/en/panama-canal-port-457717")]),
"msc": dict(crono_mas=[("2026-02-23", "Su filial TiL toma de forma interina la terminal de Cristóbal, en Panamá.")],
    fuentes_mas=[("Maersk and MSC take over as Panama seizes key canal ports (Trans.info)", "https://trans.info/en/panama-canal-port-457717")]),
"cmc": dict(
    res_mas=["El 24 de enero de 2026 fueron puestos bajo investigación su vicepresidente primero, Zhang Youxia, y el jefe del Estado Mayor Conjunto, Liu Zhenli: la comisión quedó reducida a Xi Jinping y Zhang Shengmin."],
    crono_mas=[("2026-01-24", "Investigación a Zhang Youxia y Liu Zhenli.")],
    fuentes_mas=[("China's top military general under investigation (Global News, AP)", "https://globalnews.ca/news/11638076/china-xi-jinping-military"),
                 ("When Loyalty Becomes Liability: The Fall of Zhang Youxia (ISDP)", "https://www.isdp.eu/when-loyalty-becomes-liability-the-fall-of-zhang-youxia-and-xis-grip-on-the-pla/")]),
"epl": dict(crono_mas=[("2026-01-24", "Caen Zhang Youxia y Liu Zhenli, los dos militares de mayor rango.")],
    fuentes_mas=[("China's top military general under investigation (Global News, AP)", "https://globalnews.ca/news/11638076/china-xi-jinping-military")]),
"ptk": dict(
    res_mas=["Su IX Congreso (19 a 25 de febrero de 2026) reeligió a Kim Jong-un secretario general, renovó la dirigencia y consagró la condición nuclear del país."],
    crono_mas=[("2026-02-22", "El IX Congreso reelige a Kim Jong-un.")],
    fuentes_mas=[("What the Ninth Party Congress Tells Us About Where North Korea Is Headed (KEIA)", "https://keia.org/analysis/what-the-ninth-party-congress-tells-us-about-where-north-korea-is-headed/")]),
"talibanes": dict(
    res_mas=["Desde el 26 de febrero de 2026 están en «guerra abierta» con Pakistán, que bombardeó Kabul y Kandahar; hubo pausas negociadas por países de la región."],
    crono_mas=[("2025-06-17", "Cancelan el contrato petrolero de Amu Daria con una filial de CNPC."), ("2026-02-27", "Pakistán bombardea Kabul y Kandahar y declara la «guerra abierta»."),
               ("2026-03-18", "Pausa en los combates por el fin del Ramadán, a pedido de países mediadores.")],
    fuentes_mas=[("Pakistan is in 'open war' with Afghanistan after latest strikes (AP)", "https://www.washingtonexaminer.com/?p=4474138"),
                 ("Taliban cancels landmark oil deal with Chinese company (Afghanistan International)", "https://www.afintl.com/en/202506175674")]),
"ejercito_pak": dict(crono_mas=[("2026-02-27", "Operación Ghazab lil Haq: bombardeos sobre Kabul, Kandahar y Paktia.")],
    fuentes_mas=[("Pakistan declares 'open war' with Afghanistan after clashes (Bloomberg)", "https://news.bgov.com/bloomberg-government-news/pakistan-declares-open-war-with-afghanistan-after-clashes-2")]),
"ttp": dict(crono_mas=[("2026-02", "Pakistán acusa a los talibanes afganos de darle refugio y abre la guerra contra ellos.")],
    fuentes_mas=[("2026 Afghanistan–Pakistan conflict (Wikipedia)", W + "2026_Afghanistan%E2%80%93Pakistan_conflict")]),
"junta_mali": dict(
    res_mas=["El 25 de abril de 2026 el JNIM y el FLA lanzaron una ofensiva coordinada sobre Bamako, Kati, Gao, Sévaré, Mopti y Kidal: murió el ministro de Defensa Sadio Camara, el FLA recuperó Kidal y el JNIM anunció el bloqueo de Bamako. La junta resistió en la capital con apoyo del Africa Corps."],
    manda=["El general Assimi Goïta, que también asumió el Ministerio de Defensa tras la muerte de Sadio Camara."],
    crono_mas=[("2026-04-25", "Ofensiva del JNIM y el FLA; muere el ministro de Defensa Sadio Camara."), ("2026-04-28", "El JNIM anuncia el bloqueo de Bamako.")],
    fuentes_mas=[("Mali: Defense Minister Sadio Camara Killed During Coordinated Attacks (AllAfrica)", "https://allafrica.com/stories/202604260055.html"),
                 ("What can save Mali from collapse? (Atlantic Council)", "https://www.atlanticcouncil.org/blogs/africasource/what-can-save-mali-from-collapse/")]),
"jnim": dict(crono_mas=[("2026-04-25", "Ofensiva coordinada con el FLA en todo Malí; mata al ministro de Defensa."), ("2026-04-28", "Anuncia el bloqueo de Bamako.")],
    fuentes_mas=[("Mali Hit by Major Coordinated Offensive (War Mapper)", "https://warmapper.substack.com/p/mali-hit-by-major-coordinated-offensive")]),
"fla": dict(
    res_mas=["En abril de 2026 anunció su alianza con el JNIM y retomó Kidal en la ofensiva coordinada contra la junta."],
    crono_mas=[("2026-04-27", "Declara el control de Kidal y su alianza con el JNIM.")],
    fuentes_mas=[("Mali separatists confirm they joined Islamic militants in coordinated attacks (AP)", "https://www.cp24.com/news/world/2026/04/26/mali-separatists-confirm-they-joined-islamic-militants-in-co-ordinated-attacks/")]),
"africacorps": dict(crono_mas=[("2026-04", "Defiende Bamako y Kati; según la prensa negocia su retirada de Kidal, Tessalit y Aguelhok.")],
    fuentes_mas=[("Mali: Jihadists and Tuareg on the offensive. The Russians leave the North (FW Mag)", "https://fw-mag.com/shownews/1048/mali-jihadists-and-tuareg-on-the-offensive-the-russians-leave-the-north")]),
"kagame": dict(
    res_mas=["El Tesoro de EE.UU. sancionó al ejército ruandés y a cuatro de sus jefes el 2 de marzo de 2026, y al Ministerio de Defensa y a la financiera de las fuerzas de seguridad, Zigama, el 28 de octubre, por apoyar al M23."],
    crono_mas=[("2026-03-02", "EE.UU. sanciona al ejército ruandés y a cuatro generales."), ("2026-10-28", "Sanciones al Ministerio de Defensa y a Zigama.")],
    fuentes_mas=[("Treasury Sanctions Rwandan Ministry of Defence and Financial Institution Supporting M23 (Tesoro de EE.UU.)", "https://content.govdelivery.com/accounts/USTREAS/bulletins/430c4a3")]),
"m23": dict(crono_mas=[("2026-03-02", "EE.UU. sanciona al ejército de Ruanda por apoyarlo.")],
    fuentes_mas=[("OFAC Sanctions Rwanda Defence Force and Senior Officials (Cleary Gottlieb)", "https://www.clearygottlieb.com/news-and-insights/publication-listing/ofac-sanctions-rwanda-defence-force-and-senior-officials-in-connection-with-drc-conflict")]),
"ypf": dict(
    res_mas=["En marzo de 2026 la Cámara de Apelaciones del Segundo Circuito de EE.UU. revocó, por 2 a 1, la condena de 16.100 millones de dólares contra la Argentina por la expropiación de 2012, un juicio financiado por Burford Capital; luego rechazó revisar el fallo y a los demandantes solo les queda la Corte Suprema."],
    crono_mas=[("2023-09", "Un juzgado de Nueva York condena a la Argentina a pagar 16.100 millones de dólares."), ("2026-03-27", "El Segundo Circuito revoca la condena.")],
    fuentes_mas=[("Argentina Gets $16 Billion US Judgment Tossed on Appeal (Bloomberg Law)", "https://news.bloomberglaw.com/litigation/argentina-wins-reversal-of-us-decision-in-ypf-case-on-appeal"),
                 ("NY court denies Burford appeal in YPF expropriation case (Buenos Aires Herald)", "https://buenosairesherald.com/economics/ny-court-denies-burford-appeal-in-ypf-expropriation-case")]),
"milei": dict(crono_mas=[("2026-03-27", "Un tribunal de apelación de EE.UU. revoca la condena por YPF.")]),
"nis": dict(
    res_mas=["En enero de 2026 Gazprom Neft y Gazprom acordaron vender su 56,15 % a la húngara MOL; Serbia firmó con MOL en junio el acuerdo de accionistas, pero la operación depende del contrato final y del permiso de la OFAC."],
    manda=["Gazprom Neft, su accionista principal, mientras negocia la venta a MOL; el Estado serbio tiene casi el 30 %."],
    crono_mas=[("2026-01-19", "Acuerdo vinculante para vender la mayoría a MOL."), ("2026-06-16", "Acuerdo de accionistas entre Serbia y MOL.")],
    fuentes_mas=[("MOL to acquire majority ownership of Serbian NIS (Oil & Gas Journal)", "https://www.ogj.com/general-interest/news/55356961/mol-to-acquire-majority-ownership-of-serbian-nis-as-pancevo-refinery-restarts"),
                 ("Serbia, MOL sign agreement on future management of NIS (Interfax)", "https://interfax.com/newsroom/top-stories/118099/")]),
"mol": dict(
    res_mas=["En 2026 negocia comprar a Gazprom Neft la mayoría de NIS, la petrolera de Serbia, con el visto bueno pendiente de la OFAC y ADNOC como posible socio minoritario."],
    crono_mas=[("2026-01-19", "Acuerdo vinculante para comprar el 56,15 % de NIS.")],
    fuentes_mas=[("Hungary's MOL agrees to buy Serbian refiner NIS from Gazprom (Enerdata)", "https://www.enerdata.net/publications/daily-energy-news/hungarys-mol-agrees-buy-serbian-refiner-nis-gazprom.html")]),
"gob_groenlandia": dict(
    res=["Gobierno autónomo de Groenlandia dentro del Reino de Dinamarca, que conserva la defensa y la política exterior. La isla, rica en minerales y clave en el Ártico, está en el centro de la presión de Trump.",
         "Tras la crisis de enero de 2026, en la que Trump amenazó con quedarse con la isla, EE.UU., Dinamarca y Groenlandia firmaron el 22 de septiembre de 2026 un acuerdo de seguridad: más presencia militar estadounidense, con dos bases nuevas, y veto a bases e inversiones sensibles de sus adversarios, sin cesión de soberanía."],
    crono_mas=[("2026-01-22", "Trump anuncia en Davos un marco de acuerdo y retira la amenaza de tomar la isla."), ("2026-09-22", "Firma del acuerdo de seguridad con EE.UU. y Dinamarca en la ONU.")],
    fuentes_mas=[("Trump signs US-Denmark-Greenland agreement to bolster Arctic security (AP)", "https://www.valleynewslive.com/2026/09/23/trump-signs-us-denmark-greenland-agreement-bolster-arctic-security-after-prolonged-tensions/"),
                 ("US to build two new military bases in Greenland (ITV)", "https://www.itv.com/news/2026-09-22/us-to-build-two-new-military-bases-in-greenland-under-deal-with-denmark")]),
"saf": dict(
    res_mas=["En 2026 avanzó en Kordofán del Norte y aflojó el cerco de El Obeid, que las FAR atacan con drones; en noviembre Sudán acusó a Etiopía de albergar bases de drones de las FAR."],
    crono_mas=[("2026-08", "Deserciones en las FAR y avances del ejército en Kordofán del Norte."), ("2026-11", "Toma las localidades que rodean El Obeid y entra en Kordofán Occidental.")],
    fuentes_mas=[("Is Sudan's battlefield shaping the terms of its next political phase? (Al Jazeera)", "https://www.aljazeera.com/news/2026/8/26/is-sudans-battlefield-shaping-the-terms-of-its-next-political-phase"),
                 ("Civil War in Sudan (Council on Foreign Relations)", "https://www.cfr.org/global-conflict-tracker/conflict/power-struggle-sudan")]),
"far_sudan": dict(
    crono_mas=[("2026-02-19", "EE.UU. sanciona a comandantes de las FAR por la masacre de El Fasher."), ("2026-06", "Asedio y ataques con drones sobre El Obeid.")],
    fuentes_mas=[("Sudan: RSF drone strikes on civilians in El Obeid should be investigated as war crimes (Amnistía Internacional)", "https://www.amnestyusa.org/press-releases/sudan-devastating-rsf-drone-strikes-on-civilians-in-el-obeid-should-be-investigated-as-war-crimes/")]),
"kremlin": dict(
    res_mas=["El 14 de febrero de 2026 el Reino Unido, Suecia, Francia, Alemania y los Países Bajos declararon que Alexéi Navalni murió envenenado con epibatidina en prisión y responsabilizaron al Estado ruso, que lo niega."],
    crono_mas=[("2026-02-14", "Cinco gobiernos europeos atribuyen al Estado ruso la muerte de Navalni."), ("2026-11-10", "Ronda trilateral con EE.UU. y Ucrania en Abu Dabi.")],
    fuentes_mas=[("Joint statement on Alexei Navalny's death (Gobierno de Suecia)", "https://www.government.se/statements/2026/02/joint-statement-by-the-uk-sweden-france-germany-and-the-netherlands/"),
                 ("Russia and Ukraine begin U.S.-backed peace talks in Abu Dhabi (The Washington Post)", "https://www.washingtonpost.com/world/2026/11/10/russia-ukraine-begin-us-backed-peace-talks-abu-dhabi/")]),
"zelenski": dict(crono_mas=[("2026-11-10", "Tercera ronda trilateral en Abu Dabi, la primera desde febrero.")],
    fuentes_mas=[("Ukraine-Russia peace talks enter second day (Euronews)", "https://www.euronews.com/2026/11/11/ukraine-russia-peace-talks-enter-second-day-with-territory-and-security-guarantees-in-focu")]),
"netanyahu": dict(
    res=["Primer ministro de Israel en funciones, conduce la guerra contra Irán y controla los servicios de inteligencia y las fuerzas armadas.",
         "En las elecciones del 27 de octubre de 2026 su bloque obtuvo 53 bancas, lejos de las 61 de la mayoría; el bloque opositor de Gadi Eisenkot, 48. Las negociaciones para formar gobierno siguen abiertas."],
    fuentes_mas=[("Israel election: Netanyahu's bloc falls short (Latin Times)", "https://www.latintimes.com/israel-election-netanyahu-coalition-talks-600895")]),
"dem": dict(
    res=["Uno de los dos partidos que se alternan en el gobierno de EE.UU.; oposición al gobierno de Trump.",
         "En las elecciones legislativas del 3 de noviembre de 2026, el conteo de AP al 20 de noviembre (6:35, hora argentina) le asignaba 257 bancas ganadas en la Cámara de Representantes, donde 6 bancas no figuraban como ganadas por ningún partido, y un total de 56 en el Senado, incluidos 2 que votan con el bloque."]),
"gop": dict(
    res=["Partido de gobierno de EE.UU. desde 2025, transformado por el movimiento de Donald Trump.",
         "En las elecciones legislativas del 3 de noviembre de 2026, el conteo de AP al 20 de noviembre (6:35, hora argentina) le asignaba 172 bancas ganadas en la Cámara de Representantes, donde 6 bancas no figuraban como ganadas por ningún partido, y un total de 44 en el Senado."]),
"congreso_eeuu": dict(crono_mas=[("2026-11-03", "Elecciones de medio término: se renuevan la Cámara y un tercio del Senado.")]),
"viv_ansanm": dict(
    crono_mas=[("2026-02-07", "Termina el Consejo Presidencial de Transición; el primer ministro Fils-Aimé queda como único ejecutivo."), ("2026-10-28", "Las elecciones se postergan al 18 de julio de 2027.")],
    fuentes_mas=[("BINUH statement on the end of the mandate of the Transitional Presidential Council (ONU)", "https://binuh.unmissions.org/en/press-releases/binuh-statement-end-mandate-transitional-presidential-council"),
                 ("Haiti postpones first presidential election in a decade to July 2027 (Reuters)", "https://www.thestar.com.my/news/world/2026/10/29/haiti-postpones-first-presidential-election-in-a-decade-to-july-2027")]),
"gob_somalilandia": dict(
    res=["Gobierno de un territorio que funciona como Estado independiente desde 1991. Israel lo reconoció el 26 de diciembre de 2025, el primer país en hacerlo; Somalia y la Unión Africana lo condenaron. DP World opera su puerto de Berbera."],
    crono_mas=[("2025-12-26", "Israel lo reconoce como Estado independiente.")],
    fuentes_mas=[("Israel recognises Somaliland as independent state (Reuters, Al-Monitor)", "https://www.al-monitor.com/originals/2025/12/israel-recognises-somaliland-somalias-breakaway-region-independent-state")]),
}

# ───────── «Quién define aquí»: nota del país (se mantiene el actor salvo que se indique)
MANDA_NOTA = {
    "Greenland": "Dinamarca conserva la defensa y la política exterior; el acuerdo de septiembre de 2026 amplía la presencia militar de EE.UU.",
    "Somaliland": "DP World opera el puerto de Berbera; Israel la reconoció como Estado en diciembre de 2025, el único país que lo hizo.",
}

# ───────── Texto corto del país en el mapa (paises.py)
PAIS_X = {
    "Somaliland": "Reconocida solo por Israel, desde diciembre de 2025.",
}

# ───────── Fichas de país: campos que se reemplazan
PAIS_SET = {
    "N. Cyprus": dict(juego="Si la división se vuelve definitiva como «dos Estados», la línea de Ankara, o si se reabre la negociación: desde octubre de 2025 lo preside Tufan Erhürman, favorable a una federación, que se reúne con el presidente grecochipriota bajo la ONU."),
    "Yemen": dict(gob="Dividido entre los hutíes, que controlan Saná y el norte, y el gobierno reconocido, sostenido por Arabia Saudita; el separatismo del sur quedó debilitado tras la disolución del CTS anunciada en Riad en 2026."),
    "Myanmar": dict(gob="Gobierno con fachada civil encabezado desde abril de 2026 por el exjefe de la junta, Min Aung Hlaing, elegido por un Parlamento dominado por el ejército; perdió buena parte del territorio frente a guerrillas étnicas y de resistencia."),
    "Haiti": dict(gob="Estado colapsado: desde febrero de 2026 gobierna solo el primer ministro interino Alix Didier Fils-Aimé, sin elecciones desde 2016; las pandillas controlan la mayor parte de la capital."),
    "Somaliland": dict(gob="República presidencialista democrática, reconocida solo por Israel."),
    "Br. Indian Ocean Ter.": dict(gob="Territorio británico con base militar conjunta de EE.UU.; el tratado de 2025 que lo traspasa a Mauricio con arriendo de la base no entró en vigor."),
}

# ───────── Fichas de país: cronología. Cada valor es una lista de (año, hecho) que se agrega,
# o (texto viejo, (año, texto nuevo) | None) para corregir o quitar una entrada.
PAIS_CRONO = {
    "Panama": [(2026, "La Corte Suprema anula la concesión portuaria de CK Hutchison; Maersk y MSC operan Balboa y Cristóbal de forma interina.")],
    "Myanmar": [(2025, "Elecciones por etapas sin la oposición disuelta."), (2026, "El Parlamento elige presidente a Min Aung Hlaing.")],
    "Paraguay": [(2025, "EE.UU. levanta las sanciones a Horacio Cartes.")],
    "Mauritius": [("Acuerdo de traspaso de Chagos.", (2025, "Firma del tratado de traspaso de Chagos.")), (2026, "Se frena la ratificación británica: el tratado no entra en vigor.")],
    "Greenland": [(2026, "Crisis con EE.UU. en enero y acuerdo de seguridad en septiembre: dos bases nuevas de EE.UU., sin cesión de soberanía.")],
    "Denmark": [(2026, "Acuerdo de seguridad con EE.UU. y Groenlandia.")],
    "Sudan": [(2026, "El ejército avanza en Kordofán; las FAR atacan El Obeid con drones.")],
    "Iran": [("Guerra con EE.UU. e Israel.", (2026, "Guerra con EE.UU. e Israel desde el 28 de febrero: muere Ali Jamenei e Irán cierra el estrecho de Ormuz.")),
             (2026, "Alto el fuego del 8 de abril al 8 de julio y bloqueo naval de EE.UU. a sus puertos, reimpuesto en julio.")],
    "Ukraine": [(2026, "Negociaciones trilaterales con EE.UU. y Rusia en Abu Dabi, sin acuerdo.")],
    "Haiti": [(2026, "Termina el Consejo de Transición; las elecciones se postergan a julio de 2027.")],
    "N. Cyprus": [(2025, "Gana la presidencia Tufan Erhürman, favorable a la reunificación federal."), (2026, "Reuniones semanales con el presidente grecochipriota bajo la ONU.")],
    "Afghanistan": [(2025, "Los talibanes cancelan el contrato petrolero chino de Amu Daria."), (2026, "Guerra abierta con Pakistán.")],
    "Pakistan": [(2026, "Guerra abierta con los talibanes afganos y mediación entre EE.UU. e Irán.")],
    "Mali": [(2026, "Ofensiva del JNIM y el FLA: muere el ministro de Defensa y cae Kidal.")],
    "Burkina Faso": [(2026, "Inaugura su primera refinería de oro, estatal.")],
    "Rwanda": [(2026, "EE.UU. sanciona a su ejército y a su Ministerio de Defensa por el apoyo al M23.")],
    "Argentina": [(2026, "Un tribunal de apelación de EE.UU. revoca la condena de 16.100 millones de dólares por la expropiación de YPF.")],
    "Serbia": [(2026, "Gazprom Neft acuerda vender NIS a la húngara MOL; falta el permiso de EE.UU.")],
    "China": [(2026, "Purga de la cúpula militar: caen Zhang Youxia y Liu Zhenli.")],
    "North Korea": [(2026, "IX Congreso del partido.")],
    "United Arab Emirates": [(2026, "Sale de la OPEP y la OPEP+.")],
    "Syria": [(2026, "Ofensiva sobre el noreste y disolución de las FDS dentro del ejército.")],
    "Yemen": [(2026, "Arabia Saudita frena al CTS, cuya disolución se anuncia en Riad.")],
    "Somaliland": [(2025, "Israel la reconoce como Estado.")],
    "Norway": [("Sabotaje de los gasoductos Nord Stream en su vecindad.", (2022, "Tras el sabotaje de los gasoductos Nord Stream pasa a ser el principal proveedor de gas de Europa."))],
    "Br. Indian Ocean Ter.": [(2026, "La ratificación británica del traspaso se frena.")],
}

# ───────── Bloques en cada país: acciones (ta = transoceánico, ea = euroasiático). Mismo formato que PAIS_CRONO.
PB_TA = {
    "Mauritius": [("Tratado que le traspasa Chagos con arriendo de la base.", (2025, "Firma del tratado que le traspasaría Chagos con arriendo de la base.")), (2026, "EE.UU. retira su apoyo y la ratificación británica se frena.")],
    "Br. Indian Ocean Ter.": [(2026, "La ratificación del traspaso se frena; EE.UU. retira su apoyo.")],
    "Greenland": [(2026, "Acuerdo de seguridad con Dinamarca y Groenlandia: dos bases nuevas y veto a bases de adversarios.")],
    "Denmark": [(2026, "Acuerdo de seguridad sobre Groenlandia.")],
    "Sudan": [(2026, "Sanciones a comandantes de las FAR por la masacre de El Fasher.")],
    "Iran": [(2026, "Bloqueo naval a sus puertos desde abril.")],
    "Rwanda": [(2026, "Sanciones a su ejército, su Ministerio de Defensa y la financiera Zigama.")],
    "Panama": [(2026, "Los puertos de Hutchison pasan a operadores interinos de Maersk y MSC.")],
    "Somaliland": [(2025, "Israel la reconoce como Estado.")],
    "Mali": [("Se van Francia y la misión de la ONU.", (2022, "Se van las tropas francesas.")), (2023, "Termina la misión de la ONU (MINUSMA).")],
    "Colombia": [("Socio global de la OTAN.", (2018, "Pasa a ser socio global de la OTAN."))],
    "Kyrgyzstan": [("EE.UU. sanciona bancos kirguises.", (2025, "EE.UU. sanciona al Keremet Bank por pagos vinculados a Rusia."))],
    "Bulgaria": [("Corta el gas ruso.", (2022, "Tras el corte de Gazprom, compra gas por el interconector con Grecia."))],
    "Estonia": [("Brigada alemana permanente en Lituania.", (2025, "La OTAN lanza la misión Baltic Sentry tras los cortes de cables."))],
    "Latvia": [("Brigada alemana permanente en Lituania.", (2025, "La OTAN lanza la misión Baltic Sentry tras los cortes de cables."))],
}
PB_EA = {
    "Afghanistan": [("Contrato petrolero chino en Amu Daria.", (2023, "Contrato petrolero con una filial de CNPC en Amu Daria, cancelado por los talibanes en 2025."))],
    "Burkina Faso": [("Rusia construye una planta de refinado de oro.", None)],
    "Mali": [(2025, "Comienza la construcción de una refinería de oro con la rusa Yadran."), (2026, "El Africa Corps se repliega del extremo norte tras la ofensiva rebelde.")],
    "Nigeria": [("Refinería y ferrocarriles con capital chino.", (2021, "Inaugura el ferrocarril Lagos-Ibadán, construido por una empresa china con crédito chino."))],
    "Bulgaria": [("La fiscalía vincula explosiones en depósitos de armas con la inteligencia militar rusa.", (2021, "La fiscalía vincula explosiones en depósitos de armas con la inteligencia militar rusa."))],
    "Armenia": [("Rusia no la defiende en Karabaj; Armenia congela su participación en la OTSC.", (2023, "Rusia no la defiende en Karabaj.")), (2024, "Armenia congela su participación en la OTSC.")],
    "Norway": [("Sabotajes de cables en el mar de Barents.", None)],
    "Serbia": [(2026, "Gazprom Neft acuerda vender NIS bajo presión de las sanciones de EE.UU.")],
}

# ───────── Puntos de fricción: hitos que se agregan a la cronología (número del punto -> lista)
FR_CRONO = {
    1: [("2026-01-24", "Purga de la cúpula militar china: investigan a Zhang Youxia y Liu Zhenli."),
        ("2026-11-18", "Cumbre de la APEC en Shenzhen con Trump y Xi; la tregua comercial vence el 10 de enero de 2027.")],
    3: [("2026-01-29", "La Corte Suprema de Panamá anula la concesión portuaria de CK Hutchison; en febrero Maersk y MSC toman las terminales."),
        ("2026-02-07", "Termina el Consejo de Transición en Haití; las elecciones se postergan a 2027.")],
    5: [("2026-04-25", "Ofensiva del JNIM y el FLA en Malí: muere el ministro de Defensa y cae Kidal."),
        ("2026-11", "El ejército sudanés avanza en Kordofán; Sudán acusa a Etiopía de albergar drones de las FAR.")],
    6: [("2026-03-02", "EE.UU. sanciona al ejército de Ruanda por su apoyo al M23; en octubre, al Ministerio de Defensa.")],
    7: [("2026-02-14", "Cinco gobiernos europeos atribuyen al Estado ruso la muerte de Navalni."),
        ("2026-11-10", "Ronda trilateral de negociación entre EE.UU., Rusia y Ucrania en Abu Dabi.")],
    8: [("2026-01-09", "El CTS de Yemen anuncia su disolución en Riad tras ser frenado por Arabia Saudita."),
        ("2026-02-27", "Pakistán declara la «guerra abierta» a los talibanes afganos."),
        ("2026-02-28", "EE.UU. e Israel atacan Irán; muere Ali Jamenei e Irán cierra el estrecho de Ormuz."),
        ("2026-04-13", "Bloqueo naval de EE.UU. a los puertos iraníes, reimpuesto en julio."),
        ("2026-05-01", "Emiratos sale de la OPEP y la OPEP+."),
        ("2026-08-25", "Las FDS se disuelven dentro del ejército sirio.")],
    9: [("2026-04-03", "Min Aung Hlaing, jefe de la junta de Myanmar, es elegido presidente.")],
}

# ───────── Relaciones nuevas (a, b, tipo, explicación, intensidad) y textos corregidos
REL_MAS = [
    ("fla", "jnim", "Alianza", "El FLA anunció en abril de 2026 su alianza con el JNIM para la ofensiva que retomó Kidal.", 2),
    ("tesoro_eeuu", "kagame", "Enfrentamiento", "El Tesoro de EE.UU. sancionó en 2026 al ejército y al Ministerio de Defensa de Ruanda por apoyar al M23.", 2),
    ("mol", "nis", "Contrato", "MOL acordó en enero de 2026 comprar el 56,15 % de NIS; falta el permiso de la OFAC.", 2),
    ("mol", "gazprom", "Contrato", "Negocia con Gazprom Neft la compra de su participación en NIS.", 1),
    ("maersk", "ckh", "Enfrentamiento", "APM Terminals (Maersk) se quedó en 2026 de forma interina con la terminal de Balboa que CK Hutchison perdió por fallo judicial; Hutchison la amenazó con acciones legales.", 2),
    ("ejercito_pak", "talibanes", "Enfrentamiento", "Guerra abierta desde febrero de 2026: bombardeos paquistaníes sobre Kabul y Kandahar.", 3),
    ("alnahyan", "opep", "Ambigua", "Emiratos dejó la OPEP y la OPEP+ el 1 de mayo de 2026 para producir sin cuotas.", 2),
    ("prosperidad", "saf", "Enfrentamiento", "Sudán acusó en noviembre de 2026 a Etiopía de albergar bases de drones de las FAR; Etiopía expulsó a seis diplomáticos sudaneses.", 1),
    ("talibanes", "cnpc", "Enfrentamiento", "Los talibanes cancelaron en 2025 el contrato petrolero de Amu Daria con una filial de CNPC.", 1),
]
REL_TEXTO = {  # (a, b) en cualquier orden -> (tipo, explicación, intensidad)
    ("ejercito_pak", "talibanes"): ("Enfrentamiento", "Guerra abierta desde febrero de 2026: bombardeos paquistaníes sobre Kabul y Kandahar, con pausas negociadas por países de la región.", 3),
    ("alnahyan", "opep"): ("Ambigua", "Emiratos dejó la OPEP y la OPEP+ el 1 de mayo de 2026 para producir sin cuotas.", 2),
}
