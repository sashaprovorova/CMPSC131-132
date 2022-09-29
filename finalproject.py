#part 1
def palindrome(num1):
    
    num1=int(num1)
    ispalindrome=False
    reverse=0
    temp=num1
    
    while num1>0:
        digit=num1%10
        reverse=reverse*10+digit
        num1=num1//10
        
    if(temp==reverse):
        ispalindrome=True
        
    return(ispalindrome)

#part 2
def nearprime(num2):
    
    num2=int(num2)
    isnearprime=False
    temp=0
    
    for k in range (2, num2):
        if num2%k==0:
            temp+=1
            
    if temp==1 or temp==0 or temp==2:
        isnearprime=True

    return(isnearprime)

#part 3
def nicenum(num3):
    
    num3=int(num3)
    isnicenum=False
    previous=0
    down=0
    up=0
    upinupdown=0
    downinupdown=0
    countnum=0
    lst=[]
    
    while num3>0:
        digit=num3%10
        countnum+=1
        if num3//10!=0:
            previous=(num3%100)//10
        elif num3//10==0:
            previous=digit

        if digit >= previous:
            up+=1
            if digit != previous:
                lst.append(1)
        if digit <= previous:
            down+=1
            if digit != previous:
                lst.append(0)    
        num3=num3//10
    
    for j in range (1,len(lst)):
        if lst[j] > lst[j-1]:
            upinupdown+=1
        if lst[j] < lst[j-1]:
            downinupdown+=1      
    
    if up==countnum or down==countnum or (downinupdown==0 and upinupdown!=0):
        isnicenum=True
            
    return(isnicenum)

#part 4

def main():

    givenlst=[]
    score=0
    print("Please enter a numeber (type " " to stop): ", end="")
    for i in range (1000):
        e=input()
        givenlst.append(e)
        if givenlst[i]=="":
            givenlst.pop()
            break

    scorelst=[]
    
    for k in range (len(givenlst)):
        score=int(givenlst[k])
        result1=palindrome(givenlst[k])

        if result1:
            score=score*2
        result2=nearprime(givenlst[k])

        if result2:
            score=score*2
        result3=nicenum(givenlst[k])
  
        if result3:
            score=score*3
            
        scorelst.append(score)   
    
    finallst=[]
    finallst=givenlst+scorelst

    finallst2=finallst.copy()
    finallst2[len(givenlst):len(finallst)]=sorted(finallst[len(givenlst):len(finallst)])

    for s in range (len(finallst)//2, len(finallst)):
        
        indexwas=finallst.index(finallst[s])
        indexnow=finallst2.index(finallst[s])
        
        newindex1=indexwas-int(len(finallst)//2)
        newindex2=indexnow-int(len(finallst)//2)

        finallst2[newindex2]=finallst[newindex1]

    print("The numbers sorted by their scores: ", end="")
    for h in range (len(finallst2)//2):
        print(finallst2[h], end=" ")
    
main()

