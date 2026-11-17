"""Genera fuente/paises_datos.py con las cifras clave de cada país del mapa.

Fuente: CIA World Factbook (dominio público), vía el espejo
github.com/factbook/factbook.json, y nombres en español de
github.com/mledoze/countries.

Uso:
  git clone --depth 1 https://github.com/factbook/factbook.json /tmp/factbook
  curl -sL -o /tmp/countries.json https://raw.githubusercontent.com/mledoze/countries/master/countries.json
  python3 scripts/importar_factbook.py /tmp/factbook /tmp/countries.json
"""
import json, glob, re, sys, os, subprocess, pprint

FB = sys.argv[1] if len(sys.argv) > 1 else '/tmp/factbook'
CJ = sys.argv[2] if len(sys.argv) > 2 else '/tmp/countries.json'
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MAP = {'United States of America': 'north-america/us', 'Macedonia': 'europe/mk', 'Bosnia and Herz.': 'europe/bk',
 'Micronesia': 'australia-oceania/fm', 'Marshall Is.': 'australia-oceania/rm', 'Vatican': 'europe/vt',
 'Macao': 'east-n-southeast-asia/mc', 'Dominican Rep.': 'central-america-n-caribbean/dr',
 'Bahamas': 'central-america-n-caribbean/bf', 'United Arab Emirates': 'middle-east/ae',
 'Palestine': ['middle-east/we', 'middle-east/gz'], 'Myanmar': 'east-n-southeast-asia/bm',
 'Solomon Is.': 'australia-oceania/bp', 'W. Sahara': 'africa/wi', 'S. Sudan': 'africa/od',
 'Dem. Rep. Congo': 'africa/cg', 'Congo': 'africa/cf', 'Central African Rep.': 'africa/ct',
 "Côte d'Ivoire": 'africa/iv', 'Gambia': 'africa/ga', 'Eq. Guinea': 'africa/ek',
 'São Tomé and Principe': 'africa/tp', 'Antigua and Barb.': 'central-america-n-caribbean/ac',
 'St. Kitts and Nevis': 'central-america-n-caribbean/sc', 'St. Vin. and Gren.': 'central-america-n-caribbean/vc',
 'N. Mariana Is.': 'australia-oceania/cq', 'U.S. Virgin Is.': 'central-america-n-caribbean/vq',
 'S. Geo. and the Is.': 'south-america/sx', 'Br. Indian Ocean Ter.': 'south-asia/io', 'Saint Helena': 'africa/sh',
 'Pitcairn Is.': 'australia-oceania/pc', 'Falkland Is.': 'south-america/fk', 'Cayman Is.': 'central-america-n-caribbean/cj',
 'British Virgin Is.': 'central-america-n-caribbean/vi', 'Turks and Caicos Is.': 'central-america-n-caribbean/tk',
 'Cook Is.': 'australia-oceania/cw', 'Curaçao': 'central-america-n-caribbean/uc', 'St. Pierre and Miquelon': 'north-america/sb',
 'Wallis and Futuna Is.': 'australia-oceania/wf', 'St-Martin': 'central-america-n-caribbean/rn',
 'St-Barthélemy': 'central-america-n-caribbean/tb', 'Fr. Polynesia': 'australia-oceania/fp',
 'Fr. S. Antarctic Lands': 'antarctica/fs', 'Faeroe Is.': 'europe/fo',
 'Indian Ocean Ter.': ['australia-oceania/kt', 'australia-oceania/ck'], 'Heard I. and McDonald Is.': 'antarctica/hm',
 'Ashmore and Cartier Is.': 'australia-oceania/at',
 'N. Cyprus': None, 'Somaliland': None, 'Åland': None, 'Siachen Glacier': None}

