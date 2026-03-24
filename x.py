i=1
fact=1
num=int(input("entr a number: "))
# while i<=num:
#     fact=fact*i
#     i=i+1
#     print(fact)
# print(fact)

for i in range(1,num+1):
    fact=fact*i
print(fact)