while True:
    a = int(input("1-son: "))
    b = int(input("2-son: "))
    print(f"Yig‘indi: {a + b}")
    
    stop = input("Yana hisoblashni xohlaysizmi? (ha/yo‘q): ")
    if stop.lower() != "ha":
        break