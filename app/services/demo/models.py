from typing import List

from pydantic import BaseModel, Field


class Medico(BaseModel):
    idmedico: int = Field(examples=[1, 2, 3, 999])
    nombre: str = Field(examples=['John'])
    apellidos: str = Field(examples=['Doe'])
    ruc: str = Field(examples=['0102030405001'])
    direccion: str = Field(examples=['Av de las americas'])
    correo: str = Field(examples=['correo@correo.com'])
    telefono: str = Field(examples=['099216548'])
    id_ciudad: str = Field(examples=['01_AZ'])


ObtenerMedicosResponse = List[Medico]
