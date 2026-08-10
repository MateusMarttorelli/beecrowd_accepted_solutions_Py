renas = ("Dasher", "Dancer", "Prancer", "Vixen", "Comet", "Cupid", "Donner", "Blitzen", "Rudolph")

bolas_de_neve = map(int, input().split())
total = sum(bolas_de_neve)

print(renas[(total % 9) - 1])



