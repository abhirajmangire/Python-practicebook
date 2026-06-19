#Dictonary & set in python
#dictonary :- used to store the data values in key:value pairs
#they are unordered ,mutable and dont allow duplicate

info ={
    "name": "Abhiraj",
    "DOB" :  "12-03-2006",
    "Age": 20,
    "Role": ["a","b","c"]

}
print(info)

#can use mutables as values and immutables ans both keys and values

print(info["name"])
info["name"] ="Abhi" #over write old values
info["surname"]= "Mangire"
print(info)

null_dict ={}
print(null_dict)

#nested dictionary in python
student = {
    "name":"Abhiraj",
    "subjects" :{
        "phy":98,
        "maths":99
    },
    "roll_no": 1220

}
print(student)
print(student["subjects"])
print(student["subjects"]["phy"])

#methods in Dictionary
print(info.keys()) #returns all keys
print(info.values()) #returns all values
print(info.items()) #returns all the (key,val) paisr as tuplee
print(info.get("name")) #returns the key accordilngly to values
newDict = {"city": "PuneS"}
print(info.update(newDict)) #insert the specified items too the dictio
print(list(info.values()))


#sets in python
#set is mutable but the elements are immutable
#so we can pass tuple in set and cant pass list or string
#set is the collection of the unorderded items , each element in the set must be unique and immutable
#num ={1,2,,3,4,4,5,5,6} repetded elements stored only once , so it resolved to {1,2,3,4,5,6}
collection= {1,2,3,4,5}
print(collection)
print(len(collection)) #total numbers of items
print(type(collection))
null_set= set() #empty set
null_dict ={} #empty dictionary

#methods of set
collection.add(7) #adds an element 
print(collection)
collection.remove(1) #removes an element
print(collection)

#collection.add([1,2,34,4,]) #error for both unhashable (thing that mutate)

print(collection.pop()) #removes a random value 

collection.clear() #empties the set
print(collection)

set1= {1,2,3,4,5,6}
set2={3,4,5,6,7,8,9,10}
print(set1.union(set2)) #combines both set vlaues And return values
print(set1.intersection(set2)) #combines common values and return vlaues