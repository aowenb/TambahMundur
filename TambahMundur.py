# Function untuk tambah mundur
def tambahMundur(x,y):
    temp_1 = int(str(x)[::-1]) # reverse input 1
    temp_2 = int(temp_1 + y) # input 2 + reverse(input 1) 
    temp_3 = int(str(temp_2)[::-1]) # final reverse
    return temp_3

# While loop untuk return input yang valid
while True:
    try:
        x = int(input('Masukkan angka 1 : '))
        y = int(input('Masukkan angka 2 : '))
    # untuk filter input yang bukan int seperti str,float, etc
    except ValueError: 
        print('invalid input !')
        break
    # setting limit int untuk input
    if x > 359999 or y > 359999:
        print('invalid input !')
        break
    # jika input sudah valid run def tambahMundur()
    else:
        print(tambahMundur(x,y))
        break