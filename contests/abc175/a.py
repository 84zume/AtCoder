s = str(input())

if(s.count("RRR") == 1):
    print(3)
elif(s.count("RR") == 1):
    print(2)
elif(s.count("R") == 1 or s.count("RSR") == 1):
    print(1)
elif(s.count("SSS") == 1):
    print(0)
