a = int( input() )
b = int( input() ) + 1
[ print(num, end = " ") for num in range(a,b) if a<b and num%2 == 0]
