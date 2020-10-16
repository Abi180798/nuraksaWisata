from fastapi import APIRouter
from app.response import *
from .views import WisataViewControl
from .schemas import *

wisataRouter = APIRouter()
viewControl = WisataViewControl()

@wisataRouter.post("/",status_code=status.HTTP_201_CREATED,response_model=WisataResponse)
async def post(
  res:Response,
  wisata:WisataModel
  ):
  return httpResponse(viewControl.post,res=res,wisata=wisata) 

@wisataRouter.get("/",status_code=status.HTTP_200_OK,response_model=WisatasResponse)
async def get(
  res:Response,
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
  wisata:WisataModel
  ):
  return httpResponse(viewControl.update,res=res,id=id,wisata=wisata) 

@wisataRouter.delete("/{id}",status_code=status.HTTP_200_OK,response_model=WisataResponse)
async def deleteById(
  res:Response,
  id:int,
  ):
  return httpResponse(viewControl.delete,res=res,id=id) 