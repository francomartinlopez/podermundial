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
