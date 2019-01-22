import urllib.request as rere

global salary_comp
salary_comp=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
ages={10:0,20:0,30:0,40:0,50:0,60:0,70:0,80:0,90:0}


workclass={" Private":0, " Self-emp-not-inc":0, " Self-emp-inc":0, " Federal-gov":0, " Local-gov":0,
           " State-gov":0, " Without-pay":0, " Never-worked":0," ?":0}

education={" Bachelors":0, " Some-college":0, " 11th":0, " HS-grad":0, " Prof-school":0, " Assoc-acdm":0,
            " Assoc-voc":0, " 9th":0, " 7th-8th":0, " 12th":0, " Masters":0, " 1st-4th":0, " 10th":0, " Doctorate":0,
            " 5th-6th":0, " Preschool":0," ?":0}

marital_status={" Married-civ-spouse":0, " Divorced":0, " Never-married":0, " Separated":0,
" Widowed":0, " Married-spouse-absent":0," Married-AF-spouse":0," ?":0}

occupation={" Tech-support":0, " Craft-repair":0, " Other-service":0, " Sales":0, " Exec-managerial":0, " Prof-specialty":0,
            " Handlers-cleaners":0, " Machine-op-inspct":0, " Adm-clerical":0, " Farming-fishing":0, " Transport-moving":0,
            " Priv-house-serv":0, " Protective-serv":0, " Armed-Forces":0," ?":0}

relationship={" Wife":0, " Own-child":0, " Husband":0, " Not-in-family":0, " Other-relative":0, " Unmarried":0,"?":0}

race={" White":0, " Asian-Pac-Islander":0, " Amer-Indian-Eskimo":0, " Other":0, " Black":0," ?":0}

sex={" Female":0, " Male":0,"?":0}

hours_per_week={0:0,10:0,20:0,30:0,40:0,50:0,60:0,80:0}

native={" United-States":0, " Cambodia":0, " England":0, " Puerto-Rico":0, " Canada":0, " Germany":0
    , " Outlying-US(Guam-USVI-etc)":0, " India":0, " Japan":0, " Greece":0, " South":0, " China":0,
        " Cuba":0, " Iran":0, " Honduras":0, " Philippines":0, " Italy":0, " Poland":0, " Jamaica":0, " Vietnam":0,
        " Mexico":0, " Portugal":0, " Ireland":0, " France":0, " Dominican-Republic":0, " Laos":0, " Ecuador":0,
        " Taiwan":0, " Haiti":0, " Columbia":0, " Hungary":0, " Guatemala":0, " Nicaragua":0, " Scotland":0,
        " Thailand":0, " Yugoslavia":0, " El-Salvador":0, " Trinadad&Tobago":0, " Peru":0, " Hong":0
    , " Holand-Netherlands":0," ?":0}

salary={" >50K":0, " <=50K":0}



def upper_lower(attr,samp,innt):
    if(attr[innt]==samp[innt]):
        if ('<' in attr[10]):
            salary_comp[innt][0]+=1
        elif('>' in attr[10]):
            salary_comp[innt][1]+= 1

def classification(attr_list,sample):
        num1=attr_list[0][0] + "0"
        num2=sample[0][0]+"0"
        tempera=ages[int(num1)]
        ages[int(num1)]=tempera+1
        if((num1)==(num2)):
            if ('<' in attr_list[10]):
                salary_comp[0][0] += 1
            elif ('>' in attr_list[10]):
                salary_comp[0][1] += 1


        temp=workclass[attr_list[1]]
        workclass[attr_list[1]]=temp+1
        upper_lower(attr_list,sample,1)


        temp1=education[attr_list[2]]
        education[attr_list[2]]=temp1+1
        upper_lower(attr_list,sample,2)


        temp2=marital_status[attr_list[3]]
        marital_status[attr_list[3]]=temp2+1
        upper_lower(attr_list,sample,3)


        temp3=occupation[attr_list[4]]
        occupation[attr_list[4]]=temp3+1
        upper_lower(attr_list,sample,4)


        temp4=relationship[attr_list[5]]
        relationship[attr_list[5]]=temp4+1
        upper_lower(attr_list,sample,5)

        temp5=race[attr_list[6]]
        race[attr_list[6]]=temp5+1
        upper_lower(attr_list,sample,6)


        temp6=sex[attr_list[7]]
        sex[attr_list[7]]=temp6+1
        upper_lower(attr_list,sample,7)

        num3=attr_list[8][0]+"0"
        num4=sample[8][0]+"0"
        hours_per_week[int(num3)]+=1
        if((num3)==(num4)):
            if ('<' in attr_list[10]):
                salary_comp[8][0] += 1
            elif ('>' in attr_list[10]):
                salary_comp[8][1] += 1

        temp7=native[attr_list[9]]
        native[attr_list[9]]=temp7+1
        upper_lower(attr_list,sample,9)

        if ('<' in attr_list[10]):
            temper=salary[" <=50K"]
            salary[" <=50K"]=temper+1
        elif ('>' in attr_list[10]):
            temper1=salary[" >50K"]
            salary[" >50K"]=temper1+1




def crop_data(line):
    del line[2]
    del line[3]
    del line[8]
    del line[8]
f=open(r"","r")
lines_of_data=f.readlines()
global predict_person
predict_person=lines_of_data[1].split(',')
crop_data(predict_person)
print(predict_person)
for i in lines_of_data[2:-1]:
    sample_people=i.split(',')
    crop_data(sample_people)
    classification(sample_people,predict_person)

def pos(bayes_list):
    return float(bayes_list[1]/(bayes_list[0]+bayes_list[1]))
def neg(bayes_list):
    return float(bayes_list[0]/(bayes_list[0]+bayes_list[1]))

negative=salary[" <=50K"]/(salary[" <=50K"]+salary[" >50K"])
positive=salary[" >50K"]/(salary[" >50K"]+salary[" <=50K"])
for i in salary_comp:
    negative=negative*neg(i)
    positive=positive*pos(i)

print("Probability of under 50K=  ",negative)
print("Probability of over 50K=  ",positive)
if(negative<positive):
    print("This person's salary is over 50K")
else:
    print("This person's salary is under 50K")

