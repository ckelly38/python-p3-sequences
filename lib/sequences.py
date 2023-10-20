#!/usr/bin/env python3

def isnum(myvar):
    if (myvar == None): return False;
    else: return (type(myvar) == int or type(myvar) == float);

myfibcache = [];
def fibnum(index):
    #print(f"index = {index}");
    if (isnum(index)): pass;
    else: raise Exception("index must be defined and a number, but it was not a number!");
    if (index == 0): return 0;
    elif (index == 1 or index == 2): return 1;
    elif (index < 0): return -1 * fibnum(index * -1);
    else: pass;
    global myfibcache;
    #print(f"OLD fibcache = {myfibcache}");
    #check to see if it is on the cache...
    maxindexvaloncache = -1;
    maxindexvalcachei = -1;
    if (len(myfibcache) < 1):
        myfibcache.append((0, 0));
        myfibcache.append((1, 1));
        myfibcache.append((2, 1));
        #print(f"NEW fibcache = {myfibcache}");
    else: pass;

    if (len(myfibcache) < 1):
        raise Exception("there must be at least 3 values on the cache now!");
    else:
        #search the cache for the index and return result if present...
        #the cache will be a list/array of tuples...
        for i in range(len(myfibcache)):
            if (maxindexvaloncache < myfibcache[i][0]):
                maxindexvaloncache = myfibcache[i][0];
                maxindexvalcachei = i;
            else: pass;
            if (myfibcache[i][0] == index): return myfibcache[i][1];
            else: pass;
    #print("index is not on the cache...!");
    #print(f"maxindexvaloncache = {maxindexvaloncache}");
    #print(f"maxindexvalcachei = {maxindexvalcachei}");
    if (maxindexvalcachei < 0 or maxindexvalcachei > len(myfibcache) - 1):
        raise Exception("the index maxindexvalcachei on the cache was wrong!");
    else: pass;
    #we start with the maximum cached index result on the cache
    #we have its result on the cache
    #depending what the previous index is, we may also have that on the cache
    #fibonacci[n] = fibonacci[n - 1] + fibonacci[n - 2];
    #move from index backwards...
    #get fibonacci[index - 1] and fibonacci[index - 2];
    #cache them, then return what we want...
    valb = fibnum(index - 2);
    #print(f"FINAL index = {index}");
    #print(f"FINAL valb = {valb}");
    addit = True;
    for i in range(len(myfibcache)):
        if (myfibcache[i][0] == (index - 2)):
            if (myfibcache[i][1] == valb):
                addit = False;
                break;
            else: raise Exception("valb must be on the cache because its index was, but it was not!");
        else: pass;
    if (addit):
        myfibcache.append((index - 2, valb));
        #print(f"ADDED valb ({valb}) TO THE CACHE!");
    #print(f"NEW fibcache = {myfibcache}");
    #print("NOW NEED TO GET vala!");
    vala = fibnum(index - 1);
    #print(f"FINAL index = {index}");
    #print(f"FINAL vala = {vala}");
    #print(f"FINAL valb = {valb}");
    addit = True;
    for i in range(len(myfibcache)):
        if (myfibcache[i][0] == (index - 1)):
            if (myfibcache[i][1] == vala):
                addit = False;
                break;
            else: raise Exception("vala must be on the cache because its index was, but it was not!");
        else: pass;
    if (addit):
        myfibcache.append((index - 1, vala));
        #print(f"ADDED vala ({vala}) TO THE CACHE!");
    #print(f"NEW fibcache = {myfibcache}");
    
    addit = True;
    for i in range(len(myfibcache)):
        if (myfibcache[i][0] == index):
            if (myfibcache[i][1] == (vala + valb)):
                addit = False;
                break;
            else: raise Exception("vala must be on the cache because its index was, but it was not!");
        else: pass;
    if (addit):
        myfibcache.append((index, vala + valb));
        #print(f"ADDED vala + valb ({(vala + valb)}) TO THE CACHE!");
    #print(f"FINAL fibcache = {myfibcache}");
    return vala + valb;

def print_fibonacci(length):
    if (isnum(length)): pass;
    else: raise Exception("length must be defined and a number, but it was not a number!");
    if (length < 0): raise Exception("length must be defined, a number, positive or zero!");
    elif (length == 0):
        print("[]");
        return [];
    elif (length == 1):
        print("[0]");
        return [0];
    else: pass;
    #fibonacci takes the previous number and the number before that and adds it together.
    #n = length - 1 as an index that that starts at 0 and goes to length
    #fibonacci[n] = fibonacci[n - 1] + fibonacci[n - 2];
    #fibonacci[0] = 0 and fibonacci[1] = 1;
    #fibonacci[n < 0] not defined. Though one may comfortably define it as being -1*fibonacci[-1*n];
    myresarr = [];
    for i in range(length):
        #print(f"i = {i}");
        myresarr.append(fibnum(i));
    #print(f"myresarr = {myresarr}");
    print(myresarr);
    return myresarr;

#print(fibnum(-2));#-1
#print(fibnum(-3));#-2
#print_fibonacci(0);#[0]
#print_fibonacci(1);#[0]
#print_fibonacci(2);#[0, 1]
#print_fibonacci(3);#[0, 1, 1]
#print_fibonacci(9);#[0, 1, 1, 2, 3, 5, 8, 13, 21]
