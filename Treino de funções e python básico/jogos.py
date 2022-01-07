import python1e2 as jg

print("-----bem vindo a plataforma de jogos-----")
print("------------escolha seu jogo-------------")
x = int(input(" digite 1 para adivinhacao e 2 para forca\n"))

if x == 1:
    jg.advinhacao()
elif x == 2:
    jg.forca()
else:
    print("voce não escolheu nenhum jogo disponível")
