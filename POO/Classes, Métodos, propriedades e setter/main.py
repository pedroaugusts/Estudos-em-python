from contas import Conta

marcelo = Conta(131, "Marcelo", 500)

pedro = Conta(121, 'Pedro', 300)

marcelo.tranferencia(pedro, 300)

pedro.extrato()
pedro.sacar(1700)
