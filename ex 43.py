
print("""

*********************CÁLCULO DE IMC*********************

    Vamos calcular o seu índice de massa córporea.
    Para isso precisamos de algumas informações.
                    Vamos lá!
                    
********************************************************

""")
while True:
    peso_str=str(input("Seu Peso: "))
    altura_str=str(input("Sua altura: "))

    peso_str = peso_str.replace(',', '.')
    altura_str = altura_str.replace(',', '.')

    peso = float(peso_str)
    altura = float(altura_str)

    if peso<=0 or altura <=0:
        print("\n\aAtenção, digite valores válidos.\n")
    else:
        break




imc=peso/altura**2

if imc<18.5:
    print(f"Seu IMC é {imc:.1f}. Você está abaixo do peso.")

elif imc<25:
    print(f"Seu IMC é {imc:.1f}. Você está no peso ideal.")

elif imc<30:
    print(f"Seu IMC é {imc:.1f}.Você está com sobrepeso.")

elif imc<40:
    print(f"Seu IMC é {imc:.1f}. Você está obeso.")

else:
    print(f"Seu IMC é {imc:.1f}. Você está com obesidade mórbida.")