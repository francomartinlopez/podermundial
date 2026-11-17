# Intereses y acciones de cada bloque en cada país (2016-2026).
# T: imperio transoceánico (EE.UU. y aliados). E: alianza euroasiática (China, Rusia, Irán y aliados).
# Campos: ti, ei (intereses: qué quiere cada bloque ahí); ta, ea (acciones de los últimos diez años: [(año, hecho)]).
# Una lista vacía significa que no hay acciones relevantes de ese bloque en el período.

PB = {}


def B(k, ti, ta, ei, ea):
    PB[k] = dict(ti=ti, ta=ta, ei=ei, ea=ea)


# ───────────────────────── América del Norte ─────────────────────────

B('United States of America',
  'Es el centro del bloque: conservar la primacía militar, el dólar y la delantera tecnológica, y reindustrializarse.',
  [(2018, 'Primera guerra comercial con China y controles a Huawei.'), (2022, 'Ley de chips y controles a la exportación de semiconductores avanzados a China.'),
   (2025, 'Aranceles generales a aliados y rivales.'), (2026, 'Guerra con Irán y captura de Maduro.')],
  'Erosionar su hegemonía: desdolarizar el comercio, acceder a su tecnología y dividir su opinión pública y sus alianzas.',
  [(2016, 'Injerencia rusa en la elección presidencial, documentada por la inteligencia de EE.UU. y el Senado.'), (2020, 'Ciberespionaje SolarWinds, atribuido a la inteligencia rusa.'),
   (2023, 'Globo espía chino sobre territorio estadounidense.'), (2024, 'Intrusión china Salt Typhoon en las redes de telecomunicaciones.')])

B('Canada',
  'Mantenerlo integrado en la defensa de América del Norte (NORAD), el Ártico y las cadenas de energía y minerales.',
  [(2018, 'Arresto de la directora financiera de Huawei a pedido de EE.UU.'), (2020, 'Entra en vigor el T-MEC.'), (2025, 'EE.UU. le aplica aranceles y su presidente habla de anexarlo.')],
  'Influencia en su diáspora y su política, acceso al Ártico y a sus minerales.',
  [(2018, 'China detiene a dos canadienses en represalia por el caso Huawei (liberados en 2021).'), (2023, 'Expulsión de un diplomático chino por intimidar a un diputado.'), (2024, 'Una comisión pública confirma injerencia china e india en sus elecciones.')])

B('Mexico',
  'Cerrar la frontera a la droga y la migración, integrar su industria a EE.UU. y frenar la entrada de capital chino.',
  [(2019, 'Amenaza de aranceles para forzar el control migratorio; despliegue de la Guardia Nacional.'), (2020, 'T-MEC.'),
   (2025, 'EE.UU. declara terroristas a los cárteles, presiona con aranceles y obtiene extradiciones masivas.')],
  'Usarlo como puerta al mercado de EE.UU. y ampliar su influencia en el vecino del rival.',
  [(2023, 'Ola de inversiones industriales chinas en el norte del país.'), (2024, 'Los precursores chinos del fentanilo, en el centro de la disputa con EE.UU.'), (2025, 'México sube aranceles a importaciones chinas bajo presión de EE.UU.')])

B('Greenland',
  'El Ártico, la base de Pituffik, las rutas marítimas y las tierras raras; impedir la entrada de China.',
  [(2019, 'EE.UU. propone comprar la isla.'), (2020, 'Reapertura del consulado estadounidense en Nuuk.'), (2025, 'Nueva presión de EE.UU. para controlarla; visita del vicepresidente a Pituffik.')],
  'Acceso a sus minerales y presencia en el Ártico.',
  [(2018, 'Dinamarca frena la construcción de aeropuertos por una empresa china.'), (2021, 'Se suspende la mina de uranio y tierras raras de Kvanefjeld, con capital chino.')])

B('Bermuda', 'Mantenerla como plaza de seguros ligada a Londres y Wall Street.', [(2023, 'Adopta un impuesto empresarial en línea con el mínimo global de la OCDE.')],
  'Ninguno relevante.', [])
B('St. Pierre and Miquelon', 'Ninguno particular: territorio de Francia.', [], 'Ninguno relevante.', [])

# ───────────────────────── Centroamérica y Caribe ─────────────────────────

B('Guatemala', 'Contener la migración y el narcotráfico, y conservar su reconocimiento de Taiwán.',
  [(2019, 'Acuerdo de «tercer país seguro» con EE.UU.'), (2024, 'Apoyo de EE.UU. a la asunción del presidente electo frente a la fiscalía.'), (2025, 'Acepta deportados de otros países.')],
  'Que cambie el reconocimiento de Taiwán a China.', [])
B('Belize', 'Seguridad del Caribe y control del narcotráfico.', [], 'Ninguno relevante; reconoce a Taiwán.', [])
B('Honduras', 'La base de Soto Cano, el narcotráfico y la migración.',
  [(2022, 'Extradición del expresidente Hernández a EE.UU., condenado en 2024 por narcotráfico.'), (2025, 'Indulto de EE.UU. a Hernández y respaldo a la oposición en las elecciones.')],
  'Ganarla para su lado frente a Taiwán.', [(2023, 'Rompe con Taiwán y reconoce a China.'), (2024, 'Firma de memorandos y apertura de embajada china.')])
B('El Salvador', 'Seguridad, migración y su uso como destino de deportados.',
  [(2019, 'Acuerdo migratorio con EE.UU.'), (2025, 'Recibe en el CECOT a deportados de EE.UU. a cambio de pagos.')],
  'Influencia económica tras el reconocimiento.', [(2018, 'Rompe con Taiwán y reconoce a China.'), (2019, 'China financia una biblioteca nacional y un estadio.')])
B('Costa Rica', 'Frenar el narcotráfico y excluir a China de las redes 5G.', [(2023, 'Decreto que excluye a proveedores de países sin tratado de ciberseguridad, en la práctica Huawei.')],
  'Comercio e inversión.', [])
B('Panama', 'El canal: asegurar el paso prioritario de la marina de EE.UU. y sacar a las empresas chinas de los puertos.',
  [(2025, 'EE.UU. exige el control del canal; Panamá sale de la Franja y la Ruta.'), (2025, 'CK Hutchison acuerda vender sus puertos del canal a un consorcio con BlackRock.'), (2025, 'Acuerdo de seguridad para presencia rotativa de tropas de EE.UU.')],
  'Mantener a sus empresas en la logística del canal y en la construcción.',
  [(2017, 'Rompe con Taiwán y reconoce a China.'), (2018, 'Se suma a la Franja y la Ruta.'), (2025, 'China rechaza la venta de los puertos de CK Hutchison.')])
B('Nicaragua', 'Aislar al régimen y frenar su cooperación con Rusia y China.',
  [(2018, 'Sanciones tras la represión.'), (2021, 'Ley RENACER: más sanciones.'), (2023, 'EE.UU. recibe a los 222 presos políticos desterrados.')],
  'Un aliado en el istmo frente a EE.UU.',
  [(2021, 'Rompe con Taiwán y reconoce a China.'), (2023, 'Tratado de libre comercio con China.'), (2024, 'Cooperación policial y militar con Rusia.')])
B('Cuba', 'Que caiga o cambie el régimen y que no vuelva a ser base de potencias rivales.',
  [(2017, 'Revierte el deshielo de Obama.'), (2021, 'Vuelve a la lista de Estados patrocinadores del terrorismo.'), (2026, 'Asfixia petrolera tras la caída de Maduro.')],
  'Una plataforma de inteligencia y presencia a 150 km de EE.UU.',
  [(2023, 'Denuncias de bases de escucha chinas en la isla.'), (2024, 'Visita de buques de guerra rusos y un submarino nuclear a La Habana.'), (2025, 'Rusia y China le envían petróleo y alimentos.')])
B('Haiti', 'Contener las pandillas y la migración.', [(2023, 'EE.UU. impulsa en la ONU la misión liderada por Kenia.'), (2025, 'Designa terroristas a las principales pandillas.')],
  'Ninguno relevante.', [])
B('Dominican Rep.', 'Excluir a China y mantener la cooperación antinarcóticos.', [(2025, 'Permite a EE.UU. usar aeropuertos para las operaciones en el Caribe.')],
  'Comercio e inversión tras el reconocimiento.', [(2018, 'Rompe con Taiwán y reconoce a China.')])
B('Jamaica', 'Seguridad y la base de bauxita.', [], 'Infraestructura y la planta de alúmina de capital chino.', [(2016, 'Una empresa china compra la refinería de alúmina de Alpart.')])
B('Trinidad and Tobago', 'Usarla como aliada frente a Venezuela.', [(2025, 'Respalda el despliegue naval de EE.UU. y admite un radar estadounidense.')], 'Gas y comercio.', [])
B('Bahamas', 'Seguridad marítima y control del lavado.', [], 'Inversión turística.', [(2017, 'Inauguración del complejo Baha Mar, financiado por bancos chinos.')])
B('Puerto Rico', 'Base de operaciones en el Caribe.', [(2025, 'Despliegue de cazas y marines para la campaña contra Venezuela.')], 'Ninguno.', [])
for k in ['Antigua and Barb.', 'Barbados', 'Dominica', 'Grenada', 'St. Kitts and Nevis', 'Saint Lucia', 'St. Vin. and Gren.']:
    B(k, 'Controlar la venta de pasaportes y la seguridad del Caribe.',
      [(2025, 'EE.UU. amenaza con restringir visas a los ciudadanos de los países con ciudadanía por inversión.')],
      'Influencia diplomática y votos en organismos internacionales.', [])
for k in ['U.S. Virgin Is.', 'Anguilla', 'Montserrat', 'St-Martin', 'St-Barthélemy', 'Sint Maarten']:
    B(k, 'Ninguno particular: territorio de una potencia del bloque.', [], 'Ninguno relevante.', [])
for k in ['Cayman Is.', 'British Virgin Is.', 'Turks and Caicos Is.']:
    B(k, 'Mantenerlo como plaza extraterritorial ligada a la City y a Wall Street, con más transparencia.',
      [(2016, 'Papeles de Panamá.'), (2018, 'El Parlamento británico ordena registros públicos de beneficiarios finales, aún sin cumplir del todo.')],
      'Usarlo para mover capital y ocultar dueños.', [(2016, 'Gran parte de las sociedades extraterritoriales chinas están registradas allí.')])
for k in ['Aruba', 'Curaçao']:
    B(k, 'La base antinarcóticos y la vigilancia de Venezuela.', [(2025, 'Uso de su base en la campaña de EE.UU. contra Venezuela.')], 'Ninguno relevante.', [])

# ───────────────────────── Sudamérica ─────────────────────────

B('Colombia', 'Su principal aliado militar en la región: la guerra contra la droga y el control de Venezuela.',
  [(2017, 'Socio global de la OTAN.'), (2025, 'EE.UU. le quita la certificación antinarcóticos y sanciona al presidente Petro.'), (2026, 'Reacomodo con el nuevo gobierno.')],
  'Comercio e infraestructura.', [(2020, 'Un consorcio chino gana el metro de Bogotá.'), (2025, 'Se suma a la Franja y la Ruta.')])
B('Venezuela', 'El petróleo, sacar a Rusia, China e Irán, y la migración.',
  [(2019, 'Reconoce a Guaidó y aplica sanciones petroleras.'), (2020, 'Acusa a Maduro de narcoterrorismo.'), (2025, 'Ataques a lanchas en el Caribe.'), (2026, 'Captura a Maduro y toma la transición.')],
  'Un aliado petrolero y militar en el patio trasero de EE.UU.',
  [(2018, 'Bombarderos rusos en Caracas.'), (2019, 'Asesores militares rusos.'), (2020, 'Irán le envía nafta y técnicos.'), (2023, 'China sigue comprando su crudo a través de intermediarios.')])
B('Ecuador', 'Bases y cooperación contra las bandas y los cárteles.',
  [(2023, 'Acuerdos de cooperación militar con EE.UU.'), (2025, 'Un referéndum rechaza bases extranjeras.')],
  'Petróleo, minería e infraestructura, con deuda.', [(2016, 'Represa Coca Codo Sinclair, construida por empresas chinas, con fallas.'), (2023, 'Tratado de libre comercio con China.')])
B('Peru', 'Contrarrestar el puerto chino de Chancay y asegurar los minerales.', [(2024, 'EE.UU. advierte por el uso dual de Chancay.')],
  'Una puerta logística al Pacífico y la minería.', [(2016, 'Empresas chinas dominan la minería del cobre (Las Bambas).'), (2024, 'Inauguración de Chancay, de COSCO.'), (2023, 'Empresas chinas compran la distribuidora eléctrica de Lima.')])
B('Bolivia', 'Volver a tenerlo cerca y acceder al litio.', [(2025, 'Acercamiento con el gobierno que sucede al MAS.')],
  'El litio y un aliado político.', [(2023, 'Contratos de litio con CATL (China) y Uranium One (Rusia).')])
B('Chile', 'El cobre y el litio, y mantener a China lejos de la infraestructura crítica.', [(2023, 'Acuerdo de asociación con la UE.')],
  'Su mayor comprador: cobre, litio y energía.', [(2020, 'State Grid compra la mayor distribuidora eléctrica, CGE.'), (2018, 'Tianqi compra el 24 % de SQM.')])
B('Argentina', 'Alinearla, sacar a China del espacio y la energía, y abrir el litio y Vaca Muerta.',
  [(2024, 'Compra de cazas F-16.'), (2025, 'Rescate financiero del Tesoro de EE.UU. y acuerdo comercial.')],
  'Soja, litio, puerto y la estación espacial de Neuquén.', [(2018, 'Empieza a operar la estación espacial china de Neuquén.'), (2023, 'Ampliación del swap de monedas con China.')])
B('Uruguay', 'Seguridad portuaria y control del narcotráfico.', [], 'Comercio y un tratado de libre comercio, frenado por el Mercosur.', [(2022, 'Negociación de un tratado comercial con China.')])
B('Paraguay', 'Mantenerlo como aliado de Taiwán y controlar la Triple Frontera.', [(2023, 'Sanciona a un expresidente por corrupción y vínculos con Hezbolá.')],
  'Que reconozca a China.', [])
B('Brazil', 'Evitar que se incline hacia China y Rusia y recuperarlo como socio.',
  [(2025, 'Aranceles de EE.UU. del 50 % y sanciones a un juez del Supremo.')],
  'El mayor socio de los BRICS en América: comercio, energía y un aliado diplomático.',
  [(2019, 'China pasa a ser destino de un tercio de sus exportaciones.'), (2025, 'Cumbre de los BRICS en Río.')])
B('Guyana', 'El petróleo de ExxonMobil y defenderla de Venezuela.', [(2023, 'Ejercicios militares con EE.UU. frente al reclamo venezolano.')],
  'Infraestructura.', [])
B('Suriname', 'El petróleo marino.', [], 'Infraestructura y deuda.', [])
B('Falkland Is.', 'La base de Mount Pleasant y la proyección al Atlántico Sur y la Antártida.', [], 'Ninguno relevante.', [])
B('S. Geo. and the Is.', 'Ninguno particular: territorio británico.', [], 'Pesca de buques chinos en la zona.', [])

# ───────────────────────── Europa occidental ─────────────────────────

B('United Kingdom', 'Socio nuclear y de inteligencia (Cinco Ojos), la City y su papel en Ucrania.',
  [(2020, 'Excluye a Huawei de su red 5G por presión de EE.UU.'), (2021, 'Pacto AUKUS.'), (2022, 'Primer proveedor europeo de armas a Ucrania.')],
  'Acceso a la City para mover capital, y debilitar su apoyo a Ucrania.',
  [(2018, 'Envenenamiento de Skripal en Salisbury con Novichok por la inteligencia militar rusa.'), (2024, 'Sabotajes e incendios encargados por Rusia en depósitos.'), (2025, 'Juicio por espionaje para China en el Parlamento, luego archivado.')])
B('Ireland', 'Las sedes europeas de las tecnológicas de EE.UU. y su régimen fiscal.', [(2025, 'Amenaza de EE.UU. de repatriar inversiones farmacéuticas con aranceles.')],
  'Ninguno central; posición neutral.', [(2023, 'Buques rusos merodean sus cables submarinos.')])
