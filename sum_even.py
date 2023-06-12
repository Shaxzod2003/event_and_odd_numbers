#A four-digit integer is given. Find the sum of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var_int=8365
#Create a variable "sum_even" and assign it 0.
sum_even=0
#Find the sum of the even digits in the variable "var_int".
d1=var_int%10
var_int=var_int//10

d2=var_int%10
var_int=var_int//10

d3=var_int%10
var_int=var_int//10

d4=var_int%10
var_int=var_int//10
sum_even=(d1+1)%2*d1+(d2+1)%2*d2+(d3+1)%2*d3+(d4+1)%2*d4
print(sum_even)