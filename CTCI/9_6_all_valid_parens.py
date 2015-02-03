def generate_parens(n):
    if n == 0:
        return ''
    res = []
    dfs(n, 0, '', res)
    return res

def dfs(left, right, buf, res):
    if left == 0:
        buf += right * ')'
        res.append(buf)
        return
    else:
        dfs(left-1, right+1, buf+'(', res)
        if right > 0:
            dfs(left, right-1, buf+')', res)


if __name__ == '__main__':
    print generate_parens(2)