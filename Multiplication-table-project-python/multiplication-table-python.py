

print('Welcome In Multiplication App')
print('Please Enter The First Number And The Last Number Of The Muliplication Table')

start = int(input('Enter The First Number Of The Table : '))
end = int(input('Enter The Last Number Of The Table : '))

for x in range(start,end+1):
    for y in range(1,13):
        print(x, 'X' ,y, '=' , x*y)
    print('-----------------------')