B('France', 'Que su autonomía estratégica no divida a la OTAN; su peso nuclear y africano.',
  [(2021, 'AUKUS le hace perder el contrato de submarinos con Australia.'), (2025, 'Aranceles de EE.UU. a la UE.')],
  'Debilitarla en África y dividir su opinión pública.',
  [(2022, 'Wagner y la propaganda rusa la expulsan de Malí.'), (2023, 'Salida de Burkina Faso y Níger.'), (2024, 'Campañas de desinformación rusas antes de los Juegos Olímpicos.')])
B('Germany', 'El rearme, el corte del gas ruso y menos dependencia de China.',
  [(2022, 'EE.UU. presiona contra el Nord Stream 2, saboteado ese año.'), (2024, 'Acuerdo para desplegar misiles estadounidenses de largo alcance desde 2026.'), (2025, 'Aranceles a sus autos.')],
  'Su mercado e industria: el gas ruso antes y China como cliente y competidor.',
  [(2021, 'Termina el Nord Stream 2.'), (2022, 'Rusia corta el gas.'), (2024, 'Complot ruso para asesinar al jefe de Rheinmetall, desbaratado.'), (2024, 'Detenidos por espiar para China.')])
B('Italy', 'Su lugar en la OTAN y el Mediterráneo, y sacarla de la Franja y la Ruta.', [(2023, 'Italia abandona la Franja y la Ruta.')],
  'Puertos e infraestructura en el Mediterráneo.', [(2019, 'Primer país del G7 en sumarse a la Franja y la Ruta.'), (2020, 'Misión militar rusa de ayuda por el covid.')])
B('Spain', 'La base de Rota y Morón y el flanco sur.', [(2025, 'Presión de EE.UU. por su negativa a gastar el 5 % del PBI en defensa.')],
  'Inversión e influencia; en el caso ruso, el independentismo catalán.', [(2017, 'Campañas rusas de desinformación sobre el referéndum catalán.'), (2023, 'Visita del jefe de gobierno a China y apertura a fábricas chinas.')])
B('Portugal', 'Las Azores y la base de Lajes.', [(2025, 'Uso de Lajes para el despliegue sobre Irán.')], 'La energía y los puertos.', [(2019, 'Fracasa la oferta de China Three Gorges para controlar EDP.')])
B('Netherlands', 'Que ASML no venda a China las máquinas para chips avanzados.', [(2023, 'Restricciones a la exportación de ASML tras presión de EE.UU.'), (2025, 'Toma del control de Nexperia, de capital chino.')],
  'Tecnología de chips y el puerto de Róterdam.', [(2025, 'China corta los chips de Nexperia en represalia.')])
B('Belgium', 'Las sedes de la OTAN y la UE y el uso de las reservas rusas para Ucrania.', [(2025, 'Presión para usar los activos rusos de Euroclear.')],
  'Recuperar sus reservas inmovilizadas y espiar a la OTAN y la UE.', [(2024, 'Investigación por pagos rusos a eurodiputados vía Voice of Europe.')])
B('Luxembourg', 'Plaza financiera de la UE.', [], 'Mover capital a través de sus fondos.', [])
B('Switzerland', 'Que aplique las sanciones y entregue información fiscal.', [(2022, 'Adopta las sanciones de la UE a Rusia.'), (2025, 'Arancel del 39 % de EE.UU.')],
  'Sus bancos y casas de materias primas para mover capital.', [(2022, 'Traders de petróleo ruso se mudan a Dubái tras las sanciones.')])
B('Austria', 'Que no sea la puerta de la inteligencia rusa en Europa.', [], 'Viena como centro de espionaje y el gas.', [(2024, 'Escándalo del espía austríaco Egisto Ott para Rusia.')])
for k in ['Liechtenstein', 'Monaco', 'San Marino', 'Andorra']:
    B(k, 'Más transparencia financiera.', [], 'Usar sus plazas para guardar fortunas.', [])
B('Vatican', 'Su voz moral sobre Ucrania y China.', [(2025, 'Elección de un papa estadounidense, León XIV.')],
  'Controlar la designación de obispos en China.', [(2018, 'Acuerdo provisional con China sobre los obispos, renovado en 2020, 2022 y 2024.')])
B('Malta', 'Cerrar la venta de pasaportes y el contrabando de petróleo.', [(2025, 'La justicia europea declara ilegal su venta de ciudadanía.')], 'Registro de buques para la flota en la sombra.', [])

# ───────────────────────── Europa del norte ─────────────────────────

B('Denmark', 'Groenlandia, los estrechos del Báltico y el F-35.', [(2025, 'Presión de EE.UU. por Groenlandia.')],
  'Atravesar sus estrechos con la flota en la sombra.', [(2024, 'Petroleros rusos de la flota en la sombra cruzan sus estrechos sin seguro adecuado.')])
B('Norway', 'El gas para Europa y la frontera ártica.', [(2021, 'Acuerdo de bases con EE.UU.')], 'El Ártico y Svalbard.', [(2022, 'Drones sobre plataformas de gas.'), (2024, 'Sabotajes de cables en el mar de Barents.')])
B('Sweden', 'Su ingreso a la OTAN y el Báltico.', [(2024, 'Entra en la OTAN.')], 'Debilitarla en el Báltico.', [(2023, 'Daños a cables en el Báltico por buques chinos y rusos.'), (2024, 'Bandas reclutadas por Irán para atacar objetivos israelíes.')])
B('Finland', 'Su frontera con Rusia, ya en la OTAN.', [(2023, 'Entra en la OTAN; acuerdo de bases con EE.UU.')], 'Presionarla en la frontera.', [(2023, 'Rusia empuja migrantes hacia la frontera; Finlandia la cierra.'), (2024, 'Buque de la flota en la sombra corta el cable Estlink 2.')])
B('Iceland', 'El corredor GIUK y la base de Keflavík.', [(2016, 'Vuelven los aviones antisubmarinos de EE.UU. a Keflavík.')], 'Ninguno relevante.', [])
B('Faeroe Is.', 'Ninguno particular.', [], 'Pesca con Rusia.', [(2022, 'Mantiene su acuerdo pesquero con Rusia pese a las sanciones.')])
B('Åland', 'Ninguno particular.', [], 'Que siga desmilitarizada.', [])

# ───────────────────────── Europa central y oriental ─────────────────────────

B('Poland', 'El frente oriental de la OTAN.', [(2017, 'Llegan tropas de la OTAN y de EE.UU.'), (2023, 'Compra de tanques Abrams, Patriot y HIMARS.')],
  'Desestabilizarla y frenar la ayuda a Ucrania.', [(2021, 'Bielorrusia empuja migrantes a su frontera.'), (2024, 'Sabotajes e incendios encargados por Rusia.'), (2025, 'Drones rusos sobre su territorio; la OTAN los derriba.')])
B('Czechia', 'Que siga en la línea de Ucrania.', [(2024, 'Coordina la compra de municiones para Ucrania.')], 'Debilitar su apoyo a Ucrania.', [(2021, 'Expulsa a diplomáticos rusos por la explosión de Vrbětice en 2014.'), (2024, 'Desbarata la red de propaganda Voice of Europe.')])
B('Slovakia', 'Que no rompa el frente de la UE.', [], 'Un aliado dentro de la UE.', [(2023, 'Gobierno favorable a Moscú que corta la ayuda militar a Ucrania.')])
B('Hungary', 'Su vuelta a la línea común de la UE y la OTAN.', [(2026, 'Respaldo al nuevo gobierno.')], 'Un caballo de Troya dentro de la UE.', [(2023, 'Fábricas chinas de baterías (CATL).'), (2024, 'Bloqueos a la ayuda europea a Ucrania.'), (2026, 'Pierde a su aliado tras la derrota de Orbán.')])
B('Slovenia', 'Ninguno particular.', [], 'Ninguno relevante.', [])
B('Croatia', 'La terminal de gas de Krk como alternativa al gas ruso.', [(2021, 'Inauguración de Krk con apoyo de EE.UU.')], 'Ninguno relevante.', [])
B('Romania', 'La base del mar Negro y el escudo antimisiles.', [(2016, 'Activa el escudo antimisiles de Deveselu.'), (2024, 'Ampliación de la base de Mihail Kogălniceanu.')],
  'Influir en sus elecciones.', [(2024, 'Anulación de la elección presidencial por una campaña en TikTok atribuida a Rusia.')])
B('Bulgaria', 'Cortar su dependencia energética rusa.', [(2022, 'Corta el gas ruso.')], 'Su energía y su política interna.', [(2022, 'Rusia corta el gas.'), (2020, 'La fiscalía vincula explosiones en depósitos de armas con la inteligencia militar rusa.')])
B('Greece', 'Las bases de Souda y Alexandroupolis.', [(2019, 'Acuerdo de defensa ampliado con EE.UU.')], 'El puerto del Pireo como puerta a Europa.', [(2016, 'COSCO compra el control del puerto del Pireo.')])
B('Cyprus', 'Sacar de su banca el dinero ruso y usarlo como plataforma regional.', [(2022, 'EE.UU. levanta el embargo de armas.'), (2023, 'Sanciones a empresas chipriotas de servicios a oligarcas rusos.')],
  'Su banca y sus empresas pantalla.', [(2020, 'Al Jazeera revela la venta de pasaportes a personas cuestionadas.')])
B('N. Cyprus', 'Ninguno particular.', [], 'Universidades y bancos que sirven a capitales rusos e iraníes.', [])
for k, x in [('Estonia', 'ciberataques y sabotajes de cables.'), ('Latvia', 'presión sobre la minoría rusa y la frontera.')]:
    B(k, 'El frente báltico de la OTAN.', [(2017, 'Despliegue de batallones de la OTAN.'), (2025, 'Brigada alemana permanente en Lituania.')], 'Presionarlo: ' + x,
      [(2024, 'Interferencia del GPS sobre el Báltico.'), (2024, 'Cables submarinos cortados por buques que salieron de puertos rusos.')])
B('Lithuania', 'El frente báltico de la OTAN.', [(2017, 'Despliegue de batallones de la OTAN.'), (2025, 'Brigada alemana permanente en Lituania.')],
  'Kaliningrado, Bielorrusia y castigar su apoyo a Taiwán.', [(2021, 'China le corta el comercio por la oficina de Taiwán en Vilna.'), (2025, 'Globos desde Bielorrusia cierran el aeropuerto de Vilna.')])

# ───────────────────────── Balcanes ─────────────────────────

B('Albania', 'Su papel en la OTAN y la cooperación contra la mafia.', [(2024, 'Base aérea de Kuçova de la OTAN.')], 'Ninguno relevante.', [(2022, 'Ciberataque iraní contra el gobierno: rompe relaciones con Irán.')])
B('Macedonia', 'Que siga en la OTAN.', [(2020, 'Entra en la OTAN.')], 'Frenar su integración occidental.', [(2018, 'Campañas rusas contra el acuerdo de Prespa.')])
B('Montenegro', 'Que siga en la OTAN.', [(2017, 'Entra en la OTAN.')], 'Recuperar influencia.', [(2016, 'Intento de golpe atribuido a la inteligencia militar rusa (condenas en 2019, anuladas luego).'), (2021, 'Deuda china por la autopista.')])
B('Bosnia and Herz.', 'Preservar Dayton y frenar el secesionismo serbio.', [(2022, 'Sanciones de EE.UU. a Dodik.'), (2025, 'EE.UU. levanta las sanciones a Dodik y su entorno.')],
  'Usar la República Srpska como palanca en los Balcanes.', [(2018, 'Rusia respalda a Dodik y entrena a la policía serbobosnia.')])
B('Serbia', 'Alejarla de Rusia y China y acercarla a la UE.', [(2024, 'Acuerdo de litio con la UE.'), (2025, 'Sanciones de EE.UU. a la petrolera NIS, de capital ruso.')],
  'Su principal aliado en los Balcanes.', [(2016, 'China compra la acería de Smederevo y luego la mina de Bor.'), (2022, 'Le vende defensa antiaérea HQ-22.'), (2024, 'Visita de Xi Jinping.')])
B('Kosovo', 'La base de Bondsteel y la KFOR.', [(2023, 'Refuerzo de la KFOR tras Banjska.')], 'Impedir su reconocimiento.', [(2023, 'Rusia y China bloquean su ingreso a organismos internacionales.')])

for k in ['Jersey', 'Guernsey', 'Isle of Man']:
    B(k, 'Más transparencia financiera.', [(2016, 'Papeles de Panamá y presión por registros de beneficiarios.')], 'Usar sus plazas para guardar fortunas.', [])

# ───────────────────────── Rusia y su periferia ─────────────────────────

B('Russia', 'Debilitarla, cortarle la renta energética y evitar su alianza plena con China.',
  [(2022, 'Sanciones masivas e inmovilización de las reservas del banco central.'), (2024, 'Uso de las rentas de los activos rusos para Ucrania.'), (2025, 'Sanciones a Rosneft y Lukoil.')],
  'Es uno de los centros de la alianza: sostener su guerra y su economía.',
  [(2019, 'Gasoducto Fuerza de Siberia hacia China.'), (2022, 'Amistad «sin límites» con China.'), (2023, 'Irán y Corea del Norte le venden drones y municiones.'), (2024, 'Tropas norcoreanas en Kursk.')])
B('Ukraine', 'Que no caiga, que Rusia no gane, y sus minerales.',
  [(2022, 'Ayuda militar y financiera masiva de EE.UU. y Europa.'), (2025, 'Acuerdo de minerales con EE.UU. y presión para negociar.')],
  'Rusia: anexarla o neutralizarla; China: sostener a Rusia sin entrar en la guerra.',
  [(2022, 'Invasión rusa a gran escala.'), (2023, 'China provee componentes de uso dual a Rusia.'), (2023, 'Drones iraníes Shahed contra ciudades ucranianas.'), (2024, 'Tropas norcoreanas.')])
B('Belarus', 'Separarla de Rusia o, al menos, sacar presos políticos.', [(2021, 'Sanciones tras el desvío del avión de Ryanair.'), (2025, 'EE.UU. obtiene liberaciones de presos y levanta sanciones a Belavia.')],
  'Integrarla militarmente a Rusia.', [(2022, 'Plataforma de la invasión a Ucrania.'), (2023, 'Despliegue de armas nucleares tácticas rusas.')])
B('Moldova', 'Su camino a la UE.', [(2022, 'Candidata a la UE con apoyo financiero europeo.')], 'Mantenerla en la órbita rusa.',
  [(2022, 'Corte de gas y apagones.'), (2024, 'Compra de votos financiada desde Rusia en el referéndum europeo.'), (2025, 'Redes de compra de votos en las legislativas.')])
B('Georgia', 'Sacarla de la deriva prorrusa.', [(2024, 'EE.UU. suspende la cooperación estratégica y sanciona a su hombre fuerte.')], 'Mantenerla fuera de la OTAN y la UE.', [(2024, 'Ley de agentes extranjeros, al estilo ruso.'), (2024, 'China construye el puerto de Anaklia.')])
B('Armenia', 'Sacarla de la órbita rusa y abrir el corredor hacia Asia central.', [(2025, 'Acuerdo de paz en Washington y corredor «Trump» por Syunik.')],
  'Mantener la base rusa de Gyumri y su dependencia.', [(2023, 'Rusia no la defiende en Karabaj; Armenia congela su participación en la OTSC.')])
B('Azerbaijan', 'Gas para Europa y un socio entre Rusia e Irán.', [(2025, 'EE.UU. levanta la restricción a la ayuda militar.')],
  'Rusia: retener influencia; Irán: frenar el corredor.', [(2024, 'Rusia derriba por error un avión de Azerbaijan Airlines.'), (2025, 'Choque diplomático con Rusia.')])

# ───────────────────────── Asia central ─────────────────────────

B('Kazakhstan', 'Uranio, petróleo y el corredor transcaspio que evita a Rusia.', [(2025, 'Acuerdos de minerales críticos y compra de aviones con EE.UU.; se suma a los Acuerdos de Abraham.')],
  'Rusia: su retaguardia; China: tránsito y energía.', [(2022, 'Tropas de la OTSC sofocan la revuelta de enero.'), (2023, 'China construye un segundo ferrocarril fronterizo.')])
