from glob import glob
import re

plist = ['he', 'she', 'they', 'her', 'hers', 'his', 'him', 'theirs', 'them', 'their']
filelist = glob('*.out')
for f in filelist:
	flag = False
	print('\n\n' + '#'*40 + 'Parsing file ' + f + '#'*40)
	text = ''
	with open(f, 'r') as ffile:
		for line in ffile:
			text += line
	
	split = text.split('Coreference set:')
	for elem in range(1, len(split)):
		
		split[elem] = split[elem].strip()

		ll = []

		for key in plist:
			if re.search(r'\b' + key + r'\b', split[elem]) is None:
				continue

			ll.append(key)
			flag = True
			if key == plist[len(plist) - 1]:
				print('\n' + str(ll))
				
				print('Coreference set:')
				print(split[elem])
			

	if flag:
		print('\n\n' + '*'*20 + 'Done parsing File ' + f + ' has relevant data' + '*'*20)
		print('\n' + ' ORIGINAL TEXT ' * 14 + '\n')
		f_or = f[:-4]
		i = 1
		with open(f_or, 'r') as ffile:
			#for line in ffile: 
			#	print(str(i) + ' : ' + line, end='')
			#	i += 1
			print(ffile.read())

		print('-'*100 + '\n\n\n\n\n') 
