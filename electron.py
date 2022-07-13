import re
import math
import numpy as np
tokens = []
var = ''''''
def listcount(list,thing):
    count = 0
    for i in list:
        if i == thing:
            count = count + 1
    return count
def lexer(input):
    global tokens
    input = input.splitlines()
    for line in input:
        lis = []
        li = []
        num = []
        op = []
        func = re.findall('([a-z]+):',line)
        for i in func:
            lis.append({'func':i})
        valstr = re.findall('=([\w]+)=',line)
        for i in valstr:
            lis.append({'str':i})
        valnum = re.findall("!([0-9]+)!|<([0-9]+[.][0-9]+)>|@(-[0-9]+)@|[>](-[0-9]+[.][0-9]+)[<]",line)
        for i in valnum:
            if i == '':
                continue
            y = i
            for x in y:
                if x != '':
                    z = x
            num.append({'num':z})
        lis.append(num)
        operator = re.findall('[(]([+-/*])[)]',line)
        for i in operator:
            if i == '.':
                continue
            op.append({'op':i})
        expression = re.findall('[&]([+-/*][0-9]+)[&]',line)
        lis.append(op)
        for i in expression:
            lis.append({'expression':i})
        for i in lis:
            if i != []:
                li.append(i)
            else:
                pass
        tokens.append(li)
    return tokens
var = lexer(var)
def order(tk):
    orli = []
    for i in tk:
        if i[0] == {'func': 'square'} or i[0] == {'func': 'sqrt'} or i[0] == {'func': 'log'} or i[0] == {'func': 'factorial'} or i[0] == {'func': 'calc'}:
            li = []
            li.append(i[0])
            try:
                v = i[2]
                for x in range(0,len(i[1])):
                    if x == len(i[1])-1:
                        li.append(i[1][x])
                    else:
                        li.append(i[1][x])
                        li.append(i[2][x])
                orli.append(li)
            except:
                if len(i[1]) == 1:
                    orli.append([i[0],i[1][0]])
        elif i[0] == {'func':'say'}:
            try:
                for key in i[1]:
                    if key == 'str':
                        orli.append(i)
                    else:
                        print('Bad type')
                        quit()
            except:
                print('Unknown type')
                quit()
        elif i[0] == {'func':'type'}:
            orli.append(i)
        elif i[0] == {'func':'loop'}:
            orli.append(i)
        else:
            print('Bad function')
            quit()
    return orli
