class Solution:
    def threeSum(self, nums): # -> list[list[int]]:
        sorted_numbers = list(sorted(nums))
        current_index = 0
        answer_list = []

        print('sorted_nums are: ', sorted_numbers)

        for x in sorted_numbers:
            pointer_1 = 0
            pointer_2 = len(sorted_numbers) - 1

            while pointer_1 < pointer_2:
                print('x is: ', x, ' pointer_1 is: ', pointer_1, ' pointer_2 is: ', pointer_2)
                print('pointer_1 val is: ', sorted_numbers[pointer_1], ' pointer_2 val is: ', sorted_numbers[pointer_2])

                if (x + sorted_numbers[pointer_1] + sorted_numbers[pointer_2]) > 0 and pointer_2 > pointer_1:
                    pointer_2 -= 1
                elif pointer_2 == current_index:
                    pointer_2 -= 1
                elif pointer_1 == current_index:
                    pointer_1 += 1
                elif (x + sorted_numbers[pointer_1] + sorted_numbers[pointer_2]) < 0 and pointer_1 < pointer_2:
                    pointer_1 += 1

                elif (x + sorted_numbers[pointer_1] + sorted_numbers[pointer_2]) == 0:

                    sorted_answer = sorted([x, sorted_numbers[pointer_1], sorted_numbers[pointer_2]])

                    if sorted_answer not in answer_list:
                        answer_list.append(sorted_answer)
                        print('x is: ', x, sorted_numbers[pointer_1], sorted_numbers[pointer_2])

                    pointer_1 += 1

                else:
                    pass

            current_index += 1

        return answer_list

test = Solution()
print('hi: ', test.threeSum(nums=[-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))

# -2, -1, 1, 2