from sqlalchemy.orm import Session
from models import Usuario, Categoria, Producto, Venta, DetalleVenta
from schemas import UsuarioCreate, CategoriaCreate, ProductoCreate, VentaCreate, DetalleVentaCreate

# Usuarios
def create_usuario(db: Session, usuario: UsuarioCreate):
    db_usuario = Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def get_usuario(db: Session, id_usuario: int):
    return db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()

def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Usuario).offset(skip).limit(limit).all()

def update_usuario(db: Session, id_usuario: int, usuario: UsuarioCreate):
    db_usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
    if db_usuario:
        for key, value in usuario.dict().items():
            setattr(db_usuario, key, value)
        db.commit()
        db.refresh(db_usuario)
    return db_usuario

def delete_usuario(db: Session, id_usuario: int):
    db_usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
    return db_usuario

# Categorías
def create_categoria(db: Session, categoria: CategoriaCreate):
    db_categoria = Categoria(**categoria.dict())
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def get_categoria(db: Session, id_categoria: int):
    return db.query(Categoria).filter(Categoria.id_categoria == id_categoria).first()

def get_categorias(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Categoria).offset(skip).limit(limit).all()

def update_categoria(db: Session, id_categoria: int, categoria: CategoriaCreate):
    db_categoria = db.query(Categoria).filter(Categoria.id_categoria == id_categoria).first()
    if db_categoria:
        for key, value in categoria.dict().items():
            setattr(db_categoria, key, value)
        db.commit()
        db.refresh(db_categoria)
    return db_categoria

def delete_categoria(db: Session, id_categoria: int):
    db_categoria = db.query(Categoria).filter(Categoria.id_categoria == id_categoria).first()
    if db_categoria:
        db.delete(db_categoria)
        db.commit()
    return db_categoria

# Productos
def create_producto(db: Session, producto: ProductoCreate):
    db_producto = Producto(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def get_producto(db: Session, id_producto: int):
    return db.query(Producto).filter(Producto.id_producto == id_producto).first()

def get_productos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Producto).offset(skip).limit(limit).all()

def update_producto(db: Session, id_producto: int, producto: ProductoCreate):
    db_producto = db.query(Producto).filter(Producto.id_producto == id_producto).first()
    if db_producto:
        for key, value in producto.dict().items():
            setattr(db_producto, key, value)
        db.commit()
        db.refresh(db_producto)
    return db_producto

def delete_producto(db: Session, id_producto: int):
    db_producto = db.query(Producto).filter(Producto.id_producto == id_producto).first()
    if db_producto:
        db.delete(db_producto)
        db.commit()
    return db_producto

# Ventas
def create_venta(db: Session, venta: VentaCreate):
    db_venta = Venta(**venta.dict())
    db.add(db_venta)
    db.commit()
    db.refresh(db_venta)
    return db_venta

def get_venta(db: Session, id_venta: int):
    return db.query(Venta).filter(Venta.id_venta == id_venta).first()

def get_ventas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Venta).offset(skip).limit(limit).all()

def update_venta(db: Session, id_venta: int, venta: VentaCreate):
    db_venta = db.query(Venta).filter(Venta.id_venta == id_venta).first()
    if db_venta:
        for key, value in venta.dict().items():
            setattr(db_venta, key, value)
        db.commit()
        db.refresh(db_venta)
    return db_venta

def delete_venta(db: Session, id_venta: int):
    db_venta = db.query(Venta).filter(Venta.id_venta == id_venta).first()
    if db_venta:
        db.delete(db_venta)
        db.commit()
    return db_venta

# Detalle Venta
def create_detalle_venta(db: Session, detalle_venta: DetalleVentaCreate):
    db_detalle = DetalleVenta(**detalle_venta.dict())
    db.add(db_detalle)
    db.commit()
    db.refresh(db_detalle)
    return db_detalle

def get_detalle_venta(db: Session, id_detalle: int):
    return db.query(DetalleVenta).filter(DetalleVenta.id_detalle == id_detalle).first()

def get_detalles_venta(db: Session, skip: int = 0, limit: int = 100):
    return db.query(DetalleVenta).offset(skip).limit(limit).all()

def update_detalle_venta(db: Session, id_detalle: int, detalle_venta: DetalleVentaCreate):
    db_detalle = db.query(DetalleVenta).filter(DetalleVenta.id_detalle == id_detalle).first()
    if db_detalle:
        for key, value in detalle_venta.dict().items():
            setattr(db_detalle, key, value)
        db.commit()
        db.refresh(db_detalle)
    return db_detalle

def delete_detalle_venta(db: Session, id_detalle: int):
    db_detalle = db.query(DetalleVenta).filter(DetalleVenta.id_detalle == id_detalle).first()
    if db_detalle:
        db.delete(db_detalle)
        db.commit()
    return db_detalle
