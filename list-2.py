# SUM menjumlahkan semua data
numbers = [5, 6, 7, 8, 1]

# cara 1
init_numbers = 0
for number in numbers:
    init_numbers += number

# cara 2
total = sum(numbers)
print(total)
print(init_numbers) 

# menampilkan angka terbesar
# cara 1
max =max(numbers)
print(max)
#cara 2
numbers.sort()
max_numbers = numbers[-1]

#cara 3
max_numbers = numbers[0]
for number in numbers:
    if number > max_numbers:
        max_numbers = number

print(max_numbers)
