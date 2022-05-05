import platform
import getpass
from datetime import datetime

print("Nome do Computador..................: ", platform.node())
print("Arquitetura.........................: ", platform.architecture())
print("Sistema Operacional:..................", platform.system())
print("Versap do So:.........................", platform.release())
print("Processador.........................: ", platform.processor())
print("Versão do Python....................: ", platform.python_version())

print (datetime.now() .month)

usuario = getpass.getuser()
senha = getpass.getpass("Digite sua senha:...")

if usuario == "Matheus" and senha == "hello":
    print("Bem-Vindo Matheus")
else:
    print("Voce nao tem acesso")
