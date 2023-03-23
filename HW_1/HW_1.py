from typing import List, Tuple
def print_hi():
    print('Hello World')
from collections import Counter


if __name__ == '__main__':
    List = [3, 3, 2, 2, 3, 3, 1]
    counter = Counter(List)
    most_common = counter.most_common(1)
    least_common = counter.most_common()[::-1]
    z = (int(most_common[0][0]),int(least_common[0][0]))
    print(z)
