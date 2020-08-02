#Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função
def éPrimo(k):
	n = k
	i = 0
	primo = True
	while n>1:
		if k%n==0:
			i += 1
			n = n-1
		else:
			n = n-1
	if i == 1:
		primo = True
	else:
		primo = False
	return primo

def maior_primo(k):
	while k > 1:
		if éPrimo(k) == True:
			return k
		else:
			k += -1
			
