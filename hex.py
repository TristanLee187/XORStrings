import sys
mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]
key = open(keyfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
inp = open(inpfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
debug = False

if(debug):
    print("mode: "+mode)
    print("key: "+key)
    print("inp: "+inp)

#YOUR CODE HERE!
pairs=[(key[i%len(key)],inp[i]) for i in range(len(inp))]

if mode=='human':
    xor=[chr(ord(a)^ord(b)) for a,b in pairs]
    print(''.join(xor))
else:
    xor = [hex(ord(a) ^ ord(b))[2:] for a, b in pairs]
    print(' '.join(xor))