
strs='bbcabcdab abcdabcdabde'

def origin(substr):
    m=len(strs)
    n=len(substr)

    for i in range(m-n+1):
        if substr==strs[i:i+n]:
            return True

    return False

result=origin('bbcabcdab abcdabcdabd')
print(result)

def kmp():
    pass


