'''
for given integer array of size n, find three indexes x,y and z such that 1<=x<=y<=z<=n-1 and 
sum([1,x)) - sum([x,y)) + sum([y,z)) - sum([z, n-1))
where sum([a,b)) is sum of array values from index a to b, including a and excluding b and in case of a == b sum([a,b)) = 0

'''