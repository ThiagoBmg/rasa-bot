with open('./tmp.csv', 'rb') as file:
    lines = file.readlines()
    for line in lines:
        a:list = str(line).split(",")
        # print(a[7])
        with open('ext.txt', 'a') as file2:
            file2.write( f'- {a[7].lower()}\n')