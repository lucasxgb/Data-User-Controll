'''
    Classe de usuários;
    Será a responsável pela criação de novas instâncias de usuários que serão adicionados
    a lista de usuários.
'''
class User:
    def __init__(self, name, email, age): # Atributos que são iniciados na criação de nova instância
        self.name = name
        self.email = email
        self.age = age
        pass
    

'''
    Classe responsável por gerenciar todo o sistema, nela ocorrerá o processamento de dados, 
    bem como a exibição de informações
'''
class SystemManagement:
    def __init__(self):
        self.usersList = []
    
    # Metódo que exibe todas as informações de um usuário
    def showUserInfo(self, user):
         print(f'''  
                Usuário : {user.name}
                Email : {user.email}
                Idade : {user.age}
                \n
                  ''')
         
    # Esse Metódo irá criar um novo usuário e adicionar na lista de usuários
    def createNewUser(self, name, email, age):
        newUser = User(name, email, age)
        emailIsUsed = False
        for user in self.usersList: # Verificação para não permitir cadastrar um novo usuário com email já utilizado
            if user.email.lower() == newUser.email.lower():
                print("Email já cadastrado!")
                emailIsUsed = True
             
        if emailIsUsed == False:
            self.usersList.append(newUser)
            print("Usuário cadastrado com sucesso!")
    
    # Metódo que exibe as informações de todos os usuários presentes na lista
    def displayAllUsers(self):
        for user in self.usersList: # for irá iterar sobre a lista e para cada usuário serão exibido suas informações
            self.showUserInfo(user)

    # Função que irá realizar uma busca linear na lista
    # comparando se o usuário procurado está presente nela através do nome.
    def searchUserInList(self, searchName):
        searchResult = []
        for user in self.usersList:
            if  searchName.lower() in user.name.lower(): # Verifica se o usuário da lista possui o mesmo nome procurado
                searchResult.append(user) # usando lista, pois, em um caso pode-se encontrar mais de um usuário com o mesmo nome
    
        if (searchResult == []): # caso não seja encontrado devolve essa informação ao usuário
            print("Usuário não encontrado!")
        else: # Caso seja encontado, exibe os dados utilizando o metódo de exibição
            for resultUser in searchResult:
                self.showUserInfo(resultUser)

   
# Opções de entrada do usuário
def showOptions():
    print("\n")
    print("""
        1 - Cadastrar novo usuário
        2 - Visualizar todos os usuários
        3 - Buscar por nome de usuário
        0 - Sair 
                   """)
    option = int(input("Informe a opção desejada: "))
    return option


def systemExecution(): # Menu de tratamento de dados, onde irá exibir as opções para o usuário e dependendo da escolha irá realizar a funcionalidade
    system = SystemManagement() # instancia do Controle
    option = showOptions() # Exibição das opções do usuário
    if option == 0:
        print('Programa Encerrado!')
    else:
        while option != 0:
            if option == 1: # Cadastro de usuário na lista
                name = input("Informe o nome do usuário: ")
                email = input("Informe o email do usuário: ")
                age = input("Informe a idade do usuário: ")
                system.createNewUser(name, email, age)
            elif option == 2:
                system.displayAllUsers()      
            elif option == 3:
                searchName = input("Informe o nome do usuário que deseja buscar: ")
                system.searchUserInList(searchName)
            else:
                print("Opção inválida!")
            option = showOptions()
        if option == 0:
                print('Programa Encerrado!')
    
                    
# Chamada para execução do sistema!
systemExecution()
       

