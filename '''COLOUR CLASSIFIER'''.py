'''COLOUR CLASSIFIER'''
def classify(rgb):
    red_range = range(170, 255)
    blue_range = range(0, 86)
    green_range = range(0, 86)
    r,g,b=rgb

    if r in red_range and b in blue_range and g in green_range:
        return 'Red'
    elif b in red_range and r in blue_range and g in green_range:
        return 'Blue'
    elif g in red_range and b in blue_range and r in green_range:
        return 'green'
    else:
        return "unclassified"
    
r=int(input("Enter the values for red (0-255):"))
b=int(input("Enter the values for blue (0-255):"))
g=int(input("Enter the values for green (0-255):"))

rgb = r,g,b
classification=classify(rgb)
print("The color is:",classification)
