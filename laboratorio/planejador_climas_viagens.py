#Objetivo: Cumprir as user stories abaixo e fazer todos os testes passarem para completar o laboratório.

#Você deve criar as seguintes variáveis:
#distance_mi (um número que representa a distância a percorrer em milhas)
#is_raining (um booleano que representa se o usuário está atualmente enfrentando clima chuvoso)
#has_bike (um booleano que representa se o usuário tem uma bicicleta)
#has_car (um booleano que representa se o usuário tem um carro)
#has_ride_share_app (um booleano que representa se o usuário tem um app que permite solicitar uma corrida)
#Você deve usar declarações condicionais para determinar se o deslocamento é possível com base nos valores dessas variáveis.
#Você deve usar as declarações if, elif e else para avaliar as categorias de distância em ordem crescente.
#Se distance_mi for um valor falso:
#Você deve imprimir False.
##Se a distância for menor ou igual a 1 milha:
##Você deve imprimir True somente se não estiver chovendo.
##Caso contrário, você deve imprimir False.
#Se a distância for maior que 1 milha e menor ou igual a 6 milhas:
#Você deve imprimir True somente se a pessoa tiver uma bicicleta e não estiver chovendo.
#Caso contrário, você deve imprimir False.
#Se a distância for maior que 6 milhas:
#Você deve imprimir True se a pessoa tiver um carro ou um aplicativo de carona.
#Caso contrário, você deve imprimir False.

distance_mi = 1
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True

if not distance_mi:
    print('False')
elif distance_mi <= 1:
    if not is_raining:
        print('True')
    else:
        print('False')
elif distance_mi <= 6:
    if has_bike and not is_raining:
        print('True')
    else:
        print('False')
else:
    if has_car or has_ride_share_app:
        print('True')
    else:
        print('False')