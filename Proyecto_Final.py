import sqlite3


class Ley:
    def __init__(self, Nro_Registro, Tipo_Normativa, Nro_Normativa, Fecha, Descripcion, Categoria, Jurisdiccion, Organo_Legislativo, Palabras_Clave):
        self.Nro_Registro = Nro_Registro
        self.Tipo_Normativa = Tipo_Normativa
        self.Nro_Normativa = Nro_Normativa
        self.Fecha = Fecha
        self.Descripcion = Descripcion
        self.Categoria = Categoria
        self.Jurisdiccion = Jurisdiccion
        self.Organo_Legislativo = Organo_Legislativo
        self.Palabras_Clave = Palabras_Clave


class BaseDatos:
    def __init__(self):
        self.conexion = sqlite3.connect("ProyectoFinal2.0")
        self.cursor = self.conexion.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS Leyes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Nro_Registro TEXT,
                Tipo_Normativa TEXT,
                Nro_Normativa INTEGER,
                Fecha TEXT,
                Descripcion TEXT,
                Categoria TEXT,
                Jurisdiccion TEXT,
                Organo_Legislativo TEXT,
                Palabras_Clave TEXT
            )"""
        )

    def crear_ley(self, ley):
        self.cursor.execute(
            """INSERT INTO Leyes (Nro_Registro, Tipo_Normativa, Nro_Normativa, Fecha, Descripcion, Categoria, Jurisdiccion, Organo_Legislativo, Palabras_Clave)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                ley.Nro_Registro,
                ley.Tipo_Normativa,
                ley.Nro_Normativa,
                ley.Fecha,
                ley.Descripcion,
                ley.Categoria,
                ley.Jurisdiccion,
                ley.Organo_Legislativo,
                ",".join(ley.Palabras_Clave),
            ),
        )

        self.conexion.commit()
        print("La ley se ha creado correctamente.")
