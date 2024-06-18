class Watu:
#constructor

    def __init__(self, jina, miaka):
        self.jina = jina
        self.miaka= miaka

    #method
    def kuonyesha(self):
        print(self.jina, self.miaka)
    #object
my_watu= Watu(jina='George', miaka= 60)
my_watu.kuonyesha()
my_watu =Watu(jina='Christiano', miaka= 70)
my_watu.kuonyesha()
my_watu= Watu(jina='Neymar', miaka=90)
my_watu.kuonyesha()