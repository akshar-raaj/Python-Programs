def permutation(li):
    stack = []
    if len(li)==1:
        return [li]
    else:
        for i, each in enumerate(li):
            left_list = li[:i]
            right_list = li[i+1:]
            left_list = left_list + right_list
            result = [e for e in permutation(left_list)]
            for res in result:
                res.insert(0, each)
                stack.append(res)
        return stack

result = permutation(['a', 'b', 'c'])
print len(result)
print result
