# Datos para la web de informes de Plexum (archivo datos-informe.json en la raíz del sitio).
# Especificación: «Datos que cada web publica», versión 1.3 (25/11/2026), apartado 11:
# novedades de cambios de gobierno y de acuerdos comerciales o de inversión que involucren
# a la Argentina o a sus principales socios (Brasil, EE.UU., China y la Unión Europea, según
# la ficha de exposición de la Argentina), más la agenda de los próximos 60 días.
# Solo se publica lo que el sitio ya muestra: cada registro apunta a un hito del sitio («ref»),
# y el generador comprueba que exista. Fecha completa (AAAA-MM-DD) obligatoria.
# El generador deja solo las novedades de los últimos 90 días y la agenda de los próximos 60.
# Se revisa en cada actualización trimestral.
#
# ref: ("a", id de actor, fecha del hito) o ("f", número de punto de fricción, fecha del hito).
# Valores de eje, tipo, alcance.nivel, rubros y exposicion: listas cerradas de la especificación.

WEB = "Mapa del Poder Global"
VERSION = "1.3"
SITIO = "https://francomartinlopez.github.io/podermundial/"

NOVEDADES = [
 dict(id="2026-11-18-apec-tregua-eeuu-china", ref=("f", 1, "2026-11-18"),
      titulo="Trump y Xi se reúnen en la cumbre de la APEC; la tregua comercial vence el 10 de enero",
      resumen="En la cumbre de la APEC en Shenzhen se reunieron los presidentes de EE.UU. y China, dos de los cuatro grandes socios comerciales de la Argentina. La tregua comercial entre ambos países vence el 10 de enero de 2027.",
      tipo="medida comercial", alcance=dict(nivel="mundo", provincia="", localidad="", pais=""),
      rubros=[], subrubros=[], exposicion=["Exporta", "Importa insumos"]),
 dict(id="2026-11-03-eeuu-elecciones-medio-termino", ref=("a", "congreso_eeuu", "2026-11-03"),
      titulo="EE.UU. renueva la Cámara de Representantes y un tercio del Senado",
      resumen="Elecciones de medio término en Estados Unidos, segundo destino de las exportaciones argentinas: se renovaron la Cámara de Representantes y un tercio del Senado.",
      tipo="elección", alcance=dict(nivel="país", provincia="", localidad="", pais="Estados Unidos"),
      rubros=[], subrubros=[], exposicion=[]),
 dict(id="2026-10-29-bce-renuncia-lagarde", ref=("a", "bce", "2026-10-29"),
      titulo="Christine Lagarde anuncia que dejará antes de tiempo la presidencia del Banco Central Europeo",
      resumen="La presidenta del Banco Central Europeo anunció su renuncia anticipada. El banco fija la política monetaria de la zona del euro; la Unión Europea es el cuarto destino de las exportaciones argentinas y el tercer origen de sus importaciones.",
      tipo="otro", alcance=dict(nivel="país", provincia="", localidad="", pais="Unión Europea"),
      rubros=[], subrubros=[], exposicion=[]),
 dict(id="2026-10-25-brasil-reeleccion-lula", ref=("a", "lula", "2026-10-25"),
      titulo="Lula es reelecto presidente de Brasil",
      resumen="Luiz Inácio Lula da Silva ganó el balotaje y seguirá al frente del gobierno de Brasil, primer destino de las exportaciones argentinas y segundo origen de sus importaciones.",
      tipo="elección", alcance=dict(nivel="país", provincia="", localidad="", pais="Brasil"),
      rubros=[], subrubros=[], exposicion=[]),
]

AGENDA = [
 dict(fecha="2026-11-29", ref=("a", "sanchez", "2026-10-05"),
      evento="Elecciones generales en España (Unión Europea)",
      alcance=dict(nivel="país", provincia="", localidad="", pais="España"), rubros=[]),
 dict(fecha="2027-01-10", ref=("f", 1, "2026-11-18"),
      evento="Vence la tregua comercial entre EE.UU. y China",
      alcance=dict(nivel="mundo", provincia="", localidad="", pais=""), rubros=[]),
]

# Indicadores: el apartado 11 no pide cifras.
INDICADORES = []
