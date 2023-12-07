from carro import *


carro = Carro(modelo="Fusca", cor="Azul", ano=2005)
gasolina = Gasolina(quantidade=30)
motor = Motor(gasolina=gasolina)


motor.ligar_carro()


motor.velocidade(2000)

motor.desligar_carro()
