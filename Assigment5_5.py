def Factorial(no,ans):
    #print(no)
    if no>0:
        
        ans=ans*no
        no=no-1
        Factorial(no,ans)
    else:
        print(ans)

def main():
    number=int(input("Enter number"))
    ans=1
    Factorial(number,ans)

if __name__=="__main__":
    main()
