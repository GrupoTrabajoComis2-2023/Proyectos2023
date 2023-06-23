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

    def leer_leyes(self):
        self.cursor.execute("SELECT * FROM Leyes")
        leyes = self.cursor.fetchall()
        for ley in leyes:
            print("ID:", ley[0])
            print("Número:", ley[1])
            print("Tipo de normativa:", ley[2])
            print("Número de normativa:", ley[3])
            print("Fecha:", ley[4])
            print("Descripción:", ley[5])
            print("Categoría:", ley[6])
            print("Jurisdicción:", ley[7])
            print("Órgano legislativo:", ley[8])
            print("Palabras clave:", ley[9])
            print()
    
        if not leyes:
            print("No hay Leyes registradas.")

    def actualizar_ley(self, id_ley, Nro_Registro, Tipo_Normativa, Nro_Normativa, Fecha, Descripcion, Categoria, Jurisdiccion, Organo_Legislativo, Palabras_Clave):
        self.cursor.execute(
            """UPDATE Leyes
            SET Nro_Registro = ?,
                Tipo_Normativa = ?,
                Nro_Normativa = ?,
                Fecha = ?,
                Descripcion = ?,
                Categoria = ?,
                Jurisdiccion = ?,
                Organo_Legislativo = ?,
                Palabras_Clave = ?
            WHERE id = ?""",
            (
                Nro_Registro,
                Tipo_Normativa,
                Nro_Normativa,
                Fecha,
                Descripcion,
                Categoria,
                Jurisdiccion,
                Organo_Legislativo,
                ",".join(Palabras_Clave),
                id_ley,
            ),
        )

        self.conexion.commit()
        print("La ley se ha actualizado correctamente.")