from model import model_lead
import control

def add_lead():
    name = input("Nome: ")
    email = input("E-mal: ")
    stage = input("Etapa de vendas: ")

    #validar os dados
    #modelar os dados (leads) como um dicionário
    #modelar -- model
    print(model_lead(name,email,stage))

    #de acordo com os dados modelados (lead como dict)
    #enviar dado do lead para o leads.json
    #control irá ajudar nisso
    control.create_leads(model_lead(name, email, stage))

    print('lead adicionado (func)')

    def list_leads():
        leads = control.read_leads()
        print(leads)

def main():
    while True:
        print('\nMini CRM de Leads')
        print('[1] Adicionar lead')
        print('[2] Listar leads')
        print('[0] Sair do programa')

        opt = input('Escolha uma opção: ')
        if opt == '1':
            add_lead()
        elif opt == '2':
            print('Listar leads')
        elif opt == '0':
            print('Sair do programa')
            print('Até mais...')
            break
        else:
            print('Opção inválida.')

if __name__ == '__main__':
    main()