B('Uzbekistan', 'Minerales críticos y un socio que evite a Rusia.', [(2025, 'Acuerdos de minerales con EE.UU.')], 'Rusia: migrantes y energía; China: inversión.', [(2023, 'Rusia le envía gas por primera vez.')])
B('Kyrgyzstan', 'Frenar la evasión de sanciones.', [(2024, 'EE.UU. sanciona bancos kirguises.')], 'Base aérea rusa de Kant y reexportación de bienes a Rusia.', [(2023, 'Récord de reexportaciones hacia Rusia.')])
B('Tajikistan', 'Frontera con Afganistán.', [], 'Base militar rusa 201 y presencia china en la frontera afgana.', [(2019, 'La prensa revela un puesto militar chino en el Pamir.')])
B('Turkmenistan', 'Gas por el Caspio.', [], 'China: su gas.', [(2022, 'China sigue siendo casi el único comprador de su gas.')])
B('Mongolia', 'Un «tercer vecino» democrático.', [(2023, 'Acuerdo de cielos abiertos y minerales con EE.UU.')], 'Rusia y China: tránsito y minería.', [(2024, 'Recibe a Putin pese a la orden de la Corte Penal Internacional.')])
B('Afghanistan', 'Contener al Estado Islámico-Khorasan y recuperar la base de Bagram.', [(2021, 'Retirada de EE.UU.'), (2025, 'EE.UU. pide la devolución de Bagram.')],
  'Minerales y estabilidad en sus fronteras.', [(2023, 'Contrato petrolero chino en Amu Daria.'), (2025, 'Rusia reconoce al gobierno talibán.')])

# ───────────────────────── Turquía y Medio Oriente ─────────────────────────

B('Turkey', 'Mantenerla en la OTAN y controlando los estrechos.', [(2019, 'Expulsada del programa F-35 por comprar los S-400 rusos.'), (2020, 'Sanciones CAATSA.'), (2024, 'Aprueba la venta de F-16 tras el ingreso de Suecia a la OTAN.')],
  'Alejarla de la OTAN y usarla para evadir sanciones.', [(2019, 'Compra el sistema antiaéreo S-400.'), (2023, 'Rusia construye la central nuclear de Akkuyu.'), (2022, 'Récord de comercio con Rusia.')])
B('Israel', 'Su principal aliado en la región: la seguridad frente a Irán y los Acuerdos de Abraham.',
  [(2018, 'Traslado de la embajada de EE.UU. a Jerusalén.'), (2020, 'Acuerdos de Abraham.'), (2023, 'Apoyo militar masivo en la guerra de Gaza.'), (2025, 'Bombardeo de EE.UU. a instalaciones nucleares iraníes.')],
  'Irán: destruirlo o desgastarlo; China: comercio y puertos.', [(2021, 'China opera el puerto de Haifa.'), (2023, 'Ataque de Hamás, apoyado por Irán.'), (2024, 'Ataques directos de misiles iraníes.')])
B('Palestine', 'Contener a Hamás y normalizar la región con Israel.', [(2018, 'Corta la ayuda a la UNRWA.'), (2025, 'Plan de paz de EE.UU. para Gaza.')],
  'Usar la causa palestina contra Israel y Occidente.', [(2023, 'Irán arma y financia a Hamás y la Yihad Islámica.'), (2024, 'China reúne a Hamás y Fatah en Pekín.')])
B('Lebanon', 'Desarmar a Hezbolá y sostener al ejército libanés.', [(2024, 'Alto el fuego mediado por EE.UU. y Francia.'), (2025, 'Presión para el desarme de Hezbolá.')],
  'Irán: mantener a Hezbolá como su brazo armado.', [(2016, 'Hezbolá impone su candidato presidencial.'), (2024, 'Guerra con Israel: muere Nasralá.')])
B('Syria', 'Integrar al nuevo gobierno, contener al Estado Islámico y proteger a los kurdos.', [(2019, 'Muerte de al-Baghdadi.'), (2025, 'Levanta las sanciones y recibe a al-Sharaa en Washington.')],
  'Rusia: sus bases de Tartús y Hmeimim; Irán: el corredor hacia Hezbolá.', [(2016, 'Rusia y el régimen toman Alepo.'), (2024, 'Caída de Asad; Irán pierde su corredor.'), (2025, 'Rusia negocia mantener sus bases.')])
B('Jordan', 'Un aliado estable y bases para la región.', [(2021, 'Acuerdo de defensa con EE.UU.'), (2024, 'Derriba drones iraníes sobre su territorio.')], 'Contrabando de armas y captagón por su frontera.', [(2024, 'Redes ligadas a Irán intentan pasar armas a Cisjordania.')])
B('Iraq', 'Contener a Irán y al Estado Islámico.', [(2020, 'EE.UU. mata a Soleimani en Bagdad.'), (2024, 'Acuerdo para el fin de la misión de la coalición en 2026.')],
  'Irán: controlar su gobierno y sus milicias; China: petróleo.', [(2019, 'Acuerdo «petróleo por infraestructura» con China.'), (2024, 'Milicias proiraníes atacan bases de EE.UU.')])
B('Iran', 'Impedir que tenga armas nucleares y desarmar su red regional, o cambiar el régimen.',
  [(2018, 'EE.UU. abandona el acuerdo nuclear y aplica «máxima presión».'), (2020, 'Muerte de Soleimani.'), (2025, 'Bombardeo de Fordow, Natanz e Isfahán.'), (2026, 'Guerra abierta con EE.UU. e Israel.')],
  'Es uno de los socios de la alianza: China compra su petróleo y Rusia su armamento.', [(2021, 'Acuerdo de cooperación de 25 años con China.'), (2023, 'Ingresa a la OCS y a los BRICS.'), (2025, 'Tratado de asociación estratégica con Rusia.')])
B('Saudi Arabia', 'El petróleo en dólares, las compras de armas y la normalización con Israel.', [(2017, 'Paquete de armas de 110.000 millones.'), (2025, 'Acuerdos de inversión y defensa por cientos de miles de millones.')],
  'China: su petróleo y su ingreso a los BRICS.', [(2023, 'China media su reconciliación con Irán.'), (2023, 'Invitada a los BRICS.')])
B('United Arab Emirates', 'Defensa, inteligencia artificial y los Acuerdos de Abraham.', [(2020, 'Acuerdos de Abraham.'), (2025, 'Acuerdo de chips e inteligencia artificial con EE.UU.')],
  'Dubái como plaza para el capital ruso y el comercio con Irán.', [(2022, 'Llegan fortunas y traders rusos.'), (2021, 'EE.UU. detecta una instalación china en el puerto de Jalifa.')])
B('Qatar', 'La base de Al Udeid y su mediación.', [(2022, 'Designado aliado principal no miembro de la OTAN.'), (2025, 'Garantía de seguridad de EE.UU. tras el ataque israelí.')],
  'Gas para China.', [(2022, 'Contrato de gas de 27 años con Sinopec.'), (2025, 'Irán ataca Al Udeid en represalia por los bombardeos de EE.UU.')])
B('Bahrain', 'La base de la Quinta Flota.', [(2023, 'Acuerdo de seguridad integral con EE.UU.')], 'Irán: la mayoría chií.', [])
B('Kuwait', 'Bases de EE.UU.', [], 'Ninguno central.', [])
B('Oman', 'Su mediación y el acceso a sus puertos.', [(2019, 'Acuerdo de acceso a los puertos de Duqm y Salalah.')], 'Su mediación con Irán.', [(2025, 'Media en las negociaciones nucleares entre Irán y EE.UU.')])
B('Yemen', 'Que los hutíes no cierren el mar Rojo.', [(2024, 'Operación Guardián de la Prosperidad y bombardeos.'), (2025, 'Campaña aérea de EE.UU. y tregua en mayo.')],
  'Irán: usar a los hutíes contra Israel y el tráfico marítimo.', [(2019, 'Ataque con drones a Abqaiq, atribuido a Irán.'), (2023, 'Ataques hutíes en el mar Rojo con armas iraníes.')])
B('Egypt', 'Estabilidad, el canal de Suez y la paz con Israel.', [(2023, 'Mantiene los 1.300 millones anuales de ayuda militar.')],
  'Canal de Suez y su nueva capital: China construye; Rusia, su central nuclear.', [(2017, 'Rusia acuerda la central nuclear de El Dabaa.'), (2023, 'Invitado a los BRICS.')])

# ───────────────────────── Asia del Sur ─────────────────────────

B('India', 'Un contrapeso a China (Quad) y un mercado para sus armas y tecnología.', [(2017, 'Relanzamiento del Quad.'), (2023, 'Acuerdo de motores de caza y tecnología crítica.'), (2025, 'Aranceles del 50 % por comprarle petróleo a Rusia.')],
  'Rusia: armas y petróleo; China: frenarla en el Himalaya.', [(2020, 'Choque en Galwan con soldados chinos.'), (2022, 'Récord de compras de petróleo ruso.'), (2024, 'Acuerdo de patrullaje fronterizo con China.')])
B('Pakistan', 'Contraterrorismo y alejarlo de China.', [(2025, 'Acercamiento con EE.UU. por minerales y criptomonedas.')], 'China: su principal aliado militar y el corredor CPEC hasta Gwadar.',
  [(2017, 'Avanzan las obras del Corredor Económico China-Pakistán y el puerto de Gwadar.'), (2025, 'Usa cazas chinos J-10 contra India.')])
B('Bangladesh', 'Un socio en el golfo de Bengala.', [], 'China: puertos e infraestructura.', [(2016, 'Visita de Xi y créditos por 24.000 millones.'), (2017, 'Le compra submarinos.')])
B('Sri Lanka', 'Frenar la presencia naval china.', [], 'China: Hambantota y Colombo Port City.', [(2017, 'Cede Hambantota a China por 99 años.'), (2022, 'Polémica por la escala de un buque espía chino.')])
B('Nepal', 'Equilibrar a China.', [(2022, 'Ratifica el programa estadounidense Millennium Challenge.')], 'China: tránsito y la Franja y la Ruta.', [(2017, 'Se suma a la Franja y la Ruta.')])
B('Bhutan', 'Ninguno particular.', [], 'China: su frontera.', [(2017, 'Choque de Doklam entre India y China en territorio que reclama Bután.')])
B('Maldives', 'Seguridad marítima en el Índico.', [], 'China: inversión e influencia.', [(2017, 'Tratado de libre comercio con China.'), (2024, 'Acuerdo militar con China.')])
B('Siachen Glacier', 'Ninguno particular.', [], 'Ninguno directo; la zona limita con territorio en disputa con China.', [])

# ───────────────────────── Sudeste asiático ─────────────────────────

B('Myanmar', 'Contener a la junta y cortar el narcotráfico y las estafas.', [(2021, 'Sanciones tras el golpe.'), (2025, 'Sanciones a redes de estafas en la frontera.')],
  'China: tierras raras, gasoductos y salida al Índico; Rusia: armas.', [(2021, 'Rusia le vende aviones y armas.'), (2025, 'China presiona a las guerrillas para que devuelvan Lashio a la junta.')])
B('Thailand', 'Un aliado tratado en la región.', [(2025, 'Mediación de EE.UU. para el alto el fuego con Camboya.')], 'China: tren y submarinos.', [(2017, 'Compra un submarino chino.'), (2025, 'Deporta uigures a China.')])
B('Laos', 'Ninguno central.', [], 'China: el tren y su deuda.', [(2021, 'Tren Kunming-Vientián.')])
B('Cambodia', 'Que no se convierta en base china.', [(2021, 'Sanciones por la base de Ream.')], 'China: la base naval de Ream.', [(2025, 'Inauguración de la base de Ream renovada por China.')])
B('Vietnam', 'Un socio frente a China.', [(2023, 'Asociación estratégica integral con EE.UU.')], 'China: controlar el mar; Rusia: armas.', [(2019, 'Choque por Vanguard Bank.'), (2024, 'Visita de Putin a Hanói.')])
B('Malaysia', 'El estrecho de Malaca y los chips.', [], 'China: inversión y presión en el mar de China.', [(2016, 'Grandes proyectos chinos, renegociados en 2019.')])
B('Singapore', 'El acceso naval y su plaza financiera.', [(2019, 'Renovación del acuerdo de acceso militar con EE.UU.')], 'Plaza para el capital chino.', [(2023, 'Escándalo de lavado de 2.000 millones de redes chinas.')])
B('Indonesia', 'Los estrechos y el níquel fuera del dominio chino.', [(2023, 'Asociación estratégica integral con EE.UU.')], 'China: níquel y el tren rápido.', [(2023, 'Inauguración del tren Yakarta-Bandung, construido por China.'), (2025, 'Ingresa a los BRICS.')])
B('Brunei', 'Ninguno central.', [], 'Reclamos en el mar de China Meridional.', [])
B('Philippines', 'Bases frente a Taiwán y al mar de China Meridional.', [(2023, 'Cuatro bases nuevas para EE.UU.'), (2024, 'Despliegue del misil Typhon.')],
  'China: imponer su control sobre los arrecifes.', [(2016, 'China desconoce el fallo arbitral.'), (2023, 'Embestidas y cañones de agua contra buques filipinos.')])
B('Timor-Leste', 'Ninguno central; Australia cuida su seguridad.', [], 'China: infraestructura.', [])

# ───────────────────────── Asia oriental ─────────────────────────

B('China', 'Frenar su ascenso militar y tecnológico sin una guerra.', [(2018, 'Guerra comercial.'), (2022, 'Controles a los chips avanzados.'), (2025, 'Aranceles de hasta el 145 % y tregua posterior.')],
  'Es el otro centro de la alianza.', [(2022, 'Amistad «sin límites» con Rusia.'), (2023, 'Media entre Arabia Saudita e Irán.'), (2025, 'Controles a la exportación de tierras raras.')])
B('Hong Kong', 'Su autonomía y su plaza financiera.', [(2020, 'Fin del trato especial y sanciones a funcionarios.')], 'Control total por Pekín.', [(2020, 'Ley de seguridad nacional.')])
B('Macao', 'Ninguno central.', [], 'Control total por Pekín.', [])
B('Taiwan', 'Sus chips y que no caiga en manos de China.', [(2022, 'Visita de Pelosi.'), (2024, 'Fábrica de TSMC en Arizona.'), (2025, 'Ventas de armas y presión para gastar más en defensa.')],
  'China: la reunificación, por las buenas o por la fuerza.', [(2022, 'Maniobras de bloqueo.'), (2024, 'Ejercicios Joint Sword.'), (2025, 'Ejercicios Strait Thunder.')])
B('Japan', 'Su rearme y las bases de Okinawa.', [(2022, 'Nueva estrategia de seguridad y duplicación del gasto.'), (2023, 'Acuerdo de Camp David con Corea del Sur.')],
  'China: las islas Senkaku; Rusia: las Kuriles.', [(2023, 'Récord de incursiones chinas cerca de las Senkaku.'), (2024, 'Primera incursión de un avión militar chino en su espacio aéreo.')])
B('South Korea', 'Su alianza frente a Corea del Norte y sus chips y astilleros.', [(2016, 'Despliegue del escudo THAAD.'), (2023, 'Declaración de Washington sobre disuasión nuclear.'), (2025, 'Acuerdo de inversión para astilleros en EE.UU.')],
  'China: frenar su alianza con EE.UU.', [(2017, 'Boicot chino por el THAAD.')])
B('North Korea', 'Desnuclearizarla o contenerla.', [(2018, 'Cumbre de Singapur.'), (2019, 'Cumbre de Hanói, sin acuerdo.')], 'Rusia: soldados y municiones; China: su supervivencia.', [(2023, 'Le vende municiones a Rusia.'), (2024, 'Tratado de defensa con Rusia y tropas en Kursk.')])

# ───────────────────────── Oceanía ─────────────────────────

B('Australia', 'Base aliada en el Indo-Pacífico (AUKUS).', [(2021, 'Pacto AUKUS.'), (2023, 'Más rotaciones de tropas de EE.UU. en Darwin.')],
  'China: sus minerales y presionarla.', [(2020, 'Castigo comercial de China (vino, cebada, carbón).'), (2025, 'Flotilla naval china con ejercicios de tiro en el mar de Tasmania.')])
