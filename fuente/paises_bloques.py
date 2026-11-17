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
