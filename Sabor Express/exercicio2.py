# Exercício 1 - Digitar um número e determinar se é par ou ímpar
def exercicio1():
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("Número Par")
    else:
        print("Número ímpar")

#2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade
#  em categorias de acordo com as seguintes condições:
def exercicio2():
    idade = int(input("Diga sua idade: "))
    if idade < 13:
        print("Você é uma criança")
    elif idade < 19:
        print("Você é um adolescente")
    else:
        print("Você é um adulto")

#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e 
#a senha fornecidos correspondem aos valores esperados determinados por você.
def exercicio3():
    nome = str(input("Nome de usuário: "))
    senha = str(input("Senha: "))
    if nome == "jnn" and senha == "1234":
        print("Login efetuado com sucesso")
    else:
        print("Usuário ou senha incorretos")

#4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else 
# para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
def exercicio4():
    coordenada_x = int(input(print("Digite a primeira coordenada: ")))
    coordenada_y = int(input(print("Digite a segunda coordenada: ")))
    if coordenada_x > 0 and coordenada_y > 0:
        print("Primeiro quadrante")
    elif coordenada_x < 0 and coordenada_y > 0:
        print("Segundo quadrante")
    elif coordenada_x < 0 and coordenada_y < 0:
        print("Terceiro quadrante")
    elif coordenada_x > 0 and coordenada_y < 0 :
        print("Quarto quadrante")
    else:
        print("Localizado no eixo ou origem")

def main():
    exercicio2()

if __name__ == '__main__':
    main()

