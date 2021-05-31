from ClaseIGerente import IGerente
from ClaseITesorero import ITesorero
from ClaseManejadorEmpleados import ManejadorEmpleados
from ClaseEmpleado import Empleado
def tesorero(manejarTesorero):
    print("Tesorero, Acceder a gastos de la empresa en concepto de sueldos")
    dni= int(input('Ingrese el DNI: '))
    manejarTesorero.gastosSueldoPorEmpleado(dni)
def gerente(manejarGerente):
    while True:
        print("_____MENU DE OPCIONES PARA GERENTE_____")
        print("[1]...Modificar sueldo basico de empleado de planta")
        print("[2]...Modificar viatico de empleado externo")
        print("[3]...Modificar valor por hora de los empleados contratados")
        print("[0]...Salir")
        try:
            op= int(input('Seleccione una opcion: '))
            if op in range(4):
                if op == 1:
                    dni= int(input("Ingresa el DNI del empleado: "))
                    nuevoBasico= int(input("Ingrese el nuevo sueldo basico del empleado: "))
                    manejarGerente.modificarBasicoEPlanta(dni,nuevoBasico)
                if op == 2:
                    dni= int(input("Ingresa el DNI del empleado: "))
                    nuevoViatico= int(input('Ingrese el nuevo monto viatico del empleado: '))
                    manejarGerente.modificarViaticoEExterno(dni,nuevoViatico)
                if op == 3:
                    nuevoValorHora= int(input('Ingrese el nuevo valor por hora del empleado: '))
                    manejarGerente.modificarValorEPorHora(0,nuevoValorHora)
                if op == 0:
                    print("_____MENU FINALIZADO_____")
                    break
            else:
                print("ERROR, solo puede ingresar numeros del 0 al 3")
        except ValueError:
            print("ERROR, ingrese solamente numeros")
def testInterface(Empleados):
    usuario= input('Usuario: ')
    clave= input('Clave: ')
    if (usuario.lower() == 'Gerente'.lower())and(clave == 'uGerente/ufC77#!1'):
        gerente(IGerente(Empleados))
    elif (usuario.lower() == 'Tesorero'.lower())and(clave == 'uTesoreso/ag@74ck'):
        tesorero(ITesorero(Empleados))
    else:
        print("Usuario y/o contraseña incorrectos")
if __name__=='__main__':
    dimension= int(input('Ingrese la dimension del arreglo de Empleados: '))
    Empleados= ManejadorEmpleados(dimension,5)
    Empleados.leerPlantas()
    Empleados.leerContratados()
    Empleados.leerExternos()
    while True:
        print("_____MENU DE OPCIONES_____")
        print("[1]...Registrar Horas")
        print("[2]...Total de Tarea")
        print("[3]...Ayuda Solidaria")
        print("[4]...Calcular Sueldo")
        print("[5]...Tesorero/Gerente")
        print("[0]...Salir")
        try:
            op= int(input('Seleccione una opcion: '))
            if op in range(6):
                if op == 1:
                    Empleados.incrementarHoras()
                if op == 2:
                    Empleados.TotalTarea()
                if op == 3:
                    Empleados.Ayuda()
                if op == 4:
                    Empleados.CalcularSueldo()
                if op == 5:
                    testInterface(Empleados)
                if op == 0:
                    print("_____MENU FINALIZADO_____")
                    break
            else:
                print("ERROR, solo puede seleccionar numeros del 0 al 5")
        except ValueError:
            print("ERROR, ingrese solamente numeros")
