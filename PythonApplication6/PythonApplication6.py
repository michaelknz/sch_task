#15
def is_pol(s):
    i=0
    j=len(s)-1
    while(i<j):
        if(s[i]!=s[j]):
            return False
        i+=1
        j-=1
    return True


A,B=map(int,input().split())
col=0
sum=0
for i in range(A,B+1):
    if(not is_pol(str(i))):
        sum+=i
        col+=1

print(sum//col,col)
