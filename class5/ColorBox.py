from Box import Box
class ColorBox(Box):
    def __init__(self,ppp):
        self.ppp=ppp
def main():
    cb = ColorBox('red')
    print(cb)

if __name__ == '__main__':
    main()