""" Desafio 004: """

if __name__ == '__main__':

    print('-'*40)
    n = input('Digite algo: ')
    print('-'*40)
    print(f'O tipo primitivo desse valor é {type(n)}')
    print(f'É alfabético e numérico? {n.isalnum()}')
    print(f'É apenas alfabético? {n.isalpha()}')
    print(f'Todos os caracteres são maiúsculos? {n.isupper()}')
    print(f'É possivel ser mostrado na tela? {n.isprintable()}')
    print(f'Faz parte do padrão ASCII? {n.isascii()}')
    print(f'É apenas numérico? {n.isnumeric()}')
    print(f'É um dígito? {n.isdigit()}')
    print(f'Todos os caracteres são espaços? {n.isspace()}')
    print(f'É um título? {n.istitle()}')
    print(f'Todos os caracteres são minúsculos? {n.islower()}')
