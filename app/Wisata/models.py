from sqlalchemy import *

from database import session,Base

from .schemas import WisataModel

class Wisata(Base):
  __tablename__= "wisata"
  id_wisata= Column(Integer, primary_key=True, index=True)
  nama_wisata= Column(String, nullable=False, default="")
  alamat_wisata= Column(String, default="")
  deskripsi_wisata = Column(Text, default="")
  gambar_wisata = Column(String, default="")
  kategori = Column(String, nullable=False, default="")
  latitude = Column(Float, nullable=False, default=0)
  longitude = Column(Float, nullable=False, default=0)

  @staticmethod
  def fromModel(wisata : WisataModel):
    return Wisata(
      nama_wisata = wisata.nama_wisata,
      alamat_wisata = wisata.alamat_wisata,
      deskripsi_wisata = wisata.deskripsi_wisata,
      gambar_wisata = wisata.gambar_wisata,
      kategori = wisata.kategori,
      latitude = wisata.latitude,
      longitude = wisata.longitude
    )

  @staticmethod
  def addNewWisata(wisata : WisataModel):
    newWisata = Wisata.fromModel(wisata)
    session.add(newWisata)
    session.commit()
    return newWisata

  @staticmethod
  def getWisata():
    return session.query(Wisata).all()

  @staticmethod
  def getWisataBy(*args, **kwargs):
    return session.query(Wisata).filter(*args, **kwargs).first()

  def setNamaWisata(self,newName):
    if newName is not None and newName:
      self.nama_wisata=newName

  def setAlamatWisata(self,newAlamat):
    if newAlamat is not None and newAlamat:
      self.alamat_wisata=newAlamat

  def setDeskripsiWisata(self,newDeskripsi):
    if newDeskripsi is not None and newDeskripsi:
      self.deskripsi_wisata=newDeskripsi

  def setGambarWisata(self,newGambar):
    if newGambar is not None and newGambar:
      self.gambar_wisata=newGambar

  def setKategoriWisata(self,newKategori):
    if newKategori is not None and newKategori:
      self.kategori=newKategori

  def setLatitudeWisata(self,newLatitude):
    if newLatitude is not None:
      self.latitude=newLatitude

  def setLongitudeWisata(self,newLongitude):
    if newLongitude is not None:
      self.longitude=newLongitude

  @staticmethod
  def update(wisata:WisataModel,id):
    old_wisata : Wisata=Wisata.getWisataBy(Wisata.id_wisata==id)
    if old_wisata is not None:
      old_wisata.setNamaWisata(wisata.nama_wisata)
      old_wisata.setAlamatWisata(wisata.alamat_wisata)
      old_wisata.setDeskripsiWisata(wisata.deskripsi_wisata)
      old_wisata.setGambarWisata(wisata.gambar_wisata)
      old_wisata.setKategoriWisata(wisata.kategori)
      old_wisata.setLatitudeWisata(wisata.latitude)
      old_wisata.setLongitudeWisata(wisata.longitude)
      session.commit()
    return old_wisata

  @staticmethod
  def delete(id):
    wisata: Wisata = Wisata.getWisataBy(Wisata.id_wisata==id)
    if wisata is not None:
      session.delete(wisata)
      session.commit()
      return True
    return wisata


