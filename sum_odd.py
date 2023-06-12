#A four-digit integer is given. Find the sum of odd digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var_int=4931
#Create a variable "sum_odd" and assign it 0.
sum_odd=0
#Find the sum of the odd digits in the variable "var_int".
d1=var_int%10
var_int=var_int//10

d2=var_int%10
var_int=var_int//10

d3=var_int%10
var_int=var_int//10

d4=var_int%10
var_int=var_int//10

sum_odd=d1%2*d1+d2%2*d2+d3%2*d3+d4%2*d4
print(sum_odd)
