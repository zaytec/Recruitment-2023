'''PATTERN RECOGNISER'''
lst = input("Enter your pattern: ").strip().split(',')
pattern_list=[]
half_length=len(lst)//2
for i in range(half_length):
    pattern_list=lst[:i+1]
    repeated = len(lst)//len(pattern_list)

    if lst == pattern_list*repeated:
        print("The pattern found is:",pattern_list,"and the pattern is repeated:",repeated,"times.")
        break
else:
    print("pattern not found")
        

