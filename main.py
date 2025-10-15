from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
import os
from pydantic import BaseModel, EmailStr
import smtplib
from email.message import EmailMessage
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from email.mime.text import MIMEText
from dotenv import load_dotenv


# Cargar variables de entorno
load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))  
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


app = FastAPI()

# Carpeta FRONTEND relativa a main.py en BACKEND
frontend_path = os.path.join(os.path.dirname(__file__), "..", "FRONTEND")

# Montar la carpeta FRONTEND como /static
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

# Configurar templates para HTML
templates = Jinja2Templates(directory=os.path.join(frontend_path, "HTML"))

# Rutas para cada página
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("CABECERA.HTML", {"request": request})

@app.get("/NOSOTROS")
def nosotros(request: Request):
    return templates.TemplateResponse("NOSOTROS.HTML", {"request": request})

@app.get("/PRODUCTOS")
def productos(request: Request):
    return templates.TemplateResponse("PRODUCTOS.HTML", {"request": request})

@app.get("/CONTACTAR")
def contactar(request: Request):
    return templates.TemplateResponse("CONTACTAR.HTML", {"request": request})

@app.get("/DOMICILIO")
def domicilio(request: Request):
    return templates.TemplateResponse("DOMICILIO.HTML", {"request": request})

@app.get("/HORARIOS")
def horarios(request: Request):
    return templates.TemplateResponse("HORARIOS.HTML", {"request": request})


# Configuración de CORS (por si el frontend está en otro dominio)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringirlo a tu dominio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint que recibe los datos del formulario
@app.post("/enviar-formulario", response_class=HTMLResponse)
async def enviar_formulario(
    nombre_completo: str = Form(...),
    apellidos: str = Form(...),
    telefono: str = Form(...),
    correo_electronico: EmailStr = Form(...),
    pais: str = Form(...),
    ciudad: str = Form(...),
    CP: str = Form(None),
    heladerias_favoritas: str = Form(None),
    comentario: str = Form(None)
):
    
# --- 1. Guardar datos en base de datos (puedes agregarlo después) ---
    
# --- 2. Preparar mensaje ---
        mensaje = f"""
        Nuevo mensaje recibido:
        Nombre: {nombre_completo} {apellidos}
        Teléfono: {telefono}
        Correo: {correo_electronico}
        País: {pais}
        Ciudad: {ciudad}
        Código Postal: {CP or '-'}
        Heladerías Favoritas: {heladerias_favoritas or '-'}
        Comentario: {comentario or '-'}
        """

# -----3. Enviar correo----
        try:
            msg = MIMEText(mensaje)
            msg["Subject"] = "Nuevo formulario recibido"
            msg["From"] = os.getenv("SMTP_USER")
            msg["To"] = os.getenv("SMTP_USER")

            #Conexión SMTP

            with smtplib.SMTP(os.getenv("SMTP_SERVER"), int(os.getenv("SMTP_PORT"))) as server:
                server.starttls()
                server.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASSWORD"))
                server.send_message(msg)

        except Exception as e:
            return HTMLResponse (f"<h2>Error al enviar correo: {e}</h2>", status_code=500) 

    # --- 3. Respuesta al usuario ---
        return HTMLResponse(f"<h2>Gracias {nombre_completo}, por contactar con Heladería Porto Bello Madrid. En breve atenderemos su mensaje.</h2>")
        
   
