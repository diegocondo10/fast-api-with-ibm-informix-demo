from pydantic import BaseModel


class MedicoIn(BaseModel):
    nombres: str
    apellidos: str
    ruc: str
    id_ciudad: int
