class Solution:
# @param x, a float
# @param n, a integer
# @return a float
def myPow(self, x, n):
    if(n==0):
        return 1;
    elif(n==1):
        return x;
    if(n<0):
        return self.myPow(1/x,-n);
    else:
        if(n%2==0):
            return self.myPow(x*x,n/2);
        else:
            return self.myPow(x*x,(n-1)/2)*x
        


        
