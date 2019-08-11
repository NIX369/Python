# To obtain square of all values in a new array

nums=[1,2,3,4,5,6,7,8,9,10]
# Normal way
#square_nums = [ ]
#for num in nums:
#    square_nums.append(num**2)
#print(square_nums)

# Comprehension method
# square_nums = [num**2 for num in nums]
# print(square_nums)

#To print even square numbers

square_nums = [ ]
for num in nums:
    if(num**2)%2 == 0:
        square_nums.append(num**2)
print(square_nums)

#Comprehension Method

square_nums = [num**2 for num in nums if (num**2)%2==0]
print(square_nums)