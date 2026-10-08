import random as rn
import time

num = rn.randint(2, 100)
ran = [1, 100]

def randomNumber(ran):
    return rn.randint(ran[0], ran[1])

def randomNumSPECIAL(ran):
    return rn.randint(ran[0], ran[1])

def split(num, ran, Inum):

    if Inum > num:
        ran[0] = num
        return ran, False

    if Inum < num:
        ran[1] = num
        return ran, False

    if Inum == num:
        ran[0] = num
        ran[1] = num
        return ran, True

def repeat():
    print("Quantes vegades vols repetir la busqueda del número?")
    sel = int(input(">>> "))

    return sel

def Ologn():
    

    sel = repeat()
    trobat = []
    inicio = time.perf_counter()
    while sel != 0:
        ran = [0, 10000]
        Inum = randomNumber(ran)
        fin = False
        while fin != True:
            num = randomNumSPECIAL(ran)
            ran, fin = split(num, ran, Inum)
            #print(f"Rango {ran} ||| Numero {num}")
        print(f"TROBAT: {Inum}")
        trobat.append(num)
        sel -= 1
        #print("================================================")
    print(trobat)
    final = time.perf_counter()
    tiempo = final - inicio
    print(f"Tiempo: {tiempo:.6f} segundos")
    print(f"Tiempo: {tiempo * 1000:.3f} ms")

def On():
    sel = repeat()
    trobat = []
    inicio = time.perf_counter()
    while sel != 0:
        ran = [0, 10000]
        Inum = randomNumber(ran)

        for num in range(ran[0], ran[1] + 1):
            #print(f"Numero: {num}")
            if num == Inum:
                print(f"TROBAT: {Inum}")
                trobat.append(num)
                break

        sel -= 1
    print(trobat)
    final = time.perf_counter()
    tiempo = final - inicio
    print(f"Tiempo: {tiempo:.6f} segundos")
    print(f"Tiempo: {tiempo * 1000:.3f} ms")

def O1():
    sel = repeat()
    trobat = []
    inicio = time.perf_counter()

    while sel != 0:
        ran = [0, 10000]
        Inum = randomNumber(ran)

        num = Inum
        if num == Inum:
            print(f"TROBAT: {num}")
            trobat.append(num)

        sel -= 1
    print(trobat)
    final = time.perf_counter()
    tiempo = final - inicio
    print(f"Tiempo: {tiempo:.6f} segundos")
    print(f"Tiempo: {tiempo * 1000:.3f} ms")

def On2():
    sel = repeat()
    trobat = []
    inicio = time.perf_counter()

    while sel != 0:
        ran = [0, 10000]
        Inum = randomNumber(ran)

        for i in range(ran[0], ran[1] + 1):
            for j in range(ran[0], ran[1] + 1):
                #print(f"{i}, {j}")

                if i == Inum and j == Inum:
                    print(f"TROBAT: {Inum}")
                    trobat.append(Inum)
                    break

        sel -= 1

    print(trobat)
    final = time.perf_counter()
    tiempo = final - inicio
    print(f"Tiempo: {tiempo:.6f} segundos")
    print(f"Tiempo: {tiempo * 1000:.3f} ms")

def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    mitad = len(lista) // 2

    izquierda = merge_sort(lista[:mitad])
    derecha = merge_sort(lista[mitad:])

    resultado = []
    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado


def Onlogn():
    sel = repeat()
    trobat = []
    inicio = time.perf_counter()

    while sel != 0:
        ran = [0, 10000]
        Inum = randomNumber(ran)

        numeros = list(range(ran[0], ran[1] + 1))

        numeros = merge_sort(numeros)

        if Inum in numeros:
            print(f"TROBAT: {Inum}")
            trobat.append(Inum)

        sel -= 1

    print(trobat)
    final = time.perf_counter()
    tiempo = final - inicio
    print(f"Tiempo: {tiempo:.6f} segundos")
    print(f"Tiempo: {tiempo * 1000:.3f} ms")

if __name__ == "__main__":
    user = 999999999
    while user != 0:
        print("""Tria la magnitud per la que vols buscar:\n
        [0] SORTIR\n
        [1] O(log n)\n
        [2] O(n)\n
        [3] O(1)\n
        [4] O(n^2)\n
        [5] O(n log n)""")

        user = int(input("\n>>> "))
        if user == 1:
            Ologn()
            print()
        elif user == 2:
            On()
            print()
        elif user == 3:
            O1()
            print()
        elif user == 4:
            On2()
            print()
        elif user == 5:
            Onlogn()
            print()