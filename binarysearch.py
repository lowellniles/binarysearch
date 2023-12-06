def binary_search(my_list, low, high, target):
   if high >= low:
      mid = (high + low) // 2
      if my_list[mid] == target:
         return mid
      elif my_list[mid] > target:
         return binary_search(my_list, low, mid - 1, target)
      else:
         return binary_search(my_list, mid + 1, high, target)
   else:
      return -1
     
my_list = [ 1, 9, 11, 21, 34, 54, 67, 90 ]
target_to_search = 13
print("The list is", end=' ')
print(my_list)
print("The target is", end=' ')
print(target_to_search)

my_result = binary_search(my_list,0,len(my_list)-1,target_to_search)

if my_result != -1:
   print("Target found at index ", str(my_result))
else:
   print("Target not found!")
