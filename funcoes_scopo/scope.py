def my_func():
    my_var = 10
    print(my_var)

my_func()


def outer_func():
    msg = 'Hello there!'

    def inner_func():
        print(msg)

    inner_func()

outer_func()


def outer_func():
    msg = 'Hello there!'
    res = ""  # Declare res in the enclosing scope

    def inner_func():
        nonlocal res  # nonlocal serve para modificar e colocar valores dentro de uma varial externa (função externa ) -> (função principal)
        res = 'How are you?'
        print(msg)  # Accessing msg from outer_func()

    inner_func()
    print(res)  # Now res is accessible and modified

outer_func()

idade =50 

def motrar_idade(): #variavel global(variavel fora de uma função) consegue ser acessada por uma função 
    print(idade)

motrar_idade()


my_var_1 = 7

def show_vars():
    global my_var_2 #global serve para deixar a variavel visivel em todo programa não precisando chamar a função especificamente  
    my_var_2 = 10
    global teste
    teste = 50 
    print(my_var_1)
    print(my_var_2)
    print(teste)

show_vars() # 7 10

print(my_var_2) # 10

print(teste)


my_var = 10  #variavel global (função exerga essa variavel por padrão)

def change_var():
    global my_var  # se o globla não for colado, além do erro de execução o 
                    #progama não irá enxergar o valor 20 atribuido a variavel vai continuar ocmo padrão o a varialvel global iniciada no começo do codigo
    my_var = 20

change_var()

print(my_var)


