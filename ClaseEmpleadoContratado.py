from ClaseEmpleado import Empleado
class EmpleadoContratado(Empleado):
    ValorPorHora= 300
    __fechaInicio= None
    __fechaFinalizacion= None
    __cantHoras= 0
    @classmethod
    def getValorPorHora(cls):
        return cls.ValorPorHora
    @classmethod
    def setValorPorHora(cls,nuevoValorHora):
        cls.ValorPorHora= nuevoValorHora
    def __init__(self,dn='',nom='',dir='',tel='',fechaI=None,fechaF=None,cantH=0):
        super().__init__(dn,nom,dir,tel)
        self.__fechaInicio= fechaI
        self.__fechaFinalizacion= fechaF
        self.__cantHoras= cantH
    def __str__(self):
        return 'CONTRATADO\nDNI: {}, Nombre: {}, Direccion: {}, Telefono: {},Fecha Inicio: {},Fecha Fin: {},Cant H: {}'.format(super().getDNI(),super().getNombre(),super().getDireccion(),super().getTelefono(),self.__fechaInicio,self.__fechaFinalizacion,self.__cantHoras)
    def getSueldo(self):
        return self.__cantHoras * self.getValorPorHora()
    def sumarHora(self,horasHoy):
        self.__cantHoras += horasHoy
