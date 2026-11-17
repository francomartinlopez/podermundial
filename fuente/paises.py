# Países: bloque, posición y zona liberada. Clave = nombre en el mapa (Natural Earth).
BLOQ = {"T": "Transoceánico", "E": "Euroasiático", "I": "Independiente", "D": "Terreno disputado"}
POS = {"C": "Centro", "A": "Aliado con autonomía", "G": "Integrado", "R": "Protectorado", "K": "Colonia de hecho", "U": "Autónomo",
       "P": "Pendular", "IT": "Inclinado al transoceánico", "IE": "Inclinado al euroasiático", "S": "Sin alinear"}
GRADO = {"": "", "P": "Parcial", "X": "Extendida", "T": "Total"}
ASP = {"t": "Territorial", "c": "Crimen organizado", "f": "Fronteras", "e": "Fiscal y económico", "x": "Presencia extranjera"}
RAW = """
United States of America|Estados Unidos|T|C|||Centro del imperio transoceánico.
Canada|Canadá|T|G|||Integrado por la defensa aérea común con EE.UU. (NORAD) y por una economía que vende a EE.UU. unas tres cuartas partes de sus exportaciones; tensión por los aranceles desde 2025.
United Kingdom|Reino Unido|T|A|||Conserva criterio estratégico propio, según el libro.
France|Francia|T|A|||Potencia nuclear con política exterior propia.
Germany|Alemania|T|G|||Principal economía de Europa; aloja bases y armas nucleares de EE.UU. y se rearma desde 2022 tras perder el gas ruso.
Italy|Italia|T|G|||Aloja bases de EE.UU. y de la OTAN; la 'Ndrangheta domina parte de Calabria y del tráfico de cocaína en Europa.
Spain|España|T|G|||Aloja las bases de EE.UU. en Rota y Morón; Ceuta y Melilla son su frontera terrestre con Marruecos.
Portugal|Portugal|T|G|||
Netherlands|Países Bajos|T|G|||Róterdam es, con Amberes, la principal puerta de entrada de cocaína a Europa; sede de ASML, clave para los chips avanzados.
Belgium|Bélgica|T|G|||Sede de la OTAN y de la Comisión Europea; Euroclear guarda la mayor parte de las reservas rusas inmovilizadas.
Luxembourg|Luxemburgo|T|G|||
Ireland|Irlanda|T|G|||
Denmark|Dinamarca|T|G|||
Greenland|Groenlandia|T|G|||Territorio danés bajo presión de EE.UU.
Norway|Noruega|T|G|||Principal proveedor de gas de Europa desde 2022 y dueño del mayor fondo soberano del mundo.
Sweden|Suecia|T|G|||
Finland|Finlandia|T|G|||
Iceland|Islandia|T|G|||
Poland|Polonia|T|G|||El país de la OTAN que más gasta en defensa en proporción a su PBI; frontera del bloque con Rusia y Bielorrusia.
Czechia|Chequia|T|G|||
Slovakia|Eslovaquia|T|G|||
Hungary|Hungría|T|G|||Gobierno proeuropeo de Péter Magyar desde su victoria de abril de 2026 sobre Orbán.
Austria|Austria|T|G|||
Switzerland|Suiza|T|A|||Neutral, integrada al sistema financiero occidental.
Slovenia|Eslovenia|T|G|||
Croatia|Croacia|T|G|||
Romania|Rumania|T|G|||
Bulgaria|Bulgaria|T|G|||
Greece|Grecia|T|G|||Sus armadores controlan la mayor flota mercante del mundo.
Cyprus|Chipre|T|G|P|x|El norte está bajo control turco desde 1974.
N. Cyprus|Chipre del Norte|D|K|P|x|Colonia de hecho de Turquía: solo Ankara la reconoce, mantiene allí decenas de miles de soldados, sostiene su presupuesto y su moneda es la lira turca.
Malta|Malta|T|G|||
Estonia|Estonia|T|G|||
Latvia|Letonia|T|G|||
Lithuania|Lituania|T|G|||
Albania|Albania|T|G|||
Macedonia|Macedonia del Norte|T|G|||
Montenegro|Montenegro|T|G|||
Bosnia and Herz.|Bosnia y Herzegovina|T|R|||Bajo supervisión del Alto Representante internacional.
Kosovo|Kosovo|T|R|||Depende de la presencia de la OTAN (KFOR).
Turkey|Turquía|T|P|||Miembro de la OTAN con agenda propia y compras de armas rusas.
Israel|Israel|T|A|||Margen de iniciativa militar sin igual dentro del bloque, según el libro.
Japan|Japón|T|G|||Aloja la mayor concentración de tropas de EE.UU. en el exterior y se rearma frente a China.
South Korea|Corea del Sur|T|G|||Unas 28.000 tropas de EE.UU. y un mando combinado de guerra; potencia en chips y astilleros.
Taiwan|Taiwán|T|R|||Su seguridad depende de EE.UU.
Australia|Australia|T|G|||Pacto AUKUS con EE.UU. y el Reino Unido para submarinos nucleares; ancla del bloque en el Pacífico Sur.
New Zealand|Nueva Zelanda|T|G|||
Philippines|Filipinas|T|G|P|t|Insurgencias residuales en Mindanao.
Ukraine|Ucrania|T|R|P|x t|Depende del apoyo occidental; parte de su territorio está ocupado por Rusia.
Micronesia|Micronesia|T|K|||Colonia de hecho de EE.UU.: por el Pacto de Libre Asociación, Washington decide su defensa y puede vetar la presencia militar de otros países; usa el dólar y depende de los fondos del pacto.
Marshall Is.|Islas Marshall|T|K|||Colonia de hecho de EE.UU.: por el Pacto de Libre Asociación, Washington decide su defensa y tiene allí la base de pruebas de misiles Reagan en Kwajalein; usa el dólar.
Palau|Palaos|T|K|||Colonia de hecho de EE.UU.: por el Pacto de Libre Asociación, Washington decide su defensa; usa el dólar y depende de los fondos del pacto.
Liechtenstein|Liechtenstein|T|G|||
Monaco|Mónaco|T|G|||
San Marino|San Marino|T|G|||
Andorra|Andorra|T|G|||
Vatican|Vaticano|D|S|||Sede de la Santa Sede.
Russia|Rusia|E|C|||Centro de la alianza euroasiática junto con China.
China|China|E|C|||Centro de la alianza euroasiática junto con Rusia.
Hong Kong|Hong Kong|E|G|||Bajo control directo de Pekín desde la ley de seguridad nacional de 2020.
Macao|Macao|E|G|||
Iran|Irán|E|A|||Miembro de la alianza euroasiática con agenda propia; tras la guerra de 2026 con EE.UU. e Israel, el poder se desplazó hacia la Guardia Revolucionaria.
Belarus|Bielorrusia|E|R|||Integrada militar y económicamente a Rusia.
North Korea|Corea del Norte|E|A|||Potencia nuclear con tratado de defensa mutua con Rusia desde 2024; envió tropas a la guerra en Ucrania.
Cuba|Cuba|E|G|||Crisis económica profunda y emigración masiva; sostenida por Rusia y China.
Nicaragua|Nicaragua|E|G|||Régimen familiar de Ortega y Murillo, alineado con Rusia.
India|India|I|U|||Independiente, por escala y por decisión propia.
Brazil|Brasil|I|U|P|c t|Territorios bajo control de facciones criminales y minería ilegal en la Amazonía.
Mexico|México|D|IT|X|c f|Amplias zonas bajo control de cárteles.
Guatemala|Guatemala|D|IT|P|c|
Belize|Belice|D|IT|||
Honduras|Honduras|D|IT|P|c|
El Salvador|El Salvador|D|IT|||
Nicaragua_|—|D|S|||
Costa Rica|Costa Rica|D|IT|||
Panama|Panamá|D|IT|||Canal bajo presión estratégica de EE.UU.
Colombia|Colombia|D|IT|X|t c|Grupos armados y narcotráfico en amplias regiones; gobierno de De la Espriella desde agosto de 2026.
Venezuela|Venezuela|T|R|P|c|Protectorado de EE.UU. en transición desde la captura de Maduro en enero de 2026.
Ecuador|Ecuador|D|IT|X|c|Ola de violencia de bandas ligadas al narcotráfico.
Peru|Perú|D|IT|P|c t|Gran productor de cobre; una naviera estatal china opera el puerto de Chancay desde 2024.
Bolivia|Bolivia|D|IT|P|c f|
Chile|Chile|D|IT|||Primer productor mundial de cobre y una de las mayores reservas de litio.
Argentina|Argentina|D|IT|||Gobierno alineado con EE.UU.
Uruguay|Uruguay|D|S|||
Paraguay|Paraguay|D|IT|P|c f|Triple Frontera.
Guyana|Guyana|D|IT|||Boom petrolero operado por ExxonMobil; Venezuela reclama el Esequibo.
Suriname|Surinam|D|S|||
Haiti|Haití|D|S|T|c t|Pandillas controlan la mayor parte de la capital.
Dominican Rep.|República Dominicana|D|IT|||
Jamaica|Jamaica|D|IT|P|c|
Trinidad and Tobago|Trinidad y Tobago|D|IT|P|c|
Bahamas|Bahamas|D|IT|||
Puerto Rico|Puerto Rico|T|G|||Territorio de EE.UU.
Saudi Arabia|Arabia Saudita|D|IT|||Aliada de seguridad de EE.UU. con agenda propia.
United Arab Emirates|Emiratos Árabes Unidos|D|IT|||Potencia financiera y logística con agenda propia en Sudán, Libia y Yemen; aloja tropas de EE.UU.
Qatar|Catar|D|IT|||Base de Al Udeid; mediador con actores del eje iraní.
Bahrain|Baréin|D|R|||Sede de la Quinta Flota de EE.UU.
Kuwait|Kuwait|D|IT|||
Oman|Omán|D|S|||
Yemen|Yemen|D|S|X|t x|Dividido entre hutíes, gobierno reconocido y fuerzas del sur.
Jordan|Jordania|D|R|||Depende de la ayuda y la protección de EE.UU.
Egypt|Egipto|D|IT|||Las fuerzas armadas controlan buena parte de la economía; dueño del canal de Suez.
Iraq|Irak|D|P|P|x|Disputado entre Irán y EE.UU.; milicias con poder propio.
Syria|Siria|D|S|X|t x|El gobierno de al-Sharaa recuperó el noreste en 2026, pero Israel ocupa una franja del sur.
Lebanon|Líbano|D|P|P|x t|Hezbolá y presencia israelí en el sur.
Palestine|Palestina|D|S|T|x t|Ocupación y guerra en Gaza.
Afghanistan|Afganistán|D|S|P|f|Gobierno talibán; frontera disputada con Pakistán.
Pakistan|Pakistán|D|P|P|t f|Entre China, EE.UU. y Arabia Saudita; insurgencias en el oeste.
Bangladesh|Bangladés|D|S|||Tras la caída de Sheikh Hasina en 2024, el BNP ganó las elecciones de 2026.
Sri Lanka|Sri Lanka|D|S|||
Nepal|Nepal|D|S|||
Bhutan|Bután|D|S|||
Maldives|Maldivas|D|S|||
Myanmar|Myanmar|D|IE|X|t c|Junta apoyada por China y Rusia; perdió buena parte del territorio.
Thailand|Tailandia|D|S|||El ejército y la monarquía conservan poder por encima de los gobiernos electos.
Laos|Laos|D|IE|P|c|Zona económica especial del Triángulo de Oro.
Cambodia|Camboya|D|IE|P|c|Complejos de estafa a escala industrial.
Vietnam|Vietnam|D|S|||Partido único con economía integrada a las cadenas de suministro de EE.UU.; disputa islas con China.
Malaysia|Malasia|D|S|||Ribera del estrecho de Malaca; equilibra entre China y EE.UU.
Singapore|Singapur|D|IT|||Centro financiero y logístico sobre el estrecho de Malaca; socio de seguridad de EE.UU. sin alianza formal.
Indonesia|Indonesia|D|S|||El país musulmán más poblado; controla los estrechos de Malaca, la Sonda y Lombok y no se alinea.
Brunei|Brunéi|D|S|||
Timor-Leste|Timor Oriental|D|S|||
Mongolia|Mongolia|D|S|||
Kazakhstan|Kazajistán|D|IE|||Miembro de la OTSC con política multivectorial.
Kyrgyzstan|Kirguistán|D|IE|||
Tajikistan|Tayikistán|D|IE|||
Uzbekistan|Uzbekistán|D|S|||
Turkmenistan|Turkmenistán|D|S|||
Azerbaijan|Azerbaiyán|D|S|||Cerca de Turquía e Israel.
Armenia|Armenia|D|S|||Se aleja de Rusia desde 2023.
Georgia|Georgia|D|P|P|x|Abjasia y Osetia del Sur bajo control ruso.
Moldova|Moldavia|D|IT|P|x|Transnistria con tropas rusas.
Serbia|Serbia|D|P|||Candidata a la UE con lazos con Rusia y China.
Papua New Guinea|Papúa Nueva Guinea|D|IT|||
Solomon Is.|Islas Salomón|D|IE|||Pacto de seguridad con China de 2022.
Fiji|Fiyi|D|IT|||
Vanuatu|Vanuatu|D|S|||
Samoa|Samoa|D|S|||
Tonga|Tonga|D|S|||
Kiribati|Kiribati|D|IE|||
Nauru|Nauru|D|IT|||
Morocco|Marruecos|D|IT|||Aliado de EE.UU. que logró el reconocimiento de su soberanía sobre el Sahara Occidental.
W. Sahara|Sahara Occidental|D|S|P|t|Territorio disputado entre Marruecos y el Frente Polisario.
Algeria|Argelia|D|S|||Gran proveedor de gas de Europa y comprador de armas rusas.
Tunisia|Túnez|D|S|||
Libya|Libia|D|S|X|t x f|Dividida entre dos gobiernos con apoyos externos.
Sudan|Sudán|D|S|T|t x|Guerra entre el ejército y las Fuerzas de Apoyo Rápido.
S. Sudan|Sudán del Sur|D|S|X|t|
Ethiopia|Etiopía|D|S|P|t|Conflictos en Amhara y tensión en Tigray.
Eritrea|Eritrea|D|IE|||
Djibouti|Yibuti|D|P|||Bases de EE.UU., Francia, China, Japón e Italia.
Somalia|Somalia|D|S|X|t x|Al Shabaab controla zonas rurales.
Somaliland|Somalilandia|D|IT|||No reconocida internacionalmente.
Kenya|Kenia|D|IT|||Socio de seguridad de EE.UU. en África oriental; encabezó la misión internacional en Haití.
Uganda|Uganda|D|S|||
Rwanda|Ruanda|D|IT|||Ejército eficaz; la ONU documentó su apoyo al M23 en el este del Congo.
Burundi|Burundi|D|S|||
Tanzania|Tanzania|D|S|||
Dem. Rep. Congo|República Democrática del Congo|D|S|X|t x|El este, en manos de grupos armados y del M23.
Congo|Congo|D|S|||
Central African Rep.|República Centroafricana|D|IE|X|t x|Seguridad del gobierno a cargo de fuerzas rusas.
Cameroon|Camerún|D|S|P|t|
Chad|Chad|D|S|P|f|
Niger|Níger|D|IE|X|t f|Junta aliada con Rusia; avance yihadista.
Mali|Malí|D|IE|X|t|Junta apoyada por Africa Corps; el norte y el centro en manos de grupos armados.
Burkina Faso|Burkina Faso|D|IE|X|t|Junta apoyada por Rusia; gran parte del territorio fuera de control.
Nigeria|Nigeria|D|S|P|t c|Insurgencia en el noreste y bandidaje en el noroeste.
Benin|Benín|D|S|P|t|
Togo|Togo|D|S|P|t|
Ghana|Ghana|D|S|||
Côte d'Ivoire|Costa de Marfil|D|IT|||
Liberia|Liberia|D|IT|||
Sierra Leone|Sierra Leona|D|S|||
Guinea|Guinea|D|S|||
Guinea-Bissau|Guinea-Bisáu|D|S|P|c|Escala del narcotráfico hacia Europa.
Senegal|Senegal|D|S|||
Gambia|Gambia|D|S|||
Mauritania|Mauritania|D|S|||
Cabo Verde|Cabo Verde|D|IT|||
Gabon|Gabón|D|S|||
Eq. Guinea|Guinea Ecuatorial|D|S|||
São Tomé and Principe|Santo Tomé y Príncipe|D|S|||
Angola|Angola|D|S|||
Zambia|Zambia|D|S|||
Zimbabwe|Zimbabue|D|IE|||
Malawi|Malaui|D|S|||
Mozambique|Mozambique|D|S|P|t|Insurgencia en Cabo Delgado.
Madagascar|Madagascar|D|S|||
Namibia|Namibia|D|S|||
Botswana|Botsuana|D|S|||
South Africa|Sudáfrica|D|S|||Miembro de los BRICS con política no alineada.
Lesotho|Lesoto|D|S|||
eSwatini|Esuatini|D|IT|||
Mauritius|Mauricio|D|S|||
Comoros|Comoras|D|S|||
Seychelles|Seychelles|D|S|||
Antigua and Barb.|Antigua y Barbuda|D|S|||
Barbados|Barbados|D|S|||
Dominica|Dominica|D|S|||
Grenada|Granada|D|S|||
St. Kitts and Nevis|San Cristóbal y Nieves|D|S|||
Saint Lucia|Santa Lucía|D|S|||
St. Vin. and Gren.|San Vicente y las Granadinas|D|S|||
"""
PAISES = []
for ln in RAW.strip().splitlines():
    m, es, b, p, z, a, n = ln.split("|")
    if es == "—": continue
    PAISES.append((m, es, b, p, z, a.split(), n))
