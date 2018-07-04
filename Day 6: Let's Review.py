def splitter(x):
    for element in x:
        print str(element[0::2]) + " " + str(element[1::2])
    
if __name__ == "__main__":
    n = input()
    for i in range(1,n+1):
        x = raw_input().split("\n")
        splitter(x)
