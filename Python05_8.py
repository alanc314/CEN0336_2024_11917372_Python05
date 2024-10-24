#!/usr/bin/env python3
dicionario_fav = {'livro' : 'Harry Potter', 'som' : 'Under Pressure', 'arvore': 'Ipê'}                                  
dicionario_fav['organismo'] = 'Arabidopsis thaliana'
chaves_dicionario = list(dicionario_fav.keys())


fav_thing = input(f'Qual item do dicionário {chaves_dicionario} deseja alterar? ')                                                 
alterado = input('Qual o novo valor da chave? ')
dicionario_fav[fav_thing] = alterado
print(dicionario_fav)

