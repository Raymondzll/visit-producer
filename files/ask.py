import requests
import sys
import time
name='https://xn--fx-ex2c330n.ml/show.php?url=https://www.luogu.com.cn/discuss/423386'
turn=600
if len(sys.argv)>1:
	try:
		turn=int(sys.argv[1])
	except Exception as e:
		print("Found error:",e)
		print("will use default value as number of turns.")
if len(sys.argv)>2:
	if len(sys.argv[1])<=8 or not(sys.argv[1][:8]!='https://' or sys.argv[1][:7]!='http://'):
		print("bad input.")
		exit()
	else:
		name=sys.argv[1]
cnt=0
while 1:
	try:
		r = requests.get(name)
	except Exception as ex:
		print("exit with error:",ex)
		break
	else:
		if r.status_code!=200:
			print("exit with bad code:",r.status_code)
			break
		cnt+=1
		print("requested successfully!")
		if cnt==turn:
			break
		time.sleep(0.005)
		if cnt%60==0:
			print("wait for a while...")
			time.sleep(3)
		elif cnt%20==0:
			print("wait for a while...")
			time.sleep(1)
