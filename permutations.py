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

def permutation_helper(li, r=None):
    if r and r>len(li):
        print("You can't arrange %d elements out of %d elements." % (r, len(li)))
        return
    else:
        return permutation(li)

result = permutation_helper(['a', 'b', 'c', 'd'], 5)
if result:
    print len(result)
    print result
