import pyodbc
from main import clear

def anadir(estudiante, cntion):
    try:
        cursor = cntion.cursor()
        query = 'INSERT INTO Estudiantes VALUES (?, ?, ?, ?)'
        cursor.execute(query, estudiante['EstudianteID'], estudiante ['Nombre'], estudiante['Apellido'], estudiante['FechaNacimiento'])
        cursor.commit()
        cursor.close()
        return True
    except pyodbc.Error as error: 
        print(f'Error al conectar con la base de datos:{error}')
        cursor.close()
        input('Presione Enter para continuar...')
        return None
    
def leer(studentID, cntion):

    try:
        cursor = cntion.cursor()
        query = 'SELECT * FROM Estudiantes WHERE EstudianteID = ?'
        cursor.execute(query, studentID)
        r = cursor.fetchone()
        return r

    except pyodbc.Error as error:
        print(f"Ocurrió un error al Leer los estudiantes: {error}")
        input('Presione Enter para continuar...')
        cursor.close()
        clear()
        return None
        
def actualizar(studentID, cntion):
    try:
        r = leer(studentID, cntion) 
        if not r:
            print("Error: El ID ingresado no corresponde a ningún estudiante.")
            return


        print(f"----Estudiante----\n ID: {r[0]}.\n Nombre: {r[1]}.\n Apellido: {r[2]}.\n Fecha de Nacimiento: {r[3]}.\n")
        opcion = input("¿Qué campo desea actualizar?\n 1-Nombre.\n 2-Apellido.\n 3-Fecha de Nacimiento (AÑO-MES-DIA).\n 4-Todos los campos.\n 5-Cancelar.\n> ")

        if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
            print("Opción inválida. Intente nuevamente.")
            return

        opcion = int(opcion)

        cursor = cntion.cursor()
        match opcion:
            case 1:
                nombre = input("Ingrese el nuevo nombre: ")
                query = "UPDATE Estudiantes SET Nombre = ? WHERE EstudianteID = ?"
                cursor.execute(query, (nombre, studentID))
                return r
            case 2:
                apellido = input("Ingrese el nuevo apellido: ")
                query = "UPDATE Estudiantes SET Apellido = ? WHERE EstudianteID = ?"
                cursor.execute(query, (apellido, studentID))
                return r
            case 3:
                fechaNac = input("Ingrese la nueva fecha de nacimiento (AÑO-MES-DIA): ")
                query = "UPDATE Estudiantes SET FechaNacimiento = ? WHERE EstudianteID = ?"
                cursor.execute(query, (fechaNac, studentID))
                return r
            case 4:
                nombre = input("Ingrese el nuevo nombre: ")
                apellido = input("Ingrese el nuevo apellido: ")
                fechaNac= input("Ingrese la nueva fecha de nacimiento (AÑO-MES-DIA): ")
                query = "UPDATE Estudiantes SET Nombre = ?, Apellido = ?, FechaNacimiento = ? WHERE EstudianteID = ?"
                cursor.execute(query, (nombre, apellido, fechaNac, studentID))
                return r
            case 5:
                cursor.close()
                return
        cntion.commit()
        cursor.close()
    except pyodbc.Error as Error:
        print(f"Ocurrió un error al actualizar el estudiante: {Error}")

def eliminar(studentID, cntion):
    r = leer(studentID, cntion)
    if not (r):
        print('Estudiante no encontrado...')
        input('Presione Enter para continuar...')
        return None
        
    print(f'----Estudiantes----\n ID: {r[0]}.\n Nombre: {r[1]}.\n Apellido: {r[2]}.\n Fecha de Nacimiento: {r[3]}. ')
    print('Desea eliminarlo?:\n 1 - Si\n2 - No')
    r = int(input())
    match r:
        case 1:
            cursor = cntion.cursor()
            cursor.execute('DELETE FROM Estudiantes WHERE EstudianteID = ?', studentID)
            cursor.commit()
            cursor.close()
            return True
        case 2:
            return False
