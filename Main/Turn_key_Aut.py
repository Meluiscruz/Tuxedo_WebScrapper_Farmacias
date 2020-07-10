# -*- coding: utf-8 -*-

print('  ________  ___  __ __________  ____     ____  ____  ____      ____________________')
print(' /_  __/ / / / |/ // ____/ __ \/ __ \   / __ \/ __ \/ __ \    / / ____/ ____/_  __/')
print('  / / / / / /|   // __/ / / / / / / /  / /_/ / /_/ / / / /_  / / __/ / /     / /   ')
print(' / / / /_/ //   |/ /___/ /_/ / /_/ /  / ____/ _, _/ /_/ / /_/ / /___/ /___  / /    ')
print('/_/  \____//_/|_/_____/_____/\____/  /_/   /_/ |_|\____/\____/_____/\____/ /_/     ')
print('')

while True:
    starting = input(" BIENVENIDO A TUXEDO! ********** Por favor, oprima 'R' para Iniciar.: ")
    if starting == 'R':
        break
    elif starting == 'r':
        break
    else :
        print('Caracter no valido')

print( '********* INICIO DEL PROCESO ********* ' )

product_list = GetVar('products')

print(f'Esta es la lista de productos que vamos a buscar: {product_list}')