import string, os

def funkcja(x):
    return 0+x

y = []

user_input = 0

for user_input in range(69):
    x = 1
    y.append(funkcja(x))
    z = sum(y)
    
    myfile = open('LOLFILE.txt', 'w')
    myfile.write('lol\nxD\nxDDDD')
    myfile.close()
    os.rename('LOLFILE.txt', 'LOLFILE' + ' ' + (str(z)) + '.txt')