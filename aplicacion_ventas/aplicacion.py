from modelos import Producto, Cliente
from pedido import Factura
from descuentos import DescuentoVIP, DescuentoVolumen
from impuestos import IVA, Excentos

cliente = Cliente(123, "Juan", False)
producto1 = Producto(567, "arepas", "alimentos", 2000)
producto2 = Producto(949, "Suscripción Netflix", "Servicio", 25000)
producto3 = Producto(111, "Computador", "Tecnologia", 2000000)

miFactura = Factura(cliente)

miFactura.agregar_linea(producto1, 11)

descuento_a_aplicar = DescuentoVolumen()
impuesto_a_aplicar = IVA()

print(miFactura.calcular_total(descuento_a_aplicar, impuesto_a_aplicar))
