# Ficha de exposición internacional por país: socios comerciales por bloque, alineamientos,
# sanciones y designaciones, deuda y financiamiento, y organismos internacionales.
# Hoy solo la tiene la Argentina. Los puntos de fricción que tocan al país no se cargan acá:
# el sitio los toma de fuente/friccion.py.
# Se revisa en cada actualización trimestral (fecha en "rev"). Todo dato lleva fuente.
# Socios: participación en exportaciones e importaciones (%); el bloque de cada socio sale del mapa
# (clave del país en el mapa) salvo para la Unión Europea, que se agrupa con el transoceánico.

CEI = "https://www.cancilleria.gob.ar/es/cei/actualidad/intercambio-comercial-argentino-enero-julio-2026"
INDEC_SEP = "https://www.indec.gob.ar/ftp/ica_digital/ica_d_10_263F42E3F39F/"

EXPO = {
 "Argentina": dict(
  rev="2026-11-25",
  socios=dict(
   periodo="enero a julio de 2026",
   filas=[
    # (clave en el mapa o "UE", nombre, % de exportaciones, % de importaciones)
    ("Brazil", "Brasil", 12.7, 21.6),
    ("United States of America", "Estados Unidos", 10.2, 9.4),
    ("China", "China", 9.6, 22.5),
    ("UE", "Unión Europea", 8.9, 13.7),
   ],
   nota="Los cuatro grandes socios suman el 41,4 % de las exportaciones y el 67,2 % de las importaciones. Los mayores superávits fueron con Chile, India, EE.UU., Perú y Vietnam; los mayores déficits, con China, Paraguay y Brasil. De enero a septiembre de 2026 las exportaciones sumaron USD 77.267 millones (+21,6 %) y las importaciones USD 56.069 millones (−2,5 %).",
   fuentes=[("Cancillería, CEI: Intercambio comercial argentino, enero-julio 2026", CEI),
            ("INDEC: Intercambio comercial argentino, septiembre de 2026", INDEC_SEP)]),
  alineamientos=[
   ("2026-02-05", "Firma con EE.UU. el Acuerdo sobre Comercio e Inversiones Recíprocos: EE.UU. elimina los aranceles recíprocos para 1.675 productos argentinos y amplía a 100.000 toneladas la cuota de carne; la Argentina abre su mercado a bienes estadounidenses y se compromete a cooperar en seguridad económica. Protocolo adicional en octubre de 2026.",
    "https://www.cancilleria.gob.ar/es/destacados/argentina-y-estados-unidos-firmaron-un-acuerdo-sobre-comercio-e-inversiones-reciprocos"),
   ("2026-01-17", "Firma del Acuerdo de Asociación y del Acuerdo Comercial Interino entre el Mercosur y la Unión Europea en Asunción; la Argentina lo aprueba por ley 27.800 (26/2/2026) y se aplica de forma provisional desde el 1 de mayo de 2026.",
    "https://www.afip.gob.ar/convenios-internacionales/materia/documentos/Acuerdos-de-cooperacion-y-asistencia-mutua/Multilaterales/Aduaneros/ficha-tecnica/Ficha-tecnica-Mercosur-UE.pdf"),
   ("2026-01-17", "Declara organización terrorista a la Fuerza Quds iraní y a trece personas vinculadas; antes había incluido a Hamás y Hezbolá en el registro RePET.",
    "https://www.argentina.gob.ar/node/490007"),
   ("2026-03-31", "Declara organización terrorista a la Guardia Revolucionaria de Irán y la incorpora al RePET, con referencia a los atentados contra la Embajada de Israel y la AMIA.",
    "https://www.argentina.gob.ar/noticias/comunicado-oficial-numero-142"),
   ("2026-03-17", "Se hace efectiva su salida de la Organización Mundial de la Salud, un año después de notificarla; sigue en la Organización Panamericana de la Salud.",
    "https://www.lanacion.com.ar/politica/la-argentina-formalizo-su-salida-de-la-organizacion-mundial-de-la-salud-nid17032026/"),
   ("2026-08-05", "Renueva por cinco años el swap de monedas con el Banco Popular de China, por unos USD 19.000 millones, mientras profundiza el acuerdo con EE.UU.",
    "https://es-us.finanzas.yahoo.com/noticias/argentina-renueva-a%C3%B1os-swap-us-164951329.html"),
  ],
  sanciones=[
   ("2026-11-11", "Irán designa a la Armada y a la Fuerza Aérea argentinas como «organizaciones terroristas», en reciprocidad por la designación de la Guardia Revolucionaria y bajo una ley iraní de 2019.",
    "https://www.emol.com/noticias/Internacional/2026/11/11/1216723/iran-argentina-terroristas.html"),
   ("2025-03-21", "El Departamento de Estado de EE.UU. designa a la expresidenta Cristina Fernández de Kirchner y al exministro Julio De Vido bajo la sección 7031(c) por corrupción significativa, con base en sus condenas judiciales: no pueden ingresar a EE.UU., igual que sus familiares directos.",
    "https://www.jurist.org/news/2025/03/us-state-department-bans-former-argentine-president-cristina-fernandez-de-kirchner-citing-significant-corruption"),
  ],
  deuda=[
   ("FMI", "Mayor deudor del Fondo: unos 41.789 millones de DEG (USD 57.250 millones) en abril de 2026, alrededor de un tercio de los préstamos vigentes del organismo. El programa de Facilidades Extendidas de abril de 2025 es de USD 20.000 millones; tras la segunda revisión (mayo de 2026) se habían girado unos USD 15.800 millones. La tercera revisión tiene acuerdo técnico desde octubre y pasa al Directorio a principios de diciembre, por unos USD 900 millones.",
    "https://www.lanacion.com.ar/economia/el-fmi-aprobo-la-segunda-revision-del-acuerdo-y-hara-un-desembolso-de-us1000-millones-nid21052026/"),
   ("Deuda pública", "Deuda bruta de la Administración Central: USD 479.273 millones a mayo de 2026, tras el récord de USD 496.676 millones de abril.",
    "https://www.lanacion.com.ar/economia/la-deuda-bruta-cayo-35-en-mayo-y-corto-una-seguidilla-de-seis-meses-en-alza-nid16062026/"),
   ("Con organismos internacionales", "USD 97.095 millones a enero de 2026, de los cuales USD 57.744 millones con el FMI (Secretaría de Finanzas).",
    "https://dolarhoy.com/economia/la-deuda-bruta-nacional-crecio-en-enero-a-usd-460-934-millones-pese-a-fuertes-pagos-de-vencimientos-2026223121023"),
   ("Tesoro de EE.UU.", "Línea de swap de hasta USD 20.000 millones firmada en octubre de 2025; el Banco Central usó unos USD 2.500 millones antes de las elecciones y los devolvió en diciembre de 2025. La línea sigue vigente.",
    "https://www.bloomberglinea.com/latinoamerica/argentina/tesoro-de-estados-unidos-y-banco-central-confirman-que-argentina-devolvio-los-fondos-del-swap/"),
   ("China", "Swap de monedas con el Banco Popular de China renovado en agosto de 2026 por cinco años, por unos USD 19.000 millones.",
    "https://es-us.finanzas.yahoo.com/noticias/argentina-renueva-a%C3%B1os-swap-us-164951329.html"),
   ("Banco Mundial", "Paquete de USD 12.000 millones anunciado en abril de 2025 y garantías por USD 2.000 millones aprobadas en junio de 2026 para refinanciar vencimientos.",
    "https://www.lanacion.com.ar/economia/el-banco-mundial-aprobo-la-garantia-de-us2000-millones-para-que-la-argentina-refinancie-pagos-de-nid17062026/"),
   ("BID", "Hasta USD 10.000 millones entre 2025 y 2028 (7.000 al sector público y 3.000 de BID Invest al privado).",
    "https://www.iadb.org/es/noticias/el-bid-apoyara-argentina-con-us10000-millones"),
  ],
  organismos=dict(
   miembro="ONU, G20, OMC, Mercosur, OEA, FMI, Grupo Banco Mundial, BID, CAF y OPS.",
   cambios=[("2026-03-17", "Sale de la OMS.", "https://www.lanacion.com.ar/politica/la-argentina-formalizo-su-salida-de-la-organizacion-mundial-de-la-salud-nid17032026/")]),
 ),
}
