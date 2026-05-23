palindromo = str(input('DIGITE A PALAVRA/FRASE:'))
left = 0
right = len(palindromo) - 1
while (left < right):
    if palindromo[left] != palindromo[right]:
        print('NÃO É PALINDROMO!')
        break
    left += 1
    right -= 1
else:
    print('É PALINDROMO!')
