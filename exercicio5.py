import math

def area_circulo (raio):
    if raio.isnumeric():
        raio1 = float(raio)
        area = raio1**2 * math.pi
        return print("A área do círculo é",round(area, 2))
    else:
        return

def comprimento_circulo (raio):
    if raio.isnumeric():
        raio1 = float(raio)
        comprimento = 2 * (math.pi * raio1)
        return print("O comprimento do círculo é", round(comprimento, 2))
    else:
        print("Digite um valor numérico")      
    
raio = input("Digite o raio do círculo: ")

area_circulo(raio)
comprimento_circulo(raio)