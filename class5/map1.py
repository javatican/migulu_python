def main():
    print(__name__)
    x={'mon':"Monday", 'tue':"Tuesday", 'wed':"Wednesday",'thr':"Thursday",'fri':"Friday"}
    print(x)
    print(x['thr'])
    x['sat']='Saturday'
    x['sun']='sunday'
    print(x)
    x['sun']='Sunday'
    print(x)
    
    for a in x:
        print(a) # key
        print(x[a]) # value
    
    for k,v in x.items():
        print(k) #key
        print(v) #value
    
    for i,v in enumerate(x):
        print(i) #index
        print(v) #key
    
    print(x.keys())
    print(x.values())

if __name__ == '__main__':
    main()