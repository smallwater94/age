drive = input('請問你有沒有開過車? ')
if drive != '有' and drive != '沒有':
	print('請輸入 有/沒有')
	raise SystemExit
age = input('請問你的年齡? ')
age = int(age)
if drive =='有':
	if age >= 18:
		print('沒問題')
	else:
		print('奇怪...')
elif drive == '沒有':
	if age >= 18:
		print('該考駕照了喔')
	else:
		print('好吧 在等等')