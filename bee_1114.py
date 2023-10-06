while True:
    senha = "2002"
    senha_recebida = input()

    if senha_recebida == senha:
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")
