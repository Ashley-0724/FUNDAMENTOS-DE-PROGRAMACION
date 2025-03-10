# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (3 semanas)
temperaturas = [
    [  # Ciudad Milagro
        [  # Semana 1
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 29}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 28}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 28}
        ],

    ],
    [  # Ciudad Naranjal
        [  # Semana 1
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 32}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 32}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 34},
            {"day": "Martes", "temp": 34},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 33}
        ],

    ],
    [  # Ciudad Yaguachi
        [  # Semana 1
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 34},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 31}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 34},
            {"day": "Martes", "temp": 34},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 27}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 34},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 34}
        ],

    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Ciudad Milagro", "Ciudad Naranjal", "Ciudad Yaguachi"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")