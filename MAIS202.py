import csv
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

list1 = []
list2 = []

with open('home_ownership_data.csv', 'r') as file1:  # open the file
    reader1 = csv.reader(file1)
    count = 0
    print(file1)
    for row in reader1:
        list1.append(row[0])
        list2.append(row[1])

    count += 1

list3 = []
list4 = []

with open('loan_data.csv', 'r') as file2:
    reader2 = csv.reader(file2)
    count2 = 0
    print(file2)
    for row in reader2:
        list3.append(row[0])
        list4.append(row[1])
    count2 += 1

A = 'MORTGAGE'
B = 'OWN'
C = 'RENT'
loanadd1 = 0
loanadd2 = 0
loanadd3 = 0
loan_amnt0 = 0.0
loan_amnt1 = 0.0
loan_amnt2 = 0.0
i = 0
j = 0
times1 = 0
times2 = 0
times3 = 0
for i in range(0, len(list2)):
    if (list2[i] == A):
        for j in range(0, len(list3)):  # calculate total of the same type

            if (list1[i] == list3[j]):
                times1 += 1
                loanadd1 = int(list4[j]) + loanadd1

        j += 1
    if (list2[i] == B):
        for j in range(0, len(list3)):
            if (list1[i] == list3[j]):
                times2 += 1
                loanadd2 = int(list4[j]) + loanadd2

        j += 1
    if (list2[i] == C):
        for j in range(0, len(list3)):
            if (list1[i] == list3[j]):
                times3 += 1
                loanadd3 = int(list4[j]) + loanadd3

        j += 1

i += 1
MORdata = loanadd1 / times1
OWNdata = loanadd2 / times2
RENTdata = loanadd3 / times3

loan_amnt0 = round((float(loanadd1) / times1), 6)  # round the number to 6 decimal places
loan_amnt1 = round(float(loanadd2) / times2, 6)
loan_amnt2 = round(float(loanadd3) / times3, 6)
print(loan_amnt0)
print(loan_amnt1)
print(loan_amnt2)

x = [A, B, C]
y = [loan_amnt0, loan_amnt1, loan_amnt2]
gridspec = {'width_ratios': (1, 2.5)}
fig, axs = plt.subplots(1, 2, gridspec_kw=gridspec, figsize=(18.3, 7))
y_pos = [0, 1.2, 2.5]
plt.xticks(y_pos, x)
plt.bar(y_pos, y)
plt.xlabel('Hopltme ownership')
plt.ylabel('Average loan amount($)')
plt.title('Average loan  amounts per home ownership')
axs[0].axis('off')

rows = ('0', '1', '2')  # plot the table
cols = ('home_ownership', 'loan_amnt')
colour = (['gainsboro', 'gainsboro'], ['white', 'white'], ['gainsboro', 'gainsboro'])
rowcolor = ('gainsboro', 'white', 'gainsboro')
text = ([A, loan_amnt0], [B, loan_amnt1], [C, loan_amnt2])
table = axs[0].table(cellText=text,
                     cellColours=colour,
                     rowLabels=rows,
                     rowColours=rowcolor,
                     colLabels=cols,
                     loc='lower center',

                     )

A = []
for key, cell in table.get_celld().items():
    rows, cols = key
    A.append(cell)
    cell.set_edgecolor('none')
for x in A[0:]:
    if (x == A[0]):
        x.set_text_props(fontproperties=FontProperties(weight='bold'))
    if (x == A[1]):
        x.set_text_props(fontproperties=FontProperties(weight='bold'))
    if (x == A[7]):
        x.set_text_props(fontproperties=FontProperties(weight='bold'))
    if (x == A[6]):
        x.set_text_props(fontproperties=FontProperties(weight='bold'))
    if (x == A[9]):
        x.set_text_props(fontproperties=FontProperties(weight='bold'))

plt.show()