B('New Zealand', 'Cinco Ojos y el Pacífico.', [(2024, 'Se abre a sumarse al pilar 2 de AUKUS.')], 'Influencia china.', [])
B('Papua New Guinea', 'Bases y un aliado en el Pacífico.', [(2023, 'Acuerdo de defensa con EE.UU.'), (2025, 'Tratado de defensa con Australia.')], 'China: minería e infraestructura.', [])
B('Solomon Is.', 'Revertir la entrada china.', [], 'China: presencia policial y de seguridad.', [(2019, 'Reconoce a China.'), (2022, 'Pacto de seguridad con China.')])
B('Fiji', 'Un socio en el Pacífico.', [], 'China: cooperación policial.', [])
B('Vanuatu', 'Seguridad con Australia.', [], 'China: infraestructura.', [])
B('Samoa', 'Ninguno central.', [], 'Influencia china.', [(2021, 'Se cancela un puerto con financiamiento chino.')])
B('Tonga', 'Ninguno central.', [], 'Deuda con China.', [])
B('Kiribati', 'Ninguno central.', [], 'China: presencia policial y la pista de la isla Kanton.', [(2019, 'Reconoce a China.')])
B('Nauru', 'Seguridad con Australia.', [(2024, 'Tratado de seguridad con Australia.')], 'Reconocimiento.', [(2024, 'Reconoce a China.')])
for k in ['Micronesia', 'Marshall Is.', 'Palau']:
    B(k, 'Acceso militar exclusivo de EE.UU. y negar el área a China.', [(2023, 'Renovación del Pacto de Libre Asociación.')], 'Desplazar a EE.UU.', [])
for k in ['Guam', 'N. Mariana Is.']:
    B(k, 'Base avanzada frente a China.', [(2023, 'Nueva base de marines en Guam.')], 'Objetivo militar en caso de guerra.', [(2023, 'Malware chino Volt Typhoon en su infraestructura.')])
B('American Samoa', 'Ninguno particular.', [], 'Ninguno relevante.', [])
B('Cook Is.', 'Que no se aleje de Nueva Zelanda.', [(2025, 'Nueva Zelanda congela su ayuda tras el acuerdo con China.')], 'Minerales del lecho marino.', [(2025, 'Acuerdo de cooperación con China.')])
B('Niue', 'Ninguno particular.', [], 'Ninguno relevante.', [])
B('Fr. Polynesia', 'Ninguno particular: territorio de Francia.', [], 'Ninguno relevante.', [])
B('New Caledonia', 'Que siga francesa y el níquel.', [], 'Ninguno relevante.', [])
for k in ['Wallis and Futuna Is.', 'Pitcairn Is.', 'Norfolk Island', 'Heard I. and McDonald Is.', 'Ashmore and Cartier Is.']:
    B(k, 'Ninguno particular.', [], 'Ninguno relevante.', [])
B('Indian Ocean Ter.', 'Vigilancia en el Índico.', [(2023, 'Ampliación de la pista de las islas Cocos.')], 'Ninguno relevante.', [])

# ───────────────────────── África del Norte ─────────────────────────

B('Morocco', 'Un aliado estable, puerta de África y socio de Israel.', [(2020, 'EE.UU. reconoce su soberanía sobre el Sahara.'), (2025, 'Resolución de la ONU que respalda su plan de autonomía.')],
  'China: fábricas de baterías e infraestructura.', [(2024, 'Inversiones chinas en baterías para autos eléctricos.')])
B('W. Sahara', 'Que quede bajo soberanía marroquí con autonomía.', [(2020, 'Reconocimiento estadounidense de la soberanía marroquí.')], 'Argelia y Rusia: sostener al Polisario en la ONU.', [])
B('Algeria', 'Gas para Europa y alejarla de Rusia.', [(2022, 'Italia y España aumentan sus compras de gas argelino.')], 'Rusia: su principal proveedor de armas.', [(2023, 'Pide su ingreso a los BRICS (rechazado).')])
B('Tunisia', 'Contener la migración.', [(2023, 'Acuerdo migratorio con la UE.')], 'Influencia rusa y china en el giro del gobierno.', [])
B('Libya', 'Petróleo y frenar a Rusia en el flanco sur.', [], 'Rusia: bases para proyectarse a África.', [(2019, 'Wagner apoya la ofensiva de Haftar sobre Trípoli.'), (2024, 'Rusia traslada equipos de Siria a bases libias.')])
B('Mauritania', 'Un aliado estable frente al Sahel.', [], 'Pesca china.', [])

# ───────────────────────── Sahel y África occidental ─────────────────────────

B('Mali', 'Frenar el yihadismo y la presencia rusa.', [(2022, 'Se van Francia y la misión de la ONU.')], 'Rusia: oro y presencia militar.', [(2021, 'Llega Wagner.'), (2024, 'Wagner sufre una derrota en Tinzaouaten.'), (2025, 'El Africa Corps reemplaza a Wagner.')])
B('Burkina Faso', 'Frenar el yihadismo y la presencia rusa.', [(2023, 'Salen las tropas francesas.')], 'Rusia: minas de oro y propaganda.', [(2023, 'Llegan instructores rusos.'), (2024, 'Rusia construye una planta de refinado de oro.')])
B('Niger', 'Vigilancia del Sahel y uranio.', [(2024, 'EE.UU. pierde la base de drones de Agadez.')], 'Rusia: uranio y presencia; China: petróleo.', [(2024, 'Llegan instructores rusos.'), (2024, 'Oleoducto chino hacia Benín.')])
B('Chad', 'Que no se pase a Rusia.', [(2025, 'Se van las tropas francesas.')], 'Rusia: presencia militar.', [(2024, 'Acercamiento con Moscú.')])
B('Senegal', 'Su petróleo y gas.', [], 'Ninguno central.', [])
B('Gambia', 'Ninguno central.', [], 'Ninguno relevante.', [])
B('Guinea-Bissau', 'Cortar la ruta de la cocaína.', [], 'Ninguno relevante.', [])
B('Guinea', 'Bauxita y hierro fuera del control chino.', [], 'China: Simandou y la bauxita.', [(2025, 'Primer embarque de hierro de Simandou, con capital chino.')])
B('Sierra Leone', 'Ninguno central.', [], 'China: minería.', [])
B('Liberia', 'Su registro de buques y la estabilidad.', [], 'Ninguno relevante.', [])
B("Côte d'Ivoire", 'Un aliado estable en el golfo de Guinea.', [], 'Ninguno central.', [])
B('Ghana', 'Oro, cacao y democracia estable.', [], 'China: bauxita y minería ilegal de ciudadanos chinos.', [(2023, 'Detenciones de mineros chinos ilegales.')])
B('Togo', 'Seguridad del norte.', [], 'Rusia: acercamiento militar.', [(2025, 'Acuerdo militar con Rusia.')])
B('Benin', 'Contener el yihadismo.', [], 'China: oleoducto de Níger.', [])
B('Nigeria', 'Su peso regional y el combate a los yihadistas.', [(2025, 'EE.UU. lo designa «país de especial preocupación» por la violencia contra cristianos.')], 'China: infraestructura y deuda.', [(2023, 'Refinería y ferrocarriles con capital chino.')])
B('Cabo Verde', 'Su posición atlántica.', [], 'Ninguno relevante.', [])

# ───────────────────────── África central ─────────────────────────

B('Cameroon', 'Contener a Boko Haram.', [], 'China: puerto de Kribi.', [])
B('Central African Rep.', 'Que no quede bajo control ruso.', [], 'Rusia: minas a cambio de seguridad.', [(2018, 'Llegan Wagner y los instructores rusos.'), (2023, 'Wagner sigue operando tras la muerte de Prigozhin.')])
B('Gabon', 'Estabilidad tras el golpe.', [], 'Ninguno central.', [])
B('Eq. Guinea', 'Que no haya base naval china en el Atlántico.', [(2021, 'EE.UU. presiona contra una base china en Bata.')], 'China: base naval en el Atlántico.', [])
B('São Tomé and Principe', 'Ninguno central.', [], 'Ninguno relevante.', [])
B('Congo', 'Ninguno central.', [], 'China: petróleo y deuda.', [])
B('Dem. Rep. Congo', 'Cobalto y cobre fuera del control chino y la paz con Ruanda.', [(2025, 'Acuerdo de paz y de minerales con EE.UU. y Ruanda.')], 'China: el cobalto.', [(2016, 'China Molybdenum compra la mina de Tenke.'), (2024, 'Renegociación del contrato minero chino.')])
B('Rwanda', 'Su eficacia y sus tropas de paz.', [(2025, 'Acuerdo con el Congo mediado por EE.UU.')], 'Ninguno central.', [])
B('Burundi', 'Ninguno central.', [], 'China y Rusia: minería.', [])

# ───────────────────────── África oriental y Cuerno ─────────────────────────

B('Sudan', 'Que termine la guerra y frenar la base rusa.', [(2025, 'EE.UU. declara genocidio de las FAR en Darfur.')], 'Rusia: base naval en Port Sudan.', [(2020, 'Acuerdo para una base rusa en Port Sudan.')])
B('S. Sudan', 'Ninguno central.', [], 'China: petróleo.', [])
B('Ethiopia', 'Estabilidad y la gran represa.', [(2021, 'EE.UU. lo saca del AGOA por la guerra de Tigray.')], 'China: deuda e infraestructura.', [(2018, 'Tren Adís Abeba-Yibuti, de capital chino.')])
B('Eritrea', 'Ninguno central.', [], 'Rusia: puerto de Massawa.', [(2023, 'Acercamiento militar con Rusia.')])
B('Djibouti', 'La base de Camp Lemonnier.', [], 'China: su primera base militar en el exterior.', [(2017, 'Base naval china en Yibuti.')])
B('Somalia', 'Combatir a Al Shabaab y al Estado Islámico.', [(2025, 'Bombardeos de EE.UU.')], 'Ninguno central: los actores externos son Turquía y los Emiratos.', [])
B('Somaliland', 'Una base en Berbera.', [], 'Taiwán, no China, es su aliado.', [])
B('Kenya', 'Su aliado principal en África oriental.', [(2024, 'Designado aliado principal no miembro de la OTAN.')], 'China: tren y puerto con deuda.', [(2017, 'Tren Mombasa-Nairobi financiado por China.')])
B('Uganda', 'Ninguno central.', [], 'China: petróleo del lago Alberto.', [])
B('Tanzania', 'Ninguno central.', [], 'China: infraestructura.', [])

# ───────────────────────── África austral ─────────────────────────

B('Angola', 'El corredor de Lobito para sacar minerales sin China.', [(2024, 'Visita de Biden a Lobito.')], 'China: petróleo y deuda.', [])
B('Zambia', 'El cobre y el corredor de Lobito.', [(2023, 'EE.UU. y la UE lanzan el corredor de Lobito.')], 'China: minería y deuda.', [(2023, 'Reestructuración de la deuda con China.')])
B('Zimbabwe', 'Ninguno central.', [], 'China: litio.', [(2022, 'Empresas chinas compran sus principales minas de litio.')])
B('Malawi', 'Ninguno central.', [], 'Ninguno relevante.', [])
B('Mozambique', 'El gas de Cabo Delgado.', [], 'Ninguno central.', [])
B('Madagascar', 'Ninguno central.', [], 'Ninguno relevante.', [])
B('Namibia', 'Uranio y petróleo.', [], 'China: uranio.', [(2016, 'Mina de uranio Husab, de capital chino.')])
B('Botswana', 'Ninguno central.', [], 'Ninguno relevante.', [])
B('South Africa', 'Alejarla de los BRICS.', [(2025, 'EE.UU. expulsa a su embajador y boicotea el G20 de Johannesburgo.')], 'Un socio clave en los BRICS.', [(2023, 'Cumbre de los BRICS en Johannesburgo y ejercicios navales con Rusia y China.')])
B('Lesotho', 'Ninguno central.', [], 'Ninguno relevante.', [])
B('eSwatini', 'Su reconocimiento de Taiwán.', [(2025, 'Recibe deportados desde EE.UU.')], 'Que reconozca a China.', [])
B('Comoros', 'Ninguno central.', [], 'Ninguno relevante.', [])
B('Mauritius', 'La base de Diego García.', [(2025, 'Tratado que le traspasa Chagos con arriendo de la base.')], 'China: influencia en el Índico.', [])
B('Seychelles', 'Seguridad marítima.', [], 'Ninguno relevante.', [])
B('Saint Helena', 'La base de Ascensión.', [], 'Ninguno relevante.', [])
B('Br. Indian Ocean Ter.', 'Conservar Diego García.', [(2025, 'Acuerdo de traspaso a Mauricio con arriendo de 99 años.')], 'Que la base se pierda.', [])
B('Fr. S. Antarctic Lands', 'Ninguno particular.', [], 'Ninguno relevante.', [])


# ═════════════════ Intereses ampliados (reemplazan ti y ei de arriba) ═════════════════

def Q(k, ti, ei):
    PB[k]['ti'] = ti
    PB[k]['ei'] = ei


# América del Norte
Q('United States of America',
  'Es el centro del bloque. Quiere conservar la primacía militar en todos los océanos, el dólar como moneda de reserva y de las sanciones, la delantera en chips, inteligencia artificial y biotecnología, y volver a fabricar en casa lo estratégico. Hacia adentro, cerrar la frontera sur y bajar su dependencia de China en minerales y medicamentos.',
  'China quiere alcanzarlo en tecnología, desplazarlo del Pacífico occidental y restarle peso al dólar. Rusia quiere que se retire de Europa y deje de armar a Ucrania. Irán quiere sacarlo de Medio Oriente. Los tres buscan dividir su opinión pública y explotar su polarización.')
Q('Canada',
  'Mantenerlo dentro de la defensa común de América del Norte (NORAD) y de los Cinco Ojos, que modernice la vigilancia del Ártico y del paso del Noroeste, y que su petróleo, uranio, potasa y minerales críticos abastezcan a EE.UU. y no a China. Que gaste más en defensa y se alinee en comercio con Washington.',
  'China quiere sus minerales y su energía, influir en su gran diáspora y en su política, y acceso a las rutas del Ártico. Rusia disputa el Ártico y la plataforma continental del polo Norte.')
Q('Mexico',
  'Cerrar la frontera al fentanilo, a los cárteles y a la migración irregular; integrarlo como fábrica cercana que reemplace a China (el nearshoring), y que no sea la puerta trasera de productos y capitales chinos al mercado de EE.UU. Que coopere con fuerzas y agencias estadounidenses contra los cárteles.',
  'China quiere usarlo como plataforma industrial para entrar al mercado de EE.UU. sin aranceles y ganar presencia en el vecino de su rival. Rusia busca influir en su opinión pública y mantener canales de inteligencia en la frontera de EE.UU.')
Q('Greenland',
  'Controlar el Ártico occidental: la base espacial de Pituffik, la vigilancia de misiles y submarinos en el corredor entre Groenlandia, Islandia y el Reino Unido, las rutas que abre el deshielo y sus tierras raras y uranio. EE.UU. llegó a plantear comprarla o anexarla.',
  'China quiere minerales e infraestructura (aeropuertos, puertos, minas) y presencia como «Estado cercano al Ártico». Rusia quiere que el Ártico no quede bajo control exclusivo de la OTAN.')
Q('Bermuda', 'Que siga siendo la gran plaza mundial de reaseguros ligada a Londres y Wall Street, y que cumpla los estándares de transparencia e impuesto mínimo de la OCDE.',
  'No tiene intereses relevantes: algún uso de sus vehículos financieros para capitales asiáticos.')
Q('St. Pierre and Miquelon', 'Que Francia conserve sus derechos de pesca y su plataforma marítima frente a Canadá.', 'No tiene intereses relevantes.')

# Centroamérica y Caribe
Q('Guatemala', 'Que frene la migración hacia EE.UU. y acepte deportados, combata el narcotráfico, mantenga el reconocimiento de Taiwán y limpie su justicia de las redes de corrupción.',
  'China quiere que cambie su reconocimiento de Taiwán por el de Pekín, como hicieron sus vecinos, y abrir su mercado e infraestructura.')
Q('Belize', 'Cooperación antinarcóticos en su costa y su frontera, y que siga reconociendo a Taiwán.', 'China quiere que reconozca a Pekín.')
Q('Honduras', 'Conservar la base de Soto Cano, frenar el narcotráfico y la migración, y recuperar su reconocimiento de Taiwán.',
  'China quiere consolidar el cambio de reconocimiento de 2023 con obras y créditos. Rusia y Venezuela buscan gobiernos afines en el istmo.')
Q('El Salvador', 'Un aliado firme: que reciba deportados, mantenga la seguridad sin pandillas, use el dólar y no profundice con China.',
  'China quiere influencia económica tras su reconocimiento de 2018: obras, puertos y préstamos.')
Q('Costa Rica', 'Que frene el paso de la cocaína hacia Europa y EE.UU., excluya a Huawei y a otros proveedores chinos de su 5G y siga siendo plataforma de fábricas de chips y dispositivos médicos estadounidenses.',
  'China quiere comercio, obras y proveedores tecnológicos en un país que la reconoce desde 2007.')
