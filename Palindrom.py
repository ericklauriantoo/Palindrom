import os

def palindrom(n):
    inputan_awal = n
    inputan_akhir = ""
    for i in range(len(n)-1,-1,-1):
        inputan_akhir = inputan_akhir + inputan_awal[i]
    if inputan_awal == inputan_akhir :
        print("\n====================================================")
        print(f">>> Kata dari {inputan_awal} merupakan PALINDROM")
    else :
        print("\n====================================================")
        print(f">>> Kata dari {inputan_awal} BUKAN merupakan PALINDROM")

while True :
    os.system("cls")
    try :
        print("Program Untuk Mengecek Palindrom / Bukan")
        print("========================================")
        inputan = input("Masukan Kata Yang Ingin Di Cek : ")

    except ValueError:
        print(">>> Error : Mohon masukan data inputan berupa STRING")

    except Exception as e :
        print(f">>> Error : {e}")

    else :
        palindrom(inputan)
        print()
        print()        
        while True :
            ulang = input("Apakah Anda Ingin Mengulang [y/n] ? : ")
            if ulang in ("y","n"):
                break
            else :
                continue
        if ulang == "y":
            continue
        elif ulang == "n":
            print("\n***Selamat Tinggal***\n")
            break