# Fichas: tanda 1 (las 40 de mayor poder en red). Revisadas el 2026-11-16.
# Campos: res (resumen, párrafos), manda (quién manda adentro), dinero, crono [(fecha, hito)], fuentes [(título, url)].
W = "https://en.wikipedia.org/wiki/"

FICHAS = {
"pcch": dict(
 res=["Partido único que gobierna China desde 1949 y que está por encima del Estado: dirige el gobierno, el Ejército Popular de Liberación, los tribunales, la prensa y las grandes empresas estatales.",
      "Con unos 100 millones de miembros, su poder real no pasa por elecciones competitivas: se ejerce a través de la Comisión Militar Central, el Departamento de Organización (que nombra a los cuadros) y la censura."],
 manda=["Xi Jinping, secretario general desde 2012, presidente de la Comisión Militar Central y jefe de Estado.",
        "Comité Permanente del Politburó: el núcleo de siete miembros que decide la línea.",
        "Departamento de Organización: controla los nombramientos en el Estado y en las empresas públicas."],
 dinero="Controla indirectamente el sector estatal chino: bancos como ICBC, el Banco Popular de China y las grandes empresas públicas.",
 crono=[("1921-07", "Fundación en Shanghái."), ("1949-10", "Proclamación de la República Popular."), ("2012-11", "Xi Jinping asume como secretario general."), ("2018-03", "Se eliminan los límites de mandato presidencial.")],
 fuentes=[("Chinese Communist Party (Wikipedia)", W + "Chinese_Communist_Party"), ("Xi Jinping (Wikipedia)", W + "Xi_Jinping")]),

"casablanca": dict(
 res=["Poder Ejecutivo de Estados Unidos: comanda las fuerzas armadas, las agencias de inteligencia, la política exterior y una burocracia federal de millones de personas.",
      "En 2026 libró una guerra contra Irán iniciada el 28 de febrero, con bloqueo naval a los puertos iraníes reimpuesto en julio y vigente en noviembre."],
 manda=["Donald Trump, presidente desde enero de 2025.",
        "Gabinete y Consejo de Seguridad Nacional: Marco Rubio (Estado), Scott Bessent (Tesoro), Pete Hegseth (Guerra).",
        "Fiscal general Todd Blanche y secretario de Seguridad Nacional Markwayne Mullin, que reemplazaron a Pam Bondi y Kristi Noem."],
 dinero="Administra el presupuesto federal y, a través del Tesoro, el sistema de sanciones financieras con alcance mundial.",
 crono=[("2025-01-20", "Comienza el segundo mandato de Trump."), ("2026-02-28", "Ataques de EE.UU. e Israel contra Irán; muere Ali Jamenei."), ("2026-04-13", "Primer bloqueo naval a los puertos iraníes."), ("2026-07-14", "Se reimpone el bloqueo tras el colapso del acuerdo provisional.")],
 fuentes=[("Trump administration who's who (Political.org)", "https://political.org/explained/trump-administration-whos-who/"),
          ("Timeline of the US-Israel war with Iran (Anadolu)", "https://aa.com.tr/en/us-israel-iran-war/timeline-how-the-us-israel-war-with-iran-unfolded-over-108-days/3967739"),
          ("US reimposes blockade on Iranian ports (Al Jazeera)", "https://www.aljazeera.com/news/2026/7/14/us-strikes-new-targets-in-iran-as-tehran-hits-gulf-states-hormuz")]),

"kremlin": dict(
 res=["Administración Presidencial de Rusia: el centro de un sistema de poder personal donde el presidente concentra la decisión sobre la guerra, los servicios de seguridad y las grandes empresas de energía y armas.",
      "Sostiene la guerra en Ucrania desde 2022; en 2026 sus avances territoriales se redujeron al mínimo, mientras continúan las negociaciones trilaterales con EE.UU. y Ucrania."],
 manda=["Vladimir Putin, presidente.",
        "Consejo de Seguridad y los jefes del FSB, las Fuerzas Armadas y la Rosgvardia.",
        "Círculo económico que controla Gazprom, Rosneft y Rostec."],
 dinero="Controla a través del Estado los ingresos por energía, presionados por las sanciones y por la caída de exportaciones.",
 crono=[("2000-05", "Putin asume su primer mandato."), ("2022-02-24", "Invasión a gran escala de Ucrania."), ("2024-06", "Tratado de defensa mutua con Corea del Norte."), ("2026-10-27", "Tregua local en Kherson, la más larga de la guerra, que termina el 1 de noviembre.")],
 fuentes=[("Presidential Administration of Russia (Wikipedia)", W + "Presidential_Administration_of_Russia"),
          ("Russia's territorial gains dwindle (Al Jazeera)", "https://www.aljazeera.com/amp/news/2026/11/6/in-ukraine-russias-territorial-gains-dwindle-as-its-diesel-goes-unsold"),
          ("Longest truce of Ukraine war ends in Kherson (AFP vía BSS)", "https://www.bssnews.net/international/440974")]),

"consejoestado": dict(
 res=["Gobierno central de China: administra los ministerios, las provincias y, a través de la SASAC, las grandes empresas estatales.",
      "Ejecuta la línea que fija el Partido Comunista; por eso figura como subordinado pese a su enorme capacidad."],
 manda=["Primer ministro Li Qiang, número dos del Partido.", "Comité Permanente del Partido, por encima del Consejo."],
 dinero="Supervisa el sector público chino, el mayor conjunto de empresas estatales del mundo.",
 crono=[("1954-09", "Creación del Consejo de Estado."), ("2023-03", "Li Qiang asume como primer ministro.")],
 fuentes=[("State Council of the People's Republic of China (Wikipedia)", W + "State_Council_of_the_People%27s_Republic_of_China")]),

"pentagono": dict(
 res=["El Departamento de Defensa de EE.UU., que usa como título secundario Departamento de Guerra desde septiembre de 2025. Es la mayor organización del mundo por presupuesto y personal.",
      "En 2026 condujo la guerra contra Irán (Operación Furia Épica) y el bloqueo naval; también controla la NSA y la OTAN en lo operativo."],
 manda=["Pete Hegseth, secretario, que usa el título de secretario de Guerra.", "General Dan Caine, jefe del Estado Mayor Conjunto.", "Una serie de destituciones de altos mandos en 2025 y 2026 concentró el poder en el secretario."],
 dinero="El mayor presupuesto militar del planeta; es el principal cliente de Lockheed Martin, RTX, Boeing, General Dynamics, Palantir y SpaceX.",
 crono=[("1947-09", "Creación del Establecimiento Militar Nacional."), ("2025-09-05", "Orden ejecutiva que autoriza el nombre Departamento de Guerra."), ("2026-02-28", "Comienza la Operación Furia Épica contra Irán.")],
 fuentes=[("Department of Defense or Department of War (USAFacts)", "https://usafacts.org/articles/department-of-defense-or-department-of-war-which-is-it/"),
          ("Hegseth fires the Pentagon's top military planner (AJC)", "https://www.ajc.com/news/2026/10/hegseth-fires-the-pentagons-top-military-planner-even-as-trump-considers-new-iran-strikes/")]),

"lider_iran": dict(
 res=["La máxima autoridad formal de Irán: comanda las fuerzas armadas, la justicia y los medios estatales.",
      "Tras la muerte de Ali Jamenei en los ataques del 28 de febrero de 2026, la Asamblea de Expertos eligió a su hijo Mojtaba. Según fuentes citadas por Reuters, su papel es en gran medida legitimar decisiones que toman los comandantes de la Guardia Revolucionaria."],
 manda=["Mojtaba Jamenei, líder supremo desde marzo de 2026.", "Comandantes de la Guardia Revolucionaria y el Consejo Supremo de Seguridad Nacional, que dominan la estrategia de guerra."],
 dinero="Controla fundaciones y conglomerados como Setad, bajo creciente presión por el bloqueo naval de EE.UU.",
 crono=[("1989-06", "Ali Jamenei sucede a Jomeini."), ("2026-02-28", "Ali Jamenei muere en los ataques de EE.UU. e Israel."), ("2026-03-08", "Mojtaba Jamenei es anunciado como nuevo líder supremo."), ("2026-08-10", "Nombra una nueva cúpula militar.")],
 fuentes=[("Iran names Mojtaba Khamenei as supreme leader (Hawaii Tribune-Herald, NYT)", "https://www.hawaiitribune-herald.com/2026/03/09/nation-world-news/iran-names-mojtaba-khamenei-as-supreme-leader/"),
          ("Iran's Guards seize wartime power, blunting Supreme Leader's role (Reuters vía Times of Israel)", "https://www.timesofisrael.com/irgc-shores-up-wartime-power-in-iran-blunting-supreme-leaders-role/")]),

"cgri": dict(
 res=["Cuerpo de la Guardia Revolucionaria Islámica: fuerza militar, servicio de inteligencia, conglomerado económico y patrocinador de milicias en la región.",
      "Desde la guerra de 2026 concentra el poder de decisión en Irán: según Reuters, impuso a Mojtaba Jamenei como líder supremo y sus comandantes dominan la estrategia."],
 manda=["Ahmad Vahidi, comandante en jefe desde el 1 de marzo de 2026, confirmado en agosto.", "Mostafa Izadi, segundo comandante; Ali Azmaei, jefe de la Armada de la Guardia; Hossein Taeb, jefe del Basij."],
 dinero="Controla empresas de construcción, energía y comercio, y redes de contrabando de petróleo.",
 crono=[("1979-05", "Creación tras la revolución."), ("2025-06", "Muere su comandante Hossein Salami en un ataque israelí."), ("2026-02-28", "Muere su comandante Mohammad Pakpour."), ("2026-03", "La Guardia impone la elección de Mojtaba Jamenei.")],
 fuentes=[("Iran appoints Abdollahi armed forces chief, Vahidi IRGC commander (Anadolu)", "https://www.aa.com.tr/en/middle-east/iran-appoints-abdollahi-armed-forces-chief-vahidi-irgc-commander/4023476"),
          ("Iran's new leader was elevated by the Revolutionary Guards (Reuters vía GMA)", "https://www.gmanetwork.com/news/topstories/world/979526/iran-s-new-leader-still-silent-was-elevated-by-the-revolutionary-guards/story/")]),

"saud": dict(
 res=["La familia real gobierna Arabia Saudita como monarquía absoluta y controla Saudi Aramco y el fondo soberano PIF.",
      "El poder efectivo lo ejerce el príncipe heredero, primer ministro desde 2022, bajo el reinado de su padre."],
 manda=["Rey Salmán bin Abdulaziz.", "Príncipe heredero y primer ministro Mohammed bin Salmán, gobernante de hecho."],
 dinero="Controla la mayor empresa petrolera del mundo (Aramco) y el PIF, uno de los mayores fondos soberanos.",
 crono=[("1932-09", "Fundación del reino."), ("2017-06", "Mohammed bin Salmán es nombrado heredero."), ("2022-09", "Asume como primer ministro."), ("2026-08", "El rey reconstituye el gabinete bajo la presidencia del heredero.")],
 fuentes=[("Saudi King reconstitutes Cabinet under Crown Prince (The National)", "https://thenationalnews.com/news/gulf/2026/08/13/saudi-king-reconstitutes-cabinet-under-crown-prince-mohammed-bin-salman"),
          ("House of Saud (Wikipedia)", W + "House_of_Saud")]),

"pm_israel": dict(
 res=["Jefatura del gobierno de Israel, que conduce las guerras en Gaza, Líbano e Irán y comanda el Mossad.",
      "Tras las elecciones del 27 de octubre de 2026, ni el bloque de Netanyahu (53 bancas) ni la oposición (48) alcanzaron mayoría; Netanyahu sigue como primer ministro en funciones."],
 manda=["Benjamín Netanyahu, primer ministro en funciones.", "Gabinete de seguridad.", "Partidos árabes con 19 bancas, decisivos para cualquier coalición."],
 dinero="Administra el presupuesto de defensa y la ayuda militar de EE.UU.",
 crono=[("2023-10-07", "Ataque de Hamás y comienzo de la guerra en Gaza."), ("2025-06", "Guerra de doce días con Irán."), ("2026-02-28", "Ataques conjuntos con EE.UU. contra Irán."), ("2026-10-27", "Elecciones sin mayoría.")],
 fuentes=[("Israel election result shows no overall majority (Al Jazeera)", "https://www.aljazeera.com/news/2026/10/29/israel-election-result-shows-no-overall-majority-as-vote-count-complete"),
          ("Right-wing bloc wins 53 seats (JNS)", "https://jns.org/news/israel-news/right-wing-bloc-wins-israeli-election-with-53-seats-likud-emerges-as-largest-party")]),

"spacex": dict(
 res=["Empresa aeroespacial que domina los lanzamientos orbitales y opera Starlink, la mayor red de satélites del mundo.",
      "En febrero de 2026 absorbió a xAI, que a su vez era dueña de la red social X, y creó un conglomerado de cohetes, internet satelital, inteligencia artificial y medios."],
 manda=["Elon Musk, fundador y accionista de control."],
 dinero="La fusión valuó a SpaceX en 1 billón de dólares y a xAI en 250.000 millones, según Reuters.",
 crono=[("2002-05", "Fundación."), ("2019-05", "Primeros satélites Starlink."), ("2025-03", "xAI absorbe a X."), ("2026-02-02", "SpaceX absorbe a xAI.")],
 fuentes=[("SpaceX Acquires xAI as Elon Musk Aims to Build Space-Based AI Data Centers (Outlook Business)", "https://www.outlookbusiness.com/corporate/spacex-acquires-xai-as-elon-musk-aims-to-build-space-based-ai-data-centers"),
          ("Elon Musk consolidates xAI into SpaceX (Built In)", "https://builtin.com/articles/elon-musk-consolidates-xai-spacex-20260203")]),

"amazon": dict(
 res=["Mayor empresa de comercio electrónico y logística de Occidente y dueña de AWS, la principal nube del mundo, usada por gobiernos y agencias de inteligencia.",
      "Su red física de depósitos y transporte y su nube le dan poder sobre la infraestructura de la economía digital."],
 manda=["Andy Jassy, director ejecutivo.", "Jeff Bezos, fundador y presidente ejecutivo del directorio."],
 dinero="Ingresos anuales de más de 600.000 millones de dólares; AWS aporta la mayor parte de la ganancia.",
 crono=[("1994-07", "Fundación."), ("2006-03", "Lanzamiento de AWS."), ("2013", "Contrato de nube con la CIA."), ("2022-12", "Contrato de nube militar conjunta (JWCC) con el Pentágono.")],
 fuentes=[("Amazon (company) (Wikipedia)", W + "Amazon_(company)"), ("Joint Warfighting Cloud Capability (Wikipedia)", W + "Joint_Warfighting_Cloud_Capability")]),

"gob_india": dict(
 res=["Gobierno de la India, el país más poblado del mundo y una potencia nuclear que mantiene autonomía entre los bloques.",
      "Compra petróleo y armas a Rusia mientras participa del Quad con EE.UU., Japón y Australia."],
 manda=["Narendra Modi, primer ministro desde 2014.", "Partido Popular Indio (BJP) y su organización matriz, el RSS."],
 dinero="Administra la quinta economía del mundo por PIB nominal.",
 crono=[("2014-05", "Modi llega al gobierno."), ("2020-06", "Choque fronterizo con China en Galwan."), ("2025-05", "Enfrentamiento militar con Pakistán.")],
 fuentes=[("Government of India (Wikipedia)", W + "Government_of_India"), ("Narendra Modi (Wikipedia)", W + "Narendra_Modi")]),

"alphabet": dict(
 res=["Dueña de Google, YouTube y Android: decide qué información encuentran miles de millones de personas y concentra datos de uso a escala mundial.",
      "Un tribunal de EE.UU. declaró en 2024 que su buscador es un monopolio ilegal."],
 manda=["Sundar Pichai, director ejecutivo.", "Larry Page y Sergey Brin, fundadores con mayoría de los votos por acciones de clase especial."],
 dinero="Una de las empresas más rentables del mundo, con ganancias anuales de más de 100.000 millones de dólares.",
 crono=[("1998-09", "Fundación de Google."), ("2006-10", "Compra de YouTube."), ("2015-10", "Reestructuración como Alphabet."), ("2024-08", "Fallo que la declara monopolio en búsquedas.")],
 fuentes=[("Alphabet Inc. (Wikipedia)", W + "Alphabet_Inc."), ("United States v. Google LLC (2020) (Wikipedia)", W + "United_States_v._Google_LLC_(2020)")]),

"downing": dict(
 res=["Gobierno del Reino Unido, potencia nuclear y miembro permanente del Consejo de Seguridad, con criterio estratégico propio dentro del bloque transoceánico.",
      "Andy Burnham asumió como primer ministro el 20 de julio de 2026, tras la renuncia de Keir Starmer."],
 manda=["Andy Burnham, primer ministro.", "John Healey, ministro de Hacienda; Ed Miliband, canciller."],
 dinero="Administra el presupuesto británico y supervisa la City de Londres, uno de los dos grandes centros financieros del mundo.",
 crono=[("2024-07", "Starmer gana las elecciones."), ("2026-07-20", "Burnham asume como primer ministro.")],
 fuentes=[("Andy Burnham becomes the UK's seventh prime minister in a decade (AP)", "https://www.local10.com/news/2026/07/20/andy-burnham-becomes-britains-7th-prime-minister-in-a-decade-after-starmer-resigns/"),
          ("UK politics explained, who holds power in 2026 (Rio Times)", "https://www.riotimesonline.com/uk-politics-explained-who-holds-power-2026/")]),

"turquia": dict(
 res=["Presidencia de Turquía: controla el segundo ejército de la OTAN, el estrecho del Bósforo y una política exterior que negocia con ambos bloques.",
      "El sistema presidencial vigente desde 2018 concentra el poder ejecutivo en el presidente."],
 manda=["Recep Tayyip Erdoğan, presidente.", "Organización Nacional de Inteligencia (MIT)."],
 dinero="Dirige el fondo soberano turco y la industria de defensa, con exportaciones de drones en ascenso.",
 crono=[("2003-03", "Erdoğan llega al gobierno como primer ministro."), ("2016-07", "Intento de golpe fallido."), ("2018-07", "Entra en vigor el sistema presidencial."), ("2019-07", "Recibe el sistema antiaéreo ruso S-400.")],
 fuentes=[("Presidency of Turkey (Wikipedia)", W + "President_of_Turkey")]),

"alnahyan": dict(
 res=["La familia gobernante de Abu Dabi controla el gobierno federal de Emiratos y algunos de los mayores fondos soberanos del mundo.",
      "Paneles de expertos de la ONU señalaron envíos de armas desde Emiratos a las Fuerzas de Apoyo Rápido de Sudán; Emiratos lo niega."],
 manda=["Mohamed bin Zayed, presidente de Emiratos y gobernante de Abu Dabi.", "Tahnoun bin Zayed, asesor de seguridad nacional y figura central de las inversiones en inteligencia artificial."],
 dinero="ADIA, Mubadala y ADQ administran en conjunto activos superiores al billón de dólares.",
 crono=[("1971-12", "Formación de Emiratos Árabes Unidos."), ("2022-05", "Mohamed bin Zayed asume la presidencia.")],
 fuentes=[("Al Nahyan family (Wikipedia)", W + "Al_Nahyan_family"), ("Abu Dhabi Investment Authority (Wikipedia)", W + "Abu_Dhabi_Investment_Authority")]),

"ffaa_egipto": dict(
 res=["Las Fuerzas Armadas son el poder real de Egipto desde 1952: de sus filas salen los presidentes y controlan una parte grande de la economía.",
      "Reciben ayuda militar anual de EE.UU. y derrocaron en 2013 al gobierno de la Hermandad Musulmana."],
 manda=["Abdelfatá al Sisi, presidente y exjefe del ejército.", "Consejo Supremo de las Fuerzas Armadas."],
 dinero="Empresas militares en construcción, alimentos, energía e infraestructura, con privilegios fiscales.",
 crono=[("1952-07", "Golpe de los Oficiales Libres."), ("2013-07", "Derrocamiento de Mohamed Morsi."), ("2014-06", "Sisi asume la presidencia.")],
 fuentes=[("Egyptian Armed Forces (Wikipedia)", W + "Egyptian_Armed_Forces"), ("Military economy of Egypt (Wikipedia)", W + "Economy_of_the_Egyptian_Armed_Forces")]),

"ptk": dict(
 res=["Partido único de Corea del Norte, que controla el Estado, el ejército y una economía cerrada, con armas nucleares.",
      "Desde 2024 es aliado militar formal de Rusia, a la que envió tropas."],
 manda=["Kim Jong-un, secretario general."],
 dinero="Ingresos por venta de armas a Rusia, trabajo en el exterior y robo de criptomonedas atribuido por la ONU.",
 crono=[("1949-06", "Fundación."), ("2011-12", "Kim Jong-un sucede a su padre."), ("2024-06", "Tratado de asociación estratégica con Rusia.")],
 fuentes=[("Workers' Party of Korea (Wikipedia)", W + "Workers%27_Party_of_Korea")]),

"santasede": dict(
 res=["Gobierno central de la Iglesia católica, con unos 1.400 millones de fieles, una red diplomática con casi todos los Estados y un territorio soberano propio.",
      "Su poder es sobre todo cultural y de relaciones; mantiene un acuerdo con China sobre el nombramiento de obispos."],
 manda=["Papa León XIV, elegido en mayo de 2025.", "Secretaría de Estado y la Curia romana."],
 dinero="Patrimonio inmobiliario, el Instituto para las Obras de Religión y donaciones.",
 crono=[("1929-02", "Pactos de Letrán y creación del Estado Vaticano."), ("2018-09", "Acuerdo provisorio con China."), ("2025-05", "Elección de León XIV.")],
 fuentes=[("Holy See (Wikipedia)", W + "Holy_See"), ("Pope Leo XIV (Wikipedia)", W + "Pope_Leo_XIV")]),

"althani": dict(
 res=["La familia gobernante de Catar controla una de las mayores reservas de gas del mundo, la cadena Al Jazeera y el fondo soberano QIA.",
      "Alberga la mayor base de EE.UU. en Medio Oriente y a la vez actúa como mediador con Hamás y otros actores del eje iraní."],
 manda=["Emir Tamim bin Hamad Al Thani."],
 dinero="La Autoridad de Inversiones de Catar administra cientos de miles de millones de dólares en activos.",
 crono=[("1971-09", "Independencia."), ("2013-06", "Tamim sucede a su padre."), ("2022-11", "Organiza el Mundial de fútbol.")],
 fuentes=[("House of Thani (Wikipedia)", W + "House_of_Thani"), ("Al Udeid Air Base (Wikipedia)", W + "Al_Udeid_Air_Base")]),

"meta": dict(
 res=["Dueña de Facebook, Instagram y WhatsApp: decide qué contenidos ven miles de millones de personas y concentra datos de comunicaciones privadas.",
      "Fue parte del programa PRISM revelado en 2013 y recibió sanciones de la Unión Europea por protección de datos y competencia."],
 manda=["Mark Zuckerberg, fundador, director ejecutivo y titular de la mayoría de los votos."],
 dinero="Ingresos por publicidad de más de 150.000 millones de dólares anuales.",
 crono=[("2004-02", "Fundación de Facebook."), ("2012-04", "Compra de Instagram."), ("2014-02", "Compra de WhatsApp."), ("2021-10", "Cambio de nombre a Meta.")],
 fuentes=[("Meta Platforms (Wikipedia)", W + "Meta_Platforms"), ("PRISM (Wikipedia)", W + "PRISM")]),

"microsoft": dict(
 res=["Dueña del sistema operativo y del software de oficina más usados del mundo, de la nube Azure y de una participación de alrededor del 27 % en OpenAI.",
      "Es proveedora central de gobiernos y del Pentágono."],
 manda=["Satya Nadella, director ejecutivo y presidente del directorio."],
 dinero="Ganancias anuales de más de 80.000 millones de dólares.",
 crono=[("1975-04", "Fundación."), ("2019-07", "Primera inversión en OpenAI."), ("2025-10", "Reestructuración de OpenAI y nueva participación.")],
 fuentes=[("Microsoft (Wikipedia)", W + "Microsoft"), ("OpenAI (Wikipedia)", W + "OpenAI")]),

"planalto": dict(
 res=["Presidencia de Brasil, la mayor economía de América Latina e independiente entre los bloques.",
      "Luiz Inácio Lula da Silva ganó el balotaje del 25 de octubre de 2026 con alrededor del 51,7 % y asumirá su cuarto mandato; Flávio Bolsonaro pidió anular el resultado."],
 manda=["Luiz Inácio Lula da Silva, presidente.", "Partido de los Trabajadores y una coalición en el Congreso."],
 dinero="Controla Petrobras, el BNDES y los bancos públicos.",
 crono=[("2023-01", "Lula asume su tercer mandato."), ("2025", "Aranceles de EE.UU. a Brasil."), ("2026-10-25", "Lula gana el balotaje.")],
 fuentes=[("Lula holds off far right with victory in Brazil presidential election (Al Jazeera)", "https://aljazeera.com/news/2026/10/26/lula-holds-off-far-right-with-victory-in-brazil-presidential-election"),
          ("Lula re-elected, Bolsonaro refuses to accept result (Sky News vía Radio X)", "https://www.radiox.co.uk/news/uk-world/lula-re-elected-president-in-brazil-electoral/")]),

"comisioneu": dict(
 res=["Órgano ejecutivo de la Unión Europea: propone leyes, negocia el comercio y aplica sanciones y normas de competencia que obligan a empresas de todo el mundo.",
      "Sus multas a Alphabet, Meta, Apple y X muestran un poder regulatorio de alcance global."],
 manda=["Ursula von der Leyen, presidenta.", "Colegio de comisarios."],
 dinero="Administra el presupuesto europeo y fondos comunes como el mecanismo para Ucrania.",
 crono=[("1958-01", "Creación de la Comisión de la CEE."), ("2019-12", "Von der Leyen asume la presidencia."), ("2022-11", "Entra en vigor la Ley de Mercados Digitales.")],
 fuentes=[("European Commission (Wikipedia)", W + "European_Commission"), ("Digital Markets Act (Wikipedia)", W + "Digital_Markets_Act")]),

"apple": dict(
 res=["Fabricante del iPhone y dueña de una plataforma de aplicaciones que controla qué software usan más de mil millones de personas.",
      "En septiembre de 2026 John Ternus reemplazó a Tim Cook como director ejecutivo; Cook pasó a presidente ejecutivo del directorio."],
 manda=["John Ternus, director ejecutivo desde el 1 de septiembre de 2026.", "Tim Cook, presidente ejecutivo, a cargo del vínculo con gobiernos."],
 dinero="Capitalización de alrededor de 4 billones de dólares al anunciarse la sucesión.",
 crono=[("1976-04", "Fundación."), ("2007-01", "Presentación del iPhone."), ("2011-08", "Tim Cook asume como director ejecutivo."), ("2026-09-01", "John Ternus asume como director ejecutivo.")],
 fuentes=[("Tim Cook stepping down, John Ternus confirmed as next Apple CEO (9to5Mac)", "https://9to5mac.com/2026/04/20/apple-ceo-tim-cook-stepping-down-john-ternus/"),
          ("Apple (Wikipedia)", W + "Apple_Inc.")]),

"ejercito_pak": dict(
 res=["El ejército es el poder real de Pakistán, potencia nuclear: define la política exterior y de seguridad por encima de los gobiernos civiles.",
      "En 2026 Pakistán medió entre EE.UU. e Irán y fue sede de las negociaciones."],
 manda=["Mariscal de campo Asim Munir, jefe del ejército y jefe de las Fuerzas de Defensa.", "Inteligencia Interservicios (ISI)."],
 dinero="Conglomerados empresariales como la Fundación Fauji.",
 crono=[("1958-10", "Primer golpe militar."), ("2025-05", "Enfrentamiento con la India."), ("2026-04", "Mediación en las negociaciones entre EE.UU. e Irán.")],
 fuentes=[("Pakistan Army (Wikipedia)", W + "Pakistan_Army"),
          ("US launches Iran blockade as talks continue (The National)", "https://www.thenationalnews.com/news/mena/2026/04/13/us-launches-iran-blockade-as-talks-continue-to-keep-ceasefire-alive")]),

"exxon": dict(
 res=["La mayor petrolera privada de Occidente, con producción en todos los continentes y fuerte influencia sobre la política energética de EE.UU."],
 manda=["Directorio y gerencia ejecutiva; sus mayores accionistas son fondos como Vanguard y BlackRock."],
 dinero="Ingresos de varios cientos de miles de millones de dólares anuales.",
 crono=[("1999-11", "Fusión de Exxon y Mobil."), ("2024-05", "Compra de Pioneer Natural Resources.")],
 fuentes=[("ExxonMobil (Wikipedia)", W + "ExxonMobil")]),

"samsung": dict(
 res=["Conglomerado familiar que es el mayor fabricante de memorias y de teléfonos del mundo y pesa decisivamente en la economía de Corea del Sur."],
 manda=["La familia Lee, que controla el grupo mediante participaciones cruzadas; Lee Jae-yong preside Samsung Electronics."],
 dinero="Samsung Electronics es la mayor empresa de Corea del Sur por ingresos.",
 crono=[("1938-03", "Fundación."), ("2022-10", "Lee Jae-yong asume la presidencia ejecutiva.")],
 fuentes=[("Samsung (Wikipedia)", W + "Samsung")]),

"sinaloa": dict(
 res=["Ya no es una sola organización: tras la captura de Ismael Zambada en 2024 se partió en facciones en guerra entre sí, con cientos de homicidios en Sinaloa.",
      "Los Mayos, la facción de Zambada, es la que más terreno ganó según estudios de 2026; Los Chapitos recibieron combatientes y dinero del CJNG, según reconoció el gobierno mexicano."],
 manda=["Los Mayos: liderados por Ismael Zambada Sicairos, hijo de El Mayo, según investigaciones periodísticas.", "Los Chapitos: Iván Archivaldo y Jesús Alfredo Guzmán Salazar.", "Otras dos facciones, una encabezada por Aureliano Guzmán, según Crisis Group."],
 dinero="Tráfico de fentanilo, cocaína y metanfetamina hacia EE.UU. El Mayo fue condenado en julio de 2026 a cadena perpetua y a un decomiso de 15.000 millones de dólares.",
 crono=[("2024-07", "Captura de Ismael Zambada en EE.UU."), ("2025-02", "EE.UU. lo designa organización terrorista extranjera."), ("2026-07-20", "Condena perpetua de El Mayo.")],
 fuentes=[("Ismael Zambada García (InSight Crime)", "https://insightcrime.org/mexico-organized-crime-news/ismael-zambada-garcia-el-mayo/"),
          ("Batalla por el Cartel de Sinaloa (WTOP)", "https://wtop.com/news/2026/07/batalla-por-el-cartel-de-sinaloa-asi-es-la-confrontacion-entre-grupos-que-ha-disparado-la-violencia-en-ese-estado-de-mexico/"),
          ("El día que un Chapito sedó a El Mayo (El Diario)", "https://www.eldiario.ec/centro/el-dia-que-un-chapito-sedo-a-el-mayo-y-cambio-para-siempre-el-cartel-de-sinaloa-10072026/")]),

"eliseo": dict(
 res=["Presidencia de Francia, única potencia nuclear de la Unión Europea, con fuerzas en el exterior y asiento permanente en el Consejo de Seguridad.",
      "Perdió su presencia militar en el Sahel, donde la reemplazó Rusia."],
 manda=["Emmanuel Macron, presidente hasta 2027.", "Consejo de Defensa y la DGSE."],
 dinero="Influye sobre empresas con participación estatal en energía, defensa y aeronáutica.",
 crono=[("1958-10", "Quinta República."), ("2017-05", "Macron asume."), ("2022-08", "Fin de la operación Barkhane en Malí.")],
 fuentes=[("President of France (Wikipedia)", W + "President_of_France")]),

"cia": dict(
 res=["Agencia de inteligencia exterior de EE.UU.: espionaje humano, operaciones encubiertas y, cada vez más, ciberoperaciones ofensivas.",
      "En 2026 se reorganizó para acelerar la adopción de inteligencia artificial."],
 manda=["John Ratcliffe, director desde enero de 2025."],
 dinero="Presupuesto clasificado dentro del programa nacional de inteligencia; su fondo In-Q-Tel invierte en empresas tecnológicas.",
 crono=[("1947-09", "Creación por la Ley de Seguridad Nacional."), ("1999", "Creación de In-Q-Tel."), ("2026-06-30", "Ratcliffe anuncia la reorganización tecnológica.")],
 fuentes=[("CIA reorganization prioritizes cyberoperations (GV Wire)", "https://gvwire.com/2026/07/01/cia-reorganization-prioritizes-cyberoperations/"),
          ("Director Ratcliffe delivers remarks at AWS Summit (CIA)", "https://www.cia.gov/stories/story/director-ratcliffe-delivers-remarks-at-amazon-web-services-summit/")]),

"jpmorgan": dict(
 res=["El mayor banco de EE.UU. y uno de los pilares del sistema financiero mundial por pagos, crédito y operaciones con bonos del Tesoro."],
 manda=["Jamie Dimon, presidente y director ejecutivo desde 2006, que planea seguir hasta tres años más.", "Doug Petno y Troy Rohrbaugh, copresidentes y candidatos a sucederlo desde junio de 2026."],
 dinero="Activos de más de 4 billones de dólares.",
 crono=[("2000-12", "Fusión de Chase Manhattan y J.P. Morgan."), ("2008-03", "Compra de Bear Stearns con apoyo de la Reserva Federal."), ("2026-06-25", "Nombramiento de dos copresidentes.")],
 fuentes=[("JPMorgan sets a new succession plan but Dimon plans to stay on (Virginia Business, Reuters)", "https://virginiabusiness.com/jpmorgan-reshuffles-leadership-jamie-dimon-stays/"),
          ("JPMorgan Chase (Wikipedia)", W + "JPMorgan_Chase")]),

"maktoum": dict(
 res=["La familia gobernante de Dubái convirtió el emirato en un centro mundial de comercio, logística, finanzas y aviación."],
 manda=["Mohammed bin Rashid Al Maktoum, gobernante de Dubái y vicepresidente de Emiratos."],
 dinero="Controla DP World, Emirates y el holding Dubai World.",
 crono=[("1833", "Los Al Maktoum se establecen en Dubái."), ("2006-01", "Mohammed bin Rashid asume como gobernante.")],
 fuentes=[("Al Maktoum family (Wikipedia)", W + "Al_Maktoum_family"), ("DP World (Wikipedia)", W + "DP_World")]),

"fdi": dict(
 res=["Fuerzas armadas de Israel, con capacidades de inteligencia de señales (Unidad 8200) entre las mejores del mundo y un poder aéreo que actúa en toda la región.",
      "En 2026 combatieron en Irán, Líbano y Gaza; mantienen una zona de seguridad en el sur del Líbano."],
 manda=["Teniente general Eyal Zamir, jefe del Estado Mayor desde marzo de 2025."],
 dinero="Presupuesto de defensa más la ayuda militar anual de EE.UU.",
 crono=[("1948-05", "Creación."), ("2023-10-07", "Comienza la guerra en Gaza."), ("2025-10", "Acuerdo con Hamás que pone fin a la guerra en Gaza y devuelve a los rehenes."), ("2026-02-28", "Ataques conjuntos con EE.UU. contra Irán.")],
 fuentes=[("Zamir: IDF to maintain Lebanon security zone (JNS)", "https://www.jns.org/news/israel-news/zamir-idf-to-maintain-lebanon-security-zone-until-long-term-security-is-ensured"),
          ("Eyal Zamir's legacy in the balance (Jerusalem Post)", "https://www.jpost.com/israel-news/defense-news/article-908276")]),

"nvidia": dict(
 res=["Diseña los chips que dominan el entrenamiento de inteligencia artificial; sus ventas a China están sujetas a controles de exportación de EE.UU.",
      "Depende de TSMC para fabricarlos y en 2025 anunció una inversión de hasta 100.000 millones de dólares en OpenAI."],
 manda=["Jensen Huang, fundador y director ejecutivo."],
 dinero="Una de las empresas más valiosas del mundo por capitalización.",
 crono=[("1993-04", "Fundación."), ("2022-10", "Primeros controles de EE.UU. a la exportación de chips avanzados a China."), ("2025-09", "Acuerdo de inversión con OpenAI.")],
 fuentes=[("Nvidia (Wikipedia)", W + "Nvidia")]),

"pfizer": dict(
 res=["Una de las mayores farmacéuticas del mundo; su vacuna contra el COVID-19 la convirtió en un actor de política sanitaria global."],
 manda=["Directorio y gerencia ejecutiva."],
 dinero="Ingresos anuales de decenas de miles de millones de dólares.",
 crono=[("1849", "Fundación en Nueva York."), ("2020-12", "Primera autorización de su vacuna contra el COVID-19.")],
 fuentes=[("Pfizer (Wikipedia)", W + "Pfizer")]),

"toyota": dict(
 res=["El mayor fabricante de automóviles del mundo por unidades vendidas, central para la industria japonesa."],
 manda=["La familia Toyoda conserva influencia en la conducción; Akio Toyoda preside el directorio."],
 dinero="Una de las mayores empresas del mundo por ingresos.",
 crono=[("1937-08", "Fundación de Toyota Motor."), ("1997-12", "Lanzamiento del Prius.")],
 fuentes=[("Toyota (Wikipedia)", W + "Toyota")]),

"visa": dict(
 res=["La mayor red de pagos con tarjeta del mundo: puede habilitar o cortar el acceso de países, empresas o personas al sistema de pagos.",
      "Salió de Rusia en 2022 tras la invasión de Ucrania."],
 manda=["Directorio y gerencia ejecutiva."],
 dinero="Margen de ganancia entre los más altos de las grandes empresas.",
 crono=[("1958", "Lanzamiento de BankAmericard."), ("2008-03", "Salida a bolsa."), ("2022-03", "Suspensión de operaciones en Rusia.")],
 fuentes=[("Visa Inc. (Wikipedia)", W + "Visa_Inc.")]),

"airbus": dict(
 res=["Fabricante europeo de aviones comerciales, helicópteros y sistemas de defensa y espacio, que comparte con Boeing el duopolio mundial de grandes aviones."],
 manda=["Directorio con participación estatal de Francia, Alemania y España."],
 dinero="Ingresos anuales de varias decenas de miles de millones de euros.",
 crono=[("1970-12", "Creación de Airbus Industrie."), ("2000-07", "Formación de EADS, antecesora del grupo actual.")],
 fuentes=[("Airbus (Wikipedia)", W + "Airbus")]),

"blackrock": dict(
 res=["La mayor gestora de activos del mundo: vota como accionista en miles de empresas y su plataforma Aladdin procesa riesgo para buena parte de la industria financiera.",
      "En 2020 la Reserva Federal la contrató para administrar compras de bonos."],
 manda=["Larry Fink, cofundador, presidente y director ejecutivo."],
 dinero="Más de 12 billones de dólares en activos administrados.",
 crono=[("1988", "Fundación."), ("2009-06", "Compra de Barclays Global Investors."), ("2020-03", "Contrato con la Reserva Federal.")],
 fuentes=[("BlackRock (Wikipedia)", W + "BlackRock"), ("Aladdin (BlackRock) (Wikipedia)", W + "Aladdin_(BlackRock)")]),
}

