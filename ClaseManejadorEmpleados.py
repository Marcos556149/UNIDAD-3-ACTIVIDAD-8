import csv
import numpy as np
from zope.interface import implementer
from datetime import datetime
from ClaseEmpleado import Empleado
from ClaseEmpleadoContratado import EmpleadoContratado
from ClaseEmpleadoPlanta import EmpleadoPlanta
from ClaseEmpleadoExterno import EmpleadoExterno
from ClaseIGerente import IGerente
from ClaseITesorero import ITesorero
@implementer(IGerente)
@implementer(ITesorero)
class ManejadorEmpleados:
    __cantidad= 0
    __dimension= 0
    __incremento= 5
    __arregloEmpleados= None
    def __init__(self,dim,incr=5):
        self.__arregloEmpleados= np.empty(dim,dtype=Empleado)
        self.__dimension= dim
        self.__cantidad= 0
        self.__incremento= incr
    def MostrarTodo(self):
        for Empleado in self.__arregloEmpleados:
            print(Empleado)
    def agregarEmpleado(self,empleadoNuevo):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arregloEmpleados.resize(self.__dimension)
        self.__arregloEmpleados[self.__cantidad]= empleadoNuevo
        self.__cantidad += 1
    def leerPlantas(self):
        archivo1= open('planta.csv')
        reader= csv.reader(archivo1,delimiter=',')
        for fila in reader:
            dn= int(fila[0])
            nom= fila[1]
            dir= fila[2]
            tel= fila[3]
            suel= int(fila[4])
            anti= int(fila[5])
            nuevoPlanta= EmpleadoPlanta(dn,nom,dir,tel,suel,anti)
            self.agregarEmpleado(nuevoPlanta)
        archivo1.close()
    def leerContratados(self):
        archivo2= open('contratados.csv')
        reader= csv.reader(archivo2,delimiter=',')
        for fila in reader:
            dn= int(fila[0])
            nom= fila[1]
            dir= fila[2]
            tel= fila[3]
            fechaI= fila[4]
            fechaF= fila[5]
            cantH= int(fila[6])
            nuevoContratado= EmpleadoContratado(dn,nom,dir,tel,fechaI,fechaF,cantH)
            self.agregarEmpleado(nuevoContratado)
        archivo2.close()
    def leerExternos(self):
        archivo3= open('externos.csv')
        reader= csv.reader(archivo3,delimiter=',')
        for fila in reader:
            dn= int(fila[0])
            nom= fila[1]
            dir= fila[2]
            tel= fila[3]
            tar= fila[4]
            fechaII= fila[5]
            fechaFF= fila[6]
            montoV= int(fila[7])
            cost= int(fila[8])
            montoS= int(fila[9])
            nuevoExterno= EmpleadoExterno(dn,nom,dir,tel,tar,fechaII,fechaFF,montoV,cost,montoS)
            self.agregarEmpleado(nuevoExterno)
        archivo3.close()
    def incrementarHoras(self):
        dni= int(input("Ingrese el DNI de un empleado: "))
        horasHoy= int(input('Ingrese la cantidad de horas trabajadas hoy del empleado: '))
        i= 0
        bandera= False
        while (bandera == False)and(i < self.__cantidad):
            if dni == self.__arregloEmpleados[i].getDNI():
                bandera= True
                if (isinstance(self.__arregloEmpleados[i],EmpleadoContratado)):
                    self.__arregloEmpleados[i].sumarHora(horasHoy)
                    print("LAS HORAS QUE EL EMPLEADO TRABAJO HOY FUERON AUMENTADAS EXITOSAMENTE")
                else:
                    print("ERROR, el DNI ingresado no corresponde con un empleado contratado")
            i += 1
        if bandera == False:
            print("ERROR, el DNI ingresado no corresponde con ningun empleado")
    def TotalTarea(self):
        tareaa= input("Ingrese tarea, las tareas disponibles son: carpinteria, electricidad, plomeria: ")
        Total= 0
        if (tareaa.lower() == 'carpinteria')or(tareaa.lower() == 'electricidad')or(tareaa.lower() == 'plomeria'):
            for p in range(self.__cantidad):
                if (isinstance(self.__arregloEmpleados[p],EmpleadoExterno)):
                    if (tareaa.lower() == self.__arregloEmpleados[p].getTarea())and(datetime.now() < datetime.strptime(self.__arregloEmpleados[p].getFechaF(),'%Y-%m-%d')):
                        Total += self.__arregloEmpleados[p].getSueldo()
            print("El monto a pagar para la tarea {} es: {}".format(tareaa.lower(),Total))
        else:
            print("ERROR, La tarea ingresada no corresponde con ninguna tarea disponible")
    def Ayuda(self):
        print("EMPLEADOS A LOS QUE LE CORRESPONDE LA AYUDA")
        for j in range(self.__cantidad):
            if self.__arregloEmpleados[j].getSueldo() < 25000:
                print("Nombre: {}, Direccion: {}, DNI: {}".format(self.__arregloEmpleados[j].getNombre(),self.__arregloEmpleados[j].getDireccion(),self.__arregloEmpleados[j].getDNI()))
    def CalcularSueldo(self):
        print("NOMBRE, TELEFONO Y SUELDO A COBRAR DE TODOS LOS EMPLEADOS")
        for k in range(self.__cantidad):
            print("Nombre: {}, Telefono: {}, Sueldo: {}".format(self.__arregloEmpleados[k].getNombre(),self.__arregloEmpleados[k].getTelefono(),self.__arregloEmpleados[k].getSueldo()))
    def modificarBasicoEPlanta(self,dni,nuevoBasico):
        i= 0
        bandera= False
        while (bandera == False)and(i < self.__cantidad):
            if dni == self.__arregloEmpleados[i].getDNI():
                bandera= True
                if isinstance(self.__arregloEmpleados[i],EmpleadoPlanta):
                    self.__arregloEmpleados[i].setSueldoBasico(nuevoBasico)
                    print("SUELDO BASICO MODIFICADO")
                else:
                    print("ERROR, el DNI ingresado no corresponde con un empleado contratado")
            i += 1
        if bandera == False:
            print("ERROR, el DNI ingresado no corresponde con ningun empleado")
    def modificarViaticoEExterno(self,dni,nuevoViatico):
        i= 0
        bandera= False
        while (bandera == False)and(i < self.__cantidad):
            if dni == self.__arregloEmpleados[i].getDNI():
                bandera = True
                if isinstance(self.__arregloEmpleados[i],EmpleadoExterno):
                    self.__arregloEmpleados[i].setMontoViatico(nuevoViatico)
                    print("MONTO VIATICO MODIFICADO")
                else:
                    print("ERROR, el DNI ingresado no corresponde con un empleado externo")
            i += 1
        if bandera == False:
            print("ERROR, el DNI ingresado no corresponde con ningun empleado")
    def modificarValorEPorHora(self,dni,nuevoValorHora):
        print("Valor por Hora antes de ser modificado: {}".format(EmpleadoContratado.getValorPorHora()))
        EmpleadoContratado.setValorPorHora(nuevoValorHora)
        print("Valor por Hora luego de ser modificado: {}".format(EmpleadoContratado.getValorPorHora()))
    def gastosSueldoPorEmpleado(self,dni):
        bandera= False
        i= 0
        while (bandera == False)and(i < self.__cantidad):
            if dni == self.__arregloEmpleados[i].getDNI():
                print("El gasto de sueldos para el empleado con dni {} es: {}".format(dni,self.__arregloEmpleados[i].getSueldo()))
                bandera= True
            i += 1
        if bandera == False:
            print("ERROR, El DNI ingresado no corresponde con ningun empleado")
