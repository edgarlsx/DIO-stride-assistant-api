from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from app.utils import generate_stride_analysis

app = FastAPI(
    title="STRIDE Threat Analysis API",
    description="Análise automática de ameaças usando Azure OpenAI e imagens de arquitetura.",
    version="1.0.0"
)

# Libera o CORS (útil para front-ends)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    response = generate_stride_analysis(image_bytes)
    return response
