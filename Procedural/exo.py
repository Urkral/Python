# --------------------------------------------- Page283--------------------------------------


# text = input("Enter your message: ")
# cipher = ''
# for char in text:
#  if not char.isalpha():
#  continue
#  char = char.upper()
#  code = ord(char) + 1
#  if code > ord('Z'):
#  code = ord('A')
#  cipher += chr(code)
# print(cipher) 

# userSentence = input("Entrez la phrase que vous voulez chiffrer: ")
# userCode = int(input("Entrez vore clé de chiffrement: "))
# answer = ''

# for char in userSentence:
#     if not char.isalpha():
#         print('Erreur veillez rentrer a nouveau une valeur')
#         userSentence = input("Entrez la phrase que vous voulez chiffrer: ")

#     elif(type(userCode) != int):
#         print('Erreur veillez entrer une nouvelle valeur')
#         userCode = int(input("Entrez vore clé de chiffrement: "))

#     elif(userCode > 25):
#         print('Veillez entrer une valeur maximale de 25')
#         userCode = int(input("Entrez vore clé de chiffrement: "))

#     else:
#         char = char.upper()
#         cryptage = ord(char) + userCode
#         if(cryptage > ord('Z')):
#             cryptage = ord('A')
#         answer += chr(cryptage)
#         print(answer)

        
userSentence = input("Entrez la phrase que vous voulez chiffrer: ")
userCode = int(input("Entrez vore clé de chiffrement: "))
answer = ''
for char in userSentence:
        if not char.isalpha():
            print('Erreur veillez rentrer a nouveau une valeur')
            userSentence = input("Entrez la phrase que vous voulez chiffrer: ")
            
        while(type(userCode) != int):
                print('Erreur veillez entrer une nouvelle valeur')
                userCode = int(input("Entrez vore clé de chiffrement: "))

        while(userCode > 25):
                print('Veillez entrer une valeur maximale de 25')
                userCode = int(input("Entrez vore clé de chiffrement: "))

        else:
            char = char.upper()
            cryptage = ord(char) + userCode
            if(cryptage > ord('Z')):
                cryptage = ord(char) - 26 + userCode
            answer += chr(cryptage)
            print(answer)