ABREV = {'USA': 'Estados Unidos', 'US': 'Estados Unidos', 'UK': 'Reino Unido', 'UAE': 'Emiratos Árabes Unidos',
 'S. Korea': 'Corea del Sur', 'South Korea': 'Corea del Sur', 'N. Korea': 'Corea del Norte', 'North Korea': 'Corea del Norte',
 'Hong Kong': 'Hong Kong', 'Taiwan': 'Taiwán', 'Russia': 'Rusia', 'Vietnam': 'Vietnam', 'Czechia': 'Chequia',
 'Turkey': 'Turquía', 'Netherlands': 'Países Bajos', 'Burma': 'Myanmar', 'Macau': 'Macao', 'Iran': 'Irán',
 'DRC': 'RD del Congo', 'Republic of the Congo': 'Congo', 'Congo': 'Congo', "Cote d'Ivoire": 'Costa de Marfil',
 "C&ocirc;te d'Ivoire": 'Costa de Marfil', "Côte d'Ivoire": 'Costa de Marfil', 'Bosnia and Herzegovina': 'Bosnia y Herzegovina',
 'Laos': 'Laos', 'Syria': 'Siria', 'Bolivia': 'Bolivia', 'Venezuela': 'Venezuela', 'Tanzania': 'Tanzania',
 'Moldova': 'Moldavia', 'North Macedonia': 'Macedonia del Norte', 'Brunei': 'Brunéi', 'Micronesia': 'Micronesia',
 'The Bahamas': 'Bahamas', 'Bahamas, The': 'Bahamas', 'The Gambia': 'Gambia', 'Gambia, The': 'Gambia',
 'West Bank': 'Cisjordania', 'Gaza Strip': 'Franja de Gaza', 'Palestine': 'Palestina', 'Kosovo': 'Kosovo',
 'Curacao': 'Curazao', 'Sint Maarten': 'Sint Maarten', 'Eswatini': 'Esuatini', 'Timor-Leste': 'Timor Oriental',
 'Sao Tome and Principe': 'Santo Tomé y Príncipe', 'Holy See': 'Vaticano', 'Saint Lucia': 'Santa Lucía',
 'Marshall Islands': 'Islas Marshall', 'Solomon Islands': 'Islas Salomón', 'Cabo Verde': 'Cabo Verde',
 'British Virgin Islands': 'Islas Vírgenes Británicas', 'Virgin Islands': 'Islas Vírgenes de EE.UU.',
 'Cayman Islands': 'Islas Caimán', 'Falkland Islands': 'Malvinas', 'Saint Helena, Ascension, and Tristan da Cunha': 'Santa Elena',
 'Saint Pierre and Miquelon': 'San Pedro y Miquelón', 'Guam': 'Guam', 'Puerto Rico': 'Puerto Rico',
 'New Caledonia': 'Nueva Caledonia', 'French Polynesia': 'Polinesia Francesa', 'Greenland': 'Groenlandia',
 'Faroe Islands': 'Islas Feroe', 'Isle of Man': 'Isla de Man', 'Gibraltar': 'Gibraltar', 'Jersey': 'Jersey',
 'Guernsey': 'Guernsey', 'Bermuda': 'Bermudas', 'Aruba': 'Aruba', 'Montserrat': 'Montserrat', 'Anguilla': 'Anguila',
 'Turks and Caicos Islands': 'Islas Turcas y Caicos', 'Northern Mariana Islands': 'Islas Marianas del Norte',
 'American Samoa': 'Samoa Americana', 'Cook Islands': 'Islas Cook', 'Niue': 'Niue', 'Wallis and Futuna': 'Wallis y Futuna',
 'Saint Martin': 'San Martín', 'Saint Barthelemy': 'San Bartolomé', 'Western Sahara': 'Sahara Occidental',
 'South Sudan': 'Sudán del Sur', 'Central African Republic': 'República Centroafricana', 'Equatorial Guinea': 'Guinea Ecuatorial',
 'Dominican Republic': 'República Dominicana', 'Papua New Guinea': 'Papúa Nueva Guinea', 'Saudi Arabia': 'Arabia Saudita',
 'Antigua and Barbuda': 'Antigua y Barbuda', 'Saint Kitts and Nevis': 'San Cristóbal y Nieves',
 'Saint Vincent and the Grenadines': 'San Vicente y las Granadinas', 'Trinidad and Tobago': 'Trinidad y Tobago',
 'Singapore': 'Singapur', 'Philippines': 'Filipinas', 'Japan': 'Japón', 'Germany': 'Alemania', 'France': 'Francia',
 'Italy': 'Italia', 'Spain': 'España', 'Belgium': 'Bélgica', 'Switzerland': 'Suiza', 'Poland': 'Polonia',
 'Brazil': 'Brasil', 'Mexico': 'México', 'Canada': 'Canadá', 'India': 'India', 'China': 'China', 'Thailand': 'Tailandia',
 'Malaysia': 'Malasia', 'South Africa': 'Sudáfrica', 'Egypt': 'Egipto', 'Morocco': 'Marruecos', 'Algeria': 'Argelia',
 'Tunisia': 'Túnez', 'Iraq': 'Irak', 'Jordan': 'Jordania', 'Lebanon': 'Líbano', 'Kuwait': 'Kuwait', 'Qatar': 'Catar',
 'Bahrain': 'Baréin', 'Oman': 'Omán', 'Yemen': 'Yemen', 'Afghanistan': 'Afganistán', 'Pakistan': 'Pakistán',
 'Kazakhstan': 'Kazajistán', 'Uzbekistan': 'Uzbekistán', 'Kyrgyzstan': 'Kirguistán', 'Tajikistan': 'Tayikistán',
 'Turkmenistan': 'Turkmenistán', 'Azerbaijan': 'Azerbaiyán', 'Belarus': 'Bielorrusia', 'Ukraine': 'Ucrania',
 'Sweden': 'Suecia', 'Norway': 'Noruega', 'Denmark': 'Dinamarca', 'Finland': 'Finlandia', 'Ireland': 'Irlanda',
 'Austria': 'Austria', 'Hungary': 'Hungría', 'Romania': 'Rumania', 'Bulgaria': 'Bulgaria', 'Greece': 'Grecia',
 'Cyprus': 'Chipre', 'Lithuania': 'Lituania', 'Latvia': 'Letonia', 'Estonia': 'Estonia', 'Slovakia': 'Eslovaquia',
 'Slovenia': 'Eslovenia', 'Croatia': 'Croacia', 'Serbia': 'Serbia', 'Albania': 'Albania', 'Montenegro': 'Montenegro',
 'Portugal': 'Portugal', 'Luxembourg': 'Luxemburgo', 'Iceland': 'Islandia', 'Malta': 'Malta', 'Israel': 'Israel',
 'Australia': 'Australia', 'New Zealand': 'Nueva Zelanda', 'Indonesia': 'Indonesia', 'Bangladesh': 'Bangladés',
 'Sri Lanka': 'Sri Lanka', 'Nepal': 'Nepal', 'Cambodia': 'Camboya', 'Mongolia': 'Mongolia', 'Nigeria': 'Nigeria',
 'Ghana': 'Ghana', 'Kenya': 'Kenia', 'Ethiopia': 'Etiopía', 'Uganda': 'Uganda', 'Rwanda': 'Ruanda', 'Zambia': 'Zambia',
 'Zimbabwe': 'Zimbabue', 'Mozambique': 'Mozambique', 'Namibia': 'Namibia', 'Botswana': 'Botsuana', 'Angola': 'Angola',
 'Cameroon': 'Camerún', 'Senegal': 'Senegal', 'Mali': 'Malí', 'Niger': 'Níger', 'Chad': 'Chad', 'Sudan': 'Sudán',
 'Libya': 'Libia', 'Mauritania': 'Mauritania', 'Burkina Faso': 'Burkina Faso', 'Benin': 'Benín', 'Togo': 'Togo',
 'Guinea': 'Guinea', 'Sierra Leone': 'Sierra Leona', 'Liberia': 'Liberia', 'Gabon': 'Gabón', 'Madagascar': 'Madagascar',
 'Mauritius': 'Mauricio', 'Malawi': 'Malaui', 'Burundi': 'Burundi', 'Somalia': 'Somalia', 'Djibouti': 'Yibuti',
 'Eritrea': 'Eritrea', 'Colombia': 'Colombia', 'Peru': 'Perú', 'Chile': 'Chile', 'Argentina': 'Argentina',
 'Uruguay': 'Uruguay', 'Paraguay': 'Paraguay', 'Ecuador': 'Ecuador', 'Guyana': 'Guyana', 'Suriname': 'Surinam',
 'Panama': 'Panamá', 'Costa Rica': 'Costa Rica', 'Nicaragua': 'Nicaragua', 'Honduras': 'Honduras',
 'El Salvador': 'El Salvador', 'Guatemala': 'Guatemala', 'Belize': 'Belice', 'Cuba': 'Cuba', 'Haiti': 'Haití',
 'Jamaica': 'Jamaica', 'Barbados': 'Barbados', 'Fiji': 'Fiyi', 'Samoa': 'Samoa', 'Tonga': 'Tonga', 'Vanuatu': 'Vanuatu',
 'Kiribati': 'Kiribati', 'Nauru': 'Nauru', 'Palau': 'Palaos', 'Tuvalu': 'Tuvalu', 'Maldives': 'Maldivas',
 'Bhutan': 'Bután', 'Georgia': 'Georgia', 'Armenia': 'Armenia', 'Lesotho': 'Lesoto', 'Comoros': 'Comoras',
 'Seychelles': 'Seychelles', 'Dominica': 'Dominica', 'Grenada': 'Granada', 'Andorra': 'Andorra', 'Monaco': 'Mónaco',
 'Liechtenstein': 'Liechtenstein', 'San Marino': 'San Marino', 'Guinea-Bissau': 'Guinea-Bisáu',
 'Christmas Island': 'Isla de Navidad', 'Cocos (Keeling) Islands': 'Islas Cocos', 'Norfolk Island': 'Isla Norfolk',
 'Tokelau': 'Tokelau', 'Pitcairn Islands': 'Islas Pitcairn', 'Nigeria ': 'Nigeria', 'Saint Helena': 'Santa Elena',
 'Uzbekistan ': 'Uzbekistán', 'Bonaire, Sint Eustatius, and Saba': 'Caribe Neerlandés', 'Svalbard': 'Svalbard', 'NZ': 'Nueva Zelanda', 'St. Lucia': 'Santa Lucía',
 'St. Kitts and Nevis': 'San Cristóbal y Nieves', 'St. Vincent and the Grenadines': 'San Vicente y las Granadinas',
 'United Kingdom': 'Reino Unido'}

