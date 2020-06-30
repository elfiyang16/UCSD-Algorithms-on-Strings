# python3
import sys

def BWT(text):
	strings = []
	for i in range(len(text)):
		strings.append(text)
		text = text[-1] + text[:-1]
	strings.sort()
	return ''.join([s[-1] for s in strings])

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))