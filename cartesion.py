def cart(li):
    #In case an empty list is provided
    #eg : cart([])
    if len(li) == 0:
        return [()]
    stack = []
    if len(li) == 1:
        return [[each] for each in li[0]]
    else:
        for each in li[0]:
            results = cart(li[1:])
            for each_result in results:
                each_result.insert(0, each)
                stack.append(each_result)
        return stack

result = cart([['title1', 'title2'], ['body1', 'body2', 'body3'], ['url1', 'url2', 'url3']])
for combination in result:
    print combination
