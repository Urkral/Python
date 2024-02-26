n1 = float(input("Entrez votre premier nombre: "))
n2 = float(input("Entrez votre deuxiéme nombre: "))
op = input("Entrez l'opération que vous désirez faire (/.-.*.+): ")
answer = float

if (op == "+"):
        answer = n1 + n2
        print("La solution est", answer)
elif (op == "-"):
    answer = n1 - n2
    print("La solution est", answer)
elif (op == '*'):
    answer = n1 * n2
    print("La solution est", answer)
elif (op == "/" and n2 == 0):
    while (n2 == 0):
        print("Erreur division par 0 impossible")
        n2 = float(input("Entrez a nouveau votre deuxiéme nombre: ")) 
        answer = n1/n2
        print("La solution est", answer)
        break
