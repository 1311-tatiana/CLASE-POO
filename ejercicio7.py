from abc import ABC, abstractmethod

class MedioComunicacion(ABC):

    @abstractmethod
    def enviar_mensaje(self, mensaje):
          ...

class CorreoElectronico(MedioComunicacion):
        def enviar_mensaje(self, mensaje):
              print("Mensaje enviado por correo electronico:", mensaje)

class SMS(MedioComunicacion):
    def enviar_mensaje(self, mensaje):
            print("Mensaje enviado por SMS:", mensaje)

class Push(MedioComunicacion):
    def enviar_mensaje(self, mensaje):
            print("Mensaje enviado por notificacion al celular:", mensaje)

class FactoryMedios:
      
      @staticmethod
      def crear_medio(tipo):
            if tipo == "correo":
                  return CorreoElectronico()
            elif tipo == "sms":
                    return SMS()
            elif tipo == "push":
                  return Push()
            else:
                raise ValueError("Medio de comunicacion no existe")
            
class GestorEnvios:
    def __init__(self, tipos):
            self.tipos = [FactoryMedios.crear_medio (t) for t in tipos]

    def enviar_mensajes(self, mensaje):
          for t in self.tipos:
                t.enviar_mensaje(mensaje)

gestor = GestorEnvios(["correo", "sms", "push"])
gestor.enviar_mensajes("Hola")