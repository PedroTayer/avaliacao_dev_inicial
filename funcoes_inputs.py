import heapq

def verificar_numero(valor_str, pode_float = True):
	R = '\033[31m'
	W = '\033[0m'
	print(f'Valor inserido: {valor_str}')
	try:
		if pode_float:
			valor_num = float(valor_str)
		else:
			valor_num = int(valor_str)
		if valor_num<0:
			print('Valor negativo inserido. Favor inserir valor positivo.')
			return -1
		return valor_num

	except ValueError:
		if pode_float:
			print(R+'Valor não numérico! Favor inserir valor numérico, separador decimal é ".", exemplo: 5.8'+W)
		else:
			print(R+'Número não inteiro! Favor inserir número inteiro, exemplo: 5.'+W)
		return -1

def coletar_input(texto, pode_float = True):
	valor_str = input(f'{texto}')
	valor = verificar_numero(valor_str, pode_float)

	if valor == -1:
		return coletar_input(texto, pode_float)
	else:
		return valor

def main():
	R = '\033[31m'
	G = '\033[32m'
	W = '\033[0m'
	B = '\033[94m'
	separador = 45 * '#'

	print(f'\nDigite 0 para sair a qualquer momento.\n{separador}')

	galao = coletar_input('Insira o volume do galão (em litros): ', pode_float=True)

	if galao==0:
		print('0 inserido.. Obrigado por utilizar o programa!!')
		return False, 0, {}, []

	qtd_garrafas = coletar_input('Insira a quantidade de garrafas: ', pode_float = False)

	if qtd_garrafas==0:
		print('0 inserido.. Obrigado por utilizar o programa!!')
		return False, 0, {}, []

	garrafas_dict = {}
	heap_garrafas = []
	for garrafa in range(1, qtd_garrafas+1):
		garrafas_dict[garrafa] = coletar_input(f'Insira a quantidade na garrafas {garrafa}: ', pode_float=True)
		if garrafas_dict[garrafa] == 0:
			print('0 inserido.. Obrigado por utilizar o programa!!')
			return False, 0, {}, []
		heapq.heappush(heap_garrafas, -garrafas_dict[garrafa])

	return True, galao, garrafas_dict, heap_garrafas