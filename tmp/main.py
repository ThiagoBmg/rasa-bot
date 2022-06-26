with open('./tmp.csv', 'rb') as file:
    lines = file.readlines()
    for line in lines:
        a:list = str(line).split("\\xc3\\xa9")
        b:str = a[1].split("\\n'")[0].replace(" ","")
        b = b.replace("\\xc3\\x", "")
        a:str = a[0].split("b'")[1]

        with open('ext.txt', 'a') as file2:
            file2.write( f'- meu nome é [{b}](name)\n')