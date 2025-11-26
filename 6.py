lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lst2 = []
for d in lst:
    if d % 2 != 0:
        lst2.append(d**2)

# print(f'{lst2=}')

lst2_1 = [k**2 for k in lst if k % 2 != 0]
print(f'{lst2_1=}')

lst = [k for k in range(1,100 + 1)]
print(f'{lst=}')

string = 'А роза упала на лапу Азора'

def is_palindrome(string: str) -> bool:
   spaceless1 = [k.upper() for k in string if k != ('')]
   spaceless2 = [k.upper() for k in string if k != ('')]
   spaceless2.reverse()


   return spaceless1 == spaceless2


