while True:
    try:
        level = input("Masukkan Level kamu: ")
        level = int(level)
        print(level)
    except ValueError:
        print("YAng kamu masukkan bukan angka!")