# ---- Tanda 2 (posiciones 41 a 80) ----
FICHAS.update({
"fsb": dict(
 res=["Servicio Federal de Seguridad de Rusia, heredero del KGB: contrainteligencia, seguridad interior, guardia de fronteras y operaciones sensibles en el espacio postsoviético.",
      "Pieza central del aparato de Putin y principal vigilante de las élites rusas."],
 manda=["Aleksandr Bórtnikov, director desde 2008; Serguéi Koroliov, primer subdirector.",
        "En septiembre de 2026 se informó de una reorganización en preparación que podría alcanzar a la conducción."],
 dinero="Presupuesto reservado dentro del gasto de seguridad del Estado ruso.",
 crono=[("1995-04", "Creación del FSB sobre la base del antiguo KGB."), ("2008-05", "Bórtnikov asume como director."),
        ("2026-09", "Informes sobre una reestructuración interna y salida del jefe de seguridad económica.")],
 fuentes=[("Federal Security Service (Wikipedia)", W + "Federal_Security_Service"),
          ("Meduza: el FSB prepara cambios de conducción (2026-09-14)", "https://meduza.io/en/news/2026/09/14/russia-s-dominant-security-agency-the-fsb-is-reportedly-preparing-for-a-leadership-shake-up-and-major-overhaul-as-early-as-october")]),

"lockheed": dict(
 res=["El mayor contratista de defensa del mundo: fabrica el F-35, misiles y sistemas espaciales para EE.UU. y sus aliados.",
      "Su producción condiciona la capacidad aérea de buena parte de la OTAN, Israel, Japón y Corea del Sur."],
 manda=["Jim Taiclet, presidente y director ejecutivo."],
 dinero="La mayor parte de sus ingresos proviene de contratos del gobierno de EE.UU.",
 crono=[("1995-03", "Fusión de Lockheed y Martin Marietta."), ("2006-12", "Primer vuelo del F-35.")],
 fuentes=[("Lockheed Martin (Wikipedia)", W + "Lockheed_Martin"), ("F-35 (Wikipedia)", W + "Lockheed_Martin_F-35_Lightning_II")]),

"mastercard": dict(
 res=["Segunda red de pagos con tarjeta del mundo; junto con Visa domina el cobro electrónico fuera de China.",
      "Suspendió sus operaciones en Rusia en 2022."],
 manda=["Michael Miebach, director ejecutivo."],
 dinero="Cobra comisiones por cada transacción procesada en su red.",
 crono=[("1966", "Origen como Interbank Card Association."), ("2006-05", "Salida a bolsa."), ("2022-03", "Suspensión en Rusia.")],
 fuentes=[("Mastercard (Wikipedia)", W + "Mastercard")]),

"openai": dict(
 res=["Creadora de ChatGPT y uno de los laboratorios de inteligencia artificial más influyentes del mundo.",
      "Completó en 2025 su conversión a sociedad con fines de lucro, abriendo el camino a una salida a bolsa."],
 manda=["Sam Altman, director ejecutivo; Sarah Friar, directora financiera.", "Microsoft es accionista relevante; la fundación sin fines de lucro conserva una participación."],
 dinero="Compromisos de inversión en centros de datos por cifras del orden del billón de dólares.",
 crono=[("2015-12", "Fundación como entidad sin fines de lucro."), ("2022-11", "Lanzamiento de ChatGPT."),
        ("2023-11", "Despido y regreso de Altman en cinco días."), ("2025-10", "Reestructuración aprobada; se convierte en sociedad de beneficio público.")],
 fuentes=[("OpenAI (Wikipedia)", W + "OpenAI"),
          ("Reuters vía Ynet: OpenAI prepara salida a bolsa", "https://www.ynetnews.com/business/article/rjnvbnx1bl")]),

"pcc": dict(
 res=["Primeiro Comando da Capital, la mayor facción criminal de Brasil: nacida en las cárceles de São Paulo, controla rutas de cocaína hacia Europa y presencia en los 27 estados.",
      "EE.UU. la designó organización terrorista el 28 de mayo de 2026."],
 manda=["Estructura de 'sintonías' con conducción histórica desde prisión."],
 dinero="Narcotráfico internacional y lavado en empresas formales, incluidas fintechs y combustibles.",
 crono=[("1993-08", "Fundación en el penal de Taubaté."), ("2006-05", "Ola de ataques en São Paulo."),
        ("2025-08", "Operación contra su estructura financiera."), ("2026-05-28", "Designación como organización terrorista por EE.UU.")],
 fuentes=[("Primeiro Comando da Capital (Wikipedia)", W + "Primeiro_Comando_da_Capital"),
          ("O Povo / AFP: CV y PCC designados terroristas (2026-05-28)", "https://www.opovo.com.br/noticias/mundo/2026/05/28/amp/comando-vermelho-e-pcc-as-faccoes-criminosas-mais-poderosas-do-brasil.html")]),

"tsmc": dict(
 res=["Fabrica la mayoría de los chips más avanzados del mundo, incluidos los de Apple y Nvidia: es el cuello de botella de la inteligencia artificial.",
      "Su ubicación en Taiwán la vuelve una pieza central del conflicto entre EE.UU. y China."],
 manda=["C. C. Wei, presidente y director ejecutivo."],
 dinero="Inversiones de decenas de miles de millones de dólares en plantas en Arizona, Japón y Alemania.",
 crono=[("1987-02", "Fundación por Morris Chang."), ("2020-05", "Anuncio de la planta de Arizona.")],
 fuentes=[("TSMC (Wikipedia)", W + "TSMC")]),

"ffaa_rusia": dict(
 res=["Fuerzas armadas con el mayor arsenal nuclear del mundo, en guerra en Ucrania desde 2022.",
      "El gasto bélico consume una parte creciente del presupuesto ruso."],
 manda=["Andréi Belousov, ministro de Defensa desde mayo de 2024; Valeri Guerásimov, jefe del Estado Mayor."],
 dinero="Según Belousov, el gasto directo en la guerra superó en 2025 el 5% del PBI.",
 crono=[("2022-02-24", "Invasión a gran escala de Ucrania."), ("2024-05-14", "Belousov reemplaza a Shoigú."), ("2026-10", "Tregua local en Jersón del 27 de octubre al 1 de noviembre.")],
 fuentes=[("Russian Armed Forces (Wikipedia)", W + "Russian_Armed_Forces"),
          ("Euromaidan Press: el costo de la guerra según Belousov", "https://euromaidanpress.com/?p=381438")]),

"glencore": dict(
 res=["Una de las mayores comercializadoras y mineras del mundo: cobre, cobalto, carbón, zinc y petróleo.",
      "En 2022 se declaró culpable de sobornos en siete países ante EE.UU., Reino Unido y Brasil."],
 manda=["Gary Nagle, director ejecutivo."],
 dinero="Pagó más de 1.500 millones de dólares en resoluciones por corrupción y manipulación de mercados en 2022.",
 crono=[("1974", "Fundación como Marc Rich + Co AG."), ("2011-05", "Salida a bolsa en Londres."), ("2022-05", "Declaración de culpabilidad por sobornos.")],
 fuentes=[("Glencore (Wikipedia)", W + "Glencore")]),

"goldman": dict(
 res=["Banco de inversión líder en fusiones, emisiones y operaciones de mercado; cantera histórica de secretarios del Tesoro de EE.UU."],
 manda=["David Solomon, presidente y director ejecutivo."],
 dinero="Activos por más de 1,5 billones de dólares.",
 crono=[("1869", "Fundación en Nueva York."), ("2008-09", "Conversión en banco holding durante la crisis."), ("2020-10", "Acuerdo por el escándalo 1MDB.")],
 fuentes=[("Goldman Sachs (Wikipedia)", W + "Goldman_Sachs"), ("1MDB scandal (Wikipedia)", W + "1Malaysia_Development_Berhad_scandal")]),

"palantir": dict(
 res=["Software de análisis de datos para inteligencia, defensa y policía; contratista clave del Pentágono y de servicios aliados.",
      "Fue financiada al inicio por In-Q-Tel, el brazo de inversión de la CIA."],
 manda=["Alex Karp, director ejecutivo; Peter Thiel, cofundador y presidente del directorio."],
 dinero="Ingresos crecientes por contratos gubernamentales y comerciales de inteligencia artificial.",
 crono=[("2003", "Fundación."), ("2020-09", "Salida a bolsa."), ("2024-11", "Ingreso al índice S&P 500.")],
 fuentes=[("Palantir Technologies (Wikipedia)", W + "Palantir_Technologies"), ("In-Q-Tel (Wikipedia)", W + "In-Q-Tel")]),

"harvard": dict(
 res=["La universidad más rica del mundo y cantera de élites políticas y económicas.",
      "Desde 2025 enfrenta al gobierno de Trump, que le cortó más de 2.600 millones de dólares en fondos de investigación; un juez federal declaró ilegal el corte en septiembre de 2025."],
 manda=["Alan Garber, presidente; la Corporación de Harvard extendió su mandato por tiempo indefinido en diciembre de 2025."],
 dinero="Fondo patrimonial superior a 50.000 millones de dólares.",
 crono=[("1636", "Fundación."), ("2025-04", "Congelamiento de fondos federales."), ("2025-09-03", "Fallo judicial contra el corte de fondos."),
        ("2026-02", "Trump eleva a 1.000 millones de dólares su exigencia de acuerdo.")],
 fuentes=[("Harvard University (Wikipedia)", W + "Harvard_University"),
          ("Harvard Magazine: continuidad de Garber", "https://www.harvardmagazine.com/university-news/harvard-garber-presidency-courts-research-funding"),
          ("Daily Signal: Trump pide 1.000 millones (2026-02-05)", "https://www.dailysignal.com/2026/02/05/why-trump-is-frustrated-with-harvard-university-negotiations/")]),

"bjp": dict(
 res=["Partido gobernante de la India desde 2014, brazo político del movimiento nacionalista hindú que encabeza la RSS.",
      "Se presenta como el partido con más afiliados del mundo."],
 manda=["Narendra Modi, primer ministro, y Amit Shah, ministro del Interior, son el centro del poder.",
        "Nitin Nabin asumió como presidente nacional del partido el 20 de enero de 2026, sucediendo a J. P. Nadda."],
 dinero="Principal receptor de financiamiento político empresario en la India.",
 crono=[("1925-09", "Fundación de la RSS."), ("1980-04", "Fundación del BJP."), ("2014-05", "Modi llega al gobierno."), ("2026-01-20", "Nitin Nabin, presidente del partido.")],
 fuentes=[("Bharatiya Janata Party (Wikipedia)", W + "Bharatiya_Janata_Party"), ("Rashtriya Swayamsevak Sangh (Wikipedia)", W + "Rashtriya_Swayamsevak_Sangh"),
          ("All India Radio: Nabin asume (2026-01-20)", "https://newsonair.gov.in/bjp-appoints-nitin-nabin-as-new-national-party-president-pm-shows-confidence-in-his-leadership/")]),

"cjng": dict(
 res=["Cártel Jalisco Nueva Generación: una de las organizaciones criminales más violentas y extendidas del mundo, con presencia en México, EE.UU. y decenas de países.",
      "Designado organización terrorista por EE.UU. en 2025."],
 manda=["Su fundador, Nemesio Oseguera, 'El Mencho', murió en un operativo militar en Tapalpa el 22 de febrero de 2026.",
        "EE.UU. señala desde julio de 2026 a su hijastro Juan Carlos Valencia González, 'El 03', como nuevo líder; analistas sostienen que el poder está repartido entre mandos regionales."],
 dinero="Fentanilo, metanfetamina, cocaína, extorsión, robo de combustible y lavado.",
 crono=[("2009", "Surgimiento tras la ruptura del cártel del Milenio."), ("2025-02", "Designación como organización terrorista por EE.UU."),
        ("2026-02-22", "Muerte de 'El Mencho' en Tapalpa."), ("2026-07", "EE.UU. identifica a 'El 03' como líder y ofrece 5 millones de dólares.")],
 fuentes=[("Jalisco New Generation Cartel (Wikipedia)", W + "Jalisco_New_Generation_Cartel"),
          ("El Financiero: EE.UU. señala a 'El 03' (2026-07-08)", "https://elfinanciero.com.mx/nacional/2026/07/08/cjng-tiene-nuevo-lider-el-03-toma-mando-tras-muerte-del-mencho-segun-eu/"),
          ("InSight Crime: el poder en el CJNG se comparte", "https://insightcrime.org/es/news/ee-uu-senalo-heredero-mencho-poder-cjng-comparte/")]),

"fifa": dict(
 res=["Gobierna el fútbol mundial y su torneo más rentable; decide sedes con peso diplomático, como el Mundial 2034 en Arabia Saudita.",
      "Organizó el Mundial 2026 en EE.UU., México y Canadá."],
 manda=["Gianni Infantino, presidente desde 2016."],
 dinero="Ingresos de varios miles de millones de dólares por ciclo mundialista.",
 crono=[("1904-05", "Fundación en París."), ("2015-05", "Escándalo de corrupción y detenciones en Zúrich."), ("2026-06", "Mundial en Norteamérica.")],
 fuentes=[("FIFA (Wikipedia)", W + "FIFA"), ("2015 FIFA corruption case (Wikipedia)", W + "2015_FIFA_corruption_case")]),

"prince": dict(
 res=["Conglomerado camboyano que EE.UU. y el Reino Unido sancionaron en octubre de 2025 acusándolo de operar centros de estafa con trabajadores víctimas de trata.",
      "EE.UU. promovió el decomiso de 127.271 bitcoins vinculados al grupo."],
 manda=["Su fundador, Chen Zhi, fue detenido en Camboya y extraditado a China el 7 de enero de 2026; Camboya le revocó la ciudadanía.",
        "El grupo niega las acusaciones."],
 dinero="Según la acusación de EE.UU., fraude con criptomonedas y lavado a escala de miles de millones de dólares.",
 crono=[("2015", "Fundación del grupo."), ("2025-10", "Acusación en EE.UU. y sanciones de EE.UU. y Reino Unido."),
        ("2026-01-07", "Extradición de Chen Zhi a China.")],
 fuentes=[("Prince Group (Wikipedia)", W + "Prince_Group"),
          ("Dawn / AFP: Camboya extradita a Chen Zhi (2026-01-09)", "https://www.dawn.com/news/1965921")]),

"boeing": dict(
 res=["Uno de los dos fabricantes de grandes aviones comerciales del mundo y gran contratista de defensa y espacio de EE.UU."],
 manda=["Kelly Ortberg, presidente y director ejecutivo desde agosto de 2024."],
 dinero="Las ventas de aviones son una herramienta de la diplomacia comercial de Washington.",
 crono=[("1916-07", "Fundación."), ("2019-03", "Inmovilización mundial del 737 MAX."), ("2024-08-08", "Ortberg asume como director ejecutivo."),
        ("2026-10", "La FAA certifica el 737 MAX 10.")],
 fuentes=[("Boeing (Wikipedia)", W + "Boeing"), ("Leeham News", "https://leehamnews.com/tag/ortberg-first-anniversary/")]),

"deloitte": dict(
 res=["La mayor red de servicios profesionales del mundo: auditoría, consultoría y asesoría a gobiernos y grandes empresas."],
 manda=["Red de firmas miembro coordinadas por Deloitte Touche Tohmatsu Limited, con sede en Londres."],
 dinero="Ingresos globales superiores a 60.000 millones de dólares.",
 crono=[("1845", "Fundación por William Welch Deloitte en Londres."), ("1989", "Fusión que da origen a la red actual.")],
 fuentes=[("Deloitte (Wikipedia)", W + "Deloitte")]),

"mit": dict(
 res=["Instituto de investigación tecnológica de primer nivel mundial, ligado históricamente al complejo militar e industrial de EE.UU."],
 manda=["Sally Kornbluth, presidenta."],
 dinero="Fondo patrimonial de varias decenas de miles de millones de dólares y grandes contratos federales de investigación.",
 crono=[("1861-04", "Fundación."), ("1951", "Creación del Lincoln Laboratory para defensa.")],
 fuentes=[("Massachusetts Institute of Technology (Wikipedia)", W + "Massachusetts_Institute_of_Technology"), ("MIT Lincoln Laboratory (Wikipedia)", W + "MIT_Lincoln_Laboratory")]),

"rtx": dict(
 res=["Gigante de defensa y aeroespacial: misiles Patriot y Tomahawk, motores Pratt & Whitney y aviónica Collins."],
 manda=["Chris Calio, director ejecutivo."],
 dinero="Su segmento de defensa creció con la demanda de misiles por las guerras de Ucrania y Medio Oriente.",
 crono=[("2020-04", "Fusión de Raytheon y United Technologies."), ("2023-07", "Nombre actual, RTX.")],
 fuentes=[("RTX Corporation (Wikipedia)", W + "RTX_Corporation")]),

"siemens": dict(
 res=["Conglomerado industrial alemán: automatización, redes eléctricas, ferrocarriles y software industrial."],
 manda=["Roland Busch, director ejecutivo."],
 dinero="En 2008 pagó unos 1.600 millones de dólares en EE.UU. y Alemania por un caso de sobornos.",
 crono=[("1847-10", "Fundación en Berlín."), ("2008-12", "Acuerdo por sobornos.")],
 fuentes=[("Siemens (Wikipedia)", W + "Siemens")]),

"stanford": dict(
 res=["Universidad en el corazón de Silicon Valley: origen de fundadores, capital de riesgo y tecnología de las grandes plataformas."],
 manda=["Jonathan Levin, presidente desde agosto de 2024."],
 dinero="Fondo patrimonial superior a 35.000 millones de dólares.",
 crono=[("1885-11", "Fundación."), ("1998-09", "Google nace de un proyecto de doctorado en Stanford.")],
 fuentes=[("Stanford University (Wikipedia)", W + "Stanford_University")]),

"ndrangheta": dict(
 res=["Mafia calabresa considerada una de las organizaciones criminales más poderosas del mundo por su control de buena parte de la cocaína que entra a Europa.",
      "Opera en sociedad con facciones brasileñas y redes sudamericanas a través de puertos de carga."],
 manda=["Estructura federada de familias ('ndrine') con sede histórica en Calabria."],
 dinero="Reinvierte ganancias del narcotráfico en empresas legales en Italia, Alemania y otros países.",
 crono=[("2007-08", "Masacre de Duisburgo."), ("2021-01", "Maxi juicio Rinascita Scott."),
        ("2026-09-17", "Operación EREDITÀ de Italia y Brasil con apoyo de Europol.")],
 fuentes=[("'Ndrangheta (Wikipedia)", W + "%27Ndrangheta"),
          ("Europol vía IEU Monitoring: operación EREDITÀ (2026-09-17)", "https://ieu-monitoring.com/?p=1250004")]),

"cv": dict(
 res=["Comando Vermelho, la facción criminal más antigua de Brasil: controla barrios enteros de Río de Janeiro y se expandió al norte del país.",
      "EE.UU. la designó organización terrorista el 28 de mayo de 2026, junto con el PCC."],
 manda=["Conducción colegiada con jefes históricos presos."],
 dinero="Narcotráfico, control territorial y cobros a servicios; la policía de Río atribuyó a su núcleo financiero un movimiento de unos 6.000 millones de reales en un año.",
 crono=[("1979", "Surgimiento en el penal de Ilha Grande."), ("2025-10", "Operativo en Río con más de cien muertos."),
        ("2026-05-28", "Designación como organización terrorista por EE.UU.")],
 fuentes=[("Comando Vermelho (Wikipedia)", W + "Comando_Vermelho"),
          ("SBT News: operativo contra el brazo financiero del CV (2026-05-29)", "https://sbtnews.sbt.com.br/noticia/policia/operacao-no-rio-mira-nucleo-financeiro-do-cv-14-sao-presos")]),

"coi": dict(
 res=["Dueño de los Juegos Olímpicos: decide sedes, sanciones a países y reglas del deporte de alto rendimiento."],
 manda=["Kirsty Coventry, presidenta desde junio de 2025, primera mujer en el cargo."],
 dinero="Ingresos por derechos de televisión y patrocinios de varios miles de millones de dólares por ciclo.",
 crono=[("1894-06", "Fundación en París."), ("2025-06", "Coventry asume la presidencia.")],
 fuentes=[("International Olympic Committee (Wikipedia)", W + "International_Olympic_Committee")]),

"berkshire": dict(
 res=["Conglomerado inversor con seguros, ferrocarriles, energía y grandes participaciones en Apple, bancos y petroleras."],
 manda=["Greg Abel, director ejecutivo desde el 1 de enero de 2026; Warren Buffett sigue como presidente del directorio."],
 dinero="Una de las mayores reservas de efectivo de cualquier empresa del mundo.",
 crono=[("1965", "Buffett toma el control."), ("2026-01-01", "Abel sucede a Buffett como director ejecutivo.")],
 fuentes=[("Berkshire Hathaway (Wikipedia)", W + "Berkshire_Hathaway"),
          ("Fortune: cambios de directores ejecutivos (2026-01-09)", "https://fortune.com/2026/01/09/fortune-500-power-moves-2025-review-jan-9-2026/")]),

"cargill": dict(
 res=["La mayor empresa privada de EE.UU. y una de las grandes comercializadoras de granos del mundo (grupo ABCD)."],
 manda=["Brian Sikes, director ejecutivo; las familias Cargill y MacMillan son dueñas de la mayoría."],
 dinero="Ingresos superiores a 150.000 millones de dólares sin cotizar en bolsa.",
 crono=[("1865", "Fundación en Iowa.")],
 fuentes=[("Cargill (Wikipedia)", W + "Cargill"), ("ABCD Grain Traders (Wikipedia)", W + "ABCD_Grain_Traders")]),

"walton": dict(
 res=["Familia controladora de Walmart, el mayor empleador privado del mundo y la mayor cadena minorista."],
 manda=["Greg Penner, yerno de Rob Walton, preside Walmart; John Furner es director ejecutivo desde el 1 de febrero de 2026."],
 dinero="Una de las mayores fortunas familiares del mundo.",
 crono=[("1962-07", "Sam Walton abre el primer Walmart."), ("2026-02-01", "Furner sucede a Doug McMillon.")],
 fuentes=[("Walton family (Wikipedia)", W + "Walton_family"),
          ("Retail Insight Network: Furner, director ejecutivo de Walmart", "https://www.retail-insight-network.com/?p=117567")]),

"fed": dict(
 res=["Banco central de EE.UU.: fija la tasa de referencia mundial y provee dólares al sistema financiero global mediante líneas de canje con otros bancos centrales."],
 manda=["Kevin Warsh, presidente desde el 22 de mayo de 2026, elegido por Trump; Jerome Powell permanece como miembro de la Junta."],
 dinero="Su balance supera los 6 billones de dólares.",
 crono=[("1913-12", "Ley de la Reserva Federal."), ("2008-11", "Comienza la expansión cuantitativa."),
        ("2026-05-22", "Warsh jura como presidente.")],
 fuentes=[("Federal Reserve (Wikipedia)", W + "Federal_Reserve"),
          ("Deseret News: jura de Warsh (2026-05-22)", "https://www.deseret.com/politics/2026/05/22/president-trump-clarence-thomas-federal-reserve-kevin-walsh-interest-rates/")]),

"reuters": dict(
 res=["Agencia de noticias y proveedor de datos financieros y legales: sus despachos alimentan a miles de medios del mundo."],
 manda=["La familia Thomson controla la empresa a través de Woodbridge."],
 dinero="Ingresos principalmente por servicios legales, fiscales y de información profesional.",
 crono=[("1851", "Paul Julius Reuter funda la agencia en Londres."), ("2008-04", "Thomson compra Reuters.")],
 fuentes=[("Thomson Reuters (Wikipedia)", W + "Thomson_Reuters"), ("Reuters (Wikipedia)", W + "Reuters")]),

"sud": dict(
 res=["Iglesia mormona con más de 17 millones de miembros declarados y una red misionera global.",
      "Su fondo de inversión, Ensign Peak, administra una de las mayores carteras de inversión religiosa del mundo."],
 manda=["La Primera Presidencia y el Quórum de los Doce Apóstoles."],
 dinero="En 2023 la SEC multó a la iglesia y a Ensign Peak por ocultar inversiones en sociedades pantalla.",
 crono=[("1830-04", "Fundación por Joseph Smith."), ("2023-02", "Multa de la SEC.")],
 fuentes=[("The Church of Jesus Christ of Latter-day Saints (Wikipedia)", W + "The_Church_of_Jesus_Christ_of_Latter-day_Saints"),
          ("Ensign Peak Advisors (Wikipedia)", W + "Ensign_Peak_Advisors")]),

"nsa": dict(
 res=["Agencia de inteligencia de señales de EE.UU.: intercepta comunicaciones en todo el mundo y comparte información con la alianza Cinco Ojos.",
      "Su director también conduce el Comando Cibernético, que participó en operaciones contra instalaciones nucleares iraníes y en la caída de Maduro."],
 manda=["Gen. Joshua Rudd, director y jefe del Comando Cibernético, confirmado por el Senado el 10 de marzo de 2026 tras casi un año de vacancia."],
 dinero="Presupuesto reservado dentro del programa de inteligencia nacional.",
 crono=[("1952-11", "Creación."), ("2013-06", "Revelaciones de Snowden."), ("2025-04", "Trump destituye al director Timothy Haugh."),
        ("2026-03-10", "Confirmación de Rudd.")],
 fuentes=[("National Security Agency (Wikipedia)", W + "National_Security_Agency"),
          ("SecurityWeek: confirmación de Rudd", "https://www.securityweek.com/senate-confirms-joshua-rudd-to-lead-nsa-and-us-cyber-command/"),
          ("Nextgov: el Comando Cibernético en 2025", "https://www.nextgov.com/cybersecurity/2026/04/cyber-command-carried-out-over-8000-missions-2025-director-says/413035/")]),

"alibaba": dict(
 res=["Gigante chino de comercio electrónico, nube y pagos (a través de Ant Group)."],
 manda=["Eddie Wu, director ejecutivo; Joe Tsai, presidente del directorio."],
 dinero="Su nube es una de las principales de Asia en inteligencia artificial.",
 crono=[("1999-04", "Fundación por Jack Ma."), ("2020-11", "Suspensión de la salida a bolsa de Ant Group."), ("2023-03", "Reorganización en seis unidades.")],
 fuentes=[("Alibaba Group (Wikipedia)", W + "Alibaba_Group"), ("Ant Group (Wikipedia)", W + "Ant_Group")]),

"mps_china": dict(
 res=["Ministerio de Seguridad Pública: policía nacional china, vigilancia masiva y control del orden interno.",
      "Ejecutó en 2026 la extradición desde Camboya del jefe del Prince Group."],
 manda=["Wang Xiaohong, ministro; subordinado a la Comisión Central de Asuntos Políticos y Legales del Partido."],
 dinero="Parte del gasto de seguridad interna, que supera al de defensa.",
 crono=[("1949-10", "Creación."), ("2022-06", "Wang Xiaohong, ministro."), ("2026-01-07", "Repatriación de Chen Zhi desde Nom Pen.")],
 fuentes=[("Ministry of Public Security (China) (Wikipedia)", W + "Ministry_of_Public_Security_(China)"),
          ("KuCoin / BlockBeats: repatriación de Chen Zhi", "https://www.kucoin.com/news/flash/chinese-national-chen-zhi-head-of-prince-group-extradited-from-cambodia")]),

"tencent": dict(
 res=["Dueña de WeChat, la aplicación que concentra mensajería, pagos y servicios para más de mil millones de usuarios en China, y la mayor empresa de videojuegos del mundo."],
 manda=["Ma Huateng (Pony Ma), cofundador, presidente y director ejecutivo."],
 dinero="Participaciones en cientos de empresas tecnológicas de China y el exterior.",
 crono=[("1998-11", "Fundación en Shenzhen."), ("2011-01", "Lanzamiento de WeChat.")],
 fuentes=[("Tencent (Wikipedia)", W + "Tencent"), ("WeChat (Wikipedia)", W + "WeChat")]),

"gates": dict(
 res=["Una de las mayores fundaciones del mundo; uno de los principales donantes de la OMS y de programas de vacunación como Gavi.",
      "Anunció en 2025 que gastará su patrimonio y cerrará en 2045."],
 manda=["Bill Gates preside el directorio; Mark Suzman es director ejecutivo."],
 dinero="Dotación de más de 70.000 millones de dólares.",
 crono=[("2000-01", "Fundación."), ("2000", "Creación de Gavi con su apoyo."), ("2025-05", "Anuncio de cierre en 2045.")],
 fuentes=[("Gates Foundation (Wikipedia)", W + "Gates_Foundation"), ("Gavi (Wikipedia)", W + "Gavi,_the_Vaccine_Alliance")]),

"bayer": dict(
 res=["Grupo químico y farmacéutico alemán; con la compra de Monsanto pasó a ser uno de los dos mayores proveedores de semillas y agroquímicos del mundo."],
 manda=["Bill Anderson, director ejecutivo."],
 dinero="Arrastra miles de millones de dólares en litigios por el glifosato en EE.UU.",
 crono=[("1863", "Fundación."), ("2018-06", "Compra de Monsanto.")],
 fuentes=[("Bayer (Wikipedia)", W + "Bayer"), ("Monsanto (Wikipedia)", W + "Monsanto")]),

"gendyn": dict(
 res=["Contratista de defensa: submarinos nucleares, tanques Abrams, munición y aviones Gulfstream."],
 manda=["Phebe Novakovic, presidenta y directora ejecutiva."],
 dinero="Principal constructor de los submarinos nucleares de la Armada de EE.UU.",
 crono=[("1952", "Fundación."), ("1999", "Compra de Gulfstream.")],
 fuentes=[("General Dynamics (Wikipedia)", W + "General_Dynamics")]),

"msc": dict(
 res=["La mayor naviera de contenedores del mundo, de capital privado de la familia Aponte; también opera puertos y cruceros."],
 manda=["Familia Aponte; Soren Toft, director ejecutivo."],
 dinero="Flota de más de 800 buques; control de terminales en varios continentes.",
 crono=[("1970", "Fundación por Gianluigi Aponte."), ("2022-01", "Supera a Maersk como mayor naviera.")],
 fuentes=[("Mediterranean Shipping Company (Wikipedia)", W + "Mediterranean_Shipping_Company")]),

"mckinsey": dict(
 res=["La consultora estratégica más influyente: asesora a gobiernos y grandes empresas y forma a buena parte de la dirigencia corporativa."],
 manda=["Bob Sternfels, socio director global."],
 dinero="En 2021 pagó más de 570 millones de dólares a estados de EE.UU. por su asesoramiento a fabricantes de opioides.",
 crono=[("1926", "Fundación en Chicago."), ("2021-02", "Acuerdo por la crisis de los opioides.")],
 fuentes=[("McKinsey & Company (Wikipedia)", W + "McKinsey_%26_Company")]),

"bytedance": dict(
 res=["Dueña de TikTok y Douyin: el algoritmo de recomendación más influyente fuera de las plataformas estadounidenses.",
      "En enero de 2026 cerró la creación de TikTok USDS, una sociedad conjunta en EE.UU. donde conserva el 19,9%; Oracle, Silver Lake y MGX tienen el 15% cada uno."],
 manda=["Liang Rubo, director ejecutivo; el fundador Zhang Yiming conserva una participación relevante."],
 dinero="Uno de los mayores ingresos publicitarios del mundo.",
 crono=[("2012-03", "Fundación."), ("2017-11", "Compra de Musical.ly."), ("2024-04", "Ley de EE.UU. que obliga a vender TikTok."),
        ("2026-01-22", "Cierre de la sociedad conjunta TikTok USDS.")],
 fuentes=[("ByteDance (Wikipedia)", W + "ByteDance"),
          ("ABC News: TikTok cierra el acuerdo en EE.UU. (2026-01-23)", "https://abc7news.com/post/tiktok-finalizes-deal-keep-operating-us/18451438/")]),
})

