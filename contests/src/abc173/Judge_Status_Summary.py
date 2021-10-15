n = int(input())
s = [str(input()) for i in range(n)]
print("AC x ",  s.count("AC"), sep="")
print("WA x ",  s.count("WA"), sep="")
print("TLE x ",  s.count("TLE"), sep="")
print("RE x ",  s.count("RE"), sep="")
