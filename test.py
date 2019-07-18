from house import house

for key, value in house.items():
    # print(key) #meta, objects
    # print(type(value)) #<class 'dict'>, <class 'list'>
    
    if(type(value) == list):
        # print(value) #Prints every object
        print(len(value)) #336
        print(value[292]) #The Mississauga East Cooksville represenative in the house{'objects'} list.
        print(value[292]['photo_url'])


#1: What are the keys in this (top-level) dictionary?
#A: meta, objects

#2: What is the data type of the value that goes with the first key?
#A: Dictionary

#3: What is the data type of the value that goes with the last key?
#A: List

#4: How many representatives are there in this collection?
#A: 336

#5: Get the URL for the photo of one representative into a variable.
#A: http://www.ourcommons.ca/Parliamentarians/Images/OfficialMPPhotos/42/FonsecaPeter_Lib.jpg