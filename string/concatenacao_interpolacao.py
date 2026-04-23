my_string1 = 'vitorio'

my_string2 = 'batista'

age = 25

my_name = my_string1 + ' '+ my_string2 # o espaço entre as duplas 

my_name = my_string1 + ' '+ my_string2 +' ' +str(age) # para concatenar outra variavel sem ser string usamos str(nomedavariavel)

concatanacao = my_string1

concatanacao += str(age)

print(concatanacao)



print(my_name)


print(f"meu nome é {my_name} e minha idade é {age}")