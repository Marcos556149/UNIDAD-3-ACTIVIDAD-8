from ClaseEmpleado import Empleado
class EmpleadoPlanta(Empleado):
    __sueldo= 0.0
    __antiguedad= 0
    def __init__(self,dn='',nom='',dir='',tel='',suel=0.0,anti=0):
        super().__init__(dn,nom,dir,tel)
        self.__sueldo= suel
        self.__antiguedad= anti
    def __str__(self):
        return 'PLANTA\nDNI: {}, Nombre: {}, Direccion: {}, Telefono: {},Sueldo: {},Antiguedad: {}'.format(super().getDNI(),super().getNombre(),super().getDireccion(),super().getTelefono(),self.__sueldo,self.__antiguedad)
    def setSueldoBasico(self,nuevoBasico):
        self.__sueldo= nuevoBasico
    def getSueldo(self):
        return int(self.__sueldo + ((self.__sueldo * 0.01)*self.__antiguedad))
