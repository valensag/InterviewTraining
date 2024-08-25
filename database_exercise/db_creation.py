import sqlite3

def create_database():
    conn = sqlite3.connect('jokes.db')
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT UNIQUE NOT NULL,
        contrasena TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Tematicas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT UNIQUE NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Chistes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        cuerpo TEXT NOT NULL,
        autor_id INTEGER,
        FOREIGN KEY (autor_id) REFERENCES Usuarios(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Chistes_Tematicas (
        chiste_id INTEGER,
        tematica_id INTEGER,
        FOREIGN KEY (chiste_id) REFERENCES Chistes(id),
        FOREIGN KEY (tematica_id) REFERENCES Tematicas(id)
    )
    ''')

    conn.commit()
    conn.close()

def insert_data():
    conn = sqlite3.connect('jokes.db')
    cursor = conn.cursor()

    # Insert users
    users = [
        ('Manolito', 'pass1'),
        ('Pepe', 'pass2'),
        ('Isabel', 'pass3'),
        ('Pedro', 'pass4')
    ]

    cursor.executemany('INSERT OR IGNORE INTO Usuarios (nombre, contrasena) VALUES (?, ?)', users)

    # Insert themes
    themes = [
        ('humor negro',),
        ('humor amarillo',),
        ('chistes verdes',)
    ]

    cursor.executemany('INSERT OR IGNORE INTO Tematicas (nombre) VALUES (?)', themes)

    # Commit to get the auto-incremented IDs
    conn.commit()

    # Fetch IDs for users
    user_ids = {name: id for id, name in cursor.execute('SELECT id, nombre FROM Usuarios').fetchall()}

    # Fetch IDs for themes
    theme_ids = {name: id for id, name in cursor.execute('SELECT id, nombre FROM Tematicas').fetchall()}

    # Insert jokes
    jokes = [
        ('Chiste 1 humor negro', 'Cuerpo del chiste 1', user_ids['Manolito']),
        ('Chiste 2 humor negro', 'Cuerpo del chiste 2', user_ids['Manolito']),
        ('Chiste 3 humor negro', 'Cuerpo del chiste 3', user_ids['Manolito']),
        ('Chiste 1 humor amarillo', 'Cuerpo del chiste 1', user_ids['Pepe']),
        ('Chiste 2 humor amarillo', 'Cuerpo del chiste 2', user_ids['Pepe']),
        ('Chiste 3 humor amarillo', 'Cuerpo del chiste 3', user_ids['Isabel']),
        ('Chiste 1 chistes verdes', 'Cuerpo del chiste 1', user_ids['Pedro']),
        ('Chiste 2 chistes verdes', 'Cuerpo del chiste 2', user_ids['Pedro']),
        ('Chiste 3 chistes verdes', 'Cuerpo del chiste 3', user_ids['Isabel']),
    ]

    cursor.executemany('INSERT INTO Chistes (titulo, cuerpo, autor_id) VALUES (?, ?, ?)', jokes)

    # Link jokes to themes
    joke_theme_links = [
        (1, theme_ids['humor negro']),
        (2, theme_ids['humor negro']),
        (3, theme_ids['humor negro']),
        (4, theme_ids['humor amarillo']),
        (5, theme_ids['humor amarillo']),
        (6, theme_ids['humor amarillo']),
        (7, theme_ids['chistes verdes']),
        (8, theme_ids['chistes verdes']),
        (9, theme_ids['chistes verdes']),
    ]

    cursor.executemany('INSERT INTO Chistes_Tematicas (chiste_id, tematica_id) VALUES (?, ?)', joke_theme_links)

    conn.commit()
    conn.close()

def execute_query():
    conn = sqlite3.connect('jokes.db')
    cursor = conn.cursor()

    # Query 1: Get all jokes created by "Manolito"
    cursor.execute('''
    SELECT Chistes.*
    FROM Chistes
    JOIN Usuarios ON Chistes.autor_id = Usuarios.id
    WHERE Usuarios.nombre = "Manolito"
    ''')
    manolito_jokes = cursor.fetchall()
    print("Jokes created by Manolito:")
    for joke in manolito_jokes:
        print(f"ID: {joke[0]}, Title: {joke[1]}, Body: {joke[2]}")

    # Query 2: Get all jokes from the theme "humor negro"
    cursor.execute('''
    SELECT Chistes.*
    FROM Chistes
    JOIN Chistes_Tematicas ON Chistes.id = Chistes_Tematicas.chiste_id
    JOIN Tematicas ON Chistes_Tematicas.tematica_id = Tematicas.id
    WHERE Tematicas.nombre = "humor negro"
    ''')
    humor_negro_jokes = cursor.fetchall()
    print("\nJokes from the theme 'humor negro':")
    for joke in humor_negro_jokes:
        print(f"ID: {joke[0]}, Title: {joke[1]}, Body: {joke[2]}")

    # Query 3: Get all jokes from the theme "humor negro" created by "Manolito"
    cursor.execute('''
    SELECT Chistes.*
    FROM Chistes
    JOIN Usuarios ON Chistes.autor_id = Usuarios.id
    JOIN Chistes_Tematicas ON Chistes.id = Chistes_Tematicas.chiste_id
    JOIN Tematicas ON Chistes_Tematicas.tematica_id = Tematicas.id
    WHERE Usuarios.nombre = "Manolito" AND Tematicas.nombre = "humor negro"
    ''')
    manolito_humor_negro_jokes = cursor.fetchall()
    print("\nJokes from the theme 'humor negro' created by Manolito:")
    for joke in manolito_humor_negro_jokes:
        print(f"ID: {joke[0]}, Title: {joke[1]}, Body: {joke[2]}")

    conn.close()

if __name__ == '__main__':
    create_database()
    insert_data()
    execute_query()