# ---- Tanda 3 (posiciones 81 a 120) ----
FICHAS.update({
"talibanes": dict(
 res=["Gobiernan Afganistán desde agosto de 2021 tras la retirada de EE.UU.; Rusia fue en 2025 el primer país en reconocer formalmente su gobierno."],
 manda=["Hibatullah Akhundzada, líder supremo, gobierna desde Kandahar."],
 dinero="Aduanas, minería y comercio regional; ayuda internacional muy reducida.",
 crono=[("1994", "Surgimiento en Kandahar."), ("2001-11", "Caída de su primer gobierno."), ("2021-08-15", "Toma de Kabul."), ("2025-07", "Reconocimiento de Rusia.")],
 fuentes=[("Taliban (Wikipedia)", W + "Taliban"), ("Islamic Emirate of Afghanistan (Wikipedia)", W + "Islamic_Emirate_of_Afghanistan")]),

"anduril": dict(
 res=["Contratista de defensa de Silicon Valley: drones, sistemas autónomos y software de mando para el Pentágono y aliados."],
 manda=["Palmer Luckey, fundador; Brian Schimpf, director ejecutivo."],
 dinero="Valuada en decenas de miles de millones de dólares en rondas privadas.",
 crono=[("2017", "Fundación."), ("2024-12", "Acuerdo con OpenAI para defensa antidrones.")],
 fuentes=[("Anduril Industries (Wikipedia)", W + "Anduril_Industries")]),

"bae": dict(
 res=["Mayor contratista de defensa de Europa: buques, submarinos nucleares británicos, aviones de combate y munición; gran proveedor de Arabia Saudita."],
 manda=["Charles Woodburn, director ejecutivo."],
 dinero="En 2010 pagó cerca de 450 millones de dólares en EE.UU. y Reino Unido por un caso de corrupción ligado a ventas de armas.",
 crono=[("1999-11", "Fusión de British Aerospace y Marconi Electronic Systems."), ("2010-02", "Acuerdo por corrupción.")],
 fuentes=[("BAE Systems (Wikipedia)", W + "BAE_Systems"), ("Al-Yamamah arms deal (Wikipedia)", W + "Al-Yamamah_arms_deal")]),

"bce": dict(
 res=["Banco central de la eurozona: fija la política monetaria de 21 países y supervisa a los grandes bancos europeos."],
 manda=["Christine Lagarde, presidenta; anunció el 29 de octubre de 2026 que dejará el cargo el 7 de febrero de 2027, nueve meses antes de terminar su mandato.",
        "El sucesor lo designa el Consejo Europeo, antes de la elección presidencial francesa de 2027."],
 dinero="Emisor del euro, segunda moneda de reserva del mundo.",
 crono=[("1998-06", "Creación."), ("2012-07", "\"Whatever it takes\" de Draghi."), ("2019-11", "Lagarde asume."), ("2026-10-29", "Anuncio de renuncia anticipada de Lagarde.")],
 fuentes=[("European Central Bank (Wikipedia)", W + "European_Central_Bank"),
          ("Banque de France: comunicado del BCE (2026-10-29)", "https://www.banque-france.fr/en/press-release/ecb-president-lagarde-step-down-7-february-2027")]),

"epl": dict(
 res=["Ejército Popular de Liberación: las fuerzas armadas más grandes del mundo, subordinadas al Partido Comunista y no al Estado.",
      "Desde 2023 atraviesa purgas en su cúpula, incluida la expulsión del vicepresidente de la Comisión Militar Central He Weidong en 2025."],
 manda=["Xi Jinping preside la Comisión Militar Central."],
 dinero="Segundo presupuesto militar del mundo.",
 crono=[("1927-08-01", "Fundación."), ("2015-12", "Reforma militar de Xi."), ("2025-10", "Expulsión de He Weidong y otros generales.")],
 fuentes=[("People's Liberation Army (Wikipedia)", W + "People%27s_Liberation_Army"), ("Central Military Commission (China) (Wikipedia)", W + "Central_Military_Commission_(China)")]),

"spglobal": dict(
 res=["Calificadora de riesgo e índices bursátiles (S&P 500): sus notas condicionan el costo de deuda de países y empresas."],
 manda=["Martina Cheung, directora ejecutiva."],
 dinero="Junto con Moody's y Fitch concentra casi todo el mercado mundial de calificaciones.",
 crono=[("1860", "Origen en la guía de Henry Varnum Poor."), ("2011-08", "Rebaja de la nota de EE.UU."), ("2022-02", "Compra de IHS Markit.")],
 fuentes=[("S&P Global (Wikipedia)", W + "S%26P_Global"), ("Big Three (credit rating agencies) (Wikipedia)", W + "Big_Three_(credit_rating_agencies)")]),

"nyt": dict(
 res=["El diario de referencia de EE.UU. y uno de los más influyentes del mundo en la agenda política y diplomática."],
 manda=["La familia Ochs-Sulzberger controla la empresa; A. G. Sulzberger es editor."],
 dinero="Más de 11 millones de suscriptores, mayormente digitales.",
 crono=[("1851-09", "Fundación."), ("1896", "Adolph Ochs compra el diario."), ("1971-06", "Papeles del Pentágono.")],
 fuentes=[("The New York Times (Wikipedia)", W + "The_New_York_Times")]),

"vitol": dict(
 res=["La mayor comercializadora independiente de petróleo del mundo, con sede en Ginebra y Róterdam."],
 manda=["Sociedad privada de sus socios; Russell Hardy, director ejecutivo."],
 dinero="En 2020 pagó 135 millones de dólares en EE.UU. y Brasil por sobornos en América Latina.",
 crono=[("1966", "Fundación en Róterdam."), ("2020-12", "Acuerdo por sobornos.")],
 fuentes=[("Vitol (Wikipedia)", W + "Vitol")]),

"isis": dict(
 res=["Red yihadista con provincias activas en el Sahel, Mozambique, el Congo, Afganistán (ISIS-K) y remanentes en Siria e Irak."],
 manda=["Liderazgo central clandestino; las provincias tienen gran autonomía operativa."],
 dinero="Extorsión, secuestros y tributos en zonas de control en África.",
 crono=[("2014-06", "Proclamación del califato en Mosul."), ("2019-03", "Caída de Baghuz, último territorio en Siria."), ("2024-03", "Atentado de ISIS-K en Moscú.")],
 fuentes=[("Islamic State (Wikipedia)", W + "Islamic_State")]),

"jnim": dict(
 res=["Rama de Al Qaeda en el Sahel, la organización yihadista que más crece en el mundo; controla rutas y zonas rurales de Malí, Burkina Faso y Níger.",
      "Desde 2025 impone bloqueos de combustible sobre ciudades de Malí, incluida Bamako."],
 manda=["Iyad Ag Ghaly, líder."],
 dinero="Impuestos a poblaciones rurales, secuestros, minería de oro y contrabando.",
 crono=[("2017-03", "Fusión de grupos yihadistas sahelianos."), ("2024-09", "Ataque en Bamako."), ("2025-09", "Bloqueo de combustible en Malí.")],
 fuentes=[("Jama'at Nusrat al-Islam wal-Muslimin (Wikipedia)", W + "Jama%27at_Nasr_al-Islam_wal_Muslimin")]),

"aramco": dict(
 res=["La petrolera más rentable del mundo y caja central del Estado saudí; su producción condiciona el precio internacional del crudo.",
      "En la guerra con Irán, Arabia Saudita desvió exportaciones al puerto de Yanbu, sobre el mar Rojo, para evitar Ormuz."],
 manda=["Amin Nasser, director ejecutivo; el Estado saudí y el fondo soberano PIF son dueños de casi todo el capital."],
 dinero="Ganancias anuales superiores a 100.000 millones de dólares.",
 crono=[("1933", "Concesión a Standard Oil of California."), ("1980", "Nacionalización completa."), ("2019-09", "Ataque a Abqaiq."), ("2019-12", "Salida a bolsa en Riad.")],
 fuentes=[("Saudi Aramco (Wikipedia)", W + "Saudi_Aramco"),
          ("Al-Monitor / Reuters: ataques hutíes a petroleros saudíes (2026-07)", "https://www.al-monitor.com/originals/2026/07/houthis-claim-attacks-saudi-tankers-red-sea-raising-risk-new-chokepoint-iran-war")]),

"telegram": dict(
 res=["Mensajería con canales masivos: principal canal de información de la guerra de Ucrania, de gobiernos, militares y también de redes criminales."],
 manda=["Pavel Durov, fundador y dueño; investigado en Francia desde 2024 por presunta complicidad con delitos cometidos en la plataforma, que niega."],
 dinero="Ingresos por publicidad, suscripciones y bonos.",
 crono=[("2013-08", "Lanzamiento."), ("2024-08", "Detención de Durov en París.")],
 fuentes=[("Telegram (Wikipedia)", W + "Telegram_(software)"), ("Pavel Durov (Wikipedia)", W + "Pavel_Durov")]),

"hutis": dict(
 res=["Ansar Allah controla el norte de Yemen y la capital Saná; con misiles y drones amenaza el estrecho de Bab el-Mandeb.",
      "Entraron en la guerra de Irán en 2026 y en julio atacaron petroleros saudíes en el mar Rojo, anunciando un bloqueo a Arabia Saudita."],
 manda=["Abdul-Malik al-Huthi, líder."],
 dinero="Recaudación en zonas controladas, contrabando y apoyo iraní.",
 crono=[("2014-09", "Toma de Saná."), ("2023-11", "Comienzo de ataques al tráfico en el mar Rojo."), ("2026-07-23", "Ataques a los petroleros Encelia y Layla.")],
 fuentes=[("Houthis (Wikipedia)", W + "Houthis"),
          ("PBS / AP: ataques a petroleros saudíes (2026-07-23)", "https://www.pbs.org/newshour/amp/world/yemens-houthis-attack-saudi-tankers-in-the-red-sea-threatening-to-widen-iran-war")]),

"bbc": dict(
 res=["Servicio público británico de radio, televisión y noticias, con audiencia mundial en decenas de idiomas.",
      "Enfrenta una demanda de Trump por 10.000 millones de dólares por la edición de un discurso, y la renovación de su carta real."],
 manda=["Matt Brittin, ex Google, director general desde el 18 de mayo de 2026; Rhodri Talfan Davies, director general adjunto."],
 dinero="Financiada principalmente por la licencia de televisión.",
 crono=[("1922-10", "Fundación."), ("2025-11", "Renuncia de Tim Davie."), ("2026-05-18", "Brittin asume.")],
 fuentes=[("BBC (Wikipedia)", W + "BBC"),
          ("Arab News: Brittin designado (2026-03-25)", "https://www.arabnews.pk/node/2637630")]),

"maersk": dict(
 res=["Una de las mayores navieras de contenedores y operadoras portuarias del mundo; desvió sus buques del mar Rojo por los ataques hutíes."],
 manda=["La familia Mærsk Mc-Kinney Møller controla la empresa a través de A.P. Møller Holding; Vincent Clerc, director ejecutivo."],
 dinero="Ingresos de decenas de miles de millones de dólares; terminales en todos los continentes vía APM Terminals.",
 crono=[("1904", "Fundación en Dinamarca."), ("2017-06", "Ciberataque NotPetya.")],
 fuentes=[("Maersk (Wikipedia)", W + "Maersk")]),

"moodys": dict(
 res=["Calificadora de riesgo: sus notas mueven el costo del crédito de países y empresas; en 2025 quitó a EE.UU. la máxima calificación."],
 manda=["Rob Fauber, director ejecutivo; Berkshire Hathaway es uno de sus principales accionistas."],
 dinero="Margen de ganancia muy alto en un mercado concentrado en tres firmas.",
 crono=[("1909", "Primeras calificaciones de bonos ferroviarios."), ("2017-01", "Acuerdo de 864 millones de dólares por sus calificaciones previas a 2008."), ("2025-05", "Rebaja de la nota de EE.UU.")],
 fuentes=[("Moody's Ratings (Wikipedia)", W + "Moody%27s_Ratings")]),

"newscorp": dict(
 res=["Fox News, The Wall Street Journal, The Times y medios australianos: el grupo mediático conservador más influyente del mundo anglosajón."],
 manda=["Lachlan Murdoch, que en 2025 consolidó el control del fideicomiso familiar tras un acuerdo con sus hermanos."],
 dinero="Fox News es uno de los canales de cable más rentables de EE.UU.",
 crono=[("1980", "Fundación de News Corporation."), ("1996-10", "Lanzamiento de Fox News."), ("2023-04", "Acuerdo de 787 millones de dólares con Dominion."), ("2025-09", "Acuerdo sobre el fideicomiso familiar.")],
 fuentes=[("News Corp (Wikipedia)", W + "News_Corp"), ("Fox Corporation (Wikipedia)", W + "Fox_Corporation")]),

"trafigura": dict(
 res=["Una de las mayores comercializadoras de petróleo y metales del mundo."],
 manda=["Sociedad privada de sus empleados socios; Richard Holtum, director ejecutivo."],
 dinero="En 2024 un tribunal suizo la declaró culpable de sobornos en Angola.",
 crono=[("1993", "Fundación."), ("2006", "Caso de vertido tóxico en Costa de Marfil."), ("2024-12", "Condena en Suiza.")],
 fuentes=[("Trafigura (Wikipedia)", W + "Trafigura")]),

"oxford": dict(
 res=["Universidad que formó a decenas de primeros ministros británicos y a buena parte de la élite del antiguo imperio."],
 manda=["Irene Tracey, vicerrectora."],
 dinero="Patrimonio repartido entre la universidad y sus colegios.",
 crono=[("1096", "Primeros registros de enseñanza."), ("1902", "Creación de la beca Rhodes.")],
 fuentes=[("University of Oxford (Wikipedia)", W + "University_of_Oxford"), ("Rhodes Scholarship (Wikipedia)", W + "Rhodes_Scholarship")]),

"otan": dict(
 res=["Alianza militar de 32 países bajo liderazgo de EE.UU.; en 2025 sus miembros acordaron elevar el gasto de defensa al 5% del PBI hacia 2035."],
 manda=["Mark Rutte, secretario general; el comandante militar supremo es siempre un general estadounidense."],
 dinero="El presupuesto común es menor; el peso está en el gasto militar de cada miembro.",
 crono=[("1949-04-04", "Tratado de Washington."), ("2023-04", "Ingreso de Finlandia."), ("2024-03", "Ingreso de Suecia."), ("2025-06", "Cumbre de La Haya: meta del 5%.")],
 fuentes=[("NATO (Wikipedia)", W + "NATO"), ("2025 The Hague NATO summit (Wikipedia)", W + "2025_The_Hague_NATO_summit")]),

"stategrid": dict(
 res=["La mayor empresa eléctrica del mundo, de propiedad estatal china; opera redes en Brasil, Chile, Portugal, Filipinas y otros países."],
 manda=["Depende de la comisión estatal de activos (SASAC) y del Partido."],
 dinero="Ingresos superiores a 500.000 millones de dólares.",
 crono=[("2002-12", "Creación tras la división de la antigua empresa eléctrica estatal."), ("2017", "Compra de CPFL en Brasil.")],
 fuentes=[("State Grid Corporation of China (Wikipedia)", W + "State_Grid_Corporation_of_China")]),

"ucrania": dict(
 res=["Conduce la defensa de Ucrania frente a la invasión rusa, sostenida por ayuda militar y financiera occidental."],
 manda=["Volodímir Zelenski, presidente; la ley marcial suspende las elecciones."],
 dinero="Dependencia de la ayuda de la Unión Europea, EE.UU. y otros aliados.",
 crono=[("2019-05", "Zelenski asume."), ("2022-02-24", "Invasión rusa a gran escala."), ("2026-10", "Tregua local en Jersón.")],
 fuentes=[("President of Ukraine (Wikipedia)", W + "President_of_Ukraine"), ("Russian invasion of Ukraine (Wikipedia)", W + "Russian_invasion_of_Ukraine")]),

"byd": dict(
 res=["El mayor fabricante de autos eléctricos e híbridos del mundo; superó a Tesla en ventas de eléctricos y produce sus propias baterías."],
 manda=["Wang Chuanfu, fundador, presidente y director ejecutivo."],
 dinero="Plantas en China, Brasil, Hungría, Turquía y Tailandia.",
 crono=[("1995-02", "Fundación como fabricante de baterías."), ("2008-09", "Inversión de Berkshire Hathaway.")],
 fuentes=[("BYD Company (Wikipedia)", W + "BYD_Company")]),

"bpi": dict(
 res=["El banco de los bancos centrales: coordina normas de capital (Basilea) y foros de supervisión financiera mundial."],
 manda=["Pablo Hernández de Cos, gerente general desde julio de 2025."],
 dinero="Administra parte de las reservas de bancos centrales.",
 crono=[("1930-05", "Fundación en Basilea."), ("1988", "Primer acuerdo de Basilea.")],
 fuentes=[("Bank for International Settlements (Wikipedia)", W + "Bank_for_International_Settlements")]),

"catl": dict(
 res=["El mayor fabricante de baterías para autos eléctricos del mundo; provee a Tesla, BMW, Volkswagen y otras."],
 manda=["Robin Zeng (Zeng Yuqun), fundador y presidente."],
 dinero="Salida a bolsa en Hong Kong en 2025, una de las mayores del año.",
 crono=[("2011", "Fundación en Ningde."), ("2025-05", "Cotización en Hong Kong.")],
 fuentes=[("CATL (Wikipedia)", W + "CATL")]),

"kanzleramt": dict(
 res=["Gobierno de la mayor economía de Europa; encabeza el rearme alemán tras reformar en 2025 el freno constitucional a la deuda."],
 manda=["Friedrich Merz, canciller desde mayo de 2025, en coalición con el SPD."],
 dinero="Fondos especiales de cientos de miles de millones de euros para defensa e infraestructura.",
 crono=[("2025-03", "Reforma del freno a la deuda."), ("2025-05-06", "Merz asume como canciller.")],
 fuentes=[("Chancellor of Germany (Wikipedia)", W + "Chancellor_of_Germany"), ("Friedrich Merz (Wikipedia)", W + "Friedrich_Merz")]),

"dhs": dict(
 res=["Departamento de Seguridad Nacional: inmigración (ICE), fronteras, aduanas, Guardia Costera y ciberseguridad (CISA); ejecuta las deportaciones masivas."],
 manda=["Markwayne Mullin, secretario desde el 24 de marzo de 2026, tras la salida de Kristi Noem."],
 dinero="Presupuesto ampliado en 2025 para detención y deportaciones.",
 crono=[("2002-11", "Creación tras el 11 de septiembre."), ("2026-03-24", "Mullin jura como secretario.")],
 fuentes=[("United States Department of Homeland Security (Wikipedia)", W + "United_States_Department_of_Homeland_Security"),
          ("Casa Blanca: jura de Mullin (2026-03)", "https://www.whitehouse.gov/releases/2026/03/secretary-markwayne-mullin-is-ready-to-deliver-on-president-trumps-agenda")]),

"elbit": dict(
 res=["Principal fabricante de armamento privado de Israel: drones, electrónica, artillería y sistemas de vigilancia, exportados a decenas de países."],
 manda=["Bezhalel Machlis, director ejecutivo."],
 dinero="Ingresos impulsados por las guerras de Israel y el rearme europeo.",
 crono=[("1966", "Origen en Elron."), ("1996", "Constitución como Elbit Systems.")],
 fuentes=[("Elbit Systems (Wikipedia)", W + "Elbit_Systems")]),

"kantei": dict(
 res=["Gobierno de la cuarta economía del mundo y principal aliado de EE.UU. en Asia; acelera el rearme y endureció su postura sobre Taiwán."],
 manda=["Sanae Takaichi, primera ministra desde octubre de 2025; ganó por amplio margen las elecciones anticipadas de febrero de 2026."],
 dinero="Mayor acreedor externo de EE.UU. en bonos del Tesoro.",
 crono=[("2025-10-21", "Takaichi, primera mujer en el cargo."), ("2026-02", "Victoria en elecciones anticipadas y reelección por el Parlamento.")],
 fuentes=[("Prime Minister of Japan (Wikipedia)", W + "Prime_Minister_of_Japan"),
          ("Asia Economy: Takaichi reelecta (2026-02-18)", "https://www.asiae.co.kr/en/article/2026021815312552109")]),

"huawei": dict(
 res=["Gigante chino de telecomunicaciones y chips: provee redes 5G a buena parte del Sur Global y desarrolla procesadores propios pese a las sanciones de EE.UU."],
 manda=["Ren Zhengfei, fundador; presidencia rotativa entre ejecutivos.", "Se declara propiedad de sus empleados a través de un sindicato."],
 dinero="Gasto en investigación entre los más altos del mundo.",
 crono=[("1987", "Fundación en Shenzhen."), ("2019-05", "Inclusión en la lista negra comercial de EE.UU."), ("2023-08", "Teléfono con chip avanzado de fabricación china.")],
 fuentes=[("Huawei (Wikipedia)", W + "Huawei")]),

"mossad": dict(
 res=["Servicio de inteligencia exterior y operaciones especiales de Israel, con historial de sabotajes y asesinatos selectivos, incluido el programa nuclear iraní."],
 manda=["Roman Gofman, director desde el 2 de junio de 2026, ex secretario militar de Netanyahu y sin carrera previa en inteligencia; su predecesor David Barnea se opuso a la designación."],
 dinero="Presupuesto reservado.",
 crono=[("1949-12", "Creación."), ("2024-09", "Ataque con buscapersonas a Hezbolá."), ("2026-06-02", "Gofman asume.")],
 fuentes=[("Mossad (Wikipedia)", W + "Mossad"),
          ("Washington Times: aprobación de Gofman (2026-04-13)", "https://m.washingtontimes.com/news/2026/apr/13/roman-gofman-israeli-army-general-approved-director-mossad/"),
          ("Al Majalla: perfil de Gofman", "https://en.majalla.com/node/331426/profiles/roman-gofman-israels-new-netanyahu-friendly-mossad-chief")]),

"trenaragua": dict(
 res=["Banda nacida en la cárcel de Tocorón que se expandió por Sudamérica y EE.UU. con extorsión, trata y narcotráfico; designada terrorista por EE.UU. en 2025.",
      "Su líder histórico murió en junio de 2026; según InSight Crime, la cohesión del grupo ya se venía debilitando."],
 manda=["Héctor Guerrero Flores, 'Niño Guerrero', murió el 12 de junio de 2026 en una operación conjunta de EE.UU. y Venezuela en el estado Bolívar; no hay sucesor claro."],
 dinero="Extorsión, explotación sexual, tráfico de migrantes y minería ilegal.",
 crono=[("2014", "Consolidación en Tocorón."), ("2023-09", "Toma de Tocorón por el gobierno venezolano."), ("2025-02", "Designación como organización terrorista."),
        ("2026-06-12", "Muerte de 'Niño Guerrero'.")],
 fuentes=[("Tren de Aragua (Wikipedia)", W + "Tren_de_Aragua"),
          ("InSight Crime: perfil de Niño Guerrero", "https://insightcrime.org/es/?p=233191"),
          ("NCTC: Tren de Aragua", "https://www.dni.gov/nctc/terrorist_groups/tren_de_aragua.html")]),

"gazprom": dict(
 res=["Gigante gasífero estatal ruso; perdió casi todo el mercado europeo desde 2022 y busca reorientarse hacia China."],
 manda=["Alekséi Miller, director ejecutivo; el Estado ruso es accionista mayoritario."],
 dinero="Registró pérdidas tras el corte de exportaciones a Europa.",
 crono=[("1989-08", "Creación a partir del ministerio soviético del gas."), ("2019-12", "Inicio del gasoducto Fuerza de Siberia."), ("2022-09", "Sabotaje de los Nord Stream.")],
 fuentes=[("Gazprom (Wikipedia)", W + "Gazprom")]),

"x": dict(
 res=["Red social de Elon Musk, integrada a SpaceX junto con xAI en febrero de 2026; plataforma central del debate político en EE.UU."],
 manda=["Elon Musk."],
 dinero="Publicidad y suscripciones; su valor se integró al grupo SpaceX.",
 crono=[("2006-03", "Lanzamiento de Twitter."), ("2022-10", "Compra por Musk."), ("2025-03", "Fusión con xAI."), ("2026-02", "Integración a SpaceX.")],
 fuentes=[("X Corp. (Wikipedia)", W + "X_Corp."), ("Twitter (Wikipedia)", W + "Twitter")]),

"far_sudan": dict(
 res=["Fuerzas de Apoyo Rápido, surgidas de las milicias Janjaweed de Darfur, en guerra con el ejército sudanés desde 2023.",
      "Tras tomar El Fasher en octubre de 2025 controlan casi todo Darfur y encabezan un gobierno paralelo que la Unión Africana no reconoce."],
 manda=["Mohamed Hamdan Dagalo, 'Hemedti', comandante y presidente del consejo presidencial del gobierno paralelo."],
 dinero="Oro de Darfur y apoyo externo atribuido por investigaciones de la ONU a Emiratos Árabes Unidos, que lo niega.",
 crono=[("2013", "Creación formal."), ("2023-04-15", "Comienzo de la guerra con el ejército."), ("2025-07", "Anuncio del gobierno paralelo."), ("2025-10", "Caída de El Fasher.")],
 fuentes=[("Rapid Support Forces (Wikipedia)", W + "Rapid_Support_Forces"),
          ("Al Arabiya: Hemedti jura como jefe del gobierno paralelo", "https://english.alarabiya.net/News/middle-east/2025/08/30/rsf-s-hemedti-sworn-in-as-head-of-parallel-sudanese-government")]),

"vanguard": dict(
 res=["Segunda gestora de activos del mundo; por sus fondos indexados es accionista de casi todas las grandes empresas de EE.UU."],
 manda=["Salim Ramji, director ejecutivo; los fondos son dueños de la empresa."],
 dinero="Alrededor de 10 billones de dólares administrados.",
 crono=[("1975-05", "Fundación por John Bogle."), ("1976", "Primer fondo indexado para el público.")],
 fuentes=[("The Vanguard Group (Wikipedia)", W + "The_Vanguard_Group")]),

"doj": dict(
 res=["Departamento de Justicia de EE.UU., del que depende el FBI: persecución penal federal y extradiciones; brazo jurídico de la ofensiva contra cárteles designados terroristas."],
 manda=["Todd Blanche, fiscal general tras el despido de Pam Bondi en 2026."],
 dinero="Decomisos de activos, incluidos los bitcoins del Prince Group.",
 crono=[("1870-06", "Creación."), ("1908-07", "Creación del FBI."), ("2026", "Blanche reemplaza a Bondi.")],
 fuentes=[("United States Department of Justice (Wikipedia)", W + "United_States_Department_of_Justice"),
          ("Political.org: quién es quién en el gobierno de Trump", "https://political.org/explained/trump-administration-whos-who/")]),

"hezbola": dict(
 res=["Partido y milicia chiita libanesa aliada de Irán; entró en la guerra el 2 de marzo de 2026 tras la muerte de Ali Jamenei, y Israel respondió con bombardeos y una invasión terrestre del sur del Líbano.",
      "Rechaza las negociaciones directas entre el Líbano e Israel iniciadas en abril bajo patrocinio de EE.UU."],
 manda=["Naim Qassem, secretario general desde octubre de 2024."],
 dinero="Financiamiento iraní, redes comerciales y servicios propios en el Líbano.",
 crono=[("1982", "Surgimiento durante la invasión israelí del Líbano."), ("2024-09", "Muerte de Hasán Nasralá."), ("2026-03-02", "Nueva guerra con Israel.")],
 fuentes=[("Hezbollah (Wikipedia)", W + "Hezbollah"),
          ("L'Orient-Le Jour: Qassem y las negociaciones (2026-06)", "https://today.lorientlejour.com/article/1538471/qassem-says-lebanon-israel-negotiations-must-be-limited-to-mutual-security.html")]),

"sunyeeon": dict(
 res=["Una de las tríadas más grandes de Hong Kong, con presencia en el juego, el préstamo usurario y el lavado en Asia y entre comunidades chinas del exterior."],
 manda=["Estructura de sociedad secreta con conducción no pública."],
 dinero="Juego ilegal, usura, extorsión y lavado.",
 crono=[("1919", "Origen en Hong Kong.")],
 fuentes=[("Sun Yee On (Wikipedia)", W + "Sun_Yee_On")]),

"boe": dict(
 res=["Banco central del Reino Unido y custodio de reservas de oro de decenas de países en su bóveda de Londres."],
 manda=["Andrew Bailey, gobernador."],
 dinero="Emisor de la libra esterlina.",
 crono=[("1694", "Fundación."), ("1997-05", "Independencia operativa.")],
 fuentes=[("Bank of England (Wikipedia)", W + "Bank_of_England")]),
})

