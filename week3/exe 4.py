class rectangle :
    def __init__(self,width , height):
        self.width = width
        self.height = height

rec = rectangle(70,50)
# area = rectangle.width * rectangle.height why we dont use like this
area = rec.width*rec.height
print(area)