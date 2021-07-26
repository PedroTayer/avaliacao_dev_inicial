**Descreva como você projetaria um sistema online que atenda as histórias:**

**1) Quero poder enviar arquivos em formato .csv para o sistema, de modo que seja possível baixá-los depois.**

**2) Quero poder ler o conteúdo dos meus arquivos .csv de maneira consolidada na plataforma;**

**3) Quero poder ver a lista dos meus arquivos enviados e poder fazer busca através de filtros e parâmetros;**

**4) Quero poder exportar os dados lidos dos meus arquivos em formato .csv**

**5) Quero poder enviar por email os dados lidos dos meus arquivos.**

**De maneira simplificada, comente qual é a arquitetura ou design que você considera mais adequados para essa solução?**

Algumas considerações adotadas para responder à pergunta:
* Quem utiliza o sistema é um usuário interno da EuReciclo
* O projeto do front-end é desconsiderado
* Os .csv tem o mesmo formato e não mudarão (mesmas colunas)

A arquitetura mais adequada é baseada em uma **API conectada a um banco de dados SQL** (Redshift, PostgreSQL, MySQL, etc).

A API deve ser capaz de:
* Inserir um .csv no database SQL devidamente identificado
* Ler o database SQL com os devidos filtros (query request)
* Salvar uma query em formato .csv remotamente
* Enviar um email o .csv salvo da query

O fluxo de processos para inserir um .csv
1. Conexão ao database
2. Inserção do .csv no database (local para remoto)

O fluxo de processos para enviar um .csv por email
1. Conexão ao database
2. Query no database com os filtros desejados
3. Salva o resultado da query em formato .csv (remoto para local)
4. Envio o arquivo .csv a um email