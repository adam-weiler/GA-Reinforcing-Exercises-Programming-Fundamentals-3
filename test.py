from house import house


# from pprint import pprint
# pprint(house)




for key, value in house.items():
    # print(type(value))
    if(type(value) == list):
        # print('hey')
        # print(value[0])
        print(len(value))
#     pass




#1: What are the keys in this (top-level) dictionary?
#A: meta, objects

#2: What is the data type of the value that goes with the first key?
#A: Dictionary

#3: What is the data type of the value that goes with the last key?
#A: List

#4: How many representatives are there in this collection?
#A: 336

#5: Get the URL for the photo of one representative into a variable.
#A: 