# Ficha de cada país: qué está en juego, cronología y datos cualitativos.
# Clave: nombre del país en el mapa (data/nombres_mapa.json).
# Campos: cap (capital), gob (gobierno: forma y poder real), soc (idiomas y religión),
# rec (recursos), eco (base de la economía), juego (qué está en juego), crono [(año, hecho)].
# Las cifras (población, PBI, etc.) salen de fuente/paises_datos.py.

PJ = {}
EXTRA = {}  # cifras a mano para lugares que el Factbook no cubre: {clave: {pob: (n, año), area: km2}}


def P(k, cap, gob, soc, rec, eco, juego, crono):
    PJ[k] = dict(cap=cap, gob=gob, soc=soc, rec=rec, eco=eco, juego=juego, crono=crono)


# ───────────────────────── América del Norte ─────────────────────────

P('United States of America', 'Washington D.C.',
  'República federal presidencialista con dos partidos dominantes; el poder real se reparte entre la presidencia, el aparato de seguridad nacional, Wall Street y las grandes tecnológicas.',
  'Inglés; español muy extendido. Mayoría cristiana (protestantes y católicos) y creciente población sin religión.',
  'Petróleo y gas de esquisto (primer productor mundial de ambos), carbón, tierras agrícolas, madera, cobre, oro, uranio.',
  'La mayor economía del mundo: servicios financieros, tecnología, defensa, energía y agroindustria; emite la moneda de reserva global.',
  'Sostener la hegemonía del dólar, el control de los océanos y la primacía tecnológica frente a China, mientras la polarización interna y la deuda pública erosionan la base del imperio.',
  [(1776, 'Declaración de independencia de las trece colonias.'),
   (1945, 'Sale de la Segunda Guerra Mundial como potencia dominante y funda el orden de Bretton Woods, la ONU y luego la OTAN.'),
   (1971, 'Fin de la convertibilidad del dólar en oro.'),
   (1991, 'Disolución de la URSS: queda como única superpotencia.'),
   (2001, 'Atentados del 11 de septiembre y comienzo de la «guerra contra el terrorismo».'),
   (2025, 'Ofensiva arancelaria contra aliados y rivales.'),
   (2026, 'Captura de Maduro en Venezuela y guerra con Irán junto a Israel.')])

P('Canada', 'Ottawa',
  'Monarquía constitucional parlamentaria y federal; reino de la Mancomunidad Británica.',
  'Inglés y francés (oficiales). Mayoría cristiana, con fuerte crecimiento de quienes no tienen religión.',
  'Petróleo (arenas bituminosas), gas, potasa, uranio, níquel, oro, madera, agua dulce.',
  'Exportadora de energía, minerales y manufacturas, casi toda hacia EE.UU.; banca concentrada y sólida.',
  'Cómo diversificar su comercio y su seguridad sin romper con EE.UU., del que depende para casi todo, y cómo defender el Ártico que se abre.',
  [(1867, 'Confederación del Dominio de Canadá.'),
   (1958, 'Firma del NORAD, la defensa aérea común con EE.UU.'),
   (1982, 'Repatriación de la constitución.'),
   (1994, 'Entra en vigor el TLCAN con EE.UU. y México.'),
   (2025, 'Aranceles de EE.UU. y amenazas de anexión; giro hacia Europa en defensa.')])

P('Mexico', 'Ciudad de México',
  'República federal presidencialista; un partido dominante concentra el poder desde 2018 y la reforma judicial de 2024 eligió a los jueces por voto popular. Los cárteles controlan amplias zonas.',
  'Español y 68 lenguas indígenas reconocidas. Mayoría católica.',
  'Petróleo, plata (primer productor mundial), cobre, oro, zinc, gas, madera.',
  'Manufactura integrada a EE.UU. (automotriz, electrónica), remesas, petróleo estatal en declive y turismo.',
  'Qué hace EE.UU. con los cárteles —declarados organizaciones terroristas— y con el comercio, del que depende el 80 % de sus exportaciones.',
  [(1821, 'Independencia de España.'),
   (1848, 'Pierde la mitad de su territorio en la guerra con EE.UU.'),
   (1910, 'Revolución mexicana.'),
   (1994, 'Entra en el TLCAN; levantamiento zapatista.'),
   (2006, 'Comienza la guerra contra el narcotráfico.'),
   (2025, 'EE.UU. designa terroristas a los cárteles y presiona con aranceles.')])

P('Greenland', 'Nuuk',
  'Territorio autónomo del Reino de Dinamarca; Copenhague conserva defensa y política exterior.',
  'Groenlandés y danés. Luteranismo.',
  'Pesca, tierras raras, uranio, hierro, zinc, petróleo y gas sin explotar.',
  'Pesca y subsidio anual de Dinamarca, que cubre más de la mitad del presupuesto.',
  'El Ártico y sus minerales: EE.UU. quiere comprarla o controlarla, y la isla busca la independencia sin caer en otra dependencia.',
  [(1721, 'Colonización danesa.'),
   (1951, 'Acuerdo de defensa: EE.UU. instala la base de Thule (hoy Pituffik).'),
   (1979, 'Autonomía interna.'),
   (2009, 'Autogobierno ampliado con derecho a la independencia.'),
   (2025, 'EE.UU. insiste en anexarla y Dinamarca refuerza su presencia militar.')])

P('Bermuda', 'Hamilton', 'Territorio británico de ultramar con autogobierno.', 'Inglés. Cristianismo.',
  'Ninguno relevante.', 'Reaseguros y servicios financieros extraterritoriales; turismo.',
  'Su papel de centro de reaseguros y de paraíso fiscal frente a la presión de la OCDE por el impuesto mínimo global.',
  [(1612, 'Colonización inglesa.'), (1968, 'Constitución con autogobierno.'),
   (1995, 'Referéndum: rechaza la independencia.'), (2023, 'Aprueba un impuesto a las grandes empresas por el mínimo global.')])

P('St. Pierre and Miquelon', 'Saint-Pierre', 'Colectividad francesa de ultramar.', 'Francés. Catolicismo.',
  'Pesca.', 'Administración pública y pesca, con subsidios de París.',
  'Los derechos de pesca y la plataforma marítima frente a Canadá.',
  [(1763, 'Queda para Francia tras la Guerra de los Siete Años.'), (1992, 'Un tribunal arbitral fija su zona marítima frente a Canadá.'), (2003, 'Pasa a ser colectividad de ultramar.')])

# ───────────────────────── Centroamérica ─────────────────────────

P('Guatemala', 'Ciudad de Guatemala',
  'República presidencialista con instituciones capturadas por élites económicas y redes de corrupción.',
  'Español y 22 lenguas mayas. Católicos y evangélicos.',
  'Petróleo, níquel, maderas, pesca, tierras para café, azúcar y cardamomo.',
  'Agroexportación, remesas desde EE.UU. (cerca de una quinta parte del PBI) y maquila.',
  'Si el gobierno logra contener a las redes que capturaron fiscalía y justicia, y su papel como corredor de la droga y la migración hacia EE.UU.',
  [(1954, 'Golpe apoyado por la CIA contra Árbenz.'), (1960, 'Comienza una guerra civil de 36 años.'),
   (1996, 'Acuerdos de paz.'), (2019, 'Expulsión de la comisión de la ONU contra la impunidad (CICIG).'),
   (2024, 'Asume un gobierno reformista tras intentos de la fiscalía de impedirlo.')])

P('Belize', 'Belmopán', 'Monarquía constitucional parlamentaria; reino de la Mancomunidad Británica.',
  'Inglés (oficial), español y criollo. Católicos y protestantes.',
  'Maderas, pesca, tierras agrícolas, petróleo.', 'Turismo, azúcar, bananas, cítricos y pesca.',
  'El reclamo guatemalteco sobre su territorio, en manos de la Corte Internacional de Justicia, y el narcotráfico por su costa.',
  [(1862, 'Colonia de Honduras Británica.'), (1981, 'Independencia del Reino Unido.'), (2019, 'Referéndum para llevar el diferendo con Guatemala a La Haya.')])

P('Honduras', 'Tegucigalpa', 'República presidencialista con instituciones débiles y fuerte peso de las fuerzas armadas.',
  'Español. Católicos y evangélicos.', 'Maderas, oro, plata, zinc, pesca, hidroelectricidad.',
  'Remesas, maquila, café y bananas.',
  'La violencia de las maras y el narcotráfico, la base estadounidense de Soto Cano y la oscilación entre Taiwán y China.',
  [(1980, 'Base de Soto Cano: plataforma de EE.UU. contra la Nicaragua sandinista.'), (2009, 'Golpe contra Zelaya.'),
   (2022, 'Un expresidente es extraditado a EE.UU. por narcotráfico.'), (2023, 'Rompe con Taiwán y reconoce a China.')])

P('El Salvador', 'San Salvador', 'República presidencialista con el poder concentrado en el presidente desde 2019; reelección inmediata y estado de excepción permanente.',
  'Español. Católicos y evangélicos.', 'Hidroelectricidad, geotermia, tierras agrícolas.',
  'Remesas, maquila y servicios; dolarizada desde 2001.',
  'Si la seguridad lograda con encarcelamiento masivo se sostiene sin contrapesos, y su papel como cárcel tercerizada de EE.UU.',
  [(1980, 'Guerra civil.'), (1992, 'Acuerdos de paz.'), (2001, 'Dolarización.'),
   (2022, 'Estado de excepción y encarcelamiento masivo de pandilleros.'), (2025, 'Recibe en el CECOT a deportados desde EE.UU.')])

P('Costa Rica', 'San José', 'República presidencialista sin ejército desde 1948; democracia estable.',
  'Español. Mayoría católica.', 'Hidroelectricidad, biodiversidad, tierras agrícolas.',
  'Dispositivos médicos, servicios, turismo y agroexportación.',
  'El avance del narcotráfico, que convirtió al país en plataforma de cocaína hacia Europa y elevó los homicidios.',
  [(1821, 'Independencia.'), (1948, 'Guerra civil breve y abolición del ejército.'), (1987, 'Premio Nobel de la Paz por el plan de paz centroamericano.'), (2023, 'Récord de homicidios por el narcotráfico.')])

P('Panama', 'Ciudad de Panamá', 'República presidencialista; economía dolarizada y élite comercial y financiera.',
  'Español. Mayoría católica.', 'Posición geográfica, cobre, maderas, pesca.',
  'El canal, servicios financieros y logísticos, zona libre de Colón; la mina de cobre está cerrada.',
  'El control del canal: EE.UU. reclama prioridad y presionó para sacar a la empresa de Hong Kong de los puertos.',
  [(1903, 'Separación de Colombia con apoyo de EE.UU.; tratado del canal.'), (1977, 'Tratados Torrijos-Carter.'),
   (1989, 'Invasión de EE.UU. y caída de Noriega.'), (1999, 'Panamá recibe el canal.'),
   (2023, 'Protestas masivas cierran la mina de cobre.'), (2025, 'Presión de EE.UU. sobre el canal y venta de los puertos de CK Hutchison.')])

P('Nicaragua', 'Managua', 'Régimen familiar de partido dominante; la copresidencia de Ortega y Murillo concentra todos los poderes desde la reforma de 2025.',
  'Español. Católicos y evangélicos.', 'Oro, maderas, pesca, tierras agrícolas.',
  'Oro, remesas, maquila, café y carne.',
  'La supervivencia del régimen bajo sanciones, la sucesión dentro de la familia y su alianza con Rusia y China.',
  [(1979, 'Revolución sandinista.'), (1990, 'Derrota electoral sandinista.'), (2007, 'Ortega vuelve al poder.'),
   (2018, 'Represión de las protestas: cientos de muertos.'), (2023, 'Destierro de presos políticos y quita de nacionalidad.')])

# ───────────────────────── Caribe ─────────────────────────

P('Cuba', 'La Habana', 'Estado de partido único comunista; las fuerzas armadas controlan la economía de divisas a través de GAESA.',
  'Español. Católicos, sincretismo afrocubano y muchos sin religión.', 'Níquel, cobalto, petróleo, tierras agrícolas.',
  'Turismo, remesas, servicios médicos en el exterior, níquel y tabaco.',
  'Si el régimen sobrevive a la peor crisis desde los noventa —apagones, éxodo de más de un millón de personas— y a la presión de EE.UU. tras la caída de Maduro.',
  [(1959, 'Revolución cubana.'), (1962, 'Crisis de los misiles.'), (1991, 'Fin del subsidio soviético: «período especial».'),
   (2015, 'Deshielo con EE.UU., revertido en 2017.'), (2021, 'Protestas masivas del 11 de julio.'),
   (2026, 'Pierde el petróleo venezolano y se agrava la crisis energética.')])

P('Haiti', 'Puerto Príncipe', 'Estado colapsado: un consejo de transición sin elecciones desde 2016; las pandillas controlan la mayor parte de la capital.',
  'Criollo haitiano y francés. Católicos, protestantes y vudú.', 'Bauxita, cobre, mármol, tierras agrícolas.',
  'Remesas, ayuda externa y maquila.',
  'Si una fuerza internacional puede recuperar el control frente a las pandillas, y quién paga.',
  [(1804, 'Primera república negra independiente.'), (1915, 'Ocupación de EE.UU. hasta 1934.'), (1986, 'Caída de los Duvalier.'),
   (2010, 'Terremoto: unos 200.000 muertos.'), (2021, 'Asesinato del presidente Moïse.'), (2024, 'Llega la misión de seguridad liderada por Kenia.')])

P('Dominican Rep.', 'Santo Domingo', 'República presidencialista estable.', 'Español. Católicos y evangélicos.',
  'Oro, níquel, plata, bauxita.', 'Turismo, zonas francas, remesas y minería; una de las de mayor crecimiento de América Latina.',
  'La frontera con Haití y el control migratorio, y su papel como escala del narcotráfico.',
  [(1844, 'Independencia de Haití.'), (1930, 'Dictadura de Trujillo hasta 1961.'), (1965, 'Intervención de EE.UU.'), (2013, 'Fallo que quita la nacionalidad a descendientes de haitianos.')])

P('Jamaica', 'Kingston', 'Monarquía constitucional parlamentaria; reino de la Mancomunidad Británica.', 'Inglés y patois. Protestantes.',
  'Bauxita, yeso, piedra caliza.', 'Turismo, remesas, bauxita y alúmina.',
  'La violencia de las bandas y el debate sobre convertirse en república.',
  [(1655, 'Conquista inglesa.'), (1962, 'Independencia.'), (2010, 'Operativo en Tivoli Gardens por la extradición de un capo a EE.UU.')])

P('Trinidad and Tobago', 'Puerto España', 'República parlamentaria.', 'Inglés. Cristianos, hindúes y musulmanes.',
  'Petróleo, gas, asfalto.', 'Gas natural licuado y petroquímica; centro financiero del Caribe.',
  'El declive del gas, los acuerdos de gas con Venezuela y el uso de su territorio en las operaciones de EE.UU. en el Caribe.',
  [(1962, 'Independencia.'), (1990, 'Intento de golpe islamista.'), (2025, 'Apoya el despliegue naval de EE.UU. frente a Venezuela.')])

P('Bahamas', 'Nasáu', 'Monarquía constitucional parlamentaria; reino de la Mancomunidad Británica.', 'Inglés. Protestantes.',
  'Sal, aragonita, pesca.', 'Turismo y servicios financieros extraterritoriales.',
  'Su lugar como paraíso fiscal y escala marítima del narcotráfico hacia EE.UU.',
  [(1973, 'Independencia.'), (2019, 'Huracán Dorian.'), (2022, 'Quiebra de FTX, con sede en Nasáu.')])

P('Puerto Rico', 'San Juan', 'Estado libre asociado: territorio no incorporado de EE.UU.; sin voto en el Congreso.',
  'Español e inglés. Católicos y protestantes.', 'Cobre, níquel, potencial petrolero.',
  'Farmacéutica, manufactura, turismo y fondos federales; salió de la quiebra en 2022.',
  'Su estatus —estado, independencia o colonia— y su papel en el despliegue militar de EE.UU. en el Caribe.',
  [(1898, 'Pasa de España a EE.UU.'), (1917, 'Ciudadanía estadounidense.'), (1952, 'Estado libre asociado.'),
   (2017, 'Huracán María y quiebra del gobierno.'), (2025, 'Reapertura de la base de Roosevelt Roads para operaciones en el Caribe.')])

P('Antigua and Barb.', "Saint John's", 'Monarquía constitucional parlamentaria; reino de la Mancomunidad Británica.', 'Inglés. Protestantes.',
  'Ninguno relevante.', 'Turismo, ciudadanía por inversión y servicios financieros.',
  'La venta de pasaportes bajo presión de EE.UU. y la UE.', [(1981, 'Independencia.'), (2009, 'Cae el Stanford International Bank por fraude.')])
