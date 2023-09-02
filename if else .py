n=int(input())

if ( n%2 == 1 and 1 <= n <= 100):

    print("Weird")

elif (n%2 == 0 and 2 < n < 5):
    print("Not weird")

elif (n%2 == 0 and 6 < n < 20):
    print("Weird")

elif (n%2 == 0 and n > 20):
    print("Not Weird")
else:
    print("not valid operation")




