def permutation(li):
    stack = []
    if len(li)==1:
        return li
    else:
        for i, each in enumerate(li):
            left_list = li[:i]
            right_list = li[i+1:]
            left_list.extend(right_list)
            result = permutation(left_list)
            for res in result:
                stack.append(each+res)
        return stack

result = permutation(['a', 'b', 'c'])
print len(result)
print result