P('Barbados', 'Bridgetown', 'República parlamentaria desde 2021.', 'Inglés. Protestantes.', 'Petróleo, pesca.',
  'Turismo y servicios financieros extraterritoriales.', 'Su liderazgo en el reclamo de reparaciones por la esclavitud y de financiamiento climático.',
  [(1966, 'Independencia.'), (2021, 'Deja la monarquía británica y se vuelve república.')])
P('Dominica', 'Roseau', 'República parlamentaria.', 'Inglés y criollo francés. Católicos.', 'Maderas, hidroelectricidad.',
  'Turismo, ciudadanía por inversión y bananas.', 'La venta de pasaportes y la reconstrucción tras los huracanes.', [(1978, 'Independencia.'), (2017, 'Huracán María.')])
P('Grenada', "Saint George's", 'Monarquía constitucional parlamentaria; reino de la Mancomunidad Británica.', 'Inglés. Católicos y protestantes.',
  'Maderas, pesca.', 'Turismo, nuez moscada y ciudadanía por inversión.', 'La venta de pasaportes y la vulnerabilidad a los huracanes.',
  [(1974, 'Independencia.'), (1983, 'Invasión de EE.UU. tras un golpe interno.')])
P('St. Kitts and Nevis', 'Basseterre', 'Monarquía constitucional parlamentaria y federal; reino de la Mancomunidad Británica.', 'Inglés. Protestantes.',
  'Arena, tierras agrícolas.', 'Turismo y ciudadanía por inversión, la mayor fuente de ingresos del Estado.',
  'El programa de pasaportes, el más antiguo del mundo, ante la presión de EE.UU. y la UE.', [(1983, 'Independencia.'), (1984, 'Lanza la ciudadanía por inversión.')])
P('Saint Lucia', 'Castries', 'Monarquía constitucional parlamentaria; reino de la Mancomunidad Británica.', 'Inglés y criollo francés. Católicos.',
  'Pesca, geotermia, maderas.', 'Turismo y ciudadanía por inversión.', 'La dependencia del turismo y del programa de pasaportes.', [(1979, 'Independencia.')])
P('St. Vin. and Gren.', 'Kingstown', 'Monarquía constitucional parlamentaria; reino de la Mancomunidad Británica.', 'Inglés. Protestantes.',
  'Hidroelectricidad, tierras agrícolas.', 'Turismo, bananas y remesas.', 'La reconstrucción tras huracanes y erupciones.', [(1979, 'Independencia.'), (2021, 'Erupción del volcán La Soufrière.'), (2024, 'Huracán Beryl.')])

P('U.S. Virgin Is.', 'Charlotte Amalie', 'Territorio no incorporado de EE.UU. con autogobierno.', 'Inglés. Protestantes.', 'Ninguno relevante.',
  'Turismo y refinación.', 'Su régimen fiscal especial y la dependencia de fondos federales.', [(1917, 'EE.UU. compra las islas a Dinamarca.')])
P('Anguilla', 'The Valley', 'Territorio británico de ultramar.', 'Inglés. Protestantes.', 'Sal, pesca, dominio .ai.',
  'Turismo, servicios financieros y la venta de dominios .ai, que ya aporta una parte grande del presupuesto.',
  'Los ingresos inesperados del dominio de internet .ai.', [(1969, 'Se separa de San Cristóbal; intervención británica.'), (1980, 'Territorio británico separado.')])
P('Cayman Is.', 'George Town', 'Territorio británico de ultramar con autogobierno.', 'Inglés. Protestantes.', 'Pesca.',
  'Uno de los mayores centros financieros extraterritoriales: fondos de inversión y empresas sin impuestos.',
  'Su papel de paraíso fiscal frente al impuesto mínimo global y los registros de beneficiarios finales.',
  [(1670, 'Pasa a Inglaterra.'), (1962, 'Elige seguir británica cuando Jamaica se independiza.'), (1966, 'Ley de bancos que lo lanza como centro extraterritorial.')])
P('British Virgin Is.', 'Road Town', 'Territorio británico de ultramar; Londres tomó amenazas de gobierno directo en 2022.', 'Inglés. Protestantes.', 'Ninguno relevante.',
  'Registro de sociedades extraterritoriales y turismo.', 'Su modelo de empresas pantalla, expuesto en los Papeles de Panamá.',
  [(1672, 'Colonia inglesa.'), (2016, 'Papeles de Panamá: la mitad de las sociedades de Mossack Fonseca estaban allí.'), (2022, 'Arresto de su jefe de gobierno en EE.UU. por narcotráfico.')])
P('Turks and Caicos Is.', 'Cockburn Town', 'Territorio británico de ultramar.', 'Inglés. Protestantes.', 'Pesca.',
  'Turismo y servicios financieros.', 'La corrupción y la migración irregular desde Haití.', [(2009, 'Londres suspende el autogobierno por corrupción hasta 2012.')])
P('Montserrat', 'Plymouth (abandonada); gobierno en Brades', 'Territorio británico de ultramar.', 'Inglés. Protestantes.', 'Ninguno relevante.',
  'Ayuda británica.', 'La recuperación tras la erupción que dejó inhabitable el sur.', [(1995, 'Erupción del volcán Soufrière Hills: la capital queda sepultada.')])
P('Aruba', 'Oranjestad', 'País autónomo del Reino de los Países Bajos.', 'Papiamento y neerlandés. Católicos.', 'Playas.',
  'Turismo.', 'Su cercanía a Venezuela y su papel en las operaciones antinarcóticos.', [(1986, 'Status aparte dentro del reino.')])
P('Curaçao', 'Willemstad', 'País autónomo del Reino de los Países Bajos.', 'Papiamento y neerlandés. Católicos.', 'Calizas.',
  'Turismo, refinación (cerrada) y servicios financieros.', 'La refinería que operaba Venezuela y la base antinarcóticos de EE.UU.', [(2010, 'Pasa a ser país autónomo dentro del reino.'), (2019, 'Cierra la refinería Isla.')])
P('St-Martin', 'Marigot', 'Colectividad francesa de ultramar.', 'Francés. Católicos.', 'Ninguno relevante.', 'Turismo.',
  'La reconstrucción y la frontera abierta con la parte neerlandesa.', [(1648, 'División de la isla entre Francia y Países Bajos.'), (2017, 'Huracán Irma.')])
P('St-Barthélemy', 'Gustavia', 'Colectividad francesa de ultramar.', 'Francés. Católicos.', 'Ninguno relevante.', 'Turismo de lujo.',
  'Su régimen fiscal propio.', [(1878, 'Suecia la devuelve a Francia.'), (2007, 'Colectividad de ultramar separada de Guadalupe.')])
P('Sint Maarten', 'Philipsburg', 'País autónomo del Reino de los Países Bajos.', 'Inglés y neerlandés. Protestantes y católicos.', 'Ninguno relevante.',
  'Turismo y cruceros.', 'La gobernanza y la reconstrucción con fondos neerlandeses.', [(2010, 'País autónomo dentro del reino.'), (2017, 'Huracán Irma.')])

# ───────────────────────── Sudamérica ─────────────────────────

P('Colombia', 'Bogotá', 'República presidencialista unitaria; grupos armados y redes del narcotráfico controlan amplias regiones.',
  'Español. Mayoría católica.', 'Petróleo, carbón, oro, esmeraldas, níquel, gas, hidroelectricidad.',
  'Petróleo, carbón, café, flores, servicios; la cocaína es la mayor economía ilegal.',
  'Si el Estado recupera el territorio de las disidencias de las FARC, el ELN y el Clan del Golfo, y cómo se recompone la relación con EE.UU.',
  [(1819, 'Independencia.'), (1948, 'El Bogotazo abre la Violencia.'), (1964, 'Nacen las FARC y el ELN.'),
   (1993, 'Muerte de Pablo Escobar.'), (2016, 'Acuerdo de paz con las FARC.'), (2026, 'Asume un gobierno de derecha tras el de Petro.')])

P('Venezuela', 'Caracas', 'Protectorado de EE.UU. en transición desde la captura de Maduro en enero de 2026; el chavismo residual y los militares conservan cuotas de poder.',
  'Español. Mayoría católica.', 'Las mayores reservas probadas de petróleo del mundo, gas, oro, coltán, hierro, bauxita.',
  'Petróleo; la economía cayó cerca de tres cuartas partes entre 2013 y 2021 y casi 8 millones emigraron.',
  'Quién controla el petróleo y la transición: EE.UU., las petroleras, los restos del chavismo o una oposición que no gobernó nunca.',
  [(1811, 'Declaración de independencia.'), (1976, 'Nacionalización del petróleo.'), (1999, 'Llega Chávez al poder.'),
   (2013, 'Muere Chávez; lo sucede Maduro.'), (2024, 'Fraude electoral denunciado por la oposición.'), (2026, 'EE.UU. captura a Maduro y toma el control de la transición.')])

P('Ecuador', 'Quito', 'República presidencialista unitaria; estado de «conflicto armado interno» contra las bandas desde 2024.',
  'Español; kichwa y shuar en uso oficial regional. Mayoría católica.', 'Petróleo, cobre, oro, pesca, maderas, hidroelectricidad.',
  'Petróleo, bananas (primer exportador mundial), camarón; dolarizada desde 2000.',
  'Si el Estado frena a las bandas ligadas a los cárteles mexicanos y a la mafia albanesa que usan sus puertos para mandar cocaína.',
  [(1830, 'Se separa de la Gran Colombia.'), (2000, 'Dolarización.'), (2009, 'Cierre de la base estadounidense de Manta.'),
   (2023, 'Asesinato del candidato Villavicencio.'), (2024, 'Declaración de conflicto armado interno.')])

P('Peru', 'Lima', 'República presidencialista con un Congreso fragmentado que destituye presidentes con frecuencia.',
  'Español, quechua y aimara. Mayoría católica.', 'Cobre, oro, plata, zinc, gas, pesca, fosfatos.',
  'Minería, pesca, agroexportación; el puerto de Chancay, de capital chino, abrió en 2024.',
  'La rivalidad entre EE.UU. y China por el puerto de Chancay, la minería ilegal de oro y la inestabilidad política crónica.',
  [(1821, 'Independencia.'), (1980, 'Sendero Luminoso inicia la lucha armada.'), (1992, 'Autogolpe de Fujimori.'),
   (2022, 'Destitución de Castillo tras intentar cerrar el Congreso.'), (2024, 'Inauguración del puerto de Chancay.'), (2026, 'Asume un nuevo gobierno tras las elecciones.')])

P('Bolivia', 'La Paz (sede de gobierno); Sucre (capital constitucional)', 'República presidencialista unitaria y plurinacional.',
  'Español y 36 lenguas indígenas oficiales. Mayoría católica.', 'Litio (las mayores reservas del mundo), gas, estaño, plata, zinc, oro.',
  'Gas en declive, minería, soja; crisis de dólares y de combustibles desde 2023.',
  'Quién explota el litio —China, Rusia u Occidente— y cómo sale el país de la crisis económica tras dos décadas de MAS.',
  [(1825, 'Independencia.'), (1952, 'Revolución nacional.'), (2006, 'Llega Evo Morales; nacionalización de los hidrocarburos.'),
   (2019, 'Crisis y renuncia de Morales.'), (2025, 'El MAS pierde el poder en las elecciones.')])

P('Chile', 'Santiago', 'República presidencialista unitaria con instituciones sólidas.', 'Español. Católicos y evangélicos.',
  'Cobre (primer productor mundial), litio, molibdeno, plata, oro, pesca, madera.',
  'Minería, agroexportación, celulosa, salmón y servicios financieros.',
  'Cómo reparte el litio entre el Estado y los privados, y cómo equilibra a China, su mayor comprador, con EE.UU.',
  [(1818, 'Independencia.'), (1973, 'Golpe de Pinochet.'), (1990, 'Retorno de la democracia.'),
   (2019, 'Estallido social.'), (2023, 'Segundo proyecto constitucional rechazado.'), (2026, 'Asume un gobierno de derecha.')])

P('Argentina', 'Buenos Aires', 'República presidencialista federal; gobierno alineado con EE.UU. desde 2023.',
  'Español. Católicos y evangélicos.', 'Tierras de la pampa, petróleo y gas de Vaca Muerta, litio, cobre, plata, oro.',
  'Agroindustria (soja, maíz, carne), energía y minería en expansión, industria y servicios.',
  'Si la estabilización económica se sostiene, el rescate y el alineamiento con EE.UU. frente a China, y el reclamo por Malvinas.',
  [(1816, 'Independencia.'), (1946, 'Llega Perón.'), (1976, 'Golpe militar y represión ilegal.'), (1982, 'Guerra de Malvinas.'),
   (2001, 'Default y crisis.'), (2023, 'Gana Milei.'), (2025, 'Rescate financiero de EE.UU.')])

P('Uruguay', 'Montevideo', 'República presidencialista unitaria; una de las democracias más estables del continente.',
  'Español. Católicos y gran proporción sin religión.', 'Tierras agrícolas, hidroelectricidad, pesca.',
  'Carne, celulosa, soja, lácteos, servicios y software.',
  'El puerto de Montevideo como escala de la cocaína hacia Europa y cómo comerciar con China sin romper el Mercosur.',
  [(1828, 'Independencia.'), (1973, 'Golpe cívico-militar.'), (1985, 'Retorno de la democracia.'), (2013, 'Legaliza el cannabis.')])

P('Paraguay', 'Asunción', 'República presidencialista dominada por el Partido Colorado desde 1947.', 'Español y guaraní. Mayoría católica.',
  'Hidroelectricidad (Itaipú y Yacyretá), tierras agrícolas, maderas.', 'Soja, carne, energía y comercio de triangulación.',
  'La Triple Frontera, el contrabando y el narcotráfico, y su reconocimiento de Taiwán.',
  [(1811, 'Independencia.'), (1870, 'Pierde la Guerra de la Triple Alianza.'), (1954, 'Dictadura de Stroessner hasta 1989.'),
   (1984, 'Itaipú empieza a generar.'), (2023, 'EE.UU. sanciona a un expresidente por corrupción.')])

P('Brazil', 'Brasilia', 'República presidencialista federal; un Congreso fragmentado y el Supremo Tribunal tienen un peso decisivo.',
  'Portugués. Católicos y evangélicos en rápido crecimiento.', 'Hierro, petróleo del presal, niobio, bauxita, oro, madera, agua, tierras.',
  'Agroindustria (soja, carne, azúcar, café), petróleo, minería, industria y servicios.',
  'Su autonomía frente a EE.UU. y China, la Amazonía con minería ilegal y facciones criminales, y la polarización interna.',
  [(1822, 'Independencia de Portugal.'), (1964, 'Golpe militar.'), (1985, 'Retorno de la democracia.'), (1994, 'Plan Real.'),
   (2014, 'Operación Lava Jato.'), (2023, 'Asalto a los tres poderes en Brasilia.'), (2025, 'Condena de Bolsonaro y aranceles de EE.UU.')])

P('Guyana', 'Georgetown', 'República con presidente elegido por lista parlamentaria; política dividida por origen étnico.',
  'Inglés. Hindúes, cristianos y musulmanes.', 'Petróleo, oro, bauxita, diamantes, maderas.',
  'Petróleo operado por ExxonMobil: la economía de más rápido crecimiento del mundo.',
  'El reclamo de Venezuela sobre el Esequibo y cómo se reparte la renta petrolera.',
  [(1966, 'Independencia.'), (2015, 'Descubrimiento de petróleo frente a la costa.'), (2019, 'Primera producción.'), (2023, 'Venezuela convoca un referéndum para anexar el Esequibo.')])

P('Suriname', 'Paramaribo', 'República parlamentaria.', 'Neerlandés y sranan tongo. Cristianos, hindúes y musulmanes.',
  'Oro, bauxita, petróleo, maderas.', 'Oro, petróleo y el próximo desarrollo petrolero marino.',
  'El petróleo marino que empieza a explotarse y la memoria del narcotráfico en la élite.',
  [(1975, 'Independencia.'), (1980, 'Golpe de Bouterse.'), (2019, 'Condena de Bouterse por los asesinatos de 1982.'), (2020, 'Descubrimiento de petróleo marino.')])

