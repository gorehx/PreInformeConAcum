#Un algoritmo que imprima los números pares entre 1 y 30.
cont=0
for num in range (1,31):
  if num%2==0:
    print(num)
  cont=cont+1