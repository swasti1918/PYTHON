### a.items

marks = {
     "swasti":80,
     "kriyanshi":100,
     "divit":70 ,
     0 : "swasti"
 
 } 
print(marks.items())

# ### a.keys()

marks={
     "swasti":80,
     "kriyanshi":100,
     "divit":70 ,
     0 : "swasti"
  
 } 
# # print(marks.keys())
# print(marks.values())

 ### a.updates
marks = {
     "swasti":27,
     "sanyam":78,
    0:"swasti" 
 }
# marks.update({"swasti":84,"kriyanshi":96})
# print(marks)

### a.get()

marks = {
    "swasti":89,
    "kriyanshi":92,
    "sanyam":89
}


print(marks.get("swasti 1"))     ######## prints none
print(marks["swasti 1"])         ######## Returns an error


