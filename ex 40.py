
nota1=float(input("Primeira nota: "))
nota2=float(input("Segunda nota: "))
media=(nota1+nota2)/2

print(f"Sendo as notas {nota1} e {nota2} a média é {media:.1f}.")

if media>=7:
    print("Parabéns. Você está aprovado.")

elif 5<media<7:
    print("Você está de recuperação.")

else:
    print("Você está reprovado")