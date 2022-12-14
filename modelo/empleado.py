class Empleado:
  __listaComunas = []  
  __listaCargos = []  
  def __init__(self, runEmpleado=None, nombreEmpleado=None, apellidoEmpleado=None, cargo=None, direccionEmpleado=None, claveEmpleado=None, correoEmpleado=None, comuna=None):
        self.__runEmpleado = runEmpleado
        self.__nombreEmpleado = nombreEmpleado
        self.__apellidoEmpleado = apellidoEmpleado
        self.__cargo = cargo
        self.__direccionEmpleado = direccionEmpleado
        self.__claveEmpleado = claveEmpleado
        self.__correoEmpleado = correoEmpleado
        self.__comuna = comuna


  def __str__(self):
        return f'''\nNombre: {self.__nombreEmpleado} {self.__apellidoEmpleado} - {self.__runEmpleado} 
Cargo: {self.__cargo} - Dirección: {self.__direccionEmpleado} 
Correo: {self.__correoEmpleado} - Comuna: {self.__comuna}\n'''

#  ------ Getters  ---------
  def getRunEmpleado(self):
      return self.__runEmpleado

  def getNombreEmpleado(self):
      return self.__nombreEmpleado

  def getApellidoEmpleado(self):
      return self.__apellidoEmpleado

  def getCargo(self):
      return self.__cargo

  def getDireccionEmpleado(self):
      return self.__direccionEmpleado
  
  def getClaveEmpleado(self):
      return self.__claveEmpleado 

  def getCorreoEmpleado(self):
      return self.__correoEmpleado 

  def getComuna(self):
      return self.__comuna 

  def getListaComuna(self):
    return self.__listaComunas    

  def getListaCargos(self):
    return self.__listaCargos   

#  ------ Setters  ---------
  def setRunEmpleado(self, a):
      self.__runEmpleado = a

  def setNombreEmpleado(self, a):
      self.__nombreEmpleado = a

  def setApellidoEmpleado(self, a):
       self.__apellidoEmpleado = a

  def setCargo(self, a):
       self.__cargo = a

  def setDireccionEmpleado(self, a):
       self.__direccionEmpleado = a
  
  def setClaveEmpleado(self, a):
       self.__claveEmpleado = a

  def setCorreoEmpleado(self, a):
       self.__correoEmpleado = a

  def setComuna(self, a):
       self.__comuna = a

#  ------ Methods  ---------

 

