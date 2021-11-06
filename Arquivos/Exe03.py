# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
# https://pt.wikipedia.org/wiki/Matriz_transposta
# Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de sistemas de IA.
matrix = [[1, 2],[3,4],[5,6],[7,8]]
transposta = [[mat[i] for mat in matrix] for i in range(2)]
print(transposta)