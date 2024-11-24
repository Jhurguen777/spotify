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
