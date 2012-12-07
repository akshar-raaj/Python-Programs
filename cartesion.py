def cartesion(new_list, prepared_list):
    created_list = []
    for each in new_list:
        for pre_each in prepared_list:
            temp = [e for e in pre_each]
            temp.insert(0, each)
            created_list.append(temp)
    return created_list

def create_cartesion(input_list):
    if len(input_list)>1:
        temp = input_list[-1]
        tt = [[each] for each in temp]
        input_list[-1] = tt
    while len(input_list)>1:
        result = cartesion(input_list.pop(-2), input_list.pop(-1))
        input_list.append(result)
    return input_list


result = create_cartesion([['title1', 'title2', 'title3'], ['body1', 'body2', 'body3'], ['url1', 'url2', 'url3']])
result = result[0]
for combination in result:
    print combination
