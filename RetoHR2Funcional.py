from functools import reduce
def minmax(arr):
    #python3.8

    print(reduce(lambda a,b:a+b,sorted(arr)[0:4]),reduce(lambda x,y:x+y, sorted(arr)[1:])) if len(arr)>=1 and len(arr)<=10**9 else None 

minmax([7,2,69,221,8974])
