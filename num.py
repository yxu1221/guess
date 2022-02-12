import random
start = input('請輸入開始範圍:')
end = input('請輸入結束範圍')
start = int(start)
end = int(end)

r = random.randint(start, end)
while True:
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('你猜對了!')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
