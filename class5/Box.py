import datetime
class Box:
    #三個資料(屬性) h, w,  d (長寬高)
    #行為(方法),calculate_volume() 計算體積, print_info（）列印資訊
    #建構子（__init__())
    
    def __init__(self, h, w, d):
        self.h = h
        self.w = w
        self.d = d
        self.volume = self.h*self.w*self.d
    def calculate_volume(self):
        return self.volume
    def print_info(self):
        print("h:",self.h,",w:",self.w,",d:",self.d,",volume:",self.volume)


def main():
    #產生Box物件
    b1 = Box(10,20,30)
    b1.h=100
    b1.print_info()
    b2 = Box(50,60,70)
    b2.print_info() 
    Box.print_info(b2)
     
if __name__ == '__main__':
    main()
    
