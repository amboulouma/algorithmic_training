nbPages = int(input())
for idPage in range(2, nbPages+1):
   page = input()
   if idPage % 2 == 0:
      decalage = -3 * idPage
   else:
      decalage = 5 * idPage
   for idCaractere in range(len(page)):
      caractere = page[idCaractere]
      if caractere.isalpha():
         isMaj = caractere.isupper()
         if isMaj:
            caractere = caractere.lower()
         numero = (ord(caractere) - ord("a") + decalage) % 26
         caractere = chr(numero + ord("a"))
         if isMaj:
            caractere = caractere.upper()
      print(caractere, end = "")
   print()