Q('Panama', 'El canal: paso garantizado y prioritario para la marina de EE.UU., sacar a las empresas chinas de los puertos y de las obras del canal, y que Panamá siga fuera de la Franja y la Ruta. Que sus registros de buques y bancos no sirvan para evadir sanciones.',
  'China quiere mantener a sus empresas en la logística, los puertos y las obras del canal, por donde pasa una parte grande de su comercio con América. Irán y Rusia usan su bandera de conveniencia para petroleros sancionados.')
Q('Nicaragua', 'Aislar al régimen de Ortega y Murillo, impedir que aloje presencia militar o de inteligencia rusa o china y frenar su uso como puente migratorio hacia EE.UU.',
  'Rusia quiere un aliado y un punto de apoyo militar y de inteligencia en el istmo. China quiere comercio, el reconocimiento ganado en 2021 y, a futuro, obras. Irán busca cooperación con un régimen aliado.')
Q('Cuba', 'La caída o la transformación del régimen comunista, y que la isla no vuelva a ser base militar o de espionaje de una potencia rival a 150 km de Florida.',
  'China quiere bases de escucha para vigilar a EE.UU. Rusia quiere un aliado histórico donde mostrar buques de guerra. Ambos lo sostienen con petróleo y ayuda para que el régimen no caiga.')
Q('Haiti', 'Contener a las pandillas, que no se vuelva una base del narcotráfico ni una fuente de migración masiva, y que una fuerza internacional, no de EE.UU., cargue con la seguridad.', 'No tiene intereses relevantes.')
Q('Dominican Rep.', 'Mantenerlo como aliado estable y escala para las operaciones en el Caribe, frenar el tránsito de drogas y que no avance la inversión china en puertos y energía.',
  'China quiere comercio, infraestructura y consolidar el reconocimiento de 2018.')
Q('Jamaica', 'Cooperación contra el narcotráfico y las bandas, y frenar la inversión china en infraestructura y bauxita.', 'China quiere su alúmina y bauxita y obras de infraestructura.')
Q('Trinidad and Tobago', 'Usarla como aliada y plataforma frente a Venezuela y asegurar su gas.', 'Venezuela, aliada de la alianza, quería sus acuerdos de gas; China, comercio.')
Q('Bahamas', 'Seguridad marítima frente a la droga y la migración hacia Florida, y control del lavado de dinero en su plaza financiera.', 'China quiere inversión turística e influencia a 80 km de Florida.')
Q('Puerto Rico', 'Usarlo como base aérea y naval para el Caribe y Venezuela, y mantener su estatus de territorio.', 'No tiene intereses relevantes.')
for k in ['Antigua and Barb.', 'Barbados', 'Dominica', 'Grenada', 'St. Kitts and Nevis', 'Saint Lucia', 'St. Vin. and Gren.']:
    Q(k, 'Que su venta de pasaportes no sirva a delincuentes ni a ciudadanos de países sancionados, que coopere contra el narcotráfico y que vote con Occidente en los organismos internacionales.',
      'China quiere sus votos en la ONU y la OEA, alejarlos de Taiwán (algunos todavía lo reconocen) y obras de infraestructura y deuda.')
for k in ['U.S. Virgin Is.', 'Anguilla', 'Montserrat', 'St-Martin', 'St-Barthélemy', 'Sint Maarten']:
    Q(k, 'Mantenerlo como territorio de una potencia del bloque, con controles de lavado y de migración.', 'No tiene intereses relevantes.')
for k in ['Cayman Is.', 'British Virgin Is.', 'Turks and Caicos Is.']:
    Q(k, 'Que siga como plaza extraterritorial ligada a la City y a Wall Street, pero que entregue información sobre los dueños reales de sus sociedades y no sirva para evadir sanciones.',
      'Usar sus sociedades pantalla para mover capital y ocultar dueños: muchas empresas chinas y fortunas rusas están registradas allí.')
for k in ['Aruba', 'Curaçao']:
    Q(k, 'Mantener la base antinarcóticos de EE.UU. y usarlo como punto de vigilancia frente a Venezuela.', 'No tiene intereses relevantes desde la caída de Maduro.')

# Sudamérica
Q('Colombia', 'Su principal aliado militar en Sudamérica: que combata la producción de cocaína, coopere con sus fuerzas armadas, sea socio global de la OTAN, vigile Venezuela y no deje entrar a China en infraestructura sensible.',
  'China quiere obras (el metro de Bogotá), comercio y su ingreso a la Franja y la Ruta. Rusia busca alejarlo de EE.UU. aprovechando choques como los del gobierno de Petro.')
Q('Venezuela', 'Controlar su petróleo y que lo exploten empresas occidentales, sacar a Rusia, China, Irán y Cuba del país, frenar el narcotráfico y la migración, y conducir la transición tras la captura de Maduro.',
  'China quiere cobrar los préstamos pagados con petróleo y no perder su acceso al crudo. Rusia quería una base política y militar en el hemisferio. Irán usaba el país para triangular petróleo y obtener oro. Tras 2026 los tres pierden terreno.')
Q('Ecuador', 'Bases o presencia de seguridad contra las bandas ligadas a los cárteles mexicanos y la mafia albanesa, control de sus puertos y que no dependa de China para su deuda y sus represas.',
  'China quiere cobrar su deuda, mantener sus represas y minas (Mirador) y su tratado de libre comercio. Rusia, comprar banano y camarón.')
Q('Peru', 'Que el puerto chino de Chancay no tenga uso militar, asegurar el cobre y que las empresas occidentales no queden afuera de la minería y la energía.',
  'China quiere Chancay como su puerta al Pacífico sudamericano, el cobre (Las Bambas, Toromocho) y la distribución eléctrica de Lima, que ya compró.')
Q('Bolivia', 'Recuperarlo como socio tras dos décadas de MAS, acceder al litio y frenar la producción de coca.',
  'China y Rusia quieren el litio (contratos de CATL y Uranium One) y un aliado político; Irán buscaba cooperación en drones.')
Q('Chile', 'El cobre y el litio, que la infraestructura crítica (puertos, energía, cables) no quede en manos chinas y su apoyo diplomático.',
  'China, su mayor cliente, quiere cobre, litio, la distribución eléctrica y que Chile siga siendo un socio abierto.')
Q('Argentina', 'Alinearla con Washington, sacar a China de la estación espacial de Neuquén, del swap y de la infraestructura, abrir el litio, el cobre y Vaca Muerta a empresas occidentales, y que se proyecte sobre el Atlántico Sur y la Antártida como aliada.',
  'China quiere soja, carne y litio, mantener la estación espacial y el swap de monedas, puertos y obras. Rusia quiere comprarle granos y venderle tecnología nuclear.')
Q('Uruguay', 'Que el puerto de Montevideo no sea escala de la cocaína y que no firme un tratado comercial con China por fuera del Mercosur.', 'China quiere un tratado de libre comercio, carne y celulosa.')
Q('Paraguay', 'Que siga reconociendo a Taiwán, combatir el contrabando y las redes de Hezbolá en la Triple Frontera.', 'China quiere que reconozca a Pekín, el último gran Estado sudamericano que no lo hace.')
Q('Brazil', 'Evitar que se incline hacia China y Rusia dentro de los BRICS, que no acepte monedas alternativas al dólar, abrir su mercado y sus minerales críticos (tierras raras, niobio) y proteger a sus aliados políticos.',
  'China, su mayor socio, quiere soja, hierro, petróleo y que Brasil sostenga a los BRICS. Rusia le vende fertilizantes y diésel. Ambos quieren que lidere un «Sur global» autónomo de EE.UU.')
Q('Guyana', 'Proteger el petróleo que extrae ExxonMobil y defender a Guyana del reclamo venezolano sobre el Esequibo.', 'China quiere participación en el petróleo (CNOOC es socia) e infraestructura.')
Q('Suriname', 'El petróleo marino que explotan TotalEnergies y otras, y alejarlo de la deuda china.', 'China quiere infraestructura y su deuda.')
Q('Falkland Is.', 'Conservar la base de Mount Pleasant, que proyecta al Reino Unido y a la OTAN sobre el Atlántico Sur, el paso de Drake y la Antártida, y la pesca y el petróleo.', 'No tiene intereses relevantes; China pesca en la milla 201.')
Q('S. Geo. and the Is.', 'La puerta a la Antártida y el control de la pesca.', 'Buques pesqueros chinos operan en la zona.')

# Europa occidental
Q('United Kingdom', 'Su socio militar y de inteligencia más cercano: armas nucleares compartidas, los Cinco Ojos, AUKUS, la City como segunda plaza financiera del bloque y su peso en el apoyo a Ucrania. Que mantenga a Huawei y a China fuera de su infraestructura.',
  'Rusia quiere debilitar su apoyo a Ucrania, usar Londres para mover capital y castigar a desertores. China quiere sus universidades, su tecnología y la City como puerta financiera, e influir en su política.')
Q('Ireland', 'Que siga siendo la sede europea de las tecnológicas y farmacéuticas de EE.UU. y que su régimen fiscal favorezca a esas empresas, aunque se repatrie producción a EE.UU.',
  'Rusia vigila sus cables submarinos, por donde pasa buena parte del tráfico de datos entre Europa y América. China, comercio.')
Q('France', 'Que siga en la OTAN y aporte su arsenal nuclear a la defensa europea, que su «autonomía estratégica» no divida a Occidente y que conserve su presencia en África y el Indo-Pacífico frente a Rusia y China.',
  'Rusia quiere expulsarla de África (lo logró en el Sahel), dividir su sociedad con desinformación y alentar a sus partidos más afines. China quiere su mercado, su tecnología aeronáutica y nuclear, y que frene la línea dura de la UE.')
Q('Germany', 'Que se rearme y sea el pilar convencional de la OTAN en Europa, que no vuelva a depender del gas ruso, que reduzca su exposición industrial a China y que aloje los misiles y las bases de EE.UU. (Ramstein).',
  'Rusia quiere recuperar el negocio del gas, frenar su apoyo a Ucrania y alentar a la ultraderecha y a la izquierda prorrusa. China quiere que sus autos, química y máquinas sigan dependiendo de su mercado, y su tecnología.')
Q('Italy', 'Que siga en la OTAN con sus bases (Sigonella, Aviano, Nápoles), controle el Mediterráneo central y la migración, y se mantenga fuera de la Franja y la Ruta.',
  'China quería sus puertos (Trieste, Génova) y su ingreso a la Franja y la Ruta. Rusia quiere aliados políticos que frenen las sanciones.')
Q('Spain', 'Las bases de Rota y Morón, su aporte al flanco sur de la OTAN y que cumpla el gasto en defensa; que su apertura a fábricas chinas de autos y baterías no sea puerta de entrada de China a la UE.',
  'China quiere fábricas de autos eléctricos y baterías dentro de la UE y un gobierno que frene los aranceles europeos. Rusia, explotar el independentismo catalán y la polarización.')
Q('Portugal', 'Las Azores y la base de Lajes, escala clave hacia Europa y Medio Oriente, y que su energía y puertos no queden en manos chinas.',
  'China quiere su energía (es accionista de EDP y de las redes eléctricas) y el puerto de Sines.')
Q('Netherlands', 'Que ASML no venda a China las máquinas para chips avanzados, el puerto de Róterdam como gran puerta de Europa y su aporte a la OTAN.',
  'China quiere las máquinas de ASML y las empresas de chips como Nexperia. Rusia usaba Róterdam para su petróleo antes de las sanciones.')
Q('Belgium', 'Que aloje a la OTAN y la UE sin filtraciones, que use las reservas rusas de Euroclear para Ucrania y que el puerto de Amberes no sea la entrada de la cocaína.',
  'Rusia quiere recuperar sus reservas inmovilizadas en Euroclear y espiar a la OTAN y la UE desde Bruselas. China, el puerto de Zeebrugge, donde COSCO tiene una terminal.')
Q('Luxembourg', 'Que su plaza de fondos de inversión cumpla las sanciones y la transparencia fiscal.', 'Usar sus fondos y sociedades para mover capital.')
Q('Switzerland', 'Que aplique las sanciones a Rusia, entregue información bancaria y que sus traders de materias primas no sirvan para evadirlas.',
  'Rusia quiere sus bancos y casas de materias primas para mover capital; China, su plaza financiera y su tecnología de precisión.')
Q('Austria', 'Que su neutralidad no la convierta en el centro de la inteligencia rusa en Europa y que corte el gas ruso.', 'Rusia usa Viena como base de espionaje y tenía allí su gran puerta de gas a Europa.')
for k in ['Liechtenstein', 'Monaco', 'San Marino', 'Andorra']:
    Q(k, 'Transparencia financiera y que cumpla las sanciones.', 'Usar sus plazas para guardar fortunas de oligarcas y funcionarios.')
Q('Vatican', 'Que la Santa Sede apoye la causa de Ucrania y la libertad religiosa en China, y que su diplomacia no legitime a Moscú ni a Pekín.',
  'China quiere controlar el nombramiento de obispos y que el Vaticano rompa con Taiwán, su último aliado en Europa. Rusia quiere su neutralidad en la guerra.')
Q('Malta', 'Que deje de vender pasaportes y que sus buques y su registro no sirvan para el contrabando de petróleo ruso o libio.', 'Rusia usa registros y puertos para su flota en la sombra.')

# Europa del norte
Q('Denmark', 'Groenlandia y las islas Feroe, el control de los estrechos que unen el Báltico con el mar del Norte, la compra de F-35 y su apoyo a Ucrania.',
  'Rusia necesita sus estrechos para sacar petróleo y su flota del Báltico. China quiere minerales e infraestructura en Groenlandia.')
Q('Norway', 'Que sea el principal proveedor de gas de Europa en reemplazo de Rusia, la frontera ártica con Rusia y la vigilancia de los submarinos rusos de la península de Kola.',
  'Rusia quiere el Ártico, la pesca y Svalbard, y sabotear la infraestructura energética noruega si hay guerra.')
Q('Sweden', 'Su ingreso a la OTAN, su industria de defensa (Saab) y cerrar el Báltico a Rusia con Gotland.', 'Rusia quiere un Báltico abierto para su flota; Irán ha usado bandas suecas para atacar objetivos israelíes.')
Q('Finland', 'Su frontera de 1.300 km con Rusia ya dentro de la OTAN, su artillería y su acuerdo de bases con EE.UU.', 'Rusia quiere presionarla en la frontera y en el golfo de Finlandia, su salida desde San Petersburgo.')
Q('Iceland', 'El corredor entre Groenlandia, Islandia y el Reino Unido, por donde salen los submarinos rusos al Atlántico, y la base de Keflavík.', 'Rusia quiere ese corredor libre. China, presencia en el Ártico.')
Q('Faeroe Is.', 'Que siga alineada con la OTAN en el Atlántico Norte.', 'Rusia quiere su acuerdo de pesca y acceso a sus puertos.')
Q('Åland', 'Que Finlandia pueda defenderla en caso de guerra, aunque esté desmilitarizada.', 'Rusia quiere que siga desmilitarizada: está a la entrada del golfo de Botnia.')

# Europa central y oriental
Q('Poland', 'El frente oriental de la OTAN: tropas y bases de EE.UU., compra masiva de armas estadounidenses y coreanas, corredor de la ayuda a Ucrania y freno a Bielorrusia.',
  'Rusia quiere desestabilizarla con sabotajes, migrantes empujados desde Bielorrusia y drones, y frenar su papel de corredor de armas. China, su mercado.')
Q('Czechia', 'Que siga en la línea de apoyo a Ucrania (la iniciativa de municiones) y fuera del alcance de la influencia rusa y china.', 'Rusia quiere un gobierno que frene la ayuda a Ucrania y redes de propaganda en su territorio.')
Q('Slovakia', 'Que no rompa el frente común de la UE y la OTAN sobre Ucrania.', 'Rusia quiere un aliado que bloquee sanciones y ayuda, y que siga comprando su gas y petróleo.')
Q('Hungary', 'Que vuelva a la línea común de la UE y la OTAN, deje de vetar la ayuda a Ucrania y no sea la puerta de China en Europa.',
  'Rusia quería un aliado que vetara desde adentro las decisiones europeas. China, que fuera su puerta industrial en la UE (fábricas de baterías y autos).')