def limpiar(t):
    t = re.sub(r'<[^>]+>', '', t or '').replace('&nbsp;', ' ').replace('&ocirc;', 'ô')
    return re.sub(r'\s+', ' ', t).strip()

def texto(d, *ks):
    for k in ks:
        if not isinstance(d, dict) or k not in d:
            return None
        d = d[k]
    if isinstance(d, dict):
        d = d.get('text')
    return limpiar(d) if isinstance(d, str) else None

def ultimo(d, pref):
    """Valor más reciente de un campo con subclaves por año."""
    if not isinstance(d, dict):
        return None
    if 'text' in d:
        return limpiar(d['text'])
    for k in sorted(d.keys(), reverse=True):
        if k.startswith(pref) and isinstance(d[k], dict) and 'text' in d[k]:
            return limpiar(d[k]['text'])
    return None

ESC = {'trillion': 1e12, 'billion': 1e9, 'million': 1e6}
def anio(t):
    m = re.search(r'\((?:\D*?)(\d{4})', t or '')
    return int(m.group(1)) if m else None
def num(t):
    if not t: return None
    m = re.search(r'(-?[\d,]*\.?\d+)\s*(trillion|billion|million)?', t)
    if not m: return None
    v = float(m.group(1).replace(',', ''))
    if m.group(2): v *= ESC[m.group(2)]
    return v
