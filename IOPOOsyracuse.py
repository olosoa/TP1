class TP:


        def syra(self):
                print("nombre de depart ? ")
                n=int(input())

                sr=[n]
                while n!=1:
                    if n%2 == 0:
                        n = n//2
                    else:
                        n=3*n + 1


                    sr.append(n)
                
                return (sr)

        def ecr(self):
            with open("syracuse.py", "a") as fichier:
                fichier.write("\n#Test en ecriture")

        def li(self):
            with open("syracuse.py", "r") as fichier:
                print (fichier.read())      

resultat=TP()
print (resultat.syra())

print(resultat.ecr())
print(resultat.li())


#with open("syracuse.py", "a") as fichier:
#    fichier.write("\n#Test en ecriture")

#with open("syracuse.py", "r") as fichier:
#    print (fichier.read())