# ---- Tanda 4 (posiciones 121 a 160) ----
FICHAS.update({
"cfr": dict(
 res=["El principal centro de pensamiento de política exterior de EE.UU.; edita Foreign Affairs y reúne a exfuncionarios, banqueros y periodistas."],
 manda=["Michael Froman, presidente; directorio de figuras del gobierno y las finanzas."],
 dinero="Financiado por cuotas de miembros corporativos y donaciones.",
 crono=[("1921", "Fundación en Nueva York."), ("1922-09", "Primer número de Foreign Affairs.")],
 fuentes=[("Council on Foreign Relations (Wikipedia)", W + "Council_on_Foreign_Relations")]),

"wef": dict(
 res=["Organiza la reunión anual de Davos, punto de encuentro de jefes de Estado, banqueros y directores ejecutivos.",
      "Atraviesa una transición tras la salida de su fundador Klaus Schwab en abril de 2025 y de su presidente Børge Brende a comienzos de 2026."],
 manda=["Larry Fink (BlackRock) y André Hoffmann (Roche), copresidentes interinos; el directorio corteja a Christine Lagarde para presidirlo."],
 dinero="Cuotas de unas mil empresas socias.",
 crono=[("1971", "Fundación por Klaus Schwab."), ("2025-04", "Renuncia de Schwab."), ("2025-08", "Fink y Hoffmann, copresidentes interinos.")],
 fuentes=[("World Economic Forum (Wikipedia)", W + "World_Economic_Forum"),
          ("ESG News: Fink y Hoffmann, copresidentes interinos", "https://esgnews.com/?p=37918"),
          ("Swissinfo / Bloomberg: el WEF corteja a Lagarde", "https://www.swissinfo.ch/eng/lagarde-is-still-being-pursued-by-the-wef-for-its-top-job/91923016")]),

"gchq": dict(
 res=["Agencia británica de inteligencia de señales y ciberseguridad, socia principal de la NSA en la alianza Cinco Ojos."],
 manda=["Anne Keast-Butler, directora, primera mujer en el cargo."],
 dinero="Presupuesto dentro de la cuenta única de inteligencia británica.",
 crono=[("1919", "Origen como escuela de códigos."), ("1946", "Acuerdo UKUSA con EE.UU."), ("2013-06", "Revelaciones de Snowden sobre el programa Tempora.")],
 fuentes=[("GCHQ (Wikipedia)", W + "GCHQ"), ("UKUSA Agreement (Wikipedia)", W + "UKUSA_Agreement")]),

"hanwha": dict(
 res=["Principal fabricante de armamento de Corea del Sur: obuses K9, motores de aviación y sistemas espaciales; gran proveedor del rearme de Polonia y otros países de la OTAN."],
 manda=["Grupo Hanwha, controlado por la familia Kim."],
 dinero="Exportaciones de defensa en fuerte crecimiento desde 2022.",
 crono=[("1952", "Fundación del grupo Hanwha."), ("2022-08", "Contratos marco con Polonia.")],
 fuentes=[("Hanwha Aerospace (Wikipedia)", W + "Hanwha_Aerospace"), ("K9 Thunder (Wikipedia)", W + "K9_Thunder")]),

"heritage": dict(
 res=["Centro de pensamiento conservador de EE.UU.; coordinó el Proyecto 2025, programa de gobierno y de personal para la segunda presidencia de Trump."],
 manda=["Kevin Roberts, presidente."],
 dinero="Donaciones privadas e institucionales.",
 crono=[("1973", "Fundación."), ("1981", "Mandate for Leadership para el gobierno de Reagan."), ("2023-04", "Lanzamiento del Proyecto 2025.")],
 fuentes=[("Heritage Foundation (Wikipedia)", W + "Heritage_Foundation"), ("Project 2025 (Wikipedia)", W + "Project_2025")]),

"mss": dict(
 res=["Ministerio de Seguridad del Estado: inteligencia exterior y contrainteligencia de China, señalado por gobiernos occidentales por espionaje industrial y operaciones cibernéticas."],
 manda=["Chen Yixin, ministro."],
 dinero="Presupuesto reservado.",
 crono=[("1983-07", "Creación."), ("2023-08", "Comienza a publicar en redes sociales.")],
 fuentes=[("Ministry of State Security (China) (Wikipedia)", W + "Ministry_of_State_Security_(China)")]),

"osf": dict(
 res=["Red filantrópica de George Soros que financia organizaciones de derechos humanos, justicia y medios en más de cien países; blanco frecuente de gobiernos nacionalistas."],
 manda=["Alexander Soros, presidente del directorio."],
 dinero="Dotación de varios miles de millones de dólares.",
 crono=[("1984", "Primera fundación en Hungría."), ("2018", "Traslado de su oficina de Budapest a Berlín."), ("2023-06", "Alexander Soros asume la conducción.")],
 fuentes=[("Open Society Foundations (Wikipedia)", W + "Open_Society_Foundations")]),

"pboc": dict(
 res=["Banco central de China: maneja el yuan, las mayores reservas internacionales del mundo y el sistema de pagos interbancarios CIPS."],
 manda=["Pan Gongsheng, gobernador; subordinado al Consejo de Estado y al Partido."],
 dinero="Reservas internacionales superiores a 3 billones de dólares.",
 crono=[("1948-12", "Fundación."), ("2015-10", "Lanzamiento del sistema CIPS."), ("2023-07", "Pan Gongsheng, gobernador.")],
 fuentes=[("People's Bank of China (Wikipedia)", W + "People%27s_Bank_of_China")]),

"cas": dict(
 res=["Mayor organismo de investigación científica del mundo por número de investigadores; pilar del desarrollo tecnológico y militar chino."],
 manda=["Depende del Consejo de Estado."],
 dinero="Presupuesto estatal y empresas derivadas, como en su origen Lenovo.",
 crono=[("1949-11", "Fundación.")],
 fuentes=[("Chinese Academy of Sciences (Wikipedia)", W + "Chinese_Academy_of_Sciences")]),

"norinco": dict(
 res=["Conglomerado estatal de armamento terrestre de China: blindados, artillería, munición y armas livianas exportadas a decenas de países."],
 manda=["Empresa estatal bajo la comisión de activos del Estado."],
 dinero="Sancionada por EE.UU. por ventas a Irán y otros países.",
 crono=[("1980", "Fundación.")],
 fuentes=[("Norinco (Wikipedia)", W + "Norinco")]),

"petrobras": dict(
 res=["Petrolera de control estatal de Brasil, líder mundial en extracción en aguas profundas (presal)."],
 manda=["Magda Chambriard, presidenta; el gobierno federal tiene la mayoría de los votos."],
 dinero="Una de las mayores pagadoras de dividendos de América Latina.",
 crono=[("1953-10", "Fundación."), ("2006", "Descubrimiento del presal."), ("2014-03", "Operación Lava Jato.")],
 fuentes=[("Petrobras (Wikipedia)", W + "Petrobras"), ("Operation Car Wash (Wikipedia)", W + "Operation_Car_Wash")]),

"rosneft": dict(
 res=["La mayor petrolera de Rusia y fuente clave de ingresos del Kremlin; EE.UU. la sancionó junto con Lukoil en octubre de 2025."],
 manda=["Ígor Sechin, director ejecutivo, del círculo íntimo de Putin."],
 dinero="Exportaciones reorientadas hacia India y China.",
 crono=[("1993", "Creación."), ("2004", "Compra de los activos principales de Yukos."), ("2025-10", "Sanciones de EE.UU.")],
 fuentes=[("Rosneft (Wikipedia)", W + "Rosneft")]),

"sinopec": dict(
 res=["Refinadora y petroquímica estatal de China, una de las mayores empresas del mundo por ingresos."],
 manda=["Empresa estatal bajo la comisión de activos del Estado."],
 dinero="Ingresos superiores a 400.000 millones de dólares.",
 crono=[("2000", "Salida a bolsa en Hong Kong, Nueva York y Londres.")],
 fuentes=[("Sinopec (Wikipedia)", W + "Sinopec")]),

"yamaguchi": dict(
 res=["El mayor sindicato yakuza de Japón, en declive por la presión legal; en 2025 dio por terminada su guerra interna con el Kobe Yamaguchi-gumi."],
 manda=["Kenichi Shinoda (Tsukasa Shinobu), jefe."],
 dinero="Extorsión, construcción, juego y préstamos.",
 crono=[("1915", "Fundación en Kobe."), ("2015-08", "Escisión del Kobe Yamaguchi-gumi."), ("2025-04", "Fin declarado del conflicto interno.")],
 fuentes=[("Yamaguchi-gumi (Wikipedia)", W + "Yamaguchi-gumi")]),

"boj": dict(
 res=["Banco central de Japón y mayor tenedor de bonos de su propio gobierno; sus decisiones mueven el flujo mundial de capitales (carry trade del yen)."],
 manda=["Kazuo Ueda, gobernador."],
 dinero="Dueño de alrededor de la mitad de la deuda pública japonesa.",
 crono=[("1882-10", "Fundación."), ("2024-03", "Fin de las tasas negativas.")],
 fuentes=[("Bank of Japan (Wikipedia)", W + "Bank_of_Japan")]),

"brookings": dict(
 res=["Centro de pensamiento de Washington, referencia del establishment demócrata en economía y política exterior."],
 manda=["Cecilia Rouse, presidenta."],
 dinero="Dotación y donaciones de fundaciones, empresas y gobiernos.",
 crono=[("1916", "Fundación como Institute for Government Research.")],
 fuentes=[("Brookings Institution (Wikipedia)", W + "Brookings_Institution")]),

"icann": dict(
 res=["Administra el sistema de nombres de dominio y la asignación de direcciones de Internet; desde 2016 sin supervisión del gobierno de EE.UU."],
 manda=["Kurt Lindqvist, director ejecutivo; modelo de múltiples partes interesadas."],
 dinero="Ingresos por tasas de registro de dominios.",
 crono=[("1998-09", "Fundación."), ("2016-10", "Fin del contrato con el Departamento de Comercio.")],
 fuentes=[("ICANN (Wikipedia)", W + "ICANN")]),

"iso": dict(
 res=["Fija normas técnicas que rigen la producción, la calidad y la seguridad en casi toda la economía mundial (ISO 9001, ISO 27001 y otras)."],
 manda=["Federación de organismos nacionales de normalización de 170 países."],
 dinero="Venta de normas y cuotas de sus miembros.",
 crono=[("1947-02", "Fundación en Ginebra."), ("1987", "Primera ISO 9000.")],
 fuentes=[("International Organization for Standardization (Wikipedia)", W + "International_Organization_for_Standardization")]),

"mi6": dict(
 res=["Servicio de inteligencia exterior británico, socio estrecho de la CIA y actor central en el apoyo occidental a Ucrania."],
 manda=["Blaise Metreweli, jefa ('C') desde octubre de 2025, primera mujer en el cargo."],
 dinero="Presupuesto dentro de la cuenta única de inteligencia.",
 crono=[("1909", "Creación del Secret Service Bureau."), ("1994", "Ley de servicios de inteligencia."), ("2025-10", "Metreweli asume.")],
 fuentes=[("Secret Intelligence Service (Wikipedia)", W + "Secret_Intelligence_Service")]),

"dem": dict(
 res=["Uno de los dos partidos que se alternan en el gobierno de EE.UU.; oposición al gobierno de Trump.",
      "En las elecciones legislativas del 3 de noviembre de 2026, el conteo de AP al 16 de noviembre le asignaba 256 bancas en la Cámara de Representantes y 55 en el Senado (incluidos 2 independientes que votan con el bloque); quedaban bancas sin adjudicar en el conteo."],
 manda=["Conducción repartida entre el Comité Nacional Demócrata, presidido por Ken Martin, y los jefes de bloque en el Congreso."],
 dinero="Recaudación de pequeños donantes vía ActBlue y grandes comités de acción política.",
 crono=[("1828", "Fundación."), ("2024-11", "Derrota presidencial."), ("2026-11-03", "Elecciones legislativas de medio término.")],
 fuentes=[("Democratic Party (United States) (Wikipedia)", W + "Democratic_Party_(United_States)"),
          ("2026 United States elections (Wikipedia)", W + "2026_United_States_elections")]),

"gop": dict(
 res=["Partido de gobierno de EE.UU. desde 2025, transformado por el movimiento de Donald Trump.",
      "En las elecciones legislativas del 3 de noviembre de 2026, el conteo de AP al 16 de noviembre le asignaba 169 bancas en la Cámara de Representantes y 44 en el Senado; quedaban bancas sin adjudicar en el conteo."],
 manda=["Donald Trump es el líder de hecho; Joe Gruters preside el Comité Nacional Republicano."],
 dinero="Grandes donantes, comités de acción política y la estructura de campaña de Trump.",
 crono=[("1854", "Fundación."), ("2024-11", "Victoria de Trump."), ("2026-11-03", "Elecciones legislativas de medio término.")],
 fuentes=[("Republican Party (United States) (Wikipedia)", W + "Republican_Party_(United_States)"),
          ("2026 United States elections (Wikipedia)", W + "2026_United_States_elections")]),

"statestreet": dict(
 res=["Uno de los mayores custodios de valores del mundo y tercer gestor de fondos indexados detrás de BlackRock y Vanguard."],
 manda=["Ron O'Hanley, presidente y director ejecutivo."],
 dinero="Custodia decenas de billones de dólares en activos.",
 crono=[("1792", "Origen en Boston."), ("1993", "Lanzamiento del primer fondo cotizado de EE.UU. (SPY).")],
 fuentes=[("State Street Corporation (Wikipedia)", W + "State_Street_Corporation")]),

"asml": dict(
 res=["Única fabricante en el mundo de las máquinas de litografía ultravioleta extrema para los chips más avanzados; sus exportaciones a China están restringidas por presión de EE.UU."],
 manda=["Christophe Fouquet, director ejecutivo."],
 dinero="Cada máquina EUV cuesta varios cientos de millones de euros.",
 crono=[("1984", "Fundación como empresa conjunta de Philips y ASM."), ("2019", "Primeras restricciones a ventas EUV a China.")],
 fuentes=[("ASML Holding (Wikipedia)", W + "ASML_Holding")]),

"bm": dict(
 res=["Principal banco multilateral de desarrollo; su presidente lo designa por tradición EE.UU."],
 manda=["Ajay Banga, presidente."],
 dinero="Préstamos y donaciones por decenas de miles de millones de dólares al año.",
 crono=[("1944-07", "Conferencia de Bretton Woods."), ("2023-06", "Banga asume.")],
 fuentes=[("World Bank (Wikipedia)", W + "World_Bank")]),

"icbc": dict(
 res=["El mayor banco del mundo por activos, de control estatal chino; financia infraestructura y empresas chinas en el exterior."],
 manda=["Directorio designado por el Estado y el Partido."],
 dinero="Activos superiores a 6 billones de dólares.",
 crono=[("1984-01", "Fundación."), ("2006-10", "Salida a bolsa, entonces la mayor de la historia.")],
 fuentes=[("Industrial and Commercial Bank of China (Wikipedia)", W + "Industrial_and_Commercial_Bank_of_China")]),

"rostec": dict(
 res=["Conglomerado estatal ruso que agrupa la mayor parte de la industria de defensa: aviones, helicópteros, blindados y electrónica."],
 manda=["Serguéi Chémezov, director general, antiguo colega de Putin en el KGB."],
 dinero="Producción militar en máximos por la guerra de Ucrania.",
 crono=[("2007-11", "Creación.")],
 fuentes=[("Rostec (Wikipedia)", W + "Rostec")]),

"tsinghua": dict(
 res=["Universidad de élite de Pekín, formadora de buena parte de la dirigencia del Partido, incluido Xi Jinping, y de la industria tecnológica china."],
 manda=["Secretario del Partido y presidente de la universidad."],
 dinero="Financiamiento estatal y empresas derivadas.",
 crono=[("1911", "Fundación.")],
 fuentes=[("Tsinghua University (Wikipedia)", W + "Tsinghua_University")]),

"aipac": dict(
 res=["El principal grupo de presión proisraelí de EE.UU.; desde 2022 gasta directamente en primarias del Congreso a través de su comité de acción política."],
 manda=["Directorio de donantes; Elliot Brandt, director ejecutivo."],
 dinero="Decenas de millones de dólares en las campañas de 2024.",
 crono=[("1963", "Fundación."), ("2021-12", "Creación de su comité de acción política.")],
 fuentes=[("AIPAC (Wikipedia)", W + "American_Israel_Public_Affairs_Committee")]),

"cosco": dict(
 res=["Naviera estatal china, una de las cuatro mayores del mundo, con terminales en Grecia (Pireo), España, Perú (Chancay) y otros países.",
      "Beijing condicionó la venta de los puertos de CK Hutchison a BlackRock y MSC a que COSCO tuviera una participación; la operación seguía empantanada en 2026."],
 manda=["Empresa estatal bajo la comisión de activos del Estado."],
 dinero="EE.UU. la incluyó en 2021 en su lista de empresas militares chinas.",
 crono=[("2016-02", "Fusión de COSCO y China Shipping."), ("2016-08", "Control del puerto del Pireo."), ("2024-11", "Inauguración de Chancay.")],
 fuentes=[("COSCO Shipping (Wikipedia)", W + "COSCO_Shipping"),
          ("Bloomberg Law: el acuerdo de puertos de Hutchison sigue trabado (2026-03)", "https://news.bloomberglaw.com/international-trade/ck-hutchison-looks-to-trump-xi-summit-as-ports-deal-drags-on")]),

"scotus": dict(
 res=["Corte Suprema de EE.UU., con mayoría conservadora de 6 a 3.",
      "En 2026 anuló los aranceles de Trump basados en la ley de emergencias (IEEPA) y, en Trump contra Slaughter, amplió el poder del presidente para destituir a miembros de agencias independientes."],
 manda=["John Roberts, presidente de la Corte."],
 dinero="Sin poder de bolsa, pero define la validez de leyes y decretos.",
 crono=[("1789", "Creación."), ("2022-06", "Fallo Dobbs."), ("2026-02-20", "Anulación de los aranceles IEEPA."), ("2026-06-29", "Fallo Trump contra Slaughter.")],
 fuentes=[("Supreme Court of the United States (Wikipedia)", W + "Supreme_Court_of_the_United_States"),
          ("PolitiFact: la Corte anula los aranceles (2026-02-20)", "https://www.politifact.com/article/2026/feb/20/supreme-court-strikes-down-tariffs-Trump/")]),

"dpworld": dict(
 res=["Operadora portuaria y logística de Dubái con terminales en más de 70 países, incluido el puerto de Posorja en Ecuador y Callao en Perú."],
 manda=["Propiedad del emirato de Dubái a través de Dubai World."],
 dinero="Inversión en zonas francas y corredores logísticos en África y Asia.",
 crono=[("2005", "Fusión que crea DP World."), ("2006", "Polémica en EE.UU. por la compra de P&O.")],
 fuentes=[("DP World (Wikipedia)", W + "DP_World")]),

"fmi": dict(
 res=["Prestamista de última instancia para países en crisis; impone condiciones de política económica a cambio de su financiamiento (Argentina es su mayor deudor)."],
 manda=["Kristalina Georgieva, directora gerente; EE.UU. tiene poder de veto en decisiones clave."],
 dinero="Recursos prestables cercanos a 1 billón de dólares.",
 crono=[("1944-07", "Bretton Woods."), ("2018-06", "Mayor acuerdo de su historia con Argentina."), ("2026-09", "Isabel Schnabel designada consejera financiera.")],
 fuentes=[("International Monetary Fund (Wikipedia)", W + "International_Monetary_Fund")]),

"nbim": dict(
 res=["El mayor fondo soberano del mundo; posee alrededor del 1,5% de todas las acciones cotizadas del planeta."],
 manda=["Nicolai Tangen, director ejecutivo; responde al Banco de Noruega y al Parlamento."],
 dinero="Valor cercano a 2 billones de dólares, alimentado por la renta petrolera.",
 crono=[("1990", "Creación del fondo petrolero."), ("1998", "Creación de NBIM.")],
 fuentes=[("Government Pension Fund of Norway (Wikipedia)", W + "Government_Pension_Fund_of_Norway")]),

"globo": dict(
 res=["El mayor grupo de medios de América Latina: TV Globo, diarios, radio y streaming en Brasil."],
 manda=["Familia Marinho."],
 dinero="Domina la audiencia y la publicidad televisiva brasileña.",
 crono=[("1925", "Fundación del diario O Globo."), ("1965-04", "Lanzamiento de TV Globo.")],
 fuentes=[("Grupo Globo (Wikipedia)", W + "Grupo_Globo")]),

"pif": dict(
 res=["Fondo soberano saudí, motor del plan Visión 2030: NEOM, LIV Golf, participaciones en Uber, Nintendo y videojuegos."],
 manda=["Mohammed bin Salmán preside el fondo; Yasir Al-Rumayyan es gobernador."],
 dinero="Activos cercanos a 1 billón de dólares.",
 crono=[("1971", "Creación."), ("2015", "Pasa a depender de Mohammed bin Salmán."), ("2017-10", "Anuncio de NEOM.")],
 fuentes=[("Public Investment Fund (Wikipedia)", W + "Public_Investment_Fund")]),

"cac": dict(
 res=["Regulador y censor de Internet en China: controla contenidos, algoritmos, datos y la aprobación de modelos de inteligencia artificial."],
 manda=["Depende de la Comisión Central de Asuntos del Ciberespacio que preside Xi Jinping."],
 dinero="Organismo administrativo.",
 crono=[("2014", "Creación."), ("2021-07", "Investigación a Didi tras su salida a bolsa en Nueva York.")],
 fuentes=[("Cyberspace Administration of China (Wikipedia)", W + "Cyberspace_Administration_of_China")]),

"pmf": dict(
 res=["Coalición de milicias iraquíes, en su mayoría chiitas y varias alineadas con Irán, integrada formalmente al Estado tras la guerra contra el Estado Islámico."],
 manda=["Falih al-Fayyadh, presidente de la comisión; facciones como Kataib Hezbolá tienen mando propio."],
 dinero="Presupuesto estatal iraquí y negocios propios.",
 crono=[("2014-06", "Fatwa de Sistani y movilización contra el Estado Islámico."), ("2016-11", "Ley que las incorpora al Estado."), ("2020-01", "Muerte de Abu Mahdi al-Muhandis junto a Soleimani.")],
 fuentes=[("Popular Mobilization Forces (Wikipedia)", W + "Popular_Mobilization_Forces")]),

"chatham": dict(
 res=["Instituto de asuntos internacionales de Londres, creador de la 'regla de Chatham House' para conversaciones reservadas."],
 manda=["Bronwen Maddox, directora."],
 dinero="Socios corporativos, gobiernos y fundaciones.",
 crono=[("1920", "Fundación."), ("1927", "Formulación de la regla de Chatham House.")],
 fuentes=[("Chatham House (Wikipedia)", W + "Chatham_House")]),

"dgse": dict(
 res=["Servicio de inteligencia exterior de Francia, con capacidad de acción clandestina en África, Medio Oriente y Europa."],
 manda=["Nicolas Lerner, director general."],
 dinero="Presupuesto reservado.",
 crono=[("1982-04", "Creación."), ("1985-07", "Hundimiento del Rainbow Warrior.")],
 fuentes=[("DGSE (Wikipedia)", W + "Directorate-General_for_External_Security")]),

"cmport": dict(
 res=["Operadora portuaria estatal china con participaciones en terminales de decenas de países, del Sri Lanka (Hambantota) a Brasil (Paranaguá) y Yibuti."],
 manda=["Grupo China Merchants, empresa estatal."],
 dinero="Inversiones vinculadas a la Iniciativa de la Franja y la Ruta.",
 crono=[("1872", "Origen de China Merchants."), ("2017-07", "Concesión de 99 años en Hambantota.")],
 fuentes=[("China Merchants Port (Wikipedia)", W + "China_Merchants_Port"), ("Hambantota International Port (Wikipedia)", W + "Hambantota_International_Port")]),
})

