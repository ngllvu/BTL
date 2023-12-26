import random


def count_digits_at_wrong_position(nums, n):
    count = 0
    for i in range(len(nums)):
        if n[i] in nums and n[i] != nums[i]:
            count += 1

    return count


def count_digits_at_right_position(nums, n):
    count = 0
    for i in range(len(nums)):
        if n[i] == nums[i]:
            count += 1

    return count


nums = random.randrange(1000, 10000)  # generate a random number

n = int(input("Enter a number : "))

if n == nums:

    print("Excellent ! You won in the first try !")

else:

    tried = 0

    while (n != nums):

        count = 0

        tried += 1

        n = str(n)

        nums = str(nums)

        result = []

        for i in range(0, 4):

            if n[i] == nums[i]:

                count += 1

                result.append(n[i])

            else:

                continue

        if count < 4 and count != 0:

            correct_position = count_digits_at_right_position(nums, n)
            wrong_position = count_digits_at_wrong_position(nums, n)

            # Display results
            print("Correct number - Correct position :", correct_position)
            print("Correct number - Wrong position :", wrong_position)

            # print(count,"Correct number\n",correct_position,"Correct position\n",wrong_position,"Wrong position")

            n = int(input("Enter a number : "))

        elif count == 0:

            print("None of number match the result . Try again")

            n = int(input("Enter a number : "))

    if n == nums:
        print("Congratulations! You got the correct number !")

        print("You've tried", tried, "times to win")