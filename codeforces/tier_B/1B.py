
def cell_converter(cell_text):
    number_count=0
    letter_count=0

    if cell_text[0]=="R" and cell_text[1].isdigit()==True and cell_text.index('C')!=0:
        b = cell_text.index('C')
        row = cell_text[1:b]
        col = int(cell_text[(b+1):])
        column_name = ""
        while col > 0:
            col, remainder = divmod(col - 1, 26)
            column_name = chr(65 + remainder) + column_name
            
        print(str(column_name)+str(row))
        
        
        
    else:
        for i in range(len(cell_text)):
            if cell_text[i].isdigit()!=True:    
                letter_count+=1
            else:
                number_count+=1

        col=cell_text[0:letter_count]
        row=cell_text[letter_count:]
                
        col = col.upper()
        column_number = 0
        for char in col:
            column_number = column_number * 26 + (ord(char) - ord('A') + 1)
        
        print("R"+str(row)+"C"+str(column_number))

  

n = int(input())

for i in range(n):
    cell_converter(input())
    
"""
onek chodon er por milse -_-
"""