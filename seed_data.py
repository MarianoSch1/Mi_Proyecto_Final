from ejemplo.models import Familiar

Familiar(nombre="Ana", direccion="Juramento 3045", numero_pasaporte=123123).save()
Familiar(nombre="Victor", direccion=" Campana 2001", numero_pasaporte=890890).save()
Familiar(nombre="Saul", direccion="Angel Gallardo 75", numero_pasaporte=345345).save()
Familiar(nombre="Felipe", direccion="Campana 3045", numero_pasaporte=567567).save()

print("Se cargo con éxito los usuarios de pruebas")