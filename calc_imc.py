 
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
total_usuarios = int(input('Digite o total de usuarios:'))

# loop para cada usuarios definido no input
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

print("\n===Relatório final===")
print(f'{'Nome':<10}{'Altura':<10}{'Peso':<10}{'IMC':<10}{'Classificacao'}')
print("-" * 50)


for i in usuarios:
    print(f"{i['Nome']:<10}{i['Altura']:<10.2f}{i['Peso']:<10.1f}{i['IMC']:<10.2f}{i['Classificação']}")

