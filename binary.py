from colorama import Style, Fore, Back
_ALL_COLORS_ = [Fore.RED,Fore.BLUE,Fore.GREEN,Fore.YELLOW,
    Fore.CYAN,Fore.MAGENTA,Fore.WHITE,Fore.BLACK
]

# num = int(input('===>'))
# # binarycode= ''
# def div(num):
#     binarycode= ''
#     while num>0:
#         if num%2!=0:
#             code = 1
#             binarycode += str(1)
#         else:
#             code = 0 
#             binarycode += str(0)
#         print("{} is {}".format(num,code))
#         num = num//2
#     print("Biary code  is {}".format(binarycode))              
# # div(num)

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
def strToBinary(s): 
    bin_conv = [] 
  
    for c in s: 
          
        # convert each char to 
        # ASCII value 
        ascii_val = ord(c) 
          
        # Convert ASCII value to binary 
        binary_val = bin(ascii_val) 
        bin_conv.append(binary_val[2:]) 
          
    return (' '.join(bin_conv)) 
  
# Driver Code 
if __name__ == '__main__': 
    s = input('===#')
  
print (strToBinary(s)) 