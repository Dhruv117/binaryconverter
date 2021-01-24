from colorama import Style, Fore, Back
_ALL_COLORS_ = [Fore.RED,Fore.BLUE,Fore.GREEN,Fore.YELLOW,
    Fore.CYAN,Fore.MAGENTA,Fore.WHITE,Fore.BLACK
]

try:
    number = int(input("===>"))
except ValueError:
    print('Enter a integer not a string.')    
    number = int(input("===>"))

    
def binary(num):
    code = ""
    while num>0:
        remainder = num%2
        code += str(remainder)
        print(f"{_ALL_COLORS_[0]}2 {_ALL_COLORS_[6]}|{_ALL_COLORS_[1]} {num} {_ALL_COLORS_[6]}|{_ALL_COLORS_[3]} {remainder}")
        num = num//2
    binarycode = list(code)
    binarycode.reverse()
    binarycode = str(binarycode)
    binarycode = binarycode.strip("[")
    binarycode = binarycode.strip("]")
    binarycode = binarycode.replace(" ","")
    binarycode = binarycode.replace("'","")
    binarycode = binarycode.replace(",","")
    print("Binary number is ",binarycode)           
binary(number)
again = input('Wanna Run Again Y/N')    
while again != 'N' or 'n':
    number = int(input("===>"))
    binary(number)
    again = input('Wanna Run Again Y/N: ') 
    if again == 'N' or 'n':
        print('Thanku For using')
        break
