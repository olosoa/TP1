print("nombre de depart ? ")
n = int(input())
sr=[n]
while n != 1:
    if n%2 == 0:
        n = n//2
    else:
        n = 3*n + 1

    sr.append(n)
print(sr)

#commentaires sur myenv