P('Falkland Is.', 'Puerto Argentino / Stanley', 'Territorio británico de ultramar con autogobierno; reclamado por la Argentina.',
  'Inglés. Cristianos.', 'Pesca, petróleo en la plataforma.', 'Licencias de pesca de calamar, cría de ovejas y turismo.',
  'La soberanía, el petróleo de la cuenca norte y la base de Mount Pleasant, que proyecta al Reino Unido sobre el Atlántico Sur y la Antártida.',
  [(1833, 'Ocupación británica.'), (1965, 'La ONU llama a negociar la soberanía.'), (1982, 'Guerra de Malvinas.'), (2013, 'Referéndum de los isleños por seguir británicos.')])

P('S. Geo. and the Is.', 'King Edward Point', 'Territorio británico de ultramar sin población permanente; reclamado por la Argentina.',
  'Inglés.', 'Pesca, krill.', 'Licencias de pesca.', 'El acceso a la Antártida y a la pesca del Atlántico Sur.',
  [(1775, 'Cook toma posesión.'), (1982, 'Desembarco argentino y recuperación británica.')])

# ───────────────────────── Europa occidental ─────────────────────────

P('United Kingdom', 'Londres', 'Monarquía constitucional parlamentaria; la City de Londres y el aparato de seguridad conservan un peso propio.',
  'Inglés; galés y gaélico. Cristianos, musulmanes y muchos sin religión.', 'Petróleo y gas del mar del Norte, carbón, tierras agrícolas.',
  'Finanzas, servicios, defensa, farmacéutica; la City administra la red de territorios con secreto fiscal.',
  'Su lugar fuera de la UE, la unidad del reino frente al independentismo escocés y su papel como socio nuclear de EE.UU.',
  [(1707, 'Unión de Inglaterra y Escocia.'), (1945, 'Comienza la descolonización del imperio.'), (1973, 'Entra en la Comunidad Europea.'),
   (1998, 'Acuerdo de Viernes Santo en Irlanda del Norte.'), (2020, 'Sale de la UE.'), (2021, 'Pacto AUKUS con EE.UU. y Australia.')])

P('Ireland', 'Dublín', 'República parlamentaria.', 'Inglés e irlandés. Mayoría católica.', 'Gas, turba, zinc, plomo, tierras agrícolas.',
  'Sedes europeas de grandes tecnológicas y farmacéuticas atraídas por impuestos bajos; agroindustria.',
  'Su modelo de impuestos bajos frente al mínimo global y a los aranceles de EE.UU., y la frontera con Irlanda del Norte tras el Brexit.',
  [(1922, 'Estado Libre Irlandés.'), (1949, 'República.'), (1973, 'Entra en la Comunidad Europea.'), (2016, 'La UE ordena a Apple devolver 13.000 millones en impuestos (confirmado en 2024).')])

P('France', 'París', 'República semipresidencialista; el presidente concentra defensa y política exterior.',
  'Francés. Católicos, musulmanes y muchos sin religión.', 'Tierras agrícolas, uranio (importado), bosques, pesca.',
  'Industria aeroespacial, nuclear, lujo, agroindustria, turismo; deuda pública alta.',
  'Su autonomía estratégica como única potencia nuclear de la UE, la pérdida del Sahel y la inestabilidad política interna.',
  [(1789, 'Revolución francesa.'), (1958, 'Quinta República.'), (1962, 'Independencia de Argelia.'), (1966, 'Sale del mando militar de la OTAN (vuelve en 2009).'),
   (2023, 'Expulsión de sus tropas de Malí, Burkina Faso y Níger.'), (2024, 'Disolución de la Asamblea y parlamento sin mayoría.')])

P('Germany', 'Berlín', 'República parlamentaria federal.', 'Alemán. Católicos, protestantes, musulmanes y muchos sin religión.',
  'Carbón, lignito, potasa, sal, tierras agrícolas.', 'Industria (automotriz, química, maquinaria), exportaciones; en estancamiento desde 2023.',
  'Su rearme tras perder el gas ruso, el futuro de su industria frente a China y EE.UU., y el ascenso de la ultraderecha.',
  [(1871, 'Unificación.'), (1945, 'Derrota y división.'), (1990, 'Reunificación.'), (2008, 'Merkel frena en Bucarest el plan de ingreso de Ucrania y Georgia a la OTAN.'), (2011, 'Tras Fukushima acelera el abandono nuclear; se inaugura Nord Stream 1.'), (2022, 'Fin del gas ruso, del que dependía en más de la mitad; voladura de Nord Stream y fondo de rearme.'), (2023, 'Cierra sus últimos reactores nucleares.'), (2025, 'Reforma constitucional para financiar la defensa.')])

P('Italy', 'Roma', 'República parlamentaria.', 'Italiano. Mayoría católica.', 'Gas, mármol, tierras agrícolas, pesca.',
  'Industria del norte, lujo, turismo; deuda pública muy alta.',
  'La deuda, la migración por el Mediterráneo y el poder de la \'Ndrangheta en el tráfico de cocaína europeo.',
  [(1861, 'Unificación.'), (1922, 'Fascismo.'), (1946, 'República.'), (1992, 'Mani Pulite y asesinatos de Falcone y Borsellino.')])

P('Spain', 'Madrid', 'Monarquía parlamentaria con autonomías amplias.', 'Español; catalán, gallego y euskera cooficiales. Mayoría católica.',
  'Tierras agrícolas, carbón, hierro, cobre, zinc, sol y viento.', 'Turismo, servicios, agroindustria, automotriz; crece más que la media europea.',
  'La fragmentación parlamentaria, el independentismo catalán y su frontera sur con Marruecos.',
  [(1939, 'Fin de la guerra civil y dictadura de Franco.'), (1978, 'Constitución democrática.'), (1986, 'Entra en la Comunidad Europea y confirma la OTAN.'),
   (2004, 'Atentados del 11-M.'), (2017, 'Referéndum ilegal en Cataluña.')])

P('Portugal', 'Lisboa', 'República semipresidencialista.', 'Portugués. Mayoría católica.', 'Pesca, corcho, litio, tungsteno, sol y viento.',
  'Turismo, servicios, industria liviana.', 'La estabilidad de gobiernos minoritarios y su papel atlántico por las Azores.',
  [(1910, 'República.'), (1974, 'Revolución de los Claveles.'), (1986, 'Entra en la Comunidad Europea.')])

P('Netherlands', 'Ámsterdam (sede de gobierno en La Haya)', 'Monarquía constitucional parlamentaria.', 'Neerlandés. Católicos, protestantes y mayoría sin religión.',
  'Gas, petróleo, tierras agrícolas.', 'Comercio (puerto de Róterdam), agroexportación, finanzas y ASML, clave para los chips avanzados.',
  'Las restricciones a la venta de máquinas de chips a China y la guerra contra la mafia de la cocaína.',
  [(1581, 'Independencia de España.'), (1949, 'Independencia de Indonesia.'), (2021, 'Asesinato del periodista Peter R. de Vries por la mafia.'), (2023, 'Restringe exportaciones de ASML a China.')])

P('Belgium', 'Bruselas', 'Monarquía constitucional parlamentaria y federal dividida entre flamencos y francófonos.', 'Neerlandés, francés y alemán. Católicos y muchos sin religión.',
  'Arena, carbón.', 'Servicios, química, logística (Amberes) y finanzas.',
  'Las reservas rusas inmovilizadas en Euroclear y el narcotráfico por el puerto de Amberes.',
  [(1830, 'Independencia.'), (1960, 'Independencia del Congo.'), (1993, 'Federalización.'), (2022, 'Congela los activos del banco central ruso en Euroclear.')])

P('Luxembourg', 'Luxemburgo', 'Monarquía constitucional (gran ducado).', 'Luxemburgués, francés y alemán. Católicos.',
  'Hierro (agotado).', 'Finanzas y fondos de inversión; sede de instituciones europeas.',
  'Su papel en la planificación fiscal de las multinacionales.', [(1867, 'Neutralidad garantizada.'), (2014, 'LuxLeaks expone sus acuerdos fiscales.')])

P('Switzerland', 'Berna', 'República federal con democracia directa y un gobierno colegiado.', 'Alemán, francés, italiano y romanche. Católicos, protestantes y muchos sin religión.',
  'Hidroelectricidad, madera, sal.', 'Banca privada, farmacéutica, maquinaria de precisión y comercio de materias primas.',
  'Su neutralidad tras sumarse a las sanciones contra Rusia y su secreto bancario en retirada.',
  [(1291, 'Pacto fundador.'), (1815, 'Neutralidad reconocida.'), (2009, 'Cede el secreto bancario ante EE.UU.'), (2022, 'Adopta las sanciones de la UE contra Rusia.'), (2023, 'Rescate de Credit Suisse por UBS.')])

P('Austria', 'Viena', 'República parlamentaria federal; neutral.', 'Alemán. Católicos.', 'Hierro, madera, hidroelectricidad, grafito.',
  'Industria, turismo y banca con fuerte presencia en Europa del Este.', 'Su neutralidad, el gas ruso y los servicios de inteligencia que operan en Viena.',
  [(1918, 'Fin del Imperio austrohúngaro.'), (1955, 'Tratado de Estado y neutralidad.'), (1995, 'Entra en la UE.')])

P('Liechtenstein', 'Vaduz', 'Monarquía constitucional con un príncipe de amplios poderes.', 'Alemán. Católicos.', 'Ninguno relevante.',
  'Servicios financieros, fundaciones y manufactura de precisión.', 'Su papel en el resguardo de fortunas.', [(1806, 'Soberanía.'), (2008, 'Escándalo de evasión de clientes alemanes.')])
P('Monaco', 'Mónaco', 'Monarquía constitucional; el príncipe concentra el poder.', 'Francés. Católicos.', 'Ninguno.',
  'Turismo de lujo, casino, inmobiliaria y residencia sin impuesto a la renta.', 'Su atractivo para grandes fortunas y la vigilancia por lavado de dinero.',
  [(1297, 'Los Grimaldi toman el peñón.'), (2024, 'El GAFI la incluye en la lista gris.')])
P('San Marino', 'San Marino', 'República parlamentaria con dos capitanes regentes.', 'Italiano. Católicos.', 'Piedra.',
  'Turismo, banca e industria liviana.', 'Su acuerdo de asociación con la UE.', [(301, 'Fundación según la tradición.')])
P('Andorra', 'Andorra la Vella', 'Coprincipado parlamentario: los copríncipes son el presidente de Francia y el obispo de Urgel.', 'Catalán. Católicos.',
  'Hidroelectricidad, madera.', 'Turismo, comercio y banca.', 'El fin de su secreto bancario y el acuerdo de asociación con la UE.',
  [(1278, 'Paréage que crea el coprincipado.'), (1993, 'Constitución.'), (2015, 'Intervención de la Banca Privada d\'Andorra por lavado.')])
P('Vatican', 'Ciudad del Vaticano', 'Monarquía electiva absoluta: el papa concentra los tres poderes y encabeza la Santa Sede.', 'Italiano y latín. Católicos.',
  'Ninguno.', 'Donaciones, museos, inversiones y el Banco Vaticano.',
  'La influencia de la Santa Sede sobre 1.400 millones de católicos, su diplomacia y la limpieza de sus finanzas.',
  [(1929, 'Pactos de Letrán.'), (1982, 'Quiebra del Banco Ambrosiano.'), (2013, 'Renuncia de Benedicto XVI.'), (2023, 'Condena del cardenal Becciu por un fraude inmobiliario.'), (2025, 'Elección de León XIV, primer papa estadounidense.')])
P('Malta', 'La Valeta', 'República parlamentaria.', 'Maltés e inglés. Católicos.', 'Piedra caliza, sal.',
  'Turismo, juego en línea, servicios financieros y registro de buques.', 'La venta de pasaportes, frenada por la justicia europea, y la corrupción.',
  [(1964, 'Independencia.'), (2004, 'Entra en la UE.'), (2017, 'Asesinato de la periodista Daphne Caruana Galizia.'), (2025, 'La justicia europea declara ilegal su venta de ciudadanía.')])

# ───────────────────────── Europa del norte ─────────────────────────

P('Denmark', 'Copenhague', 'Monarquía constitucional parlamentaria.', 'Danés. Luteranos.', 'Petróleo y gas, pesca, tierras agrícolas.',
  'Farmacéutica (Novo Nordisk), transporte marítimo (Maersk), agroindustria y energía eólica.',
  'Groenlandia frente a la presión de EE.UU. y el control de los estrechos del Báltico.',
  [(1849, 'Constitución.'), (1949, 'Miembro fundador de la OTAN.'), (1973, 'Entra en la Comunidad Europea.'), (2025, 'Refuerza su defensa de Groenlandia.')])
P('Norway', 'Oslo', 'Monarquía constitucional parlamentaria.', 'Noruego. Luteranos.', 'Petróleo, gas, pesca, hidroelectricidad, minerales.',
  'Petróleo y gas; el mayor fondo soberano del mundo.', 'Su papel como principal proveedor de gas de Europa y la frontera ártica con Rusia.',
  [(1905, 'Independencia de Suecia.'), (1969, 'Descubrimiento de petróleo.'), (1990, 'Creación del fondo petrolero.'), (2022, 'Sabotaje de los gasoductos Nord Stream en su vecindad.')])
P('Sweden', 'Estocolmo', 'Monarquía constitucional parlamentaria.', 'Sueco. Luteranos y muchos sin religión.', 'Hierro, cobre, madera, uranio, hidroelectricidad.',
  'Industria (Volvo, Ericsson, Saab), minería, madera y servicios.', 'Su ingreso a la OTAN, la seguridad del Báltico y la violencia de las bandas.',
  [(1814, 'Comienza su neutralidad.'), (1995, 'Entra en la UE.'), (2024, 'Entra en la OTAN.')])
P('Finland', 'Helsinki', 'República parlamentaria.', 'Finés y sueco. Luteranos.', 'Madera, hierro, cobre, níquel.',
  'Industria forestal, tecnología (Nokia), maquinaria.', 'Su frontera de 1.300 km con Rusia ya como miembro de la OTAN.',
  [(1917, 'Independencia de Rusia.'), (1939, 'Guerra de Invierno.'), (1995, 'Entra en la UE.'), (2023, 'Entra en la OTAN.')])
P('Iceland', 'Reikiavik', 'República parlamentaria; sin fuerzas armadas propias.', 'Islandés. Luteranos.', 'Pesca, geotermia, hidroelectricidad.',
  'Pesca, turismo y aluminio.', 'Su posición en el corredor GIUK, vital para la OTAN en el Atlántico Norte.',
  [(1944, 'República.'), (1949, 'Miembro fundador de la OTAN.'), (2008, 'Quiebra de sus bancos.')])
P('Faeroe Is.', 'Tórshavn', 'Territorio autónomo del Reino de Dinamarca.', 'Feroés. Luteranos.', 'Pesca.',
  'Pesca y salmón de cultivo.', 'Su autonomía y la pesca con Rusia.', [(1948, 'Autogobierno.')])
EXTRA['Åland'] = {'pob': (30500, 2024), 'area': 1580}
P('Åland', 'Mariehamn', 'Región autónoma y desmilitarizada de Finlandia.', 'Sueco. Luteranos.', 'Pesca.',
  'Transporte marítimo y turismo.', 'Su desmilitarización en el Báltico ahora que Finlandia está en la OTAN.',
  [(1921, 'La Sociedad de Naciones la asigna a Finlandia, autónoma y desmilitarizada.')])

# ───────────────────────── Europa central y oriental ─────────────────────────

P('Poland', 'Varsovia', 'República parlamentaria con presidente electo de amplio veto.', 'Polaco. Mayoría católica.',
  'Carbón, cobre, plata, gas, tierras agrícolas.', 'Industria, servicios y agroindustria; crece sin pausa desde 1992.',
  'Su papel como frontera armada de la OTAN con Rusia y Bielorrusia y el choque entre gobierno y presidencia.',
  [(1918, 'Independencia.'), (1939, 'Invasión alemana y soviética.'), (1989, 'Fin del comunismo.'), (1999, 'Entra en la OTAN.'), (2004, 'Entra en la UE.')])
P('Czechia', 'Praga', 'República parlamentaria.', 'Checo. Mayoría sin religión.', 'Carbón, caolín, madera.',
  'Industria automotriz y de maquinaria.', 'Su orientación ante Ucrania y la UE tras el regreso de gobiernos escépticos.',
  [(1918, 'Checoslovaquia.'), (1968, 'Primavera de Praga.'), (1989, 'Revolución de Terciopelo.'), (1993, 'Separación pacífica.')])
P('Slovakia', 'Bratislava', 'República parlamentaria.', 'Eslovaco. Mayoría católica.', 'Carbón, hierro, cobre, madera.',
  'Industria automotriz (mayor producción per cápita del mundo).', 'Su acercamiento a Moscú dentro de la UE y la OTAN.',
  [(1993, 'Independencia.'), (2004, 'Entra en la UE y la OTAN.'), (2018, 'Asesinato del periodista Ján Kuciak.'), (2024, 'Atentado contra el primer ministro.')])
