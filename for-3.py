numbers = [1,2,3,4,5,6,7,8,9]
odd_count=0
even_count=0
for a in numbers:
        if a % 2:
            odd_count+=1
        else:
             even_count+=1
print("total even numbers is:",even_count)
print("total odd numbers is:",odd_count)