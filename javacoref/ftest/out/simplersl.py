from glob import glob
import re

wordlist = ['any']
filelist = glob('*.in')

for fil in filelist:
	flag2 = False # Word matching

	wl = []
	text = ''


	with open(fil, 'r') as f:
		text = f.read()

	for word in wordlist:
		if re.search(r'\b' + word + r'\b', text) is None:
			continue

		wl.append(word)
		flag2 = True

	
	if flag2:
		print('*'*20 + 'For file {0}, parse done'.format(fil) + '*'*20)

		print('\nWord listing : ' + str(wl) + '\n' + '/' * 40)

		print('original text : ' * 10)
		print(text)
		print('@' * 100 + '\n\n')
	
