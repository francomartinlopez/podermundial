# Coordenadas aproximadas de las sedes (longitud, latitud). None = sin sede fija.
C = {
"Abu Dabi, Emiratos Árabes Unidos":(54.37,24.45),"Ankara, Turquía":(32.85,39.93),"Arlington, EE.UU.":(-77.06,38.87),"Baar, Suiza":(8.53,47.2),
"Bagdad, Irak":(44.36,33.31),"Bamako, Malí (operación principal)":(-8.0,12.64),"Basilea, Suiza":(7.59,47.56),"Bastrop, EE.UU.":(-97.32,30.11),
"Beirut, Líbano":(35.5,33.89),"Bentonville, EE.UU.":(-94.21,36.37),"Berlín, Alemania":(13.4,52.52),"Bethesda, EE.UU.":(-77.1,38.98),
"Boston, EE.UU.":(-71.06,42.36),"Brasilia, Brasil":(-47.88,-15.79),"Bruselas, Bélgica":(4.35,50.85),"Calabria, Italia":(16.35,38.9),
"Cambridge, EE.UU.":(-71.11,42.37),"Changwon, Corea del Sur":(128.68,35.23),"Cheltenham, Reino Unido":(-2.08,51.9),"Ciudad de México, México":(-99.13,19.43),
"Ciudad del Vaticano":(12.45,41.9),"Cologny, Suiza":(6.18,46.22),"Copenhague, Dinamarca":(12.57,55.68),"Costa Mesa, EE.UU.":(-117.92,33.64),
"Culiacán, México":(-107.39,24.81),"Cupertino, EE.UU.":(-122.03,37.32),"Darfur, Sudán":(24.9,13.5),"Denver, EE.UU.":(-104.99,39.74),
"Dhahran, Arabia Saudita":(50.1,26.29),"Doha, Catar":(51.53,25.29),"Dubái, Emiratos Árabes Unidos":(55.27,25.2),"El Cairo, Egipto":(31.24,30.04),
"Fort Meade, EE.UU.":(-76.77,39.11),"Fráncfort, Alemania":(8.68,50.11),"Gaza, Palestina":(34.47,31.5),"Ginebra, Suiza":(6.14,46.2),
"Guadalajara, México":(-103.35,20.67),"Haifa, Israel":(34.99,32.79),"Hangzhou, China":(120.16,30.27),"Hong Kong":(114.17,22.32),
"Houston, EE.UU.":(-95.37,29.76),"Hsinchu, Taiwán":(120.97,24.8),"Islamabad, Pakistán":(73.05,33.68),"Jerusalén, Israel":(35.21,31.77),
"Kabul, Afganistán":(69.17,34.53),"Kiev, Ucrania":(30.52,50.45),"Kobe, Japón":(135.2,34.69),"La Haya, Países Bajos":(4.3,52.08),
"La Hulpe, Bélgica":(4.48,50.73),"La Meca, Arabia Saudita":(39.83,21.42),"Langley, EE.UU.":(-77.15,38.95),"Lausana, Suiza":(6.63,46.52),
"Leiden, Países Bajos":(4.49,52.16),"Leverkusen, Alemania":(6.98,51.03),"Londres, Reino Unido":(-0.13,51.51),"Los Ángeles, EE.UU.":(-118.24,34.05),
"Luxemburgo":(6.13,49.61),"Malvern, EE.UU.":(-75.51,40.04),"Menlo Park, EE.UU.":(-122.18,37.45),"Minnetonka, EE.UU.":(-93.5,44.91),
"Moscú, Rusia":(37.62,55.76),"Mountain View, EE.UU.":(-122.08,37.39),"Múnich, Alemania":(11.58,48.14),"Ningde, China":(119.55,26.67),
"Nom Pen, Camboya":(104.92,11.56),"Nueva Delhi, India":(77.21,28.61),"Nueva York, EE.UU.":(-74.0,40.71),"Omaha, EE.UU.":(-95.94,41.26),
"Origen en Aragua, Venezuela":(-67.6,10.24),"Oslo, Noruega":(10.75,59.91),"Oxford, Reino Unido":(-1.26,51.75),"París, Francia":(2.35,48.86),
"Pekín, China":(116.4,39.9),"Pionyang, Corea del Norte":(125.76,39.04),"Purchase, EE.UU.":(-73.71,41.04),"Rawalpindi, Pakistán":(73.05,33.6),
"Redmond, EE.UU.":(-122.12,47.67),"Reston, EE.UU.":(-77.34,38.96),"Riad, Arabia Saudita":(46.68,24.71),"Roma, Italia":(12.5,41.9),
"Río de Janeiro, Brasil":(-43.17,-22.91),"Sahel central (Malí)":(-2.0,15.5),"Salt Lake City, EE.UU.":(-111.89,40.76),"San Francisco, EE.UU.":(-122.42,37.77),
"San Petersburgo, Rusia":(30.32,59.93),"Santa Clara, EE.UU.":(-121.96,37.35),"Santa Mónica, EE.UU.":(-118.49,34.02),"Saná, Yemen":(44.19,15.37),
"Seattle, EE.UU.":(-122.33,47.61),"Seúl, Corea del Sur":(126.98,37.57),"Shanghái, China":(121.47,31.23),"Shenzhen, China":(114.06,22.54),
"Sin sede central (origen en Egipto)":None,"Sin sede fija":None,"Sin sede fija (secretaría en Leiden, Países Bajos)":None,"Singapur":(103.82,1.35),
"Stanford, EE.UU.":(-122.17,37.43),"Starbase, EE.UU.":(-97.16,25.99),"São Paulo, Brasil":(-46.63,-23.55),"Taipéi, Taiwán":(121.57,25.03),
"Teherán, Irán":(51.39,35.69),"Tel Aviv, Israel":(34.78,32.09),"Tokio, Japón":(139.69,35.69),"Toronto, Canadá":(-79.38,43.65),
"Toyota, Japón":(137.16,35.08),"Veldhoven, Países Bajos":(5.4,51.42),"Viena, Austria":(16.37,48.21),"Washington, EE.UU.":(-77.04,38.9),"Zúrich, Suiza":(8.54,47.37),
"Buenos Aires, Argentina":(-58.38,-34.6),"Bogotá, Colombia":(-74.07,4.71),"Caracas, Venezuela":(-66.9,10.49),"La Habana, Cuba":(-82.37,23.11),
"Santiago, Chile":(-70.65,-33.45),"Quito, Ecuador":(-78.47,-0.18),"Frontera colombo-venezolana":(-71.9,7.9),"Urabá, Colombia":(-76.6,8.0),
"Guayaquil, Ecuador":(-79.9,-2.19),"Abuya, Nigeria":(7.4,9.06),"Lagos, Nigeria":(3.38,6.52),"Pretoria, Sudáfrica":(28.19,-25.75),
"Adís Abeba, Etiopía":(38.75,9.03),"Nairobi, Kenia":(36.82,-1.29),"Kigali, Ruanda":(30.06,-1.95),"Goma, RD Congo":(29.22,-1.68),
"Puerto Sudán, Sudán":(37.22,19.62),"Rabat, Marruecos":(-6.84,34.02),"Casablanca, Marruecos":(-7.59,33.57),"Argel, Argelia":(3.06,36.75),
"Bengasi, Libia":(20.07,32.12),"Sur de Somalia":(43.5,2.5),"Bamako, Malí":(-8.0,12.64),"Madrid, España":(-3.7,40.42),
"Varsovia, Polonia":(21.01,52.23),"Budapest, Hungría":(19.04,47.5),"Düsseldorf, Alemania":(6.77,51.23),"Yakarta, Indonesia":(106.85,-6.21),
"Hanói, Vietnam":(105.85,21.03),"Manila, Filipinas":(120.98,14.6),"Bangkok, Tailandia":(100.5,13.76),"Naipyidó, Myanmar":(96.13,19.76),
"Canberra, Australia":(149.13,-35.28),"Melbourne, Australia":(144.96,-37.81),"Bombay, India":(72.88,19.08),"Ahmedabad, India":(72.57,23.02),
"Astaná, Kazajistán":(71.45,51.17),"Kuala Lumpur, Malasia":(101.69,3.14),"Daca, Bangladés":(90.41,23.81),"Damasco, Siria":(36.29,33.51),
"Ottawa, Canadá":(-75.7,45.42),
"Miami, EE.UU.":(-80.19,25.76),"Austin, EE.UU.":(-97.74,30.27),"Johannesburgo, Sudáfrica":(28.05,-26.2),"Arteixo, España":(-8.51,43.3),
"Ámsterdam, Países Bajos":(4.9,52.37),"Nuevo Taipéi, Taiwán":(121.46,25.01),"Estambul, Turquía":(28.98,41.01),"Perth, Australia":(115.86,-31.95),
"Stuttgart, Alemania":(9.18,48.78),"Nayaf, Irak":(44.34,32.0),
}

from locales import COORDS as _CL
C.update(_CL)

from nucleo import COORDS as _CN
C.update(_CN)

from nucleo2 import COORDS as _CN2
C.update(_CN2)
from nucleo3 import COORDS as _CN3
C.update(_CN3)
from nucleo4 import COORDS as _CN4
C.update(_CN4)
import importlib as _il
for _t in ["nucleo5", "nucleo6", "nucleo7", "nucleo8", "nucleo9", "nucleo10"]: C.update(_il.import_module(_t).COORDS)
