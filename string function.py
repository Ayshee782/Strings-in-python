#string.endswith("substring")-> here return true if ends with substring
a="hi baby"
print(a.endswith("by")) #it will be true
print(a.endswith("hmm"))#it will be false 


#string.capitalize()-> capitalize 1st char

a="hi baby"
b="how are you?"
c="HI BABY"

print(a.capitalize())
print(a.find("a"))#find in index
print(a.casefold()==b.casefold())
print(a.casefold()==c.casefold()) """the meaning is if the sentence is 
                                   same then it's give us true otherwise 
                                   it's gives false"""
