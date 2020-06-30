# python3
import sys


def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  result = []
    suffixes = []

    for i in range(len(text)):
        suffixes.append((i, text[i:]))

    suffixes = sorted(suffixes, key=lambda t: t[1])

    for i in range(len(suffixes)):
        result.append(suffixes[i][0])

    return result



if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
