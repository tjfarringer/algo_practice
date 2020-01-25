list_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def list_parser(list_of_nums, num_of_sublists):
    small_list = []
    combined_list = []
    small_pointer = 0

    batch_size = len(list_of_nums) // num_of_sublists

    print('len of list: ', len(list_of_nums))

    while small_pointer <= (len(list_of_nums) - 1):
        if (small_pointer + batch_size) <= len(list_of_nums):
            small_list = list_of_nums[small_pointer:small_pointer + batch_size]
            combined_list.append(small_list)
            small_pointer += (batch_size)

        else:
            for x in combined_list:
                if small_pointer <= (len(list_of_nums) - 1):
                    x.append(list_of_nums[small_pointer])
                else:
                    break
                small_pointer += 1

    return combined_list

