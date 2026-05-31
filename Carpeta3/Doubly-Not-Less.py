def doubly_not_less(n):
    def rev(s):
        return str(int(s[::-1]))
    
    def geq(a, b):
        if len(a) != len(b):
            return len(a) > len(b)
        return a >= b
    
    def increment_str(s):
        digits = list(s)
        i = len(digits) - 1
        while i >= 0:
            if digits[i] < '9':
                digits[i] = str(int(digits[i]) + 1)
                return ''.join(digits)
            digits[i] = '0'
            i -= 1
        return '1' + '0' * len(s)
    
    m = n
    for _ in range(10000):
        if geq(rev(m), n):
            return m
        if m[-1] < n[0]:
            diff = int(n[0]) - int(m[-1])
            m = str(int(m) + diff)
        elif len(m) > 10 and m[-1] >= n[0] and not geq(rev(m), n):
            digits = list(m)
            for start in range(len(m) - 2, -1, -1):
                digits[start] = '9'
                test = ''.join(digits)
                if geq(rev(test), n):
                    m = test
                    break
        else:
            m = increment_str(m)
    
    return m