# ---- Tanda 5 (posiciones 161 a 200) ----
FICHAS.update({
"ffaa_ucrania": dict(
 res=["Sostienen desde 2022 la defensa frente a la invasión rusa, con una de las industrias de drones militares más grandes y probadas del mundo."],
 manda=["Mijaílo Drapatyi, comandante en jefe desde el 21 de julio de 2026, tras el despido de Oleksandr Syrskyi en medio de protestas masivas."],
 dinero="Dependientes de la ayuda militar y financiera de Europa y EE.UU.",
 crono=[("2022-02-24", "Invasión rusa a gran escala."), ("2024-02", "Syrskyi reemplaza a Zaluzhnyi."), ("2024-08", "Incursión en Kursk."), ("2026-07-21", "Drapatyi, comandante en jefe.")],
 fuentes=[("Armed Forces of Ukraine (Wikipedia)", W + "Armed_Forces_of_Ukraine"),
          ("Euronews: Drapatyi reemplaza a Syrskyi (2026-07-21)", "https://www.euronews.com/2026/07/21/zelenskyy-replaces-oleksandr-syrskyi-with-mykhailo-drapatyi-as-ukraines-commander-in-chief")]),

"oms": dict(
 res=["Agencia sanitaria de la ONU: declara emergencias internacionales, fija normas sanitarias y coordina respuestas a pandemias; EE.UU. inició en 2025 su retiro del organismo."],
 manda=["Tedros Adhanom Ghebreyesus, director general; la Asamblea Mundial de la Salud reúne a los Estados."],
 dinero="Depende en gran parte de contribuciones voluntarias de Estados y fundaciones, como la Fundación Gates.",
 crono=[("1948-04-07", "Creación."), ("2020-03", "Declaración de pandemia de covid-19."), ("2025-01", "EE.UU. anuncia su retiro."), ("2025-05", "Aprobación del acuerdo sobre pandemias.")],
 fuentes=[("World Health Organization (Wikipedia)", W + "World_Health_Organization")]),

"stf": dict(
 res=["Corte suprema y constitucional de Brasil, con poder sobre plataformas digitales y causas penales contra altas autoridades.",
      "Condenó a Jair Bolsonaro a 27 años y 3 meses por la trama golpista; desde marzo de 2026 cumple prisión domiciliaria humanitaria."],
 manda=["Once ministros; Alexandre de Moraes es relator de las causas del golpe."],
 dinero="Sin poder económico propio; decide sobre regulación, impuestos y contratos públicos.",
 crono=[("1891", "Creación republicana."), ("2024-08", "Suspensión de X en Brasil."), ("2025-09", "Condena de Bolsonaro."), ("2025-11-25", "Inicio de la ejecución de la pena."), ("2026-03-24", "Prisión domiciliaria humanitaria.")],
 fuentes=[("Supreme Federal Court (Wikipedia)", W + "Supreme_Federal_Court"),
          ("STF: prisión domiciliaria de Bolsonaro (2026-03-24)", "https://noticias.stf.jus.br/postsnoticias/stf-concede-prisao-domiciliar-temporaria-ao-ex-presidente-jair-bolsonaro/")]),

"africacorps": dict(
 res=["Estructura bajo control del Ministerio de Defensa ruso que reemplazó al Grupo Wagner en el Sahel; protege a juntas militares en Malí, Burkina Faso y Níger a cambio de acceso a minería y bases."],
 manda=["Mando del Ministerio de Defensa y la inteligencia militar rusa (GRU)."],
 dinero="Concesiones mineras, sobre todo de oro, y pagos de los gobiernos protegidos.",
 crono=[("2023-08", "Muerte de Yevgueni Prigozhin."), ("2024", "Despliegue de Africa Corps."), ("2025-06", "Wagner anuncia su salida de Malí.")],
 fuentes=[("Africa Corps (Russia) (Wikipedia)", W + "Africa_Corps_(Russia)"), ("Wagner Group (Wikipedia)", W + "Wagner_Group")]),

"epc": dict(
 res=["Fuerzas armadas de Corea del Norte, dueñas de un arsenal nuclear y de misiles; enviaron tropas a combatir junto a Rusia en Kursk."],
 manda=["Kim Jong-un, comandante supremo."],
 dinero="Una de las mayores proporciones de gasto militar sobre el PBI del mundo.",
 crono=[("1948-02", "Creación."), ("2006-10", "Primera prueba nuclear."), ("2024-10", "Envío de tropas a Rusia.")],
 fuentes=[("Korean People's Army (Wikipedia)", W + "Korean_People%27s_Army")]),

"gru": dict(
 res=["Inteligencia militar rusa: sabotaje, ciberataques, operaciones de influencia y control de fuerzas expedicionarias como Africa Corps.",
      "Gobiernos occidentales le atribuyen el envenenamiento de Skripal y ataques informáticos como NotPetya."],
 manda=["Ígor Kostiukov, jefe desde 2018."],
 dinero="Presupuesto reservado dentro del Ministerio de Defensa.",
 crono=[("1918", "Origen soviético."), ("2018-03", "Caso Skripal en Salisbury."), ("2018-10", "Kostiukov asume.")],
 fuentes=[("GRU (Wikipedia)", W + "GRU_(Russian_Federation)")]),

"isi": dict(
 res=["Inteligencia de las Fuerzas Armadas de Pakistán, eje del poder del ejército sobre la política interna y la relación con Afganistán."],
 manda=["Teniente general Asim Malik, director general; responde al jefe del Ejército."],
 dinero="Presupuesto reservado.",
 crono=[("1948", "Creación."), ("1980s", "Canal del apoyo a los muyahidines en Afganistán."), ("2025-05", "Conflicto armado con India.")],
 fuentes=[("Inter-Services Intelligence (Wikipedia)", W + "Inter-Services_Intelligence")]),

"morena": dict(
 res=["Partido gobernante de México, con mayoría calificada en el Congreso desde 2024; impulsó la elección popular de jueces de 2025."],
 manda=["Claudia Sheinbaum, presidenta de la República; Andrés Manuel López Obrador, fundador, conserva influencia."],
 dinero="Financiamiento público de partidos.",
 crono=[("2014-07", "Registro como partido."), ("2018-07", "López Obrador gana la presidencia."), ("2024-10-01", "Sheinbaum asume."), ("2025-06", "Primera elección judicial.")],
 fuentes=[("Morena (political party) (Wikipedia)", W + "Morena_(political_party)")]),

"opusdei": dict(
 res=["Prelatura personal de la Iglesia católica con fuerte presencia en universidades, escuelas de negocios y élites de España y América Latina."],
 manda=["Fernando Ocáriz, prelado; en 2022 el papa Francisco redujo su autonomía institucional."],
 dinero="Red de fundaciones, universidades (como la de Navarra y la Austral) y escuelas de negocios (IESE).",
 crono=[("1928-10", "Fundación por Josemaría Escrivá."), ("1982-11", "Prelatura personal."), ("2022-07", "Motu proprio Ad charisma tuendum.")],
 fuentes=[("Opus Dei (Wikipedia)", W + "Opus_Dei")]),

"pt_br": dict(
 res=["Partido de Lula, que gobierna Brasil y ganó la reelección en octubre de 2026."],
 manda=["Luiz Inácio Lula da Silva, líder; Edinho Silva, presidente del partido."],
 dinero="Fondo electoral público y aportes de afiliados.",
 crono=[("1980-02", "Fundación."), ("2002-10", "Primera victoria de Lula."), ("2016-08", "Destitución de Dilma Rousseff."), ("2026-10-25", "Reelección de Lula.")],
 fuentes=[("Workers' Party (Brazil) (Wikipedia)", W + "Workers%27_Party_(Brazil)")]),

"rand": dict(
 res=["Centro de investigación financiado sobre todo por el Pentágono; diseñó buena parte de la doctrina estratégica nuclear de EE.UU."],
 manda=["Jason Matheny, presidente."],
 dinero="Contratos federales de investigación.",
 crono=[("1948-05", "Fundación a partir del Proyecto RAND de la Fuerza Aérea.")],
 fuentes=[("RAND Corporation (Wikipedia)", W + "RAND_Corporation")]),

"swift": dict(
 res=["Red de mensajería que usan más de 11.000 bancos para los pagos internacionales; la exclusión de SWIFT es una de las sanciones más duras (Irán, Rusia)."],
 manda=["Cooperativa de bancos con sede en Bélgica, bajo supervisión del Banco Nacional de Bélgica y bancos centrales del G10."],
 dinero="Ingresos por tarifas de mensajes.",
 crono=[("1973-05", "Fundación."), ("2012-03", "Desconexión de bancos iraníes."), ("2022-03", "Exclusión de bancos rusos.")],
 fuentes=[("SWIFT (Wikipedia)", W + "SWIFT")]),

"aljazeera": dict(
 res=["Cadena de noticias financiada por el Estado de Catar, la más influyente del mundo árabe y herramienta de la diplomacia catarí."],
 manda=["Red de medios del Estado catarí."],
 dinero="Financiamiento público de Catar.",
 crono=[("1996-11", "Lanzamiento."), ("2006-11", "Lanzamiento de Al Jazeera English."), ("2024-05", "Cierre de sus oficinas en Israel.")],
 fuentes=[("Al Jazeera (Wikipedia)", W + "Al_Jazeera")]),

"smic": dict(
 res=["Mayor fabricante de chips de China, pieza central de su autonomía tecnológica frente a las restricciones de EE.UU."],
 manda=["Empresa con fuerte participación de fondos estatales chinos."],
 dinero="Inversiones respaldadas por el Fondo Nacional de Circuitos Integrados.",
 crono=[("2000-04", "Fundación en Shanghái."), ("2020-12", "Inclusión en la lista negra comercial de EE.UU."), ("2023-08", "Chip de 7 nm para Huawei.")],
 fuentes=[("SMIC (Wikipedia)", W + "Semiconductor_Manufacturing_International_Corporation")]),

"xinhua": dict(
 res=["Agencia oficial de noticias de China, órgano del Consejo de Estado y del Partido, con oficinas en todo el mundo."],
 manda=["Dependiente del Departamento de Propaganda del Partido."],
 dinero="Presupuesto estatal.",
 crono=[("1931-11", "Fundación como Agencia Roja de Noticias.")],
 fuentes=[("Xinhua News Agency (Wikipedia)", W + "Xinhua_News_Agency")]),

"rothschild": dict(
 res=["Familia de banqueros europeos cuyo banco, Rothschild & Co, es uno de los principales asesores en fusiones y reestructuraciones de deuda soberana del mundo."],
 manda=["Alexandre de Rothschild, presidente ejecutivo de Rothschild & Co."],
 dinero="La familia retiró al banco de la bolsa en 2023 para controlarlo por completo.",
 crono=[("1760s", "Mayer Amschel Rothschild inicia el negocio en Fráncfort."), ("1815", "Financiamiento británico en las guerras napoleónicas."), ("1875", "Lionel de Rothschild presta al gobierno británico el dinero para comprar las acciones del canal de Suez."), ("2004", "Deja de fijarse en sus oficinas el precio del oro de Londres."), ("2008", "Emmanuel Macron entra como banquero en Rothschild & Cie, donde trabaja hasta 2012."), ("2023", "Retiro de la bolsa de París."), ("2024-08", "Como asesor de Ucrania, cierra la reestructuración de 20.500 millones de dólares de bonos.")],
 fuentes=[("Rothschild family (Wikipedia)", W + "Rothschild_family"), ("Rothschild & Co (Wikipedia)", W + "Rothschild_%26_Co"), ("How Ukraine clinched a wartime debt restructuring (Reuters, en The Star)", "https://www.thestar.com.my/news/world/2024/09/03/conflict-creditors-and-a-car-crash-how-ukraine-clinched-a-wartime-debt-restructuring")]),

"ugle": dict(
 res=["La gran logia más antigua del mundo y referencia de la masonería regular en los países anglosajones."],
 manda=["El duque de Kent, gran maestre desde 1967."],
 dinero="Cuotas de unos 175.000 miembros y fundaciones benéficas.",
 crono=[("1717-06", "Fundación de la Gran Logia de Londres."), ("1813", "Unión que da origen a la Gran Logia Unida.")],
 fuentes=[("United Grand Lodge of England (Wikipedia)", W + "United_Grand_Lodge_of_England")]),

"hamas": dict(
 res=["Movimiento islamista palestino que gobernó Gaza desde 2007; tras el alto el fuego de octubre de 2025 aceptó en julio de 2026 un acuerdo de desarme por fases supervisado por la Junta de Paz de Trump.",
      "Israel y EE.UU. condicionan la retirada israelí y la reconstrucción al desarme completo."],
 manda=["Conducción colectiva tras la muerte de Yahya Sinwar; Khalil al-Hayya encabeza la negociación."],
 dinero="Financiamiento externo de Irán y redes de donantes; Catar alojó a su liderazgo político.",
 crono=[("1987-12", "Fundación."), ("2007-06", "Toma de Gaza."), ("2023-10-07", "Ataque contra Israel."), ("2025-10", "Alto el fuego."), ("2026-07", "Acuerdo de desarme por fases.")],
 fuentes=[("Hamas (Wikipedia)", W + "Hamas"),
          ("Al Jazeera: acuerdo de desarme de Hamás (2026-07)", "https://www.aljazeera.com/news/2026/7/40/gaza-board-of-peace-announces-hamas-disarmament-agreement-what-we-know")]),

"hermandad": dict(
 res=["Movimiento islamista transnacional nacido en Egipto, con partidos y redes en decenas de países; proscripto en Egipto, Arabia Saudita y Emiratos.",
      "El 13 de enero de 2026 EE.UU. designó terroristas a sus ramas de Egipto, Jordania y el Líbano; la rama egipcia rechazó la designación."],
 manda=["Sin conducción central efectiva; ramas nacionales autónomas."],
 dinero="Redes de beneficencia, empresas y donantes; Catar y Turquía han dado refugio a dirigentes.",
 crono=[("1928", "Fundación por Hasan al-Banna."), ("2012-06", "Mohamed Morsi gana la presidencia de Egipto."), ("2013-07", "Golpe militar en Egipto."), ("2026-01-13", "Designaciones de EE.UU.")],
 fuentes=[("Muslim Brotherhood (Wikipedia)", W + "Muslim_Brotherhood"),
          ("The National: designación de tres ramas (2026-01-13)", "https://www.thenationalnews.com/news/us/2026/01/13/us-designates-3-branches-of-muslim-brotherhood-as-terrorist-organisations")]),

"euroclear": dict(
 res=["Depositario central de valores con sede en Bruselas; custodia la mayor parte de los activos del banco central ruso inmovilizados en Europa desde 2022."],
 manda=["Valérie Urbain, directora ejecutiva; accionistas bancarios e institucionales."],
 dinero="Las ganancias extraordinarias sobre los activos rusos inmovilizados financian ayuda a Ucrania.",
 crono=[("1968", "Fundación."), ("2022-02", "Inmovilización de activos rusos."), ("2024", "Primer uso de ganancias para Ucrania.")],
 fuentes=[("Euroclear (Wikipedia)", W + "Euroclear")]),

"patriarcado": dict(
 res=["La Iglesia ortodoxa más grande del mundo, estrechamente aliada al Kremlin; respaldó la guerra en Ucrania."],
 manda=["Patriarca Kiril de Moscú."],
 dinero="Propiedades, donaciones y apoyo estatal.",
 crono=[("1589", "Creación del patriarcado de Moscú."), ("2009-02", "Kiril, patriarca."), ("2018-10", "Ruptura con Constantinopla por Ucrania.")],
 fuentes=[("Russian Orthodox Church (Wikipedia)", W + "Russian_Orthodox_Church")]),

"alazhar": dict(
 res=["La institución de enseñanza islámica sunita más prestigiosa del mundo; sus dictámenes tienen peso en todo el mundo musulmán."],
 manda=["Gran imán Ahmed el-Tayeb."],
 dinero="Presupuesto del Estado egipcio y donaciones.",
 crono=[("970", "Fundación de la mezquita en El Cairo."), ("2019-02", "Documento sobre la fraternidad humana con el papa Francisco.")],
 fuentes=[("Al-Azhar University (Wikipedia)", W + "Al-Azhar_University")]),

"ufwd": dict(
 res=["Departamento del Partido Comunista Chino que coordina la influencia sobre élites no comunistas, la diáspora china, religiones, Hong Kong y Taiwán."],
 manda=["Shi Taifeng, jefe del departamento."],
 dinero="Presupuesto del Partido y redes de asociaciones afines.",
 crono=[("1942", "Creación."), ("2014", "Xi lo llama un 'arma mágica' del Partido.")],
 fuentes=[("United Front Work Department (Wikipedia)", W + "United_Front_Work_Department")]),

"tjue": dict(
 res=["Máxima corte de la Unión Europea: su jurisprudencia se impone sobre las leyes nacionales y define el poder de Bruselas sobre datos, competencia y comercio."],
 manda=["Koen Lenaerts, presidente."],
 dinero="Sin poder económico propio; sus fallos afectan multas de miles de millones a grandes empresas.",
 crono=[("1952", "Creación."), ("1964", "Fallo Costa contra ENEL sobre la primacía del derecho europeo."), ("2020-07", "Fallo Schrems II.")],
 fuentes=[("European Court of Justice (Wikipedia)", W + "European_Court_of_Justice")]),

"cic": dict(
 res=["Fondo soberano de China para inversiones en el exterior y en bancos estatales chinos a través de Central Huijin."],
 manda=["Depende del Consejo de Estado."],
 dinero="Activos superiores a 1 billón de dólares.",
 crono=[("2007-09", "Creación.")],
 fuentes=[("China Investment Corporation (Wikipedia)", W + "China_Investment_Corporation")]),

"csonu": dict(
 res=["Única instancia internacional que puede autorizar el uso de la fuerza y sanciones obligatorias; paralizado por los vetos de sus cinco miembros permanentes.",
      "En noviembre de 2025 aprobó la Resolución 2803 sobre Gaza, con abstención de Rusia y China; en 2026 conduce la selección del sucesor de António Guterres."],
 manda=["Cinco miembros permanentes con veto (EE.UU., China, Rusia, Francia y Reino Unido) y diez electivos."],
 dinero="Decide misiones de paz financiadas por los Estados miembros.",
 crono=[("1946-01", "Primera sesión."), ("2025-11", "Resolución 2803 sobre Gaza."), ("2026-07", "Comienzan los sondeos para elegir secretario general.")],
 fuentes=[("United Nations Security Council (Wikipedia)", W + "United_Nations_Security_Council"),
          ("CRS: designación del secretario general (2026-09)", "https://www.everycrsreport.com/reports/IF10454.html")]),

"bilderberg": dict(
 res=["Conferencia anual y reservada de unas 130 figuras de la política, las finanzas, la defensa y los medios de Europa y Norteamérica."],
 manda=["Comité directivo; la secretaría está en los Países Bajos."],
 dinero="Financiamiento de sus participantes y fundaciones.",
 crono=[("1954-05", "Primera reunión en el hotel Bilderberg, Países Bajos.")],
 fuentes=[("Bilderberg meeting (Wikipedia)", W + "Bilderberg_meeting")]),

"qia": dict(
 res=["Fondo soberano de Catar, con participaciones en bancos, inmobiliarias de Londres, Volkswagen, Barclays y clubes deportivos."],
 manda=["Depende de la familia gobernante Al Thani."],
 dinero="Activos superiores a 500.000 millones de dólares.",
 crono=[("2005", "Creación."), ("2008-10", "Inyección de capital en Barclays durante la crisis.")],
 fuentes=[("Qatar Investment Authority (Wikipedia)", W + "Qatar_Investment_Authority")]),

"lmm": dict(
 res=["Organización saudí de proyección religiosa, que financió durante décadas mezquitas y centros en todo el mundo y hoy promueve el discurso del 'islam moderado' oficial."],
 manda=["Mohammad al-Issa, secretario general."],
 dinero="Financiamiento del Estado saudí.",
 crono=[("1962", "Fundación en La Meca.")],
 fuentes=[("Muslim World League (Wikipedia)", W + "Muslim_World_League")]),

"taiwan": dict(
 res=["Gobierno de Taiwán, sede de la industria de chips más avanzada del mundo (TSMC) y principal foco de tensión militar entre EE.UU. y China."],
 manda=["Lai Ching-te, presidente desde mayo de 2024; el Parlamento lo controla la oposición."],
 dinero="Su industria de semiconductores es crítica para la economía mundial.",
 crono=[("1949", "Retirada del gobierno nacionalista a Taiwán."), ("1996-03", "Primera elección presidencial directa."), ("2024-05-20", "Lai asume.")],
 fuentes=[("President of the Republic of China (Wikipedia)", W + "President_of_the_Republic_of_China")]),

"rosgvardia": dict(
 res=["Guardia Nacional de Rusia, fuerza de seguridad interior subordinada directamente a Putin para el control de protestas y la protección del régimen."],
 manda=["Víktor Zólotov, director, exjefe de la guardia personal de Putin."],
 dinero="Presupuesto federal de seguridad.",
 crono=[("2016-04", "Creación."), ("2023-06", "Motín de Wagner.")],
 fuentes=[("National Guard of Russia (Wikipedia)", W + "National_Guard_of_Russia")]),

"brics": dict(
 res=["Bloque de economías emergentes ampliado desde 2024 a Irán, Egipto, Etiopía, Emiratos e Indonesia; su Nuevo Banco de Desarrollo busca financiar sin condicionamientos occidentales."],
 manda=["Cumbres anuales de jefes de Estado; Dilma Rousseff preside el Nuevo Banco de Desarrollo."],
 dinero="Capital autorizado del banco de 100.000 millones de dólares.",
 crono=[("2009-06", "Primera cumbre."), ("2015-07", "Inicio del Nuevo Banco de Desarrollo."), ("2024-01", "Primera ampliación.")],
 fuentes=[("BRICS (Wikipedia)", W + "BRICS"), ("New Development Bank (Wikipedia)", W + "New_Development_Bank")]),

"trilateral": dict(
 res=["Foro privado fundado por David Rockefeller que reúne a élites políticas y empresarias de Norteamérica, Europa y Asia-Pacífico."],
 manda=["Presidencias regionales y comité ejecutivo."],
 dinero="Cuotas de miembros y donaciones.",
 crono=[("1973-07", "Fundación.")],
 fuentes=[("Trilateral Commission (Wikipedia)", W + "Trilateral_Commission")]),

"mit_tr": dict(
 res=["Inteligencia de Turquía, con operaciones en Siria, Libia, Irak y Asia Central, y canal de mediación en conflictos regionales."],
 manda=["İbrahim Kalın, jefe desde 2023, depende de Erdoğan."],
 dinero="Presupuesto reservado.",
 crono=[("1965", "Creación."), ("2016-07", "Intento de golpe de Estado."), ("2023-06", "Kalın asume.")],
 fuentes=[("National Intelligence Organization (Turkey) (Wikipedia)", W + "National_Intelligence_Organization_(Turkey)")]),

"cips": dict(
 res=["Sistema de pagos internacionales en yuanes creado por China como alternativa a SWIFT, usado por bancos rusos tras su exclusión."],
 manda=["Operado bajo supervisión del Banco Popular de China."],
 dinero="Volumen de operaciones en fuerte crecimiento desde 2022.",
 crono=[("2015-10", "Lanzamiento.")],
 fuentes=[("Cross-Border Interbank Payment System (Wikipedia)", W + "Cross-Border_Interbank_Payment_System")]),

"opep": dict(
 res=["Cártel de productores de petróleo ampliado con Rusia y otros países; administra cuotas que mueven el precio mundial del crudo."],
 manda=["Arabia Saudita y Rusia son los ejes de las decisiones."],
 dinero="Sus miembros concentran cerca de la mitad de la producción mundial.",
 crono=[("1960-09", "Fundación en Bagdad."), ("1973-10", "Embargo petrolero."), ("2016-12", "Acuerdo OPEP+ con Rusia.")],
 fuentes=[("OPEC (Wikipedia)", W + "OPEC"), ("OPEC+ (Wikipedia)", W + "OPEC%2B")]),

"rt": dict(
 res=["Canal internacional del Estado ruso en varios idiomas, con fuerte audiencia en América Latina, África y Medio Oriente; prohibido en la Unión Europea desde 2022."],
 manda=["Margarita Simonián, directora."],
 dinero="Presupuesto estatal ruso.",
 crono=[("2005-12", "Lanzamiento como Russia Today."), ("2022-03", "Prohibición en la Unión Europea.")],
 fuentes=[("RT (TV network) (Wikipedia)", W + "RT_(TV_network)")]),

"omc": dict(
 res=["Organización que administra las reglas del comercio mundial; su órgano de apelación está paralizado desde 2019 por el bloqueo de EE.UU."],
 manda=["Ngozi Okonjo-Iweala, directora general."],
 dinero="Presupuesto de cuotas de sus miembros.",
 crono=[("1995-01", "Creación."), ("2001-12", "Ingreso de China."), ("2019-12", "Parálisis del órgano de apelación.")],
 fuentes=[("World Trade Organization (Wikipedia)", W + "World_Trade_Organization")]),

"ocs": dict(
 res=["Organización de seguridad y cooperación euroasiática liderada por China y Rusia, con India, Pakistán, Irán y países de Asia Central."],
 manda=["Consejo de jefes de Estado; secretaría en Pekín."],
 dinero="Presupuesto reducido; peso político de sus miembros.",
 crono=[("2001-06", "Fundación."), ("2017-06", "Ingreso de India y Pakistán."), ("2023-07", "Ingreso de Irán.")],
 fuentes=[("Shanghai Cooperation Organisation (Wikipedia)", W + "Shanghai_Cooperation_Organisation")]),

"cpi": dict(
 res=["Tribunal penal permanente contra genocidio, crímenes de guerra y de lesa humanidad; emitió órdenes de detención contra Putin y Netanyahu.",
      "EE.UU. sancionó a su fiscal, a jueces y en agosto de 2026 a su presidenta; los Estados parte destituyeron al fiscal Karim Khan el 24 de julio de 2026 por denuncias de conducta sexual indebida."],
 manda=["Jueza Tomoko Akane, presidenta; fiscales adjuntos a cargo de la fiscalía."],
 dinero="Cuotas de 125 Estados parte.",
 crono=[("2002-07", "Entrada en vigor del Estatuto de Roma."), ("2023-03", "Orden contra Putin."), ("2024-11", "Órdenes contra Netanyahu y Gallant."), ("2025-02", "Sanciones de EE.UU."), ("2026-07-24", "Destitución de Khan.")],
 fuentes=[("International Criminal Court (Wikipedia)", W + "International_Criminal_Court"),
          ("UN News: destitución de Khan (2026-07-24)", "https://www.globalsecurity.org/military/library/news/2026/07/mil-260724-unnews04.htm"),
          ("Irish Times: sanciones a la presidenta de la CPI (2026-08-18)", "https://www.irishtimes.com/world/americas/2026/08/18/us-sanctions-international-criminal-court-president-and-israel-prosecutor/")]),
})