Q('Slovenia', 'Que siga integrada en la OTAN y la UE.', 'No tiene intereses relevantes.')
Q('Croatia', 'La terminal de gas de Krk y el puerto de Rijeka como alternativas al gas ruso y a los puertos chinos.', 'China quería el puerto de Rijeka.')
Q('Romania', 'La gran base de la OTAN en el mar Negro (Mihail Kogălniceanu), el escudo antimisiles de Deveselu, el gas marino y frenar a Rusia en Moldavia.',
  'Rusia quiere influir en sus elecciones, debilitar el flanco sur de la OTAN y presionarla desde el mar Negro.')
Q('Bulgaria', 'Que deje de depender del gas y del petróleo rusos y que su costa del mar Negro sea segura para la OTAN.', 'Rusia quiere su energía, su red de influencia política y sus depósitos de armas fuera del alcance de Ucrania.')
Q('Greece', 'Las bases de Souda y Alexandroupolis, su rivalidad controlada con Turquía y que el puerto del Pireo no sea plataforma china.',
  'China quiere el Pireo, que controla COSCO, como puerta a Europa. Rusia, influencia por la iglesia ortodoxa y sus armadores.')
Q('Cyprus', 'Sacar el dinero ruso de su banca, usarlo como plataforma para operar en Medio Oriente (con bases británicas), el gas del Mediterráneo y acercarlo a la OTAN.',
  'Rusia quiere su banca y sus empresas pantalla para mover capital; China, su posición en el Mediterráneo oriental.')
Q('N. Cyprus', 'Que la división no se vuelva definitiva y que no sirva de refugio a capitales sancionados.', 'Universidades, bancos y casinos que sirven a capitales rusos e iraníes.')
Q('Estonia', 'Que resista en la frontera con Rusia con tropas de la OTAN, y su experiencia en ciberdefensa.', 'Rusia quiere presionarla por la minoría rusa, con ciberataques y sabotajes de cables, y probar a la OTAN.')
Q('Latvia', 'Que resista en la frontera con Rusia y Bielorrusia con tropas de la OTAN.', 'Rusia quiere presionarla por su gran minoría rusa y probar a la OTAN.')
Q('Lithuania', 'El corredor de Suwałki, que une a los bálticos con Polonia, y la brigada alemana permanente.', 'Rusia quiere el paso a Kaliningrado; China, castigar su apoyo a Taiwán.')

# Balcanes
Q('Albania', 'Su papel en la OTAN (la base de Kuçova), su ingreso a la UE y su lucha contra la mafia de la cocaína.', 'Irán la castiga por alojar a los opositores de los Muyahidines del Pueblo.')
Q('Macedonia', 'Que siga en la OTAN y avance hacia la UE.', 'Rusia quiere frenar su integración occidental.')
Q('Montenegro', 'Que siga en la OTAN, avance hacia la UE y su costa adriática no caiga en manos rusas o chinas.', 'Rusia quiere recuperar influencia por la iglesia serbia; China, cobrar la deuda de la autopista.')
Q('Bosnia and Herz.', 'Preservar el acuerdo de Dayton, frenar el secesionismo serbobosnio e integrarla a la UE y la OTAN.', 'Rusia usa la República Srpska como palanca en los Balcanes y para frenar el ingreso a la OTAN.')
Q('Serbia', 'Alejarla de Rusia y China, que reconozca a Kosovo y avance a la UE, y su litio para Europa.',
  'Rusia quiere su principal aliado en los Balcanes, su petrolera NIS y su veto a Kosovo. China quiere minas (Bor), acerías y fábricas, y venderle armas.')
Q('Kosovo', 'La base de Bondsteel, la KFOR y su reconocimiento internacional.', 'Rusia y China quieren bloquear su reconocimiento para no sentar precedentes (Crimea, Taiwán).')
for k in ['Jersey', 'Guernsey', 'Isle of Man']:
    Q(k, 'Transparencia financiera y que cumpla las sanciones.', 'Usar sus plazas para guardar fortunas.')

# Rusia y su periferia
Q('Russia', 'Debilitarla para que no pueda volver a invadir a sus vecinos, cortarle la renta del petróleo y el gas, impedir su alianza plena con China y que acepte una Ucrania soberana. Una parte de EE.UU. busca además separarla de Pekín con un acuerdo.',
  'Es uno de los centros de la alianza. China quiere su energía barata, sus materias primas y un socio militar que distraiga a EE.UU. en Europa; Irán y Corea del Norte, tecnología militar a cambio de drones, misiles y municiones.')
Q('Ukraine', 'Que no caiga en manos de Rusia y que Rusia no gane la guerra; integrarla a la UE y, en la visión de muchos aliados, a la OTAN, como frontera oriental de Europa; reconstruirla con empresas occidentales y acceder a sus tierras negras, su litio, titanio y tierras raras.',
  'Rusia quiere anexar los territorios ocupados, una Ucrania neutral, desarmada y fuera de la OTAN y la UE, y un gobierno afín en Kiev. China quiere que Rusia no pierda, sin quedar atrapada en sanciones. Irán y Corea del Norte prueban sus armas en el frente.')
Q('Belarus', 'Separarla de Rusia, liberar a los presos políticos, frenar el despliegue de armas nucleares y que no sirva de plataforma para atacar a Ucrania o presionar a Polonia y los bálticos.',
  'Rusia quiere integrarla en el «Estado de la Unión», con armas nucleares y tropas, como plataforma contra la OTAN. China, un corredor ferroviario hacia Europa.')
Q('Moldova', 'Que entre a la UE, se libere de la energía rusa y que Transnistria no se vuelva un frente más.', 'Rusia quiere mantenerla en su órbita, conservar sus tropas en Transnistria y un gobierno afín.')
Q('Georgia', 'Que retome el camino a la UE y la OTAN, frene la deriva autoritaria y siga siendo el corredor del Cáucaso que evita a Rusia e Irán.',
  'Rusia quiere mantenerla fuera de la OTAN y la UE y conservar Abjasia y Osetia del Sur. China quiere el puerto de Anaklia y el corredor hacia Europa.')
Q('Armenia', 'Sacarla de la órbita rusa (la base de Gyumri, la OTSC), firmar la paz con Azerbaiyán y abrir un corredor bajo gestión de EE.UU. por Syunik hacia Asia central.',
  'Rusia quiere conservar su base y su control del país. Irán quiere que no haya corredor que lo aísle de Armenia y que sus fronteras no cambien.')
Q('Azerbaijan', 'Gas para Europa por fuera de Rusia, un socio laico entre Rusia e Irán, cercano a Israel y Turquía, y el corredor transcaspio.',
  'Rusia quiere retener influencia en el Cáucaso. Irán teme el nacionalismo azerí en su propio territorio y la alianza con Israel.')

# Asia central
Q('Kazakhstan', 'Uranio, petróleo y minerales críticos para Occidente, y el corredor transcaspio que une Asia con Europa sin pasar por Rusia. Que no sirva para evadir sanciones.',
  'Rusia quiere mantenerlo en la OTSC y la Unión Euroasiática, como su retaguardia. China quiere su tránsito ferroviario hacia Europa, su petróleo, gas y uranio.')
Q('Uzbekistan', 'Minerales críticos, que abra su economía a Occidente y que no dependa de Rusia.', 'Rusia quiere sus migrantes y su mercado; China, inversión, minería y tránsito.')
Q('Kyrgyzstan', 'Que deje de ser la vía para reexportar a Rusia productos sancionados.', 'Rusia quiere su base aérea de Kant y usarlo para importar lo sancionado; China, el ferrocarril hacia Uzbekistán.')
Q('Tajikistan', 'Que contenga a los grupos yihadistas de la frontera afgana.', 'Rusia quiere su base 201; China, vigilar la frontera con Afganistán y Xinjiang.')
Q('Turkmenistan', 'Que su gas llegue a Europa por el Caspio, sin pasar por Rusia.', 'China quiere su gas, del que es casi el único comprador.')
Q('Mongolia', 'Un «tercer vecino» democrático entre Rusia y China, con minerales y tierras raras para Occidente.', 'Rusia quiere un gasoducto hacia China por su territorio; China, sus minerales.')
Q('Afghanistan', 'Contener al Estado Islámico-Khorasan y a Al Qaeda, recuperar la base de Bagram y que no vuelva a ser santuario terrorista.',
  'China quiere cobre, litio y petróleo, y que no se exporte el yihadismo a Xinjiang. Rusia, un régimen estable en su retaguardia. Irán, agua del río Helmand y frontera tranquila.')

# Turquía y Medio Oriente
Q('Turkey', 'Que siga en la OTAN, controle los estrechos del Bósforo y los Dardanelos para cerrar el mar Negro a Rusia, aloje la base de Incirlik y no compre armas rusas.',
  'Rusia quiere alejarla de la OTAN, venderle armas y energía (Akkuyu, TurkStream) y usarla para evadir sanciones. China, que sea un nodo del corredor medio.')
Q('Israel', 'Su principal aliado en Medio Oriente: superioridad militar frente a Irán y sus aliados, ampliar los Acuerdos de Abraham con Arabia Saudita e integrarlo a la región, y sus empresas de tecnología y defensa.',
  'Irán quiere destruirlo o desgastarlo con Hamás, Hezbolá y los hutíes. China quiere comercio y puertos (Haifa) sin pelearse con los árabes. Rusia mantiene canales con Israel y con Irán a la vez.')
Q('Palestine', 'Que Hamás no gobierne Gaza, que la Autoridad Palestina se reforme y que la normalización árabe con Israel avance.',
  'Irán quiere usar a Hamás y la Yihad Islámica contra Israel. China quiere aparecer como mediadora y referente del «Sur global» en la causa palestina.')
Q('Lebanon', 'Desarmar a Hezbolá, fortalecer al ejército libanés y que el país no sea una base iraní en la frontera de Israel.',
  'Irán quiere mantener a Hezbolá como su brazo armado más poderoso y su frente contra Israel.')
Q('Syria', 'Integrar al nuevo gobierno a la órbita occidental y árabe, contener al Estado Islámico, proteger a kurdos y drusos y sacar a Rusia e Irán.',
  'Rusia quiere conservar sus bases de Tartús y Hmeimim, su única salida militar al Mediterráneo. Irán quería su corredor terrestre hacia Hezbolá, que perdió en 2024.')
Q('Jordan', 'Un aliado estable que aloja bases de EE.UU., protege la frontera de Israel y derriba drones iraníes.', 'Irán quiere usar su frontera para pasar armas a Cisjordania.')
Q('Iraq', 'Que no quede bajo control iraní, que se disuelvan o integren las milicias, contener al Estado Islámico y que su petróleo siga en el mercado en dólares.',
  'Irán quiere controlar su gobierno, sus milicias y su sistema bancario para evadir sanciones. China quiere su petróleo y obras.')
Q('Iran', 'Impedir que tenga armas nucleares, desarmar su red de milicias (Hezbolá, hutíes, milicias iraquíes) y, para una parte del bloque, la caída del régimen.',
  'Es uno de los socios de la alianza: China compra casi todo su petróleo y Rusia le compra drones y le vende armas y tecnología.')
Q('Saudi Arabia', 'Que venda petróleo en dólares, compre armas estadounidenses, invierta en EE.UU., normalice relaciones con Israel y se mantenga del lado occidental frente a China.',
  'China quiere su petróleo, pagarlo en yuanes y su ingreso pleno a los BRICS. Rusia quiere coordinar la producción de petróleo en la OPEP+.')
Q('United Arab Emirates', 'Defensa, inteligencia artificial, los Acuerdos de Abraham y que deje de ser plaza para el capital ruso y el comercio con Irán.',
  'Rusia quiere Dubái como plaza para mover capital y comerciar; Irán, su comercio a través de Dubái; China, puertos e inteligencia artificial.')
Q('Qatar', 'La base de Al Udeid, sede del comando de EE.UU. para Medio Oriente, y su papel de mediador con Hamás y los talibanes.', 'China quiere su gas a largo plazo. Irán comparte con Qatar el mayor yacimiento de gas del mundo.')
Q('Bahrain', 'La base de la Quinta Flota de EE.UU. y su alianza con Israel.', 'Irán quiere influir sobre su mayoría chií.')
Q('Kuwait', 'Bases de EE.UU. para todo el golfo.', 'No tiene intereses relevantes más allá del petróleo.')
Q('Oman', 'Su mediación con Irán y el acceso a los puertos de Duqm y Salalah, fuera del estrecho de Ormuz.', 'Irán lo usa como canal de mediación; China, sus puertos y petróleo.')
Q('Yemen', 'Que los hutíes no cierren el mar Rojo ni el estrecho de Bab el-Mandeb, por donde pasa una parte grande del comercio mundial.',
  'Irán quiere usar a los hutíes contra Israel, Arabia Saudita y el tráfico marítimo. China y Rusia evitan condenarlos en la ONU.')
Q('Egypt', 'Estabilidad, el canal de Suez abierto, la paz con Israel y su control de la frontera con Gaza.',
  'China quiere el canal, la zona económica de Suez y obras en la nueva capital. Rusia construye su central nuclear y le vende trigo y armas.')

# Asia del Sur
Q('India', 'Un contrapeso a China en Asia: el Quad con EE.UU., Japón y Australia, comprarle armas y tecnología, mover fábricas desde China hacia India y que deje de comprar petróleo y armas rusas.',
  'Rusia quiere venderle petróleo y armas y mantenerla neutral en Ucrania. China quiere frenarla en el Himalaya, mantenerla fuera de alianzas con EE.UU. y competir por el océano Índico.')
Q('Pakistan', 'Cooperación contra el terrorismo, que su arsenal nuclear esté seguro, acceso a sus minerales y alejarlo de China.',
  'China quiere el Corredor Económico China-Pakistán y el puerto de Gwadar, su salida al mar Arábigo, y un aliado militar contra India.')
Q('Bangladesh', 'Un socio en el golfo de Bengala, que no se vuelva plataforma china ni dependa de su deuda.', 'China quiere puertos, obras y venderle armas; Rusia construye su central nuclear de Rooppur.')
Q('Sri Lanka', 'Que no aloje buques militares o espías chinos y que su deuda no la entregue a China.', 'China quiere Hambantota y Colombo Port City como escalas en el océano Índico.')
Q('Nepal', 'Equilibrar a China con programas de ayuda estadounidenses.', 'China quiere tránsito, la Franja y la Ruta y frenar el activismo tibetano.')
Q('Bhutan', 'Que siga ligado a India.', 'China quiere cerrar la frontera en su favor, incluido Doklam, cerca del corredor que une India con su noreste.')
Q('Maldives', 'Seguridad marítima en el Índico y que no se vuelva base china.', 'China quiere influencia y una escala en las rutas del océano Índico.')
Q('Siachen Glacier', 'No tiene intereses particulares.', 'China vigila la zona, vecina al Aksai Chin que controla.')

# Sudeste asiático
Q('Myanmar', 'Contener a la junta, apoyar a la oposición democrática, cortar las redes de estafas y el narcotráfico y que no sea una salida china al océano Índico.',
  'China quiere las tierras raras del norte, sus gasoductos y el puerto de Kyaukphyu, y un régimen estable en su frontera. Rusia quiere venderle armas.')
Q('Thailand', 'Su alianza tratada con EE.UU., ejercicios militares conjuntos y que no se incline hacia China.', 'China quiere el tren rápido hacia Laos y venderle submarinos y armas.')
Q('Laos', 'Que no quede atrapado por la deuda china.', 'China quiere el tren Kunming-Vientián y la influencia que le da su deuda.')
Q('Cambodia', 'Que la base de Ream no se vuelva una base naval china y que cierre los complejos de estafas.', 'China quiere Ream como su base en el golfo de Tailandia y un aliado en la ASEAN.')
Q('Vietnam', 'Un socio frente a China: fábricas que salen de China, cooperación en el mar de China Meridional y alejarlo de las armas rusas.',
  'China quiere controlar el mar de China Meridional, incluidas las islas que reclama Vietnam. Rusia quiere venderle armas y petróleo.')
Q('Malaysia', 'El estrecho de Malaca, los chips y que resista los reclamos chinos frente a Borneo.', 'China quiere inversión, presencia en el mar de China Meridional y su gas.')
Q('Singapore', 'Acceso naval para EE.UU., su plaza financiera y su papel de nodo neutral.', 'China quiere su plaza financiera y su influencia en la comunidad china.')
Q('Indonesia', 'Los estrechos de Malaca, la Sonda y Lombok, su níquel para baterías fuera del dominio chino y su peso en la ASEAN.',
  'China quiere su níquel, el tren rápido y su presencia en los estrechos; Rusia, venderle armas y sumarlo a los BRICS.')
