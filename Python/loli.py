def twoSum(nums, target):

  for first_number in nums:
    for second_number in nums:
      if first_number == second_number:
        print("Cant pair up")
      else:
        if(first_number + second_number) == target:
          print(f"{first_number.index},{second_number.index}")
        else:
          print("Invalid")


nums = [1,2,3,4,5,6,7,8]
twoSum(nums, 9)