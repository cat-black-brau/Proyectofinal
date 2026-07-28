# Lista principal donde se almacenan todas las citas
citas= []
from datetime import datetime


# Guarda todas las citas registradas en el archivo citas.txt
# para conservar la informacion aunque se cierre el programa
def guardar_citas():
    with open("citas.txt", "w", encoding="utf-8") as archivo:
        for cita in citas:
            linea = f"{cita['id']}|{cita['nombre']}|{cita['telefono']}|{cita['fecha']}|{cita['hora']}|{cita['motivo']}|{cita['doctor']}|{cita['observaciones']}|{cita['estado']}\n"
            archivo.write(linea)


# Carga las citas almacenadas en el archivo citas.txt
# y las guarda nuevamente en la lista citas al iniciar el sistem
def cargar_citas():
    global citas
    citas = []
    try:
        with open("citas.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                datos = linea.split("|")
                cita = {
                    "id": int(datos[0]),
                    "nombre": datos[1],
                    "telefono": datos[2],
                    "fecha": datos[3],
                    "hora": datos[4],
                    "motivo": datos[5],
                    "doctor": datos[6],
                    "observaciones": datos[7],
                    "estado": datos[8]
                }
                citas.append(cita)
    except FileNotFoundError:
        citas = []


# Permite registrar una nueva cita medica
# Solicita los datos del paciente, valida la fecha y hora,
# genera un ID automatico y guarda la informacion
def agregarcita():
    print('Nombre del paciente')
    nombre_paciente = input()
    print('Telefono:')
    telefono = input()
    # Verifica que la fecha y hora ingresadas no sean anteriores
    # a la fecha y hora actual del sistema
    while True:
        print('Fecha de la cita')
        print('(dd/mm/aaaa)')
        fecha = input()
        print('Hora')
        print('(hh:mm)')
        hora = input()
        try:
            fecha_hora = fecha + " " + hora
            cita_datetime = datetime.strptime(fecha_hora,"%d/%m/%Y %H:%M")
            if cita_datetime < datetime.now():
                print('No se puede registrar una cita en una fecha u hora pasada')
                print('Intente nuevamente')
                continue
            break
        except ValueError:
            print('Formato de fecha u hora incorrecto')
            print('Intente nuevamente')
    print('Motivo de la consulta')
    motivo = input()
    print('Doctor asignado')
    doctor = input()
    print('Observaciones:')
    observaciones = input()
    if len(citas) == 0:
        id_cita = 1   # Genera un ID automatico para identificar cada cita
    else:
        id_cita = citas[-1]['id'] + 1
    # Agrega la cita a la lista principal
    cita = {
        'id': id_cita,
        'nombre': nombre_paciente,
        'telefono': telefono,
        'fecha': fecha,
        'hora': hora,
        'motivo': motivo,
        'doctor': doctor,
        'observaciones': observaciones,
        'estado': 'Pendiente'}
    # Guarda los cambios en el archivo de texto
    citas.append(cita)
    guardar_citas()
    print('*'*30)
    print('Cita agregada correctamente')


# Muestra todas las citas registradas junto con su informacion
# completa en pantalla
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


# Permite modificar una cita existente usando su ID
# Se puede cambiar la fecha, hora, doctor o estado
def modificar_cita():
    print("Ingrese el ID de la cita: ")
    id_bucar =int(input())        
    for cita in citas:           
        if cita['id'] == id_bucar:  # Busca la cita correspondiente al ID ingresado
            print('¿Que deseas modificar?')
            print('1.Fecha')
            print("2. Hora")
            print("3. Doctor")
            print("4. Estado")
            print('selecciona una opcion')
            opcion = int(input())
            match opcion:      # Actualiza la informacion seleccionada por el usuario
                case 1 :
                    print('Integrese la nueva fecha')
                    print('(dd/mm/aaaa)')
                    nueva_fecha = input()      # Guarda los cambios realizados
                    cita['fecha'] = nueva_fecha
                    print('*'*30)     
                case 2: 
                    print ('Ingrese el( nuevo horario')
                    print('(hh/mm)')
                    nueva_hora = input()   # Guarda los cambios realizados
                    cita['hora']= nueva_hora
                    print('*'*30)
                case 3:
                    print ('¿A qué médico desea reasignar el caso?') 
                    nuevo_doctor= input()
                    cita['doctor'] = nuevo_doctor # Guarda los cambios realizados
                    print('*'*30)
                case 4:
                    print('¿Cual sera el nuevo esta de la cita?')

                    print('1. pendiente')
                    print('2. Realizado')
                    print('3. cancelada')

                    print('selecciona una opcion')
                    estado = int(input())  # Guarda los cambios realizados
                    match estado:
                        case 1: 
                            cita['estado'] = "Pendiente"  # Guarda los cambios realizados
                        case 2: 
                            cita ['estado'] = "Realizado" # Guarda los cambios realizados
                        case 3:
                            cita['estado'] = "Cancelado" # Guarda los cambios realizados
                        case _:
                            print('Opcion no valida')
                case _:
                    print('opcion no valida')
            guardar_citas()
            print('*'*30)
            print('Cita modificada correctamente')
            return    
    print('*'*30)
    print('No se encontro una cita con ese ID')
    regresar_menu()


# Busca una cita especifica mediante su ID y muestra toda la informacion relacionada
def buscar_cita():
    print('*'*30)
    print('Ingrese el ID de la cita')

    id_buscar = int(input())

    for cita in citas:

        if cita['id'] == id_buscar:

            print(f"ID: {cita['id']}")
            print(f"Paciente: {cita['nombre']}")
            print(f"Telefono: {cita['telefono']}")
            print(f"Fecha: {cita['fecha']}")
            print(f"Hora: {cita['hora']}")
            print(f"Doctor: {cita['doctor']}")
            print(f"Estado: {cita['estado']}")

            return
    print('*'*30)
    print('No se encontro una cita con ese ID')


# Muestra la cantidad total de citas registradas en el sistema
def total_citas():
    print('*'*30)
    print('TOTAL DE CITAS REGISTRADAS')
    print(len(citas))


# Genera un reporte con la cantidad de citas
# pendientes, realizadas y canceladas
def reporte_estados():
    print('*'*30)
    pendientes = 0
    realizadas = 0
    canceladas = 0

    for cita in citas:
        
        estado = cita['estado'].lower()

        if estado == 'pendiente':
              pendientes += 1

        elif estado == 'realizado':
             realizadas += 1

        elif estado == 'cancelado':
             canceladas += 1
 
    print(f'Pendientes: {pendientes}')
    print(f'Realizadas: {realizadas}')
    print(f'Canceladas: {canceladas}')


# Muestra el menu de reportes disponibles para el usuario
def reportes():

    print('1. Total de citas')
    print('2. Reporte de estados')

    opcion = int(input())

    match opcion:

        case 1:
            print('*'*30)
            total_citas()
            print('*'*30)

        case 2:
            print('*'*30)
            reporte_estados()
            print('*'*30)

        case _:
            print('*'*30)
            print('Opcion no valida')
            print('*'*30)


# Funcion recursiva que pregunta al usuario si desea
# continuar utilizando el sistema
# Si la respuesta es invalida vuelve a llamarse a si misma
def regresar_menu ():
   print('*'*30)
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
      # Llamada recursiva para solicitar nuevamente
      # una respuesta valida   
      regresar_menu()    


# Menu principal del sistema
# Permite acceder a todas las funcionalidades
# disponibles para la gestion de citas
def menu_opciones():
    cargar_citas()
    print('¿Que le gustaria realizar el dia de hoy? ')
    print('1. Agregar una cita')
    print('2. Modificar una cita')
    print('3. Ver citas')
    print('4. Buscar cita')
    print('5. Reportes')
    print('6. Salir') 

    print('seleciona una opcion')
    opcion = int(input())
    match opcion:
        case 1:
           print('*'*30)
           agregarcita()
           regresar_menu ()

        case 2:
          print('*'*30)
          modificar_cita()
          regresar_menu()

        case 3:
         print('*'*30)
         ver_cita()
         regresar_menu()

        case 4:
         print('*'*30)
         buscar_cita()
         regresar_menu()

        case 5:
          print('*'*30)
          reportes()
          regresar_menu()

        case 6:
          print('*'*30)
          print('Gracias por usar el sistema')

# Credenciales de acceso al sistema
USUARIO = "RECEPCION" 
PASSWORD = "1234"

print('*'*30)
print('Bienvenido')
print('*'*30)


# Verifica que el usuario y contraseña sean correctos
# antes de permitir el acceso al sistema
while True:    
    print("Ingrese el usuario")
    usuario = input()

    print("Ingrese la contraseña")
    contrasenia = input()

    if usuario == USUARIO and contrasenia == PASSWORD:
        print(f"Bienvenido {usuario}")
        menu_opciones()
        break  # <- sale del ciclo
    else:
        print("*** ERROR ***")
        print("Intenta de nuevo")