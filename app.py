from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()



class Curso(BaseModel):
    id: int
    nombre: str
    descripcion: Optional[str] = None

cursos_db = [
    Curso(id=1, nombre="Introducción a DevOps", descripcion="Conceptos básicos de integración y despliegue continuo"),
    Curso(id=2, nombre="Seguridad en Docker", descripcion="Buenas prácticas para asegurar contenedores y pipelines")
]

@app.get("/cursos", response_model=List[Curso])
async def get_cursos():
    return cursos_db

@app.post("/cursos", response_model=Curso)
async def create_curso(curso: Curso):
    cursos_db.append(curso)
    return curso

@app.get("/cursos/{curso_id}", response_model=Curso)
async def get_curso(curso_id: int):
    for curso in cursos_db:
        if curso.id == curso_id:
            return curso
    raise HTTPException(status_code=404, detail="Curso no encontrado")

@app.put("/cursos/{curso_id}", response_model=Curso)
async def update_curso(curso_id: int, updated_curso: Curso):
    for i, curso in enumerate(cursos_db):
        if curso.id == curso_id:
            cursos_db[i] = updated_curso
            return updated_curso
    raise HTTPException(status_code=404, detail="Curso no encontrado")

@app.delete("/cursos/{curso_id}")
async def delete_curso(curso_id: int):
    for i, curso in enumerate(cursos_db):
        if curso.id == curso_id:
            del cursos_db[i]
            return {"message": "Curso eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Curso no encontrado")


