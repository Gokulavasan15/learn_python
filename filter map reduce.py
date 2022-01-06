from functools import reduce
num = [1,2,3,6,5,4,9,8,7]
even = list(filter(lambda n : n%2==0,  num))
print(even)
odd = list(filter(lambda n : n%2!=0, num))
print(odd)
squares = list(map(lambda n : n*n , even))
print(squares)
sum = reduce(lambda a,b :a+b ,squares)
print(sum)