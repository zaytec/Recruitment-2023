'''COLOUR CLASSIFIER'''
def classify(r,g,b):

    if r in range(200,300) and b in range(100,200) and g in range(0,100):
        return 'Red'
    elif b in range(200,300) and r in range(100,200) and g in range(0,100):
        return 'Blue'
    elif g in range(200,300) and b in range(100,200) and r in range(0,100):
        return 'green'
    else:
        return "unclassified"
    
r=int(input("Enter the values for red (0-300):"))
b=int(input("Enter the values for blue (0-300):"))
g=int(input("Enter the values for green (0-300):"))

x=classify(r,g,b)
print("The color is:",x)