Q('Brunei', 'Que resista los reclamos chinos.', 'China reclama aguas que Brunéi considera propias.')
Q('Philippines', 'Bases para EE.UU. frente a Taiwán y al mar de China Meridional, y que resista la presión china en los arrecifes.',
  'China quiere imponer su control sobre los arrecifes y aguas que reclama, y alejarla de EE.UU.')
Q('Timor-Leste', 'Que no quede bajo influencia china.', 'China quiere infraestructura e influencia.')

# Asia oriental
Q('China', 'Frenar su ascenso militar y tecnológico sin llegar a la guerra, impedir que tome Taiwán y reducir la dependencia de sus fábricas y minerales.',
  'Es el otro centro de la alianza: ser la primera potencia mundial, recuperar Taiwán y dominar las cadenas de minerales y tecnologías.')
Q('Hong Kong', 'Que conserve su autonomía y su plaza financiera abierta.', 'China quiere control total sin perder su función de plaza financiera internacional.')
Q('Macao', 'No tiene intereses particulares.', 'China quiere control total.')
Q('Taiwan', 'Que no caiga en manos de China, que siga fabricando sus chips (y en parte en EE.UU.) y que gaste más en defensa.',
  'China quiere la reunificación, por las buenas o por la fuerza.')
Q('Japan', 'Su rearme, las bases de Okinawa, las islas del sur y su alianza con EE.UU. frente a China y Corea del Norte.',
  'China quiere las islas Senkaku y frenar su rearme; Rusia conservar las Kuriles.')
Q('South Korea', 'Su alianza frente a Corea del Norte, sus chips y astilleros para EE.UU., y que coopere con Japón.',
  'China quiere frenar su alianza con EE.UU. y el escudo THAAD.')
Q('North Korea', 'Desnuclearizarla o contenerla.', 'Rusia quiere soldados y municiones; China su supervivencia como amortiguador.')

# Oceanía
Q('Australia', 'Su base aliada en el Indo-Pacífico: AUKUS y los submarinos nucleares, bases para EE.UU. en el norte, sus minerales críticos fuera de China y su influencia en las islas del Pacífico.',
  'China quiere sus minerales y presionarla para que se aleje de EE.UU., y competir por las islas del Pacífico.')
Q('New Zealand', 'Su lugar en los Cinco Ojos y su influencia en el Pacífico.', 'China quiere influencia política y comercio.')
Q('Papua New Guinea', 'Bases para EE.UU. y Australia y un aliado en el Pacífico.', 'China quiere minería e infraestructura.')
Q('Solomon Is.', 'Revertir la presencia china y su pacto de seguridad.', 'China quiere presencia policial y de seguridad y un puerto.')
Q('Fiji', 'Un socio regional y una base logística.', 'China quiere cooperación policial y presencia.')
Q('Vanuatu', 'Que no aloje presencia militar china.', 'China quiere infraestructura y su apoyo.')
Q('Samoa', 'Que no dependa de China.', 'China quiere influencia y un puerto.')
Q('Tonga', 'Que no dependa de la deuda china.', 'China quiere influencia por su deuda.')
Q('Kiribati', 'Que no aloje presencia china en el Pacífico central, cerca de Hawái.', 'China quiere presencia policial y la pista de Kanton.')
Q('Nauru', 'Su alianza con Australia.', 'China quiere su reconocimiento.')
for k in ['Micronesia', 'Marshall Is.', 'Palau']:
    Q(k, 'Acceso militar exclusivo de EE.UU. y negar el área a China.', 'China quiere desplazar a EE.UU.')
for k in ['Guam', 'N. Mariana Is.']:
    Q(k, 'Base avanzada frente a China.', 'Es un objetivo militar en caso de guerra.')
Q('American Samoa', 'No tiene intereses particulares.', 'No tiene intereses relevantes.')
Q('Cook Is.', 'Que no se aleje de Nueva Zelanda.', 'China quiere minerales del lecho marino.')
Q('Niue', 'No tiene intereses particulares.', 'No tiene intereses relevantes.')
Q('Fr. Polynesia', 'Que siga francesa.', 'No tiene intereses relevantes.')
Q('New Caledonia', 'Que siga francesa y su níquel.', 'No tiene intereses relevantes.')
for k in ['Wallis and Futuna Is.', 'Pitcairn Is.', 'Norfolk Island', 'Heard I. and McDonald Is.', 'Ashmore and Cartier Is.']:
    Q(k, 'No tiene intereses particulares.', 'No tiene intereses relevantes.')
Q('Indian Ocean Ter.', 'Vigilancia del océano Índico.', 'No tiene intereses relevantes.')

# Asia oriental y Pacífico: versión más detallada
Q('China', 'Frenar su ascenso militar y tecnológico sin llegar a la guerra: negarle los chips y las máquinas más avanzadas, sacar de su territorio las cadenas de suministro estratégicas, reducir la dependencia de sus tierras raras, impedir que tome Taiwán o domine el mar de China Meridional, y abrir su mercado a las empresas occidentales.',
  'Es el otro centro de la alianza: llegar a ser la primera potencia mundial hacia mediados de siglo, recuperar Taiwán, expulsar a EE.UU. de la primera cadena de islas, dominar las cadenas de minerales, baterías y autos eléctricos, y armar un orden alternativo (BRICS, OCS, pagos en yuanes). Rusia le aporta energía y materias primas; Irán, petróleo barato.')
Q('Hong Kong', 'Que conserve su autonomía, su justicia independiente y su plaza financiera abierta; sancionar a los responsables de la represión.',
  'China quiere control político total sin perder su papel de puerta financiera de China al mundo y de plaza para emitir deuda y acciones.')
Q('Macao', 'Que no sirva para sacar capitales chinos ni para evadir sanciones.', 'China quiere control total y que el juego siga financiando la región.')
Q('Taiwan', 'Que no caiga en manos de China, porque es el eslabón central de la primera cadena de islas y fabrica casi todos los chips avanzados; que gaste más en defensa y que TSMC produzca también en EE.UU.',
  'China quiere la reunificación, por las buenas o por la fuerza: romper la cadena de islas que encierra a su marina y quedarse con la industria de chips. Rusia apoya la posición china.')
Q('Japan', 'Su rearme (contraataque de largo alcance, el doble del gasto), las bases de Okinawa y las islas del sur, la alianza con EE.UU. y Corea del Sur frente a China y Corea del Norte, y su industria de chips y astilleros.',
  'China quiere las islas Senkaku, frenar su rearme y separarlo de EE.UU. Rusia quiere conservar las Kuriles y que no levante más sanciones.')
Q('South Korea', 'Su alianza frente a Corea del Norte (28.000 soldados estadounidenses), sus chips, baterías y astilleros para EE.UU., y que coopere con Japón.',
  'China quiere frenar su alianza con EE.UU. y el escudo THAAD, y que no se sume a una defensa de Taiwán. Rusia quiere que no le venda armas a Ucrania.')
Q('North Korea', 'Desnuclearizarla o, al menos, contener sus misiles y frenar su cooperación militar con Rusia.',
  'Rusia quiere sus soldados, municiones y misiles para Ucrania a cambio de tecnología. China quiere que sobreviva como amortiguador frente a las tropas de EE.UU.')
Q('Papua New Guinea', 'Bases y accesos para EE.UU. y Australia (Manus, Lombrum), y que sea el ancla de seguridad del Pacífico Sur.', 'China quiere minería, puertos y cooperación policial.')
Q('Solomon Is.', 'Revertir la presencia china y que su pacto de seguridad con Pekín no derive en una base.', 'China quiere presencia policial y de seguridad, un puerto y el voto del país en organismos internacionales.')
Q('Fiji', 'Un socio regional y la sede de instituciones del Pacífico, con cooperación militar.', 'China quiere cooperación policial y presencia diplomática.')
Q('Vanuatu', 'Que no aloje presencia militar china y que mantenga su tratado de seguridad con Australia.', 'China quiere infraestructura, deuda y apoyo diplomático.')
Q('Samoa', 'Que no dependa de la deuda china.', 'China quiere influencia y un puerto.')
Q('Tonga', 'Que no dependa de la deuda china.', 'China quiere influencia por la deuda que le debe Tonga.')
Q('Micronesia', 'Acceso militar exclusivo de EE.UU. por el Pacto de Libre Asociación y negar el área a China, en la retaguardia de Guam.', 'China quiere desplazar a EE.UU. con ayuda y obras.')
Q('Marshall Is.', 'La base de pruebas de misiles de Kwajalein, el acceso militar exclusivo de EE.UU. y que siga reconociendo a Taiwán.', 'China quiere que reconozca a Pekín y desplazar a EE.UU.')
Q('Palau', 'Acceso militar exclusivo de EE.UU., el radar de largo alcance y que siga reconociendo a Taiwán.', 'China quiere que reconozca a Pekín y presiona con el turismo.')
Q('Guam', 'La base avanzada de EE.UU. en el Pacífico occidental: bombarderos, submarinos y la defensa antimisiles frente a China y Corea del Norte.', 'Es un objetivo militar chino y norcoreano en caso de guerra; sus redes son blanco del espionaje chino.')
Q('N. Mariana Is.', 'Pistas y campos de entrenamiento como complemento de Guam (Tinian).', 'Es un objetivo militar en caso de guerra.')

# África del Norte
Q('Morocco', 'Un aliado estable y puerta de África: socio de Israel, comprador de armas estadounidenses, sede del ejercicio African Lion y controlador de la migración hacia España. Apoya su soberanía sobre el Sahara.',
  'China quiere fábricas de baterías y autos para entrar a Europa y EE.UU. con sus tratados comerciales, y su fosfato. Rusia, comprarle fosfatos y venderle granos.')
Q('W. Sahara', 'Que quede bajo soberanía marroquí con autonomía y que se cierre el conflicto.', 'Rusia sostiene en la ONU al Frente Polisario, aliado de Argelia.')
Q('Algeria', 'Su gas para Europa en reemplazo del ruso, que coopere contra el yihadismo del Sahel y que compre menos armas rusas.',
  'Rusia quiere seguir siendo su principal proveedor de armas y un aliado en el Mediterráneo. China, obras y comercio.')
Q('Tunisia', 'Que frene la migración hacia Italia y no se aleje de Occidente.', 'Rusia y China buscan influencia en el giro autoritario del gobierno.')
Q('Libya', 'Su petróleo, que no se vuelva base rusa y que se reunifique bajo un gobierno aceptable.',
  'Rusia quiere bases aéreas en el este (al-Jufra, al-Khadim) para proyectarse sobre el Sahel y el Mediterráneo, a través del Africa Corps y de Haftar.')
Q('Mauritania', 'Un aliado estable frente al Sahel, que frene la migración hacia Canarias y su gas.', 'China quiere su pesca y su hierro.')

# Sahel y África occidental
Q('Mali', 'Frenar al yihadismo (JNIM, Estado Islámico del Sahel) y la presencia rusa, y que la junta vuelva a un gobierno civil.',
  'Rusia quiere su oro, una base de influencia en el Sahel y desplazar a Francia, a través de Wagner y el Africa Corps. China, minas de litio y oro.')
Q('Burkina Faso', 'Frenar al yihadismo y la presencia rusa.', 'Rusia quiere minas de oro, una refinería y presencia militar; propaganda antioccidental.')
Q('Niger', 'Recuperar su colaboración contra el yihadismo y su uranio, perdidos tras el golpe de 2023.', 'Rusia quiere su uranio y presencia militar; China, su petróleo y el oleoducto hacia Benín.')
Q('Chad', 'Que no se pase del todo a Rusia y que siga conteniendo al yihadismo del lago Chad.', 'Rusia quiere reemplazar a Francia como socio militar.')
Q('Senegal', 'Un socio democrático estable, su petróleo y gas y cooperación en seguridad, aunque cerró las bases francesas.', 'China y Rusia buscan acercarse al gobierno soberanista.')
Q('Gambia', 'Estabilidad democrática.', 'No tiene intereses relevantes.')
Q('Guinea-Bissau', 'Cortar la ruta de la cocaína hacia Europa.', 'No tiene intereses relevantes.')
Q('Guinea', 'Bauxita y hierro fuera del control chino y que la junta entregue el poder.', 'China quiere la bauxita y el hierro de Simandou para su acero y su aluminio.')
Q('Sierra Leone', 'Estabilidad.', 'China quiere minería y pesca.')
Q('Liberia', 'Su registro de buques y la estabilidad.', 'No tiene intereses relevantes.')
Q("Côte d'Ivoire", 'Un aliado estable en el golfo de Guinea, frente al avance yihadista y ruso del Sahel.', 'No tiene intereses relevantes.')
Q('Ghana', 'Oro, cacao, una democracia estable y su cooperación de seguridad.', 'China quiere bauxita y minería; muchos mineros ilegales chinos operan allí.')
Q('Togo', 'Contener el yihadismo en el norte.', 'Rusia quiere un acuerdo militar y presencia.')
Q('Benin', 'Contener el yihadismo en el norte.', 'China quiere el oleoducto que trae el petróleo de Níger.')
Q('Nigeria', 'Su peso regional, que combata a Boko Haram y al Estado Islámico, que proteja a las minorías cristianas y que no dependa de China.',
  'China quiere obras, refinerías y deuda; Rusia, influencia militar y propaganda.')
Q('Cabo Verde', 'Su posición atlántica.', 'No tiene intereses relevantes.')

# África central
Q('Cameroon', 'Contener a Boko Haram y la crisis anglófona.', 'China quiere el puerto de Kribi y obras.')
Q('Central African Rep.', 'Que no quede bajo control ruso.', 'Rusia quiere oro y diamantes a cambio de seguridad.')
Q('Gabon', 'Estabilidad tras el golpe y su petróleo y manganeso.', 'China quiere manganeso y madera.')
Q('Eq. Guinea', 'Que no haya base naval china en el Atlántico.', 'China quiere un puerto en el Atlántico.')
Q('São Tomé and Principe', 'Estabilidad.', 'No tiene intereses relevantes.')
Q('Congo', 'Su petróleo.', 'China quiere su petróleo y cobrar su deuda.')
Q('Dem. Rep. Congo', 'Su cobalto, cobre y coltán fuera del dominio chino (acuerdo de minerales a cambio de seguridad) y la paz con Ruanda y el M23.',
  'China controla la mayor parte de sus minas de cobalto y cobre y quiere conservarlas.')
Q('Rwanda', 'Su eficacia, sus tropas de paz y que deje de apoyar al M23.', 'No tiene intereses relevantes.')
Q('Burundi', 'Estabilidad.', 'China y Rusia quieren minería.')

# África oriental y Cuerno
Q('Sudan', 'Que termine la guerra, que no haya base rusa en el mar Rojo y frenar el genocidio en Darfur.',
  'Rusia quiere una base naval en Port Sudan y su oro; Irán le vende drones al ejército.')
Q('S. Sudan', 'Estabilidad.', 'China quiere su petróleo.')
Q('Ethiopia', 'Estabilidad en el Cuerno de África y la gran represa sin guerra con Egipto.', 'China quiere obras y cobrar su deuda; Rusia, influencia.')
Q('Eritrea', 'Que no se acerque a Rusia ni desestabilice a Etiopía.', 'Rusia quiere acceso al puerto de Massawa en el mar Rojo.')
Q('Djibouti', 'La base de Camp Lemonnier, la única base permanente de EE.UU. en África, junto a Bab el-Mandeb.', 'China quiere su base naval y el puerto.')
Q('Somalia', 'Combatir a Al Shabaab y al Estado Islámico.', 'No tiene intereses relevantes.')
Q('Somaliland', 'Una base en Berbera y un aliado en el golfo de Adén.', 'China quiere que no sea reconocida.')
Q('Kenya', 'Su aliado principal en África oriental: bases, la lucha contra Al Shabaab y la misión en Haití.', 'China quiere el tren Mombasa-Nairobi y cobrar la deuda.')
Q('Uganda', 'Estabilidad.', 'China quiere el petróleo del lago Alberto.')
Q('Tanzania', 'Estabilidad.', 'China quiere obras y puertos.')

