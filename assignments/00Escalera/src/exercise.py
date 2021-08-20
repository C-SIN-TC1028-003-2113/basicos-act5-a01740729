import math 
def main():
    pass
    a = float(input('Altura de la casa: '))
    b = int(input('Angulo en grados: '))

    r = math.radians(b)

    l = (a / (math.sin(b)))

    print('Largo de la escalera: '+str(math.ceil(l)))

if __name__ == '__main__':
    main()
