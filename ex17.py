vet =[]
a = int(input())
for i in range(0, a):
    vet.append(int(input('valor: ')))


if vet % 2 == 0:
        print('par')
else:
        print('impar')
print(vet)

vet.sort()
print(vet)
vet.reverse()
print(vet)