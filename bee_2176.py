mensagem = input()

if mensagem.count('1') % 2 == 0:
    mensagem = mensagem + '0'
else:
    mensagem = mensagem + '1'

print(mensagem)