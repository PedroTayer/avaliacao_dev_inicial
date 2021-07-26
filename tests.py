from main import main as script

def testar(flag_esperada, resp_esperada, sobra_esperada, galao, garrafas, teste):
	print(10*'#' + f' TESTE {teste} ' + 10*'#')
	flag_obtida, resp_obtida, sobra_obtida = script(galao=galao, garrafas=garrafas, printar=False)
	c1  = flag_obtida == flag_esperada
	c2  = resp_obtida == resp_esperada
	c3  = sobra_obtida == sobra_esperada
	if c1 and c2 and c3:
		print(G+f'Teste {teste} passou!'+W)
	else:
		print(R+f'Teste {teste} falhou.'+W)

W = '\033[0m'
G = '\033[32m'
R = '\033[31m'

teste = 0

# Teste 1
teste+=1
galao = 7
garrafas = '1,3,4.5,1.5,3.5'
resp_esperada = ['1.0L', '4.5L', '1.5L']
sobra_esperada = 0
flag_esperada = True
testar(flag_esperada, resp_esperada, sobra_esperada, galao, garrafas, teste)

# Teste 2
teste+=1
galao = 5
garrafas = '1,3,4.5,1.5'
resp_esperada = ['1.0L', '4.5L']
sobra_esperada = 0.5
flag_esperada = True
testar(flag_esperada, resp_esperada, sobra_esperada, galao, garrafas, teste)

# Teste 3
teste+=1
galao = 4.9
garrafas = '4.5, 0.4'
resp_esperada = ['4.5L', '0.4L']
sobra_esperada = 0
flag_esperada = True
testar(flag_esperada, resp_esperada, sobra_esperada, galao, garrafas, teste)


# Teste 4
teste+=1
galao = -4.9
garrafas = '4.5, 0.4'
resp_esperada = []
sobra_esperada = -1
flag_esperada = False
testar(flag_esperada, resp_esperada, sobra_esperada, galao, garrafas, teste)


# Teste 5
teste+=1
galao = -4.9
garrafas = '4.5, 0.4'
resp_esperada = []
sobra_esperada = -1
flag_esperada = False
testar(flag_esperada, resp_esperada, sobra_esperada, galao, garrafas, teste)


# Teste 6
teste+=1
galao = 4.9
garrafas = '4.5, 0.4'
resp_esperada = []
sobra_esperada = -1
flag_esperada = False
testar(flag_esperada, resp_esperada, sobra_esperada, galao, garrafas, teste)

# Teste 5
teste+=1
galao = -4.9
garrafas = '4.5, 0.4'
resp_esperada = []
sobra_esperada = -1
flag_esperada = False
testar(flag_esperada, resp_esperada, sobra_esperada, galao, garrafas, teste)