# ---- Ampliación: 50 organizaciones nuevas ----
FICHAS.update({
"casarosada": dict(
 res=["Gobierno de Javier Milei, alineado con EE.UU. e Israel y sostenido por un programa de ajuste fiscal con apoyo del FMI y del Tesoro estadounidense."],
 manda=["Javier Milei, presidente desde diciembre de 2023; Karina Milei, secretaria general de la Presidencia."],
 dinero="Mayor deudor del FMI; canje de monedas de 20.000 millones de dólares con el Tesoro de EE.UU. en 2025.",
 crono=[("2023-12-10", "Milei asume."), ("2025-04", "Nuevo acuerdo con el FMI."), ("2025-10", "Victoria oficialista en las legislativas y canje con el Tesoro de EE.UU.")],
 fuentes=[("Presidency of Javier Milei (Wikipedia)", W + "Presidency_of_Javier_Milei")]),

"gob_colombia": dict(
 res=["Gobierno de Colombia, principal socio militar de EE.UU. en Sudamérica y país con el mayor conflicto armado interno de la región."],
 manda=["Abelardo de la Espriella, presidente desde el 7 de agosto de 2026; ganó la segunda vuelta del 21 de junio a Iván Cepeda por un margen estrecho."],
 dinero="Exportaciones de petróleo, carbón y café; la economía ilícita de la cocaína pesa en regiones enteras.",
 crono=[("2016-11", "Acuerdo de paz con las FARC."), ("2022-08-07", "Petro asume."), ("2026-06-21", "De la Espriella gana la segunda vuelta."), ("2026-08-07", "Asunción.")],
 fuentes=[("President of Colombia (Wikipedia)", W + "President_of_Colombia"),
          ("El País (Cali): De la Espriella, presidente electo", "https://www.elpais.com.co/colombia/abelardo-de-la-espriella-es-declarado-oficialmente-presidente-electo-de-colombia-2439.html")]),

"miraflores": dict(
 res=["Gobierno interino de Venezuela tras la captura de Nicolás Maduro por EE.UU. el 3 de enero de 2026; opera bajo tutela de Washington, que fija la hoja de ruta de la transición.",
      "No hay fecha de elecciones: EE.UU. espera que la presidencia se declare vacante en 2027 para convocarlas."],
 manda=["Delcy Rodríguez, presidenta encargada; Jorge Rodríguez y Diosdado Cabello conservan peso en el chavismo."],
 dinero="Renta petrolera de PDVSA, abierta a inversores extranjeros con la reforma de la ley de hidrocarburos.",
 crono=[("2026-01-03", "Captura de Maduro por fuerzas de EE.UU."), ("2026-02-11", "Declaración conjunta con el secretario de Energía de EE.UU."), ("2026-10", "EE.UU. presenta su hoja de ruta para la transición.")],
 fuentes=[("2026 United States intervention in Venezuela (Wikipedia)", W + "2026_United_States_intervention_in_Venezuela"),
          ("Emol: la hoja de ruta de EE.UU. para Venezuela (2026-10-27)", "https://www.emol.com/noticias/Internacional/2026/10/27/1215321/venezuela-transicion-eeuu-pasos-elecciones.html"),
          ("Teletica / DW: sin fecha de elecciones (2026-09-02)", "https://www.teletica.com/deutsche-welle/delcy-rodriguez-dice-que-habra-elecciones-cuando-venezuela-este-preparada_416563")]),

"pdvsa": dict(
 res=["Petrolera estatal venezolana, dueña de las mayores reservas probadas de crudo del mundo, con producción muy por debajo de su capacidad."],
 manda=["Depende del gobierno interino; su apertura al capital extranjero avanza bajo supervisión de EE.UU."],
 dinero="Exportaciones reorientadas hacia EE.UU. tras la caída de Maduro.",
 crono=[("1976-01", "Nacionalización del petróleo."), ("2003", "Despidos masivos tras el paro petrolero."), ("2019-01", "Sanciones de EE.UU."), ("2026", "Reforma de la ley de hidrocarburos.")],
 fuentes=[("PDVSA (Wikipedia)", W + "PDVSA"),
          ("Mezha: Delcy Rodríguez y las concesiones a EE.UU.", "https://mezha.net/eng/bukvy/6cfd033e_delcy_rodriguez_leads/")]),

"pcc_cuba": dict(
 res=["Partido único de Cuba, en su peor crisis desde 1959: sin petróleo venezolano y bajo un bloqueo petrolero de hecho de EE.UU. desde enero de 2026.",
      "En junio de 2026 aprobó reformas para abrir la economía al capital privado."],
 manda=["Miguel Díaz-Canel, primer secretario y presidente; Raúl Castro conserva influencia; el conglomerado militar GAESA controla buena parte de la economía."],
 dinero="Turismo, remesas y empresas militares; colapso energético por falta de combustible.",
 crono=[("1965-10", "Fundación del partido actual."), ("2021-04", "Díaz-Canel, primer secretario."), ("2026-01", "Corte del petróleo venezolano y presión de EE.UU."), ("2026-06", "Reformas económicas de apertura.")],
 fuentes=[("Communist Party of Cuba (Wikipedia)", W + "Communist_Party_of_Cuba"), ("2026 Cuban crisis (Wikipedia)", W + "2026_Cuban_crisis"),
          ("El Observador: reformas de apertura (2026-06-21)", "https://www.elobservador.com.uy/estados-unidos/america-latina/cuba-aprueba-reformas-urgentes-abrir-su-economia-al-capital-privado-medio-la-presion-estados-unidos-n6048160")]),

"gob_chile": dict(
 res=["Gobierno del mayor productor de cobre del mundo y segundo de litio, insumos centrales de la transición energética."],
 manda=["José Antonio Kast, presidente desde marzo de 2026."],
 dinero="Codelco y la minería privada aportan la mayor parte de las exportaciones.",
 crono=[("2025-12", "Kast gana la segunda vuelta."), ("2026-03-11", "Asunción.")],
 fuentes=[("President of Chile (Wikipedia)", W + "President_of_Chile")]),

"codelco": dict(
 res=["La mayor productora de cobre del mundo, de propiedad estatal chilena; socia del litio del salar de Atacama con SQM."],
 manda=["Directorio designado por el Estado chileno."],
 dinero="Transfiere al fisco chileno la totalidad de sus utilidades.",
 crono=[("1976", "Creación tras la nacionalización del cobre de 1971."), ("2024-05", "Acuerdo con SQM por el litio.")],
 fuentes=[("Codelco (Wikipedia)", W + "Codelco")]),

"gob_ecuador": dict(
 res=["Gobierno de Ecuador, convertido en uno de los principales puertos de salida de cocaína hacia Europa y EE.UU., en guerra declarada contra las bandas."],
 manda=["Daniel Noboa, presidente desde 2023, reelecto en 2025."],
 dinero="Economía dolarizada; exportaciones de petróleo, banano y camarón.",
 crono=[("2024-01", "Declaración de conflicto armado interno."), ("2025-04", "Reelección de Noboa."), ("2025-11", "Rechazo en referéndum a las bases militares extranjeras.")],
 fuentes=[("Daniel Noboa (Wikipedia)", W + "Daniel_Noboa"), ("Ecuadorian security crisis (Wikipedia)", W + "Ecuadorian_security_crisis")]),

"eln": dict(
 res=["La última guerrilla histórica de Colombia, con presencia a ambos lados de la frontera con Venezuela y control de economías ilegales."],
 manda=["Comando Central; Antonio García, primer comandante."],
 dinero="Narcotráfico, extorsión, secuestro y minería ilegal.",
 crono=[("1964", "Fundación."), ("2019-01", "Atentado contra la escuela de policía de Bogotá."), ("2025-01", "Ofensiva en el Catatumbo.")],
 fuentes=[("National Liberation Army (Colombia) (Wikipedia)", W + "National_Liberation_Army_(Colombia)")]),

"clan_golfo": dict(
 res=["Ejército Gaitanista de Colombia o Clan del Golfo: la mayor organización narcotraficante de Colombia, con control de rutas hacia el Caribe y Centroamérica."],
 manda=["Estructura de mando de origen paramilitar; su jefe histórico, 'Otoniel', fue extraditado a EE.UU. en 2022."],
 dinero="Cocaína, minería ilegal, tráfico de migrantes por el Darién y extorsión.",
 crono=[("2006", "Surgimiento tras la desmovilización paramilitar."), ("2021-10", "Captura de 'Otoniel'."), ("2022-05", "Extradición a EE.UU.")],
 fuentes=[("Clan del Golfo (Wikipedia)", W + "Clan_del_Golfo")]),

"los_lobos": dict(
 res=["La mayor banda de Ecuador, socia del CJNG mexicano en el tráfico de cocaína y la minería ilegal; EE.UU. la designó organización terrorista en 2025."],
 manda=["Conducción en parte desde las cárceles ecuatorianas."],
 dinero="Narcotráfico, minería ilegal de oro y extorsión.",
 crono=[("2024-06", "Sanciones del Tesoro de EE.UU. por sus vínculos con el CJNG."), ("2025-09", "Designación como organización terrorista por EE.UU.")],
 fuentes=[("Los Lobos (Ecuador) (Wikipedia)", W + "Los_Lobos_(Ecuador)")]),

"gob_nigeria": dict(
 res=["Gobierno del país más poblado de África y primer productor de petróleo del continente, con insurgencias yihadistas en el noreste y bandidaje en el noroeste."],
 manda=["Bola Tinubu, presidente desde 2023."],
 dinero="Renta petrolera; liberó el tipo de cambio y eliminó el subsidio a los combustibles en 2023.",
 crono=[("2023-05-29", "Tinubu asume."), ("2025-11", "Trump amenaza con intervenir por la violencia contra cristianos.")],
 fuentes=[("Bola Tinubu (Wikipedia)", W + "Bola_Tinubu")]),

"dangote": dict(
 res=["El mayor conglomerado industrial de África occidental: cemento, fertilizantes, azúcar y la mayor refinería de África, en Lagos."],
 manda=["Aliko Dangote, fundador y presidente."],
 dinero="Aliko Dangote es la persona más rica de África según las listas de fortunas.",
 crono=[("1981", "Fundación."), ("2024-01", "Inicio de operaciones de la refinería Dangote.")],
 fuentes=[("Dangote Group (Wikipedia)", W + "Dangote_Group"), ("Dangote Refinery (Wikipedia)", W + "Dangote_Refinery")]),

"gob_sudafrica": dict(
 res=["Gobierno de la economía más industrializada de África, miembro de los BRICS, enfrentado con Washington desde 2025."],
 manda=["Cyril Ramaphosa, presidente, al frente de un gobierno de unidad nacional entre el ANC y la Alianza Democrática desde 2024."],
 dinero="Minería de platino, oro y carbón; sistema financiero más desarrollado del continente.",
 crono=[("1994-04", "Fin del apartheid."), ("2024-06", "Gobierno de unidad nacional."), ("2025-11", "Cumbre del G20 en Johannesburgo sin participación de EE.UU.")],
 fuentes=[("Government of National Unity (South Africa) (Wikipedia)", W + "Government_of_National_Unity_(South_Africa)")]),

"gob_etiopia": dict(
 res=["Gobierno del segundo país más poblado de África, sede de la Unión Africana, con conflictos armados en Amhara y Oromía."],
 manda=["Abiy Ahmed, primer ministro desde 2018."],
 dinero="La Gran Represa del Renacimiento, inaugurada en 2025, la vuelve potencia hidroeléctrica regional.",
 crono=[("2018-04", "Abiy asume."), ("2020-11", "Guerra de Tigray."), ("2025-09", "Inauguración de la Gran Represa del Renacimiento.")],
 fuentes=[("Abiy Ahmed (Wikipedia)", W + "Abiy_Ahmed"), ("Grand Ethiopian Renaissance Dam (Wikipedia)", W + "Grand_Ethiopian_Renaissance_Dam")]),

"gob_kenia": dict(
 res=["Gobierno de la principal economía de África oriental y aliado de EE.UU.; encabezó la misión de seguridad multinacional en Haití."],
 manda=["William Ruto, presidente desde 2022."],
 dinero="Centro financiero y logístico regional (puerto de Mombasa).",
 crono=[("2022-09", "Ruto asume."), ("2024-06", "Protestas contra el aumento de impuestos; despliegue en Haití."), ("2024-06", "EE.UU. lo designa aliado principal no miembro de la OTAN.")],
 fuentes=[("William Ruto (Wikipedia)", W + "William_Ruto")]),

"gob_ruanda": dict(
 res=["Gobierno pequeño con gran proyección militar en la región de los Grandes Lagos; expertos de la ONU lo acusan de respaldar al M23 en el este del Congo."],
 manda=["Paul Kagame, presidente y figura dominante desde 1994."],
 dinero="Organiza la exportación de minerales de la región y recibe ayuda occidental; Ruanda niega lucrar con minerales congoleños.",
 crono=[("1994", "Genocidio y toma del poder por el FPR."), ("2025-12", "Acuerdo de paz con el Congo firmado en Washington.")],
 fuentes=[("Paul Kagame (Wikipedia)", W + "Paul_Kagame"), ("Arab News: acuerdo de Washington y alto el fuego", "https://www.arabnews.com/world/angola-proposes-new-dr-congo-ceasefire-2632820")]),

"m23": dict(
 res=["Rebelión que controla Goma, Bukavu y buena parte de Kivu Norte y Kivu Sur, en el este del Congo, rico en coltán y oro.",
      "Firmó con el gobierno congoleño un marco de paz en Doha en noviembre de 2025 y una hoja de ruta en agosto de 2026, pero los combates siguen."],
 manda=["Corneille Nangaa, coordinador de la Alianza Fleuve Congo (AFC); Sultani Makenga, jefe militar."],
 dinero="Impuestos sobre minas de coltán como Rubaya y el comercio regional.",
 crono=[("2012", "Primera rebelión del M23."), ("2025-01", "Toma de Goma."), ("2025-11", "Marco de paz de Doha."), ("2026-08", "Hoja de ruta para las negociaciones.")],
 fuentes=[("March 23 Movement (Wikipedia)", W + "March_23_Movement"),
          ("Anadolu: hoja de ruta Congo-M23 (2026-08-23)", "https://www.aa.com.tr/en/africa/dr-congo-m23-rebel-group-agree-on-roadmap-for-comprehensive-peace-talks/4034875")]),

"saf": dict(
 res=["Ejército sudanés, en guerra con las Fuerzas de Apoyo Rápido desde abril de 2023; controla el centro, el norte y el este del país, incluida Jartum desde 2025."],
 manda=["General Abdel Fattah al-Burhan, jefe del Consejo de Soberanía; Kamil Idris, primer ministro desde 2025."],
 dinero="Oro, puertos del mar Rojo y empresas militares; apoyo de Egipto, Turquía y otros.",
 crono=[("2019-04", "Caída de Omar al-Bashir."), ("2021-10", "Golpe militar."), ("2023-04-15", "Comienzo de la guerra con las FAR."), ("2025-03", "Recuperación de Jartum.")],
 fuentes=[("Sudanese Armed Forces (Wikipedia)", W + "Sudanese_Armed_Forces"), ("Sudanese civil war (2023–present) (Wikipedia)", W + "Sudanese_civil_war_(2023%E2%80%93present)")]),

"majzen": dict(
 res=["El poder real de Marruecos: la monarquía y su entorno controlan la política exterior, la seguridad, la religión y grandes empresas a través del holding Al Mada.",
      "Logró apoyo internacional creciente a su soberanía sobre el Sáhara Occidental."],
 manda=["Rey Mohammed VI."],
 dinero="Al Mada y el control estatal de OCP.",
 crono=[("1999-07", "Mohammed VI asume."), ("2011-07", "Reforma constitucional."), ("2020-12", "Reconocimiento de EE.UU. sobre el Sáhara y normalización con Israel.")],
 fuentes=[("Makhzen (Wikipedia)", W + "Makhzen"), ("Al Mada (Wikipedia)", W + "Al_Mada")]),

"ocp": dict(
 res=["Administra las mayores reservas de fosfato del mundo, insumo básico de los fertilizantes: una palanca sobre la alimentación mundial."],
 manda=["Empresa de control estatal marroquí; Mostafa Terrab, presidente y director ejecutivo."],
 dinero="Uno de los principales exportadores de fertilizantes fosfatados.",
 crono=[("1920", "Fundación de la Oficina Jerifiana de Fosfatos.")],
 fuentes=[("OCP Group (Wikipedia)", W + "OCP_Group")]),

"sonatrach": dict(
 res=["Petrolera y gasífera estatal de Argelia, la mayor empresa de África; principal proveedora de gas de Italia por gasoducto."],
 manda=["Empresa del Estado argelino."],
 dinero="Sostiene la mayor parte de los ingresos fiscales de Argelia.",
 crono=[("1963-12", "Fundación."), ("1971-02", "Nacionalización de los hidrocarburos.")],
 fuentes=[("Sonatrach (Wikipedia)", W + "Sonatrach")]),

"lna": dict(
 res=["Fuerza armada que controla el este y el sur de Libia, con sus campos petroleros; respaldada por Rusia, Emiratos y Egipto según paneles de la ONU."],
 manda=["Mariscal Khalifa Haftar; su hijo Saddam Haftar, subcomandante general desde 2025."],
 dinero="Control de la mayor parte de la producción petrolera libia y del contrabando.",
 crono=[("2014-05", "Operación Dignidad."), ("2019-04", "Ofensiva fallida sobre Trípoli."), ("2020-10", "Alto el fuego nacional.")],
 fuentes=[("Libyan National Army (Wikipedia)", W + "Libyan_National_Army"), ("Khalifa Haftar (Wikipedia)", W + "Khalifa_Haftar")]),

"alshabaab": dict(
 res=["Rama de Al Qaeda en Somalia: controla zonas rurales del centro y el sur, cobra impuestos y ataca Mogadiscio y países vecinos."],
 manda=["Ahmed Diriye (Abu Ubaidah), emir."],
 dinero="Impuestos y extorsión a comercios, transporte y puertos; ingresos estimados en cientos de millones de dólares anuales por la ONU.",
 crono=[("2006", "Surgimiento."), ("2012-02", "Adhesión a Al Qaeda."), ("2013-09", "Ataque al centro comercial Westgate en Nairobi.")],
 fuentes=[("al-Shabaab (militant group) (Wikipedia)", W + "Al-Shabaab_(militant_group)")]),

"aes": dict(
 res=["Confederación de las juntas militares de Malí, Burkina Faso y Níger, que expulsaron a Francia, salieron de la CEDEAO y se apoyan en Rusia."],
 manda=["Assimi Goïta (Malí), Ibrahim Traoré (Burkina Faso) y Abdourahamane Tiani (Níger)."],
 dinero="Oro y uranio; renegociación de contratos mineros con empresas occidentales.",
 crono=[("2023-09", "Pacto de defensa mutua."), ("2024-07", "Confederación."), ("2025-01", "Salida de la CEDEAO.")],
 fuentes=[("Alliance of Sahel States (Wikipedia)", W + "Alliance_of_Sahel_States")]),

"chigi": dict(
 res=["Gobierno de la tercera economía de la eurozona; Meloni actúa como puente entre Trump y la Unión Europea."],
 manda=["Giorgia Meloni, presidenta del Consejo de Ministros desde 2022."],
 dinero="Una de las mayores deudas públicas de Europa; grandes empresas estatales como ENI y Leonardo.",
 crono=[("2022-10-22", "Meloni asume.")],
 fuentes=[("Giorgia Meloni (Wikipedia)", W + "Giorgia_Meloni")]),

"moncloa": dict(
 res=["Gobierno de España, en funciones electorales: Pedro Sánchez disolvió las Cortes y convocó elecciones generales para el 29 de noviembre de 2026."],
 manda=["Pedro Sánchez, presidente del Gobierno desde 2018."],
 dinero="La gran economía de la UE que más creció en 2024 y 2025.",
 crono=[("2018-06", "Sánchez llega por moción de censura."), ("2023-11", "Reelección parlamentaria."), ("2026-10-05", "Convocatoria de elecciones anticipadas.")],
 fuentes=[("Pedro Sánchez (Wikipedia)", W + "Pedro_S%C3%A1nchez"),
          ("La Moncloa: convocatoria de elecciones (2026-10-05)", "https://www.lamoncloa.gob.es/presidente/actividades/Paginas/2026/051026-sanchez-convocatoria-elecciones.aspx")]),

"gob_polonia": dict(
 res=["Gobierno del país de la OTAN que más gasta en defensa en proporción a su PBI, frontera oriental de la alianza frente a Rusia y Bielorrusia."],
 manda=["Donald Tusk, primer ministro; Karol Nawrocki, presidente desde agosto de 2025, de la oposición conservadora."],
 dinero="Compras masivas de armamento a EE.UU. y Corea del Sur.",
 crono=[("2023-12", "Tusk asume."), ("2025-08", "Nawrocki asume la presidencia.")],
 fuentes=[("Donald Tusk (Wikipedia)", W + "Donald_Tusk")]),

"gob_hungria": dict(
 res=["Gobierno de Hungría tras el fin de los 16 años de Viktor Orbán: Péter Magyar ganó las elecciones del 12 de abril de 2026 con mayoría de dos tercios y prometió reconstruir los lazos con la UE y la OTAN."],
 manda=["Péter Magyar, primer ministro, del partido Tisza."],
 dinero="Recuperación de fondos europeos congelados en la era Orbán.",
 crono=[("2010-05", "Orbán vuelve al poder."), ("2026-04-12", "Victoria de Magyar y reconocimiento de la derrota por Orbán.")],
 fuentes=[("Péter Magyar (Wikipedia)", W + "P%C3%A9ter_Magyar"),
          ("CBS News: Orbán reconoce la derrota (2026-04-12)", "https://www.cbsnews.com/news/hungary-general-election-viktor-orban-peter-magyar-results/")]),

"shell": dict(
 res=["Una de las mayores petroleras privadas del mundo y la mayor comercializadora de gas natural licuado."],
 manda=["Wael Sawan, director ejecutivo."],
 dinero="Ganancias de decenas de miles de millones de dólares anuales.",
 crono=[("1907", "Fusión de Royal Dutch y Shell Transport."), ("2022-01", "Traslado de la sede a Londres."), ("2021-05", "Fallo judicial neerlandés que le ordenó reducir emisiones, revocado en 2024.")],
 fuentes=[("Shell plc (Wikipedia)", W + "Shell_plc")]),

"totalenergies": dict(
 res=["Petrolera y gasífera francesa con fuerte presencia en África, Medio Oriente y gas natural licuado."],
 manda=["Patrick Pouyanné, presidente y director ejecutivo."],
 dinero="Ganancias de decenas de miles de millones de dólares anuales.",
 crono=[("1924", "Fundación de la Compagnie française des pétroles."), ("2021-05", "Cambio de nombre a TotalEnergies.")],
 fuentes=[("TotalEnergies (Wikipedia)", W + "TotalEnergies")]),

"lvmh": dict(
 res=["El mayor grupo de lujo del mundo (Louis Vuitton, Dior, Moët, Tiffany); dueño también de medios franceses como Les Échos y Le Parisien."],
 manda=["Bernard Arnault, presidente y director ejecutivo; la familia Arnault controla el grupo."],
 dinero="Bernard Arnault figura entre las personas más ricas del mundo.",
 crono=[("1987", "Fusión de Louis Vuitton y Moët Hennessy."), ("2021-01", "Compra de Tiffany.")],
 fuentes=[("LVMH (Wikipedia)", W + "LVMH")]),

"rheinmetall": dict(
 res=["El mayor fabricante de armas de Alemania y uno de los mayores productores de munición de artillería de Europa, impulsado por la guerra de Ucrania."],
 manda=["Armin Papperger, director ejecutivo."],
 dinero="Cartera de pedidos récord por el rearme europeo.",
 crono=[("1889", "Fundación."), ("2022-02", "Comienza el auge por la invasión de Ucrania."), ("2024", "Fábrica de munición en Ucrania anunciada.")],
 fuentes=[("Rheinmetall (Wikipedia)", W + "Rheinmetall")]),

"gob_indonesia": dict(
 res=["Gobierno del cuarto país más poblado del mundo y mayor productor de níquel; miembro de los BRICS desde 2025 sin abandonar la cooperación con EE.UU."],
 manda=["Prabowo Subianto, presidente desde octubre de 2024."],
 dinero="Fondo soberano Danantara, creado en 2025; prohibición de exportar níquel sin procesar.",
 crono=[("2024-10-20", "Prabowo asume."), ("2025-01", "Ingreso a los BRICS."), ("2025-02", "Creación de Danantara.")],
 fuentes=[("Prabowo Subianto (Wikipedia)", W + "Prabowo_Subianto")]),

"pcv": dict(
 res=["Partido único de Vietnam, que combina control político con apertura económica y se volvió un destino clave de las fábricas que salen de China."],
 manda=["Tô Lâm, secretario general reelecto en enero de 2026 y presidente del Estado desde el 7 de abril de 2026, el líder vietnamita más poderoso en décadas."],
 dinero="Exportaciones manufactureras en fuerte crecimiento.",
 crono=[("1930-02", "Fundación."), ("1986-12", "Reformas Doi Moi."), ("2024-08", "Tô Lâm, secretario general."), ("2026-04-07", "Tô Lâm, también presidente del Estado.")],
 fuentes=[("Communist Party of Vietnam (Wikipedia)", W + "Communist_Party_of_Vietnam"),
          ("Vietnam Law Magazine: biografía de Tô Lâm", "https://vietnamlawmagazine.vn/brief-biography-of-party-general-secretary-and-state-president-to-lam-79148.html")]),

"gob_filipinas": dict(
 res=["Gobierno de Filipinas, aliado por tratado de EE.UU. y principal contraparte de China en las disputas del mar de China Meridional."],
 manda=["Ferdinand Marcos Jr., presidente desde 2022."],
 dinero="Remesas de trabajadores en el exterior y servicios.",
 crono=[("2016-07", "Fallo arbitral contra los reclamos chinos."), ("2022-06-30", "Marcos Jr. asume."), ("2025-03", "Entrega de Rodrigo Duterte a la Corte Penal Internacional.")],
 fuentes=[("Bongbong Marcos (Wikipedia)", W + "Bongbong_Marcos")]),

"ejercito_tai": dict(
 res=["Ejército tailandés, árbitro histórico de la política del país con doce golpes exitosos desde 1932; protagonizó el conflicto fronterizo con Camboya en 2025."],
 manda=["Comandante en jefe del Ejército, con estrecha relación con la Corona."],
 dinero="Empresas, tierras y frecuencias de radio y televisión a su cargo.",
 crono=[("2014-05", "Último golpe de Estado."), ("2025-07", "Combates fronterizos con Camboya."), ("2026-02", "Elecciones ganadas por el conservador Bhumjaithai de Anutin Charnvirakul.")],
 fuentes=[("Royal Thai Army (Wikipedia)", W + "Royal_Thai_Army"),
          ("Al Jazeera: elecciones de Tailandia (2026-02-09)", "https://www.aljazeera.com/news/2026/2/9/thailands-bhumjaithai-set-for-coalition-talks-after-surprise-election-win")]),

"tatmadaw": dict(
 res=["Fuerzas armadas de Myanmar, en el poder desde el golpe de 2021 y en guerra con milicias étnicas y de la resistencia que controlan buena parte del territorio."],
 manda=["General Min Aung Hlaing."],
 dinero="Conglomerados militares, jade, gas y apoyo de China y Rusia.",
 crono=[("2021-02-01", "Golpe de Estado."), ("2023-10", "Ofensiva rebelde Operación 1027."), ("2025-12", "Elecciones por etapas sin la oposición disuelta.")],
 fuentes=[("Tatmadaw (Wikipedia)", W + "Tatmadaw")]),

"gob_corea": dict(
 res=["Gobierno de una potencia tecnológica e industrial (chips, barcos, armas) bajo protección militar de EE.UU. frente a Corea del Norte."],
 manda=["Lee Jae-myung, presidente desde junio de 2025, tras la destitución de Yoon Suk-yeol."],
 dinero="Grandes grupos familiares (chaebol) como Samsung, Hyundai y SK.",
 crono=[("2024-12-03", "Ley marcial fallida de Yoon."), ("2025-04", "Destitución de Yoon."), ("2025-06-04", "Lee asume.")],
 fuentes=[("Lee Jae-myung (Wikipedia)", W + "Lee_Jae-myung")]),

"gob_australia": dict(
 res=["Gobierno de un continente rico en minerales y aliado clave de EE.UU. en el Indo-Pacífico (AUKUS, Cinco Ojos)."],
 manda=["Anthony Albanese, primer ministro, reelecto en mayo de 2025."],
 dinero="Exportaciones de hierro, carbón, gas y litio, en gran parte a China.",
 crono=[("2021-09", "Anuncio de AUKUS."), ("2022-05", "Albanese asume."), ("2025-05", "Reelección.")],
 fuentes=[("Anthony Albanese (Wikipedia)", W + "Anthony_Albanese"), ("AUKUS (Wikipedia)", W + "AUKUS")]),

"bhp": dict(
 res=["La mayor minera del mundo por valor de mercado: hierro, cobre y potasa."],
 manda=["Directorio y gerencia ejecutiva con sede en Melbourne."],
 dinero="Ganancias de miles de millones de dólares, dependientes de la demanda china de acero.",
 crono=[("1885", "Fundación como Broken Hill Proprietary."), ("2001", "Fusión con Billiton."), ("2015-11", "Colapso de la represa de Samarco, empresa conjunta con Vale, en Mariana, Brasil.")],
 fuentes=[("BHP (Wikipedia)", W + "BHP")]),

"reliance": dict(
 res=["El mayor conglomerado privado de la India: la mayor refinería del mundo en Jamnagar, telecomunicaciones (Jio) y comercio minorista."],
 manda=["Mukesh Ambani, presidente; la familia Ambani controla el grupo."],
 dinero="Mukesh Ambani es la persona más rica de Asia según las listas de fortunas.",
 crono=[("1966", "Fundación por Dhirubhai Ambani."), ("2016-09", "Lanzamiento de Jio."), ("2024-12", "Acuerdo de suministro de crudo con Rosneft.")],
 fuentes=[("Reliance Industries (Wikipedia)", W + "Reliance_Industries")]),

"adani": dict(
 res=["Conglomerado indio de puertos, aeropuertos, energía y carbón, con concesiones en India, Israel (Haifa), Australia y otros países."],
 manda=["Gautam Adani, presidente; acusado en Nueva York en 2024 de presuntos sobornos, cargos que el grupo niega."],
 dinero="Fuerte endeudamiento; informe de Hindenburg Research de 2023, rechazado por el grupo.",
 crono=[("1988", "Fundación."), ("2023-01", "Informe de Hindenburg."), ("2024-11", "Acusación en EE.UU.")],
 fuentes=[("Adani Group (Wikipedia)", W + "Adani_Group")]),

"kazatomprom": dict(
 res=["El mayor productor de uranio del mundo, de mayoría estatal kazaja; abastece a centrales nucleares de China, Europa y EE.UU."],
 manda=["El fondo soberano Samruk-Kazyna controla la mayoría."],
 dinero="Cerca de una quinta parte de la producción mundial de uranio.",
 crono=[("1997", "Creación."), ("2018-11", "Salida a bolsa en Londres y Astaná.")],
 fuentes=[("Kazatomprom (Wikipedia)", W + "Kazatomprom")]),

"temasek": dict(
 res=["Fondo de inversión estatal de Singapur, accionista de bancos, telecomunicaciones y aerolíneas en toda Asia."],
 manda=["Propiedad del Ministerio de Finanzas de Singapur."],
 dinero="Cartera de varios cientos de miles de millones de dólares.",
 crono=[("1974", "Creación.")],
 fuentes=[("Temasek Holdings (Wikipedia)", W + "Temasek_Holdings")]),

"petronas": dict(
 res=["Petrolera estatal de Malasia, gran exportadora de gas natural licuado y pilar del presupuesto malasio."],
 manda=["Empresa del Estado malasio, bajo autoridad del primer ministro."],
 dinero="Aporta una parte significativa de los ingresos fiscales.",
 crono=[("1974-08", "Fundación.")],
 fuentes=[("Petronas (Wikipedia)", W + "Petronas")]),

"gob_bangladesh": dict(
 res=["Gobierno del octavo país más poblado del mundo y segundo exportador de ropa, tras la caída de Sheikh Hasina en 2024."],
 manda=["Tarique Rahman, primer ministro desde el 17 de febrero de 2026, tras la victoria aplastante del BNP."],
 dinero="Industria textil y remesas.",
 crono=[("2024-08", "Caída de Hasina y gobierno interino de Yunus."), ("2026-02-12", "Elecciones."), ("2026-02-17", "Rahman asume.")],
 fuentes=[("Tarique Rahman (Wikipedia)", W + "Tarique_Rahman"),
          ("Dawn / AFP: Rahman jura (2026-02-17)", "https://www.dawn.com/news/1973874")]),

"gob_siria": dict(
 res=["Gobierno surgido de la caída de Bashar al-Assad en diciembre de 2024; en 2026 recuperó el noreste e integró a las Fuerzas Democráticas Sirias al ejército."],
 manda=["Ahmed al-Sharaa, presidente interino."],
 dinero="Reconstrucción con fondos del Golfo y Turquía tras el levantamiento de sanciones de EE.UU. en 2025.",
 crono=[("2024-12-08", "Caída de Assad."), ("2025-06", "Levantamiento de sanciones de EE.UU."), ("2026-01", "Ofensiva en el noreste y acuerdo con las FDS."), ("2026-08", "Disolución formal de las FDS.")],
 fuentes=[("Ahmed al-Sharaa (Wikipedia)", W + "Ahmed_al-Sharaa"),
          ("Al Jazeera: acuerdo con las FDS (2026-01-30)", "https://www.aljazeera.com/news/2026/1/30/kurdish-led-sdf-agrees-integration-with-syrian-government-forces")]),

"gob_irak": dict(
 res=["Gobierno de un gran productor de petróleo disputado entre Irán y EE.UU., con milicias armadas integradas formalmente al Estado."],
 manda=["Ali al-Zaidi, primer ministro desde el 14 de mayo de 2026, candidato de consenso tras el veto de EE.UU. a Nuri al-Maliki."],
 dinero="El petróleo aporta casi todo el presupuesto.",
 crono=[("2003-03", "Invasión de EE.UU."), ("2025-11", "Elecciones legislativas."), ("2026-05-14", "Al-Zaidi jura con un gabinete parcial.")],
 fuentes=[("Prime Minister of Iraq (Wikipedia)", W + "Prime_Minister_of_Iraq"),
          ("The National: al-Zaidi jura (2026-05-14)", "https://thenationalnews.com/news/mena/2026/05/14/iraqi-parliament-votes-on-thursday-in-key-step-towards-installing-government/")]),

"gob_canada": dict(
 res=["Gobierno del segundo país más extenso del mundo, gran exportador de petróleo, minerales y agua, enfrentado con Trump por aranceles y amenazas de anexión."],
 manda=["Mark Carney, primer ministro desde marzo de 2025, ganó las elecciones de abril de 2025."],
 dinero="Integración económica profunda con EE.UU.",
 crono=[("2025-03-14", "Carney asume."), ("2025-04-28", "Victoria electoral liberal.")],
 fuentes=[("Mark Carney (Wikipedia)", W + "Mark_Carney")]),
})