P('Hungary', 'Budapest', 'República parlamentaria; gobierno proeuropeo desde la derrota de Orbán en abril de 2026.', 'Húngaro. Católicos y calvinistas.',
  'Bauxita, carbón, tierras agrícolas.', 'Industria automotriz y electrónica, agroindustria.',
  'Cómo se desarma el sistema de poder y clientelismo construido desde 2010 y el desbloqueo de los fondos europeos.',
  [(1956, 'Revolución aplastada por la URSS.'), (2004, 'Entra en la UE.'), (2010, 'Orbán gana con mayoría constitucional.'), (2026, 'Gana la oposición encabezada por Péter Magyar.')])
P('Slovenia', 'Liubliana', 'República parlamentaria.', 'Esloveno. Católicos.', 'Madera, hidroelectricidad.', 'Industria y servicios.',
  'Su papel como puerta de los Balcanes a la UE.', [(1991, 'Independencia.'), (2004, 'Entra en la UE y la OTAN.')])
P('Croatia', 'Zagreb', 'República parlamentaria.', 'Croata. Católicos.', 'Petróleo, bauxita, madera.', 'Turismo, industria liviana y transporte.',
  'La terminal de gas de Krk como alternativa al gas ruso.', [(1991, 'Independencia y guerra.'), (2013, 'Entra en la UE.'), (2023, 'Adopta el euro y entra en Schengen.')])
P('Romania', 'Bucarest', 'República semipresidencialista.', 'Rumano. Ortodoxos.', 'Petróleo, gas, madera, sal, tierras.',
  'Industria, servicios y agroindustria.', 'La base de la OTAN en el mar Negro y la injerencia rusa en sus elecciones.',
  [(1989, 'Caída de Ceaușescu.'), (2004, 'Entra en la OTAN.'), (2007, 'Entra en la UE.'), (2024, 'Anulación de la elección presidencial por injerencia.')])
P('Bulgaria', 'Sofía', 'República parlamentaria con gobiernos inestables.', 'Búlgaro. Ortodoxos.', 'Carbón, cobre, plomo, zinc.',
  'Industria, servicios y agricultura.', 'La corrupción y la influencia rusa en la energía.',
  [(1878, 'Autonomía del Imperio otomano.'), (1989, 'Fin del comunismo.'), (2007, 'Entra en la UE.'), (2026, 'Adopta el euro.')])
P('Greece', 'Atenas', 'República parlamentaria.', 'Griego. Ortodoxos.', 'Lignito, bauxita, mármol, petróleo.',
  'Transporte marítimo (la mayor flota mercante del mundo), turismo y servicios.', 'La rivalidad con Turquía en el Egeo y Chipre y la recuperación tras la crisis de deuda.',
  [(1830, 'Independencia.'), (1967, 'Dictadura de los coroneles.'), (1981, 'Entra en la Comunidad Europea.'), (2010, 'Rescate y crisis de la deuda.')])
P('Cyprus', 'Nicosia', 'República presidencialista; el norte está ocupado por Turquía desde 1974.', 'Griego y turco. Ortodoxos y musulmanes.',
  'Cobre, gas marino.', 'Turismo, transporte marítimo y servicios financieros (muy expuestos a capital ruso).',
  'La reunificación, el gas del Mediterráneo oriental y su papel como plataforma financiera y de inteligencia.',
  [(1960, 'Independencia del Reino Unido; bases británicas.'), (1974, 'Golpe e invasión turca.'), (2004, 'Entra en la UE.'), (2013, 'Rescate bancario con quita de depósitos.')])
EXTRA['N. Cyprus'] = {'pob': (382000, 2021), 'area': 3355}
P('N. Cyprus', 'Nicosia del Norte', 'República parlamentaria reconocida solo por Turquía; colonia de hecho de Ankara.', 'Turco. Musulmanes.',
  'Ninguno relevante.', 'Universidades, casinos, turismo y transferencias de Turquía; usa la lira turca.',
  'Si la división se vuelve definitiva como «dos Estados», como piden Ankara y su gobierno.',
  [(1974, 'Invasión turca.'), (1983, 'Proclamación unilateral de la república.'), (2004, 'El sur rechaza el plan Annan de reunificación.')])
P('Estonia', 'Tallin', 'República parlamentaria.', 'Estonio; ruso de minoría. Mayoría sin religión.', 'Esquisto bituminoso, madera.',
  'Servicios digitales, tecnología, madera.', 'Su frontera con Rusia y la minoría rusohablante.', [(1918, 'Independencia.'), (1991, 'Restauración.'), (2004, 'Entra en la UE y la OTAN.'), (2007, 'Ciberataque masivo atribuido a Rusia.')])
P('Latvia', 'Riga', 'República parlamentaria.', 'Letón; ruso de minoría. Luteranos, católicos y ortodoxos.', 'Madera, turba.',
  'Logística, madera y servicios.', 'Su frontera con Rusia y Bielorrusia y la integración de la minoría rusa.', [(1918, 'Independencia.'), (1991, 'Restauración.'), (2004, 'Entra en la UE y la OTAN.')])
P('Lithuania', 'Vilna', 'República semipresidencialista.', 'Lituano. Católicos.', 'Turba, ámbar.',
  'Industria, logística y tecnología financiera.', 'El corredor de Suwałki y su relación con Kaliningrado y Bielorrusia.', [(1990, 'Independencia.'), (2004, 'Entra en la UE y la OTAN.'), (2021, 'Choque con China por Taiwán.')])

# ───────────────────────── Balcanes ─────────────────────────

P('Albania', 'Tirana', 'República parlamentaria con un partido dominante.', 'Albanés. Musulmanes, ortodoxos y católicos.', 'Petróleo, cromo, cobre, hidroelectricidad.',
  'Turismo, remesas y agricultura; fuerte economía ilegal del cannabis y la cocaína.', 'Su candidatura a la UE y la mafia albanesa, global en la cocaína.',
  [(1912, 'Independencia.'), (1944, 'Dictadura de Hoxha.'), (1997, 'Colapso de las pirámides financieras.'), (2009, 'Entra en la OTAN.')])
P('Macedonia', 'Skopie', 'República parlamentaria.', 'Macedonio y albanés. Ortodoxos y musulmanes.', 'Cromo, plomo, zinc.',
  'Industria liviana y agricultura.', 'Su bloqueado ingreso a la UE por los vetos de Grecia y Bulgaria.', [(1991, 'Independencia.'), (2001, 'Conflicto con insurgentes albaneses.'), (2019, 'Cambia de nombre y entra en la OTAN (2020).')])
P('Montenegro', 'Podgorica', 'República parlamentaria.', 'Montenegrino y serbio. Ortodoxos.', 'Bauxita, hidroelectricidad.',
  'Turismo y servicios.', 'El adelantado del ingreso de los Balcanes a la UE y los clanes de la cocaína.', [(2006, 'Independencia.'), (2016, 'Intento de golpe atribuido a la inteligencia rusa.'), (2017, 'Entra en la OTAN.')])
P('Bosnia and Herz.', 'Sarajevo', 'República federal con presidencia tripartita bajo supervisión del Alto Representante internacional.', 'Bosnio, serbio y croata. Musulmanes, ortodoxos y católicos.',
  'Carbón, hierro, bauxita, madera.', 'Industria, remesas y servicios.', 'El secesionismo de la República Srpska y la supervivencia del acuerdo de Dayton.',
  [(1992, 'Guerra tras la independencia.'), (1995, 'Masacre de Srebrenica y acuerdos de Dayton.'), (2025, 'Condena del líder serbobosnio Dodik por desafiar al Alto Representante.')])
P('Serbia', 'Belgrado', 'República parlamentaria con el poder concentrado en la presidencia.', 'Serbio. Ortodoxos.', 'Petróleo, carbón, cobre, oro, litio.',
  'Industria, agricultura e inversión china y europea.', 'Su equilibrio entre la UE, Rusia y China, Kosovo y las protestas masivas desde 2024.',
  [(1878, 'Independencia.'), (1999, 'Bombardeo de la OTAN.'), (2000, 'Caída de Milošević.'), (2008, 'Kosovo declara la independencia.'), (2024, 'Protestas tras el derrumbe de Novi Sad.')])
P('Kosovo', 'Pristina', 'República parlamentaria reconocida por cerca de cien países; depende de la KFOR de la OTAN.', 'Albanés y serbio. Musulmanes.',
  'Lignito, plomo, zinc, níquel.', 'Remesas, servicios y construcción.', 'El norte serbio, el reconocimiento internacional y la presencia de la OTAN.',
  [(1999, 'Intervención de la OTAN.'), (2008, 'Independencia.'), (2023, 'Ataque de paramilitares serbios en Banjska.')])

# ───────────────────────── Islas británicas dependientes ─────────────────────────

P('Jersey', 'Saint Helier', 'Dependencia de la Corona británica con autogobierno.', 'Inglés y francés. Anglicanos y católicos.', 'Ninguno relevante.',
  'Servicios financieros extraterritoriales.', 'Su papel de paraíso fiscal.', [(1204, 'Queda ligada a la Corona inglesa.')])
P('Guernsey', 'Saint Peter Port', 'Dependencia de la Corona británica con autogobierno.', 'Inglés. Anglicanos.', 'Ninguno relevante.',
  'Servicios financieros y seguros cautivos.', 'Su papel de paraíso fiscal.', [(1204, 'Queda ligada a la Corona inglesa.')])
P('Isle of Man', 'Douglas', 'Dependencia de la Corona británica con parlamento propio (Tynwald).', 'Inglés y manés. Cristianos.', 'Ninguno relevante.',
  'Servicios financieros, juego en línea y registro de buques.', 'Su régimen fiscal especial.', [(1765, 'Pasa a la Corona británica.')])

# ───────────────────────── Rusia y su periferia ─────────────────────────

P('Russia', 'Moscú', 'República federal semipresidencialista en la forma; régimen personalista apoyado en los servicios de seguridad, con elecciones sin competencia real.',
  'Ruso y lenguas regionales. Ortodoxos y musulmanes.', 'Gas, petróleo, carbón, níquel, paladio, diamantes, oro, madera, trigo, uranio.',
  'Hidrocarburos y minería, con una economía de guerra desde 2022 y comercio reorientado hacia China e India.',
  'El resultado de la guerra en Ucrania, su dependencia creciente de China y la sucesión de un régimen personal.',
  [(1917, 'Revolución bolchevique.'), (1991, 'Disolución de la URSS.'), (1999, 'Putin llega al poder.'), (2001, 'Apoya a EE.UU. tras el 11 de septiembre y ofrece a Europa una asociación en el Bundestag.'), (2007, 'Discurso de Múnich contra el mundo unipolar y la ampliación de la OTAN.'), (2008, 'Guerra con Georgia.'),
   (2014, 'Anexión de Crimea.'), (2021, 'Putin publica «Sobre la unidad histórica de rusos y ucranianos».'), (2022, 'Invasión a gran escala de Ucrania.'), (2023, 'Motín de Wagner.')])
P('Ukraine', 'Kiev', 'República semipresidencialista bajo ley marcial desde 2022; depende del apoyo occidental.', 'Ucraniano; ruso extendido. Ortodoxos y grecocatólicos.',
  'Tierras negras, hierro, carbón, manganeso, titanio, litio, gas.', 'Agroexportación, metalurgia e industria de defensa; economía de guerra sostenida por ayuda externa.',
  'Su supervivencia como Estado, el territorio ocupado, los términos de un alto el fuego y el acuerdo de minerales con EE.UU.',
  [(1991, 'Independencia.'), (2004, 'Revolución Naranja.'), (2008, 'La OTAN promete en Bucarest que algún día será miembro, sin plan de ingreso: Alemania y Francia frenan el que impulsaba EE.UU.'), (2014, 'Euromaidán, anexión de Crimea y guerra en el Donbás.'), (2021, 'Putin publica un ensayo que la presenta como parte de un solo pueblo con Rusia.'), (2022, 'Invasión rusa a gran escala.'), (2025, 'Acuerdo de minerales con EE.UU.')])
P('Belarus', 'Minsk', 'República presidencialista en la forma; dictadura personal desde 1994, integrada militarmente a Rusia.', 'Bielorruso y ruso. Ortodoxos.',
  'Potasa, madera, turba.', 'Industria estatal, potasa y refinación de petróleo ruso.', 'La sucesión y su absorción por Rusia, que despliega allí armas nucleares.',
  [(1991, 'Independencia.'), (1994, 'Lukashenko llega al poder.'), (2020, 'Fraude y represión de las protestas.'), (2023, 'Rusia despliega armas nucleares tácticas.')])
P('Moldova', 'Chisinau', 'República parlamentaria; Transnistria escapa a su control con tropas rusas.', 'Rumano. Ortodoxos.', 'Tierras agrícolas, lignito.',
  'Agricultura, remesas y servicios.', 'Su camino a la UE frente a la injerencia rusa y Transnistria.',
  [(1991, 'Independencia.'), (1992, 'Guerra de Transnistria.'), (2022, 'Candidata a la UE.'), (2025, 'Elecciones con compra de votos financiada desde Rusia.')])
P('Georgia', 'Tiflis', 'República parlamentaria con el poder concentrado en el partido Sueño Georgiano y su fundador.', 'Georgiano. Ortodoxos.',
  'Manganeso, cobre, madera, hidroelectricidad.', 'Turismo, tránsito, vino y servicios.', 'Su giro hacia Moscú, que congeló el camino a la UE, y los territorios ocupados por Rusia.',
  [(1991, 'Independencia.'), (2003, 'Revolución de las Rosas.'), (2008, 'Guerra con Rusia.'), (2024, 'Ley de agentes extranjeros y freno a la adhesión a la UE.')])
P('Armenia', 'Ereván', 'República parlamentaria.', 'Armenio. Apostólicos armenios.', 'Cobre, molibdeno, oro.', 'Minería, servicios y tecnología.',
  'Su alejamiento de Rusia, el corredor hacia Najicheván y la paz con Azerbaiyán.',
  [(1991, 'Independencia.'), (1994, 'Gana la primera guerra de Karabaj.'), (2020, 'Derrota en Karabaj.'), (2023, 'Azerbaiyán toma Karabaj; éxodo armenio.'), (2025, 'Acuerdo de paz rubricado en Washington.')])
P('Azerbaijan', 'Bakú', 'República presidencialista hereditaria en los hechos.', 'Azerí. Musulmanes chiíes.', 'Petróleo, gas, hierro.',
  'Petróleo y gas hacia Europa.', 'Su papel como proveedor de gas europeo, la alianza con Turquía e Israel y el corredor hacia Najicheván.',
  [(1991, 'Independencia.'), (2006, 'Oleoducto Bakú-Tiflis-Ceyhan.'), (2023, 'Recupera Karabaj.'), (2025, 'Paz con Armenia y choque con Rusia.')])

# ───────────────────────── Asia central ─────────────────────────

P('Kazakhstan', 'Astaná', 'República presidencialista con el poder concentrado.', 'Kazajo y ruso. Musulmanes y ortodoxos.',
  'Petróleo, gas, uranio (primer productor mundial), carbón, hierro, cobre, cromo.', 'Petróleo y minería.',
  'Su política multivectorial entre Rusia, China y Occidente y el corredor de transporte transcaspio.',
  [(1991, 'Independencia.'), (2019, 'Nazarbáyev deja la presidencia.'), (2022, 'Revuelta de enero y tropas de la OTSC.')])
P('Uzbekistan', 'Taskent', 'República presidencialista autoritaria.', 'Uzbeko. Musulmanes.', 'Gas, oro, uranio, cobre, algodón.',
  'Oro, gas, algodón y remesas desde Rusia.', 'Su apertura económica y el reparto del agua de Asia central.',
  [(1991, 'Independencia.'), (2005, 'Masacre de Andiyán.'), (2016, 'Muere Karímov; apertura gradual.')])
P('Kyrgyzstan', 'Biskek', 'República presidencialista con el poder concentrado desde 2021.', 'Kirguís y ruso. Musulmanes.', 'Oro, carbón, hidroelectricidad.',
  'Oro, remesas desde Rusia y reexportación a Rusia.', 'Su uso como vía para evadir sanciones contra Rusia.',
  [(1991, 'Independencia.'), (2005, 'Revolución de los Tulipanes.'), (2020, 'Tercera revuelta en quince años.')])
