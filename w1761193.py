# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution. 

#w1761193
#28th November 2019
def display(): #function definition.
    print ('these are the new list for pass', newexecellentList)#the new lists are printed which has removed the values which are not in range.
    print ('these are the new list for defer', newdeferlist)
    print ('these are the new list for fail', newfaillist)
def new_array_append():
    execellentList1.append(newexecellentList[i])#the values with correct total are stored in these arrays.
    newdeferlist1.append(newdeferlist[i])
    newfaillist1.append(newfaillist[i])
def grading_system(): #function definition.
    if execellentList1[i]==120:  #the grading system.
        print ('**Progress**')
            
    elif execellentList1[i]==100:
        print ('**Progress - module trailer**')
            
    elif execellentList1[i]>=40 and newdeferlist1[i]>=20:
        print ('**Do not progress - module retriever**')
            
    elif execellentList1[i]>=60 and newfaillist1[i]>=40:
        print ('**Do not progress - module retriever**')
            
    elif execellentList1[i]>=20 and newdeferlist1[i]>=40:
        print ('**Do not progress - module retriever**')
            
    elif execellentList1[i]>=0 and newdeferlist1[i]>=60:
        print ('**Do not progress - module retriever**')
           
    else:   #if the above conditions are not satisfied the output should be exclude.
        print ('**Exclude**')



execellentList=[120,10,100,80,60,0,]#3 arrays inetialised, with pass defer and fail credits.
deferlist=[0,30,20,20,20,0,]
faillist=[0,50,0,20,20,120,]
newexecellentList=[] #these are new arrays in which the correct values are stored.
newdeferlist=[]
newfaillist=[]
execellentList1=[]#new arrays in which only the ones with the correct totals are stored.
newdeferlist1=[]
newfaillist1=[]
for i in range(len(execellentList)):#range checking. index positions are used to traverse the array.
    if execellentList[i]!=0 and execellentList[i]!=20 and execellentList[i]!=40 and execellentList[i]!=60 and execellentList[i]!=80 and execellentList[i]!=100 and execellentList[i]!=120  :
        print('***the value in the index position ',i,'is not in range in pass list***')
        continue
    newexecellentList.append(execellentList[i])#the values with correct ranges are stored in this array
for i in range (len(deferlist)):#range checking. 
    if deferlist[i]!=0 and deferlist[i]!=20 and deferlist[i]!=40 and deferlist[i]!=60 and deferlist[i]!=80 and deferlist[i]!=100 and deferlist[i]!=120  :
        print ('***the value in the index position ', i ,'is not in range in defer list***')
        continue
    newdeferlist.append(deferlist[i])#the values with correct ranges are stored in this array.
for i in range (len(faillist)):#range checking. 
    if faillist[i]!=0 and faillist[i]!=20 and faillist[i]!=40 and faillist[i]!=60 and faillist[i]!=80 and faillist[i]!=100 and faillist[i]!=120 :
        print ('***the value in the index position ', i ,'is not in range in fail list***')
        continue
    newfaillist.append(faillist[i])#the values with correct ranges are stored in this array.
display() #function call
for i in range (len(newexecellentList)):#checking range of the total.
    if newexecellentList[i]+newdeferlist[i]+newfaillist[i]!=120:
        print('**the values in the index ',i,'does not add up to 120, so wrong values are stored**')
        continue
    new_array_append()
for i in range (len(execellentList1)):
    grading_system()#function call
            
