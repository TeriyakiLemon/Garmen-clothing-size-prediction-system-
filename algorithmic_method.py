import os
class dress_data(): #class that does holds all the dress data and the functions to manipulate them
    def __init__(self):
        self.dress_measurements=[] #this holds the names of all the dress measurements like size, waist circumferenece, etc.
        self.dress_list=[] #a list with dress data. Each element is a dict with dress measurements
    def initial_upload(self): #uploads file with dress size data. 
        if self.dress_list or self.dress_measurements: #if we already uploaded a file, return
            return
        file="dress sizes.txt" #name of file with dress sizes. NEED TO CHANGE THIS CAUSE THE FILE HAS NO DIRECTORY.
        with open(file) as file:
            file_data=file.readlines() 
            count=1
            for line in file_data: #read each line in the file
                if line=="\n": 
                    break
                line=line.strip()
                line=line.split(",") #puts data in each text line into a list
                if count==1: #the first line in the text file is the name of the dress measurements
                    self.dress_measurements=line 
                else: #the other lines of the text file are the measurements of a dress
                    dress_dict={}
                    for index in range(len(self.dress_measurements)):
                        dress_dict[self.dress_measurements[index]]=float(line[index])
                    self.dress_list.append(dress_dict)
                count+=1
    def find_fit(self,chest,hip,waist): #algorithm to match dress sizes given a persons chest,waist,hip.
        result=[]
        for dress in self.dress_list: #iterates through all dress
            score=abs(chest-dress["bust"])+abs(hip-dress["widest hip circle"])+abs(waist-dress["waist"])
            result.append([score,dress["USA size"]]) #assigns each dress a score (lower score is better) and appends the score corresponding size to the array
        result.sort() #sort array from least to greatest according to score. If both scores are the same, the smaller size gets tiebreaker
        return result[0] #return first result
text=dress_data()
text.initial_upload()



