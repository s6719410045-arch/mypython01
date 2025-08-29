print('-----------------------------------')
print('โปรแกรม Product Sale')
print('-----------------------------------')
pro_id = input('ป้อนรหัสสินค้า : ')
pro_name = input('ป้อนชื่อสินค้า : ')
pro_type = input('ป้อนประเภทสินค้า (F/f, W/w, M/m, K/k): ')
pro_price = float(input('ป้อนราคาสินค้า : '))
print('-----------------------------------')
if pro_type == 'f' or pro_type == 'F':
    pro_price = pro_price - (pro_price * 2 / 100)
    print(f'ราคาสินค้าที่ลดแล้วเป็น : {pro_price} บาท')
elif pro_type == 'w' or pro_type == 'W':
    pro_price = pro_price - (pro_price * 4 / 100)
    print(f'ราคาสินค้าที่ลดแล้วเป็น : {pro_price} บาท')
elif pro_type == 'm' or pro_type == 'M':
    pro_price = pro_price - (pro_price * 6 / 100)
    print(f'ราคาสินค้าที่ลดแล้วเป็น : {pro_price} บาท')
elif pro_type == 'k' or pro_type == 'K':
    pro_price = pro_price - (pro_price * 10 / 100)
    print(f'ราคาสินค้าที่ลดแล้วเป็น : {pro_price} บาท')
else:
    print('คุณป้อนประเภทผิด !!! ต่าย ตาย ป้อนใหม่อีกครั้งนะ...')
print(f'รหัสสินค้า : {pro_id}')
print(f'ชื่อสินค้า : {pro_name}')
print(f'ประเภทสินค้า : {pro_type}')
print(f'ราคาสินค้า : {pro_price}')
print('-----------------------------------')
print('ขอบคุณที่ใช้บริการ')
print('-----------------------------------')