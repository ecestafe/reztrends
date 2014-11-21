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
	infilename='stop_word'
	f=open(infilename,'r')
	line_num=1
	stopArray = []
	newArray = []
	temp = ''
	flag= False
	for line in open(infilename,'r'):
		temp=f.readline()
		temp=temp.strip()
		stopArray.append(str(temp))
	for x in a_list_of_words:
		for y in stopArray:
			if x==y:
				flag=True
				break
		if flag==False:
			newArray.append(x)
		else:
			flag=False
	#return a list of words 
	return newArray

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
    best_business_array = ["suO9O-o1wk9DxYIemojpXQ", "jOSnxb3RdIGJjc66ZUPrAQ", "nCsH1m5Knb8lA8mVktBp1w", "13JSeg330MA5sNhgKzRKMw", "QOC_lGvP9zXcO8jyJ1AyxA", "ufpRzsHvtb-c9H87azPmRA", "CsYj-3uhV5c4jDue8Dp9FA", "XpZpY607eVH5DFbxl6hsag", "2C3J17swOdV7O_QHxzh2bQ", "O2v3n4EHhME9IbLEUBLtng"]
    worst_business_array = ["7fM6ZxF_uHQQIv74vby2nA", "7DYg9G8cLyBRJl1dvngvow", "29ljx7-UmdQC7iArbYwIvw", "1ytwEIHiBX8OrRvS8LTh-A", "P9gLMNOPKI0JnJeuyCr-0g", "TAmyPRgCD4cg62NpEPE6EQ", "ZUz0eeKdmmT1XYzSf2k4tg", "55wvJ5wTgthTyJ-xNHYu-Q", "UAFJr-nn7hGMMbOj26YU9g", "lFS5gqXvAYuF_JTuiLkwi"]

    goodDict ={}
    badDict = {}
    for line in open('yelp_academic_dataset_review.json','r'):
        line_num+=1
        line = line.encode('utf-8','ignore')
        business_id =  str(json.loads(line)['business_id'])
        if business_id in best_business_array:
            if not goodDict.has_key(business_id):
                tempDict = {}
                tempArray = []
                revID = str(json.loads(line)['review_id'])
                #print revID
                if revID == "0L5bdVwJhYdIIC2wAvwUsQ":
                    pass
                else:
                    revText = str(json.loads(line.encode('utf-8','ignore'))['text'])
                    revDate = str(json.loads(line)['date'])
                    revStars = float(json.loads(line)['stars'])
                    revDate = revDate.split("-")
                    revDate = datetime.date(int(revDate[0]), int(revDate[1]), int(revDate[2]))
                    tempArray.append(revDate)
                    tempArray.append(revStars)
                    tempArray.append(revText)
                    tempDict[revID]=tempArray
                    goodDict[business_id]=tempDict
                    business_text[business_id]=revText
            else:
                revID = str(json.loads(line)['review_id'])
                #print revID
                if revID == "0L5bdVwJhYdIIC2wAvwUsQ":
                    pass
                else:
                    revText = str(json.loads(line)['text'])
                    revDate = str(json.loads(line)['date'])
                    revStars = float(json.loads(line)['stars'])
                    revDate = revDate.split("-")
                    revDate = datetime.date(int(revDate[0]), int(revDate[1]), int(revDate[2]))
                    tempArray.append(revDate)
                    tempArray.append(revStars)
                    tempArray.append(revText)
                    (goodDict[business_id])[revID]=tempArray
                    business_text[business_id]+=revText
                
	# if line_num == 1000:
            # break



    # print"====Date Test====\n"
    # test_array= sorted(test_array)
    # print test_array
    reviewCount=1
    arrayIter=0
    for x in goodDict:
        print "=====Business ID:"+str(x)+"===="
        reviewDict=goodDict[x]
        colOne, colTwo = unigram_count(business_text[x])
        print colOne
        print colTwo
        for y in reviewDict:
            contentArray=reviewDict[y]
            print"Review Num:"+str(reviewCount)
            print"Date: "+str(contentArray[arrayIter])
            print"Stars: " +str(contentArray[arrayIter+1])
            print"Text: "+str(contentArray[arrayIter+2])
            reviewCount+=1
            arrayIter+=3
        reviewCount=1
        arrayIter=0
    	
    print"\nThe number of lines was: "+str(line_num)
