import random
import matplotlib.pyplot as plt
import numpy as np


def nrz_L(data):
    data_nrz = []
    for i in data:
        x = None
        if i == 1:
            x = 1
        else:
            x = -1
        data_nrz.append(x)
    data_nrz.append(1)
    xs = np.repeat(range(len(data_nrz)), 2)
    ys = np.repeat(data_nrz, 2)
    xs = xs[1:]
    ys = ys[:-1]
    plt.grid()
    plt.xlabel(str(data))
    plt.plot(xs, ys)
    plt.ylim(-3, 3)
    plt.xlim(0, 9)
    plt.title("NRZ-L")
    plt.show()


def nrz_I(data):
    data_nrz_i = []
    temp = True
    for i in range(len(data)):
        x = None
        if data[i] == 1 and temp == True:
            x = -1
            temp = False
        elif data[i] == 1 and temp == False:
            x = 1
            temp = True
        elif data[i] == 0 and temp == False:
            x = -1
        elif data[i] == 0 and temp == True:
            x = 1
        data_nrz_i.append(x)

    if data_nrz_i[0] == 0:
        data_nrz_i[0] = 1
    data_nrz_i.append(1)
    xs = np.repeat(range(len(data_nrz_i)), 2)
    ys = np.repeat(data_nrz_i, 2)
    xs = xs[1:]
    ys = ys[:-1]
    plt.grid()
    plt.title("NRZ-I")
    plt.xlabel(str(data))
    plt.plot(xs, ys)
    plt.ylim(-3, 3)
    plt.xlim(0, 9)
    plt.show()


def ami(data):
    data_ami = []
    temp = True
    for i in range(len(data)):
        if data[i] == 1 and temp == True:
            x = 1
            temp = False
        elif data[i] == 1 and temp == False:
            x = -1
            temp = True
        else:
            x = 0
        data_ami.append(x)

    data_ami.append(0)
    xs = np.repeat(range(len(data_ami)), 2)
    ys = np.repeat(data_ami, 2)
    xs = xs[1:]
    ys = ys[:-1]
    plt.grid()
    plt.xlabel(str(data))
    plt.plot(xs, ys)
    plt.ylim(-3, 3)
    plt.xlim(0, 9)
    plt.title("AMI")
    plt.show()


def Biphase_manchester(inp):
    inp1 = list(inp)
    li, init = [0], False
    for i in range(len(inp1)):
        if inp1[i] == 0:
            li.append(-1)
            if not init:
                li.append(-1)
                init = True
            li.append(1)
        elif inp1[i] == 1:
            li.append(1)
            li.append(-1)
    return li

def Differential_manchester(inp):
    inp1 = list(inp)
    li, lock, pre = [], False, ''
    for i in range(len(inp1)):
        if inp1[i] == 0 and not lock:
            li.append(-1)
            li.append(-1)
            li.append(1)
            lock = True
            pre = 'S'
        elif inp1[i] == 1 and not lock:
            li.append(1)
            li.append(1)
            li.append(-1)
            lock = True
            pre = 'Z'
        else:
            if inp1[i] == 0:
                if pre == 'S':
                    li.append(-1)
                    li.append(1)
                else:
                    li.append(1)
                    li.append(-1)
            else:
                if pre == 'Z':
                    pre = 'S'
                    li.append(-1)
                    li.append(1)
                else:
                    pre = 'Z'
                    li.append(1)
                    li.append(-1)
    return li


def B8ZS(data):
    prev = -1
    count = 0
    s = 1
    e = 1
    n = len(data)
    data_b8zs = [0]
    while s <= n and e <= n:
        if data[e - 1] == 0:
            data_b8zs.append(0)
            count = count + 1
            if count == 8:
                data_b8zs[s + 3] = prev
                data_b8zs[s + 4] = -prev
                data_b8zs[s + 6] = -prev
                data_b8zs[s + 7] = prev
                count = 0
                s = e + 1
        else:
            prev = -prev
            data_b8zs.append(prev)
            s = e + 1
            count = 0
        e = e + 1
    return data_b8zs


