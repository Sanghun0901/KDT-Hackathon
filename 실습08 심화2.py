실습 2 - 1(리스트로 푸는법도 존재)

a = {4:'Strawberry',5:'Grape',6:'Kiwi'}
b = {4:'red',5:'purple',6:'green'}

for i,k in a.items() : 
    if sheet2.cell(row = i, column = 1).value == None :
        sheet2.cell(row = i, column = 1).value = k
 
for i,k in b.items() : 
    if sheet2.cell(row = i, column = 2).value == None :
        sheet2.cell(row = i, column = 2).value = k
        
wb.save('Fruit4.xlsx')


실습 2-2
wb = xl.load_workbook('Fruit4.xlsx')
sheet3 = wb['Sheet2']

for i in range(1,7) :
    if sheet3.cell(row = i, column = 3).value == None :
        sheet3.cell(row = i, column = 3).value = int(i - 1) 
    
wb.save('Fruit5.xlsx')


실습 2-3
wb = xl.load_workbook('Fruit5.xlsx')
sheet4 = wb['Sheet2']

for i in range(1,7) :
    if sheet4.cell(row = i, column = 1).value != None :
        sheet4.cell(row = i, column = 1).value = (sheet4.cell(row = i, column = 1).value).lower()

    if sheet4.cell(row = i, column = 2).value != None :
        sheet4.cell(row = i, column = 2).value = sheet4.cell(row = i, column = 2).value[0:3]

        
wb.save('Fruit6.xlsx')
