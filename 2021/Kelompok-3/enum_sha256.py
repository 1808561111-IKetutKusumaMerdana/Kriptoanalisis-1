import hashlib


def hash_enum():
    # membuat integer i dan j
    i = 1
    j = 1
    unichr = chr  

    while i <= 26: # perulangan untuk alfabet
        while j <= 26: 
            my_enum = unichr(i+96) + unichr(j+96)
            my_string = my_enum  # mendefiniskan string menjadi enum karakter
            string_hash = hashlib.sha256(
                my_string.encode()).hexdigest()  # hash string dengan SHA256
            print(my_enum, "--", string_hash)  # mencetak hash setiap enum karakter
            j += 1
        j = 1
        i += 1