print("nbre de depart ? ")
n = int(input())
while n != 1:
    print(n)
    if n%2 == 0:
        n = n//2
    else:
        n = 3*n + 1
print(n) #affichage du resultat et commentaire vscode
