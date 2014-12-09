import json #or cjson
import re
from operator import itemgetter
from math import log10, fabs
import datetime
from stemming.porter2 import stem

def tokenize(string):
        #----your code----
	#lowerString = str.lower(string)
	varArray =  re.split( '\W+', string)
	return varArray



	#return a list of words
	#pass
    
def stopword(a_list_of_words):
	#----your code----
    stopword = []
    for line in open('stop_word','r'):
        stopword.append(re.split('\n',line)[0])
    new_list=[word for word in a_list_of_words if word not in stopword]
    return new_list

def stemming(a_list_of_words):
	#----your code----
	temp = ''
	stemmedArray = []
	for x in a_list_of_words:
		temp=stem(x)
		stemmedArray.append(temp)    
	#return a list of words
	return stemmedArray 

def unigram_count( mainString):
        line_num=1
        dictStop = {}
        dictNoStop = {}
	unfilteredArray = tokenize(mainString)
	filteredArray = stopword(unfilteredArray)
	stemmArray = stemming(filteredArray)
	for x in filteredArray:
		if dictStop.has_key(x):
			temp = dictStop[x] 
			temp+=1
			dictStop[x] = temp
		else:
			dictStop[x]=1
	for x in stemmArray:
		if dictNoStop.has_key(x):
			temp = dictNoStop[x]
			temp+=1
			dictNoStop[x] = temp
		else:
			dictNoStop[x]=1
	line_num+=1
	dictStopArray = sorted(dictStop, key=dictStop.__getitem__, reverse=True)
	dictNoStopArray = sorted(dictNoStop, key=dictNoStop.__getitem__, reverse=True)
	count=0
	tempAns = ''
	collectionOne=[]
	collectionTwo=[]
	for x in dictStopArray:
		if(count==20):
			break
		tempAns+='['+x
		tempAns+=': '
		tempAns+=str(dictStop.get(x))+']'
		collectionOne.append(str(tempAns))
		count+=1
		tempAns=''
	# print '======CollectionOne=====\n'
	# print collectionOne
	count=0
	for x in dictNoStopArray:
		if(count==20):
			break
		tempAns+='['+x
		tempAns+=': '
		tempAns+=str(dictNoStop.get(x))+']'
		collectionTwo.append(str(tempAns))
		count+=1
		tempAns=''
	# print  '======CollectionTwo=====\n'
	# print collectionTwo

	#return top 20 unigrams e.g. {[hot,99],[dog,66],...}
	return collectionOne, collectionTwo


def bigram_count(self,a_document_name):
	#-----your code-----
	f=open(a_document_name,'r')
	line_num=1
	dictStop = {}
	while(line_num<300):
		currentString = f.readline()
		currentString = Hw1.read_line(currentString)['text']
		unfilteredArray = Hw1.tokenize(currentString)
		filteredArray = Hw1.stopword(unfilteredArray)
		line_num+=1
		size=len(filteredArray)-1
		count= 0
		while count<size:
			tempString = filteredArray[count]+' '+filteredArray[count+1]
			# print tempString
			count+=1
			if dictStop.has_key(tempString):
				temp = dictStop[tempString] 
				temp+=1
				dictStop[tempString] = temp
			else:
				dictStop[tempString]=1
	dictStopArray = sorted(dictStop, key=dictStop.__getitem__, reverse=True)
	count=0
	tempAns = ''
	collectionOne=[]
	for x in dictStopArray:
		if(count==20):
			break
		tempAns+='['+x
		tempAns+=': '
		tempAns+=str(dictStop.get(x))+']'
		collectionOne.append(str(tempAns))
		count+=1
		tempAns=''
	# print '======CollectionOne=====\n'
	# print collectionOne

	#return top 20 bigrams and frequency pairs, e.g. {[hot dog,88],[apple pie,54],...}
	return collectionOne


