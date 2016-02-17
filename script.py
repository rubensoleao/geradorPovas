import yaml, glob

diretorio = 'Questoes/*' 

#aquivo de entrada
arquivos = glob.glob(diretorio)

#arquivo de saida
prova = open("prova.html","w")
gabarito = open("gabarito.html", "w")

#Imprime cabeçalho html da prova
prova.write('<meta charset="ISO-8859-1">')
#Imprime cabeçalho html do gabarito
gabarito.write('<H1> Gabarito </H1>\n')
gabarito.write('<ol type = "1">\n')

for arquivo in arquivos:
	with open(arquivo, 'r') as entrada:
		questao = yaml.load(entrada)
		prova.write("<H5>")
		prova.write(questao['Questao'])
		prova.write("</H5>\n\n")

		prova.write('<ol type="a">\n')
		for resposta in questao['Respostas']:
			prova.write("<li>")
			prova.write(resposta)
			prova.write("</li>\n")

		prova.write("</ol>")

		gabarito.write("<li>")
		gabarito.write(questao['Certa'])
		gabarito.write("</li>\n")

gabarito.write('</ol>')