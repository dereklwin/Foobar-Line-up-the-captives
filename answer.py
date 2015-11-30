#Memoize decorator to improve runtime of stirling and combination functions
def memoize(f):
    memo={}
    def helper(*args):
        if args not in memo:
            memo[args] = f(*args)
        return memo[args]
    return helper
    
@memoize
def stirling(m,n):
    if n==0 and m==0:
        return 1
    if m==0:
        return 0
    if m>n:
        return 0
    return (n-1)*sterling(m, n-1)+sterling(m-1,n-1)

@memoize
def combination(n,r):
    if r>n:
        return 0
    else:
        if r==0 or r==n:
            return 1
        else:
            return combination(n-1,r-1)+combination(n-1,r)

def answer(x,y,n):
    # Using stirling(x,n), we get all possible combinations guard x can see 
    # with n prisoners. using sterling(1-n,n), we get all possible ways to arrange rabbits given
    # n rabbits and guard x sees 1 prisoner while guard y sees 1-n prisoners. 
    return stirling(x+y-2, n-1)*combination(x+y-2,x-1)

print sterling(3,4)

