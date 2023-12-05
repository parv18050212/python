# x = "hello "
# y = 5
# try:
#     z = x + y 
# except:
#     print("Error Ocurred")

def func(a):
    if a < 4:
        b = a/a-3
    print("Abcd")

try:
    func(5)
except ZeroDivisionError:
    print("Error 1")
except TypeError:
    print("Error 2")

finally:
    print("ye to chlega hii")