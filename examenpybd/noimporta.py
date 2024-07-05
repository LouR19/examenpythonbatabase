import pyodbc

def conectarbd(SERVER, DATABASE):
    return f'DRIVER={{ODBC Driver 17 for SQL SERVER}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;'


def conectar(SERVER, DATABASE):
    cbd = conectarbd(SERVER, DATABASE)
    try:
        cntion = pyodbc.connect(cbd)
        print('La conexion se ha completado exitosamente!')
        input("")
        return cntion
    except pyodbc.Error as error:
        print(f'Conexion fallida: {error}')
        return None

def cerrar_conexion(cntion):
    if cntion:
        cntion.close()
        print('Conexión cerrada! Bye.')

def anadir(cntion):
    try:
        cursor = cntion.cursor()
        query = 'INSERT INTO Estudiantes VALUES (?, ?, ?, ?)'
        cursor.execute(query, 5, 'Douglas', 'hambre', '2024-10-10')
        cursor.commit()
        cursor.close()
        return True
    except pyodbc.Error as error: 
        print(f'Error al conectar con la base de datos:{error}')
        cursor.close()
        input('Presione Enter para continuar...')
        return None



SERVER = 'ALUMNOS'
DATABASE = 'Escuela'
TABLE = 'Estudiantes'
que = conectar(SERVER, DATABASE)
anadir(que)


