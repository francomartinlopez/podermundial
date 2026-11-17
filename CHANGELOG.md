# Cambios

## 2026-11-17 (d)

- El menú de arriba queda fijo y ya no se esconde al bajar.

- Fichas de país: se suman «Qué está en juego», una cronología y los datos clave (territorio, demografía, gobierno, recursos y economía) de los 240 países y territorios. Textos en `fuente/paises_juego.py`; cifras del CIA World Factbook en `fuente/paises_datos.py`, generadas con `scripts/importar_factbook.py`; salida en `data/paisfichas.js`.

- Marco: la democracia republicana constitucional se describe como economía de libre mercado con regulación, intervención, servicios y asistencia estatal en distintos grados según la ideología, entre polos de izquierda y derecha acotados; en autocracias y criptocracias los polos pueden ser más extremos, reales o de fachada. En la criptocracia, el extremismo llega también por el voto, empujado por los problemas que el sistema abandona o genera, y el resultado electoral le resulta barato al sistema porque no cambia el eje del poder; en la autocracia, la coerción facilita imponer extremos.
- Ficha de cada país (`#p-<país>`): mapa, dónde está parado en el orden de imperios, quién define, quién manda desde afuera y sobre quién manda, actores con sede, gráfico de relaciones con los actores de afuera, lista de relaciones y puntos de fricción. Se abre con el botón «Abrir la ficha del país» al tocar un país en cualquier mapa y desde el nombre en la tabla de Países. La lista de Actores acepta un país preseleccionado (`#actores:<país>`).
- Menú de arriba: queda fijo, se esconde al bajar y reaparece apenas se sube un poco (antes solo volvía al llegar arriba de todo).
- Relaciones duplicadas: 9 pares que figuraban dos veces (por ejemplo, Pentágono y hutíes) quedan en una sola relación; el generador ya no admite pares repetidos.
- Quién manda: la leyenda explica cada tipo de línea (dependencia, alianza, enfrentamiento, ambigua, puerta giratoria o acceso a datos).
- Marco teórico: síntesis de las seis piezas del marco; Schumpeter suma su teoría de las clases y de las élites; nueva entrada con la hipótesis de la herencia generacional (ciclos de unos ochenta años que cierran a las élites en una casta de herederos).
- Los últimos 10 actores sin vínculo reciben una relación; cuando el hecho no está probado (Sun Yee On, UnitedHealth, Samherji) se aclara en la propia relación. La ficha de los Rothschild suma Suez (1875), el precio del oro de Londres (hasta 2004), el paso de Macron por el banco y la asesoría a Ucrania en su deuda. Ningún actor queda aislado.
- 140 relaciones nuevas (`fuente/relaciones_extra.py`) para actores que no tenían ninguna: partidos y gobiernos con su bloque, la UE, la OTAN, el FMI o su potencia protectora; empresas con sus rivales, socios y reguladores; organizaciones e iglesias. Quedan 10 actores sin vínculo documentado con otros del mapa.
- El Estado Islámico, la Hermandad Musulmana y Bilderberg, sin sede fija, aparecen en el mapa en su lugar de origen o de reunión, sin país asignado.
- 13 relaciones documentadas para actores que no tenían ninguna (Goldman Sachs, Glencore, Vitol, Trafigura, Pfizer, BAE, BPI, Eli Lilly, Novo Nordisk, S&P, Moody's, SAP, State Street).
- 22 actores no estatales nuevos (600 en total, `fuente/nucleo4.py`) en países que tenían uno solo, priorizados por peso real: Vingroup (Vietnam), Ayala e Iglesia ni Cristo (Filipinas), MOL (Hungría), EPH (Chequia), Nokia (Finlandia), BRAC (Bangladés), Iglesia Ortodoxa Etíope, Asociación de Bancos del Líbano, Fuerzas Democráticas Sirias, UNRWA (Palestina), Consejo de Transición del Sur (Yemen), CK Hutchison (Hong Kong), ArcelorMittal (Luxemburgo), Raiffeisen (Austria), CENCO (Congo), NIS (Serbia), Ryanair (Irlanda), Radio Maryja (Polonia), EDP (Portugal), UGTT (Túnez) y John Fredriksen (Chipre). 24 relaciones nuevas.

## 2026-11-17 (c)
- Puntos de fricción: pasan de 7 a 9. Latinoamérica se divide en «México, Centroamérica y el Caribe» y «Sudamérica»; se suma «África central y austral» (este del Congo, minerales críticos y corredor de Lobito, Mozambique, Sudáfrica frente a EE.UU.), y el punto del norte queda como «Norte de África, Sahel y Cuerno de África». 11 relaciones nuevas.
- Buscador por nombre en Actores y en Países.
- Poder oculto de 0 a 100: puntaje de poder (ya estirado) por la brecha entre poder real y formal, con el mayor llevado a 100.
- Las listas de actores muestran el país donde cada uno tiene su base (también en Quién manda, en los paneles del mapa y en los puntos de fricción), y la página Actores suma un filtro por país.
- Inicio: las cinco tarjetas de secciones van en una sola fila en escritorio.
- Página nueva «Imperios» (`#imperios`): mapa de imperios y explicación de cada nivel (centro, aliado con autonomía, integrado, protectorado, colonia de hecho, independientes y terreno disputado) con la lista de países de cada uno. La capa «Posición» del mapa pasa a llamarse «Imperios».
- Leyenda del mapa de imperios corregida: faltaban los países pendulares (el tono ámbar apagado) y los inclinados a cada bloque.
- Marco teórico: se suma Ray Dalio (ciclo de los imperios: deuda, orden interno y orden externo) y se amplía la escuela de la elección pública en tres entradas: la política sin romanticismo (Buchanan, Tullock, Downs), la burocracia que trabaja para sí misma (Niskanen, Tullock) y el lobby, la búsqueda de rentas y la captura regulatoria (Tullock, Krueger, Olson, Stigler).

## 2026-11-17 (b)
- Nueva sección «Puntos de fricción» (`#friccion`, ficha de cada uno en `#f-1` a `#f-7`, datos en `fuente/friccion.py`): mapa de la región, qué está en juego, gráfico de los actores que intervienen con sus alianzas y enfrentamientos, qué hace cada uno, cronología y fuentes. Al tocar un punto en el mapa se puede abrir su ficha.
- El punto 3 pasa a ser «Latinoamérica» (carteles, canal de Panamá, Chancay e inversiones chinas, gobiernos enfrentados con EE.UU., frontera con México y el Caribe); el 4 suma el Sahel y los conflictos africanos (Sudán, este del Congo, Cuerno de África, Sahara Occidental); el 6 pasa a «Medio Oriente», de Ormuz y Yemen hasta Afganistán. 26 relaciones nuevas entre actores.
- «Organizaciones» pasa a llamarse «Actores» en todo el sitio (las organizaciones son un subgrupo de los actores); la ruta nueva es `#actores` y `#organizaciones` sigue funcionando. El filtro «Área» pasa a «Categoría», con enlace a la tabla de tipos y categorías del Marco.
- 57 actores nuevos (578 en total, `fuente/nucleo3.py`): todos los países soberanos tienen al menos un actor propio; estudios offshore de Caimán, Bermudas, Islas Vírgenes Británicas y Jersey; más cobertura en Sudamérica, India, Sahara y Libia, Afganistán y Pakistán, Sudeste Asiático, Kazajistán y Mongolia.
- Territorios dependientes con nombre en español y país del que dependen.
- Se quitó la sección «Cambios recientes» del Marco.
- Quién manda: el gráfico ocupa todo el ancho, la leyenda va debajo y el tamaño de cada actor es proporcional (en área) a su puntaje de poder.
- Mapa: al cambiar de capa se limpia la selección; en la capa de actores, tocar un país lista sus actores y un toque cerca de un punto elige ese actor.

## 2026-11-17 · Leyendas de los mapas

- Capa «Organizaciones»: la leyenda muestra qué significa cada color (bloque), cada forma (tipo de actor) y cada tamaño, con círculos de referencia para 100, 50 y 10 puntos.
- El tamaño de cada actor en el mapa ahora es proporcional a su puntaje de poder (antes usaba el poder efectivo, con poca diferencia visible entre actores).
- Al tocar un país o un actor, la leyenda sigue disponible debajo del panel («Cómo leer el mapa»).
- Capa «Posición»: la leyenda explica la intensidad del color.

## 2026-11-17 · El Marco, fiel a Cryptocracy

- «La tesis», «Sistemas de gobierno» y «Marco teórico» reescritos a partir del texto del libro: la tesis sobre la naturaleza humana, la criptocracia como etapa más baja de las democracias republicanas constitucionales (Estado visible y Estado operativo), la tipología de autocracias (tecnocracia de resultados, régimen nacionalista e imperial, híbrido teocrático y regímenes residuales), Kennedy como punto de inflexión según el libro y la anatomía de la decadencia.
- Marco teórico ordenado como la bibliografía del libro: geopolítica y realismo (Mearsheimer, realismo clásico, Huntington, Kilcullen); civilización, frontera y decadencia (Quigley, Turner, Schumpeter, Veblen, Mises y Hayek, Dalio); poder, élites y democracia (Burnham, Mosca, Pareto, Michels, Dahl, la escuela de la elección pública, Hoppe, Popper); naturaleza humana (el libro y Robert Greene).

## 2026-11-17 · Marco teórico ampliado y colonias de hecho

- Marco: nueva sección «La tesis», con el resumen del enfoque de *Cryptocracy* y el asesinato de Kennedy como punto de inflexión; «Sistemas de gobierno» (autocracia, criptocracia y democracia republicana constitucional, y por qué ninguna democracia actual cumple el modelo); «El orden mundial» (centros, aliados, integrados, protectorados, colonias de hecho, pendulares y zonas liberadas); y un marco teórico ampliado: Mearsheimer, el realismo clásico, la teoría de las élites, Dahl, Quigley y las fases de las civilizaciones, la teoría de la frontera de Turner y Robert Greene.
- Nueva posición de país, **colonia de hecho**: Micronesia, Islas Marshall y Palaos (EE.UU.) y Chipre del Norte (Turquía). En el mapa se ve con una trama de puntos.
- Notas nuevas para 32 países importantes (Alemania, Japón, Corea del Sur, Canadá, Irán, Egipto, Indonesia, entre otros) y textos de introducción ampliados en Países, Organizaciones y Quién manda.

## 2026-11-17 · Revisión actor por actor

- Revisados los 521 actores en cohesión interna, apoyo popular, privilegio legal y alcance efectivo. Cambios en `fuente/revision.py`:
  - Cohesión: suben las Fuerzas de Defensa de Finlandia, Nvidia y Palantir; bajan la ODNI (purgas internas) y Hezbolá (debilitada tras la guerra); Tisza pasa a 2.
  - Apoyo popular: suben el Mossad, la Unidad 8200, la inteligencia militar ucraniana, TSMC y la Casa Grimaldi; bajan el CCM de Tanzania, el ejército tailandés, el de Guinea-Bisáu, Sueño Georgiano, el PML-N, el Grupo Adani y las redes criminales sin base social (Prince Group, Sun Yee On, Tren de Aragua, Los Lobos, Yamaguchi-gumi, Viv Ansanm).
  - Privilegio: Alphabet sube a 1 (inmunidad de plataformas en EE.UU.), el Ministerio de Comercio de China a 2 (controles de exportación) y Telegram baja a 0.
  - Alcance: pasan a global Exor, los Wallenberg, los Quandt, los Rothschild, la Fundación Novo Nordisk y el Banco Central Europeo; pasan a nacional las fuerzas armadas de Corea del Sur y de Japón, la NIS, la Casa de Al Sabah, SMIC, Los Lobos, Itaú, Sberbank y el M23.

## 2026-11-17 · Método explicado en el sitio

- Marco: explica los ejes de cohesión interna, apoyo popular y privilegio legal, la corrupción dentro de «acción fuera de la ley», cómo se asigna el alcance efectivo, la división de partidos y suma una lista de cambios recientes.
- Cada ficha muestra cómo se calcula su puntaje: los cinco componentes, su peso y su valor.
- Nueva imagen para compartir con la cifra actual: 521 actores y 21 ejes.

## 2026-11-17 · Escala estirada

- El puntaje de poder se eleva al cubo antes de llevar el mayor a 100. El orden no cambia, pero las distancias se acercan a las reales: el último actor pasa de 35 a unos 5 puntos y la mediana de 57 a 19.

## 2026-11-17 · Fórmula sin categoría real

- El puntaje de categoría real deja de entrar en el puntaje de poder: se calculaba con la autonomía y las relaciones, que ya están en la fórmula. Se sigue publicando como dato informativo.
- Pesos nuevos: categoría teórica 40 %, capacidad 30 %, alcance efectivo 20 %, autonomía real 5 % y red de dependientes 5 %.

## 2026-11-17 · Alcance efectivo

- Nuevo componente del puntaje de poder: **alcance efectivo**, dónde puede actuar de verdad cada actor, más allá de lo que la ley le permita. Global (0,60), regional o en un grupo de países (0,25) o nacional (0,15), asignado actor por actor: 189 globales, 146 regionales y 186 nacionales (`fuente/alcance.py`).
- Nuevos pesos del puntaje: categoría teórica 40 %, categoría real 10 %, capacidad 20 %, alcance 20 %, autonomía real 5 % y red de dependientes 5 %.
- Suben las agencias de inteligencia y los ejércitos con alcance mundial: CIA 3.ª, MSS 4.ª, Mossad y NSA 6.ª y 7.ª, Fuerzas Armadas de Rusia 8.ª.
- Las fichas muestran el alcance y la lista de organizaciones se puede filtrar por alcance.

## 2026-11-17 · Eje 21, privilegio legal

- Nuevo eje **privilegio legal** (familia Norma, peso 1,5): lo que la ley le permite a un actor y no a otros — actuar sin supervisión, inmunidad, vetos o indultos, monopolio legal de un mercado o hacer legalmente lo que para otros sería delito. El 3 queda para privilegios con efecto mundial: la Casa Blanca, el Pentágono, la CIA, la NSA, la Reserva Federal, el Consejo de Seguridad de la ONU, el PCCh, el Partido del Trabajo de Corea, la Casa de Saud y el líder supremo de Irán. La capacidad pasa a ir de 0 a 63.
- El puntaje teórico de «Organismo de gobierno» sube de 4 a 6: el Departamento de Energía, el Congreso de EE.UU. y los departamentos del PCCh quedaban subvaluados.

## 2026-11-17 · Inteligencia que faltaba, el FBI y más actores de las potencias (521 actores)

- Inteligencia y seguridad: Organización de Inteligencia de la Guardia Revolucionaria, Oficina de Inteligencia del Estado Mayor Conjunto del EPL, Policía Armada Popular, Departamentos de Organización y de Propaganda del PCCh, SBU de Ucrania, Presidencia General de Inteligencia saudí, BfV alemana y Policía Federal de Brasil.
- El FBI pasa a ser actor propio, dependiente del Departamento de Justicia.
- Otros actores: Sedena (fuerzas armadas de México), Lashkar-e-Taiba, Khatam al-Anbiya; L3Harris, Huntington Ingalls, Booz Allen Hamilton, Leidos, KKR, Apollo, Chevron, Eli Lilly, UnitedHealth, Disney, Comcast, Federalist Society, Teamsters; Nornickel, Lukoil, Novatek; CNNC, Bank of China, China Rare Earth Group; Lloyd's, Barclays, The Economist Group, Wellcome Trust; AXA, Naval Group, Orano; SAP, BASF, Grupo Schwarz, Bertelsmann; Sony, Mitsui; DRDO; PL y la familia Bolsonaro, Itaú, BTG Pactual; Koç Holding y PML-N. 47 relaciones nuevas. Fuente: `fuente/nucleo2.py`.

## 2026-11-17 · Ejes 19 y 20 y corrupción dentro de «acción fuera de la ley»

- Eje 19, **cohesión interna**: unidad de mando frente a facciones, pujas internas o disputas de sucesión (3 = mando único sin pujas; 0 = partido en facciones enfrentadas, como el Cártel de Sinaloa o el Partido Demócrata de EE.UU.).
- Eje 20, **apoyo popular**: respaldo o legitimidad pública, en votos, aprobación, fieles o usuarios.
- Ambos pesan 1; la capacidad pasa a ir de 0 a 60. Puntaje editorial por categoría con excepciones actor por actor (`fuente/ejes_nuevos.py`).
- «Acción fuera de la ley» incluye ahora la corrupción —sobornos, tráfico de influencias, desvío de fondos, robo, fraude o violación de sanciones—, con anclas por gravedad y alcance. 16 casos nuevos documentados: ANC, FIFA, COI, BAE, Siemens, Samsung, Boeing, Pfizer, Bayer, JPMorgan, Alphabet, Apple, Meta, Lockheed Martin, Walmart (familia Walton) y el EPL.

## 2026-11-17 · Puntaje de poder de 0 a 100 y potencias completas (470 actores)

- Nuevo **puntaje de poder**, de 0 a 100, que ordena todo el sitio: media geométrica ponderada de la categoría teórica (40 %), la categoría real (20 %), la capacidad (25 %), la autonomía real (10 %) y la red de dependientes (5 %). El actor más poderoso vale 100 y el resto, en proporción.
- Cada una de las 33 categorías tiene un puntaje teórico (criterio editorial) y uno real, calculado de los datos del mapa. El Marco lista los 7 tipos y las 33 categorías con su cantidad de actores y ambos puntajes; cada ficha muestra los de su categoría.
- Los partidos se dividen en «partido único o hegemónico» (14) y «partido en sistema competitivo». El Departamento de Trabajo del Frente Unido pasa a organismo de gobierno: es un órgano del PCCh.
- 67 actores nuevos en las potencias, con ficha y fuentes: Departamento de Energía de EE.UU. (con la NNSA), Congreso, ODNI, NRO, DIA, SOCOM, Northrop Grumman, Blackstone, Koch, Cámara de Comercio; SVR, Rosatom, Sberbank, Banco Central de Rusia, VTB, Kadýrov, Kovalchuk, Rotenberg, Timchenko; Comisión Militar Central, CASC, AVIC, CETC, CNPC, Banco de Desarrollo, SASAC, Ministerio de Comercio de China; MI5, HSBC, BP, Rio Tinto; DGSI, Thales, Safran, BNP Paribas, EDF; Volkswagen, Deutsche Bank, Allianz, familia Quandt; Mitsubishi, MUFG, GPIF; RAW, IB, Tata, Banco de la Reserva, Corte Suprema de la India, Gautam Adani; Fuerzas Armadas, Congreso, Banco Central, Vale y JBS de Brasil; Fuerza Quds, MOIS, Setad, Astan Quds Razavi, Basij; Oficina General de Reconocimiento y Oficina 39 de Corea del Norte; Unidad 8200, Rafael, IAI y NSO Group; AKP y Fuerzas Armadas de Turquía. 91 relaciones nuevas. Fuente: `fuente/nucleo.py`.
- Monarcas: solo figuran los que tienen poder real; lo aclaran el Marco y la ficha de cada uno.

## 2026-11-16 · Poder real antes que jerarquía formal

- Pesos fijos nuevos: coerción violenta, adquisición de información y el nuevo eje «Acción fuera de la ley» valen doble; contactos, una vez y media. La capacidad va de 0 a 54.
- Eje 18, «Acción fuera de la ley»: operaciones encubiertas, asesinatos, sabotaje, chantaje, soborno sistemático o crimen. Puntuado en 88 actores, cada uno con un hecho documentado y su fuente.
- Autonomía real: quien tiene armas, secretos y contactos conserva poder propio aunque dependa formalmente de otro, y su jefe formal hereda menos de él.
- El Mossad pasa a «decide solo» y deja de figurar como dependiente de Netanyahu: por ley le responde, pero en los hechos fija su propia agenda.
- Las personas se dividen en dos categorías: empresarios (7) y líderes políticos (35).
- Revisión de casos: Shin Bet, MSS, ISI, SpaceX, Meta, X, Reliance y LVMH pasan de subordinados a aliados con criterio propio.

## 2026-11-16 · Un actor que define en cada país (403 actores)

- 110 actores nuevos, con ficha y fuentes, para los 136 países que no tenían ninguno: partidos de gobierno, jefes de regímenes personalistas, monarquías, juntas militares, gremios empresarios, empresas, servicios de inteligencia y organismos como la Autoridad del Canal de Panamá o la Junta de Supervisión Fiscal de Puerto Rico.
- Donde el que define es un actor extranjero ya presente en el mapa (Kosovo y la OTAN, Micronesia y el Pentágono, Hong Kong y el PCCh, Guyana y ExxonMobil, entre otros), el país apunta a ese actor con una nota.
- El panel de cada país muestra ahora «Quién define aquí».
- El país de cada actor se toma de su sede y no solo de las coordenadas, lo que corrige capitales costeras e islas.
- 22 relaciones nuevas. Fuente: `fuente/locales.py`.
- Nueva imagen para compartir con la cifra actualizada.

## 2026-11-16 · Navegación y lectura

- Portada: título más chico y sin desplazamiento suave, para que la página no quede trabada a mitad de camino al volver arriba.
- Mapas: al tocar un país, un actor o un punto de fricción el mapa se acerca; botones para acercar, alejar y volver a la vista completa.
- Gris del terreno disputado un poco más claro.
- Nota bajo los rankings de la portada que explica qué miden los puntos.
- Puntos de fricción con explicación propia; el 2 pasa a llamarse «Islas del Pacífico Sur» y se suma el 7, mar de China Meridional y estrecho de Malaca.
- Países: filtro por posición (centro, pendular, protectorado, etc.); el filtro de bloque ya no ofrece bloques que no tienen países.
- Quién manda: buscador de actores, filtros por cantidad, bloque y tipo, nombres visibles y una vista de lista por nivel.
- Marco: textos a todo el ancho.

## 2026-11-16 · Nueva imagen para compartir

- Imagen de vista previa rediseñada: mapa mundial con la red de actores y el título a la izquierda (`img/og-mapa.png`). Nombre de archivo nuevo para que WhatsApp y X no sigan mostrando la anterior.

## 2026-11-16 · Relaciones, India y hoja de puntuación

- Fuerzas Armadas de la India (293 actores) y 33 relaciones nuevas de propiedad, financiamiento y abastecimiento (296 en total).
- Recalibración de personas y gobiernos que acumulaban poder propio y de red: Netanyahu, Erdoğan, Prabowo, Lula, Kagame, Palacio Real de Marruecos y Partido Comunista de Vietnam.
- Hoja de puntuación sincronizada con el sitio; las columnas de justificación y fuentes se completan desde las fichas.

## 2026-11-16 · Del Estado formal al poder real (292 actores)

- Se quitan 31 gobiernos de países que no son centros del orden mundial. Quedan la Casa Blanca, el Kremlin, el PCCh y el Consejo de Estado, la India, Irán, la Comisión Europea y el Palacio Real de Marruecos.
- Se suman 73 actores con poder real: 16 personas (Musk, Thiel, los Ellison, Bezos, Zuckerberg, Ambani, Arnault, Milei, Erdoğan, Netanyahu, Lula, Prabowo, Zelenski, al-Sharaa, Delcy Rodríguez, Kagame), 5 sindicatos, 5 organismos internos (Tesoro de EE.UU. y OFAC, controles de exportación, Comisión de Disciplina del PCCh, Consejo de Seguridad de Rusia, City de Londres), 4 servicios de inteligencia, 9 partidos, 21 empresas y grupos familiares, 12 fuerzas armadas y la Hawza de Nayaf.
- Nuevo tipo «Persona», con forma de estrella en los gráficos.
- Las relaciones y dependencias de los gobiernos quitados pasan a sus sucesores reales (por ejemplo, las FDI y el Mossad dependen de Netanyahu; SpaceX y X, de Musk).

## 2026-11-16 · Ampliación a 250 organizaciones

- 50 organizaciones nuevas para cubrir América Latina, África, Europa del Sur y del Este, el Sudeste Asiático, Oceanía y Canadá: gobiernos (Argentina, Colombia, Venezuela, Chile, Ecuador, Nigeria, Sudáfrica, Etiopía, Kenia, Ruanda, Marruecos, Italia, España, Polonia, Hungría, Indonesia, Filipinas, Corea del Sur, Australia, Bangladés, Siria, Irak, Canadá), partidos (Cuba, Vietnam), ejércitos (Sudán, Tailandia, Myanmar), empresas (PDVSA, Codelco, OCP, Sonatrach, Dangote, Shell, TotalEnergies, LVMH, Rheinmetall, BHP, Reliance, Adani, Kazatomprom, Temasek, Petronas) y grupos armados (ELN, Clan del Golfo, Los Lobos, M23, Ejército Nacional Libio, Al Shabaab, Alianza de Estados del Sahel).
- 68 relaciones nuevas. Todas las organizaciones nuevas tienen ficha.
- Países: Hungría pasa a integrado al bloque transoceánico tras la victoria de Magyar; notas de Siria y Colombia actualizadas.

## 2026-11-16 · Tanda 5 de fichas: las 200 completas

- Fichas para las posiciones 161 a 200 (Hamás, Hermandad Musulmana, CPI, Consejo de Seguridad, STF, SWIFT, Euroclear, BRICS, OPEP+ y otras 31). Todas las organizaciones tienen ficha.
- Novedades verificadas: Drapatyi reemplaza a Syrskyi en Ucrania (21 de julio); destitución del fiscal de la CPI Karim Khan (24 de julio) y sanciones de EE.UU. a la presidenta de la Corte; acuerdo de desarme de Hamás (julio); designación de tres ramas de la Hermandad Musulmana (13 de enero); prisión domiciliaria humanitaria de Bolsonaro.

## 2026-11-16 · Tanda 4 de fichas

- Fichas para las posiciones 121 a 160 (FMI, Banco Mundial, Corte Suprema de EE.UU., partidos Demócrata y Republicano, MI6, GCHQ, ASML, COSCO, PIF y otras 30).
- Novedades verificadas: la Corte Suprema anuló los aranceles IEEPA (20 de febrero) y falló Trump contra Slaughter (29 de junio); conteo de AP de las legislativas del 3 de noviembre al 16 de noviembre; copresidencia interina de Fink y Hoffmann en el WEF; venta de los puertos de CK Hutchison trabada.

## 2026-11-16 · Tanda 3 de fichas

- Fichas para las posiciones 81 a 120 (BCE, OTAN, Mossad, Hezbolá, hutíes, Tren de Aragua, FAR de Sudán, Japón, DHS, Departamento de Justicia y otras 30).
- Novedades verificadas: Lagarde dejará el BCE el 7 de febrero de 2027; Roman Gofman dirige el Mossad desde el 2 de junio; Hezbolá en guerra con Israel desde el 2 de marzo; ataques hutíes a petroleros saudíes en julio; muerte de 'Niño Guerrero' el 12 de junio; Matt Brittin dirige la BBC; Markwayne Mullin en Seguridad Nacional y Todd Blanche como fiscal general; Takaichi reelecta en febrero.

## 2026-11-16 · Tanda 2 de fichas

- Fichas para las posiciones 41 a 80 (FSB, Lockheed, OpenAI, PCC, TSMC, Fed, NSA, CJNG, ByteDance y otras 31).
- Novedades verificadas: Kevin Warsh preside la Fed desde el 22 de mayo; Joshua Rudd dirige la NSA desde el 10 de marzo; EE.UU. señala a 'El 03' como jefe del CJNG; PCC y Comando Vermelho designados terroristas por EE.UU. el 28 de mayo; Chen Zhi (Prince Group) extraditado a China; TikTok USDS en EE.UU.; Nitin Nabin preside el BJP; Greg Abel y John Furner al frente de Berkshire y Walmart.

## 2026-11-16 · Tanda 1 de fichas
- Fichas completas (resumen, quién manda, dinero, cronología y fuentes) para las 40 organizaciones de mayor poder en red.
- Irán: la Guardia Revolucionaria pasa a autonomía 1 y la Oficina del Líder Supremo a subordinada, según reportes de Reuters sobre el reparto de poder tras la muerte de Ali Jamenei.
- Nuevas relaciones por la guerra de 2026 con Irán, la mediación de Pakistán y la alianza del CJNG con Los Chapitos.

## 2026-11-16 · Primera versión
- 200 organizaciones con puntajes en 17 ejes, autonomía, poder formal y fase de Quigley.
- 146 relaciones con intensidad y 203 países y territorios clasificados.
- Mapa mundial por capas, gráfico Quién manda, índice y fichas con perfil de poder.
- Las fichas todavía no tienen resumen, cronología ni fuentes: se cargan por tandas.
