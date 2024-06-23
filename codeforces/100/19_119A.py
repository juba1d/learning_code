import math

def main():
    a, b, n = map(int, input().split())
    
    while True:
        n -= math.gcd(a, n)
        if n <= 0:
            print(0)
            return
        
        n -= math.gcd(b, n)
        if n <= 0:
            print(1)
            return

if __name__ == "__main__":
    main()
