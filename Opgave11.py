class Excersice11:

    _dictOfProducts = {'Apricot': 300,
                       'Dates': 400,
                       'Almond': 500}
    _Cart = []

    #For fun
    def AddProduct(self):
        xName = input("Please enter the product name: ")
        xPrice = int(input("Please enter the product price: "))
        self._dictOfProducts.update({xName: xPrice})

    def PrintDict(self):
        print(self._dictOfProducts)

    def AddToCart(self):
        x = input("Add product to cart").capitalize()
        if x in self._dictOfProducts.keys():
            self._Cart.append(x)
        else:
            print("Wrong")
        #print(self._Cart)

    def ComputePrice(self):
        for i in self._Cart:
            if i == 1:
                print("Product - Price\n" + )



    def Run(self):
        # self.AddProduct()
        # self.PrintDict()
        self.AddToCart()
        self.AddToCart()
        self.ComputePrice()
