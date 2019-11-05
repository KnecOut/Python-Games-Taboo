import csv 

list_words=[]
dict_unspeakable={}
with open ('Database.csv','r') as csv_file:
    csv_content=csv.reader(csv_file)
    for i in csv_content:
        if i[0]=='ï»¿Karaoke ':
            i[0]=='Karaoke'
        list_words.append(i[0])
        
        dict_unspeakable[i[0]]=[i[1],i[2],i[3],i[4],i[5]]                




#list_words=['Nickname','Karaoke','Taxi']
#dict_unspeakable={'Nickname':['Abbreviation','Shorten','Proper','Called','Known'],'Karaoke':['Sing','Music','Song','DJ','Band'],'Taxi':['Uber','Cab','Car','Yellow','Ola']}

#print (dict_unspeakable('Nickname'))