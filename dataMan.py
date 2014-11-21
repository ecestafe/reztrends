import json #or cjson
import re
from operator import itemgetter
from math import log10, fabs
import datetime

if __name__ == '__main__':
    line_num=0
    business_revnum = {}
    business_avg = {}
    test_array = []
    average_rev = 0.0
    for line in open('yelp_academic_dataset_review.json','r'):
        line_num+=1
        business_id =  str(json.loads(line)['business_id'])
        star_num = float(json.loads(line)['stars'])
        rev_date = str(json.loads(line)['date'])
        average_rev+=star_num
        rev_date = rev_date.split("-")
        rev_date = datetime.date(int(rev_date[0]), int(rev_date[1]), int(rev_date[2]))
        test_array.append(rev_date)
        if not business_revnum.has_key(business_id):
            business_revnum[business_id]=1
            business_avg[business_id]=star_num
        else:
            business_revnum[business_id] = (business_revnum[business_id] + 1)
            business_avg[business_id]+= star_num
        # if line_num == 1000:
            # break

    for x in business_avg:
        num=float(business_avg[x])
        den=float(business_revnum[x])
        temp = float(num/den)
        business_avg[x]= float(temp)

    # print"====Date Test====\n"
    # test_array= sorted(test_array)
    # print test_array
    
    print "====Top Individual Business Averages===="
    count =1
    top_business_avg_sort = sorted(business_avg, key=business_avg.__getitem__, reverse=True)
    for x in top_business_avg_sort:
        if (business_revnum[x])> 10:
            print str(count)+". Business Id:"+str(x)+" - Average: "+str(business_avg[x])
            print "                                     - Number of Reviews: "+str(business_revnum[x])+"\n"
            count+=1
        if count == 11:
            break

    print "====Bottom Individual Business Averages===="
    count =1
    worst_business_avg_sort = sorted(business_avg, key=business_avg.__getitem__, reverse=False)
    for x in worst_business_avg_sort:
        if (business_revnum[x])> 10:
            print str(count)+". Business Id:"+str(x)+" - Average: "+str(business_avg[x])
            print "                                     - Number of Reviews: "+str(business_revnum[x])+"\n"
            count+=1
        if count == 11:
            break
		
    print"\nThe number of lines was: "+str(line_num)
