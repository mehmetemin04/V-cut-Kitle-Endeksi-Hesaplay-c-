boy = float(input("Boyunuz(ör: 1.76): "))
kilo = int(input("Kilonuz(ör:72): "))
vucud_Kitle_Endeksi  =  (kilo)/(boy**2)

zayif= (vucud_Kitle_Endeksi > 0) and (vucud_Kitle_Endeksi < 18.4)
normalKilolu = (vucud_Kitle_Endeksi > 18.5) and (vucud_Kitle_Endeksi < 24.9)
fazlaKilolu = (vucud_Kitle_Endeksi > 25.0) and (vucud_Kitle_Endeksi < 29.9)
obez = (vucud_Kitle_Endeksi > 30.0) and (vucud_Kitle_Endeksi < 34.9)

if zayif == True:
    print(f"Vücut kitle endeksiniz {vucud_Kitle_Endeksi:.2f} değerindedir.Buna göre zayıf konumundasınız.")


elif normalKilolu == True:
    print(f"Vücut kitle endeksiniz {vucud_Kitle_Endeksi:.2f} değerindedir.Buna göre normal kilolu konumundasınız.")
    
elif fazlaKilolu == True:
    print(f"Vücut kitle endeksiniz {vucud_Kitle_Endeksi:.2f} değerindedir.Buna göre fazla kilolu konumundasınız.")
    
elif obez == True:
    print(f"Vücut kitle endeksiniz {vucud_Kitle_Endeksi:.2f} değerindedir.Buna göre obez konumundasınız.")
    