P('Tajikistan', 'Dusambé', 'República presidencialista; dictadura personal y familiar.', 'Tayiko y ruso. Musulmanes.', 'Hidroelectricidad, aluminio, oro, plata.',
  'Remesas (cerca de la mitad del PBI) y aluminio.', 'Su frontera con Afganistán y la base militar rusa.',
  [(1991, 'Independencia.'), (1992, 'Guerra civil hasta 1997.'), (2024, 'Atentado de Crocus en Moscú, con atacantes tayikos.')])
P('Turkmenistan', 'Asjabad', 'República presidencialista; dictadura hereditaria.', 'Turcomano. Musulmanes.', 'Gas (cuartas reservas del mundo), petróleo, azufre.',
  'Gas exportado sobre todo a China.', 'Quién se queda con su gas.', [(1991, 'Independencia.'), (2009, 'Gasoducto hacia China.'), (2022, 'Traspaso del poder de padre a hijo.')])
P('Mongolia', 'Ulán Bator', 'República semipresidencialista.', 'Mongol. Budistas.', 'Carbón, cobre, oro, uranio, tierras raras.',
  'Minería (Oyu Tolgoi) exportada casi toda a China.', 'Su democracia entre Rusia y China y su «tercer vecino» occidental.',
  [(1921, 'Revolución con apoyo soviético.'), (1990, 'Transición democrática.')])
P('Afghanistan', 'Kabul', 'Emirato talibán sin reconocimiento amplio; el poder real está en el líder supremo en Kandahar.', 'Darí y pastún. Musulmanes.',
  'Gas, cobre, litio, hierro, tierras raras, piedras preciosas.', 'Agricultura, ayuda humanitaria y comercio; las mujeres excluidas del trabajo y la educación.',
  'El reconocimiento del gobierno talibán, la frontera disputada con Pakistán y los minerales.',
  [(1979, 'Invasión soviética.'), (1996, 'Primer gobierno talibán.'), (2001, 'Invasión de EE.UU.'), (2021, 'Retirada de EE.UU. y regreso talibán.'), (2025, 'Rusia lo reconoce; choques fronterizos con Pakistán.')])

# ───────────────────────── Turquía y Medio Oriente ─────────────────────────

P('Turkey', 'Ankara', 'República presidencialista con el poder concentrado en el presidente desde 2017; el principal rival opositor está preso.', 'Turco y kurdo. Musulmanes.',
  'Carbón, hierro, cromo, boro, mármol.', 'Industria, defensa (drones), turismo y construcción.',
  'Su autonomía dentro de la OTAN, su peso en Siria, el control de los estrechos y la deriva autoritaria.',
  [(1923, 'República.'), (1952, 'Entra en la OTAN.'), (2016, 'Intento de golpe.'), (2017, 'Referéndum presidencialista.'), (2025, 'Detención del alcalde de Estambul y disolución del PKK.')])
P('Israel', 'Jerusalén (reconocida por pocos países)', 'República parlamentaria; las fuerzas armadas y los servicios de inteligencia tienen un peso central.', 'Hebreo y árabe. Judíos y musulmanes.',
  'Gas marino, potasa, cobre.', 'Tecnología, defensa, ciberseguridad, diamantes.',
  'El futuro de Gaza y Cisjordania, su guerra con el eje iraní y su aislamiento diplomático.',
  [(1948, 'Independencia.'), (1967, 'Guerra de los Seis Días.'), (1993, 'Acuerdos de Oslo.'), (2023, 'Ataque de Hamás y guerra en Gaza.'), (2025, 'Guerra de doce días con Irán.'), (2026, 'Nueva guerra con Irán junto a EE.UU.')])
P('Palestine', 'Ramala (sede administrativa)', 'Estado reconocido por la mayoría de la ONU, sin soberanía efectiva: Cisjordania bajo ocupación israelí y Gaza destruida por la guerra.', 'Árabe. Musulmanes.',
  'Tierras agrícolas, gas marino frente a Gaza.', 'Ayuda externa, empleo en Israel y comercio controlado por Israel.',
  'El gobierno de Gaza tras la guerra, la anexión de Cisjordania y la viabilidad de un Estado.',
  [(1948, 'Nakba.'), (1967, 'Ocupación israelí.'), (1993, 'Acuerdos de Oslo.'), (2007, 'Hamás toma Gaza.'), (2023, 'Guerra en Gaza.'), (2025, 'Alto el fuego y reconocimiento de Francia, el Reino Unido y otros.')])
P('Lebanon', 'Beirut', 'República parlamentaria confesional; Hezbolá, debilitado desde 2024, mantiene armas propias.', 'Árabe. Musulmanes y cristianos.',
  'Agua, piedra caliza, gas marino.', 'Servicios y remesas; colapso financiero desde 2019.', 'El desarme de Hezbolá, la presencia israelí en el sur y la reconstrucción.',
  [(1943, 'Independencia.'), (1975, 'Guerra civil hasta 1990.'), (2006, 'Guerra entre Israel y Hezbolá.'), (2020, 'Explosión del puerto de Beirut.'), (2024, 'Guerra con Israel y muerte de Nasralá.')])
P('Syria', 'Damasco', 'Gobierno de transición de al-Sharaa desde la caída de Asad en 2024; Israel ocupa una franja del sur.', 'Árabe y kurdo. Musulmanes suníes, alauíes, drusos y cristianos.',
  'Petróleo, fosfatos, tierras agrícolas.', 'Economía destruida por la guerra; levantamiento de sanciones desde 2025.',
  'La unidad del país —kurdos, drusos, alauíes—, la reconstrucción y la competencia entre Turquía, Israel y el Golfo.',
  [(1946, 'Independencia.'), (1970, 'Hafez al-Asad toma el poder.'), (2011, 'Guerra civil.'), (2024, 'Caída de Asad.'), (2026, 'El gobierno recupera el noreste.')])
P('Jordan', 'Amán', 'Monarquía constitucional con un rey de amplios poderes; depende de la ayuda y la protección de EE.UU.', 'Árabe. Musulmanes.',
  'Fosfatos, potasa.', 'Servicios, fosfatos, ayuda externa y remesas.', 'Su estabilidad con una mayoría de origen palestino y los refugiados.',
  [(1946, 'Independencia.'), (1970, 'Septiembre Negro.'), (1994, 'Paz con Israel.')])
P('Iraq', 'Bagdad', 'República parlamentaria federal con reparto confesional; milicias proiraníes con poder propio.', 'Árabe y kurdo. Musulmanes chiíes y suníes.',
  'Petróleo, gas, fosfatos, azufre.', 'Petróleo (más del 90 % de los ingresos del Estado).', 'El pulso entre Irán y EE.UU., las milicias y la autonomía kurda.',
  [(1932, 'Independencia.'), (1979, 'Sadam Husein toma el poder.'), (2003, 'Invasión de EE.UU.'), (2014, 'Estado Islámico toma Mosul.'), (2017, 'Derrota del Estado Islámico.')])
P('Iran', 'Teherán', 'República teocrática; el poder real pasó del clero a la Guardia Revolucionaria tras la guerra de 2026.', 'Persa, azerí y kurdo. Musulmanes chiíes.',
  'Petróleo y gas (de las mayores reservas del mundo), cobre, hierro.', 'Hidrocarburos bajo sanciones, vendidos sobre todo a China.',
  'La supervivencia del régimen, su programa nuclear y el control del estrecho de Ormuz.',
  [(1953, 'Golpe contra Mossadeq.'), (1979, 'Revolución islámica.'), (1980, 'Guerra con Irak.'), (2015, 'Acuerdo nuclear (abandonado por EE.UU. en 2018).'), (2025, 'Guerra de doce días con Israel.'), (2026, 'Guerra con EE.UU. e Israel.')])
P('Saudi Arabia', 'Riad', 'Monarquía absoluta; el príncipe heredero concentra el poder.', 'Árabe. Musulmanes suníes.', 'Petróleo, gas, oro, cobre, fosfatos.',
  'Petróleo; diversificación con el fondo soberano PIF.', 'Su transformación económica, la guerra en Yemen y su lugar entre EE.UU., China e Israel.',
  [(1932, 'Fundación del reino.'), (1938, 'Descubrimiento de petróleo.'), (1945, 'Pacto con Roosevelt.'), (2015, 'Guerra en Yemen.'), (2018, 'Asesinato de Khashoggi.'), (2025, 'Pacto de defensa con Pakistán.')])
P('United Arab Emirates', 'Abu Dabi', 'Federación de siete monarquías absolutas.', 'Árabe. Musulmanes; mayoría de extranjeros.', 'Petróleo, gas.',
  'Petróleo, finanzas, logística, turismo y comercio de oro.', 'Su agenda propia en Sudán, Libia y Yemen y su papel como plaza financiera para capitales sancionados.',
  [(1971, 'Independencia.'), (2020, 'Acuerdos de Abraham con Israel.'), (2024, 'Sale de la lista gris del GAFI.')])
P('Qatar', 'Doha', 'Monarquía absoluta.', 'Árabe. Musulmanes; mayoría de extranjeros.', 'Gas (terceras reservas del mundo), petróleo.',
  'Gas natural licuado y el fondo soberano.', 'Su mediación con Hamás y los talibanes y la base de Al Udeid.',
  [(1971, 'Independencia.'), (1996, 'Nace Al Jazeera.'), (2017, 'Bloqueo de sus vecinos.'), (2025, 'Bombardeo israelí contra Hamás en Doha.')])
P('Bahrain', 'Manama', 'Monarquía constitucional con rey de amplios poderes; minoría suní gobierna a una mayoría chií.', 'Árabe. Musulmanes chiíes y suníes.',
  'Petróleo, gas.', 'Finanzas, aluminio y petróleo.', 'La base de la Quinta Flota y la tensión con la mayoría chií.',
  [(1971, 'Independencia.'), (2011, 'Protestas aplastadas con tropas saudíes.'), (2020, 'Acuerdos de Abraham.')])
P('Kuwait', 'Kuwait', 'Monarquía con parlamento, suspendido en 2024.', 'Árabe. Musulmanes.', 'Petróleo, gas.',
  'Petróleo y su fondo soberano.', 'Su vulnerabilidad entre Irak, Irán y Arabia Saudita.',
  [(1961, 'Independencia.'), (1990, 'Invasión iraquí.'), (1991, 'Liberación por la coalición.'), (2024, 'El emir suspende el parlamento.')])
P('Oman', 'Mascate', 'Monarquía absoluta (sultanato).', 'Árabe. Musulmanes ibadíes.', 'Petróleo, gas, cobre.',
  'Petróleo, gas y logística.', 'Su papel de mediador entre EE.UU. e Irán y su ribera del estrecho de Ormuz.',
  [(1970, 'Qabus toma el poder.'), (2020, 'Muere Qabus.'), (2025, 'Media en las negociaciones nucleares.')])
P('Yemen', 'Saná (en manos hutíes); Adén (gobierno reconocido)', 'Dividido entre los hutíes, el gobierno reconocido y las fuerzas separatistas del sur.', 'Árabe. Musulmanes suníes y zaidíes.',
  'Petróleo, gas, pesca.', 'Economía destruida; una de las peores crisis humanitarias del mundo.',
  'El control del estrecho de Bab el-Mandeb, los ataques hutíes al tráfico del mar Rojo y la partición del país.',
  [(1990, 'Unificación.'), (2014, 'Los hutíes toman Saná.'), (2015, 'Intervención saudí.'), (2023, 'Ataques hutíes en el mar Rojo.'), (2025, 'Campaña aérea de EE.UU.')])
P('Egypt', 'El Cairo', 'República presidencialista con las fuerzas armadas en el centro del poder y de la economía.', 'Árabe. Musulmanes suníes y cristianos coptos.',
  'Petróleo, gas, fosfatos, hierro.', 'Canal de Suez, turismo, gas, remesas y empresas militares; deuda alta.',
  'Los ingresos del canal golpeados por los ataques hutíes, la deuda y Gaza en su frontera.',
  [(1952, 'Revolución de los Oficiales Libres.'), (1956, 'Nacionalización del canal de Suez.'), (1979, 'Paz con Israel.'), (2011, 'Caída de Mubarak.'), (2013, 'Golpe militar.')])

# ───────────────────────── Asia del Sur ─────────────────────────

P('India', 'Nueva Delhi', 'República parlamentaria federal; el partido de gobierno domina desde 2014.', 'Hindi, inglés y 22 lenguas oficiales. Hindúes, musulmanes, cristianos y sijs.',
  'Carbón, hierro, bauxita, cromo, tierras agrícolas, torio.', 'Servicios informáticos, farmacéutica, industria y agricultura; el país más poblado del mundo.',
  'Su ascenso como potencia autónoma entre EE.UU., Rusia y China, la rivalidad con Pakistán y China en el Himalaya.',
  [(1947, 'Independencia y partición.'), (1962, 'Guerra con China.'), (1974, 'Primer ensayo nuclear.'), (1991, 'Apertura económica.'), (2019, 'Fin de la autonomía de Cachemira.'), (2025, 'Choque militar con Pakistán y aranceles de EE.UU. por el petróleo ruso.')])
P('Pakistan', 'Islamabad', 'República parlamentaria federal; las fuerzas armadas son el poder real.', 'Urdu, inglés y lenguas regionales. Musulmanes.',
  'Gas, carbón, cobre, oro, sal, tierras agrícolas.', 'Textiles, agricultura y remesas; dependiente de rescates del FMI.',
  'Su equilibrio entre China, EE.UU. y Arabia Saudita, la guerra fría con India y las insurgencias en el oeste.',
  [(1947, 'Independencia.'), (1971, 'Pierde Bangladés.'), (1998, 'Ensayos nucleares.'), (2011, 'Muerte de Bin Laden en Abbottabad.'), (2025, 'Choque con India y pacto de defensa con Arabia Saudita.')])
P('Bangladesh', 'Daca', 'República parlamentaria; gobierno del BNP electo en 2026 tras la caída de Sheikh Hasina.', 'Bengalí. Musulmanes e hindúes.',
  'Gas, tierras agrícolas, madera.', 'Textiles (segundo exportador mundial de ropa) y remesas.', 'Su reconstrucción institucional y los refugiados rohinyás.',
  [(1971, 'Independencia de Pakistán.'), (2009, 'Hasina vuelve al poder.'), (2017, 'Llegan cientos de miles de rohinyás.'), (2024, 'Revuelta estudiantil y caída de Hasina.'), (2026, 'Elecciones generales.')])
P('Sri Lanka', 'Colombo (sede de gobierno en Sri Jayawardenepura Kotte)', 'República semipresidencialista.', 'Cingalés y tamil. Budistas, hindúes, musulmanes y cristianos.',
  'Grafito, piedras preciosas, pesca.', 'Textiles, té, turismo y remesas.', 'Su deuda con China (el puerto de Hambantota) y su posición en el océano Índico.',
  [(1948, 'Independencia.'), (1983, 'Guerra civil hasta 2009.'), (2017, 'Cede Hambantota a China por 99 años.'), (2022, 'Default y caída del gobierno.')])
P('Nepal', 'Katmandú', 'República parlamentaria federal.', 'Nepalí. Hindúes y budistas.', 'Hidroelectricidad, madera.',
  'Remesas, turismo y agricultura.', 'Su equilibrio entre India y China y la inestabilidad política.',
  [(1996, 'Insurgencia maoísta.'), (2008, 'Fin de la monarquía.'), (2025, 'Revuelta juvenil derriba al gobierno.')])
P('Bhutan', 'Timbu', 'Monarquía constitucional.', 'Dzongkha. Budistas.', 'Hidroelectricidad, madera.', 'Venta de electricidad a India y turismo.',
  'Su frontera disputada con China y la dependencia de India.', [(1907, 'Monarquía.'), (2008, 'Primera constitución democrática.')])
P('Maldives', 'Malé', 'República presidencialista.', 'Dhivehi. Musulmanes.', 'Pesca.', 'Turismo y pesca.',
  'La subida del mar y la puja entre India y China.', [(1965, 'Independencia.'), (2023, 'Gana un gobierno que pide la salida de los militares indios.')])
EXTRA['Siachen Glacier'] = {'pob': (0, None)}
P('Siachen Glacier', '—', 'Zona en disputa bajo control militar de India desde 1984.', '—', 'Hielo y agua del Indo.',
  'Sin economía: solo guarniciones.', 'Su valor estratégico entre India, Pakistán y China.', [(1984, 'Operación Meghdoot: India ocupa el glaciar.'), (2003, 'Alto el fuego.')])

# ───────────────────────── Sudeste asiático ─────────────────────────

