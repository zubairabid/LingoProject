import glob
import re 

flist = glob.glob('*.in')
wordlist = ['person', 'customer', 'witness', 'manager', 'each']
plist = ['he', 'she', 'they', 'her', 'hers', 'his', 'him', 'theirs', 'them', 'their']

for fil in flist:
	with open(fil, 'r') as f:
		content = f.read()
		ll = []
		for word in wordlist:
			if word not in content:
				continue
			ll.append(word)
			if(word == wordlist[len(wordlist)-1]):
				print(ll)
				print(content)
				print('#*' * 40)
				print('\n'*3)
