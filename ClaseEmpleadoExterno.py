from ClaseEmpleado import Empleado
class EmpleadoExterno(Empleado):
    __tarea= ''
    __fechaInicioo= None
    __fechaFinalizacionn= None
    __montoViatico= 0.0
    __costoObra= 0.0
    __montoSeguroDeVida= 0.0
    def __init__(self,dn='',nom='',dir='',tel='',tar='',fechaII=None,fechaFF=None,montoV=0.0,cost=0.0,montoS=0.0):
        super().__init__(dn,nom,dir,tel)
        self.__tarea= tar
        self.__fechaInicioo= fechaII
        self.__fechaFinalizacionn= fechaFF
        self.__montoViatico= montoV
        self.__costoObra= cost
        self.__montoSeguroDeVida= montoS
    def __str__(self):
        return 'EXTERNO\nDNI: {}, Nombre: {}, Direccion: {}, Telefono: {},Tarea: {},Fecha Inicio: {},Fecha Fin: {},Monto V: {},Costo Obra: {},Monto S: {}'.format(super().getDNI(),super().getNombre(),super().getDireccion(),super().getTelefono(),self.__tarea,self.__fechaInicioo,self.__fechaFinalizacionn,self.__montoViatico,self.__costoObra,self.__montoSeguroDeVida)
    def setMontoViatico(self,nuevoViatico):
        self.__montoViatico = nuevoViatico
    def getSueldo(self):
        return self.__costoObra - self.__montoViatico - self.__montoSeguroDeVida
    def getFechaF(self):
        return self.__fechaFinalizacionn
    def getTarea(self):
        return self.__tarea