def par(t):
    v = num(t)
    return None if v is None else (round(v, 2) if abs(v) < 1000 else int(v), anio(t))

def socios(t, NOM):
    if not t: return None
    t = re.sub(r'\(\d{4}\)', '', t).replace('&amp;', 'and').replace('almost entirely ', '')
    t = t.replace('Bahamas, The', 'Bahamas').replace('Gambia, The', 'Gambia').replace('Congo, Republic of the', 'Republic of the Congo')
    out = []
    for p in t.split(','):
        p = p.strip(' .')
        m = re.match(r'(.+?)\s*(\d+(?:\.\d+)?)?%?$', p)
        if not m or not m.group(1): continue
        n = m.group(1).strip()
        es = ABREV.get(n) or NOM.get(n.lower())
        if not es:
            print('  socio sin traducir:', n); es = n
        out.append((es, int(float(m.group(2))) if m.group(2) else None))
    return out[:5] or None

def registro(d, NOM):
    E = d.get('Economy', {}); P = d.get('People and Society', {})
    pob = texto(P, 'Population', 'total') or texto(P, 'Population')
    return {
        'pob': par(pob) if pob and 'uninhabited' not in pob.lower() else (0, None),
        'area': (lambda v: int(v) if v is not None else None)(num(texto(d, 'Geography', 'Area', 'total ') or texto(d, 'Geography', 'Area', 'total'))),
        'crec': par(texto(P, 'Population growth rate')),
        'edad': par(texto(P, 'Median age', 'total')),
        'urb': par(texto(P, 'Urbanization', 'urban population')),
        'pib': par(ultimo(E.get('GDP (official exchange rate)'), 'GDP')),
        'pibpc': par(ultimo(E.get('Real GDP per capita'), 'Real GDP per capita')),
        'crecpib': par(ultimo(E.get('Real GDP growth rate'), 'Real GDP growth rate')),
        'infl': par(ultimo(E.get('Inflation rate (consumer prices)'), 'Inflation rate')),
        'deuda': par(ultimo(E.get('Public debt'), 'Public debt')),
        'desoc': par(ultimo(E.get('Unemployment rate'), 'Unemployment rate')),
        'mil': par(ultimo((d.get('Military and Security') or {}).get('Military expenditures'), 'Military Expenditures')),
        'expo': socios(texto(E, 'Exports - partners'), NOM),
        'impo': socios(texto(E, 'Imports - partners'), NOM),
    }

