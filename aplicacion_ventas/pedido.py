from dataclasses import dataclass, field 
from typing import List 
from modelos import Cliente, LineaFactura, Producto
from descuentos import Descuento
from impuestos import Impuestos

@dataclass
class Factura: 
    cliente: Cliente
    lineas: List[LineaFactura] = field(default_factory=list)
    
    def agregar_linea(self, producto: Producto, cantidad = 1):
        self.lineas.append(LineaFactura(producto, cantidad))

    def calcular_descuentos(self, descuento: Descuento):
        return sum(descuento.aplicar(self.cliente, 1)for l in self.lineas)

    def calcular_impuestos(self, impuestos: Impuestos):
        return sum(impuestos.aplicar(self.cliente, 1)for l in self.lineas)
    
    def calcular_total(self, impuestos: Impuestos, descuento: Descuento):
        return sum(l.subtotal for l in self. lineas) + self.calcular_impuestos(impuestos) - self.calcular_descuentos(descuento)