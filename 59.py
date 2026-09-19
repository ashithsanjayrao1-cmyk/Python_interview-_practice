def common_elements(list1, list2):
    common_number = []


    for num in list1:
        if num in list2:
            common_number.append(num)

    return common_number

teama = [1,2,3,4,5]
teamb = [4,5,6,7,8]

print(common_elements(teama,teamb))