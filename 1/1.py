import sys
import itertools

threshold = 1000
k = 2

def file_contents(file_name):
  f = open(file_name)
  try:
    return f.read()
  finally:
      f.close()

def initData():
	items = file_contents('../itemlist10000.txt')
	data = items.split('\n')[0:10000]
	for i in range(len(data)):
		data[i] = data[i].split(' ')
	return data

def getItemFromItemset(itemsets):
	keys = list(itemsets.keys())
	for i in range(len(keys)):
		keys[i] = keys[i].split(' ')
	items = list(set([j for i in keys for j in i]))
	items.sort()
	return items

def tuppleToString(tuppleList):
	for i in range(len(tuppleList)):
		str = ''
		for j in range(k):
			str += tuppleList[i][j] + ('' if j == k - 1 else ' ')
		tuppleList[i] = str

def generateCandidates(data):
	candidates = []
	if(k < 3):
		candidateItem = getItemFromItemset(data)
		candidates = list(itertools.combinations(candidateItem, k))
	else:
		# 前k-2个要一样
		keys = list(data.keys())
		for i in range(len(keys)):
			items = keys[i].split(' ')
			j = i + 1
			# 跟后面的每一个比较
			while(j < len(keys)):
				m = 0
				items2 = keys[j].split(' ')
				tag = True
				# 判断前k-2个是否都一样
				while(m < k - 2):
					if items[m] != items2[m]: 
						tag = False
						break
					m += 1
				# 如果都一样，产出候选集
				if tag:
					temp = []
					temp.extend(items)
					temp.append(items2[len(items2)-1])
					candidates.append(temp)
				j += 1
	tuppleToString(candidates)
	return candidates

def fromListToObject(list):
	result = {}
	for itemset in list:
		result[itemset] = 1
	return result


def firstMapper(data):
	result = {}
	for item in data:
		if item not in result:
			result[item] = 1
		else:
			result[item] += 1
	# result: {item: count}
	return result

def firstReducer(data):
	# filter
	items = list(data.keys())
	for item in items:
		if data[item] < threshold:
			del data[item]
	# generate candidatesv data: {'1': 2000}
	candidates = generateCandidates(data)
	# print(candidates)
	return candidates

def secondMapper(candidates):
	result = {}
	for candidate in candidates:
		items = candidate.split(' ')
		for bucket in data:
			for i in range(len(items)):
				if items[i] not in bucket:
					break
				if i == len(items) - 1:
					if candidate not in result:
						result[candidate] = 1
					else:
						result[candidate] += 1
	return result

def secondReducer(count):
	itemsets = list(count.keys())
	frequentItemsets = []
	for itemset in itemsets:
		if count[itemset] < threshold:
			del count[itemset]
		else:
			frequentItemsets.append(itemset)
	return frequentItemsets


# first round
frequentItemsets = []
data = initData()
result = firstMapper([j for i in data for j in i])
candidates = firstReducer(result)
toValidates = secondMapper(candidates)
frequentItemset = secondReducer(toValidates)
frequentItemsets.extend(frequentItemset)

#iteration
while(True):
	if len(frequentItemset) > 0:
		k += 1
		roundData = fromListToObject(frequentItemset)
		candidates = generateCandidates(roundData)
		if len(candidates) > 0:
			toValidates = secondMapper(candidates)
			frequentItemset = secondReducer(toValidates)
			frequentItemsets.extend(frequentItemset)
		else: break
	else: break

print('frequentItemsets:')
print(frequentItemsets)






