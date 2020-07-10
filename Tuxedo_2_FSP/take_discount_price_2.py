# encoding: utf-8

def string_to_list(string):             #Esta función separa una cadena de caracteres en componentes de lista, tomando en cuenta un caracter de separación
    list_result = list(string.split(";"))
    return list_result
 
#Toma el precio del robot 2.

pair_price_2 = string_to_list(GetVar('price_2').replace(" MXN","").replace(" ",";"))

#print(pair_price_2)

SetVar('price_2', pair_price_2[2])