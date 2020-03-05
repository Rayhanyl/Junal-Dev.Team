def haha():
    user = "udin" # yg benar
    passw = "123" # yg benar
    status = True # nyimpen status
    username = "" # numpang aja
    password = "" # numpang aja
    while status: # ngecek status
        username = input("Masukan Username : ") #minta inputan
        password = input("Masukan Password : ") #minta inputan
        if username == user and password == passw: #cek user atau pass benar
            print("Kamu Masuk") #  tampil berhasil
            status = False # ubah status salah
        else:
            print("salah") # tampil apa hayoo

haha()