import pickle
import json
import math,time
from multiprocessing import Process

# with open("./node_ip2cluster.pkl", "rb") as f:
#     json_content = pickle.load(f)

# with open("./node_ip2cluster.json", "w") as f:
#     json.dump(json_content, f, indent=4)

def sm_cpu():
    for i in range(10000000):
        find_primes(i)
        continue
        b = 1234568*12345678
        math.sqrt(b)
        math.log(b,9)
        
def find_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

if __name__ == "__main__":
    p_l = []
    for i in range(4):
        p = Process(target=sm_cpu)
        p_l.append(p)
        p.start()

    
    for p in p_l:
        p.join()

    