P('Myanmar', 'Naipyidó', 'Junta militar apoyada por China y Rusia; perdió buena parte del territorio frente a guerrillas étnicas y de resistencia.', 'Birmano y lenguas étnicas. Budistas.',
  'Jade, rubíes, tierras raras, gas, madera, estaño.', 'Gas, agricultura, minería; los complejos de estafas y el opio en las zonas de frontera.',
  'Si la junta se sostiene, el control de las minas de tierras raras y la ruta de China hacia el océano Índico.',
  [(1948, 'Independencia.'), (1962, 'Golpe militar.'), (2017, 'Expulsión de los rohinyás.'), (2021, 'Golpe contra el gobierno electo.'), (2023, 'Ofensiva de la Alianza de las Tres Hermandades.')])
P('Thailand', 'Bangkok', 'Monarquía constitucional; el ejército y el palacio están por encima de los gobiernos electos.', 'Tailandés. Budistas.',
  'Estaño, caucho, gas, tierras agrícolas.', 'Industria automotriz y electrónica, turismo, arroz.', 'El poder del ejército y la monarquía y la frontera con Camboya.',
  [(1932, 'Fin de la monarquía absoluta.'), (2006, 'Golpe.'), (2014, 'Golpe.'), (2025, 'Choques armados con Camboya.')])
P('Laos', 'Vientián', 'Estado de partido único comunista.', 'Lao. Budistas.', 'Hidroelectricidad, cobre, oro, madera.',
  'Electricidad, minería y la zona especial del Triángulo de Oro; deuda alta con China.', 'Su dependencia de China, que construyó el tren y gran parte de su deuda.',
  [(1975, 'Llega el régimen comunista.'), (2021, 'Inauguración del tren a China.')])
P('Cambodia', 'Nom Pen', 'Monarquía constitucional en la forma; régimen de partido dominante y transmisión familiar del poder.', 'Jemer. Budistas.',
  'Madera, gemas, petróleo, pesca.', 'Textiles, turismo y complejos de estafas a escala industrial.', 'Su alineamiento con China (base de Ream) y la economía de la estafa.',
  [(1975, 'Jemeres Rojos.'), (1979, 'Invasión vietnamita.'), (1991, 'Acuerdos de París.'), (2023, 'Hun Sen pasa el gobierno a su hijo.'), (2025, 'Choques con Tailandia.')])
P('Vietnam', 'Hanói', 'Estado de partido único comunista.', 'Vietnamita. Budistas y mayoría sin religión.', 'Petróleo, carbón, bauxita, tierras raras, pesca.',
  'Manufactura integrada a las cadenas de EE.UU., Japón y Corea.', 'Su equilibrio entre China y EE.UU. y las islas del mar de China Meridional.',
  [(1954, 'Dien Bien Phu.'), (1975, 'Reunificación.'), (1986, 'Reformas Doi Moi.'), (1995, 'Relaciones con EE.UU.'), (2023, 'Asociación estratégica con EE.UU.')])
P('Malaysia', 'Kuala Lumpur (sede de gobierno en Putrajaya)', 'Monarquía constitucional federal con rey rotativo.', 'Malayo. Musulmanes, budistas, cristianos e hindúes.',
  'Petróleo, gas, estaño, madera, caucho, aceite de palma.', 'Electrónica y semiconductores, petróleo, aceite de palma.',
  'El estrecho de Malaca, los reclamos chinos frente a Borneo y las tensiones étnicas.', [(1957, 'Independencia.'), (1965, 'Separación de Singapur.'), (2018, 'Escándalo 1MDB derriba al gobierno.')])
P('Singapore', 'Singapur', 'República parlamentaria con un partido dominante desde 1959.', 'Inglés, malayo, mandarín y tamil. Budistas, cristianos y musulmanes.',
  'Posición geográfica.', 'Finanzas, puerto, refinación y semiconductores.', 'Su papel de nodo financiero neutral entre China y EE.UU.',
  [(1965, 'Independencia.'), (1990, 'Acuerdo de acceso militar con EE.UU.')])
P('Indonesia', 'Yakarta (nueva capital en construcción en Nusantara)', 'República presidencialista; los militares recuperan poder desde 2024.', 'Indonesio. Musulmanes (el país musulmán más poblado).',
  'Níquel (primer productor mundial), carbón, gas, estaño, cobre, oro, aceite de palma.', 'Minería y procesado de níquel con capital chino, carbón, palma.',
  'Su lugar en la cadena de baterías y la soberanía sobre los estrechos de Malaca, la Sonda y Lombok.',
  [(1945, 'Independencia.'), (1965, 'Masacres anticomunistas y ascenso de Suharto.'), (1998, 'Caída de Suharto.'), (2020, 'Prohíbe exportar níquel sin procesar.'), (2025, 'Protestas masivas.')])
P('Brunei', 'Bandar Seri Begawan', 'Monarquía absoluta (sultanato).', 'Malayo. Musulmanes.', 'Petróleo, gas.', 'Petróleo y gas.',
  'Sus reclamos en el mar de China Meridional.', [(1984, 'Independencia.'), (2019, 'Aplicación de la sharía.')])
P('Philippines', 'Manila', 'República presidencialista dominada por clanes familiares.', 'Filipino e inglés. Católicos.',
  'Níquel, cobre, oro, madera, pesca.', 'Remesas, servicios de atención telefónica y electrónica.', 'El choque con China por los arrecifes y el acceso de EE.UU. a sus bases.',
  [(1946, 'Independencia.'), (1986, 'Caída de Marcos.'), (2016, 'Fallo arbitral contra China.'), (2023, 'Nuevas bases para EE.UU.'), (2025, 'Duterte entregado a la Corte Penal Internacional.')])
P('Timor-Leste', 'Dili', 'República semipresidencialista.', 'Tetun y portugués. Católicos.', 'Petróleo, gas, oro.', 'Petróleo y su fondo.',
  'El agotamiento del petróleo y el yacimiento de Greater Sunrise.', [(1975, 'Invasión indonesia.'), (2002, 'Independencia.'), (2025, 'Entra en la ASEAN.')])

# ───────────────────────── Asia oriental ─────────────────────────

P('China', 'Pekín', 'Estado de partido único comunista; el secretario general concentra el poder desde 2012.', 'Mandarín. Mayoría sin religión; budistas, taoístas, musulmanes y cristianos.',
  'Carbón, tierras raras (dominio mundial del refinado), hierro, petróleo, gas, tungsteno, antimonio.', 'Primera potencia manufacturera y comercial; crédito estatal e inversión en infraestructura.',
  'Desplazar a EE.UU. del Pacífico occidental, Taiwán, su dominio en minerales críticos y el freno de su crecimiento.',
  [(1949, 'Revolución comunista.'), (1966, 'Revolución Cultural.'), (1978, 'Reformas de Deng.'), (1989, 'Tiananmén.'), (2001, 'Entra en la OMC.'), (2013, 'Lanza la Franja y la Ruta.'), (2025, 'Guerra comercial y control de las tierras raras.')])
P('Hong Kong', 'Hong Kong', 'Región administrativa especial bajo control directo de Pekín desde 2020.', 'Cantonés, inglés y mandarín. Budistas, taoístas y cristianos.',
  'Puerto.', 'Finanzas, comercio y logística.', 'Su papel como plaza financiera de China con el mundo.',
  [(1842, 'Cedido al Reino Unido.'), (1997, 'Vuelve a China.'), (2019, 'Protestas masivas.'), (2020, 'Ley de seguridad nacional.')])
P('Macao', 'Macao', 'Región administrativa especial de China.', 'Cantonés y portugués. Budistas.', 'Ninguno.',
  'Casinos (el mayor centro de juego del mundo).', 'Su dependencia del juego y su papel en la salida de capitales chinos.', [(1557, 'Asentamiento portugués.'), (1999, 'Vuelve a China.')])
P('Taiwan', 'Taipéi', 'República semipresidencialista democrática, reconocida por pocos Estados.', 'Mandarín y taiwanés. Budistas y taoístas.',
  'Pocos recursos; capital humano.', 'Semiconductores: TSMC fabrica la mayoría de los chips avanzados del mundo.',
  'Su existencia como Estado de hecho frente a la presión de China y el compromiso de EE.UU.',
  [(1949, 'El gobierno nacionalista se refugia en la isla.'), (1971, 'Pierde la banca en la ONU.'), (1979, 'EE.UU. reconoce a Pekín; Ley de Relaciones con Taiwán.'), (1996, 'Primera elección presidencial directa.'), (2022, 'Maniobras chinas de bloqueo.')])
P('Japan', 'Tokio', 'Monarquía constitucional parlamentaria.', 'Japonés. Sintoístas y budistas.', 'Pesca, madera; casi sin recursos minerales.',
  'Industria, tecnología, finanzas; deuda pública muy alta.', 'Su rearme frente a China y Corea del Norte y la alianza con EE.UU.',
  [(1868, 'Restauración Meiji.'), (1945, 'Derrota y ocupación.'), (1951, 'Tratado de seguridad con EE.UU.'), (2011, 'Fukushima.'), (2022, 'Duplica el gasto de defensa.')])
P('South Korea', 'Seúl', 'República presidencialista.', 'Coreano. Mayoría sin religión; cristianos y budistas.', 'Carbón, tungsteno.',
  'Semiconductores, astilleros, automotriz, electrónica; grandes conglomerados familiares.', 'La alianza con EE.UU. frente a Corea del Norte y China.',
  [(1948, 'Fundación.'), (1950, 'Guerra de Corea.'), (1987, 'Democratización.'), (2024, 'Ley marcial fallida y destitución del presidente.'), (2025, 'Elección anticipada.')])
P('North Korea', 'Pionyang', 'Dictadura hereditaria de partido único.', 'Coreano. Ateísmo oficial.', 'Carbón, hierro, magnesita, tierras raras.',
  'Economía estatal bajo sanciones; ingresos por ciberrobos y venta de armas a Rusia.', 'Su arsenal nuclear y su alianza militar con Rusia.',
  [(1948, 'Fundación.'), (1950, 'Guerra de Corea.'), (2006, 'Primer ensayo nuclear.'), (2024, 'Tratado de defensa con Rusia.'), (2024, 'Envía tropas a la guerra en Ucrania.')])

# ───────────────────────── Oceanía ─────────────────────────

P('Australia', 'Canberra', 'Monarquía constitucional parlamentaria federal; reino de la Mancomunidad Británica.', 'Inglés. Cristianos y muchos sin religión.',
  'Hierro, carbón, litio, oro, bauxita, gas, uranio, tierras raras.', 'Minería exportada a China, agroindustria, educación y servicios.',
  'Su dependencia comercial de China frente a su alianza militar con EE.UU. (AUKUS).',
  [(1901, 'Federación.'), (1951, 'Tratado ANZUS.'), (2020, 'Represalias comerciales de China.'), (2021, 'Pacto AUKUS.')])
P('New Zealand', 'Wellington', 'Monarquía constitucional parlamentaria.', 'Inglés y maorí. Cristianos y muchos sin religión.',
  'Pesca, madera, oro, gas.', 'Lácteos, carne, turismo.', 'Su lugar en los Cinco Ojos y su influencia sobre las islas del Pacífico.',
  [(1840, 'Tratado de Waitangi.'), (1985, 'Prohíbe buques nucleares; sale del ANZUS en los hechos.'), (2019, 'Atentado de Christchurch.')])
P('Papua New Guinea', 'Port Moresby', 'Monarquía constitucional parlamentaria.', 'Tok pisin, inglés y más de 800 lenguas. Cristianos.',
  'Oro, cobre, gas, petróleo, madera.', 'Minería y gas natural licuado.', 'Bougainville y su independencia, y la puja entre Australia y China.',
  [(1975, 'Independencia de Australia.'), (1989, 'Guerra de Bougainville.'), (2019, 'Bougainville vota por la independencia.'), (2025, 'Tratado de defensa mutua con Australia.')])
P('Solomon Is.', 'Honiara', 'Monarquía constitucional parlamentaria.', 'Inglés y pidgin. Cristianos.', 'Madera, pesca, oro.',
  'Madera, pesca y ayuda externa.', 'El pacto de seguridad con China de 2022.', [(1978, 'Independencia.'), (2003, 'Misión regional de estabilización.'), (2019, 'Reconoce a China.'), (2022, 'Pacto de seguridad con China.')])
P('Fiji', 'Suva', 'República parlamentaria.', 'Inglés, fiyiano e hindi. Cristianos e hindúes.', 'Madera, pesca, oro.',
  'Turismo, azúcar y remesas.', 'Las tensiones étnicas y su papel de centro regional.', [(1970, 'Independencia.'), (1987, 'Golpes militares.'), (2006, 'Golpe.')])
P('Vanuatu', 'Port Vila', 'República parlamentaria.', 'Bislama, inglés y francés. Cristianos.', 'Pesca, madera.',
  'Turismo, agricultura y ciudadanía por inversión.', 'La influencia china y la venta de pasaportes.', [(1980, 'Independencia.')])
P('Samoa', 'Apia', 'República parlamentaria con jefes tradicionales.', 'Samoano e inglés. Cristianos.', 'Pesca, madera.', 'Remesas, turismo.',
  'Su equilibrio entre China y sus socios tradicionales.', [(1962, 'Independencia.'), (2021, 'Crisis constitucional.')])
P('Tonga', "Nuku'alofa", 'Monarquía constitucional.', 'Tongano e inglés. Cristianos.', 'Pesca.', 'Remesas y agricultura.',
  'Su deuda con China.', [(1970, 'Independencia del protectorado británico.'), (2022, 'Erupción del Hunga Tonga.')])
P('Kiribati', 'Tarawa', 'República presidencialista.', 'Gilbertés e inglés. Cristianos.', 'Pesca, fosfatos (agotados).', 'Licencias de pesca y ayuda externa.',
  'La subida del mar y la presencia china en el Pacífico central.', [(1979, 'Independencia.'), (2019, 'Reconoce a China.')])
P('Nauru', 'Yaren', 'República parlamentaria.', 'Nauruano e inglés. Cristianos.', 'Fosfatos (casi agotados).', 'Centro de detención de migrantes de Australia y ayuda.',
  'Su dependencia de Australia.', [(1968, 'Independencia.'), (2024, 'Reconoce a China; firma un tratado de seguridad con Australia.')])
P('Micronesia', 'Palikir', 'República federal en libre asociación con EE.UU.', 'Inglés y lenguas locales. Cristianos.', 'Pesca.',
  'Fondos del Pacto de Libre Asociación y pesca.', 'La renovación del pacto con EE.UU. y la presencia china.', [(1986, 'Pacto de Libre Asociación.'), (2023, 'Renovación del pacto.')])
P('Marshall Is.', 'Majuro', 'República en libre asociación con EE.UU.', 'Marshalés e inglés. Cristianos.', 'Pesca.',
  'Fondos del pacto, registro de buques y la base de Kwajalein.', 'El legado de los ensayos nucleares y la subida del mar.', [(1946, 'Ensayos nucleares en Bikini hasta 1958.'), (1986, 'Pacto de Libre Asociación.')])
P('Palau', 'Ngerulmud', 'República presidencialista en libre asociación con EE.UU.', 'Palauano e inglés. Cristianos.', 'Pesca, turismo.',
  'Turismo y fondos del pacto.', 'Su apoyo a Taiwán y el radar estadounidense en su territorio.', [(1994, 'Independencia en libre asociación.')])
P('Guam', 'Hagåtña', 'Territorio no incorporado de EE.UU.', 'Inglés y chamorro. Católicos.', 'Posición.', 'Bases militares y turismo.',
  'Su papel como base avanzada de EE.UU. frente a China.', [(1898, 'Pasa a EE.UU.'), (1941, 'Ocupación japonesa.'), (1950, 'Ley Orgánica.')])
P('N. Mariana Is.', 'Saipán', 'Mancomunidad en unión política con EE.UU.', 'Inglés, chamorro y caroliniano. Católicos.', 'Posición.',
  'Turismo y gastos federales.', 'Su papel militar frente a China.', [(1978, 'Mancomunidad.'), (2023, 'Ampliación de bases.')])
P('American Samoa', 'Pago Pago', 'Territorio no incorporado de EE.UU.', 'Samoano e inglés. Cristianos.', 'Pesca.', 'Enlatado de atún y fondos federales.',
  'Su dependencia de una sola industria.', [(1900, 'Pasa a EE.UU.')])
P('Cook Is.', 'Avarua', 'Estado autónomo en libre asociación con Nueva Zelanda.', 'Inglés y maorí de las Cook. Cristianos.', 'Pesca, nódulos del fondo marino.',
  'Turismo y servicios financieros.', 'Los minerales del lecho marino y su acuerdo con China, que enfrió la relación con Nueva Zelanda.', [(1965, 'Libre asociación.'), (2025, 'Acuerdo con China.')])
