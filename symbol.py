symbol = ( ' ', '*', '+', '!', '(', '{', '=', '#', '$', '@')

def testSymbol():
    for char in symbol:
        for i in range(0,50):
            print(char, end="")
        print()
