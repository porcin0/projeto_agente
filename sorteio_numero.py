import random

def sorteia_numero():
    numero = random.randint(1, 100)
    print(f'Número sorteado: {numero}')

# Exemplo de uso
def main():
    sorteia_numero()

if __name__ == '__main__':
    main()