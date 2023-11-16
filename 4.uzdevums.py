#IzveidoT Python programmu, kas aprēķina lietotāja ievadīta skaitļa faktoriālu, izmantojot for ciklu.
#Izmantot GIT, lai izsekotu kodu un veidotu komitus.
def faktiorialis(x):
    rezultats = 1
for i in range(1, x+1):
    rezultats *=i
    return rezultats
print(faktiorialis(x))