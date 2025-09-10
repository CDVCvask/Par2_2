class Pedido:
    def __init__(self, codigo, cliente,producto,cantidad,prioridad):
        self.codigo = codigo
        self.cliente = cliente
        self.producto = producto
        self.cantidad = cantidad
        self.prioridad = prioridad
class See_Pedido:
    def __init__(self):
        pedidos = {}
class Menu:
    def principal(self):
        print("Bienvenido a la cafeteria bing bong")
        print("1.Realizar pedido")
        print("2.Ver pedidos")
        print("3.Salir")
contP = 0
see_p = See_Pedido()
menus = Menu()
while 0 != 1:
    try:
        menus.principal()
    except ValueError:
        print("El tipo de dato ingresado no es valido")