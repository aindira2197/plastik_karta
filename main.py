plastik_parol = "1414"
plastik_balans = 300_000

while True:
    p = input("Parol kirit: ")
    if p == plastik_parol:
        print("1.Balans korish")
        print("2.Naqd pul yechish")
        print("3.chiqish")
        t = int(input("raqam kirit: "))
        if t == 1:
            print(plastik_balans)
        elif t == 2:
            print("1) 50 000 som")
            print("2) 100 000 som")
            print("3) 500 000 som")
            print("4) Boshqa summa")
            s = int(input("Summani tanla: "))
            if s == 1:
                if 50_000 < plastik_balans:
                    plastik_balans -= 50_000
                    print(f"Plastikdan 50 000 summa qirqib olindi")
                else:
                    print("Plastikingizda yetarli summa yoq")
            elif s == 2:
                if 100_000 < plastik_balans:
                    plastik_balans -= 100_000
                    print(f"Plastikdan 100 000 summa qirqib olindi")
                else:
                    print("Plastikingizda yetarli summa yoq")
            elif s == 3:
                if 150_000 < plastik_balans:
                    plastik_balans -= 150_000
                    print(f"Plastikdan 150 000 summa qirqib olindi")
                else:
                    print("Plastikingizda yetarli summa yoq")
            elif s == 4:
                money = int(input("Summa kirit: "))
                if money < plastik_balans:
                    plastik_balans -= money
                    print(f"Plastikdan {money} summa qirqib olindi")
                else:
                    print("Plastikingizda yetarli summa yoq")

            else:
                print("Boshqa raqam kiritdiz")
        elif t == 3:
            break
    else:
        print("Parol xato kiritdiz.")
