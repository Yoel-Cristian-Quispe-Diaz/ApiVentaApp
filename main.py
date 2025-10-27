from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud
import schemas
from database import SessionLocal, engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Usuarios Endpoints
@app.post("/usuarios/", response_model=schemas.Usuario)
def create_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    return crud.create_usuario(db, usuario)

@app.get("/usuarios/{id_usuario}", response_model=schemas.Usuario)
def read_usuario(id_usuario: int, db: Session = Depends(get_db)):
    db_usuario = crud.get_usuario(db, id_usuario)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario not found")
    return db_usuario

@app.get("/usuarios/", response_model=List[schemas.Usuario])
def read_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    usuarios = crud.get_usuarios(db, skip, limit)
    return usuarios

@app.put("/usuarios/{id_usuario}", response_model=schemas.Usuario)
def update_usuario(id_usuario: int, usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = crud.update_usuario(db, id_usuario, usuario)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario not found")
    return db_usuario

@app.delete("/usuarios/{id_usuario}", response_model=schemas.Usuario)
def delete_usuario(id_usuario: int, db: Session = Depends(get_db)):
    db_usuario = crud.delete_usuario(db, id_usuario)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario not found")
    return db_usuario

# Categorías Endpoints
@app.post("/categorias/", response_model=schemas.Categoria)
def create_categoria(categoria: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    return crud.create_categoria(db, categoria)

@app.get("/categorias/{id_categoria}", response_model=schemas.Categoria)
def read_categoria(id_categoria: int, db: Session = Depends(get_db)):
    db_categoria = crud.get_categoria(db, id_categoria)
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoria not found")
    return db_categoria

@app.get("/categorias/", response_model=List[schemas.Categoria])
def read_categorias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categorias = crud.get_categorias(db, skip, limit)
    return categorias

@app.put("/categorias/{id_categoria}", response_model=schemas.Categoria)
def update_categoria(id_categoria: int, categoria: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    db_categoria = crud.update_categoria(db, id_categoria, categoria)
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoria not found")
    return db_categoria

@app.delete("/categorias/{id_categoria}", response_model=schemas.Categoria)
def delete_categoria(id_categoria: int, db: Session = Depends(get_db)):
    db_categoria = crud.delete_categoria(db, id_categoria)
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoria not found")
    return db_categoria

# Productos Endpoints
@app.post("/productos/", response_model=schemas.Producto)
def create_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return crud.create_producto(db, producto)

@app.get("/productos/{id_producto}", response_model=schemas.Producto)
def read_producto(id_producto: int, db: Session = Depends(get_db)):
    db_producto = crud.get_producto(db, id_producto)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto not found")
    return db_producto

@app.get("/productos/", response_model=List[schemas.Producto])
def read_productos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    productos = crud.get_productos(db, skip, limit)
    return productos

@app.put("/productos/{id_producto}", response_model=schemas.Producto)
def update_producto(id_producto: int, producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    db_producto = crud.update_producto(db, id_producto, producto)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto not found")
    return db_producto

@app.delete("/productos/{id_producto}", response_model=schemas.Producto)
def delete_producto(id_producto: int, db: Session = Depends(get_db)):
    db_producto = crud.delete_producto(db, id_producto)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto not found")
    return db_producto

# Ventas Endpoints
@app.post("/ventas/", response_model=schemas.Venta)
def create_venta(venta: schemas.VentaCreate, db: Session = Depends(get_db)):
    return crud.create_venta(db, venta)

@app.get("/ventas/{id_venta}", response_model=schemas.Venta)
def read_venta(id_venta: int, db: Session = Depends(get_db)):
    db_venta = crud.get_venta(db, id_venta)
    if db_venta is None:
        raise HTTPException(status_code=404, detail="Venta not found")
    return db_venta

@app.get("/ventas/", response_model=List[schemas.Venta])
def read_ventas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    ventas = crud.get_ventas(db, skip, limit)
    return ventas

@app.put("/ventas/{id_venta}", response_model=schemas.Venta)
def update_venta(id_venta: int, venta: schemas.VentaCreate, db: Session = Depends(get_db)):
    db_venta = crud.update_venta(db, id_venta, venta)
    if db_venta is None:
        raise HTTPException(status_code=404, detail="Venta not found")
    return db_venta

@app.delete("/ventas/{id_venta}", response_model=schemas.Venta)
def delete_venta(id_venta: int, db: Session = Depends(get_db)):
    db_venta = crud.delete_venta(db, id_venta)
    if db_venta is None:
        raise HTTPException(status_code=404, detail="Venta not found")
    return db_venta

# Detalle Venta Endpoints
@app.post("/detalle_venta/", response_model=schemas.DetalleVenta)
def create_detalle_venta(detalle_venta: schemas.DetalleVentaCreate, db: Session = Depends(get_db)):
    return crud.create_detalle_venta(db, detalle_venta)

@app.get("/detalle_venta/{id_detalle}", response_model=schemas.DetalleVenta)
def read_detalle_venta(id_detalle: int, db: Session = Depends(get_db)):
    db_detalle = crud.get_detalle_venta(db, id_detalle)
    if db_detalle is None:
        raise HTTPException(status_code=404, detail="Detalle Venta not found")
    return db_detalle

@app.get("/detalle_venta/", response_model=List[schemas.DetalleVenta])
def read_detalles_venta(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    detalles = crud.get_detalles_venta(db, skip, limit)
    return detalles

@app.put("/detalle_venta/{id_detalle}", response_model=schemas.DetalleVenta)
def update_detalle_venta(id_detalle: int, detalle_venta: schemas.DetalleVentaCreate, db: Session = Depends(get_db)):
    db_detalle = crud.update_detalle_venta(db, id_detalle, detalle_venta)
    if db_detalle is None:
        raise HTTPException(status_code=404, detail="Detalle Venta not found")
    return db_detalle

@app.delete("/detalle_venta/{id_detalle}", response_model=schemas.DetalleVenta)
def delete_detalle_venta(id_detalle: int, db: Session = Depends(get_db)):
    db_detalle = crud.delete_detalle_venta(db, id_detalle)
    if db_detalle is None:
        raise HTTPException(status_code=404, detail="Detalle Venta not found")
    return db_detalle
