 
# função para calcular o IMC
def calc_imc(peso, altura): 
    return peso / altura ** 2
# função para classificar o IMC
def classificacao(imc):
    if imc < 18.5:
        return 'Abaixo do Peso'
    elif imc < 25:
        return 'Peso Normal'
    elif imc < 30:
        return 'Sobrepeso'
    elif imc < 40:
        return "Obesidade"
    else:
        return "Obesidade Grave"   
    
# lista de usuarios para preencher     
usuarios = []

# input de quantidade de usuarios para calcular o IMC
total_usuarios = int(input('Digite o total de usuarios: '))

# usando um 'for' para iterar para cada quantidade de usuarios informados no input acima
for i in range(total_usuarios):

    nome = input('Digite seu nome: ')
    altura = float(input('Digite sua altura: '))
    peso = float(input('Digite seu peso: '))

    imc = calc_imc(peso, altura)
    classific = classificacao(imc)

    relatorio = {
        'Nome': nome,
        'Altura': altura,
        'Peso': peso,
        'IMC': round(imc, ),
        'Classificação': classific
    }

    usuarios.append(relatorio)

# visualização dos dados informados atraves do input e criação de um documento txt com os dados 
with open('Relatório.txt', 'w', encoding='utf-8') as new_file:
    cabecalho = "\n===Relatório final===\n"
    cabecalho += f'{'Nome':<10}{'Altura':<10}{'Peso':<10}{'IMC':<10}{'Classificacao'}\n'
    cabecalho += "-" * 50 + "\n"

    print(cabecalho)
    new_file.write(cabecalho)

    for i in usuarios:

        linhas = f"{i['Nome']:<10}{i['Altura']:<10.2f}{i['Peso']:<10.1f}{i['IMC']:<10.2f}{i['Classificação']}\n"
        print(linhas) 
        new_file.write(linhas)
