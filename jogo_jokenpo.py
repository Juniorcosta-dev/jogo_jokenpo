import random

print("Bem-vindo ao Jokenpo!")

# Jogada do Jogador 1 (computador escolhe aleatoriamente)
jogador1 = random.choice(["papel", "pedra", "tesoura"])

# Entrada do Jogador 2 (garantindo uma escolha válida)
while True:
    jogador2 = str(input("Escolha sua jogada: (pedra/papel/tesoura)")).lower()

    if jogador2 in ["pedra", "papel", "tesoura"]:
        break
    else:
        print("Escolha inválida! por favor, escolha 'pedra', 'papel' ou 'tesoura'")


print(f"Jogador1 escolheu: {jogador1}")
print(f"Jogador2 escolheu: {jogador2}")

# Verificação do resultado
if jogador1 == jogador2:
    print("Empate!")
elif (jogador1 == "pedra" and jogador2 == "tesoura") or (jogador1 == "papel" and jogador2 == "pedra") or (jogador1 == "tesoura" and jogador2 == "papel"):
    print("Jogador 1 venceu!")
else:
    print("Jogador 2 venceu!")
    