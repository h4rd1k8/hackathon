import os

def mk_dir():
	with open('saved_messages.txt', "r") as f1:
		last_line = f1.readlines()[-1].split('||')
	location = last_line[2]
	category = last_line[1]
	user = last_line[0]
	if not os.path.exists('/home/yerdaulet/hackathon/' + location + '/' + category + '/' + user + '/'):
		os.makedirs('/home/yerdaulet/hackathon/' + location + '/' + category + '/' + user + '/')

readd()

if __name__ == '__main__':
    print('Test1')
