from glob import glob
import re

plist = ['he', 'she', 'they', 'her', 'hers', 'his', 'him', 'theirs', 'them', 'their']
wordlist = ['person', 'customer', 'witness', 'manager', 'each']
filelist = glob('*.in')

for fil in filelist:
	flag1 = False
	flag2 = False # Word matching

	wl = []
	pl = []
	text = ''

	with open(fil, 'r') as f:
		text = f.read()

	for key in plist:
		if re.search(r'\b' + key + r'\b', text) is None:
			continue
		
		pl.append(key)
		flag1 = True

	
	for word in wordlist:
		repl = r'\033[44;33m' + word + r'\033[m'

		temp = text
		text = re.sub(r'\b' + word + r'\b', repl, text, 0)

		if temp == text:
			continue

		wl.append(word)
		flag2 = True

	
	if flag1 and flag2:
		print('*'*20 + 'For file {0}, parse done'.format(fil) + '*'*20)

		print('\nPronoun listing : ' + str(pl) + '\n')
		print('\nWord listing : ' + str(wl) + '\n' + '/' * 40)

		print('original text : ' * 10)
		print(text)
		print('@' * 100 + '\n\n')
	
	#	with open('res/{0}.fuck'.format(fil), 'w') as f:
	#		f.write(st)

