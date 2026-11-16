# El mapa del poder global (podermundial)

Sitio estático publicado con GitHub Pages desde `main` (raíz). Todo en español rioplatense neutro, con fechas ISO en los datos.
Responsable editorial: Franco Martín López. Proyecto hermano de Monitor de Espionaje (`monitorespionaje`), con base técnica similar.

## Reglas
- La fuente de los datos es `fuente/*.py` (copia de la hoja de puntuación). Nunca editar `data/*.js` a mano: correr `python3 scripts/generar_datos.py` y luego `node scripts/validate.js`.
- Escala de 0 a 3 por eje, con anclas en `fuente/datos.py` (ANCLAS). El 3 solo para dominio a escala mundial.
- Pesos fijos e iguales: el sitio no ofrece controles para cambiarlos.
- El sitio no enlaza al libro Cryptocracy.
- Resguardos: fuente obligatoria para calificar a una organización de fachada o protectorado o vincularla con delitos o grupos armados; nada especulativo sobre personas vivas.
- Estética: fondo negro, rojo de marca #E10600 para rellenos y #FF3B30 para texto; euroasiático #9E1B32. Tipografías: Big Shoulders Display, Archivo, Newsreader, JetBrains Mono. Símbolo: Núcleo (img/logo.svg); versión reducida en img/favicon.svg.
- Actualización trimestral: subir `CORTE` y `PROXIMA` en `scripts/generar_datos.py`, registrar en CHANGELOG y etiquetar el commit.
