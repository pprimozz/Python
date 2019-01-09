
a=5
b=0

try:
    print("resource open")
    print(a/b)
except Exception as e:
    print("Error",e)
except ValueError as e:             #Optional
    print("Invalid Input")
finally:
    print("resource closed")

