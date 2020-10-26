from fastapi import APIRouter, Depends, File, UploadFile
from app.response import *
from .views import WisataViewControl
from .models import Wisata,session
from .schemas import *
from app.Auth.auth import get_current_superadmin, get_current_admin

import os, io, cv2
from starlette.responses import StreamingResponse

ALOWRD_FILE = ['png', 'jpg', 'jpeg']
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FOTO_DIR = os.path.join(BASE_DIR, "images")

wisataRouter = APIRouter()
viewControl = WisataViewControl()

@wisataRouter.post("/",status_code=status.HTTP_201_CREATED,response_model=WisataResponse)
async def post(
  res:Response,
  wisata:WisataModel,
  authorized = Depends(get_current_admin)
  ):
  return httpResponse(viewControl.post,res=res,wisata=wisata) 

@wisataRouter.get("/",status_code=status.HTTP_200_OK,response_model=WisatasResponse)
async def get(
  res:Response
  ):
  return httpResponse(viewControl.get,res=res) 

@wisataRouter.get("/{id}",status_code=status.HTTP_200_OK,response_model=WisataResponse)
async def getById(
  res:Response,
  id:int
  ):
  return httpResponse(viewControl.getSingle,res=res,id=id) 

@wisataRouter.put("/{id}",status_code=status.HTTP_200_OK,response_model=WisataResponse)
async def updateById(
  res:Response,
  id:int,
  wisata:WisataModel,
  authorized = Depends(get_current_admin),
  ):
  return httpResponse(viewControl.update,res=res,id=id,wisata=wisata) 

@wisataRouter.delete("/{id}",status_code=status.HTTP_200_OK,response_model=WisataResponse)
async def deleteById(
  res:Response,
  id:int,
  authorized = Depends(get_current_admin)
  ):
  return httpResponse(viewControl.delete,res=res,id=id) 


@wisataRouter.post("/wisatas/photo", status_code=status.HTTP_201_CREATED, response_model=WisataResponse)
async def uploadPhoto( 
    res : Response,
    id : int,
    photo :UploadFile = File(...)
    ):
    response = WisataResponse()
    wisata : Wisata = Wisata.getWisataBy(Wisata.id_wisata==id)
    print(wisata)
    if wisata is None:
        return response.notfound()
    # photo.file.
    try:
        img_path = os.path.join(FOTO_DIR, photo.filename)
        file_format = img_path.split(".")[1]
        if not file_format in ALOWRD_FILE:
            res.status_code = status.HTTP_400_BAD_REQUEST
            response.badrequest()
            return response
        with open(img_path, 'wb') as f:
            [f.write(chunk) for chunk in iter(lambda: photo.file.read(10000), b'')]

        wisata.gambar_wisata = photo.filename
        session.commit()
        response.created()
        response.data = wisata
        return response
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="internal server error")

@wisataRouter.get("/wisatas/photo/{photo_name}", status_code = status.HTTP_200_OK)
async def getPhot(
    res : Response,
    photo_name : str
    ):
    try:
        image = cv2.imread(os.path.join(FOTO_DIR, photo_name))
        if image is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="image not found")
        file_format = photo_name.split(".")[1]
        res, img = cv2.imencode(".{}".format(file_format), image)
        return StreamingResponse(io.BytesIO(img.tobytes()), media_type="image/{}".format(file_format))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))