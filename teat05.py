name = input('ป้อนชื่อ: ')
year_born = input('ป้อนปีเกิด พ.ศ.: ')
print('-----------------------------')
print(f'สวัสดิคุณ{name}')
print(f'คุณเกิดปีอะไร{year_born}ตอนนี้คุณอายุ{2568 - int(year_born)}')
# ใช้ ,
print("สวัสด๊คุณ", name)
print("คุณเกิดในปี พ.ศ", year_born, "ตอนนี้คุณอายุ", 2568 - int(year_born))
# ใช้ + 
print("สวัสดีคุณ "+ name)
print("คุณเกิดในปี พ.ศ " + year_born + " ตอนนี้คุณอายุ " + str(2568 - int(year_born )))
# format
print("สวัสดีคุณ {}".format(name))
print("คุณเกิดในปี พ.ศ. {} ตอนนี้คุณอายุ {}".format(year_born, 2568 - int(year_born)))