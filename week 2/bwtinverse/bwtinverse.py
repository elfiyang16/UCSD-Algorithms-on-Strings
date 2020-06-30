# python3
import sys

def InverseBWT(bwt):
    front = {'A': {}, 'C': {}, 'T': {}, 'G': {}}#letter: {idx: count}
    back = {'A': {}, 'C': {}, 'T': {}, 'G': {}}# letter: {count: idx}
    bwt_sorted = sorted(bwt)

    count = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
    for idx, letter in enumerate(bwt):
        if letter == '$': continue
        front[letter][idx] = count[letter]
        count[letter] += 1

    count = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
    for idx, letter in enumerate(bwt_sorted):
        if letter == '$': continue
        back[letter][count[letter]] = idx
        count[letter] += 1

    i = 0
    output = [""] * (len(bwt)+1)
    output[-1] = '$'
    count = 2
    while bwt[i] != '$':
        letter = bwt[i]
        output[~count] = letter

        c = front[letter][i]
        i = back[letter][c]
        count += 1

    return ''.join(output)


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))