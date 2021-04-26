from enum_sha256 import hash_enum  # mengimport modul hash
from save_read import savetxt, readtxt  # mengimport modul save dan read


def main():
    print('Program Enumerasi dan Menggabungkan SHA256')
    print("Kelompok 3 : \n- I Ketut Kusuma Merdana \n - I Gusti Ayu Mirah Agung Jayanti")
    
    print('Menu :')
   
    print("1. Mulai buat Enumerasi Hash SHA256")
    print("2. Menampilkan Database")
    menu = int(input("Choose (1/2) : "))

    if menu == 1:
        hash_enum()
        savetxt()
    elif menu == 2:
        string = readtxt()
        print(string)
    else:
        print("Tidak ada pilihan!")


main()