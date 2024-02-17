import sys

input = lambda:sys.stdin.readline().rstrip("\r\n")

def I(): return input()
def II(): return int(input())
def MII(): return map(int, input().split())
def LI(): return list(input().split())
def LII(): return list(map(int, input().split()))
def GMI(): return map(lambda x: int(x) - 1, input().split())
def LGMI(): return list(map(lambda x: int(x) - 1, input().split()))

inf = float("inf")
mod = 10**9 + 7
# from sortedcontainers import SortedList
# for _ in range(II()):
