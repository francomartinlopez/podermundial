# El mapa del poder global (podermundial)

Sitio estático publicado con GitHub Pages desde `main` (raíz). Todo en español rioplatense neutro, con fechas ISO en los datos.
Responsable editorial: Franco Martín López. Proyecto hermano de Monitor de Espionaje (`monitorespionaje`), con base técnica similar.

## Reglas
- La fuente de los datos es `fuente/*.py` (copia de la hoja de puntuación). Nunca editar `data/*.js` a mano: correr `python3 scripts/generar_datos.py` y luego `node scripts/validate.js`.
- Escala de 0 a 3 por eje (21 ejes), con anclas en `fuente/datos.py` (ANCLAS); los ejes 19 a 21 (cohesión interna, apoyo popular y privilegio legal) en `fuente/ejes_nuevos.py`. El 3 solo para dominio a escala mundial.
- Puntaje de poder (0 a 100, el mayor vale 100): media geométrica ponderada definida en `fuente/categorias.py` (categoría teórica 40 %, categoría real 20 %, capacidad 25 %, autonomía real 10 %, red 5 %). El teórico de cada categoría es editorial; el real se calcula de los datos.
- Solo figuran monarcas con poder real (lista en `fuente/categorias.py`).
- Se mide el poder real, no la jerarquía oficial. Pesos fijos en `fuente/poder_duro.py`: coerción, adquisición de información y acción fuera de la ley valen 2; contactos y privilegio legal 1,5; el resto 1. Autonomía real: el poder duro sube el factor de autonomía y reduce lo que hereda el jefe formal. El sitio no ofrece controles para cambiar pesos.
- El eje «acción fuera de la ley» incluye la corrupción (sobornos, tráfico de influencias, desvío de fondos, robo, fraude) y solo se puntúa con un hecho documentado y fuente; en personas vivas, solo lo establecido por un tribunal u organismo oficial.
- El sitio no enlaza al libro Cryptocracy.
- Resguardos: fuente obligatoria para calificar a una organización de fachada o protectorado o vincularla con delitos o grupos armados; nada especulativo sobre personas vivas.
- Estética: fondo negro, rojo de marca #E10600 para rellenos y #FF3B30 para texto; euroasiático #9E1B32. Tipografías: Big Shoulders Display, Archivo, Newsreader, JetBrains Mono. Símbolo: Núcleo (img/logo.svg); versión reducida en img/favicon.svg.
- Actualización trimestral: subir `CORTE` y `PROXIMA` en `scripts/generar_datos.py`, registrar en CHANGELOG y etiquetar el commit.
- La hoja de puntuación se regenera con `python3 scripts/exportar_hoja.py salida.xlsx` y se importa; la columna «Datos que justifican» toma el resumen de cada ficha.