P('Niue', 'Alofi', 'Estado autónomo en libre asociación con Nueva Zelanda.', 'Niuano e inglés. Cristianos.', 'Pesca.', 'Ayuda de Nueva Zelanda.',
  'La despoblación.', [(1974, 'Libre asociación.')])
P('Fr. Polynesia', 'Papeete', 'Colectividad francesa de ultramar.', 'Francés y tahitiano. Cristianos.', 'Pesca, perlas.', 'Turismo, perlas y gasto francés.',
  'El independentismo y el legado de los ensayos nucleares.', [(1966, 'Ensayos nucleares en Mururoa hasta 1996.'), (2013, 'La ONU la vuelve a listar para descolonizar.')])
P('New Caledonia', 'Numea', 'Colectividad francesa con estatus especial.', 'Francés y lenguas canacas. Cristianos.', 'Níquel (de las mayores reservas del mundo), cromo, cobalto.',
  'Níquel en crisis y transferencias francesas.', 'La independencia, tras tres referendos y la revuelta de 2024.', [(1853, 'Anexión francesa.'), (1998, 'Acuerdo de Numea.'), (2024, 'Revuelta canaca.'), (2025, 'Acuerdo de Bougival para un «Estado de Nueva Caledonia».')])
P('Wallis and Futuna Is.', 'Mata-Utu', 'Colectividad francesa con reyes tradicionales.', 'Francés y lenguas locales. Católicos.', 'Pesca.', 'Agricultura de subsistencia y gasto francés.',
  'La emigración.', [(1961, 'Territorio de ultramar.')])
P('Pitcairn Is.', 'Adamstown', 'Territorio británico de ultramar.', 'Inglés y pitkern. Adventistas.', 'Pesca.', 'Venta de sellos, miel y ayuda.',
  'Su supervivencia con unas 50 personas.', [(1790, 'Llegan los amotinados de la Bounty.'), (2004, 'Juicios por abusos.')])
P('Norfolk Island', 'Kingston', 'Territorio australiano; perdió su autonomía en 2015.', 'Inglés y norfuk. Cristianos.', 'Pesca.', 'Turismo.',
  'La pérdida del autogobierno.', [(1856, 'Llegan los descendientes de la Bounty.'), (2015, 'Australia suprime su parlamento.')])
P('Indian Ocean Ter.', 'Flying Fish Cove (Christmas) y West Island (Cocos)', 'Territorios australianos.', 'Inglés, malayo y chino. Musulmanes y budistas.', 'Fosfatos.',
  'Fosfatos, centro de detención migratoria y turismo.', 'Su uso militar y migratorio en el Índico.', [(1955, 'Cocos pasa a Australia.'), (1958, 'Christmas pasa a Australia.')])
P('Heard I. and McDonald Is.', '—', 'Territorio australiano deshabitado.', '—', 'Pesca.', 'Licencias de pesca.', 'Su reserva marina.', [(1947, 'Pasa a Australia.')])
P('Ashmore and Cartier Is.', '—', 'Territorio australiano deshabitado.', '—', 'Pesca, petróleo cercano.', 'Ninguna.', 'Los pescadores indonesios y el petróleo del mar de Timor.', [(1931, 'Pasa a Australia.')])

# ───────────────────────── África del Norte ─────────────────────────

P('Morocco', 'Rabat', 'Monarquía constitucional; el rey y su entorno (el Majzén) concentran el poder real.', 'Árabe y amazig; francés en uso. Musulmanes.',
  'Fosfatos (70 % de las reservas mundiales), pesca, plomo, zinc.', 'Fosfatos y fertilizantes, automotriz, turismo y remesas.',
  'La soberanía sobre el Sahara Occidental, ya reconocida por EE.UU., la rivalidad con Argelia y su papel de puerta de África.',
  [(1956, 'Independencia.'), (1975, 'Marcha Verde sobre el Sahara.'), (2011, 'Reforma constitucional tras las protestas.'), (2020, 'EE.UU. reconoce su soberanía sobre el Sahara a cambio de relaciones con Israel.'), (2025, 'La ONU respalda su plan de autonomía.')])
EXTRA['W. Sahara'] = {}
P('W. Sahara', 'El Aaiún', 'Territorio no autónomo: Marruecos controla cerca del 80 % al oeste del muro; el Frente Polisario, el resto.', 'Árabe hasaní. Musulmanes.',
  'Fosfatos, pesca, arena.', 'Fosfatos de Bucraa y pesca, explotados por Marruecos.', 'La soberanía, tras el aval de la ONU a la autonomía bajo Marruecos.',
  [(1975, 'Retirada española y Marcha Verde.'), (1976, 'El Polisario proclama la República Saharaui.'), (1991, 'Alto el fuego de la ONU.'), (2020, 'Fin del alto el fuego.')])
P('Algeria', 'Argel', 'República presidencialista con las fuerzas armadas como poder real.', 'Árabe y amazig. Musulmanes.',
  'Gas, petróleo, hierro, fosfatos, uranio.', 'Hidrocarburos (más del 90 % de las exportaciones).', 'Su papel como proveedor de gas de Europa, la rivalidad con Marruecos y la sucesión del régimen.',
  [(1962, 'Independencia tras la guerra con Francia.'), (1991, 'Golpe y guerra civil.'), (2019, 'Hirak y caída de Buteflika.')])
P('Tunisia', 'Túnez', 'República presidencialista con el poder concentrado desde 2021.', 'Árabe. Musulmanes.', 'Fosfatos, petróleo, hierro.',
  'Turismo, textiles, fosfatos y aceite de oliva.', 'La deriva autoritaria y su papel de filtro migratorio para la UE.',
  [(1956, 'Independencia.'), (2011, 'Revolución que abre la Primavera Árabe.'), (2021, 'El presidente cierra el parlamento.'), (2023, 'Acuerdo migratorio con la UE.')])
P('Libya', 'Trípoli', 'Dividida entre un gobierno en Trípoli y el poder de Haftar en el este, cada uno con apoyos externos.', 'Árabe. Musulmanes.',
  'Petróleo (mayores reservas de África), gas.', 'Petróleo; la renta financia a las milicias.', 'Quién controla el petróleo y la presencia de Rusia y Turquía.',
  [(1951, 'Independencia.'), (1969, 'Gadafi toma el poder.'), (2011, 'Intervención de la OTAN y caída de Gadafi.'), (2014, 'Segunda guerra civil.'), (2020, 'Alto el fuego.')])
P('Mauritania', 'Nuakchot', 'República presidencialista con fuerte peso militar.', 'Árabe; francés en uso. Musulmanes.', 'Hierro, oro, cobre, gas marino, pesca.',
  'Hierro, oro, pesca y el nuevo gas compartido con Senegal.', 'Su estabilidad frente al Sahel y su papel de filtro migratorio.',
  [(1960, 'Independencia.'), (1981, 'Última abolición de la esclavitud.'), (2008, 'Golpe.'), (2025, 'Primer gas del yacimiento GTA.')])

# ───────────────────────── Sahel y África occidental ─────────────────────────

P('Mali', 'Bamako', 'Junta militar apoyada por el Africa Corps ruso; el norte y el centro en manos de grupos armados.', 'Bambara y lenguas locales. Musulmanes.',
  'Oro, litio, uranio, fosfatos.', 'Oro y algodón.', 'Si la junta resiste al bloqueo yihadista de Bamako y quién controla el oro.',
  [(1960, 'Independencia.'), (2012, 'Rebelión tuareg y yihadista; intervención francesa.'), (2020, 'Golpe.'), (2022, 'Expulsión de Francia; llega Wagner.'), (2025, 'Bloqueo de combustible del JNIM.')])
P('Burkina Faso', 'Uagadugú', 'Junta militar apoyada por Rusia; gran parte del territorio fuera de control.', 'Mooré, francés y lenguas locales. Musulmanes y cristianos.',
  'Oro, manganeso, zinc.', 'Oro y algodón.', 'El avance yihadista y la nacionalización de las minas de oro.',
  [(1960, 'Independencia.'), (1987, 'Asesinato de Sankara.'), (2022, 'Dos golpes.'), (2023, 'Expulsión de Francia.'), (2024, 'Confederación del Sahel con Malí y Níger.')])
P('Niger', 'Niamey', 'Junta militar aliada con Rusia.', 'Hausa, zarma y francés. Musulmanes.', 'Uranio, oro, petróleo, carbón.',
  'Uranio, petróleo y agricultura de subsistencia.', 'El uranio que antes iba a Francia y el oleoducto hacia Benín.',
  [(1960, 'Independencia.'), (2023, 'Golpe; salen Francia y EE.UU.'), (2024, 'Retira la licencia de uranio de Orano.'), (2025, 'Nacionaliza la mina de Somair.')])
P('Chad', "Yamena", 'Régimen militar dinástico legitimado por elecciones.', 'Árabe y francés. Musulmanes y cristianos.', 'Petróleo, oro, uranio.',
  'Petróleo y ganadería.', 'Su papel en la guerra de Sudán y la salida de las tropas francesas.',
  [(1960, 'Independencia.'), (1990, 'Déby toma el poder.'), (2021, 'Muere Déby; lo sucede su hijo.'), (2025, 'Se van las tropas francesas.')])
P('Senegal', 'Dakar', 'República presidencialista con alternancias pacíficas.', 'Wolof y francés. Musulmanes.', 'Fosfatos, pesca, petróleo y gas marinos, oro.',
  'Pesca, fosfatos, servicios y el nuevo petróleo de Sangomar.', 'La renta petrolera y la deuda oculta descubierta en 2024.',
  [(1960, 'Independencia.'), (2024, 'Gana un gobierno soberanista.'), (2024, 'Primer petróleo.'), (2025, 'Cierre de las bases francesas.')])
P('Gambia', 'Banjul', 'República presidencialista.', 'Inglés y mandinga. Musulmanes.', 'Pesca, arena.', 'Turismo, remesas y reexportación.',
  'Las elecciones presidenciales de diciembre de 2026.', [(1965, 'Independencia.'), (1994, 'Golpe de Jammeh.'), (2017, 'Salida de Jammeh tras perder las elecciones.')])
P('Guinea-Bissau', 'Bisáu', 'República semipresidencialista con fuerte peso militar.', 'Portugués y criollo. Musulmanes y animistas.', 'Pesca, bauxita, fosfatos.',
  'Castaña de cajú; escala del narcotráfico hacia Europa.', 'El narcotráfico y las elecciones de diciembre de 2026.',
  [(1973, 'Independencia.'), (1998, 'Guerra civil.'), (2009, 'Asesinato del presidente.'), (2025, 'Golpe militar tras las elecciones.')])
P('Guinea', 'Conakri', 'Junta militar desde 2021, legitimada con elecciones en 2025.', 'Francés y lenguas locales. Musulmanes.',
  'Bauxita (mayores reservas del mundo), hierro de Simandou, oro, diamantes.', 'Bauxita y oro; Simandou empezó a exportar en 2025.',
  'El hierro de Simandou, controlado por capital chino y Rio Tinto.', [(1958, 'Independencia.'), (2021, 'Golpe.'), (2025, 'Primer embarque de Simandou y elección presidencial.')])
P('Sierra Leone', 'Freetown', 'República presidencialista.', 'Inglés y krio. Musulmanes y cristianos.', 'Diamantes, rutilo, bauxita, hierro, oro.',
  'Minería y agricultura.', 'La memoria de los diamantes de sangre y la pobreza.', [(1961, 'Independencia.'), (1991, 'Guerra civil hasta 2002.'), (2014, 'Ébola.')])
P('Liberia', 'Monrovia', 'República presidencialista.', 'Inglés. Cristianos.', 'Hierro, madera, diamantes, oro.',
  'Registro de buques (el mayor del mundo), caucho, hierro.', 'Su bandera de conveniencia y la corrupción.', [(1847, 'Independencia.'), (1989, 'Guerras civiles hasta 2003.'), (2006, 'Primera presidenta de África.')])
P("Côte d'Ivoire", 'Yamusukro (sede de gobierno en Abiyán)', 'República presidencialista.', 'Francés y lenguas locales. Musulmanes y cristianos.', 'Petróleo, gas, oro, manganeso.',
  'Cacao (primer productor mundial), café, petróleo.', 'La sucesión política y el cacao.', [(1960, 'Independencia.'), (2002, 'Guerra civil.'), (2011, 'Crisis poselectoral.'), (2025, 'Cuarto mandato presidencial.')])
P('Ghana', 'Acra', 'República presidencialista con alternancias regulares.', 'Inglés. Cristianos y musulmanes.', 'Oro, cacao, petróleo, bauxita, manganeso.',
  'Oro, cacao y petróleo.', 'La minería ilegal de oro (galamsey) y la reestructuración de su deuda.', [(1957, 'Primera independencia del África subsahariana.'), (1992, 'Retorno de la democracia.'), (2022, 'Default.')])
P('Togo', 'Lomé', 'República parlamentaria desde 2024; la misma familia gobierna desde 1967.', 'Francés y ewe. Cristianos y animistas.', 'Fosfatos, piedra caliza.',
  'Puerto de Lomé, fosfatos y agricultura.', 'La reforma que eterniza al gobernante y la amenaza yihadista en el norte.', [(1960, 'Independencia.'), (1967, 'Golpe de Eyadéma.'), (2005, 'Lo sucede su hijo.'), (2024, 'Reforma parlamentaria.')])
P('Benin', 'Porto Novo (sede de gobierno en Cotonú)', 'República presidencialista con creciente concentración del poder.', 'Francés y fon. Cristianos, musulmanes y vudú.',
  'Petróleo, piedra caliza.', 'Algodón, puerto de Cotonú y reexportación a Nigeria.', 'Los ataques yihadistas en el norte y el intento de golpe de 2025.',
  [(1960, 'Independencia.'), (1990, 'Transición democrática.'), (2025, 'Intento de golpe frustrado con apoyo nigeriano.')])
P('Nigeria', 'Abuya', 'República presidencialista federal.', 'Inglés, hausa, yoruba e igbo. Musulmanes y cristianos.', 'Petróleo, gas, estaño, carbón, tierras agrícolas.',
  'Petróleo, agricultura y servicios; el país más poblado de África.', 'La insurgencia yihadista, el bandidaje, el robo de petróleo y su peso en África occidental.',
  [(1960, 'Independencia.'), (1967, 'Guerra de Biafra.'), (1999, 'Retorno de la democracia.'), (2009, 'Insurgencia de Boko Haram.'), (2023, 'Fin del subsidio a la nafta.')])
P('Cabo Verde', 'Praia', 'República parlamentaria democrática.', 'Portugués y criollo. Católicos.', 'Sal, pesca.', 'Turismo y remesas.',
  'Su posición atlántica.', [(1975, 'Independencia.'), (1991, 'Elecciones multipartidarias.')])

# ───────────────────────── África central ─────────────────────────

P('Cameroon', 'Yaundé', 'República presidencialista; el mismo presidente gobierna desde 1982.', 'Francés e inglés. Cristianos y musulmanes.',
  'Petróleo, bauxita, hierro, madera, cacao.', 'Petróleo, madera, cacao y café.', 'La sucesión, la guerra en las regiones anglófonas y Boko Haram en el norte.',
  [(1960, 'Independencia.'), (1982, 'Biya llega al poder.'), (2017, 'Guerra en las regiones anglófonas.'), (2025, 'Octavo mandato tras elecciones disputadas.')])
P('Central African Rep.', 'Bangui', 'República presidencialista cuya seguridad depende de fuerzas rusas.', 'Sango y francés. Cristianos y musulmanes.',
  'Diamantes, oro, uranio, madera.', 'Diamantes, oro y madera.', 'El control ruso de minas a cambio de seguridad.',
  [(1960, 'Independencia.'), (2013, 'Guerra civil.'), (2018, 'Llegan los mercenarios de Wagner.'), (2023, 'Referéndum que permite un tercer mandato.')])
P('Gabon', 'Libreville', 'Régimen surgido del golpe de 2023, legitimado en elecciones en 2025.', 'Francés. Cristianos.', 'Petróleo, manganeso, madera, hierro.',
  'Petróleo, manganeso y madera.', 'El fin de la dinastía Bongo y la relación con Francia.', [(1960, 'Independencia.'), (1967, 'Omar Bongo llega al poder.'), (2023, 'Golpe contra Ali Bongo.'), (2025, 'Elección del jefe del golpe.')])
P('Eq. Guinea', 'Malabo', 'Dictadura familiar desde 1979.', 'Español, francés y portugués. Católicos.', 'Petróleo, gas, madera.',
  'Petróleo y gas en declive.', 'La sucesión familiar y la renta petrolera.', [(1968, 'Independencia de España.'), (1979, 'Golpe de Obiang.'), (1996, 'Comienza la producción de petróleo.')])
