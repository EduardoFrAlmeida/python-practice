# Lista sem duplicados
# Dada lista [1,2,2,3,4,4,5], remova duplicados

lista_original = [1, 2, 2, 3, 4, 4, 5, 6, 6]

# Transformar em set (remove duplicados) e depois voltamos para lista
lista_sem_duplicados = list(set(lista_original))

print(f"Original: {lista_original}")
print(f"Sem duplicados: {lista_sem_duplicados}")

