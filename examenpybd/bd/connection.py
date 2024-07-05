import pyodbc

def conectarbd(SERVER, DATABASE):
    return f'DRIVER={{ODBC Driver 17 for SQL SERVER}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;'


def conectar(SERVER, DATABASE):
    cbd = conectarbd(SERVER, DATABASE)
    try:
        cntion = pyodbc.connect(cbd)
        print('La conexion se ha completado exitosamente!')
        input("Presione Enter para continuar...")
        return cntion
    except pyodbc.Error as error:
        print(f'Conexion fallida: {error}')
        return None

def cerrar_conexion(cntion):
    if cntion:
        cntion.close()
        print('Conexión cerrada! Bye.')
