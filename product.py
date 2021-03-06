



class Product:
    name=''#this will hold the name of the Product
    pricePrev=0.0#Holds the previous pricePrev
    priceCurr=0.0#holds the current price
    link=""#this will hold the link for the Product

    def __init__(self,name,link,c,p):
        self.name=name
        self.link=link
        self.priceCurr=float(c)
        self.pricePrev=float(p)

    def setPricePrev(self,price):
        self.pricePrev=price
    def setPriceCurr(self,price):
        self.priceCurr=price
    def getPrice(self):
        return self.priceCurr


    def getPriceDrop(self):
        #this will get the price drop of the Product
        return self.pricePrev - self.priceCurr

    def getPriceDropPercentage(self):
        #this will get the price drop as a percentage
        return (self.getPriceDrop())/self.pricePrev *100
    def getName(self):
        return self.name

    def getLink(self):
        return self.link
    def __gt__(self,other):
        #This is the greater than function
        return self.getPriceDropPercentage() > other.getPriceDropPercentage()



if __name__ == '__main__':
    x = Product("Test","test.com",100,200)#Should give 50% off
    y = Product("hello","hello.com",100,201)#should give 67% offscreen
    #Now we will compare them to see if the gt method works Correctly
    print(x>y)#Seems to work perfectly!
