from Models.calcular import Calcular


def main():
    pontos = 0
    jogar(pontos)


def jogar(pontos):

    dificuldade = int(input("Informe o nível de dificuldade desejada(1-3): "))
    while dificuldade <= 0 or dificuldade > 3 or type(dificuldade) != int:
        dificuldade = int(input("Informe o nível de dificuldade desejada(1-3): "))
    calc = Calcular(dificuldade)
    calc.mostrar_operacao()
    resultado = int(input(f"Resposta: "))

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f"Você tem {pontos} pontos!")

    continuar = input("Deseja continuar no jogo? [S para 'sim' ou N para 'não']: ")
    while continuar.upper() != "S" and continuar.upper() != "N":
        continuar = input("Deseja continuar no jogo? [S para 'sim' ou N para 'não']: ")
    if continuar.upper() == "S":
        jogar(pontos)
    elif continuar.upper() == "N":
        print(f"Você finalizou com {pontos} pontos!")


if __name__ == "__main__":
    main()
