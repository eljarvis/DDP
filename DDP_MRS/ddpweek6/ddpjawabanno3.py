isUser = int(input("Masukkan angka = "))  # Perbaiki penamaan dan format input

# Segitiga Bintang Meningkat
for k in range(1, isUser + 1):
    print("*" * k)

print("\n==============\n")

# Segitiga Bintang Segitiga
for h in range(1, isUser + 1):
    for g in range(h):
        print("*", end="")
    print()  # Pindah ke baris baru setelah selesai mencetak bintang pada satu baris
