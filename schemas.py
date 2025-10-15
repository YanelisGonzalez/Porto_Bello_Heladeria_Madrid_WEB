from pydantic import BaseModel, EmailStr

class FormularioCreate(BaseModel):
    nombre: str
    apellidos: str
    telefono: str
    email: EmailStr
    pais: str
    ciudad: str
    cp: str
    comentario: str
