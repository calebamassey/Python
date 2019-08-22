def boxPrint(symbol, width, height):
    if len(symbol) != 1:
            raise Exception('Symbol must be a single character string.')
    if width <= 2:
            raise Exception('Width must be greater than 2.')
    if height <= 2:
            raise Exception('Height must be greater than 2.')

    print(symbol * width)
    for i in range(height -2):
        print (symbol + (' ' * (width - 2)) + symbol)
    print (symbol * width)


sym =  str(input('Enter your symbol for the rectangle: '))
h = int(input('Enter the height of the rectangle: '))
w = int(input('Enter the width of the rectangle: '))
try:
    boxPrint(sym, w, h)
except Exception  as err:
    print ('An exception has happened: ' + str(err))