# ---- Revisión: actores con poder real en lugar de gobiernos formales ----
for _k in ("pm_israel downing turquia gob_indonesia planalto gob_australia gob_canada gob_corea gob_sudafrica eliseo gob_nigeria "
           "moncloa chigi gob_etiopia gob_chile gob_ruanda gob_bangladesh gob_colombia casarosada gob_irak gob_polonia ucrania "
           "kanzleramt kantei gob_kenia gob_filipinas gob_hungria gob_ecuador gob_siria miraflores taiwan").split():
    FICHAS.pop(_k, None)

FICHAS.update({
# Personas
"musk": dict(
 res=["El empresario más rico del mundo controla SpaceX, que absorbió a xAI y a X en febrero de 2026, y Tesla: cohetes, la red satelital Starlink, inteligencia artificial y una red social central en la política de EE.UU.",
      "Starlink le da poder sobre comunicaciones militares, como mostró la guerra de Ucrania."],
 manda=["Decide personalmente en sus empresas; conserva el control de voto de SpaceX."],
 dinero="SpaceX y xAI se fusionaron con una valuación de 1,25 billones de dólares.",
 crono=[("2002", "Funda SpaceX."), ("2022-10", "Compra Twitter."), ("2025-01", "Encabeza el DOGE en el gobierno de Trump."), ("2025-05", "Deja el gobierno."), ("2026-02", "SpaceX absorbe a xAI y X.")],
 fuentes=[("Elon Musk (Wikipedia)", W + "Elon_Musk"), ("Fortune: SpaceX compra xAI (2026-02-02)", "https://fortune.com/2026/02/02/elon-musk-spacex-xai-ipo-trillion")]),
"thiel": dict(
 res=["Inversor que cofundó PayPal y Palantir, financió a Facebook en sus inicios y articula la red tecnológica y política de la nueva derecha estadounidense, incluido J. D. Vance."],
 manda=["Opera a través de Founders Fund, Thiel Capital y su presidencia del directorio de Palantir."],
 dinero="Fortuna multimillonaria concentrada en tecnología y defensa.",
 crono=[("1998", "Cofunda PayPal."), ("2003", "Cofunda Palantir."), ("2022", "Financia la campaña al Senado de J. D. Vance.")],
 fuentes=[("Peter Thiel (Wikipedia)", W + "Peter_Thiel")]),
"ellison": dict(
 res=["Larry Ellison, cofundador de Oracle, y su hijo David, que con Paramount Skydance compró Warner Bros. Discovery en octubre de 2026 y controla CBS, CNN, HBO y los estudios Warner.",
      "Oracle es socio de seguridad de TikTok en EE.UU. y constructor de centros de datos para OpenAI."],
 manda=["Larry Ellison controla Oracle; David Ellison preside Skydance, con Ynon Kreiz como codirector ejecutivo."],
 dinero="Una de las mayores fortunas del mundo; la familia financió la compra de Warner con capital propio y de RedBird.",
 crono=[("1977", "Fundación de Oracle."), ("2025-08", "Skydance se fusiona con Paramount."), ("2026-01", "Oracle, socio de TikTok USDS."), ("2026-10-06", "Cierre de la compra de Warner Bros. Discovery.")],
 fuentes=[("Larry Ellison (Wikipedia)", W + "Larry_Ellison"), ("Axios: cierre de la compra de Warner (2026-10-06)", "https://www.axios.com/2026/10/06/paramount-warner-bros-discovery-deal-skydance")]),
"bezos": dict(
 res=["Fundador de Amazon, dueño de The Washington Post y de la empresa espacial Blue Origin, competidora de SpaceX en contratos de la NASA y el Pentágono."],
 manda=["Presidente ejecutivo de Amazon y mayor accionista individual; controla Blue Origin y el Post."],
 dinero="Una de las mayores fortunas del mundo.",
 crono=[("1994", "Funda Amazon."), ("2000", "Funda Blue Origin."), ("2013", "Compra The Washington Post."), ("2021-07", "Deja la dirección ejecutiva de Amazon.")],
 fuentes=[("Jeff Bezos (Wikipedia)", W + "Jeff_Bezos")]),
"zuckerberg": dict(
 res=["Controla Meta (Facebook, Instagram, WhatsApp), con más de 3.000 millones de usuarios: decide qué contenidos circulan para buena parte de la humanidad."],
 manda=["Controla la mayoría de los votos de Meta por sus acciones de clase B."],
 dinero="Una de las mayores fortunas del mundo.",
 crono=[("2004", "Funda Facebook."), ("2012", "Compra Instagram."), ("2014", "Compra WhatsApp."), ("2025-01", "Fin del programa de verificación de datos en EE.UU.")],
 fuentes=[("Mark Zuckerberg (Wikipedia)", W + "Mark_Zuckerberg")]),
"m_ambani": dict(
 res=["El hombre más rico de Asia controla Reliance: la mayor refinería del mundo, la mayor telefónica de la India (Jio) y medios."],
 manda=["Presidente de Reliance; sus hijos dirigen las principales divisiones."],
 dinero="Fortuna estimada en más de 100.000 millones de dólares.",
 crono=[("2002", "Asume Reliance tras la muerte de su padre."), ("2016", "Lanzamiento de Jio.")],
 fuentes=[("Mukesh Ambani (Wikipedia)", W + "Mukesh_Ambani")]),
"arnault": dict(
 res=["Controla LVMH, el mayor grupo de lujo del mundo, y medios franceses como Les Échos y Le Parisien."],
 manda=["Presidente y director ejecutivo de LVMH; sus hijos ocupan puestos clave."],
 dinero="Una de las mayores fortunas del mundo.",
 crono=[("1984", "Compra Boussac, dueña de Dior."), ("1989", "Toma el control de LVMH.")],
 fuentes=[("Bernard Arnault (Wikipedia)", W + "Bernard_Arnault")]),
"milei": dict(
 res=["Presidente de la Argentina desde 2023, alineado con Trump; su programa de ajuste se sostiene con el FMI y un canje de 20.000 millones de dólares del Tesoro de EE.UU."],
 manda=["Decide con un círculo reducido: su hermana Karina Milei, secretaria general de la Presidencia, y el ministro de Economía Luis Caputo."],
 dinero="El país es el mayor deudor del FMI.",
 crono=[("2023-12-10", "Asume."), ("2025-04", "Acuerdo con el FMI."), ("2025-10", "Victoria en las legislativas y canje con el Tesoro de EE.UU.")],
 fuentes=[("Javier Milei (Wikipedia)", W + "Javier_Milei")]),
"erdogan": dict(
 res=["Gobierna Turquía desde 2003 y concentra el poder en la presidencia; conduce el segundo ejército de la OTAN, la industria de drones y la influencia turca en Siria, Libia y el Cáucaso."],
 manda=["Presidente; controla el partido AKP, la inteligencia (MİT) y la justicia; su principal rival, Ekrem İmamoğlu, fue encarcelado en 2025."],
 dinero="Su yerno Selçuk Bayraktar es accionista de Baykar.",
 crono=[("2003-03", "Primer ministro."), ("2014-08", "Presidente."), ("2017-04", "Referéndum que crea el sistema presidencial."), ("2025-03", "Detención de İmamoğlu.")],
 fuentes=[("Recep Tayyip Erdoğan (Wikipedia)", W + "Recep_Tayyip_Erdo%C4%9Fan")]),
"netanyahu": dict(
 res=["Primer ministro de Israel en funciones, conduce la guerra contra Irán y controla los servicios de inteligencia y las fuerzas armadas.",
      "En las elecciones del 27 de octubre de 2026 su bloque no alcanzó mayoría propia."],
 manda=["Primer ministro; designó a su secretario militar Roman Gofman al frente del Mossad."],
 dinero="Es juzgado por corrupción desde 2020; niega los cargos.",
 crono=[("1996", "Primer mandato."), ("2022-12", "Vuelve al poder."), ("2023-10-07", "Ataque de Hamás."), ("2026-02-28", "Guerra con Irán."), ("2026-10-27", "Elecciones.")],
 fuentes=[("Benjamin Netanyahu (Wikipedia)", W + "Benjamin_Netanyahu")]),
"lula": dict(
 res=["Presidente de Brasil, reelecto el 25 de octubre de 2026; referente del Sur Global en los BRICS con política exterior autónoma."],
 manda=["Lidera el PT; gobierna con una coalición amplia que depende del centro político y de la bancada agropecuaria."],
 dinero="Petrobras y el BNDES son herramientas de su política económica.",
 crono=[("2003-01", "Primer mandato."), ("2018-04", "Prisión, luego anulada."), ("2023-01", "Tercer mandato."), ("2026-10-25", "Reelección.")],
 fuentes=[("Luiz Inácio Lula da Silva (Wikipedia)", W + "Luiz_In%C3%A1cio_Lula_da_Silva")]),
"prabowo": dict(
 res=["Presidente de Indonesia desde 2024; exgeneral que amplió el papel de los militares y creó el fondo soberano Danantara."],
 manda=["Presidente; controla el ejército, la policía y Danantara."],
 dinero="Danantara concentra las participaciones estatales en grandes empresas.",
 crono=[("2024-10-20", "Asume."), ("2025-01", "Ingreso de Indonesia a los BRICS."), ("2025-02", "Creación de Danantara.")],
 fuentes=[("Prabowo Subianto (Wikipedia)", W + "Prabowo_Subianto")]),
"zelenski": dict(
 res=["Presidente de Ucrania en guerra; concentra la conducción política y militar bajo ley marcial."],
 manda=["Kirilo Budánov, exjefe de la inteligencia militar, dirige la Oficina del Presidente desde el 2 de enero de 2026, tras la renuncia de Andrí Yermak."],
 dinero="Depende de la ayuda de Europa y EE.UU.",
 crono=[("2019-05", "Asume."), ("2022-02-24", "Invasión rusa."), ("2025-11", "Renuncia de Yermak."), ("2026-01-02", "Budánov, jefe de la Oficina del Presidente."), ("2026-07-21", "Drapatyi, nuevo comandante en jefe.")],
 fuentes=[("Volodymyr Zelenskyy (Wikipedia)", W + "Volodymyr_Zelenskyy"), ("Ukrinform: Budánov a la Oficina del Presidente", "https://www.ukrinform.net/rubric-polytics/4076184-budanov-officially-appointed-head-of-presidential-office-ivashchenko-takes-over-gur.html")]),
"sharaa": dict(
 res=["Presidente interino de Siria tras derrocar a Assad en diciembre de 2024; en 2026 recuperó el noreste e integró a las fuerzas kurdas al ejército."],
 manda=["Exlíder de Hayat Tahrir al-Sham, disuelta en el nuevo Estado; apoyado por Turquía, el Golfo y, desde 2025, EE.UU."],
 dinero="Reconstrucción con fondos del Golfo tras el levantamiento de sanciones.",
 crono=[("2024-12-08", "Caída de Assad."), ("2025-01", "Presidente interino."), ("2025-06", "Fin de las sanciones de EE.UU."), ("2026-08", "Disolución de las FDS.")],
 fuentes=[("Ahmed al-Sharaa (Wikipedia)", W + "Ahmed_al-Sharaa")]),
"delcy": dict(
 res=["Presidenta encargada de Venezuela desde la captura de Maduro por EE.UU. el 3 de enero de 2026; gobierna bajo tutela de Washington, que elogia su gestión y no fija fecha de elecciones."],
 manda=["Comparte el poder con su hermano Jorge Rodríguez y con Diosdado Cabello; en marzo de 2026 destituyó al ministro de Defensa Vladimir Padrino López."],
 dinero="Apertura petrolera a inversores extranjeros bajo supervisión de EE.UU.",
 crono=[("2018-06", "Vicepresidenta."), ("2026-01-03", "Asume como presidenta encargada."), ("2026-03", "Destitución de Padrino López."), ("2026-10", "Hoja de ruta de EE.UU. para la transición.")],
 fuentes=[("Delcy Rodríguez (Wikipedia)", W + "Delcy_Rodr%C3%ADguez"), ("El Español: destitución de Padrino (2026-03-19)", "https://www.elespanol.com/mundo/america/20260319/delcy-rodriguez-protege-restos-madurismo-purga-vladimir-padrino-apunta-diosdado/1003744175399_0.html")]),
"kagame": dict(
 res=["Gobierna Ruanda desde 1994 y proyecta su poder militar en los Grandes Lagos; expertos de la ONU acusan a Ruanda de respaldar al M23, lo que Kigali niega."],
 manda=["Presidente; controla el Frente Patriótico Ruandés y su holding Crystal Ventures."],
 dinero="Ayuda occidental y comercio regional de minerales.",
 crono=[("1994-07", "El FPR toma el poder."), ("2000-04", "Presidente."), ("2025-12", "Acuerdo de paz con el Congo en Washington.")],
 fuentes=[("Paul Kagame (Wikipedia)", W + "Paul_Kagame")]),
# Sindicatos
"cgt_arg": dict(
 res=["Principal central obrera de la Argentina, eje de la oposición a la reforma laboral de Milei, con capacidad de paralizar el transporte y la industria."],
 manda=["Triunvirato de Jorge Sola (Seguro), Cristian Jerónimo (Vidrio) y Octavio Argüello (Camioneros), electo en noviembre de 2025 hasta 2029."],
 dinero="Los sindicatos administran obras sociales de salud con fondos obligatorios.",
 crono=[("1930", "Fundación."), ("2025-11-05", "Elección del triunvirato."), ("2026", "Plan de lucha contra la reforma laboral.")],
 fuentes=[("CGT (Argentina) (Wikipedia)", W + "General_Confederation_of_Labour_(Argentina)"), ("La Capital: nuevo triunvirato", "https://www.lacapital.com.ar/politica/la-cgt-eligio-nueva-conduccion-y-se-pone-alerta-la-reforma-laboral-milei-n10228233.html")]),
"cosatu": dict(
 res=["La mayor central sindical de Sudáfrica, aliada histórica del ANC dentro de la alianza tripartita."],
 manda=["Comité ejecutivo central."],
 dinero="Inversiones sindicales en fondos y empresas.",
 crono=[("1985-12", "Fundación."), ("1990s", "Alianza tripartita con el ANC y el Partido Comunista.")],
 fuentes=[("COSATU (Wikipedia)", W + "Congress_of_South_African_Trade_Unions")]),
"aflcio": dict(
 res=["La mayor federación sindical de EE.UU., con unos 12 millones de afiliados; principal maquinaria sindical del Partido Demócrata."],
 manda=["Liz Shuler, presidenta."],
 dinero="Gasto político electoral de sus sindicatos miembros.",
 crono=[("1955", "Fusión de la AFL y el CIO.")],
 fuentes=[("AFL–CIO (Wikipedia)", W + "AFL%E2%80%93CIO")]),
"igmetall": dict(
 res=["El mayor sindicato de Europa, con más de 2 millones de afiliados en la industria alemana; por ley de cogestión ocupa asientos en los directorios de las grandes empresas."],
 manda=["Christiane Benner, presidenta."],
 dinero="Fondos de huelga y participación en consejos de vigilancia.",
 crono=[("1949", "Fundación."), ("1976", "Ley de cogestión.")],
 fuentes=[("IG Metall (Wikipedia)", W + "IG_Metall")]),
"cut_br": dict(
 res=["La mayor central sindical de Brasil, nacida de las huelgas metalúrgicas que encabezó Lula a fines de los setenta."],
 manda=["Dirección nacional electa en congreso."],
 dinero="Aportes de sindicatos afiliados.",
 crono=[("1983-08", "Fundación.")],
 fuentes=[("Central Única dos Trabalhadores (Wikipedia)", W + "Central_%C3%9Anica_dos_Trabalhadores")]),
# Organismos internos
"tesoro_eeuu": dict(
 res=["El Tesoro de EE.UU. y su Oficina de Control de Activos Extranjeros (OFAC) deciden sanciones que cortan a países, empresas y personas del sistema financiero en dólares.",
      "En 2025 sostuvo a la Argentina con un canje de 20.000 millones de dólares."],
 manda=["Scott Bessent, secretario del Tesoro."],
 dinero="Emite la deuda del gobierno de EE.UU., el activo de reserva del mundo.",
 crono=[("1789", "Creación."), ("1950", "Origen de la OFAC."), ("2025-10", "Sanciones a Rosneft, Lukoil y el Prince Group; canje con la Argentina.")],
 fuentes=[("United States Department of the Treasury (Wikipedia)", W + "United_States_Department_of_the_Treasury"), ("Office of Foreign Assets Control (Wikipedia)", W + "Office_of_Foreign_Assets_Control")]),
"bis": dict(
 res=["Oficina del Departamento de Comercio que administra los controles de exportación: decide qué chips, máquinas y software pueden venderse a China y a otros países."],
 manda=["Subsecretario de Comercio para Industria y Seguridad."],
 dinero="Sus listas negras pueden aislar a empresas enteras de la tecnología estadounidense.",
 crono=[("2019-05", "Huawei, a la lista de entidades."), ("2022-10", "Controles sobre chips avanzados para China.")],
 fuentes=[("Bureau of Industry and Security (Wikipedia)", W + "Bureau_of_Industry_and_Security")]),
"ccdi": dict(
 res=["Órgano del Partido Comunista que investiga y castiga a sus miembros; instrumento de las purgas anticorrupción de Xi Jinping, incluidas las de la cúpula militar."],
 manda=["Li Xi, secretario, miembro del Comité Permanente del Politburó."],
 dinero="Sin presupuesto relevante; su poder es la detención extrajudicial de cuadros.",
 crono=[("1927", "Origen."), ("2012-11", "Comienza la campaña anticorrupción de Xi.")],
 fuentes=[("Central Commission for Discipline Inspection (Wikipedia)", W + "Central_Commission_for_Discipline_Inspection")]),
"consejo_seg_rusia": dict(
 res=["Órgano donde el círculo de Putin coordina la política de seguridad, defensa e inteligencia."],
 manda=["Putin lo preside; Serguéi Shoigú es su secretario desde 2024."],
 dinero="Sin presupuesto propio relevante.",
 crono=[("1992", "Creación."), ("2022-02-21", "Sesión televisada previa a la invasión de Ucrania."), ("2024-05", "Shoigú, secretario.")],
 fuentes=[("Security Council of Russia (Wikipedia)", W + "Security_Council_of_Russia")]),
"city_londres": dict(
 res=["Gobierno autónomo del distrito financiero de Londres, con una estructura medieval en la que votan empresas además de residentes; defiende los intereses de la banca británica e internacional."],
 manda=["Lord Mayor, Court of Aldermen y Court of Common Council."],
 dinero="Centro de la red financiera británica, ligada a jurisdicciones de baja tributación.",
 crono=[("1067", "Carta de Guillermo el Conquistador."), ("1986-10", "Big Bang de desregulación financiera.")],
 fuentes=[("City of London Corporation (Wikipedia)", W + "City_of_London_Corporation")]),
# Inteligencia
"shinbet": dict(
 res=["Servicio de seguridad interior de Israel, con control de inteligencia sobre Gaza y Cisjordania."],
 manda=["David Zini, director desde 2025, designado por Netanyahu tras el despido de Ronen Bar."],
 dinero="Presupuesto reservado.",
 crono=[("1949", "Creación."), ("2025-03", "Netanyahu intenta despedir a Ronen Bar."), ("2025-10", "Zini asume.")],
 fuentes=[("Shin Bet (Wikipedia)", W + "Shin_Bet")]),
"bnd": dict(
 res=["Servicio de inteligencia exterior de Alemania, socio de la CIA y de los servicios europeos frente a Rusia."],
 manda=["Martin Jäger, presidente desde 2025."],
 dinero="Presupuesto reservado.",
 crono=[("1956", "Creación."), ("2013", "Revelaciones sobre cooperación con la NSA.")],
 fuentes=[("Federal Intelligence Service (Wikipedia)", W + "Federal_Intelligence_Service")]),
"nis_corea": dict(
 res=["Inteligencia de Corea del Sur, centrada en Corea del Norte y China; históricamente influyente en la política interna."],
 manda=["Director designado por el presidente Lee Jae-myung."],
 dinero="Presupuesto reservado.",
 crono=[("1961", "Creación como KCIA."), ("1999", "Nombre actual.")],
 fuentes=[("National Intelligence Service (South Korea) (Wikipedia)", W + "National_Intelligence_Service_(South_Korea)")]),
"gur": dict(
 res=["Inteligencia militar de Ucrania: sabotajes, ataques con drones de largo alcance y operaciones dentro de Rusia."],
 manda=["Oleh Ivashchenko, jefe desde enero de 2026; su antecesor Budánov pasó a dirigir la Oficina del Presidente."],
 dinero="Presupuesto militar y fondos de apoyo externo.",
 crono=[("1992", "Creación."), ("2020-08", "Budánov, jefe."), ("2026-01-02", "Ivashchenko lo reemplaza.")],
 fuentes=[("Main Directorate of Intelligence (Ukraine) (Wikipedia)", W + "Main_Directorate_of_Intelligence_(Ukraine)"), ("Ukrinform: Ivashchenko al GUR", "https://www.ukrinform.net/rubric-polytics/4076184-budanov-officially-appointed-head-of-presidential-office-ivashchenko-takes-over-gur.html")]),
# Partidos
"ldp": dict(
 res=["Partido que gobernó Japón casi sin interrupción desde 1955; con Sanae Takaichi ganó por amplio margen las elecciones de febrero de 2026."],
 manda=["Sanae Takaichi, presidenta del partido y primera ministra; las facciones internas y Keidanren pesan en las decisiones."],
 dinero="Financiamiento empresario canalizado por Keidanren.",
 crono=[("1955-11", "Fundación."), ("2025-10", "Takaichi, primera ministra."), ("2026-02", "Victoria electoral.")],
 fuentes=[("Liberal Democratic Party (Japan) (Wikipedia)", W + "Liberal_Democratic_Party_(Japan)")]),
"anc": dict(
 res=["Partido de Mandela que gobierna Sudáfrica desde 1994; perdió la mayoría en 2024 y gobierna en coalición."],
 manda=["Cyril Ramaphosa, presidente del partido y de la República."],
 dinero="Inversiones partidarias y redes de contratos públicos.",
 crono=[("1912", "Fundación."), ("1994-04", "Primeras elecciones libres."), ("2024-05", "Pierde la mayoría absoluta.")],
 fuentes=[("African National Congress (Wikipedia)", W + "African_National_Congress")]),
"bnp": dict(
 res=["Partido que gobierna Bangladés desde febrero de 2026 con mayoría de dos tercios, tras la caída de Sheikh Hasina."],
 manda=["Tarique Rahman, presidente del partido y primer ministro."],
 dinero="Redes empresarias de la industria textil.",
 crono=[("1978", "Fundación por Ziaur Rahman."), ("2026-02-12", "Victoria electoral."), ("2026-02-17", "Rahman jura.")],
 fuentes=[("Bangladesh Nationalist Party (Wikipedia)", W + "Bangladesh_Nationalist_Party"), ("Dawn / AFP: Rahman jura", "https://www.dawn.com/news/1973874")]),
"tisza": dict(
 res=["Partido de Péter Magyar que puso fin a los 16 años de Orbán al ganar las elecciones del 12 de abril de 2026 con mayoría de dos tercios."],
 manda=["Péter Magyar, presidente del partido y primer ministro."],
 dinero="Recuperación de fondos europeos congelados.",
 crono=[("2024", "Magyar toma el control del partido."), ("2026-04-12", "Victoria electoral.")],
 fuentes=[("Tisza Party (Wikipedia)", W + "Tisza_Party"), ("CBS News: Orbán reconoce la derrota", "https://www.cbsnews.com/news/hungary-general-election-viktor-orban-peter-magyar-results/")]),
"prosperidad": dict(
 res=["Partido gobernante de Etiopía, creado por Abiy Ahmed; controla el Estado federal en medio de conflictos en Amhara y Oromía."],
 manda=["Abiy Ahmed, presidente del partido y primer ministro."],
 dinero="Control de empresas estatales y de la Gran Represa del Renacimiento.",
 crono=[("2019-12", "Fundación."), ("2021-06", "Victoria electoral."), ("2025-09", "Inauguración de la Gran Represa.")],
 fuentes=[("Prosperity Party (Wikipedia)", W + "Prosperity_Party")]),
"fpr": dict(
 res=["Partido gobernante de Ruanda desde 1994; su holding Crystal Ventures es uno de los grandes grupos económicos del país."],
 manda=["Paul Kagame, presidente del partido."],
 dinero="Crystal Ventures, con inversiones en construcción, finanzas y seguridad.",
 crono=[("1987", "Fundación en Uganda."), ("1994-07", "Toma del poder.")],
 fuentes=[("Rwandan Patriotic Front (Wikipedia)", W + "Rwandan_Patriotic_Front")]),
"psuv": dict(
 res=["Partido del chavismo, que conserva el aparato del Estado venezolano tras la captura de Maduro, bajo tutela de EE.UU."],
 manda=["Diosdado Cabello, vicepresidente del partido y ministro del Interior, controla la policía; con Delcy y Jorge Rodríguez forman los polos del poder."],
 dinero="Control de la administración pública y de las redes de distribución estatal.",
 crono=[("2007", "Fundación."), ("2026-01-03", "Captura de Maduro.")],
 fuentes=[("United Socialist Party of Venezuela (Wikipedia)", W + "United_Socialist_Party_of_Venezuela"), ("CNN: el poder de Cabello", "https://cnnespanol.cnn.com/2026/01/07/venezuela/diosdado-cabello-poder-gobierno-perfil-orix")]),
"fpa": dict(
 res=["Bancada multipartidaria del agronegocio, la más numerosa del Congreso brasileño: condiciona leyes ambientales, de tierras y de comercio."],
 manda=["Presidencia rotativa entre diputados ruralistas; respaldada por las entidades del agronegocio."],
 dinero="Brasil es el mayor exportador mundial de soja, carne vacuna y café.",
 crono=[("1995", "Origen de la bancada ruralista."), ("2008", "Formalización como frente parlamentario.")],
 fuentes=[("Bancada ruralista (Wikipedia)", W + "Bancada_ruralista")]),
"marco_coord": dict(
 res=["Alianza de los partidos chiitas que designa al primer ministro de Irak; varias de sus facciones tienen milicias propias dentro de las Fuerzas de Movilización Popular."],
 manda=["Nuri al-Maliki, Hadi al-Amiri, Qais al-Khazali y otros jefes; en 2026 eligió a Ali al-Zaidi como candidato de consenso tras el veto de EE.UU. a Maliki."],
 dinero="Reparto de ministerios y contratos del Estado petrolero.",
 crono=[("2021", "Formación tras las elecciones."), ("2026-04-27", "Ali al-Zaidi, primer ministro designado."), ("2026-05-14", "Jura del nuevo gobierno.")],
 fuentes=[("Coordination Framework (Wikipedia)", W + "Coordination_Framework"), ("The National: jura de al-Zaidi", "https://thenationalnews.com/news/mena/2026/05/14/iraqi-parliament-votes-on-thursday-in-key-step-towards-installing-government/")]),
# Empresas
"softbank": dict(
 res=["Grupo japonés de inversión de Masayoshi Son: dueño de la diseñadora de chips Arm y uno de los mayores accionistas de OpenAI."],
 manda=["Masayoshi Son, fundador, presidente y director ejecutivo."],
 dinero="Comprometió más de 60.000 millones de dólares en OpenAI, por alrededor del 13 % de la empresa.",
 crono=[("1981", "Fundación."), ("2016", "Compra de Arm."), ("2025-01", "Proyecto Stargate con OpenAI y Oracle."), ("2026-10", "Último tramo de su inversión en OpenAI.")],
 fuentes=[("SoftBank Group (Wikipedia)", W + "SoftBank_Group"), ("SoftBank: inversiones en OpenAI (2026-02-27)", "https://group.softbank/en/news/press/20260227")]),
"brookfield": dict(
 res=["Uno de los mayores dueños de infraestructura del mundo: energía, puertos, oleoductos, centros de datos e inmuebles."],
 manda=["Bruce Flatt, director ejecutivo."],
 dinero="Más de 1 billón de dólares en activos administrados.",
 crono=[("1899", "Origen en Brasil como São Paulo Tramway."), ("2005", "Nombre Brookfield.")],
 fuentes=[("Brookfield Corporation (Wikipedia)", W + "Brookfield_Corporation")]),
"techint": dict(
 res=["Grupo ítalo-argentino de la familia Rocca: Tenaris, líder mundial en tubos para petróleo y gas, y Ternium, siderúrgica de América Latina; actor clave en Vaca Muerta."],
 manda=["Paolo Rocca, presidente."],
 dinero="Ingresos de decenas de miles de millones de dólares en varios países.",
 crono=[("1945", "Fundación en Milán por Agostino Rocca."), ("2002", "Creación de Tenaris.")],
 fuentes=[("Techint (Wikipedia)", W + "Techint"), ("Tenaris (Wikipedia)", W + "Tenaris")]),
"inditex": dict(
 res=["El mayor grupo textil del mundo (Zara), con cadena de suministro global."],
 manda=["Amancio Ortega, fundador y accionista mayoritario; Marta Ortega, presidenta."],
 dinero="Amancio Ortega es una de las mayores fortunas de Europa.",
 crono=[("1975", "Primera tienda Zara."), ("2001", "Salida a bolsa.")],
 fuentes=[("Inditex (Wikipedia)", W + "Inditex")]),
"santander": dict(
 res=["El mayor banco de la zona euro por capitalización, con fuerte presencia en España, el Reino Unido, Brasil, México y EE.UU."],
 manda=["Ana Botín, presidenta, de la familia que lo conduce desde hace generaciones."],
 dinero="Activos superiores a 1,5 billones de euros.",
 crono=[("1857", "Fundación."), ("2014", "Ana Botín, presidenta.")],
 fuentes=[("Banco Santander (Wikipedia)", W + "Banco_Santander")]),
"exor": dict(
 res=["Holding de la familia Agnelli-Elkann: controla Ferrari, Stellantis, Juventus y tiene participación en The Economist."],
 manda=["John Elkann, director ejecutivo."],
 dinero="Cartera de varias decenas de miles de millones de euros.",
 crono=[("1927", "Origen en IFI de la familia Agnelli."), ("2009", "Nombre Exor.")],
 fuentes=[("Exor (company) (Wikipedia)", W + "Exor_(company)")]),
"eni": dict(
 res=["Petrolera de control estatal italiano, con producción en Libia, Argelia, Egipto, Mozambique y Kazajistán: brazo de la política energética de Italia."],
 manda=["Claudio Descalzi, director ejecutivo; el Estado italiano tiene alrededor de un 30 %."],
 dinero="Ganancias de miles de millones de euros anuales.",
 crono=[("1953", "Fundación por Enrico Mattei."), ("2015", "Descubrimiento del yacimiento Zohr en Egipto.")],
 fuentes=[("Eni (Wikipedia)", W + "Eni")]),
"hyundai": dict(
 res=["Uno de los mayores fabricantes de autos del mundo y, con Hyundai Rotem, productor de tanques K2; parte de la red de chaebol que domina la economía coreana."],
 manda=["Chung Eui-sun, presidente ejecutivo, de la familia fundadora."],
 dinero="Ingresos de más de 100.000 millones de dólares.",
 crono=[("1967", "Fundación de Hyundai Motor."), ("2020", "Chung Eui-sun asume la conducción.")],
 fuentes=[("Hyundai Motor Group (Wikipedia)", W + "Hyundai_Motor_Group")]),
"foxconn": dict(
 res=["El mayor fabricante por contrato de electrónica del mundo: ensambla iPhone y servidores de inteligencia artificial para Nvidia, con plantas en China, India, México y EE.UU."],
 manda=["Young Liu, presidente."],
 dinero="Ingresos de más de 200.000 millones de dólares.",
 crono=[("1974", "Fundación por Terry Gou.")],
 fuentes=[("Foxconn (Wikipedia)", W + "Foxconn")]),
"baykar": dict(
 res=["Fabricante de los drones Bayraktar, exportados a más de 30 países y usados en Ucrania, Libia, Siria y Nagorno Karabaj."],
 manda=["Haluk Bayraktar, director ejecutivo; Selçuk Bayraktar, director técnico y yerno de Erdoğan."],
 dinero="Uno de los mayores exportadores de defensa de Turquía.",
 crono=[("1984", "Fundación."), ("2014", "Primer Bayraktar TB2."), ("2024-12", "Compra de la italiana Piaggio Aerospace.")],
 fuentes=[("Baykar (Wikipedia)", W + "Baykar")]),
"nnpc": dict(
 res=["Petrolera estatal de Nigeria, socia de las grandes petroleras en el delta del Níger y accionista de la refinería Dangote."],
 manda=["Directorio designado por el gobierno federal."],
 dinero="Principal fuente de ingresos del Estado nigeriano.",
 crono=[("1977", "Creación."), ("2022", "Conversión en sociedad comercial.")],
 fuentes=[("Nigerian National Petroleum Corporation (Wikipedia)", W + "Nigerian_National_Petroleum_Corporation")]),
"aval": dict(
 res=["El mayor grupo financiero de Colombia, dueño de bancos, fondos de pensiones y del diario El Tiempo."],
 manda=["Familia Sarmiento Angulo."],
 dinero="Una de las mayores fortunas de América Latina.",
 crono=[("1998", "Creación del holding."), ("2012", "Compra del diario El Tiempo.")],
 fuentes=[("Grupo Aval (Wikipedia)", W + "Grupo_Aval")]),
"luksic": dict(
 res=["El mayor grupo económico de Chile: minería de cobre (Antofagasta), banca (Banco de Chile), bebidas y navieras."],
 manda=["Andrónico y Jean-Paul Luksic, de la familia controladora."],
 dinero="La mayor fortuna de Chile.",
 crono=[("1950s", "Andrónico Luksic Abaroa inicia el grupo en Antofagasta.")],
 fuentes=[("Luksic Group (Wikipedia)", W + "Grupo_Luksic")]),
"hancock": dict(
 res=["Minera de hierro de la familia Rinehart, la mayor fortuna de Australia, con fuerte influencia en la política australiana."],
 manda=["Gina Rinehart, presidenta ejecutiva."],
 dinero="Exportaciones de mineral de hierro a China.",
 crono=[("1955", "Fundación por Lang Hancock.")],
 fuentes=[("Hancock Prospecting (Wikipedia)", W + "Hancock_Prospecting")]),
"porsche_se": dict(
 res=["Holding de las familias Porsche y Piëch que controla Volkswagen, el mayor grupo automotor de Europa."],
 manda=["Familias Porsche y Piëch, dueñas de las acciones con voto."],
 dinero="Control de la mayoría de los votos de Volkswagen.",
 crono=[("2007", "Creación del holding."), ("2009", "Fracaso de la toma de Volkswagen y fusión inversa.")],
 fuentes=[("Porsche SE (Wikipedia)", W + "Porsche_SE")]),
"bollore": dict(
 res=["Grupo de la familia Bolloré, que controla Vivendi, Canal+, el canal CNews y la editorial Hachette: el principal poder mediático conservador de Francia."],
 manda=["Vincent Bolloré y sus hijos Yannick y Cyrille."],
 dinero="Vendió en 2022 su red logística africana a MSC.",
 crono=[("1822", "Fundación."), ("2022", "Venta de Bolloré Africa Logistics a MSC.")],
 fuentes=[("Bolloré (Wikipedia)", W + "Bollor%C3%A9")]),
"dassault": dict(
 res=["Grupo familiar francés que fabrica el avión de combate Rafale, posee el diario Le Figaro y es accionista de Thales."],
 manda=["Familia Dassault."],
 dinero="Exportaciones del Rafale a India, Egipto, Catar, Grecia, Emiratos e Indonesia.",
 crono=[("1929", "Fundación por Marcel Dassault."), ("2004", "Compra de Le Figaro.")],
 fuentes=[("Dassault Group (Wikipedia)", W + "Dassault_Group")]),
"safaricom": dict(
 res=["Mayor empresa de Kenia y dueña de M-Pesa, el sistema de dinero móvil que usa la mayoría de los kenianos."],
 manda=["Vodacom (del grupo británico Vodafone) y el Estado keniano son los principales accionistas."],
 dinero="M-Pesa mueve una parte sustancial del PBI keniano.",
 crono=[("2000", "Fundación."), ("2007-03", "Lanzamiento de M-Pesa.")],
 fuentes=[("Safaricom (Wikipedia)", W + "Safaricom"), ("M-Pesa (Wikipedia)", W + "M-Pesa")]),
"noboa_grupo": dict(
 res=["Grupo exportador de banano y otros negocios de la familia del presidente ecuatoriano Daniel Noboa."],
 manda=["Familia Noboa."],
 dinero="Uno de los grupos empresarios más grandes de Ecuador.",
 crono=[("1940s", "Origen con Luis Noboa Naranjo."), ("2023-11", "Daniel Noboa llega a la presidencia.")],
 fuentes=[("Álvaro Noboa (Wikipedia)", W + "%C3%81lvaro_Noboa"), ("Daniel Noboa (Wikipedia)", W + "Daniel_Noboa")]),
"danantara": dict(
 res=["Fondo soberano de Indonesia creado en 2025 que concentra las participaciones estatales en bancos, energía y telecomunicaciones."],
 manda=["Bajo control del presidente Prabowo."],
 dinero="Activos estimados en cientos de miles de millones de dólares.",
 crono=[("2025-02", "Creación.")],
 fuentes=[("Danantara (Wikipedia)", W + "Danantara")]),
"keidanren": dict(
 res=["Federación de las grandes empresas japonesas; define posiciones de política económica y es el principal apoyo empresario del LDP."],
 manda=["Presidente y consejo de las mayores corporaciones."],
 dinero="Coordina donaciones políticas de sus miembros.",
 crono=[("1946", "Fundación."), ("2002", "Fusión con Nikkeiren.")],
 fuentes=[("Keidanren (Wikipedia)", W + "Keidanren")]),
# Fuerzas armadas
"ffaa_reinounido": dict(
 res=["Fuerzas armadas británicas, potencia nuclear con submarinos Trident y bases en el exterior; pieza central del apoyo militar europeo a Ucrania."],
 manda=["Jefe del Estado Mayor de la Defensa, bajo el primer ministro."],
 dinero="Uno de los mayores presupuestos de defensa de Europa.",
 crono=[("1969", "Disuasión nuclear con submarinos."), ("2021-09", "Pacto AUKUS.")],
 fuentes=[("British Armed Forces (Wikipedia)", W + "British_Armed_Forces")]),
"ffaa_francia": dict(
 res=["Fuerzas armadas francesas, única potencia nuclear de la Unión Europea, con presencia en el Indo-Pacífico y salida forzada del Sahel."],
 manda=["Jefe del Estado Mayor de los Ejércitos, bajo el presidente de la República, que controla el arma nuclear."],
 dinero="Ley de programación militar con aumentos sostenidos.",
 crono=[("1960", "Primera prueba nuclear."), ("2022-2025", "Retiro de Malí, Burkina Faso y Níger.")],
 fuentes=[("French Armed Forces (Wikipedia)", W + "French_Armed_Forces")]),
"bundeswehr": dict(
 res=["Fuerzas armadas alemanas en pleno rearme tras la reforma del freno a la deuda de 2025, con el objetivo de ser el mayor ejército convencional de Europa."],
 manda=["Inspector general, bajo el ministro de Defensa; el Parlamento autoriza los despliegues."],
 dinero="Fondo especial de 100.000 millones de euros de 2022 y excepción del gasto de defensa del freno a la deuda.",
 crono=[("1955", "Creación."), ("2022-02-27", "Anuncio del cambio de época."), ("2025-03", "Reforma del freno a la deuda.")],
 fuentes=[("Bundeswehr (Wikipedia)", W + "Bundeswehr")]),
"jsdf": dict(
 res=["Fuerzas armadas de Japón, en expansión: duplicación del gasto de defensa y capacidad de contraataque ante China y Corea del Norte."],
 manda=["Jefe del Estado Mayor Conjunto, bajo la primera ministra."],
 dinero="Meta de gasto de defensa del 2 % del PBI.",
 crono=[("1954", "Creación."), ("2022-12", "Nueva estrategia de seguridad.")],
 fuentes=[("Japan Self-Defense Forces (Wikipedia)", W + "Japan_Self-Defense_Forces")]),
"ffaa_taiwan": dict(
 res=["Fuerzas armadas de Taiwán, frente principal de una posible guerra entre EE.UU. y China, abastecidas por armas estadounidenses."],
 manda=["Jefe del Estado Mayor General, bajo el presidente Lai Ching-te."],
 dinero="Compras de armas a EE.UU. por miles de millones de dólares.",
 crono=[("1949", "Retirada a Taiwán."), ("2024-01", "Extensión del servicio militar a un año.")],
 fuentes=[("Republic of China Armed Forces (Wikipedia)", W + "Republic_of_China_Armed_Forces")]),
"ffaa_filipinas": dict(
 res=["Fuerzas armadas filipinas, en primera línea de los choques con China en el mar de China Meridional y con acceso de EE.UU. a nueve bases."],
 manda=["Jefe del Estado Mayor, bajo el presidente Ferdinand Marcos Jr."],
 dinero="Modernización con apoyo de EE.UU. y Japón.",
 crono=[("2014", "Acuerdo de cooperación de defensa reforzada con EE.UU."), ("2023", "Ampliación a nueve bases.")],
 fuentes=[("Armed Forces of the Philippines (Wikipedia)", W + "Armed_Forces_of_the_Philippines")]),
"ffaa_corea": dict(
 res=["Fuerzas armadas de Corea del Sur, entre las más grandes y mejor equipadas del mundo, integradas al mando combinado con EE.UU."],
 manda=["Jefe del Estado Mayor Conjunto; el mando operativo en guerra lo ejerce el comando combinado con EE.UU."],
 dinero="Gran industria de defensa exportadora.",
 crono=[("1948", "Creación."), ("1953-07", "Armisticio."), ("2024-12-03", "Despliegue durante la ley marcial fallida.")],
 fuentes=[("Republic of Korea Armed Forces (Wikipedia)", W + "Republic_of_Korea_Armed_Forces")]),
"adf": dict(
 res=["Fuerzas de defensa de Australia, eje del pacto AUKUS para adquirir submarinos de propulsión nuclear con EE.UU. y el Reino Unido."],
 manda=["Jefe de las Fuerzas de Defensa, bajo el gobierno."],
 dinero="Programa de submarinos de cientos de miles de millones de dólares australianos.",
 crono=[("1901", "Creación."), ("2021-09", "Anuncio de AUKUS.")],
 fuentes=[("Australian Defence Force (Wikipedia)", W + "Australian_Defence_Force"), ("AUKUS (Wikipedia)", W + "AUKUS")]),
"ffaa_polonia": dict(
 res=["Fuerzas armadas de Polonia, en expansión acelerada en la frontera oriental de la OTAN, con compras masivas a EE.UU. y Corea del Sur."],
 manda=["Jefe del Estado Mayor General, bajo el presidente y el gobierno."],
 dinero="Gasto de defensa superior al 4 % del PBI.",
 crono=[("1999", "Ingreso a la OTAN."), ("2022", "Contratos con Corea del Sur y EE.UU.")],
 fuentes=[("Polish Armed Forces (Wikipedia)", W + "Polish_Armed_Forces")]),
"ffmm_colombia": dict(
 res=["Fuerzas militares de Colombia, el principal aliado militar de EE.UU. en Sudamérica, en guerra con el ELN, disidencias y el Clan del Golfo."],
 manda=["Comandante general, bajo el presidente Abelardo de la Espriella desde agosto de 2026."],
 dinero="Cooperación militar de EE.UU. desde el Plan Colombia.",
 crono=[("2000", "Plan Colombia."), ("2016", "Acuerdo de paz con las FARC.")],
 fuentes=[("Military Forces of Colombia (Wikipedia)", W + "Military_Forces_of_Colombia")]),
"fanb": dict(
 res=["Fuerza Armada de Venezuela, sostén del chavismo, que juró lealtad a Delcy Rodríguez tras la captura de Maduro."],
 manda=["El general Gustavo González López reemplazó a Vladimir Padrino López como ministro de Defensa en marzo de 2026."],
 dinero="Empresas militares en minería, petróleo y alimentos.",
 crono=[("2026-01", "Juramento de lealtad a Delcy Rodríguez."), ("2026-03", "Destitución de Padrino López.")],
 fuentes=[("National Bolivarian Armed Forces of Venezuela (Wikipedia)", W + "National_Bolivarian_Armed_Forces_of_Venezuela"), ("CiberCuba: la FANB reconoce a Rodríguez", "https://en.cibercuba.com/noticias/2026-01-29-u1-e135253-s27061-nid319569-fuerza-armada-venezuela-reconoce-delcy-rodriguez")]),
"tni": dict(
 res=["Fuerzas armadas de Indonesia, que recuperaron peso en el gobierno civil bajo el presidente Prabowo, exgeneral."],
 manda=["Comandante de la TNI, bajo el presidente."],
 dinero="Empresas y cooperativas militares.",
 crono=[("1945", "Creación."), ("1998", "Fin del régimen de Suharto."), ("2025-03", "Reforma de la ley de la TNI que amplía su papel civil.")],
 fuentes=[("Indonesian National Armed Forces (Wikipedia)", W + "Indonesian_National_Armed_Forces")]),
"hawza_najaf": dict(
 res=["El principal centro de autoridad religiosa del islam chiita fuera de Irán; el gran ayatolá Ali al-Sistani avala o veta de hecho a los gobiernos de Irak."],
 manda=["Gran ayatolá Ali al-Sistani, de edad muy avanzada; su sucesión es una incógnita clave para Irak e Irán."],
 dinero="Donaciones religiosas (jums) de millones de fieles y gestión de santuarios.",
 crono=[("2003", "Sistani impone elecciones tras la invasión de EE.UU."), ("2014-06", "Fatwa contra el Estado Islámico."), ("2019-11", "Respaldo a las protestas que provocan la caída del gobierno.")],
 fuentes=[("Ali al-Sistani (Wikipedia)", W + "Ali_al-Sistani"), ("Hawza of Najaf (Wikipedia)", W + "Hawza_of_Najaf")]),
})

