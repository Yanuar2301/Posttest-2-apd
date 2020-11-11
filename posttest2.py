print("-----Aplikasi Konversi Suhu-----")
celsius = "Celsius"
fahrenheit = "Fahrenheit"
kelvin = "Kelvin"
reamur = "Reamur"
def mulai():
    print("Ingen Mengkonversi dari")
    suhu = ("1. Celsius","2. Fahrenheit","3. Kelvin","4. Reamur","5. Keluar")
    print(suhu[0])
    print(suhu[1])
    print(suhu[2])
    print(suhu[3])
    print(suhu[4])
    pilihan = int(input("Masukan Pilihan Anda! = "))
    if pilihan == 1:
        print("Konversi menuju")
        ke_suhu = ("1. Fahrenheit","2. Kelvin","3. Reamur","4. Keluar")
        print(ke_suhu[0])
        print(ke_suhu[1])
        print(ke_suhu[2])
        print(ke_suhu[3])
        ke = int(input("Masukan Pilihan Anda! = "))
        if ke == 1:
            celsiusfahrenheit()
        elif ke == 2:
            celsiuskelvin()
        elif ke == 3:
            celsiusreamur()
        elif ke == 4:
            selesai()
        else:
            print("Masukan Pilihan Yang Benar!")
            celsiuske()
    elif pilihan == 2:
        print("Konversi menuju")
        ke_suhu = ("1. Celsius","2. Kelvin","3. Reamur","4. Keluar")
        print(ke_suhu[0])
        print(ke_suhu[1])
        print(ke_suhu[2])
        print(ke_suhu[3])
        ke = int(input("Masukan Pilihan Anda! = "))
        if ke == 1:
            fahrenheitcelsius()
        elif ke == 2:
            fahrenheitkelvin()
        elif ke == 3:
            fahrenheitreamur()
        elif ke == 4:
            selesai()
        else:
            print("Masukan Pilihan Yang Benar!")
            fahrenheitke()
    elif pilihan == 3:
        print("Konversi menuju")
        ke_suhu = ("1. Celsius","2. Fahrenheit","3. Reamur","4. Keluar")
        print(ke_suhu[0])
        print(ke_suhu[1])
        print(ke_suhu[2])
        print(ke_suhu[3])
        ke = int(input("Masukan Pilihan Anda! = "))
        if ke == 1:
            kelvincelsius()
        elif ke == 2:
            kelvinfahrenheit()
        elif ke == 3:
            kelvinreamur()
        elif ke == 4:
            selesai()
        else:
            print("Masukan Pilihan Yang Benar!")
            kelvinke()
    elif pilihan == 4:
        print("Konversi menuju")
        ke_suhu = ("1. Celsius","2. Fahrenheit","3. kelvin","4. Keluar")
        print(ke_suhu[0])
        print(ke_suhu[1])
        print(ke_suhu[2])
        print(ke_suhu[3])
        ke = int(input("Masukan Pilihan Anda! = "))
        if ke == 1:
            reamurcelsius()
        elif ke == 2:
            reamurfahrenheit()
        elif ke == 3:
            reamurkelvin()
        elif ke == 4:
            selesai()
        else :
            print("Masukan Pilihan Yang Benar!")
            reamurke()
    elif pilihan == 5:
        selesai()
    else:
        print("Masukan Pilihan Yang Benar!")
        mulai()
        
def celsiuske():
    print("Konversi ke")
    ke_suhu = ("1. Fahrenheit","2. Kelvin","3. Reamur","4. Keluar")
    print(ke_suhu[0])
    print(ke_suhu[1])
    print(ke_suhu[2])
    print(ke_suhu[3])
    ke = int(input("Masukan Pilihan Anda! = "))
    if ke == 1:
            celsiusfahrenheit()
    elif ke == 2:
            celsiuskelvin()
    elif ke == 3:
            celsiusreamur()
    elif ke == 4:
            selesai()
    else:
        print("Masukan Pilihan Yang Benar!")
        celsiuske()
