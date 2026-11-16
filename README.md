# El mapa del poder global

**El mundo real, sin máscaras.** Quién tiene el poder real en el mundo y quién solo lo aparenta: casi 300 organizaciones y personas con nombre propio medidas en 17 ejes, su jerarquía, sus dependencias y cuánto de su poder escapa al control público.

Sitio estático (HTML, CSS y JavaScript, sin dependencias salvo d3-geo y topojson para el mapa). Se publica con GitHub Pages desde la rama `main`.

## Secciones
- **Inicio:** mapa mundial por capas (bloques, posición, zonas liberadas, organizaciones) y los diez primeros por poder en red y por poder oculto.
- **Quién manda:** gráfico jerárquico relacional por autonomía, bloque, tipo y poder.
- **Organizaciones:** índice filtrable y ficha de cada organización.
- **Países:** clasificación de 203 países y territorios.
- **Marco:** teoría, metodología, anclas de la escala y resguardos.

## Datos
- `fuente/datos.py`, `fuente/paises.py`, `fuente/coords.py`: fuente editorial, copia de la hoja de puntuación.
- `scripts/generar_datos.py`: genera `data/meta.js`, `data/organizaciones.js`, `data/relaciones.js` y `data/paises.js`.
- `scripts/validate.js`: controla ids, puntajes, dependencias, relaciones y el vencimiento del corte.
- `data/world.js`: cartografía de Natural Earth (dominio público). `vendor/`: d3-geo, d3-array y topojson-client (licencia ISC).

## Actualización
El sitio se revisa cada tres meses. Cada corte queda etiquetado en git (por ejemplo `2026-T4`) y registrado en `CHANGELOG.md`.

```
python3 scripts/generar_datos.py
node scripts/validate.js
```
