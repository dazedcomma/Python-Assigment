def convertion():
    print("Pilihan konversi: ")
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")
    print("3. Decimal to Hexadecimal")
    print("4. Hexadecimal to Decimal")
    print("5. Berhenti")
    choice = input("Pilih jenis konversinya: ")

    if choice == 1:
        num = input("Berika bilangan integer positif dalam representasi decimal: ")
        positif(num)
        DecBin(num)
        convertion()
    elif choice == 2:
        num = input("Berikan bilangan integer positif dalam representasi binary: ")
        positif(num)
        BinDec(num)
        convertion()
    elif choice == 3:
        num = input("Berikan bilangan integer positif dalam representasi decimal: ")
        positif(num)
        DecHex(num)
        convertion()
    elif choice == 4:
        num = raw_input("Berikan input string dalam representasi hexadecimal: ")
        str_positif(num)
        convertion()
    elif choice == 5:
        print("Terima Kasih")


def positif(num):
    if (num < 0):
        print("Sorry,harus bilangan positif")
        convertion()
    else:
        return (num)


def str_positif(num):
    huruf = 'ABCDEF'
    angka = '0123456789'
    panjang = len(num)
    r = []
    for x in num:
        if x not in huruf and x not in angka:
            print('Masukan harus dalam bentuk hexadecimal')
            break
        else:
            r.append(x)
        f = ''.join(str(e) for e in r)
        g = len(f)
        if g == panjang:
            HexDec(num)


def BinDec(num):
    a = str(num)
    numlist = list(a)
    n = len(list(a))
    decimal = 0
    tampung = 0
    i = 0
    x = n - 1
    while (i < n):
        var_a = int(numlist[i])
        pangkat = 2 ** x
        tampung = var_a * pangkat
        i += 1
        x -= 1
        decimal = decimal + tampung
    print("Representasi decimal dari " + str(num) + " adalah " + str(decimal))


def DecBin(n):
    num = str(n)
    s = []
    while (1 <= n):
        x = n % 2
        n = (n - x) / 2
        # print(x)
        s.append(x)
        # print(n)
    s.reverse()
    f = ''.join(str(e) for e in s)
    print("Representasi binary dari " + num + " adalah " + f)


def DecHex(num):
    x = num
    # print(x)
    s = []
    while (1 <= x):
        n = x % 16
        x = x // 16
        # print(x)
        s.append(n)
    s.reverse()
    hex_ext2(s)
    f = ''.join(str(e) for e in s)
    print("Representasi binary dari " + str(num) + " adalah " + f)


def hex_ext2(numList):
    n = range(len(numList))
    for i in n:
        if numList[i] == 10:
            numList[i] = "A"
        elif numList[i] == 11:
            numList[i] = "B"
        elif numList[i] == 12:
            numList[i] = "C"
        elif numList[i] == 13:
            numList[i] = "D"
        elif numList[i] == 14:
            numList[i] = "E"
        elif numList[i] == 15:
            numList[i] = "F"


def HexDec(num):
    numlist = list(num)
    hex_ext(numlist)
    n = len(list(num))
    hexa = 0
    tampung = 0
    i = 0
    x = n - 1
    while (i < n):
        y = int(numlist[i])
        pangkat = 16 ** x
        tampung = y * pangkat
        i += 1
        x -= 1
        hexa = hexa + tampung
    print("Representasi decimal dari " + num + " adalah " + str(hexa))


def hex_ext(numList):
    n = range(len(numList))
    for i in n:
        if (numList[i] == "A"):
            numList[i] = 10
        elif (numList[i] == "B"):
            numList[i] = 11
        elif (numList[i] == "C"):
            numList[i] = 12
        elif (numList[i] == "D"):
            numList[i] = 13
        elif (numList[i] == "E"):
            numList[i] = 14
        elif (numList[i] == "F"):
            numList[i] = 15
convertion()
