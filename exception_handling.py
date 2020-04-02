# try:
#     print(100/0)

# print('Hello I am after excption')
#if exception occur then program terminate abnormally.
#except ka 1 b block match hojae tw baqi except k block match nhi honge.
#generic exception should be last block
#try block ki jis line me exception ae us k bad ki koi line execute nhi krti.
#if exception occurs or not finally block always execute.


a={
    'Name' : 'Kulsoom'
}
try:
    with open('data.csv','r'):
        pass         
    print(a['Name'])
except KeyError:
    print("This key doesn't exist in this ADT")
except FileNotFoundError as e:
    print(e)
    print('File does not exist')
except Exception:
    print('This is un-known exception')
finally:
    print('I am finally Block')
    print('Ending')