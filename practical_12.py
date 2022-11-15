

f = open("test.txt","r")
#reads all lines of files using readlines()
    
lines=f.readlines()
print(lines,"\n\n")
f.close()
file = open("test.txt","r")
#read first 20 letters in file 
print("20 character : ",file.read(20))
file.close()
file1=open("test.txt","r")
#length of each line in file

count =1
for line in file1 :
    print("\n lenght of line  ",count,"  :  ",len(line))
    count+=1
