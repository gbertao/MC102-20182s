obj = input()
char = input()

if obj == 'Q':
    size = int(input())

    if size >= 3:
        print(char*size)
        for i in range(0, size-2,1):
            print(char+(size-2)*" "+char)

        print(char*size)

    else:
        print("Dimensao incorreta.")

elif obj == 'R':
    width = int(input())
    length = int(input())

    if width >= 3 and length >=3:
        print(char*width)
        for i in range(0, length-2, 1):
            print(char+(width-2)*" "+char)

        print(char*width)
    
    else:
        print("Dimensao incorreta.")

elif obj == 'P':
    width = int(input())
    length = int(input())

    if width >= 3 and length >=3:
        print(char*width)
        for i in range(0, length-2, 1):
            print((i+1)*" "+char+(width-2)*" "+char)

        print((length-1)*" "+char*width)
    
    else:
        print("Dimensao incorreta.")

elif obj == 'L':
    size = int(input())

    if size >= 3:
        print((size-1)*" "+char)

        for i in range(2, size, 1):
            k = size-i
            print(k*" "+char+(2*i-3)*" "+char)

        for i in range(size, 1, -1):
            k = size-i
            print(k*" "+char+(2*i-3)*" "+char)

        print((size-1)*" "+char)
    
    else:
        print("Dimensao incorreta.")

elif obj == 'C':
    size = int(input())

    if size >= 3:
        print(size*" "+size*char)

        for i in range(0, size-2, 1):
            print(size*" "+char+(size-2)*" "+char)

        print((size*3)*char)

        for i in range(0, size-2, 1):
            print(3*(char+(size-2)*" "+char))

        print((size*3)*char)

        for i in range(0, size-2, 1):
            print(size*" "+char+(size-2)*" "+char)
    
        print(size*" "+size*char)
    else:
        print("Dimensao incorreta.")

else:
    print("Objeto incorreto.")
