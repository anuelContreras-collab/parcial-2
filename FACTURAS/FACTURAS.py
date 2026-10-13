# Esta clase solo se encarga de guardar y calcular los datos de la factura
class Factura:
    def __init__(self, items):
        self.items = items

    def calcular_subtotal(self):
        return sum(item['precio'] * item['cantidad'] for item in self.items)

# Esta clase se encarga únicamente de enviar los correos
class ServicioCorreo:
    def enviar_correo(self, destinatario, mensaje):
        print(f"Enviando correo a {destinatario}: {mensaje}")

# Esta clase junta todo de forma ordenada
class ProcesadorFactura:
    def __init__(self, servicio_correo):
        self.servicio_correo = servicio_correo

    def procesar(self, factura):
        total = factura.calcular_subtotal()
        self.servicio_correo.enviar_correo("cliente@email.com", f"Tu total es {total}")
        return total