def test_par(x):
    x[1]=100
    print("in test_par func:", x[1], ", id為", id(x))
    return

x=[1,2,3]
test_par(x)
print("in main:", x[1], ", id為", id(x))

def test_par2(x):
    x=[100,200,300]
    print("in test_par2 func:", x[1], ", id為", id(x))
    return

x=[1,2,3]
test_par2(x)
print("in main:", x[1], ", id為", id(x))


