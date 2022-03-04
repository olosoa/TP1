def Egypt(a,b):
    A=a
    B=b
    S=0
    while A!=0:
        if A%2==1:
            S=S+B
        A=A//2
        B=B+B

    print(S)

a = int(input())
b = int(input())
print("Le resultat est:")
Egypt(a,b)

#commentaires sur vscode