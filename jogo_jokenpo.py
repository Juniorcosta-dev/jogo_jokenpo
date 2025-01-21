print("Bem-vindo ao Jokenpo!")
print("Escolha sua jogada: pedra, papel ou tesoura")

jogador1 = "tesoura"
jogador2 = "pedra"

if jogador1 == jogador2:
    print("Empate!")
elif (jogador1 == "pedra" and jogador2 == "tesoura") or (jogador1 == "papel" and jogador2 == "pedra") or (jogador1 == "tesoura" and jogador2 == "papel"):
    print("Jogador 1 venceu!")
else:
    print("Jogador 2 venceu!")