import mysql.connector

# Función para conectar a la base de datos
def conectar_db():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="spotify_simulacion"
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error conectando a la base de datos: {err}")
        return None

# Función para buscar canciones por género o artista
def buscar_cancion_por_filtro():
    conexion = conectar_db()
    if conexion is None:
        print("No se pudo conectar a la base de datos.")
        return

    cursor = conexion.cursor()

    print("\n===== Buscar Canciones =====")
    print("1. Buscar por género")
    print("2. Buscar por artista")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        genero = input("Introduce el género musical que deseas buscar: ")
        cursor.execute("SELECT * FROM Canciones WHERE genero LIKE %s", ('%' + genero + '%',))
        canciones = cursor.fetchall()
    elif opcion == "2":
        artista = input("Introduce el nombre del artista que deseas buscar: ")
        cursor.execute("SELECT * FROM Canciones WHERE artista LIKE %s", ('%' + artista + '%',))
        canciones = cursor.fetchall()
    else:
        print("Opción no válida.")
        cursor.close()
        conexion.close()
        return

    # Mostrar resultados
    if canciones:
        print("\nCanciones encontradas:")
        for cancion in canciones:
            print(f"ID: {cancion[0]}, Título: {cancion[1]}, Artista: {cancion[2]}, Álbum: {cancion[3]}, Género: {cancion[4]}")
    else:
        print("No se encontraron canciones que coincidan con tu búsqueda.")

    cursor.close()
    conexion.close()

# Nueva función para agregar una canción
def agregar_cancion():
    """
    Permite al usuario agregar una nueva canción a la base de datos.
    """
    conexion = conectar_db()
    if conexion is None:
        print("No se pudo conectar a la base de datos.")
        return

    cursor = conexion.cursor()

    print("\n===== Agregar Nueva Canción =====")
    titulo = input("Introduce el título de la canción: ")
    artista = input("Introduce el nombre del artista: ")
    album = input("Introduce el álbum: ")
    genero = input("Introduce el género musical: ")

    try:
        # Insertar la nueva canción en la base de datos
        cursor.execute(
            "INSERT INTO Canciones (titulo, artista, album, genero) VALUES (%s, %s, %s, %s)",
            (titulo, artista, album, genero)
        )
        conexion.commit()  # Confirmar cambios en la base de datos
        print("Canción agregada exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error al agregar la canción: {err}")
    finally:
        cursor.close()
        conexion.close()

# Llamada de prueba para la nueva función
# agregar_cancion()
