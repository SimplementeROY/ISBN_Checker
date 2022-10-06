
with open("path_del_archivo_de_los_ISBN") as f:
    eskere = f.read()
    numbers = eskere.replace('-','').replace('\n','')
    n = 1
    number = [numbers[i:i+n] for i in range(0, len(numbers), n)]
    x = 10
    subList = [number[t:t+x] for t in range(0, len(number), x)]
    
    for i in subList:
        digito1 = int(i[0]) * 10
        digito2 = int(i[1]) * 9
        digito3 = int(i[2]) * 8
        digito4 = int(i[3]) * 7
        digito5 = int(i[4]) * 6
        digito6 = int(i[5]) * 5
        digito7 = int(i[6]) * 4
        digito8 = int(i[7]) * 3
        digito9 = int(i[8]) * 2
        digito10 = int(i[9]) * 1

        suma = digito1 + digito2 + digito3 + digito4 + digito5 + digito6 + digito7 + digito8 + digito9 + digito10
        if suma % 11 == 0:
            
            eskree = ''.join(i)
            print(eskree)
            
# Ejecuta primero el comando de arriba y guardalo

with open("ruta_del_archivo_de_los numeros_ISBN") as numbers:
    f = numbers.read()
    flag = []
    for i in f:
        bandera = flag.append(i)
        numbs = [int(val) for val in bandera]
        print(sum(numbs))
            
            
                

        
            
