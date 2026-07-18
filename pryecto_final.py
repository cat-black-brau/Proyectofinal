citas= []
def agregarcita():
    print('Nombre del paciente')
    nombre_paciente = input()
    print('Telefno: ')
    telefono = input()
    print('Fecha de la cita')
    print('(dd/mm/aaaa)')
    fecha= input()
    print('Hora (hh/mm)')
    hora= input()
    print('Motivio de la consulta')
    motivo= input()
    print('Doctor asiganado')
    doctor= input()
    print('Observaciones: ')
    observaciones= input()
    id_cita = len(citas) + 1
    cita= { 'id': id_cita ,'nombre': nombre_paciente, 'telefono': telefono, 'fecha': fecha, 'hora':hora, 'motivo':motivo, 'doctor':doctor, 'observaciones':observaciones, 'estado': 'pendiente'}
    citas.append(cita)
    print(' Cita agregada correctamente')
    regresar_menu()


def ver_cita():
    if len(citas) == 0:
        print('NO hay citas registradas')
    else:
        for cita in citas:
            print(f"ID: {cita['id']}")
            print(f"Paciente: {cita['nombre']}")
            print(f"Telefono: {cita['telefono']}")
            print(f"Fecha: {cita['fecha']}")
            print(f"Hora: {cita['hora']}")
            print(f"Motivo:{cita['motivo']}")
            print(f"Doctor: {cita['doctor']}")
            print(f"Observaciones:{cita['observaciones']}")
            print(f"Estado: {cita['estado']}")
            print("*"*30)
    regresar_menu()

def modificar_cita():
    print("Ingrese el ID de la cita: ")
    id_bucar =int(input())
    for cita in citas:
        if cita['id'] == id_bucar:
            print('¿Que deseas modificar?')
            print('1.Fecha')
            print("2. Hora")
            print("3. Doctor")
            print("4. Estado")
            print('selecciona una opcion')
            opcion = int(input())
            match opcion:
                case 1 :
                    print('Integrese la nueva fecha')
                    print('(dd/mm/aaaa)')
                    nueva_fecha = input() 
                    cita['fecha'] = nueva_fecha
                case 2: 
                    print ('Ingrese el( nuevo horario')
                    print('(hh/mm)')
                    nueva_hora = input()
                    cita['hora']= nueva_hora
                case 3:
                    print ('¿A qué médico desea reasignar el caso?') 
                    nuevo_doctor= input()
                    cita['doctor'] = nuevo_doctor
                case 4:
                    print('¿Cual sera el nuevo esta de la cita?')

                    print('1. pendiente')
                    print('2. Realizado')
                    print('3. cancelada')

                    print('selecciona una opcion')
                    estado = int(input())
                    match estado:
                        case 1:
                            cita['estado'] = "Pendiente"
                        case 2: 
                            cita ['estado'] = "Realizado"
                        case 3:
                            cita['estado'] = "Cancelado"
                        case _:
                            print('Opcion no valida')
                case _:
                    print('opcion no valida')
            print('Cita modificada correctamente')
            return    
    print('No se encontro una cita con ese ID')
    regresar_menu()
  

def regresar_menu ():
   VERDADERO  = 'SI'
   FALSO = 'NO'
   print( '¿Quieres realizar algo mas ?')
   print('responde SI o NO')
   respuesta = input()

   if respuesta == VERDADERO:
      print('okey.... seguimos operando')
      menu_opciones()
   elif respuesta== FALSO:
      print('Ten un exelente dia :D')
   else:
      print('Ingresa una respuesta valida ')   
      regresar_menu()    


def menu_opciones():
    print('¿Que le gustaria realizar el dia de hoy? ')
    print('1. Agregar una cita')
    print('2. Modificar una cita')
    print('3. Ver citas pendientes')

    print('seleciona una opcion')
    opcion = int(input())
    match opcion:
        case 1:
            agregarcita()
        case 2:
            modificar_cita()
        case 3:
            ver_cita()
        case 4:
            print('salir')
        case _:
            print('Esa opcion no exixte') 

print('Bienvedio')
print('ingrese el usuario')
usuario = input()
print('Ingrese la contraseña')
contrasenia = input()
 
USUARIO = "RECEPCION" 
PASSWORD = "1234"

#comprobscion del usurio y contrasenia 
if usuario == USUARIO and contrasenia == PASSWORD:
    print(f'Bienvedio {usuario}')
    print("*"*30)
    menu_opciones()
else: 
    print('***ERROR***')
    print('Intenta denuevo')
