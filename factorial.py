class fact_gen:
    def fact(self,n):
        self.n=n
    def compute(self):
        if self.n==0:
            return 1
        else:
            return self.n* self.compute(n-1)
        
fact_5= fact_gen()
print(fact_5.compute(5))


        
    