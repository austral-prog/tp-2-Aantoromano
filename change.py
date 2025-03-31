def change():
    expense = 23.75
    money = 100

    vuelto= money - expense #Vale 76.25 

    Pesos= int(vuelto)

    #Para los centavos
    Centavos= int ((vuelto - Pesos) * 100)

    print (f"Ingresar gasto:\n{expense}\nDinero recibido\n{money}")
    print ()
    print ("Vuelto")
    print ()
    print (f"Pesos:\n{Pesos}\nCentavos:\n{Centavos}")
