
def accountsMerge(accounts):
    index = {}
    index_vals = {}
    i_index = 0
    for i in accounts:
        if i[0] not in index:
            i_index += 1
            index[i[0]] = {i_index}
            index_vals[i_index] = set(i[1:])
        else:
            found = False
            index_found = 0
            for j in index[i[0]]:
                for k in i[1:]:
                    if k in index_vals[j]:
                        found = True
                        index_found = j
                        break
            if found:
                index_vals[index_found] = index_vals[index_found] | set(i[1:])
            else:
                i_index += 1
                index_vals[i_index] = set(i[1:])
                index[i[0]] = index[i[0]] | {i_index}
    res = []
    for i in index:
        for j in index[i]:
            vals = sorted(list(index_vals[j]))
            # print(vals)
            vals = [i] + vals
            res.append(vals)
    return res

print(accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))