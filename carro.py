class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.velocidade_atual = 0


class Freio(Carro):
    def __init__(self, tipo):
        super().__init__(modelo=None, cor=None, ano=None)
        self.tipo = tipo

    def acionar_freio(self, carro):
        if self.tipo == 'Disco':
            if carro.velocidade_atual > 0:
                print(f"Freio {self.tipo} acionado. Reduzindo a velocidade do carro.")
                carro.velocidade_atual -= 10
            else:
                print("O carro já está parado.")
        elif self.tipo == 'ABS':
            if carro.velocidade_atual > 0:
                print(f"Freio {self.tipo} acionado. Reduzindo a velocidade do carro.")
                carro.velocidade_atual -= 20
            else:
                print("O carro já está parado.")


class Gasolina(Carro):
    def __init__(self, quantidade):
        super().__init__(modelo=None, cor=None, ano=None)
        self.quantidade = quantidade

    def verificar_gasolina(self):
        return self.quantidade >= 25

    def consumir_gasolina(self):
        litros_iniciais = self.quantidade

        while self.quantidade >= 0:
            print(f"Quantidade atual: {self.quantidade}, Litros iniciais: {litros_iniciais}")
            percentual_restante = (self.quantidade / litros_iniciais) * 100
            print(f'O carro está com {percentual_restante:.0f}% de gasolina.')

            if self.quantidade == 0:
                break

            self.quantidade -= 1

        print("O tanque está vazio. Abasteça para continuar.")


class Motor(Carro):
    def __init__(self, gasolina, estaligado=False):
        super().__init__(modelo=None, cor=None, ano=None)
        self.gasolina = gasolina
        self.estaligado = estaligado

    def ligar_carro(self):
        if self.gasolina.verificar_gasolina():
            self.estaligado = True
            print("Carro ligado.")
        else:
            print("Não foi possível ligar o carro. Tanque vazio.")

    def velocidade(self, ano):
        if self.estaligado:
            if ano <= 2000:
                velocidades = [0, 30, 60, 90]
                for vel in velocidades:
                    print(f'O carro está a {vel} km/h.')
                    self.gasolina.consumir_gasolina()
            elif 2010 >= ano >= 2000:
                velocidades = [0, 30, 60, 90, 120, 150]
                for vel in velocidades:
                    print(f'O carro está a {vel} km/h.')
                    self.gasolina.consumir_gasolina()
            elif 2020 >= ano >= 2010:
                velocidades = [0, 30, 60, 90, 120, 150, 180, 210, 240]
                for vel in velocidades:
                    print(f'O carro está a {vel} km/h.')
                    self.gasolina.consumir_gasolina()
        else:
            print('O carro não está ligado.')

    def desligar_carro(self):
        pass