FICHAS["ffaa_india"] = dict(
 res=["Fuerzas armadas de la India, potencia nuclear con el segundo mayor número de efectivos del mundo, enfrentada a Pakistán y a China en sus fronteras."],
 manda=["Jefe del Estado Mayor de Defensa, bajo el gobierno de Narendra Modi."],
 dinero="Uno de los mayores importadores de armas del mundo: Rusia, Francia, EE.UU. e Israel.",
 crono=[("1974-05", "Primera prueba nuclear."), ("1999", "Guerra de Kargil."), ("2020-06", "Choque de Galwan con China."), ("2025-05", "Operación Sindoor contra Pakistán.")],
 fuentes=[("Indian Armed Forces (Wikipedia)", W + "Indian_Armed_Forces")])

from locales import FICHAS as _FL
FICHAS.update(_FL)

from nucleo import FICHAS as _FN
FICHAS.update(_FN)

from nucleo2 import FICHAS as _FN2
FICHAS.update(_FN2)
from nucleo3 import FICHAS as _FN3
FICHAS.update(_FN3)
from nucleo4 import FICHAS as _FN4
FICHAS.update(_FN4)

import importlib as _il
for _t in ["nucleo5", "nucleo6", "nucleo7", "nucleo8"]: FICHAS.update(_il.import_module(_t).FICHAS)

# Correcciones del 20 de noviembre de 2026 (ver fuente/correcciones.py)
from correcciones import PARCHES as _PAR
for _k, _p in _PAR.items():
    _f = FICHAS[_k]
    if "res" in _p: _f["res"] = list(_p["res"])
    _f["res"] = _f["res"] + _p.get("res_mas", [])
    if "manda" in _p: _f["manda"] = list(_p["manda"])
    _f["crono"] = sorted(_f["crono"] + _p.get("crono_mas", []), key=lambda c: str(c[0]))
    _f["fuentes"] = _f["fuentes"] + [x for x in _p.get("fuentes_mas", []) if x not in _f["fuentes"]]
