
palin = input('Enter a string to check palindrome(0 to exit): ')
while (palin != '0'):
    i = 0
    j = len(palin) - 1
    match = True

    while (i < j):
        if (palin[i] != palin[j]):
            match = False
        j = j - 1
        i = i + 1

    print(match)
    palin = input('Enter a string to check palindrome(0 to exit): ')

