while True:
    try:
        alfabeto = input()
        n = int(input())
        lampadas = map(int, input().split())

        frase_formada = ''.join(alfabeto[i - 1] for i in lampadas)

        print(frase_formada)

    except EOFError:
        break