def HDB3(data):
    prev = -1
    count = 0
    f = 0
    s = 1
    e = 1
    n = len(data)
    data_hdb3 = [0]
    while s <= n and e <= n:
        if data[e - 1] == 0:
            data_hdb3.append(0)
            count = count + 1
            if count == 4:
                if f == 0:
                    data_hdb3[s] = -prev
                    data_hdb3[e] = -prev
                    prev = -prev
                    count = 0
                    s = e + 1
                else:
                    data_hdb3[e] = prev
                    f = 0
                count = 0
                s = e + 1
        else:
            prev = -prev
            if f == 0:
                f = 1
            else:
                f = 0
            data_hdb3.append(prev)
            s = e + 1
            count = 0
        e = e + 1
    return data_hdb3

def plot_b8zs(data):
    plt.grid()
    plt.title("b8zs")
    plt.plot(B8ZS(data),drawstyle='steps-pre')
    plt.show()


def plot_hdb3(data):
    plt.grid()
    plt.title("hdb3")
    plt.plot(HDB3(data), drawstyle='steps-pre')
    plt.show()

def plot_BMAN(data):
    plt.grid()
    plt.title("Biphase_Manchester")
    plt.plot(Biphase_manchester(data),drawstyle='steps-pre')
    plt.show()


def plot_DMAN(data):
    plt.grid()
    plt.title("Differential_Manchester")
    plt.plot(Differential_manchester(data),drawstyle='steps-pre')
    plt.show()



def findLongestPalindromicString(text):
    N = len(text)
    if N == 0:
        return
    N = 2*N+1
    L = [0] * N
    L[0] = 0
    L[1] = 1
    C = 1
    R = 2
    i = 0
    iMirror = 0
    maxLPSLength = 0
    maxLPSCenterPosition = 0
    start = -1
    end = -1
    diff = -1

    
    for i in range(2, N):


        iMirror = 2*C-i
        L[i] = 0
        diff = R - i

        if diff > 0:
            L[i] = min(L[iMirror], diff)
        try:
            while ((i + L[i]) < N and (i - L[i]) > 0) and \
                    (((i + L[i] + 1) % 2 == 0) or
                     (text[(i + L[i] + 1) // 2] == text[(i - L[i] - 1) // 2])):
                L[i] += 1
        except Exception as e:
            pass

        if L[i] > maxLPSLength:
            maxLPSLength = L[i]
            maxLPSCenterPosition = i

        if i + L[i] > R:
            C = i
            R = i + L[i]

    start = (maxLPSCenterPosition - maxLPSLength) // 2
    end = start + maxLPSLength - 1
    print("LPS of string is " + text + " : ", text[start:end+1])



x = int(input("Type 1 if want random or 2 if want user input: "))
if x == 1:
    dec = random.randint(0,1000)
    dec = bin(int(dec))
    bin_data = str(dec).replace('0b', '')
    print("INPUT BINARY IS: "+bin_data)
    findLongestPalindromicString(bin_data)
    data = []
    for i in range(len(bin_data)):
        data.append(int(bin_data[i]))
    print("Data in binary format: ", data)
    nrz_L(data)
    nrz_I(data)
    ami(data)
    plot_BMAN(data)
    plot_DMAN(data)
    plot_b8zs(data)
    plot_hdb3(data)

elif x==2:
    dec = input("Enter decimal data: ")
    dec = bin(int(dec))
    bin_data = str(dec).replace('0b', '')
    print(bin_data)
    findLongestPalindromicString(bin_data)
    data = []
    for i in range(len(bin_data)):
        data.append(int(bin_data[i]))
    print("Data in binary format: ", data)
    nrz_L(data)
    nrz_I(data)
    ami(data)
    plot_BMAN(data)
    plot_DMAN(data)
    plot_b8zs(data)
    plot_hdb3(data)
