from .models import Wisata
from .schemas import WisataModel, WisataResponse, WisatasResponse

class WisataViewControl:

  def post(self, wisata : WisataModel):
    response = WisataResponse()
    response.badrequest()
    response.data = Wisata.addNewWisata(wisata)
    response.created()
    return response

  def get(self):
    response = WisatasResponse()
    response.badrequest()
    response.data = Wisata.getWisata()
    response.success()
    return response

  def getSingle(self, id):
    response = WisataResponse()
    response.notfound()
    wisata = Wisata.getWisataBy(Wisata.id_wisata==id)
    if wisata is not None:
      response.data=wisata
      response.success()
    return response

  def update(self, wisata: WisataModel,id):
    response = WisataResponse()
    response.notfound()
    wisata = Wisata.update(wisata, id)
    if wisata is not None:
      response.data = wisata
      response.success()
    return response

  def delete(self, id):
    response = WisataResponse()
    response.notfound()
    wisata = Wisata.delete(id)
    if wisata == True:
      response.success()
      response.message="success delete data"
    return response
      