import math
import time

def my4(n, m):
    time.sleep(m/1000)
    print(f'Square root of {n} after {m} miliseconds {math.sqrt(n)}')
    
my4(25100, 2123)