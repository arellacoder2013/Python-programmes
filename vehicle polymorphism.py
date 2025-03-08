class BMW:
    def print_model(self,modelname):
        self.modelname = modelname
        print("Model BMW:",self.modelname)
class Ferrari:
    def print_model(self,modelname):
         self.modelname = modelname
         print("Model Ferrari :",self.modelname)
Ferrariobj =Ferrari()
BMWobj=BMW()
Ferrariobj.print_model("F8 Spider")
BMWobj.print_model("8 Series.")