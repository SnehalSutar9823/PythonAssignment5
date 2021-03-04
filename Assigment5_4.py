def AdditionOfDigits(no,ans):
    print(no)
    if no>0:
        num=no%10
        #print(num)
        #print(no/10)
        ans=ans+num
        no=no//10
        AdditionOfDigits(no,ans)
    else:
        print(ans)

def main():
    number=int(input("Enter number"))
    ans=0
    AdditionOfDigits(number,ans)

if __name__=="__main__":
    main()
