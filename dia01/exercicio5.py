#write-a-function

# A Lógica do Ano Bissexto (Leap Year)
# As regras podem ser resumidas assim:
# Divisível por 400? Sempre é bissexto (Fim de papo).
# Se não, é divisível por 100? Não é bissexto (Mesmo sendo divisível por 4).
# Se não, é divisível por 4? É bissexto.
# Qualquer outra coisa: Não é bissexto.

def is_leap(year):
    leap = False
    
    # Regra 1: Divisível por 4
    if year % 4 == 0:
        leap = True
        # Regra 2: Mas se for divisível por 100, NÃO é bissexto
        if year % 100 == 0:
            leap = False
            # Regra 3: A menos que também seja divisível por 400!
            if year % 400 == 0:
                leap = True
                
    return leap

year = int(input('Digite um Ano para saber se ele é bissexto ou não: '))
print(is_leap(year))