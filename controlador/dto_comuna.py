from modelo.comuna import Comuna
from dao.dao_comuna import DaoComuna

# ---- Data Transfer Object ---> to the DAO ----
class ComunaDTO:

  # ---- Methods ----

  def addComuna(self, id, description):
        daocomuna = DaoComuna()
        resultado = daocomuna.addComuna(Comuna(idComuna=id, descripcionComuna=description))
        return resultado

  def findComuna(self, id):
        daocomuna = DaoComuna()
        res = daocomuna.findComuna(Comuna(idComuna=id))
        return True if res is not None else None

  def updateComuna(self, id, description):
        daocomuna = DaoComuna()
        res = daocomuna.updateComuna(Comuna(idComuna=id, descripcionComuna=description))
        return res

  def delComuna(self, id):
        daocomuna = DaoComuna()
        res = daocomuna.delComuna(Comuna(idComuna=id))
        return True if res is not None else None

  def findAllComuna(self):
        daocomuna = DaoComuna()
        res = daocomuna.findAllComuna()
        return res
