def permutation(li, r):
    stack = []
    if r==1:
        stack = [[each] for each in li]
        return stack
    if r:
        r = r-1
    if len(li)==1:
        return [li]
    else:
        for i, each in enumerate(li):
            left_list = li[:i]
            right_list = li[i+1:]
            left_list = left_list + right_list
            result = [e for e in permutation(left_list, r)]
            for res in result:
                res.insert(0, each)
                stack.append(res)
        return stack

def permutation_helper(li, r=None):
    if r and r>len(li):
        print("You can't arrange %d elements out of %d elements." % (r, len(li)))
        return
    else:
        return permutation(li, r)

result = permutation_helper(['a', 'b', 'c', 'd', 'e'], 3)
if result:
    print len(result)
    print result
