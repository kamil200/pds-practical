



str = "aaaaBBBBBCCCCCC."
modified_str = ''
for char in range(0, len(str)):
	
	if(str[char] == 'a'):
	
		modified_str += '$'
	else:
		
		modified_str += str[char]

print("Modified string : ")
print(modified_str)
