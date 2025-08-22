# สร้างโปรแกรมรับข้อมูลจำนวนเต็ม 5 จำนวนจากผู้ใช้
# และคำนวณหาผลรวม และค่าเฉลี่ยของข้อมูลที่รับเข้ามา
# เป็นเท่าใด แล้วแสดงผลทางหน้าจอ
# สูตร  
# ผลรวม = เลขตัวที่1 + เลขตัวที่2 + เลขตัวที่3 + เลขตัวที่4 + เลขตัวที่5
# ค่าเฉลี่ย = ผลรวมของเลข 5 จำนวน / 5
 
# ============================
# Program  Average  5  Number
# ============================
# Enter number 1 : <input>
# Enter number 2 : <input>
# Enter number 3 : <input>
# Enter number 4 : <input>
# Enter number 5 : <input>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================

# Program Average 5 Nnmber
print("Program Average 5 Nnmber" )
 
 # รับข้อมูล
num1 = int(input("พนักงานคนที่1 :"))
num2 = int(input("พนักงานคนที่2 :"))
num3 = int(input("พนักงานคนที่3 :"))
num4 = int(input("พนักงานคนที่4 :"))
num5 = int(input("พนักงานคนที่5 :"))
#คำนวณผลรวม
total = num1 + num2 + num3 + num4 + num5
 
 # เฉลี่ยผลรวม
average = total / 5

# แสดงผล
print("ผลรวมของทั้ง 5 คน : ", total)
print("รวมผลเฉลี่ยของทั้ง 5 คน: ", format(average, ".2f"))



