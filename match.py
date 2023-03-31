import json
from openpyxl import Workbook
# Make a dictionary of majors as keys, with the values being fields within that major

# The next dictionary would use fields as keys, subfields as values

# Keep getting smaller and more specific



majors = {
    "Computer Science": {
        "Software Engineering",
        "Cybersecurity",
        "Data Science"
    },
    "Mechanical Engineering": {
        "Design",
        "Manufacturing",
        "Mechanics",
        "Thermodynamics",
        "Materials"
    },
    "Chemical Engineering": {
        "Environmental",
        "Design",
        "Safety",
        "Plant",
        "Waste"
    },
    "Aerospace Engineering": {
        "Aircraft",
        "Aerodynamics",
        "Thermodynamics",
        "Materials",
        "Mechanics"

    },
    "Electrical Engineering": {
        "Electronics",
        "Computer",
        "Robotics"

    }


}

stop_words = []
stop = open("stop_words.txt")
for i in stop:
    stop_words.append(i)
    


# Make some example functions that take in familiar keywords for different 

def make_workbook(path, jobs):
    workbook = Workbook()
    sheet = workbook.active
    count = 0
    for i in jobs:
        count += 1
        sheet['A' + str(count)] = i

    workbook.save(path)
    return workbook 

def match(major):
    key = major.lower()
    if key not in majors:
        majors[key] = ""
        return false 
    return true
    

def spec(major):
    match_count = 0
    matches = []
    for val in majors[major]:
        #if json data == val, add to list of potential matches
        title = #title of job
        link = #link to job
        matches[match_count] = (title, link)




#read from json file
f = open("resume.txt")
data = f.readlines()

name = data[0] 
major = data[1]


#Check if major is in our dict
matches = match(major)
#If in dict, look for key words, else we add new key words to our new dictionary that this will create

#Make empty array of jobs
jobs = []

if(matches):
    #start searching for key words
    for x in data:
        if (x in majors[major]):
            #add to an array the jobs saved under the key
            for job in majors[major]:
                jobs.append(job)

else:
    majors[major] = " "
#Make file 

job_file = make_workbook(name + "_jobs.csv", jobs)


        


#return some sort of doc (maybe excel) with links to jobs in order of best match to worst (focus on ordering later)

f.close()