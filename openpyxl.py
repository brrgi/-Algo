from matplotlib import pyplot as plt
import csv
import openpyxl
from openpyxl.chart import (
    ScatterChart,
    Reference,
    Series,
)
f=open('analogdata2.csv', 'r', encoding='utf-8')
rdr=csv.reader(f)

#엑셀파일 열기
filename="Lee_re.xlsx"
book=openpyxl.load_workbook(filename)
sheet=book.active


number=1
plt1=[]
left=[]
right=[]
left_value=[0 for i in range(20)]
right_value=[0 for i in range(20)]
for line in rdr:
    if line[0].isdigit()==1:
        left.append(int(line[0]))
        right.append(int(line[1]))
        left_value[int(line[0])//50]+=1
        right_value[int(line[1])//50]+=1
        plt1.append(number)
        number+=1
left_low=min(left)
left_high=max(left)
right_low=min(right)
right_high=max(right)
left_middle=(left_low+left_high)/2
right_middle=(right_low+right_high)/2
left_result=[]
right_result=[]

'''
for i in left:
    #선이 있으면 1입력
    if abs(left_low-i)>abs(left_high-i):
        left_result.append(1)
    else:
        left_result.append(0)

for i in right:
    #선이 있으면 1입력
    if abs(right_low-i)>abs(right_high-i):
        right_result.append(1)
    else:
        right_result.append(0)
'''
for i in left:
    #선이 있으면 1입력
    if left_middle<i:
        left_result.append(1000)
    else:
        left_result.append(0)

for i in right:
    #선이 있으면 1입력
    if right_middle<i:
        right_result.append(1000)
    else:
        right_result.append(0)

total=[]
print(left)
print(right)
print(left_result)
print(right_result)


for i in range(len(left_result)):
    if left_result[i]==right_result[i] and left_result[i]==1:
        total.append(1)
    else:
        total.append(0)


plt.plot(plt1,total)
plt.xlabel("test")
plt.ylabel("col")
plt.title("testing")
plt.show()


sheet[str(chr(66)) + str(1)] ="Left"
sheet[str(chr(67)) + str(1)] ="Right"
sheet[str(chr(68)) + str(1)] ="Converted Left"
sheet[str(chr(69)) + str(1)] ="Converted Right"
cell=sheet[str(chr(66)) + str(1)]
cell=sheet[str(chr(67)) + str(1)]
cell=sheet[str(chr(68)) + str(1)]
cell=sheet[str(chr(69)) + str(1)]
# left, right, 0left, 0right
#A
for j in range(len(left)):
    sheet[str(chr(65))+str(j+2)]=j+1
    cell=sheet[str(chr(65))+str(j+2)]
#B
for j in range(len(left)):
    sheet[str(chr(66))+str(j+2)]=left[j]
    cell=sheet[str(chr(66))+str(j+2)]
#C
for j in range(len(right)):
    sheet[str(chr(67))+str(j+2)]=right[j]
    cell=sheet[str(chr(67))+str(j+2)]
#D
for j in range(len(left)):
    sheet[str(chr(68))+str(j+2)]=left_result[j]
    cell=sheet[str(chr(68))+str(j+2)]
#E
for j in range(len(left)):
    sheet[str(chr(69))+str(j+2)]=right_result[j]
    cell=sheet[str(chr(69))+str(j+2)]

#원래 값
chart=ScatterChart()
chart.title = "LeeRe"
chart.style=13
chart.x_axis.title='x'
chart.y_axis.title='y'

#0,1값
# chart2=ScatterChart()
# chart2.title = "LeeRe"
# chart2.style=13
# chart2.x_axis.title='x'
# chart2.y_axis.title='y'

xvalues=Reference(sheet, min_col=1, min_row=2, max_row=134)  #active한 것, 왼쪽 시작, 위쪽 시작, 아래쪽 끝
# xvalues2=Reference(sheet, min_col=1, min_row=2, max_row=134)
for i in range(2, 6):
    values = Reference(sheet, min_col=i, min_row=1, max_row=134)
    series = Series(values, xvalues, title_from_data=True)
    chart.series.append(series)

# for i in range(4, 6):
#     values2 = Reference(sheet, min_col=i, min_row=1, max_row=134)
#     series2 = Series(values2, xvalues2, title_from_data=True)
#     chart2.series.append(series2)

sheet.add_chart(chart, "A10")
# sheet.add_chart(chart2, "A10")

book.save(filename)
f.close
