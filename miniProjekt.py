class Auto:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
        self.__przebieg = 0
        self.__wypozyczone = False
    def __str__(self):
    
        if self.__wypozyczone:
            return f"{self.marka} {self.model} | Niedostępny (Wypożyczony) | Przebieg: {self.__przebieg} km"
        else:
            return f"{self.marka} {self.model} | Dostępny | Przebieg: {self.__przebieg} km"
    def wypozycz(self):
        if self.__wypozyczone == True:
            raise ValueError("Samochód niedostępny!")
        else: 
            self.__wypozyczone = True
    def zwroc(self, przejechane_km):
        self.__przebieg += przejechane_km
        self.__wypozyczone = False
        
flota = []
Porsche = Auto("Porsche", "911")
Audi = Auto("Audi", "RS6")
Bmw = Auto("BMW", "M5")
flota.append(Porsche)
flota.append(Audi)
flota.append(Bmw)

while True:
    print("[1] Pokaż flotę\n[2] Wypożycz auto\n[3] Zwróć auto\n[4] Zapisz raport i Zamknij system")
    wybor = input("Witaj w Woojciaa-Rental-Cars. Wybierz co dziś chcesz zrobić! :D\n")

    if wybor == "1":
        for idx, auto in enumerate(flota, start=1):
            print(f"[{idx}] {auto.marka} {auto.model}")
        
    elif wybor == "2":
        try:
            for idx, auto in enumerate(flota, start=1):
                print(f"[{idx}] {auto.marka} {auto.model}")
            wybor_auta = int(input("Wybierz nr swojego samochodu!\n"))
            wybor_auta -= 1
            flota[wybor_auta].wypozycz()
            print(f"{wybor_auta} to świetny wybor!")
        except ValueError as e:
            print(e)
        finally:
            print("Bardzo dziekujemy za skorzystanie z naszych usług!")
    elif wybor == "3":
        for idx, auto in enumerate(flota, start=1):
            print(f"[{idx}] {auto.marka} {auto.model}")

        wybor_auta = int(input("Wybierz nr samochodu ktory chcesz zwrocic!\n"))
        wybor_auta -= 1 
        przejechane_km = int(input("Podaj ilosc km ktore przejechales\n"))
        flota[wybor_auta].zwroc(przejechane_km)
        print(f"Twoj samochod {flota[wybor_auta]} został prawidłowo zwrócony, a jego aktualny przebieg to {self.__przebieg}\n")

    elif wybor == "4":
        for auto in flota:
            with open("raporty_floty.txt", "w", encoding="utf-8") as plik:
                plik.write(auto)
    else:
        print("Wybor nie prawidłowy, wybierz opcje 1-4!")
        



    



