class Auto:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
        self.__przebieg = 0
        self.wypozyczone = False
    def __str__(self):
    
        if self.wypozyczone:
            return f"\033[91m{self.marka} {self.model} | Niedostępny (Wypożyczony) | Przebieg: {self.__przebieg} km\033[0m"
        else:
            return f"\033[92m{self.marka} {self.model} | Dostępny | Przebieg: {self.__przebieg} km\033[0m"
    def wypozycz(self):
        if self.wypozyczone == True:
            raise ValueError("Samochód niedostępny!")
        else: 
            self.wypozyczone = True
    def zwroc(self, przejechane_km):
        if self.wypozyczone == False:
            raise ValueError("\033[91mBłąd: Ten samochód stoi obecnie na placu i nie jest wypożyczony!\033[0m")
        self.__przebieg += przejechane_km
        self.wypozyczone = False
        
flota = []
Porsche = Auto("Porsche", "911")
Audi = Auto("Audi", "RS6")
Bmw = Auto("BMW", "M5")
flota.append(Porsche)
flota.append(Audi)
flota.append(Bmw)

while True:
    print("\033[92mWitaj w Woojciaa-Rental-Cars!\033[0m")
    print("\033[93m[1] Pokaż flotę\n[2] Wypożycz auto\n[3] Zwróć auto\n[4] Zapisz raport i Zamknij system\033[0m")
    wybor = input("\033[92m\nWybierz co dziś chcesz zrobić! :D\n\033[0m")

    if wybor == "1":
        print("\n\033[92mW ofercie naszej floty aktualnie znajdują się te samochody: \n\033[0m")
        for idx, auto in enumerate(flota, start=1):
            print(f"\033[92m[{idx}] {auto}\033[0m")

        input("\033[93m\nNaciśnij Enter, aby powrócic do menu...\n\033[0m")
       
        
    elif wybor == "2":
        try:
            for idx, auto in enumerate(flota, start=1):
                print(f"\033[92m[{idx}] {auto}")
            wybor_auta = int(input("\n\033[93mWybierz nr swojego samochodu!\n\033[0m"))
            wybor_auta -= 1
            flota[wybor_auta].wypozycz()
            print(f"\033[92m{flota[wybor_auta].marka} to świetny wybor!\033[0m")
        except ValueError as e:
            print(e)
        finally:
            print("\033[92mBardzo dziekujemy za skorzystanie z naszych usług!\033[0m")
    elif wybor == "3":
        try:
            for idx, auto in enumerate(flota, start=1):
                print(f"\033[92m[{idx}] {auto}\033[0m")
           
            wybor_auta = int(input("\033[92mWybierz nr samochodu ktory chcesz zwrocic!\n\033[0m"))
            wybor_auta -= 1
            if wybor_auta > len(flota) - 1 or wybor_auta < 0:
                print("\033[91mNie mamy takiego samochodu :(\033[0m") 
                continue
            if flota[wybor_auta].wypozyczone == False:
                print("\033[91mBłąd: Ten samochód stoi obecnie na placu i nie jest wypożyczony!\033[0m")
                continue

            przejechane_km = int(input("\033[93mPodaj ilosc km ktore przejechales\n\033[0m"))
            flota[wybor_auta].zwroc(przejechane_km)
            print(f"\033[92mTwoj samochod {flota[wybor_auta].marka} został prawidłowo zwrócony.\nStatus: {flota[wybor_auta]}\n\033[0m")
        except ValueError as e:
            if "invalid literal" in str(e):
                print("\033[91mTypie miałeś jedno zadanie...(napisać ilość km.... jako liczba nie jako ciag znakow)\033[0m")
            else:
                print(e)
    elif wybor == "4":
    
        with open("przebieg_floty.txt", "a", encoding="utf-8") as plik:
            for auto in flota:
                plik.write(f"{auto}\n")
        break
    else:
        print("\033[91mWybor nie prawidłowy, wybierz opcje 1-4!\033[0m")
        



    



