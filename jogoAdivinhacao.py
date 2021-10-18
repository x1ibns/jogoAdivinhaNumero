chave = 13
tentativas = 3 
tentativa = 1


print('*******************')
print('Jogo da Advinhação')
print('*******************')

while ( tentativa <= tentativas ) : 
	chute = int(input('escolha um numero  '))
	
	if (chute == chave) :
		print('voce acertou') 
	else :
		print('voce errou ') 
		print('voce tem mais ',tentativas - tentativa,' tentativas')
	tentativa = tentativa +1
	
replay = input('quer jogar novamente S ou N ?')

if (replay == s ) or (replay == S) : 
	to line 6
else :
	print('até a próxima ')
