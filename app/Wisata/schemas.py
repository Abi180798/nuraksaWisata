from app.schemas import BaseModel, BaseResponse, ListMeta, Field
from typing import List, Optional

class WisataModel(BaseModel):
  id_wisata: Optional[int]=Field(description="user id generate by server")
  nama_wisata: str = Field(description="wisata name")
  alamat_wisata: str = Field(description="wisata address")
  deskripsi_wisata: Optional[str] = Field(description="wisata description")
  gambar_wisata: Optional[str] = Field(description="wisata_photo")
  kategori: str = Field(description="wisata kategori")
  latitude: float = Field(description="wisata latitude")
  longitude: float = Field(description="wisata longitude")

  class Config:
    orm_mode=True

class WisataResponse(BaseResponse):
  data: WisataModel = None

class WisatasResponse(BaseResponse):
  data: List[WisataModel] = []
  meta: ListMeta = ListMeta()