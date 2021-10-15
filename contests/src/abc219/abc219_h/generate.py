#!/usr/bin/env python3
# usage: $ oj generate-input 'python3 generate.py'
# usage: $ oj generate-input --hack-actual=./a.out --hack-expected=./naive 'python3 generate.py'
import random


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = random.randint(1, 1000)  # TODO: edit here
    X = [None for _ in range(N)]
    A = [None for _ in range(N)]
    for i in range(N):
        X[i] = random.randint(1, 10**9)  # TODO: edit here
        A[i] = random.randint(1, 10**9)  # TODO: edit here
    print(N)
    for i in range(N):
        print(X[i], A[i])


if __name__ == "__main__":
    main()