if __name__ == '__main__':
    line_num=0
    business_revnum = {}
    business_avg = {}
    business_text = {}
    test_array = []
    average_rev = 0.0
    best_business_array = ["qIyqUlzqEAeb8MmDZ2o5kQ", "YkxyI2guuPcmgWFk0a0aDQ", "i_hw78DZv-oGvBvTx8FU3A", "MY0_6BAzQCu4sqXqwNEFfg", "CDN--GWL8gm4TsFFtccpaA", "e3v5KRh05Qqb64U6R8U-rA", "K2VQpb53hzGwSI5wfepEAw", "8Cg_Y6kI0TPaGYSSLGvYgg", "A8dOA00FGNoJ46CDo6cTvQ", "M4aGbEXZjOnBFn9C6IbrYQ"]
    worst_business_array = ["UmhTiNOKareQDP7D9aAnKw", "KwLfgeylp9d8zY3KacREiw", "c2OXxIm1Gu3Hxh7K9Rsovw", "8HCC8NuJmdHnEg2XC00NPg", "WnY4HPJIYNXOPQH2mFzl2Q", "YhBFM3xy2G6DQC2VKXVkTA", "YZxA6w82eFJFntwqJLln6w", "d-_ZMeph2MIsCOEhKCkTbA", "YY1UCrnuOLCTxK3mKsqiDw", "1bnte8O-rO_RcRlp9y2u7Q"] 
    goodDict ={}
    badDict = {}
    for line in open('yelp_academic_dataset_business.json','r'):
        line_num+=1
        line = line.encode('utf-8','ignore')
        business_id =  str(json.loads(line)['business_id'])
        if business_id in best_business_array:
            if not goodDict.has_key(business_id):
                tempDict = {}
                tempArray = []
				
                addr = str(json.loads(line)['full_address'])
		hours = str(json.loads(line)['hours'])
		categories = str(json.loads(line)['categories'])
		city = str(json.loads(line)['city'])
		review_count = float(json.loads(line)['review_count'])
		name = str(json.loads(line)['name'])
		neighborhoods = str(json.loads(line)['neighborhoods'])
				
		longitude = float(json.loads(line)['longitude'])
		state = str(json.loads(line)['state'])
		stars = float(json.loads(line)['stars'])
		latitude = float(json.loads(line)['latitude'])
		attributes = str(json.loads(line)['attributes'])
			
		tempArray.append(addr)
        	tempArray.append(hours)
		tempArray.append(categories)
		tempArray.append(city)
		tempArray.append(review_count)
		tempArray.append(name)
		tempArray.append(neighborhoods)
				
		tempArray.append(longitude)
		tempArray.append(state)
		tempArray.append(stars)
		tempArray.append(latitude)
		tempArray.append(attributes)
				
		tempDict[name]=tempArray
		goodDict[business_id]=tempDict
            else:
                tempArray = []		
                addr = str(json.loads(line)['full_address'])
		hours = str(json.loads(line)['hours'])
		categories = str(json.loads(line)['categories'])
		city = str(json.loads(line)['city'])
		review_count = float(json.loads(line)['review_count'])
		name = str(json.loads(line)['name'])
		neighborhoods = str(json.loads(line)['neighborhoods'])
				
		longitude = float(json.loads(line)['longitude'])
		state = str(json.loads(line)['state'])
		stars = float(json.loads(line)['stars'])
		latitude = float(json.loads(line)['latitude'])
		attributes = str(json.loads(line)['attributes'])
			
		tempArray.append(addr)
        	tempArray.append(hours)
		tempArray.append(categories)
		tempArray.append(city)
		tempArray.append(review_count)
		tempArray.append(name)
		tempArray.append(neighborhoods)
				
		tempArray.append(longitude)
		tempArray.append(state)
		tempArray.append(stars)
		tempArray.append(latitude)
		tempArray.append(attributes)
                (goodDict[business_id])[name]=tempArray
        elif business_id in worst_business_array:
            if not badDict.has_key(business_id):
                tempDict = {}
                tempArray = []
				
                addr = str(json.loads(line)['full_address'])
		hours = str(json.loads(line)['hours'])
		categories = str(json.loads(line)['categories'])
		city = str(json.loads(line)['city'])
		review_count = float(json.loads(line)['review_count'])
		name = str(json.loads(line)['name'])
		neighborhoods = str(json.loads(line)['neighborhoods'])
				
		longitude = float(json.loads(line)['longitude'])
		state = str(json.loads(line)['state'])
		stars = float(json.loads(line)['stars'])
		latitude = float(json.loads(line)['latitude'])
		attributes = str(json.loads(line)['attributes'])
			
		tempArray.append(addr)
        	tempArray.append(hours)
		tempArray.append(categories)
		tempArray.append(city)
		tempArray.append(review_count)
		tempArray.append(name)
		tempArray.append(neighborhoods)
				
		tempArray.append(longitude)
		tempArray.append(state)
		tempArray.append(stars)
		tempArray.append(latitude)
		tempArray.append(attributes)
				
		tempDict[name]=tempArray
		badDict[business_id]=tempDict
            else:
                tempArray = []		
                addr = str(json.loads(line)['full_address'])
		hours = str(json.loads(line)['hours'])
		categories = str(json.loads(line)['categories'])
		city = str(json.loads(line)['city'])
		review_count = float(json.loads(line)['review_count'])
		name = str(json.loads(line)['name'])
		neighborhoods = str(json.loads(line)['neighborhoods'])
				
		longitude = float(json.loads(line)['longitude'])
		state = str(json.loads(line)['state'])
		stars = float(json.loads(line)['stars'])
		latitude = float(json.loads(line)['latitude'])
		attributes = str(json.loads(line)['attributes'])
			
		tempArray.append(addr)
        	tempArray.append(hours)
		tempArray.append(categories)
		tempArray.append(city)
		tempArray.append(review_count)
		tempArray.append(name)
		tempArray.append(neighborhoods)
				
		tempArray.append(longitude)
		tempArray.append(state)
		tempArray.append(stars)
		tempArray.append(latitude)
		tempArray.append(attributes)
                (badDict[business_id])[name]=tempArray
	# if line_num == 1000:
            # break



    # print"====Date Test====\n"
    # test_array= sorted(test_array)
    # print test_array
    reviewCount=1
    arrayIter=0
    print "=====================Rising Stars ====================="
    for x in goodDict:
        print "=====Business ID:"+str(x)+"===="
        reviewDict=goodDict[x]
        for y in reviewDict:
            contentArray=reviewDict[y]
            print"Name: "+str(contentArray[arrayIter+5])
            print"Address: "+str(contentArray[arrayIter])
            print"City: "+str(contentArray[arrayIter+3])
            print"State: "+str(contentArray[arrayIter+8])
            print"Stars: "+str(contentArray[arrayIter+9])
            print"Review Count: " +str(contentArray[arrayIter+4])
            print"Hours: " +str(contentArray[arrayIter+1])
            print"Categories: "+str(contentArray[arrayIter+2])
            print"Neighborhoods: "+str(contentArray[arrayIter+6])
            print"Longitude: " +str(contentArray[arrayIter+7])
            print"Latitude: " +str(contentArray[arrayIter+10])
            print"Attributes: "+str(contentArray[arrayIter+11])
            print ""
            reviewCount+=1
            arrayIter+=3
        reviewCount=1
        arrayIter=0
    print "=====================Slumping Businesses ====================="
    for x in badDict:
        print "=====Business ID:"+str(x)+"===="
        reviewDict=badDict[x]
        for y in reviewDict:
            contentArray=reviewDict[y]
            print"Name: "+str(contentArray[arrayIter+5])
            print"Address: "+str(contentArray[arrayIter])
            print"City: "+str(contentArray[arrayIter+3])
            print"State: "+str(contentArray[arrayIter+8])
            print"Stars: "+str(contentArray[arrayIter+9])
            print"Review Count: " +str(contentArray[arrayIter+4])
            print"Hours: " +str(contentArray[arrayIter+1])
            print"Categories: "+str(contentArray[arrayIter+2])
            print"Neighborhoods: "+str(contentArray[arrayIter+6])
            print"Longitude: " +str(contentArray[arrayIter+7])
            print"Latitude: " +str(contentArray[arrayIter+10])
            print"Attributes: "+str(contentArray[arrayIter+11])
            print ""
            reviewCount+=1
            arrayIter+=3
        reviewCount=1
        arrayIter=0
    	
    print"\nThe number of lines was: "+str(line_num)
