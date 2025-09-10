class Pedido:
    def __init__(self, codigo, cliente,producto,cantidad,prioridad):
        self.codigo = codigo
        self.cliente = cliente
        self.producto = producto
        self.cantidad = cantidad
        self.prioridad = prioridad
class See_Pedido:
    def __init__(self):
        self.pedidos = {}
        self.Load_Pedidos()
    def Agregar_pedido(self,pedido):
        self.pedidos[pedido.codigo] = {'Cliente':pedido.cliente,'Producto':pedido.producto,'Cantidad':pedido.cantidad,'Prioridad':pedido.prioridad}
    def Mostrar_pedidos(self):
        cont = 1
        for code,value in self.pedidos.items():
            print(f"Pedido {cont}")
            print(f"Codigo: {code}--Cliente: {value['Cliente']}--Producto: {value['Producto']}--Cantidad: {value['Cantidad']}--Prioridad: {value['Prioridad']}")
            print(" ")
            cont += 1
    def Save_Pedidos(self):
        with open("pedidos.log.txt", "w") as file:
            for code,value in self.pedidos.items():
                            file.write(f"{code}:{value['Cliente']}:{value['Producto']}:{value['Cantidad']}:{value['Prioridad']}\n")
    def Load_Pedidos(self):
        try:
            with open("pedidos.log.txt","r") as file:
                for line in file:
                    (codigo,clientes,productos,cantidad,prioridad) = line.split(":")
                    self.pedidos[codigo] = {'Cliente':clientes,'Producto':productos,'Cantidad':cantidad,'Prioridad':prioridad}
        except FileNotFoundError:
            print("No existe el archivo pedidos.log.txt")
class Notification:
    def Urgente(self,pedidos):
        ur = 0
        for code,value in pedidos.items():
            if value['Prioridad'] == "Urgente":
                ur = ur + 1
        print(f"Hay {ur} pedidos urgentes")
        cont = 1
        for code,value in pedidos.items():
            if value['Prioridad'] == "Urgente":
                print(f"Pedido Urgente {cont}")
                print(f"Codigo: {code}--Cliente: {value['Cliente']}--Producto: {value['Producto']}--Cantidad: {value['Cantidad']}--Prioridad: {value['Prioridad']}")
                print(" ")
                cont += 1
class Menu:
    def principal(self):
        print("Bienvenido a la cafeteria bing bong")
        print("1.Realizar pedido")
        print("2.Ver pedidos")
        print("3.Salir")
class Codes:
    def __init__(self):
        self.cont_p = 0
        self.Load_codes()
    def Save_codes(self,pedidos):
        with open("codigos.txt","w") as file:
            file.write(f"{pedidos}:{0}\n")
    def Load_codes(self):
        try:
            with open("codigos.txt","r") as file:
                for line in file:
                    (Cont_p,cont) = line.split(":")
                    self.cont_p = int(Cont_p)
        except FileNotFoundError:
            print("No existe el archivo codigos.txt")
    def Get_cont_p(self):
        return self.cont_p
codes = Codes()
contP = codes.Get_cont_p()
see_p = See_Pedido()
menus = Menu()
out = 0
noti = Notification()
noti.Urgente(see_p.pedidos)
while 0 != 1:
    try:
        menus.principal()
        opt = input("Ingrese la opción que desee: ")
        match opt:
            case "1":
                cont = 1
                while 0 != 1:
                    print(" ")
                    print(f"Datos del pedido {cont}")
                    print(" ")
                    code_p = f"P{contP}"
                    name = input("Ingrese el nombre del cliente(Ingrese el código para salir): ")
                    if name.strip() == "":
                        print("No puede dejar este espacio vacío")
                    elif name == "OURO":
                        print("Regresando al menú principal")
                        print(" ")
                        break
                    else:
                        product = input("Ingrese el producto: ")
                        if product.strip() == "":
                            print("No puede dejar este espacio vacío")
                        else:
                            num = int(input("Ingrese la cantidad del producto: "))
                            if num <=0 or num > 1000:
                                print("La cantidad ingresada no es valida")
                            else:
                                urgent = input("El pedido es Normal o Urgente?(Para normal ingrese N para Urgente ingrese U): ")
                                if urgent.upper() == "N":
                                    urgent = "Normal"
                                    new_pedido = Pedido(code_p,name,product,num,urgent)
                                    see_p.Agregar_pedido(new_pedido)
                                    contP += 1
                                    cont = cont + 1
                                elif urgent.upper() == "U":
                                    urgent = "Urgente"
                                    new_pedido = Pedido(code_p, name, product, num, urgent)
                                    see_p.Agregar_pedido(new_pedido)
                                    contP += 1
                                    cont = cont + 1
                                else:
                                    print("El tipo de pedido ingresado no es valido")
            case "2":
                see_p.Mostrar_pedidos()
            case "3":
                print("Gracias por utilizar el programa")
                out = 1
    except ValueError:
        print("El tipo de dato ingresado no es valido")
    if out == 1:
        see_p.Save_Pedidos()
        codes.Save_codes(contP)
        break