y = int(input())

while y <= 3000:
    if y % 4 == 0 and y % 100 != 0:
        #leap
        print(y, ' - leap')
    elif y % 400 == 0:
        print(y, ' - leap')
    else:
        print(y, '- unleap')
    y = y + 1

