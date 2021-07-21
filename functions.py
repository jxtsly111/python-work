# creating a function that returns a value
def greetings(name):
    return "Hello"+name
print(greetings("john"))

def fullname(firstnum,secondnum):
    return firstnum  +  secondnum
print(fullname(5,5))
    
def reverselist(list):
    list.sort(reverse=True)
    list.pop(-1)
    return list
b=[1,2,3,4,5]
print(reverselist(b))

def mood_today(mood = "neutral"):
   return "Today, I am feeling"+" "+mood
print(mood_today(

))
def total_distance(height,length,tower):
     steps= tower/height
     distance =(height*steps)+(length*steps)
     return round(distance,2)
print(total_distance(0.2,0.4,100.0))

def hamming_distance(txt1,txt2):
    count = 0
    for val in (txt1,txt2):
        if val[0] in txt1 != val[0] in txt2:
            count=count+1
            return count
print(hamming_distance("abcd","abdd"))

def double_char(character):
    val= "".join(character+*2 for val in character)
    return character
print(double_char("remove")) 

def double_char(txt):
    char = ""
    for val in txt:
        
        pass

        