import csv

def readdata(filenm):
    data = {}
    f=open(r"class.csv")
    reader = csv.DictReader(f)
    for row in reader:        
        key  = row.pop('NAME').upper()
        data[key]=row
    f.close()
    return data

def get_rec(mydata,txt):
    return mydata.get(txt) #,"Key nonexistent")
#    return mydata[txt]
#     for k, v in mydata.items():
#         if k==txt :
#             return v
        #print(k, v)


mydata = readdata("class.csv")
print(mydata.keys())
print("Select Comma delimited list of Name IDsr or ALL to export records to file\n")
inp=input('Enter Choice:')
with open('lesson.txt','w') as f:
    field_names = ['NAME', 'SEX', 'AGE', 'HEIGHT', 'WEIGHT']
    writer=csv.DictWriter(f,fieldnames=field_names)
    writer.writeheader()
    if inp.upper()=='ALL':
        for k, v in mydata.items():  
            v.update({'NAME':k})
            writer.writerow(v)
            #csv.writer(f).write(mydata.items())
    else:
        for i in inp.split(','):
            data=get_rec(mydata,i)
            data['NAME']=i
            writer.writerow(data)

# with open('lesson.txt','w') as f:
#     csv.writer(f).writerows(z.items())
#     f.write(f'\n' + z + '\n')
    
#print(z)

#data_points = ["id","age","sex"]




# data=[]
# f= open(r"class.csv",'r')
# for line in f:
#     data_line=line.strip().split(',')
#     data.append(data_line)
#     print(line)
# print (data)
# f.close()

# import pandas as pd
# df = pd.read_csv('class.csv')
# print(df)







# import csv
# def read_data(input_file):
#     """read in the data and return a dictionary"""    
#     data = {}
#     with open(input_file) as infile:
#         reader = csv.DictReader(infile)
#         for row in reader:
#             key  = row.pop('NAME').upper()
#             data[key]=row
#     return data            

            
# def get_subject_details(subject,data):
    
#     try:
#         return data[subject]
#     except KeyError:
#         raise KeyError("Subject not found")
        

# if __name__=="__main__":
#     data = read_data("class.csv")
    
#     value = get_subject_details("ALICE",data)
    
#     print(value)