def translate(orde):
    for i in orde:
        if i[0] == {'func':'square'}:
            if len(i) > 2:
                ex = []
                exp = []
                for x in range(1,len(i)):
                    if x%2 != 0:
                        ex.append(i[x]['num'])
                    else:
                        ex.append(i[x]['op'])
                for y in range(0,len(ex)):
                    if x%2 != 0:
                        try:
                            v = ex[y+2]

                            if ex[y+1] == '*':
                                new = str(float(ex[y])*float(ex[y+2]))
                                ex[y] = '0'
                                ex[y+1] = '+'
                                ex[y+2] = str(new)
                            elif ex[y+1] == '/':
                                new = str(float(ex[y])/float(ex[y+2]))
                                ex[y] = 0
                                ex[y+1] = '+'
                                ex[y+2] = new
                        except:
                            pass
                        else:
                            pass
                num = 0
                if ex[1] == '+':
                    num = float(ex[0])+float(ex[2])
                if ex[1] == '-':
                    num = float(ex[0])-float(ex[2])
                for h in range(3,len(ex),2):
                    if ex[h] == '+':
                        num = num+float(ex[h+1])
                    if ex[h] == '-':
                        num = num-float(ex[h+1])
                yield num*num
            else:
                yield float(i[1]['num'])*float(i[1]['num'])
        if i[0] == {'func':'sqrt'}:
            if len(i) > 2:
                ex = []
                exp = []
                for x in range(1,len(i)):
                    if x%2 != 0:
                        ex.append(i[x]['num'])
                    else:
                        ex.append(i[x]['op'])
                for y in range(0,len(ex)):
                    if x%2 != 0:
                        try:
                            v = ex[y+2]

                            if ex[y+1] == '*':
                                new = str(float(ex[y])*float(ex[y+2]))
                                ex[y] = '0'
                                ex[y+1] = '+'
                                ex[y+2] = str(new)
                            elif ex[y+1] == '/':
                                new = str(float(ex[y])/float(ex[y+2]))
                                ex[y] = 0
                                ex[y+1] = '+'
                                ex[y+2] = new
                        except:
                            pass
                        else:
                            pass
                num = 0
                if ex[1] == '+':
                    num = float(ex[0])+float(ex[2])
                if ex[1] == '-':
                    num = float(ex[0])-float(ex[2])
                for h in range(3,len(ex),2):
                    if ex[h] == '+':
                        num = num+float(ex[h+1])
                    if ex[h] == '-':
                        num = num-float(ex[h+1])
                yield num**(1/2)
            else:
                yield float(i[1]['num'])**(1/2)
        if i[0] == {'func':'log'}:
            if len(i) > 2:
                ex = []
                exp = []
                for x in range(1,len(i)):
                    if x%2 != 0:
                        ex.append(i[x]['num'])
                    else:
                        ex.append(i[x]['op'])
                for y in range(0,len(ex)):
                    if x%2 != 0:
                        try:
                            v = ex[y+2]

                            if ex[y+1] == '*':
                                new = str(float(ex[y])*float(ex[y+2]))
                                ex[y] = '0'
                                ex[y+1] = '+'
                                ex[y+2] = str(new)
                            elif ex[y+1] == '/':
                                new = str(float(ex[y])/float(ex[y+2]))
                                ex[y] = 0
                                ex[y+1] = '+'
                                ex[y+2] = new
                        except:
                            pass
                        else:
                            pass
                num = 0
                if ex[1] == '+':
                    num = float(ex[0])+float(ex[2])
                if ex[1] == '-':
                    num = float(ex[0])-float(ex[2])
                for h in range(3,len(ex),2):
                    if ex[h] == '+':
                        num = num+float(ex[h+1])
                    if ex[h] == '-':
                        num = num-float(ex[h+1])
                yield math.log(num)
            else:
                yield math.log(int(i[1]['num']))
        if i[0] == {'func':'factorial'}:
            if len(i) > 2:
                ex = []
                exp = []
                for x in range(1,len(i)):
                    if x%2 != 0:
                        ex.append(i[x]['num'])
                    else:
                        ex.append(i[x]['op'])
                for y in range(0,len(ex)):
                    if x%2 != 0:
                        try:
                            v = ex[y+2]

                            if ex[y+1] == '*':
                                new = str(float(ex[y])*float(ex[y+2]))
                                ex[y] = '0'
                                ex[y+1] = '+'
                                ex[y+2] = str(new)
                            elif ex[y+1] == '/':
                                new = str(float(ex[y])/float(ex[y+2]))
                                ex[y] = 0
                                ex[y+1] = '+'
                                ex[y+2] = new
                        except:
                            pass
                        else:
                            pass
                num = 0
                if ex[1] == '+':
                    num = float(ex[0])+float(ex[2])
                if ex[1] == '-':
                    num = float(ex[0])-float(ex[2])
                for h in range(3,len(ex),2):
                    if ex[h] == '+':
                        num = num+float(ex[h+1])
                    if ex[h] == '-':
                        num = num-float(ex[h+1])
                yield math.factorial(num)
            else:
                yield math.factorial(float(i[1]['num']))
        if i[0] == {'func':'say'}:
            print(i[1]['str'])
        if i[0] == {'func':'calc'}:
            if len(i) > 2:
                ex = []
                exp = []
                for x in range(1,len(i)):
                    if x%2 != 0:
                        ex.append(i[x]['num'])
                    else:
                        ex.append(i[x]['op'])
                for y in range(0,len(ex)):
                    if x%2 != 0:
                        try:
                            v = ex[y+2]

                            if ex[y+1] == '*':
                                new = str(float(ex[y])*float(ex[y+2]))
                                ex[y] = '0'
                                ex[y+1] = '+'
                                ex[y+2] = str(new)
                            elif ex[y+1] == '/':
                                new = str(float(ex[y])/float(ex[y+2]))
                                ex[y] = 0
                                ex[y+1] = '+'
                                ex[y+2] = new
                        except:
                            pass
                        else:
                            pass
                num = 0
                if ex[1] == '+':
                    num = float(ex[0])+float(ex[2])
                if ex[1] == '-':
                    num = float(ex[0])-float(ex[2])
                for h in range(3,len(ex),2):
                    if ex[h] == '+':
                        num = num+float(ex[h+1])
                    if ex[h] == '-':
                        num = num-float(ex[h+1])
                yield float(num)
            else:
                yield float(i[0]['num'])
        if i[0] == {'func':'type'}:
            print(i[1])
        if i[0] == {'func':'loop'}:
            for d in range(int(i[1][0]['num']),int(i[1][1]['num'])+1,int(i[1][2]['num'])):
                num = 0
                express = i[2]['expression']
                op = express[0]
                inc = re.findall('([0-9]+)',i[2]['expression'])[0]
                if op == '*':
                    num = d*float(inc)
                if op == '/':
                    num = d/float(inc)
                if op == '+':
                    num = d+float(inc)
                if op == '-':
                    num = d-float(inc)
                print(num)
def compiled(x):
    for u in x:
        print(np.float32(u))
def transpilling(x):
    compiled(translate(order(x)))
transpilling(var)
