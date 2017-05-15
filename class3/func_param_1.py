def test_par(x):
    print("in test_par func before:", x, ", id為", id(x))
    x+=1
    print("in test_par func after:", x, ", id為", id(x))
    return

x=100
test_par(x)
print("in main:", x, ", id為", id(x))


def test_par2(x):
    print("in test_par2 func before:", x,  ", id為", id(x))
    x=x+"000"
    print("in test_par2 func after:", x,  ", id為", id(x))
    return 

x="hello"
test_par2(x)
print("in main:", x,  ", id為", id(x))