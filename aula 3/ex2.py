nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))


resultado = (nota1+nota2+nota3) / 3

media = 7.0

print (f"media : {media}")

if resultado >= media:
    print(f"aprovado com a media de: {resultado}")
elif resultado < media:
    print(f"Reprovado com a media de: {resultado}")