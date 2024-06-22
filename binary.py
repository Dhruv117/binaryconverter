try:
    number = int(input("enter a number:"))
except ValueError:
    print('Enter a integer not a string.')    
    number = int(input("===>"))

    
def binary(num):
    code = ""
    while num>0:
        remainder = num%2
        code += str(remainder)
        num = num//2
    print("Binary number is :",code[-1::-1])           
binary(number)
again = input('Wanna Run Again y/n:')    
while again != 'N' or 'n':
    if(again!='y' or 'Y'):
        again = input('Wrong input enter only y/n: ')     
    number = int(input("enter number:"))
    binary(number)
    again = input('Wanna Run Again y/n: ') 
else:
    print('Thankyou for using')
