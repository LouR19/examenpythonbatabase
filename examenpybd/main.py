""" 1. *Laura* - Tabla: Estudiantes
    - Enunciado: Crear un CRUD para la tabla Estudiantes que permita añadir, leer, actualizar
    y eliminar registros de estudiantes. Los campos a manejar son EstudianteID, Nombre, Apellido y FechaNacimiento.
 """
from bd import CRUD, connection
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else: 
        os.system('clear')


SERVER = 'DESKTOP-HEMQVAQ'
DATABASE = 'Escuela'
TABLE = 'Estudiantes'

def main():
    cntion = connection.conectar(SERVER, DATABASE)
    clear()
    print("Bienvenido Usuario.")

    while True:
        print(f"Conectado...\nSERVER: {SERVER} - DATABASE: {DATABASE} - TABLE: {TABLE}.")
        print(" 1-Añadir.\n 2-Leer.\n 3-Actualizar.\n 4-Eliminar.\n 5-Salir.")
        opc = input('¿Qué acción desea realizar?: ')
        if not opc.isdigit() or int(opc) < 1 or int(opc) > 5:
            print("Ingrese lo pedido, intente nuevamente. Gracias...")
            input("Presione enter para continuar...")
            clear()
            continue

        opc=int(opc)

        match opc:
            case 1:
                clear()
                print('----Añadir Estudiante----')

                studentID=int(input('Ingrese el ID del Estudiante: '))
                nombre=input("Ingrese Nombre: ")
                apellido=input('Ingrese Apellido: ')
                fechaNac=input('Ingrese Fecha de Nacimiento (AÑO-MES-DIA): ')

                student = {
                    'EstudianteID' : studentID,
                    'Nombre' : nombre,
                    'Apellido' : apellido,
                    'FechaNacimiento' : fechaNac
                }

                r = CRUD.anadir(student, cntion)
                if(r):
                    print('El Estudiante ha sido Registrado exitosamente!')
                    input("Presione enter para continuar...")
                    clear()

            case 2:
                clear()
                print("----Leer Estudiantes----")
                studentID = input('Ingrese el ID del Estudiante que desea leer: ')
                r = CRUD.leer(studentID, cntion)
                if r:
                    print(f" ID: {r[0]} \n Nombre: {r[1]}\n Apellido: {r[2]}\n Fecha de Nacimiento: {r[3]}")
                    print('El Estudiante ha sido Leido exitosamente!') 
                    input("Presione enter para continuar...")
                    clear()
                else:
                    print('Estudiante no encontrado...')
                    input('Presione Enter para continuar...')
                    # print(CRUD.leer(cntion))
  
            case 3:
                clear()
                print('-------Actualizar-------')
                studentID = int(input("Ingrese el ID del estudiante a actualizar: "))
                r = CRUD.actualizar(studentID, cntion)
                if (r):
                    print('El Estudiante ha sido Actualizado exitosamente!')
                    input("Presione enter para continuar...")
                    clear()
            case 4:
                clear()
                print('---------Eliminar-------')
                studentID=input('Ingrese el ID del Estudiante:')
                r= CRUD.eliminar(studentID, cntion)
                if (r):
                    print('El Estudiante ha sido Eliminado exitosamente!')
                    input("Presione enter para continuar...")
                    clear()
            case 5:
                print('Hasta pronto! Cuidese.')
                input('Presione Enter para continuar...')
                r = connection.cerrar_conexion(cntion)     
                clear()
                exit()

if __name__ == '__main__':
    main()

