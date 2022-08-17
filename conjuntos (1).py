#Rafaela de Miranda

#Enunciado
#Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  criar  um  programa,  utilizando  a 
#linguagem  Python, C, ou C++.  Este  programa,  quando  executado,  irá  apresentar  os  resultados  de 
#operações que serão realizadas entre dois conjuntos de dados.  
#O  programa  que  você  desenvolverá  irá  receber  como  entrada um arquivo de texto  (.txt) 
#contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas 
#em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas 
#segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de 
#operações  que  estão  descritas  no  arquivo,  este  número  de  operações  será  um  inteiro;  as  linhas 
#seguintes  seguirão  sempre  o  mesmo  padrão  de  três  linhas:  a  primeira  linha  apresenta  o  código  da 
#operação  (U para união, I para interseção, D para diferença e C produto cartesiano),  a  segunda  e 
#terceira linhas conterão os elementos dos conjuntos separados por virgulas.

txt_open = open("texto3.txt", "r")
texto = txt_open.readlines()

a_c = []
for contar in range(len(texto)):
    if texto[contar].strip() == 'U' or texto[contar].strip() == 'I' or texto[contar].strip() == 'D' or texto[contar].strip() == 'C':
        a_c.append(texto[contar].strip())
print(len(a_c))

for id in range(len(texto)):            
    #Função intersecção
    if texto[id].strip() == 'I':
        i1 = texto[id + 1].strip().split(', ')
        i2 = texto[id + 2].strip().split(', ')
        i_ar = []
        for inter in range(len(i1)):
            for inter1 in range(len(i2)):
                if i1[inter] == i2[inter1]:
                    i_ar.append(i1[inter])
        print(f'Intersecção: conjunto 1{i1}, conjunto 2{i2}.Resultado:{i_ar}')

    #Função Produto Cartesiano
    if texto[id].strip() == 'C':        
        c1 = texto[id + 1].strip().split(', ')
        c2 = texto[id + 2].strip().split(', ')
        d_a = []
        for pc in range(len(c1)):
            for pc2 in range(len(c2)):
                d_a.append((c1[pc], c2[pc2]))    
        print(f'Plano cartesiano: conjunto 1{c1}, conjunto 2{c2}.Resultado: {d_a}')

    #Função diferença
    if texto[id].strip() == 'D':
        d1 = texto[id + 1].strip().split(', ')
        d2 = texto[id + 2].strip().split(', ')
        dife = []
        for d in d1:
            if d not in d2:
                dife.append(d)
        print(f'Diferença: conjunto 1{d1}, conjunto 2{d2}.Resultado: {dife}')

    #Função união
    if texto[id].strip() == 'U':
        u1 = texto[id + 1].strip().split(', ')
        u2 = texto[id + 2].strip().split(', ')
        i = []
        num_array = []

        for u in range(len(u1)):
            i.append(u1[u])
        for uu in range(len(u2)):
            i.append(u2[uu])

        uniao = sorted(i)
    
        for c in range(len(uniao)):
            if c != len(uniao)-1:
                if uniao[c] != uniao[c + 1]:
                    num_array.append(uniao[c])
        num_array.append(uniao[-1])
        print(f'União: conjunto 1 {u1}, conjunto 2{u2}.Resultado: {sorted(num_array)}')