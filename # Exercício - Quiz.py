# Exercício - sistema de perguntas e respostas 
# Objetivo: Atividade utilizando dicionario


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
certas = 0
for item in perguntas:
    print(item['Pergunta'])
    for posicao, opcao in enumerate(item['Opções']): #enumerate permite adicionar numeros posicionais

        print(f'{posicao}) {opcao}')
        if opcao == item['Resposta']:
            pos_certa = posicao
            
    resposta = input("Escolha uma opção: ")
    
    if resposta.isdigit():
        r = int(resposta)
        if r > len(item['Opções']) and r <=0:
            print("APENAS OPÇÕES 0 À 3!!!")
        else:
            if r == pos_certa:
                certas = certas + 1
                print("CERTA RESPOSTA!!")
            else:
                print("ERROOOUU")
    else:
        print("APENAS NÚMEROS!")
        break
print (f'TOTAL: {certas}/3')