def main():
    NOM = {}
    for c in json.load(open(CJ)):
        es = c['translations']['spa']['common']
        NOM[c['name']['common'].lower()] = es
        NOM[c['name']['official'].lower()] = es
    nombres = {}
    for f in glob.glob(FB + '/*/*.json'):
        n = texto(json.load(open(f)), 'Government', 'Country name', 'conventional short form')
        if n: nombres[n.lower()] = f[len(FB) + 1:-5]
    claves = json.loads(subprocess.check_output(['node', '-e',
        "global.window={};require(process.argv[1]);console.log(JSON.stringify(Object.keys(window.PAISES)))",
        os.path.join(RAIZ, 'data/paises.js')]))
    out = {}
    for k in claves:
        m = MAP.get(k, '?')
        if m == '?': m = nombres.get(k.lower())
        if m is None: continue
        if isinstance(m, list):
            rs = [registro(json.load(open(f'{FB}/{x}.json')), NOM) for x in m]
            r = rs[0]
            for x in ('pob', 'area'):  # se suman territorio y población; el resto es del primero
                vals = [q[x] for q in rs if q[x]]
                if x == 'pob': r[x] = (sum(v[0] for v in vals), vals[0][1])
                else: r[x] = sum(vals)
        else:
            r = registro(json.load(open(f'{FB}/{m}.json')), NOM)
        # se descartan cifras anteriores a 2020 para no mostrar datos viejos
        # y, en las que cambian rápido (inflación, crecimiento, desempleo), las anteriores a 2023
        r = {a: b for a, b in r.items() if not (isinstance(b, tuple) and b[1] and b[1] < (2023 if a in ('infl', 'crecpib', 'desoc') else 2020))}
        if k == 'Vatican': r['area'] = 0.44
        out[k] = {a: b for a, b in r.items() if b not in (None, [], (None, None))}
    with open(os.path.join(RAIZ, 'fuente/paises_datos.py'), 'w') as f:
        f.write('# Generado por scripts/importar_factbook.py: no editar a mano.\n')
        f.write('# Fuente: CIA World Factbook (dominio público), ediciones 2024-2025.\n')
        f.write('# pob, crec, edad, urb, pib, pibpc, crecpib, infl, deuda, desoc, mil: (valor, año).\n')
        f.write('# area en km²; expo/impo: (socio, % del total).\n\n')
        f.write('DATOS = ' + pprint.pformat(out, width=160, sort_dicts=False) + '\n')
    print(len(out), 'países')

main()
