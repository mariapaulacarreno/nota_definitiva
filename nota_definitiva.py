# programa para calcular nota definitiva en el colegio guanenta 

print("---------------")
print("nota definitiva")
print("---------------")

nc= int(input("ingrese la nota cognitiva (10 a 50): "))
nd= int(input("digite la nota procedimental: "))
na= int(input("ingrese la nota actitudinal: "))
au= int(input("ingrese la nota de la autoevalucion: "))
bi= int(input("ingrese la nota de la bimestral: "))

#processig 

nd= (3*nc + 3*np + 1*na + 1*au + 2*bi) // 10
nd= int(nd)

print("la nota definitiva es:", nd)