def fahrenheitke():
    print("Konversi ke")
    ke_suhu = ("1. Celsius","2. Kelvin","3. Reamur","4. Keluar")
    print(ke_suhu[0])
    print(ke_suhu[1])
    print(ke_suhu[2])
    print(ke_suhu[3])
    ke = int(input("Masukan Pilihan Anda! = "))
    if ke == 1:
        fahrenheitcelsius()
    elif ke == 2:
        fahrenheitkelvin()
    elif ke == 3:
        fahrenheitreamur()
    elif ke == 4:
        selesai()
    else:
        print("Masukan Pilihan Yang Benar!")
        fahrenheitke()
def kelvinke():
    print("Konversi ke ")
    ke_suhu = ("1. Celsius","2. Fahrenheit","3. Reamur","4. Keluar")
    print(ke_suhu[0])
    print(ke_suhu[1])
    print(ke_suhu[2])
    print(ke_suhu[3])
    ke = int(input("Masukan Pilihan Anda! = "))
    if ke == 1:
        kelvincelsius()
    elif ke == 2:
        kelvinfahrenheit()
    elif ke == 3:
        kelvinreamur()
    elif ke == 4:
        selesai()
    else :
       print("Masukan Pilihan Yang Benar!")
       kelvinke()
def reamurke():
    print("Konversi ke ")
    ke_suhu = ("1. Celsius","2. Fahrenheit","3. kelvin","4. Keluar")
    print(ke_suhu[0])
    print(ke_suhu[1])
    print(ke_suhu[2])
    print(ke_suhu[3])
    ke = int(input("Masukan Pilihan Anda! = "))
    if ke == 1:
        reamurcelsius()
    elif ke == 2:
        reamurfahrenheit()
    elif ke == 3:
        reamurkelvin()
    elif ke == 4:
        selesai()
    else:
        print("Masukan Pilihan Yang Benar!")
        reamurke()
def ulang():
    print("Apakah Anda Ingin Mengkonversi lagi?")
    Ya_Tidak = ("Ya","Tidak")
    print(Ya_Tidak[0])
    print(Ya_Tidak[1])
    tanya = str(input("= "))
    if tanya == ("Ya"):
        mulai()
    elif tanya == ("Tidak"):
        selesai()
    elif tanya != "Ya" or tanya != "Tidak":
        print("Masukan Pilihan Yang Benar!")
        ulang()
def selesai():
    print("-----Terima Kasih Telah menggunakan Aplikasi kami-----")
def celsiusfahrenheit():
    cel = float(input("Masukan Suhu Celsius! = "))
    fah = 9/5 * cel + 32
    print(fah,fahrenheit)
    ulang()
def celsiuskelvin():
    cel = float(input("Masukan Suhu Celsius! = "))
    kel = cel + 273.15
    print(kel,kelvin)
    ulang()
def celsiusreamur():
    cel = float(input("Masukan Suhu Celsius! = "))
    rea = 4/5 * cel 
    print(rea,reamur)
    ulang()
def fahrenheitcelsius():
    fah = float(input("Masukan Suhu Fahrenheit! = "))
    cel = (fah-32) * 5/9
    print(cel,celsius)
    ulang()
def fahrenheitkelvin():
    fah = float(input("Masukan Suhu Fahrenheit! = "))
    kel = (fah-32)*5/9+273
    print(kel,kelvin)
    ulang()
def fahrenheitreamur():
    fah = float(input("Masukan Suhu Fahrenheit! = "))
    rea = (fah-32)*4/9
    print(rea,reamur)
    ulang()
def kelvincelsius():
    kel = float(input("Masukan Suhu Kelvin! = "))
    cel = kel - 273
    print(cel,celsius)
    ulang()
def kelvinfahrenheit():
    kel = float(input("Masukan Suhu Kelvin! = "))
    fah = (kel-273)*9/5+32
    print(fah,fahrenheit)
    ulang() 
def kelvinreamur():
    kel = float(input("Masukan Suhu Kelvin! = "))
    rea = (kel-273)*4/5
    print(rea,reamur)
    ulang()
def reamurcelsius():
    rea = float(input("Masukan Suhu Reamur! = "))
    cel = 5/4*rea
    print(cel,celsius)
    ulang()
def reamurfahrenheit():
    rea = float(input("Masukan Suhu Reamur! = "))
    fah = 9/4*rea+32
    print(fah,fahrenheit)
    ulang()
def reamurkelvin():
    rea = float(input("Masukan Suhu Reamur! = "))
    kel = 5/4*rea+273
    print(kel,kelvin)
    ulang()
mulai()