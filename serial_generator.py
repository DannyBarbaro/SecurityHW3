import sys
# Shifu = 17715
# Yujie = 17866
# Yiming = 17793
def generate_serial(username):
    s = 0
    for i in username:
        s += ord(i)
    return s ^ 0x5678 ^ 0x1234

if __name__ == '__main__':
    print("Serial:", generate_serial(sys.argv[1].upper()))