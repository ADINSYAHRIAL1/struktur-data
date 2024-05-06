# Perbandingan
# lebih besar >
# lebih kecil <
# lebih besar sama dengan >=
# lebih kecil sama dengan <=
# sama dengan ==
# tidak sama dengan !=
# sama "is"
# tidak sama "is not"

x = 4
y = 5

hasil = x > y

# lebih besar >
hasil = x > y
print(x, '>', y, 'adalah', hasil)

# lebih kecil <
hasil = x < y
print(x, '<', y, 'adalah', hasil)

# lebih besar sama dengan >=
hasil = x >= 2
print(x, '>=', 2, 'adalah', hasil)
print(x, '>=', 4, 'adalah', hasil)

# lebih kecil sama dengan <=
hasil = x <= 2
print(x, '<=', 2, 'adalah', hasil)
hasil = x <= 4
print(x, '<=', 4, 'adalah', hasil)
hasil = x <= y
print(x, '<=', y, 'adalah', hasil)

# sama dengan ==
hasil = x == 7
print(x, '==', 7, 'adalah', hasil)

# tidak sama dengan !=
hasil = x != 7
print(x, '!=', 7, 'adalah', hasil)

# > < >= <= == != ini adalah perbandingan literal
# x= 4, 4 = literal (tidak memakan memory)
# x = objek (memory)
# 
# x = 4 (bisa)
# x isi 4 (tidak bisa, karna yang dibandingkan adalah literal)
# x is y (bisa, karna yang dibandingkan adalah object)

# is dan not
hasil = x is 4
print(x, 'is', y, 'adalah', hasil)

hasil = x is 4
print(x, 'is not', 4, 'adalah', hasil)







