"""READ : r
    WRITE : w // menghapus data dan menulis kembali && kalo file belum ada maka auto buat file
    APPEND : a // menambali data
    READ AND WRITE : r+"""

""" this is read file
my_file = open("users.txt", "r")
print(my_file.read())
my_file.close()"""

my_file = open("users.txt", "a")
print(my_file.write("\nRiskyan - User"))

my_file.close()