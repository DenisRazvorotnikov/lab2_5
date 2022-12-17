#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    p = tuple(map(int, input().split()))
    q = list(p)

    if len(p) > 10:
        for i in range(0, len(p)):
            q[i] = p[i] * i

        for i in range(2, 10):
            q[i] = -p[i]
    else:
        print(
        "В кортеже меньше 10 элементов",
        file=sys.stderr
        )
        exit(1)

    print(tuple(q))