import sys

input = lambda:sys.stdin.readline().rstrip("\r\n")

def I(): return input()
def II(): return int(input())
def MII(): return map(int, input().split())
def LI(): return list(input().split())
def LII(): return list(map(int, input().split()))

inf = float("inf")
mod = 10 ** 9 + 7
# for _ in range(II()):
