RESULTS = []
LEVEL = -1

def generate(k, N, TEMP):
    global LEVEL
    LEVEL = LEVEL + 1
    TEMP[k] = LEVEL

    if LEVEL == N:
        RESULTS.append(tuple(TEMP))
        print TEMP
    else:
        for i in xrange(N):
            if TEMP[i] == 0:
                generate(i, N, TEMP)
    LEVEL = LEVEL - 1
    TEMP[k] = 0

generate(0, 3, 3*[0])
print RESULTS