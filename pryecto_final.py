citas= []
def agregarcita():
    meses=[]
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


def ver_cita():
    if len(citas) == 0:
        print('NO hay citas registradas')
    else:
        for i, cita in enumerate(citas, start = 1):
            print(f"Cita {i}")
            print(f"Paciente: {cita['nombre']}")
            print(f"Telefono: {cita['telefono']}")
            print(f"Fecha: {cita['fecha']}")
            print(f"Hora: {cita['hora']}")\
            print('*'*

def regresar_menu ():
   VERDADERO  = 'SI'
   FALSO = 'NO'
   print( 'Quieres realizar algo mas ?')
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
    print('Que le gustaria realizar el dia de hoy? ')
    print('1. Agregar una cita')
    print('2. Modificar una cita')
    print('3. Ver citas pendientes')

    print('seleciona una opcion')
    opcion = int(input())
    match opcion:
        case 1:
            agregarcita()
        case 2:
            print('Modificar una cita')
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


