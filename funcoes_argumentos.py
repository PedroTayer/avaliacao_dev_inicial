import heapq


def organizar_input_garrafas(garrafas):
	heap_garrafas = []

	garrafas_dict = {ind: float(val) for ind, val in enumerate(garrafas, 1)}

	for garrafa in range(1, len(garrafas_dict) + 1):
		heapq.heappush(heap_garrafas, -garrafas_dict[garrafa])

	return garrafas_dict, heap_garrafas


def lista_para_args(lista):
	args = {}
	args['printar'] = False
	for i in lista:
		if i == 'printar':
			args['printar'] = True
		else:
			try:
				nome, valor = i.split('=')
			except ValueError:
				print(
					'Favor inserir parâmetros separados por espaço com o símbolo de =, exemplo:\n galao=4.6 garrafas=3.7,1,2')
				return False, {}
			args[nome] = valor
	return True, args


def verificar_argumentos(**kwargs):

	if 'galao' not in kwargs:
		print(f'Parâmetro "galao" precisa ser passado, exemplo:\n galao=4.6 garrafas=3.7,1,2')
		return False, -1, -1

	try:
		galao = float(kwargs['galao'])
		if galao <= 0:
			print(f'Valor {galao} é negativo ou 0, abortando...')
			return False, -1, -1
	except ValueError:
		print(f'Valor {galao} não é numérico, abortando...')
		return False, -1, -1

	try:
		garrafas_str = kwargs['garrafas'].split(',')
		try:
			garrafas = [float(i) for i in garrafas_str]

		except ValueError:
			print(f'Algum valor dentro de {garrafas_str} não é numérico, abortando...')
			return False, -1, -1
		if any(garrafa <= 0 for garrafa in garrafas):
			print(f'Algum valor dentro de {garrafas} é negativo ou 0, abortando...')
			return False, -1, -1

	except ValueError:
		print(
			'Favor inserir parâmetros litros da garrafa separados por "," sem espaço, exemplo:\n galao=4.6 garrafas=3.7,1,2')
		return False, -1, -1

	return True, galao, garrafas
