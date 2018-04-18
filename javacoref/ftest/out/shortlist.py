from glob import glob
import re

plist = ['he', 'she', 'they', 'her', 'hers', 'his', 'him', 'theirs', 'them', 'their']
wordlist = ['person', 'customer', 'witness', 'manager', 'each']
filelist = glob('*.out')

for fil in filelist:
	flag1 = False # Reference matching
	flag2 = False # Word matching

	pl = []
	wl = []
	infil = fil[:-4]
	text = ''
	an_text = ''


	with open(fil, 'r') as f:
		for line in f:
			an_text += line

	an_split = an_text.split('Coreference set:')
	for elem in an_split:
		if elem == an_split[0]:
			continue

		elem = elem.strip()
		tpl = []

		for key in plist:
			if re.search(r'\b' + key + r'\b', elem) is None:
				continue

			tpl.append(key)
			flag1 = True
			tx = ''

			if key == plist[len(plist) - 1]:
				tx += str(tpl) + '\n'
				tx += 'Coreference Set:\n'
				tx += elem
				pl.append(tx)

	
	with open(infil, 'r') as f:
		text = f.read()

	for word in wordlist:
		if re.search(r'\b' + word + r'\b', text) is None:
			continue

		wl.append(word)
		flag2 = True

	
	if flag1 and flag2:
		print('*'*20 + 'For files {0} and {1}, parse done'.format(fil, infil) + '*'*20)

		print('Coref listing : ')
		for ref in pl:
			print(ref)
			print('\n')

		print('Word listing : ' + str(wl) + '\n' + '/' * 40)

		print('original text : ' * 10)
		print(text)
		print('@' * 100 + '\n\n')
	
