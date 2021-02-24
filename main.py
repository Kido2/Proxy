from decorators import suma_fake, consulta_continente
from factory import Factory


@suma_fake
def suma(num):
    return 2 + num


@consulta_continente
def alerta_continente(continente=None):
    return "Continente no soportado :("


print(alerta_continente("americas"))
print("*********************")

print(suma(3))

print("*********************")
object_factory = Factory("Products").get_instance()
print(object_factory().get_name())
