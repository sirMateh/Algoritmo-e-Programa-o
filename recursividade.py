def permutar(palavra):
    if len(palavra) <= 1:
        return [palavra]

    permutacoes = []
    for c, letra in enumerate(palavra):
        letra_fixa = letra
        restante = palavra[:c] + palavra[c+1:] #### s[:i ] <<< pega todas as letras antes do índice i #### SEGUE A LÓGICA DO INTERVALO aberto )
        #### s[i+1:] >>>> pega todas as strings depois do índice i  #### segue a lógica do intervalo fechado [ 
 
        for p in permutar(restante):
            permutacoes.append(letra_fixa + p)
    
    for permutacao in permutacoes:
        if permutacoes.count(permutacao) > 1:
            while permutacoes.count(permutacao) != 1:
                permutacoes.remove(permutacao)

    return list(permutacoes) 

palavra = str(input('Digite: '))
resultado = permutar(palavra)

print(f"Permutações de {palavra}: {resultado}")
print(f"Total: {len(resultado)}")
