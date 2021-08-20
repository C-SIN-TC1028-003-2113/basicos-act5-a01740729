import math 
def main():
    pass
    a = float(input('Altura de la casa: '))
    b = int(input('Angulo en grados: '))

    r = math.radians(b)

    l = round(a / (math.sin(r)))

    print('Largo de la escalera: '+str(l))

if __name__ == '__main__':
    main()