P('São Tomé and Principe', 'Santo Tomé', 'República semipresidencialista.', 'Portugués. Católicos.', 'Pesca, petróleo marino.', 'Cacao, turismo y ayuda.',
  'La exploración petrolera.', [(1975, 'Independencia.'), (2022, 'Intento de golpe.')])
P('Congo', 'Brazzaville', 'República presidencialista; el mismo presidente gobierna desde 1997.', 'Francés, lingala y kituba. Cristianos.', 'Petróleo, madera, potasa, hierro.',
  'Petróleo.', 'La sucesión y la deuda petrolera con China y los traders.', [(1960, 'Independencia.'), (1997, 'Guerra civil y regreso de Sassou Nguesso.')])
P('Dem. Rep. Congo', 'Kinsasa', 'República semipresidencialista; el Estado no controla el este, en manos del M23 y otros grupos.', 'Francés, lingala, suajili, kikongo y tshiluba. Cristianos.',
  'Cobalto (70 % de la producción mundial), cobre, coltán, oro, diamantes, estaño, litio.', 'Minería de cobre y cobalto, con fuerte presencia china.',
  'Los minerales críticos del este, la guerra con el M23 respaldado por Ruanda y el acuerdo de minerales con EE.UU.',
  [(1960, 'Independencia; asesinato de Lumumba.'), (1965, 'Dictadura de Mobutu.'), (1996, 'Primera guerra del Congo.'), (1998, 'Segunda guerra del Congo.'), (2025, 'El M23 toma Goma y Bukavu; acuerdo de paz en Washington.')])
P('Rwanda', 'Kigali', 'República presidencialista con el poder concentrado en el partido gobernante desde 1994.', 'Kinyarwanda, francés, inglés y suajili. Cristianos.',
  'Estaño, tantalio, tungsteno, oro.', 'Servicios, turismo, minerales (incluidos los del Congo) y misiones de paz.', 'Su apoyo al M23 en el Congo y su imagen de Estado eficaz.',
  [(1962, 'Independencia.'), (1994, 'Genocidio tutsi.'), (2000, 'Kagame asume la presidencia.'), (2025, 'Acuerdo de paz con el Congo.')])
P('Burundi', 'Gitega', 'República presidencialista con un partido dominante surgido de la guerrilla.', 'Kirundi, francés e inglés. Cristianos.', 'Níquel, tierras raras, oro.',
  'Agricultura de subsistencia, café y té.', 'Su intervención en el este del Congo y la pobreza extrema.', [(1962, 'Independencia.'), (1993, 'Guerra civil.'), (2015, 'Crisis por el tercer mandato.')])

# ───────────────────────── África oriental y Cuerno ─────────────────────────

P('Sudan', 'Jartum (gobierno instalado en Port Sudan durante la guerra)', 'Junta militar en guerra con las Fuerzas de Apoyo Rápido, que controlan Darfur.', 'Árabe e inglés. Musulmanes.',
  'Oro, petróleo, tierras agrícolas, cromo.', 'Oro, agricultura y ganadería; destruida por la guerra.', 'La guerra, la partición de hecho, el oro y la intervención de Emiratos, Egipto y otros.',
  [(1956, 'Independencia.'), (1989, 'Golpe de al-Bashir.'), (2011, 'Independencia de Sudán del Sur.'), (2019, 'Caída de al-Bashir.'), (2023, 'Guerra entre el ejército y las FAR.'), (2025, 'Las FAR toman El Fasher.')])
P('S. Sudan', 'Yuba', 'República presidencialista con milicias étnicas y un acuerdo de paz frágil.', 'Inglés y lenguas locales. Cristianos y animistas.', 'Petróleo, oro, madera.',
  'Petróleo exportado por Sudán.', 'La recaída en la guerra civil y el oleoducto cortado por la guerra en Sudán.', [(2011, 'Independencia.'), (2013, 'Guerra civil.'), (2018, 'Acuerdo de paz.'), (2025, 'Arresto del vicepresidente Machar.')])
P('Ethiopia', 'Adís Abeba', 'República parlamentaria federal con poder concentrado en el primer ministro.', 'Amárico, oromo y lenguas regionales. Ortodoxos, musulmanes y protestantes.',
  'Oro, potasa, gas, hidroelectricidad.', 'Agricultura, café, aviación (Ethiopian Airlines) y servicios.',
  'La guerra en Amhara, la tensión con Tigray y Eritrea, la gran represa del Nilo y la salida al mar.',
  [(1974, 'Caída de Haile Selassie.'), (1991, 'Cae el Derg.'), (1993, 'Independencia de Eritrea.'), (2020, 'Guerra de Tigray.'), (2025, 'Inauguración de la Gran Represa del Renacimiento.')])
P('Eritrea', 'Asmara', 'Dictadura de partido único sin elecciones desde la independencia.', 'Tigriña, árabe e inglés. Ortodoxos y musulmanes.', 'Oro, cobre, potasa, pesca.',
  'Minería y remesas; servicio militar indefinido.', 'La tensión con Etiopía por el acceso al mar Rojo.', [(1993, 'Independencia.'), (1998, 'Guerra con Etiopía.'), (2018, 'Paz con Etiopía.')])
P('Djibouti', 'Yibuti', 'República presidencialista; el mismo presidente desde 1999.', 'Francés y árabe. Musulmanes.', 'Sal, geotermia.',
  'Puerto, alquiler de bases y el tren a Etiopía.', 'Las bases de EE.UU., China, Francia y Japón sobre Bab el-Mandeb.', [(1977, 'Independencia.'), (2017, 'Primera base china en el exterior.')])
P('Somalia', 'Mogadiscio', 'República federal; el gobierno depende de fuerzas africanas y Al Shabaab controla zonas rurales.', 'Somalí y árabe. Musulmanes.',
  'Uranio, hierro, petróleo, pesca.', 'Ganadería, remesas y telecomunicaciones.', 'La lucha contra Al Shabaab y la puja entre Turquía, Emiratos y Etiopía.',
  [(1960, 'Independencia.'), (1991, 'Colapso del Estado.'), (2006, 'Invasión etíope y surgimiento de Al Shabaab.'), (2024, 'Pacto de defensa con Turquía.')])
EXTRA['Somaliland'] = {'pob': (5700000, 2024), 'area': 177000}
P('Somaliland', 'Hargeisa', 'República presidencialista democrática no reconocida internacionalmente.', 'Somalí, árabe e inglés. Musulmanes.', 'Pesca, petróleo, carbón.',
  'Ganadería, remesas y el puerto de Berbera.', 'Su reconocimiento, buscado a cambio de acceso al mar para Etiopía o de una base para EE.UU.',
  [(1960, 'Independencia del Reino Unido y unión con Somalia.'), (1991, 'Declara su secesión.'), (2024, 'Memorando de acceso al mar con Etiopía.')])
P('Kenya', 'Nairobi', 'República presidencialista.', 'Suajili e inglés. Cristianos y musulmanes.', 'Tierras agrícolas, piedra caliza, oro, titanio.',
  'Agricultura, servicios financieros (M-Pesa), turismo; puerto de Mombasa.', 'La protesta juvenil contra los impuestos, la deuda con China y su papel de aliado de EE.UU.',
  [(1963, 'Independencia.'), (1998, 'Atentado a la embajada de EE.UU.'), (2013, 'Ataque al centro comercial Westgate.'), (2024, 'Protestas y asalto al parlamento.'), (2024, 'Encabeza la misión de seguridad en Haití.')])
P('Uganda', 'Kampala', 'República presidencialista; el mismo presidente gobierna desde 1986.', 'Inglés y suajili. Cristianos.', 'Petróleo, oro, cobre, tierras agrícolas.',
  'Agricultura, café y el petróleo del lago Alberto con el oleoducto EACOP.', 'La sucesión y el primer petróleo.', [(1962, 'Independencia.'), (1971, 'Dictadura de Amin.'), (1986, 'Museveni toma el poder.')])
P('Tanzania', 'Dodoma', 'República presidencialista dominada por el mismo partido desde la independencia.', 'Suajili e inglés. Cristianos y musulmanes.',
  'Oro, gas, diamantes, níquel, grafito.', 'Oro, turismo, agricultura y gas.', 'La represión tras las elecciones de 2025 y la puja minera.', [(1961, 'Independencia.'), (1964, 'Unión con Zanzíbar.'), (2025, 'Elecciones con represión de las protestas.')])

# ───────────────────────── África austral ─────────────────────────

P('Angola', 'Luanda', 'República presidencialista dominada por el MPLA desde 1975.', 'Portugués. Católicos.', 'Petróleo, diamantes, hierro, cobre.',
  'Petróleo (el 90 % de las exportaciones) y diamantes.', 'El corredor de Lobito financiado por EE.UU. y la deuda con China.', [(1975, 'Independencia y guerra civil.'), (2002, 'Fin de la guerra.'), (2017, 'Fin del gobierno de dos Santos.')])
P('Zambia', 'Lusaka', 'República presidencialista con alternancias.', 'Inglés. Cristianos.', 'Cobre, cobalto, esmeraldas.', 'Minería del cobre.',
  'La reestructuración de su deuda y el corredor de Lobito.', [(1964, 'Independencia.'), (2020, 'Default.'), (2025, 'Derrame tóxico de una minera china.')])
P('Zimbabwe', 'Harare', 'República presidencialista dominada por ZANU-PF y los militares.', 'Inglés, shona y ndebele. Cristianos.', 'Platino, oro, litio, diamantes, carbón.',
  'Minería, tabaco y remesas.', 'El litio en manos chinas y la sucesión dentro del partido.', [(1980, 'Independencia.'), (2000, 'Reforma agraria.'), (2008, 'Hiperinflación.'), (2017, 'Golpe contra Mugabe.')])
P('Malawi', 'Lilongüe', 'República presidencialista con alternancias.', 'Inglés y chichewa. Cristianos.', 'Tierras agrícolas, uranio, tierras raras.',
  'Tabaco y agricultura.', 'La escasez de divisas y la pobreza.', [(1964, 'Independencia.'), (2020, 'Anulación de elecciones fraudulentas.'), (2025, 'Vuelve Mutharika.')])
P('Mozambique', 'Maputo', 'República presidencialista dominada por el FRELIMO desde 1975.', 'Portugués. Cristianos y musulmanes.', 'Gas (grandes reservas en Cabo Delgado), carbón, grafito, titanio.',
  'Aluminio, carbón y el gas de TotalEnergies y ExxonMobil.', 'La insurgencia de Cabo Delgado y el gas.', [(1975, 'Independencia.'), (1977, 'Guerra civil hasta 1992.'), (2017, 'Insurgencia en Cabo Delgado.'), (2024, 'Protestas tras elecciones fraudulentas.')])
P('Madagascar', 'Antananarivo', 'Régimen militar de transición tras el golpe de 2025.', 'Malgache y francés. Cristianos.', 'Grafito, níquel, cobalto, ilmenita, vainilla.',
  'Vainilla, minería y textiles.', 'La transición tras la caída del gobierno.', [(1960, 'Independencia.'), (2009, 'Golpe.'), (2025, 'Revuelta juvenil y toma del poder militar.')])
P('Namibia', 'Windhoek', 'República presidencialista.', 'Inglés. Cristianos.', 'Uranio, diamantes, oro, petróleo marino, litio.',
  'Minería, pesca y nuevas reservas de petróleo.', 'El petróleo de la cuenca de Orange.', [(1990, 'Independencia de Sudáfrica.'), (2022, 'Descubrimientos petroleros.')])
P('Botswana', 'Gaborone', 'República parlamentaria estable.', 'Inglés y setsuana. Cristianos.', 'Diamantes, cobre, níquel, carbón.',
  'Diamantes (Debswana, en sociedad con De Beers).', 'La caída del precio del diamante.', [(1966, 'Independencia.'), (1967, 'Descubrimiento de diamantes.'), (2024, 'Primera alternancia.')])
P('South Africa', 'Pretoria (ejecutivo); Ciudad del Cabo; Bloemfontein', 'República parlamentaria; gobierno de coalición desde 2024.', 'Once lenguas oficiales. Cristianos.',
  'Platino (mayores reservas del mundo), oro, manganeso, cromo, carbón, hierro.', 'Minería, finanzas, industria; desempleo alto.',
  'Su papel en los BRICS, la tensión con EE.UU. y el deterioro de la energía y la logística.',
  [(1948, 'Apartheid.'), (1994, 'Primeras elecciones democráticas.'), (2010, 'Entra en los BRICS.'), (2024, 'El ANC pierde la mayoría.'), (2025, 'EE.UU. le aplica aranceles y boicotea el G20 de Johannesburgo.')])
P('Lesotho', 'Maseru', 'Monarquía constitucional.', 'Sesotho e inglés. Cristianos.', 'Agua, diamantes.', 'Textiles, agua vendida a Sudáfrica y remesas.',
  'Su dependencia de Sudáfrica.', [(1966, 'Independencia.'), (1998, 'Intervención sudafricana.')])
P('eSwatini', 'Mbabane', 'Monarquía absoluta.', 'Suazi e inglés. Cristianos.', 'Carbón, madera.', 'Azúcar y transferencias aduaneras.',
  'El poder absoluto del rey y la protesta prodemocrática.', [(1968, 'Independencia.'), (2021, 'Protestas reprimidas.'), (2025, 'Recibe deportados desde EE.UU.')])
P('Comoros', 'Moroni', 'República presidencialista federal.', 'Comorense, francés y árabe. Musulmanes.', 'Pesca.', 'Remesas, vainilla y clavo.',
  'Su reclamo sobre Mayotte.', [(1975, 'Independencia.'), (1997, 'Secesión de Anjouan.')])
P('Mauritius', 'Port Louis', 'República parlamentaria.', 'Inglés, francés y criollo. Hindúes, cristianos y musulmanes.', 'Pesca.',
  'Turismo, finanzas extraterritoriales y textiles.', 'Su soberanía sobre Chagos y la base de Diego García.', [(1968, 'Independencia.'), (2019, 'La Corte Internacional respalda su reclamo sobre Chagos.'), (2025, 'Acuerdo de traspaso de Chagos.')])
P('Seychelles', 'Victoria', 'República presidencialista.', 'Criollo, inglés y francés. Católicos.', 'Pesca.', 'Turismo, pesca y servicios financieros.',
  'Su posición en el Índico entre India, China y los Emiratos.', [(1976, 'Independencia.'), (2025, 'Alternancia electoral.')])
P('Saint Helena', 'Jamestown', 'Territorio británico de ultramar (con Ascensión y Tristán de Acuña).', 'Inglés. Anglicanos.', 'Pesca.',
  'Ayuda británica.', 'La base de Ascensión, usada por EE.UU. y el Reino Unido.', [(1659, 'Ocupación inglesa.'), (1815, 'Exilio de Napoleón.')])
P('Br. Indian Ocean Ter.', 'Diego García', 'Territorio británico con base militar conjunta de EE.UU.; acordado su traspaso a Mauricio con arriendo de la base.', 'Inglés.', 'Pesca.',
  'Sin economía civil: base militar.', 'El futuro de Diego García, base clave de EE.UU. en el Índico.', [(1965, 'Separación de Mauricio.'), (1971, 'Expulsión de los chagosianos.'), (2025, 'Tratado de traspaso a Mauricio.')])
P('Fr. S. Antarctic Lands', 'Saint-Pierre (Reunión)', 'Territorio francés de ultramar sin población permanente.', 'Francés.', 'Pesca.',
  'Licencias de pesca de austromerluza.', 'La enorme zona marítima que da a Francia.', [(1955, 'Creación del territorio.')])


def _corregir(lista, cambios, pais):
    """Agrega (año, hecho) o reemplaza/quita por texto: (texto viejo, (año, texto) | None)."""
    lista = list(lista)
    for c in cambios:
        if isinstance(c[0], str):
            i = [x for _, x in lista].index(c[0])  # falla si el texto viejo no está
            if c[1] is None: lista.pop(i)
            else: lista[i] = c[1]
        else:
            lista.append(c)
    return sorted(lista, key=lambda r: int(str(r[0])[:4]))


# Correcciones del 20 de noviembre de 2026 (ver fuente/correcciones.py)
from correcciones import PAIS_SET as _PS, PAIS_CRONO as _PC
for _k, _v in _PS.items(): PJ[_k].update(_v)
for _k, _v in _PC.items(): PJ[_k]['crono'] = _corregir(PJ[_k]['crono'], _v, _k)
