# string = input()
# n = len(string)
i=0
count=0
AB=True
BA =True

# while i<n-1:
#     if (string[i]=='A' and string[i+1]=='B') and AB:
#         count+=1
#         AB=False
#         i+=2
#     elif (string[i]=='B' and string[i+1]=='A') and BA:
#         count+=1
#         BA=False 
#         i+=2
#     else:
#         i+=1

# print( "YES" if count>=2 else "NO")

s = input()

if "AB" in s and "BA" in s.replace("AB", "-", 1):
    print("YES")
elif "BA" in s and "AB" in s.replace("BA", "-", 1):
    print("YES")
else:
    print("NO")

