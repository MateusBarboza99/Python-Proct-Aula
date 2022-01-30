from Dicionarios.Funcoes import *

usuários = {}
opcao = perguntar()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L" :
    if opcao=="I":
        inserir(usuários)
    opcao = perguntar()