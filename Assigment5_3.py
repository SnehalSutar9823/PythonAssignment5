def PrintStar(no):
    
    if no>0:
        print(no,end=" ")
        no=no-1
        
        PrintStar(no)

def main():
    number=int(input("Enter how many times * should be displayed"))
    PrintStar(number)

if __name__=="__main__":
    main()
