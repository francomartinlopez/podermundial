# Puntaje de categoría y fórmula del puntaje final (criterio editorial del 17 de noviembre de 2026).
# Cada categoría tiene un puntaje teórico (0 a 10, criterio editorial: cuánto poder real suele tener ese tipo
# de actor) y uno real, que se calcula de los datos cargados (autonomía, relaciones de mando y dependientes).

TEORICO = {
    # Estado
    "Servicio de inteligencia": 9, "Ejército": 8, "Fuerza de seguridad": 7, "Gobierno": 6, "Banco central": 6,
    "Justicia": 5, "Partido único o hegemónico": 8, "Partido en sistema competitivo": 5, "Organismo de gobierno": 4,
    # Capital
    "Empresa financiera": 7, "Familia y oficina patrimonial": 7, "Empresa tecnológica": 7, "Empresa de armamento": 6,
    "Recursos primarios": 6, "Farmacéutica y agroquímica": 5, "Empresa industrial": 5, "Consultoría y auditoría": 4,
    "Logística y transporte": 4,
    # Persona
    "Líder político": 8, "Empresario": 6,
    # Sombra
    "Organización criminal": 8, "Paramilitar": 8, "Organización reservada": 4,
    # Influencia
    "Organización religiosa": 5, "Federación empresaria": 5, "ONG, fundación o think tank": 4,
    "Organización deportiva": 4, "Sindicato": 4,
    # Información
    "Red social": 6, "Medio de comunicación": 4, "Institución de conocimiento": 3,
    # Supranacional
    "Institución mundial": 4, "Estandarización e infraestructura técnica": 4,
}

# Puntaje final: media geométrica ponderada de cinco componentes, cada uno entre 0 y 1.
PESO_FINAL = {"ct": .40, "cr": .20, "cap": .25, "aut": .10, "red": .05}

# Relevamiento del puntaje real de cada actor (se promedia por categoría y se lleva a 0-10).
PESO_REL = {"Gobierna": 1, "Propiedad": 1, "Financiamiento": 1, "Acceso a datos": 1, "Abastecimiento": .5, "Puerta giratoria": .5}

# Partidos: se separan los que monopolizan el Estado de los que compiten por el gobierno.
HEGEMONICOS = {"pcch", "ptk", "pcv", "prpl", "pcc_cuba", "pfdj", "fpr", "zanupf", "mpla", "ccm", "frelimo",
               "prosperidad", "cndd_fdd", "psuv"}

# Monarcas: solo figuran los que tienen poder real (las monarquías ceremoniales no entran).
MONARCAS = {"saud", "alnahyan", "althani", "maktoum", "mswati", "al_said", "bolkiah", "al_sabah", "al_khalifa", "hachemita",
            "liechtenstein", "grimaldi", "wangchuck", "tupou"}
NOTA_MONARCA = ("Figura porque ejerce poder real. El mapa solo incluye monarcas que gobiernan o tienen poder de veto o de decisión; "
                "las monarquías ceremoniales, como las de Reino Unido, España, Japón, los países nórdicos, Países Bajos y Bélgica, no entran.")
