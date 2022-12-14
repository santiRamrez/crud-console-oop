class Comuna:
  __listaComuna = []
  def __init__(self, idComuna="", descripcionComuna=""):
        self.__idComuna = idComuna
        self.__descripcionComuna = descripcionComuna

  def __str__(self):
        return f'\nId: {self.__idComuna} - Descripción: {self.__descripcionComuna}'

# ---- Getters ----

  def getListaComuna(self):
      return self.__listaComuna
  
  def getIdComuna(self):
      return self.__idComuna

  def getDescripcionComuna(self):
      return self.__descripcionComuna

# ---- Setters ----

  def setIdComuna(self, a):
       self.__idComuna = a

  def setDescripcionComuna(self, a):
       self.__descripcionComuna = a

  # ---- Methods ----

  def addComuna(self, a):
      self.getListaComuna().append(a)
      