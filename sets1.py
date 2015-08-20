__author__ = 'patriot'

def sets1():
    N = int(raw_input())
    ns = set(map(int, raw_input().split(" ")))
    M = int(raw_input())
    ms = set(map(int, raw_input().split(" ")))

    ls = list(ns.difference(ms))
    ls = ls + list(ms.difference(ns))
    ls.sort()
    for i in range(len(ls)):
        print ls[i]
    #return ls

sets1()