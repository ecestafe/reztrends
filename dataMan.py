import json #or cjson
import re
from operator import itemgetter
from math import log10, fabs
import datetime

if __name__ == '__main__':
    line_num=0
    business_revnum = {}
    business_avg = {}
    business_main = {}
    business_main_array = []
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
            temparray = []
            temparray.append(star_num)
            business_revnum[business_id]=1
            business_avg[business_id]=star_num
            business_main[business_id]=temparray
        else:
            business_revnum[business_id] = (business_revnum[business_id] + 1)
            business_avg[business_id]+= star_num
            temparray=business_main[business_id]
            temparray.insert(0, star_num)
            
        #if line_num == 1000:
          # break

    for x in business_avg:
        num=float(business_avg[x])
        den=float(business_revnum[x])
        temp = float(num/den)
        business_avg[x]= float(temp)

    local_avg_dict= {}
    local_avg = 0.0
    for x in business_main:
##        print "Business ID: "+str(x)
        localarray=business_main[x]
        count=1
        if len(localarray)>=10:
            for y in localarray:
                local_avg+=y
                count+=1
                if count ==10:
                    local_avg=local_avg/10
                    local_avg_dict[x]=local_avg
                    break

##    print local_avg_dict
    rising_star_dict = {}
    for x in local_avg_dict:
        tempval = business_avg[x]-local_avg_dict[x]
        rising_star_dict[x] = tempval
    #print rising_star_dict

    print"====Slumping Business Variance====\n"
    rinsing_star_sort = sorted(rising_star_dict, key=rising_star_dict.__getitem__, reverse=True)
    tempcount = 1
    for x in rinsing_star_sort:
        if tempcount == 11:
            break
        print str(tempcount)+". Business Id:"+str(x)+" - Variance: "+str(rising_star_dict[x])
        tempcount+=1

    print"====Rising Business Variance====\n"
    rinsing_star_sort = sorted(rising_star_dict, key=rising_star_dict.__getitem__, reverse=False)
    tempcount = 1
    for x in rinsing_star_sort:
        if tempcount == 11:
            break
        print str(tempcount)+". Business Id:"+str(x)+" - Variance: "+str(rising_star_dict[x])
        tempcount+=1
        
##    print "====Top Individual Business Averages===="
##    count =1
##    top_business_avg_sort = sorted(business_avg, key=business_avg.__getitem__, reverse=True)
##    for x in top_business_avg_sort:
##        if (business_revnum[x])> 10:
##            print str(count)+". Business Id:"+str(x)+" - Average: "+str(business_avg[x])
##            print "                                     - Number of Reviews: "+str(business_revnum[x])+"\n"
##            count+=1
##        if count == 11:
##            break
##
##    print "====Bottom Individual Business Averages===="
##    count =1
##    worst_business_avg_sort = sorted(business_avg, key=business_avg.__getitem__, reverse=False)
##    for x in worst_business_avg_sort:
##        if (business_revnum[x])> 10:
##            print str(count)+". Business Id:"+str(x)+" - Average: "+str(business_avg[x])
##            print "                                     - Number of Reviews: "+str(business_revnum[x])+"\n"
##            count+=1
##        if count == 11:
##            break
		
    print"\nThe number of lines was: "+str(line_num)
