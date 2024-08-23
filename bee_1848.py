gritos = 0
soma = 0

while gritos < 3:
    mensagem_corvo = input()

    if mensagem_corvo != "caw caw":
        soma += int(mensagem_corvo.replace('-', '0').replace('*', '1'), 2)
    else:
        print(soma)
        gritos += 1
        soma = 0
