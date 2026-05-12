#print(bool(False)) # False
#print(bool(1))  # False
#print(bool('')) # False

#print(bool(True)) # True
#print(bool(1)) # True
#print(bool('Hello')) # True


voto = False
idade = 19


if voto and idade >= 18: # as duas variaves precisam ser true para cair na condição verdadeira. 
    print("voce pode votar")
else:
    print("voce não pode votar")