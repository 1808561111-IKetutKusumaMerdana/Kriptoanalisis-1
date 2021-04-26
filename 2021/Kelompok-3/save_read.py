from enum_sha256 import hash_enum
import sys


def savetxt():
    conf = input("Save Hash to Database [y/n]? ")  # konfirmasi untuk menyimpan
    if conf.lower() in ['y', 'yes']: # menyimpan hasil keluaran refrensi standar
        original_stdout = sys.stdout
        with open('hashdb.txt', 'w') as file:
            sys.stdout = file
            print('CHR                            HASH SHA256')
            print(
                '======================================================================')
            print(hash_enum())
            # setel ulang keluaran
            sys.stdout = original_stdout
        print('Sukses!')
    elif conf.lower() in ['t','T', 'tidak']:
        print('Hash tidak disimpan!')


def readtxt():
    # membaca hash dari hashdb.txt
    string_file = open("hashdb.txt", "r")
    # isi string dengan input data dari dbhash.txt
    string = string_file.read()
    return string