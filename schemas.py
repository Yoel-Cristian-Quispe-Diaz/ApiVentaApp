from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

# Usuarios
class UsuarioBase(BaseModel):
    nombre: str
    correo: EmailStr
    contraseña: str
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    rol: str = "cliente"

class UsuarioCreate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    id_usuario: int

    class Config:
        from_attributes = True

# Categorías
class CategoriaBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None

class CategoriaCreate(CategoriaBase):
    pass

class Categoria(CategoriaBase):
    id_categoria: int

    class Config:
        from_attributes = True

# Productos
class ProductoBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float = Field(ge=0)
    stock: int = Field(ge=0)
    id_categoria: Optional[int] = None
    imagen: Optional[str] = None

class ProductoCreate(ProductoBase):
    pass

class Producto(ProductoBase):
    id_producto: int

    class Config:
        from_attributes = True

# Ventas
class VentaBase(BaseModel):
    id_usuario: Optional[int] = None
    total: float = Field(ge=0)
    metodo_pago: str

class VentaCreate(VentaBase):
    pass

class Venta(VentaBase):
    id_venta: int
    fecha: datetime

    class Config:
        from_attributes = True

# Detalle Venta
class DetalleVentaBase(BaseModel):
    id_venta: int
    id_producto: int
    cantidad: int = Field(gt=0)
    precio_unitario: float = Field(ge=0)

class DetalleVentaCreate(DetalleVentaBase):
    pass

class DetalleVenta(DetalleVentaBase):
    id_detalle: int
    subtotal: float

    class Config:
        from_attributes = True
