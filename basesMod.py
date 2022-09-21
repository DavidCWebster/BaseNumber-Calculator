import sys




def lengthen(list,list2):
        if len(list)>len(list2):
            diff=len(list)-len(list2)
            empt=[0]*diff
            list2[:]=empt+list2

            
        elif len(list2)>len(list):
            diff=len(list2)-len(list)
            empt=[0]*diff
            list[:]=empt+list

def clean(baseNum):


    if type(baseNum)==base:
        while baseNum.res[0]==0:
            if len(baseNum.res)==1:
                break

            baseNum.res=baseNum.res[1:]

    if type(baseNum)==list:
        while baseNum[0]==0:
            if len(baseNum)==1:
                break
            baseNum=baseNum[1:]
        return baseNum
        

def removeEdge(str):
    if len(str)<3:
        raise IndexError("small strings")
    
    return str[1:len(str)-1]






def GCD(a,b):
    if abs(a) == "0":
        return b
 
    return GCD(b % a,a)   


def LCM(x, y):
   lcm = (x*y)//GCD(x,y)
   return lcm







#################################################################################CLASS: BASE#########################



class base:
    def __init__(self,num,base):
        self.num=num
        self.base=base
        self.negative=False
        self.mant=0


        if type(num) == str:

            if num.find(".")>0:
                num=num.replace(".","")

                self.mant= len(num)-num.find(".")
                
            self.res = [int(x) for x in str(num)]

        elif type(num) == int:
            self.res= self.res = [int(x) for x in str(num)] 

        elif type(num)== list:
            self.res=num

        elif type(num)==float:
            num=str(float)
            if num.find("."):
                num=num.replace(".","")

                self.mant= len(num)-num.find(".")
            self.res = [int(x) for x in str(num)]

            
        


    def __str__(self):
        stri=""

        clean(self)

        
        
        stri+=str(self.res)


        if self.mant>0:
            stri.insert(self.mant,".")

        if self.negative==True:
            stri="-"+stri

        strbase=f' (base: {self.base})'

        stri+=strbase


        return stri

    def __len__(self):
        size=len(self.res)
        return size



    def __abs__(self):
        i=0
        stri=""

        x= base(self.res,self.base)


        clean(x)
        
        for val in x.res:
            stri+=str(val)
        
        if self.mant>0:
            str.insert(self.mant,".")


        return stri
        
    



    def __add__(self,o):
        if self.base!=o.base:
            print("Something went wrong with the bases")

        lengthen(self.res, o.res)
        lenS=len(self.res)
        sum=[0 for x in self.res]
        sum=[0]+sum

        largestMant=max(self.mant,o.mant)

        






        for i in range(lenS-1,-1,-1):
            sum[i+1]+= self.res[i]+o.res[i]
            if sum[i+1]>=self.base:
                sum[i+1]-=self.base
                sum[i]+=1
        
        summ=base(sum,self.base)
        
        return summ
        
        

    def __sub__(self,o):
        if self.base!=o.base:
            print("Something went wrong with the bases")
        lengthen(self.res,o.res)


        lenS=len(self.res)
        sum=[0 for x in self.res]
        sum=[0]+sum

        if abs(o)=="0":
            return self

        if int(abs(self))>int(abs(o)):
            for i in range(lenS-1,-1,-1):
                sum[i+1]+= self.res[i]-o.res[i]
                if sum[i+1]<0:
                    sum[i+1]+=self.base
                    sum[i]-=1
            negative=False
                

        if int(abs(self))<int(abs(o)):
            for i in range(lenS-1,-1,-1):
                
                sum[i+1]+= o.res[i]-self.res[i]
                

                if sum[i+1]<0:
                    sum[i+1]+=self.base
                    sum[i]-=1
            negative=True

                
            
        if int(abs(self))==int(abs(o)):
            return base([0],self.base)

        summ=base(sum,self.base)
        summ.negative=negative
        
        return summ


    def __mul__(self,o):
        if self.base!=o.base:
            print("Something went wrong with the bases")
        

        lenS=len(self.res)
        sum=[0 for x in self.res]
        #sum=[0]+sum

        baseSum=base(sum,self.base)

        one= base([1],self.base)

        if abs(o)=="0":
            return base([0],self.base)

        if abs(o)=="2":
            return self+self

        if abs(o)=="1":
            return self
        
        baseSum+=self+(self*(o-one))

        clean(baseSum)
        return baseSum

    
        
    

    
    def __floordiv__(self,o):
        count=base([0],self.base)
        one=base([1],self.base)
        

        baseline=base(self.res,self.base)
        baseline.negative=self.negative

        while (baseline-o).negative==False:
            

            if baseline.negative==True:
                break

            if count==999999999:
                break

            count=count+one
            baseline-=o
            
        
        return count

    def __mod__(self,o):
        x=self//o

        diff= self-(o*x)

        return diff


    


    






            
            
            




            

            
                


                


        


