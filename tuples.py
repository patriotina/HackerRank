__author__ = 'patriot'

N = int(raw_input())
a = raw_input()
T = tuple(map(int, a.split(" ")))
print hash(T)