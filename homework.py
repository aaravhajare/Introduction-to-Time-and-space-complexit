
def fun1(n , m) :

    total = n * m 
    print("total iteration = 1 " , total)

def fun2(n , m) :
    total = 0

    for i in range(1 , n+1) :

        total += m
        print(" n iterations :" , n , total)

m = int(input("enter one number"))
n = int(input("second number"))

fun1(n,m)
fun2(m,n)