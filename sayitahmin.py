import random

sayi = random.randint(1, 100)

dongu = range(5)

tamam = False

for i in dongu:
    if tamam == 0 and i != 1:
        print("Sayı girin: ")
        x = int(input())
        if x < sayi:
            print("Daha büyük sayı girin.")
        elif x > sayi:
            print("Daha küçük sayı girin.")
        else:
            print("Doğru sayıyı girdiniz!")
            tamam = True

print("Sayı girin: ")
x = int(input())
if x == sayi:
    print("Bildiniz.")
else:
    print('Bilemediniz. Doğru sayı: {}'.format(sayi))