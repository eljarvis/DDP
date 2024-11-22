#Buatlah sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius. Fungsi ini harus mengembalikan suhu yang dikonversi ke Fahrenheit.
#print(celcius_ke_fahrenheit(0))    # Output: 32.0
#print(celcius_ke_fahrenheit(100))  # Output: 212.0

def celcius_ke_fahrenheit(celcius):
    hasil_konversi = celcius *9/5 + 32
    return hasil_konversi

print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))

print("================")





#soal no 2
#Buatlah sebuah fungsi bernama is_genap yang menerima satu argumen: bilangan bulat. Fungsi ini harus mengembalikan True jika bilangan tersebut genap, dan False jika bilangan tersebut ganjil.
#print(is_genap(4))  # Output: True
#print(is_genap(7))  # Output: False

def is_genap(angka):
    return angka % 2 == 0
print(is_genap(4))

print("===================")



#soal no3
#Buatlah fungsi untuk melihat ketrangan lulus atau tidak lulus : 
#nilai (80) #lulus
#nilai(60) #gagal

def nilai(skor):
    if skor >= 75:
        print(f"Nilai {skor}: Lulus")
    else:
        print(f"Nilai {skor}: Tidak Lulus")


nilai(80)  
nilai(60)  


print("===================")
    





#soal no 4
#Buatlah fungsi untuk menampilkan bilangan ganjil yang kurang argumens
#bilangan(20) # 1,3,5,7,9,11,13,15,17,1


def bilangan(batas):
    for i in range(1, batas + 1):
        if i % 2 != 0:
            print(i, end=",")
    print() 

print("Bilangan ganjil sampai 20:")
bilangan(20)