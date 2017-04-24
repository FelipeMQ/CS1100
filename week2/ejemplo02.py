import sys, dis

def inf():
    for i in range(1,sys.maxsize):
        print(sys.maxsize)

inf()
#dis.dis(inf)