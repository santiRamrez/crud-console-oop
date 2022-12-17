from modelo.cargo import Cargo
from dao.dao_cargo import DaoCargo

# ---- Data Transfer Object ---> to the DAO ----
class CargoDTO:

  # ---- Methods ----

  def addCargo(self, id, description):
        daocargo = DaoCargo()
        resultado = daocargo.addCargo(Cargo(idCargo=id, descripcionCargo=description))
        return resultado

  def findCargo(self, id):
        daocargo = DaoCargo()
        res = daocargo.findCargo(Cargo(idCargo=id))
        return True if res is not None else None

  def updateCargo(self, id, description):
        daocargo = DaoCargo()
        res = daocargo.updateCargo(Cargo(idCargo=id, descripcionCargo=description))
        return res

  def delCargo(self, id):
        daocargo = DaoCargo()
        res = daocargo.delCargo(Cargo(idCargo=id))
        return True if res is not None else None

  def findAllCargo(self):
        daocargo = DaoCargo()
        res = daocargo.findAllCargo()
        return res

  def getRecordByName(self, name):
        daocargo = DaoCargo()
        res = daocargo.getRecordByName(Cargo(descripcionCargo=name))
        return res

  def getRecordByID(self, id):
        daocargo = DaoCargo()
        res = daocargo.getRecordByID(id)
        return res

