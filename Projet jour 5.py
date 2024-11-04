## job 1

fruits = ["pomme", "cerise", "orange"]
print(fruits)


## job 2


fruits = ["pomme", "cerise", "orange"]
print(fruits[1])


## job 3


fruits = ["pomme", "cerise", "orange"]
fruits.append("melon")
print(fruits)


## job 4

fruits = ["pomme", "cerise", "orange", "melon"]
fruits.insert(2, "mangue")
print(fruits)

## job 5


L = [1, 2, 3, 4, 5]

print (L)
print (L[1])
L[3] = L[2] + L[4]
print(L)
print (L[4])


## job 6

List = [1, 2, 3, 4, 5]
print(List)
List.reverse()
print(List)

    
## job 7


L = [8, 24, 48, 2, 16]

count = 0

for x in L:
    if x % 3 == 0:
        count += 1
print(count)


## job 8

L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
sum = 0

for x in L:
    if x % 2 == 0:
        sum += x

print(sum)

## job 9

L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

print("la max valeur est", max(L))
print("la min valeur est", min(L))


## job 10


L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
sum = 0

for x in L:
    if x <= 91 and x >= 25:
        sum += x
print(sum)

## job 11


L = [7, 11, 42, 39, 2]

for x in range(len(L)):
    L[x] += 1
print(L)


## job 12

L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
NL = []

for x in  L:
    if x not in NL:
        L.append(x)
print(NL)
