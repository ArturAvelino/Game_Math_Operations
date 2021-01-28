from random import randint


class Calcular:

    def __init__(self, dificuldade):
        self.__dificuldade = dificuldade
        self.__valor1 = self._gerar_valor
        self.__valor2 = self._gerar_valor
        self.__operacao = randint(1, 3)
        self.__resultado = self._gerar_resultado

    @property
    def dificuldade(self):
        return self.__dificuldade

    @property
    def valor1(self):
        return self.__valor1

    @property
    def valor2(self):
        return self.__valor2

    @property
    def operacao(self):
        return self.__operacao

    @property
    def resultado(self):
        return self.__resultado

    @property
    def _gerar_valor(self):
        if self.dificuldade == 1:
            return randint(1, 10)
        elif self.dificuldade == 2:
            return randint(1, 100)
        elif self.dificuldade == 3:
            return randint(1, 1000)
        else:
            return "Dificuldade desconhecida"

    @property
    def _gerar_resultado(self):
        if self.operacao == 1:
            return self.valor1 + self.valor2
        elif self.operacao == 2:
            return self.valor1 - self.valor2
        elif self.operacao == 3:
            return self.valor1 * self.valor2

    @property
    def _op_simbolo(self):
        if self.operacao == 1:
            return "+"
        elif self.operacao == 2:
            return "-"
        elif self.operacao == 3:
            return "*"

    def checar_resultado(self, resultado):
        certo = False
        if self._gerar_resultado == resultado:
            print("\033[1;92mResposta correta!\033[m")
            certo = True
        else:
            print("\033[1;91mO pesadelo do ENEM \nResposta errada, seu arrombado!\033[m")
        print(f"{self.valor1} {self._op_simbolo} {self.valor2} = {self._gerar_resultado}")
        return certo

    def mostrar_operacao(self):
        print(f"{self.valor1} {self._op_simbolo} {self.valor2} = ?")

    def __str__(self):
        if self.__operacao == 1:
            op = "Somar"
        elif self.__operacao == 2:
            op = "Subtrair"
        elif self.__operacao == 3:
            op = "Multiplicar"
        else:
            op = "Operação desconhecida"
        return f"Valor1: {self.valor1} \nValor2: {self.valor2} \nDificuldade: {self.dificuldade} \nOperação: {op}"
