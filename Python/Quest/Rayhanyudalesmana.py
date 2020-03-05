#mahasiswa = ["Rayhan",2,"Teknik Informatika"]
#print(mahasiswa[0:2])

#nama = "rayhan whoo ouuu aaa eee"
#game = "Mobile Legend"
#print(game[8:11])

#angka = 6

#if angka == 5:
#    print("Uhuy")
#else:
#    print("Edan")


#hero = "layla"

#if hero is "Zilong":
#    print(hero, "fighter Bos")
#elif hero is "layla":
#    print(hero, "Marksman Bos")    
#else:
#    print("Hero nya Leungit")
    
#angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#hari = ["Senin", "Selasa", "Rabu", "kamis", "jum'at", "Sabtu", "Minggu"]

#for i in hari:
#    print(i)
    
#for i in range(0, 10, 2):
#    if i is 4:
#        print ("Dah Lah")
#        break
#    print(i)
    
#for i in range(0, 10, 2):
#    if i is 4:
#        print ("Dah Lah")
#        continue
#    print(i)

#angka = 0
#while angka < 5:
#    print(angka)
#    angka+=1




user = "udin"
passw = "123"

username = input("Masukan Username : ")
password = input("Masukan Password : ")

while username != user or password != passw:
    if username and password == user and passw: 
        print("Kamu Masuk")
    else:
        print("salah")    
        username = input("Masukan Username : ")
        password = input("Masukan Password : ")
