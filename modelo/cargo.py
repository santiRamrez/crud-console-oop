class Cargo:
  __listaCargo = []
  def __init__(self, idCargo="", descripcionCargo=""):
        self.__idCargo = idCargo
        self.__descripcionCargo = descripcionCargo

  def __str__(self):
        return f'\nId: {self.__idCargo} - Descripción: {self.__descripcionCargo}'

# ---- Getters ----
  def getListaCargo(self):
      return self.__listaCargo
 
  def getIdCargo(self):
      return self.__idCargo

  def getDescripcionCargo(self):
      return self.__descripcionCargo

# ---- Setters ----

  def setIdCargo(self, a):
      self.__idCargo = a
 
  def setDescripcionCargo(self, a):
       self.__descripcionCargo = a

# ---- Methods ----

  def addCargo(self, a):
      self.getListaCargo().append(a)


      

