class TV:
    _numTV=0
    def __init__(self,marca,estado):
        self._marca = marca
        self._estado = estado
        self._control = None
        self._precio = 500
        self._canal = 1
        self._volumen = 1
        TV._numTV += 1
    
    def setMarca(self,marca):
        self._marca = marca
    
    def getMarca(self):
        return self._marca
    
    def turnOn(self):
        if(self._estado == False):
            self._estado = True
    
    def turnOff(self):
        if(self._estado == True):
            self._estado == False

    def getEstado(self):
        return self._estado
    
    def volumenUp(self):
        if(self._estado == True and self._volumen < 7 ):
            self._volumen += 1
    
    def volumenDown(self):
        if(self._estado == True and self._volumen > 0):
            self._volumen -= 1
    
    def setVolumen(self,numero):
        if(self._estado == True and 0 <= numero and numero <= 7):
            self._volumen = numero 

    def getVolumen(self):
        return self._volumen
    
    def canalUp(self):
        if(self._estado == True and self._canal < 120):
            self._canal += 1
    
    def canalDown(self):
        if(self._estado == True and self._canal > 1):
            self._canal -= 1
    
    def setCanal(self,numero):
        if(self._estado == True and 1 <= numero and numero <= 120):
            self._canal = numero
        
    def getCanal(self):
        return self._canal
    
    def setControl(self,control):
        self._control = control
    
    def getControl(self):
        return self._control
    
    def setPrecio(self,precio):
        self._precio = precio
    
    def getPrecio(self):
        return self._precio
    
    @classmethod
    def setNumTV(cls,numero):
        cls._numTV = numero

    @classmethod
    def getNumTV(cls):
        return cls._numTV