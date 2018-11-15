import re
import sys 


def getAddress(port):
    pattern = r'\S+'
    f = open('1.txt')
    
    while True:
        data = ''  #累加每一段
        for line in f:
            if line != '\n':
                data += line
            else:
                break
        #表示文档结束
        if not data:
            break

        PORT = re.match(pattern,data).group()

        #确认对应段
        if port == PORT:  
            pattern = r'address\s+is\s+(\S+)'
            addr = re.search(pattern,data).group(1)
            return addr 
        else:
            continue



if __name__ == "__main__":
    port = sys.argv[1]
    print(getAddress(port))