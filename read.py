sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('All comment average length', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('Have', len(new), 'comment less than 100 words')
print(new[0])
print(new[1])

good = [d for d in data if 'good' in d]

good = []
for d in data:
	if 'good'in d:
		good.append(d)
print('Have', len(good), 'comment is a good comment')
print(good[0])


data = []
count = 0
with open('reviews.txt', 'r')as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('All has been rad, Total', len(data), 'comment')

print(data[0])

#文字技術
wc = {}  #wordcount
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1  #有等於就是新加key

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))

while True:
	word = input('What do u want to search: ')
	if word == 'q':
		break
	if word in wc:
		print(word, 'came out', wc[word], 'time')
	else:
		print('I dont get this word, Try another one.')
print('Thanks For Your Using')