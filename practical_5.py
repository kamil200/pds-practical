#Python Program to Check if a Given Key Exists in a Dictionary or Not

myDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color": "red",
  "top-speed": "250 mph"
}
print(myDict)
key=input("Enter a Key to find: ")
if key in myDict:
  print("Yes, ",key ,"is one of the keys in the dictionary")
else:
    print("Key not found")
