for numero in range(2, 51):
    primo = True
    for i in range(2, numero):
        if (numero % i) == 0:
            primo = False
            break
    if primo:
        print(numero, end=" ")