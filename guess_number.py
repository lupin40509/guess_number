import random

start = int(input('請輸入這次猜謎範圍起始值:'))
end = int(input('請輸入這次猜謎範圍結束值:'))

ans = random.randint(start, end) # 設計亂數答案
count = int(0) #猜謎次數

while True:
	x = int(input('請輸入數字:'))
	count += 1
	if (x - ans) > 0:
		print('比答案大')
	elif (x - ans) < 0:
		print('比答案小')
	else:
		print('終於猜對了!')
		print('答案是: %d' % ans)
		print('總共猜了 %d 次' % count)
		break