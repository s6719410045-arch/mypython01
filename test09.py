#สร้างโปรแกรมคำนวณเงินเดือนสุทธิที่ต้องจ่ายหลังจากโดนภาษีแล้ว 7% ของเงินเดือน และหักค่าประกันสังคม 3% ของเงินเดือน
#โดยรับค่ารหัสพนักงาน ฃื่อพนักงาน เงินเดือน ทางแป้นพิมพ์และแสดงผลข้อมูลที่รับมา
# พร้อมรายละเอียดว่าต้องหักภาษีก่ีบาท หักค่าประกันสังคมกี่บาท และต้องจ่ายเงินเดือนสุทธิกี่บาท
print('+++++++++++++++++++++++++')
print('โปรแกรมคํานวณเงินเดือน')
print('+++++++++++++++++++++++++')
emp_code = input('ป้อนรหัสพนักงาน : ')
emp_name = input('ป้อนชื่อพนักงาน : ')
emp_salary = input('ป้อนเงินเดือน : ')
print('+++++++++++++++++++++++++')
tax = float(emp_salary) * 7 / 100
insurance = float (emp_salary) * 3 / 100
emp_salary_net = float (emp_salary) - tax - insurance
print(f'รหัส; {emp_code} ชื่อ {emp_name} เงินเดือน {emp_salary_net}')
print(f'หักภาษี {tax} บาท')
print(f'หักค่าประกันสังคม {insurance} บาท')
print(f'ต้องจ่ายเงินเดือนสุทธิ {emp_salary_net} บาท')
print('+++++++++++++++++++++++++')
# ใฃ้ ,
print('+++++++++++++++++++++++++')
print('รหัส',emp_code,'ชื่อ',emp_name,'เงินเดือน',emp_salary_net)
print('หักภาษี',tax,'บาท')
print('หักค่าประกันสังคม',insurance,'บาท')
print('ต้องจ่ายเงินเดือนสุทธิ',emp_salary_net,'บาท')
print('+++++++++++++++++++++++++')
# ใฃ้ +
print('+++++++++++++++++++++++++')
print('รหัส' + emp_code + 'ชื่อ' + emp_name + 'เงินเดือน' + str(emp_salary_net))
print('หักภาษี' + str(tax) + 'บาท')   
print('หักค่าประกันสังคม' + str(insurance) + 'บาท')
print('ต้องจ่ายเงินเดือนสุทธิ' + str(emp_salary_net) + 'บาท')
print('+++++++++++++++++++++++++')
# ใฃ้ format
print('+++++++++++++++++++++++++')
print('รหัส {}'.format(emp_code))
print('ชื่อ {}'.format(emp_name))
print('เงินเดือน {}'.format(emp_salary_net))
print('หักภาษี {} บาท'.format(tax))
print('หักค่าประกันสังคม {} บาท'.format(insurance))
print('ต้องจ่ายเงินเดือนสุทธิ {} บาท'.format(emp_salary_net))
print('+++++++++++++++++++++++++')