# África austral
Q('Angola', 'El corredor de Lobito para sacar los minerales del Congo y Zambia sin China, y su petróleo.', 'China quiere su petróleo y cobrar su deuda.')
Q('Zambia', 'El cobre y el corredor de Lobito.', 'China quiere el cobre y cobrar su deuda.')
Q('Zimbabwe', 'Reformas democráticas.', 'China quiere su litio.')
Q('Malawi', 'Estabilidad.', 'No tiene intereses relevantes.')
Q('Mozambique', 'El gas de Cabo Delgado.', 'China quiere minería y obras.')
Q('Madagascar', 'Estabilidad tras el golpe.', 'No tiene intereses relevantes.')
Q('Namibia', 'Su uranio, su petróleo nuevo y su estabilidad democrática.', 'China quiere su uranio.')
Q('Botswana', 'Una democracia estable.', 'No tiene intereses relevantes.')
Q('South Africa', 'Alejarla de los BRICS y de Rusia, y que no se oponga a EE.UU. en los organismos internacionales.',
  'Rusia y China quieren mantenerla como pilar africano de los BRICS y del «Sur global».')
Q('Lesotho', 'Estabilidad.', 'No tiene intereses relevantes.')
Q('eSwatini', 'Que siga reconociendo a Taiwán.', 'China quiere que reconozca a Pekín.')
Q('Comoros', 'Estabilidad.', 'No tiene intereses relevantes.')
Q('Mauritius', 'Diego García.', 'China quiere influencia en el Índico.')
Q('Seychelles', 'Seguridad marítima.', 'No tiene intereses relevantes.')
Q('Saint Helena', 'Ascensión.', 'No tiene intereses relevantes.')
Q('Br. Indian Ocean Ter.', 'Conservar Diego García.', 'Que la base se pierda.')
Q('Fr. S. Antarctic Lands', 'No tiene intereses particulares.', 'No tiene intereses relevantes.')

# Ampliación de los que quedaron cortos
Q('Belize', 'Cooperación antinarcóticos en su costa y su frontera con México y Guatemala, que el diferendo con Guatemala se resuelva en La Haya sin conflicto y que siga reconociendo a Taiwán.', 'China quiere que reconozca a Pekín, como hicieron casi todos sus vecinos, a cambio de obras y comercio.')
Q('Haiti', 'Contener a las pandillas, que no se vuelva una base del narcotráfico ni una fuente de migración masiva hacia EE.UU. y la República Dominicana, y que una fuerza internacional, no de EE.UU., cargue con la seguridad.', 'No tiene intereses relevantes; China y Rusia solo pesan como votos en el Consejo de Seguridad sobre la misión internacional.')
Q('Trinidad and Tobago', 'Usarla como aliada y plataforma frente a Venezuela (radares, acceso de buques), asegurar su gas licuado y que no siga negociando gas con Caracas sin aval de EE.UU.', 'Venezuela, cuando era aliada de la alianza, quería sus acuerdos de gas marino; China, comercio y obras.')
Q('Suriname', 'El petróleo marino que explotan TotalEnergies y otras empresas occidentales, alejarlo de la deuda china y frenar el narcotráfico y la minería ilegal de oro.', 'China quiere infraestructura, minería de oro y cobrar su deuda.')
Q('Luxembourg', 'Que su enorme plaza de fondos de inversión cumpla las sanciones, la transparencia fiscal y el impuesto mínimo a las multinacionales, y que aporte a la defensa europea.', 'Usar sus fondos y sociedades para mover capital; China tiene allí la sede europea de varios de sus bancos.')
Q('Slovakia', 'Que no rompa el frente común de la UE y la OTAN sobre Ucrania, que siga alojando tropas aliadas y que deje de depender del gas y el petróleo rusos.', 'Rusia quiere un aliado que bloquee sanciones y ayuda dentro de la UE, y que siga comprando su gas y petróleo.')
Q('Slovenia', 'Que siga integrada en la OTAN y la UE, apoye a Ucrania y que su puerto de Koper sirva a la logística aliada.', 'No tiene intereses relevantes más allá del comercio.')
Q('Latvia', 'Que resista en la frontera con Rusia y Bielorrusia con la brigada de la OTAN liderada por Canadá, integre a su minoría rusa y corte todo vínculo energético con Rusia.', 'Rusia quiere presionarla por su gran minoría rusohablante, con propaganda e incidentes de frontera, y probar la decisión de la OTAN.')
Q('Macedonia', 'Que siga en la OTAN, destrabe su ingreso a la UE y frene la influencia rusa en su política y sus medios.', 'Rusia quiere frenar su integración occidental; China, obras de autopistas con deuda.')
Q('Kosovo', 'La base de Bondsteel, la KFOR, su reconocimiento internacional y un acuerdo de normalización con Serbia que estabilice los Balcanes.', 'Rusia y China quieren bloquear su reconocimiento en la ONU para no sentar precedentes (Crimea, Taiwán) y apoyan a Serbia.')
Q('Kyrgyzstan', 'Que deje de ser la vía para reexportar a Rusia productos sancionados y que sus bancos no procesen pagos rusos; acceso a su oro y tierras raras.', 'Rusia quiere su base aérea de Kant y usarlo para importar lo sancionado; China, el ferrocarril China-Kirguistán-Uzbekistán y minería.')
Q('Tajikistan', 'Que contenga a los grupos yihadistas de la frontera afgana y al Estado Islámico-Khorasan, que recluta tayikos.', 'Rusia quiere su base 201, la mayor fuera de su territorio; China, vigilar la frontera con Afganistán, cerca de Xinjiang, y minería.')
Q('Turkmenistan', 'Que su gas llegue a Europa por un gasoducto bajo el Caspio, sin pasar por Rusia, y que se abra a empresas occidentales.', 'China quiere su gas, del que es casi el único comprador; Rusia, que no compita con su gas en Europa.')
Q('Bahrain', 'La base de la Quinta Flota de EE.UU., su alianza con Israel por los Acuerdos de Abraham y el acuerdo de seguridad integral de 2023.', 'Irán quiere influir sobre su mayoría chií y desestabilizar a la monarquía suní.')
Q('Kuwait', 'Las bases de EE.UU. (Arifjan, Ali Al Salem), su petróleo y su lugar como aliado principal no miembro de la OTAN.', 'Irán presiona por la frontera marítima y el yacimiento de gas de Dorra; China quiere su petróleo y obras.')
Q('Nepal', 'Equilibrar a China con programas de ayuda estadounidenses y mantenerlo cerca de India.', 'China quiere tránsito hacia el sur de Asia, la Franja y la Ruta y frenar el activismo tibetano.')
Q('Bhutan', 'Que siga ligado a India y no ceda frente a China en la frontera.', 'China quiere cerrar la frontera en su favor, incluido Doklam, cerca del corredor de Siliguri que une India con su noreste.')
Q('Maldives', 'Seguridad marítima en el Índico, cooperación con India y que no se vuelva base china.', 'China quiere influencia, deuda y una escala en las rutas del océano Índico.')
Q('Laos', 'Que no quede atrapado por la deuda china, que cierre las zonas de estafas y narcotráfico del Triángulo de Oro y que limpie las bombas sin explotar de la guerra.', 'China quiere el tren Kunming-Vientián como pieza del corredor hacia Singapur y la influencia que le da su deuda.')
Q('Singapore', 'Acceso naval para EE.UU. (Changi), su plaza financiera, sus refinerías y su papel de nodo neutral en el estrecho de Malaca.', 'China quiere su plaza financiera para su capital, su tecnología y su influencia en la mayoría étnica china.')
Q('Brunei', 'Que resista los reclamos chinos en el mar de China Meridional y coopere en seguridad.', 'China reclama aguas que Brunéi considera propias y quiere su gas y petróleo.')
Q('Timor-Leste', 'Que no quede bajo influencia china, que coopere con Australia en seguridad y que el yacimiento de Greater Sunrise no lo explote China.', 'China quiere infraestructura, influencia y participar del gas de Greater Sunrise.')
Q('New Zealand', 'Su lugar en los Cinco Ojos, sumarlo a AUKUS en tecnología e influencia en el Pacífico Sur a través de sus territorios asociados.', 'China quiere influencia política, comercio (es su mayor cliente) y menos alineamiento con EE.UU.')
Q('Samoa', 'Que no dependa de la deuda china y que siga en la órbita de Nueva Zelanda y Australia.', 'China quiere influencia, deuda y un puerto.')
Q('Tonga', 'Que no dependa de la deuda china y que se acerque a Australia en seguridad.', 'China quiere influencia por la deuda que le debe Tonga.')
Q('Nauru', 'Su alianza con Australia, que paga su presupuesto y tiene veto sobre su seguridad.', 'China quiere su reconocimiento, ya obtenido en 2024.')
Q('Cook Is.', 'Que no se aleje de Nueva Zelanda, que no comprometa su defensa con China y que los minerales del lecho marino los exploten empresas aliadas.', 'China quiere minerales del lecho marino y un acuerdo de cooperación.')
Q('Tunisia', 'Que frene la migración hacia Italia, no se aleje de Occidente y no quiebre.', 'Rusia y China buscan influencia en el giro autoritario del gobierno y ofrecen créditos sin condiciones.')
Q('Mauritania', 'Un aliado estable frente al Sahel, que frene la migración hacia Canarias, su gas compartido con Senegal y cooperación militar.', 'China quiere su pesca y su hierro.')
Q('Burkina Faso', 'Frenar al yihadismo, que ya controla buena parte del territorio, y la presencia rusa, y que vuelva un gobierno civil.', 'Rusia quiere minas de oro, una refinería y presencia militar, y difundir propaganda antioccidental desde allí.')
Q('Chad', 'Que no se pase del todo a Rusia tras la salida de Francia y que siga conteniendo al yihadismo del lago Chad.', 'Rusia quiere reemplazar a Francia como socio militar y cerrar el cerco del Sahel.')
Q('Senegal', 'Un socio democrático estable, su petróleo y gas y cooperación en seguridad, aunque cerró las bases francesas.', 'China y Rusia buscan acercarse al gobierno soberanista con obras, pesca y propaganda.')
Q('Gambia', 'Estabilidad democrática y que no sea ruta de migración ni de drogas.', 'No tiene intereses relevantes.')
Q('Guinea-Bissau', 'Cortar la ruta de la cocaína hacia Europa y que vuelva el orden constitucional.', 'No tiene intereses relevantes.')
Q('Sierra Leone', 'Estabilidad democrática y que no sea ruta de la cocaína.', 'China quiere minería, pesca y un puerto pesquero.')
Q('Liberia', 'Su registro de buques, el mayor del mundo y con sede en EE.UU., y su estabilidad.', 'No tiene intereses relevantes.')
Q("Côte d'Ivoire", 'Un aliado estable en el golfo de Guinea, frente al avance yihadista y ruso del Sahel, y su cacao.', 'No tiene intereses relevantes más allá del comercio con China.')
Q('Togo', 'Contener el yihadismo en el norte y que no se pase a Rusia.', 'Rusia quiere un acuerdo militar y presencia en el golfo de Guinea.')
Q('Benin', 'Contener el yihadismo en el norte y que su puerto siga abierto.', 'China quiere el oleoducto que trae el petróleo de Níger hasta su costa.')
Q('Cabo Verde', 'Su posición atlántica y la cooperación contra el narcotráfico.', 'No tiene intereses relevantes.')
Q('Cameroon', 'Contener a Boko Haram en el norte y la guerra en las regiones anglófonas.', 'China quiere el puerto de Kribi, represas y obras.')
Q('Central African Rep.', 'Que no quede bajo control ruso y que se pacifique.', 'Rusia quiere oro, diamantes y madera a cambio de seguridad, y una base de influencia en el centro de África.')
Q('Gabon', 'Estabilidad tras el golpe, su petróleo y manganeso y que no se acerque a Rusia.', 'China quiere manganeso y madera.')
Q('Eq. Guinea', 'Que no haya base naval china en el Atlántico, frente a la costa este de EE.UU.', 'China quiere un puerto con uso militar en el Atlántico.')
Q('Congo', 'Su petróleo y estabilidad.', 'China quiere su petróleo y cobrar su deuda; Rusia, un oleoducto.')
Q('Rwanda', 'Su eficacia y sus tropas de paz, pero que deje de apoyar al M23 en el Congo.', 'No tiene intereses relevantes; China y Rusia evitan condenarla.')
Q('Burundi', 'Estabilidad y que no se involucre más en la guerra del Congo.', 'China y Rusia quieren minería (níquel, tierras raras).')
Q('S. Sudan', 'Que no vuelva a la guerra civil.', 'China quiere su petróleo.')
Q('Ethiopia', 'Estabilidad en el Cuerno de África, que la gran represa no provoque una guerra con Egipto y que no estalle otra guerra con Eritrea.', 'China quiere obras y cobrar su deuda; Rusia, influencia política y militar.')
Q('Somalia', 'Combatir a Al Shabaab y al Estado Islámico, y que el país no se fragmente.', 'No tiene intereses relevantes; Turquía y los Emiratos compiten allí.')
Q('Uganda', 'Estabilidad y su aporte a misiones de paz.', 'China quiere el petróleo del lago Alberto y el oleoducto.')
Q('Tanzania', 'Estabilidad y apertura.', 'China quiere obras, puertos (Bagamoyo) y minería.')
Q('Zambia', 'El cobre y el corredor de Lobito, financiado por EE.UU. y la UE.', 'China quiere el cobre y cobrar su deuda.')
Q('Zimbabwe', 'Reformas democráticas y que su litio no quede solo en manos chinas.', 'China quiere su litio, del que ya compró las principales minas.')
Q('Malawi', 'Estabilidad democrática.', 'No tiene intereses relevantes.')
Q('Mozambique', 'El gas de Cabo Delgado, que explotan TotalEnergies y ExxonMobil, y contener la insurgencia yihadista.', 'China quiere minería y obras; Rusia intentó con Wagner combatir la insurgencia en 2019.')
Q('Madagascar', 'Estabilidad tras el golpe y su grafito y níquel.', 'No tiene intereses relevantes.')
Q('Namibia', 'Su uranio, su petróleo nuevo y su estabilidad democrática.', 'China quiere su uranio, con la mina de Husab.')
Q('Botswana', 'Una democracia estable y sus diamantes.', 'No tiene intereses relevantes.')
Q('Lesotho', 'Estabilidad.', 'No tiene intereses relevantes.')
Q('eSwatini', 'Que siga reconociendo a Taiwán, el último país africano que lo hace.', 'China quiere que reconozca a Pekín.')
Q('Comoros', 'Estabilidad.', 'No tiene intereses relevantes.')
Q('Mauritius', 'Que el traspaso de Chagos preserve la base de Diego García, clave para EE.UU. en el océano Índico.', 'China quiere influencia en el Índico y que la base pierda respaldo.')
Q('Seychelles', 'Seguridad marítima frente a la piratería y la pesca ilegal.', 'No tiene intereses relevantes.')
Q('Saint Helena', 'La base de Ascensión, escala aérea y de espionaje en el Atlántico Sur.', 'No tiene intereses relevantes.')
Q('Br. Indian Ocean Ter.', 'Conservar Diego García, base de bombarderos y buques de EE.UU. en el Índico.', 'Que la base pierda respaldo internacional.')
Q('Djibouti', 'La base de Camp Lemonnier, la única base permanente de EE.UU. en África, junto al estrecho de Bab el-Mandeb.', 'China quiere su primera base naval en el exterior y el puerto de Doraleh.')
Q('Somaliland', 'Una base en Berbera y un aliado en el golfo de Adén.', 'China quiere que no sea reconocida, porque Somalilandia es aliada de Taiwán.')
Q('Kenya', 'Su aliado principal en África oriental: bases, la lucha contra Al Shabaab y la misión en Haití.', 'China quiere el tren Mombasa-Nairobi y cobrar la deuda.')
Q('Angola', 'El corredor de Lobito para sacar los minerales del Congo y Zambia sin China, y su petróleo.', 'China quiere su petróleo y cobrar su deuda.')
Q('Eritrea', 'Que no se acerque a Rusia ni desestabilice a Etiopía.', 'Rusia quiere acceso al puerto de Massawa en el mar Rojo.')
Q('Gabon', 'Estabilidad tras el golpe, su petróleo y manganeso y que no se acerque a Rusia.', 'China quiere manganeso y madera.')
Q('Ghana', 'Oro, cacao, una democracia estable y su cooperación de seguridad.', 'China quiere bauxita y minería; muchos mineros ilegales chinos operan allí.')
Q('Guinea', 'Bauxita y hierro fuera del control chino y que la junta entregue el poder.', 'China quiere la bauxita y el hierro de Simandou para su acero y su aluminio.')
Q('Faeroe Is.', 'Que siga alineada con la OTAN en el Atlántico Norte y vigile a los submarinos rusos.', 'Rusia quiere su acuerdo de pesca y acceso a sus puertos.')
