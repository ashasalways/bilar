import bil

looping=True
Bmw_svart = bil.Bil("Bmw", "svart", "0")
Merca_gul = bil.Bil("Merca", "gul", "3")
Mitsubishi_röd = bil.Bil("Mitsubishi", "röd", "12")
Volvo_blå = bil.Bil("Volvo", "blå", "137")
Saab_vit = bil.Bil("Saab", "vit", "8")

billista = [Bmw_svart, Merca_gul, Mitsubishi_röd, Volvo_blå, Saab_vit]

print(Bmw_svart.getFabrikat())

while looping:

    i = 0

    for bil in billista:
        print(str(i+1) + " Fabrikat: " + bil.getFabrikat() + ", Färg: " + bil.getColor() )
        i += 1

    bil_nr = input("\nMata in bilnr för vald bil: ")

    print("\nEn " + billista[int(bil_nr) -1].fabrikat + ", Färg: " + billista[int(bil_nr) -1].color )

    svar_anvandare = input("\nVill du avsluta programmet? j/n : \n")

    if (svar_anvandare == "j"):
        break
