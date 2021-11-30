# + - * /

command = ""
while command != "exit":
    command = input("Perintah: ")

    if command == "exit":
        break

    if command != "+" and command != "-" and command != "*" and command != "/":
        print("Input yang anda masukkan ga ke detect")
        continue

    a = int(input("angka pertama: "))
    b = int(input("angka kedua: "))

    if command == "+":
        result = a+b
    elif command == "-":
        result = a-b
    elif command == "*":
        result = a*b
    elif command == "/":
        result = a/b
    print(f"Hasil: {result}")

print("Thankyou")