# Create a YouTube app that performs display, add, update, and delete operations using a .txt file as the backend.
import os
def display_content():
    with open(filename,"r") as f:
        content=f.readlines()
        for index,value in enumerate(content):
            print(f"{index+1} : {value}")              
print("Youtube")

filename="youtube.txt"
while(1):
    print("1) Display \n2)Add Video \n3)Update Video \n4)Delete Video\n5)Exit")
    choice=int(input("Enter your choice: "))
    match choice :
        case 1:
            if os.path.exists(filename):
                with open(filename,"r") as f:
                    content=f.readlines()
                    if content:
                        display_content()
                    else:
                        print("The file is empty")
            else:
                with open(filename,'w'):
                    print("File doesn't exist\nThe File is created")
        case 2: 
            with open(filename,'a') as f:
                no_of_video=int(input("How many video you want to enter:"))
                for i in range(no_of_video):
                    video_title=input("Enter the Title of the video:").strip()
                    video_url=f"www.youtube.com//{video_title}".strip()
                    f.writelines(f" Title: {video_title} URL: {video_url}\n")   
        case 3:
            with open(filename,"r") as f:
                content=f.readlines()
                display_content()
                n=int(input("Enter the index of video you want to update:"))
                updated_video_name=input("Enter the video name: ").strip()
                updated_video_url=f"www.youtube.com//{updated_video_name}".strip()
                i=len(content)
                if n<=i:
                    content[n-1]=f"Title: {updated_video_name} URL: {updated_video_url}\n"
                    with open(filename,'w') as f:
                        f.writelines(content)
                    print("Video Updated successfully")
                else:
                    print("Invalid Number choice")
        case 4:
            with open(filename,"r") as f:
                content=f.readlines()
                display_content()
                n=int(input("Enter the no. of video you want to delete: "))
                i=len(content)
                if n<=i:
                    del content[n-1]
                    print("Deletion Successfull")
                    with open(filename,"w") as f:
                      f.writelines(content)
                else:
                    print("Invalid number choice")
        case 5:
            print("Exiting from Youtube.........")
            break
        case __: 
            print("Invalid Choice.\n Exiting.......")
            break
                
                        
