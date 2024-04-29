# input dari user
# aitmatika

# Belajar Inputan
adins = input("masukkan kata : ")
print("isi dari adins : ", adins, "bertype data :", type adins)

#belajar aritmatika dasar
x = 10
y = 9

# penjumlahan 
hasil = x + y
print ("x + y =", hasil)

# pengurangan
hasil = x - y
print ("x - y =", hasil)

# pembagian 
hasil = x / y
print ("x : y =", hasil)

# perkalian
hasil = x * y
print ("x * y =", hasil)

# perpangkatan exponen **
hasil = x ** y
print ("x ^ y =", hasil)

# modulus %
hasil = x % y
print ("x % y =", hasil)


# floor division (pembulatan kebawah)//
hasil = x // y
print ("x // y =",hasil)

# aritmatika prioritas 
# (), exponen, perkalian/pembagian, penjumlahan/pengurangan
x = 1
y = 9
z = 4

hasil = (x ** y * (z + x) / y - z % x // y)
print(hasil)