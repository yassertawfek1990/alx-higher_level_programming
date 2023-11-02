#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    c = 0
    for i in range(len(sys.argv) - 1):
        c = c + int(sys.argv[i + 1])
    print(c)
