print('''
=== Kalkulator Sederhana ===
Operasi yang Tersedia:
Penjumlahan: +
Pengurangan: -
Perkalian: *
Pembagian: /
Lower-division: //
Exponent: **
''')
x1 = float(input("Masukkan Angka Pertama: "))
x2 = float(input("Masukkan Angka Kedua: "))
operation =  input("Masukkan Operasi: ")

if operation == "+":
    total = x1 + x2
    print(f"Total: {total}")
elif operation == "-":
    total = x1 - x2
    print(f"Total: {total}")
elif operation == "*":
    total = x1 * x2
    print(f"Total: {total}")
elif operation == "/":
    if( x2 == 0):
        print("Error: Pembagian dengan nol tidak diperbolehkan.")
    else:
        total = x1 / x2
        print(f"Total: {total}")
elif operation == "//":
    total = x1 // x2
    print(f"Total: {total}")
elif operation == "**":
    total = x1 ** x2
    print(f"Total: {total}")
else:
    print("Operasi invalid")