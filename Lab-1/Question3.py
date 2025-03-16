# Write a program that takes an input representing a day of the week and  output
 
print("Enter the name of the week ")
days=input().strip().lower()
print(f"Debug: You entered '{days}'")
match days:
    case "monday":
        print("Start of the workweek")
        
    case "tuesday" | "wednesday" | "thursday":
        print("Midweek of the week")
    
    case "friday":
        print("Almost weekend")
    
    case "saturday" | "sunday":
        print("Weekend")
    case _:
        print("Invalid Day")

    