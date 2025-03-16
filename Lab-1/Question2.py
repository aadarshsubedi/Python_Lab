word=input("Enter the value")
match word:
    case "Red" : 
        print("Stop")
    case "Yellow" :
        print("Slow down")
    case "Green" :
        print ("GO")
    case _: 
        print("Invalid Color")