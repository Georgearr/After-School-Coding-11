berat = int(input("enter your weight in pounds : "))
tinggi = int(input("enter your height : "))

def bmi (berat,tinggi):
    return (berat/tinggi) * 703


print(f"bmi anda adalah {bmi(berat,tinggi)}")