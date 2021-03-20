def intersect1d(pda1 : pdarray, pda2 : pdarray, 
                                   assume_unique : bool=False) -> pdarray:
    if not assume_unique:
        pda1 = unique(pda1)
        pda2 = unique(pda2)
    aux = concatenate((pda1, pda2), ordered=False)
    aux_sort_indices = argsort(aux)
    aux = aux[aux_sort_indices]
    mask = aux[1:] == aux[:-1]
    int1d = aux[:-1][mask]
    return int1d
