#!/usr/bin/env python3
dicionario_fav = {'livro' : 'Harry Potter', 'som' : 'Under Pressure', 'arvore': 'Ipê'}                                  
dicionario_fav['organismo'] = 'Arabidopsis thaliana'
chaves_dicionario = list(dicionario_fav.keys())

fav_thing = input(f'Qual item do dicionário {chaves_dicionario} quer olhar? ')                                                 
print(dicionario_fav[fav_thing])

