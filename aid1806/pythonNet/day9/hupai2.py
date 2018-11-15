#hupai2.py




import re




def Findshunzi(str_a):

    Lg=len(str_a)

    L_flag=0

    while len(str_a)>0:

        if len(str_a)%3!=0:           

            return 0

            break

        f1=f2=f3=-1;

        for i in range(1,10):

            s1=str(i)

            s2=str(i+1)

            s3=str(i+2)

            f1=str_a.find(s1)

            f2=str_a.find(s2)

            f3=str_a.find(s3)

            if f1>-1 and f2>-1 and f3>-1:

                str_a=str_a[0:f1]+' '+str_a[f1+1:len(str_a)]

                str_a=str_a[0:f2]+' '+str_a[f2+1:len(str_a)]

                str_a=str_a[0:f3]+' '+str_a[f3+1:len(str_a)]

                str_a=str_a.replace(' ','')

                break

        if len(str_a)==0:

            return 1

        if f1==-1 or f2==-1 or f3==-1:

            return 0

            break
















def sanlian(a):

    A=[]

    Flag=0

    for i in range(1,10):

        s1=a.count(str(i))

        if s1>2:

            A.append([str(i),s1])

    len_A=len(A)

    if len_A==0:#不存在三连牌，直接转找顺子处理

        Flag=Findshunzi(a)

        return Flag




    if len_A==1:#存在一个三连牌

        if len(a)==3:

            return 1

        Flag=Findshunzi(a)#三连牌当顺子处理

        if Flag==1:#当顺子处理能胡牌

            return 1

        elif Flag==0:#三连牌当顺子处理不能胡牌，则当三连牌处理试试

            c_s=A[0][0]

            n_s=A[0][1]

            a=a.replace(c_s,'')

            if n_s==4:

                a=a+c_s

            Flag=Findshunzi(a)#三连牌当顺子处理

            return Flag

    if len_A==2:#存在2个三连对

        if len(a)==6:

            return 1

        Flag=Findshunzi(a)#全当顺子处理

        if Flag==1:

            return 1

        elif Flag==0:

            for i in range(0,2):#其中一个三连牌当顺子处理                

                c_s=A[i][0]#c_s是字符

                n_s=A[i][1]#n_s是字符c_s的个数

                a=a.replace(c_s,'')

                if n_s==4:                    

                    a=a+c_s

                Flag=Findshunzi(a)#三连牌当顺子处理

                if Flag==1:

                    return 1

                elif Flag==0:

                    a=a+c_s+c_s+c_s

            for i in range(0,2):#2个三连牌都当三连牌处理

                c_s=A[i][0]#c_s是字符

                n_s=A[i][1]#n_s是字符c_s的个数

                a=a.replace(c_s,'')

                if n_s==4:                    

                    a=a+c_s

            Flag=Findshunzi(a)

            return Flag

    if len_A==3:#存在3个三连牌

        if len(a)==9:

            return 1

        Flag=Findshunzi(a)#3个三连牌全当顺子处理

        if Flag==1:

            return 1

        for i in range(0,3):#3个三连牌其中一个当三连牌处理，其余2个当顺子处理                        

            c_s=A[i][0]#c_s是字符

            n_s=A[i][1]#n_s是字符c_s的个数

            a=a.replace(c_s,'')

            if n_s==4:                    

                    a=a+c_s

            Flag=Findshunzi(a)

            if Flag==1:

                return 1

            elif Flag==0:

                a=a+c_s+c_s+c_s

        for i in range(0,3):#3个三连牌其中2个当三连牌处理，其余1个当顺子处理

            for j in range(i+1,3):

                AB=[]

                AB.append(i)

                AB.append(j)

                for k in AB:                    

                    c_s=A[k][0]#c_s是字符

                    n_s=A[k][1]#n_s是字符c_s的个数

                    a=a.replace(c_s,'')

                    if n_s==4:                    

                        a=a+c_s

                Flag=Findshunzi(a)

                if Flag==1:

                    return 1

                elif Flag==0:                                        

                    for k in AB:                        

                        c_s=A[k][0]#c_s是字符

                        a=a+c_s+c_s+c_s

        for i in range(0,3):#3个3连牌全部当三连牌处理                        

            c_s=A[i][0]#c_s是字符

            n_s=A[i][1]#n_s是字符c_s的个数

            a=a.replace(c_s,'')

            if n_s==4:                

                a=a+c_s        

        Flag=Findshunzi(a)

        return Flag    

    if len_A==4:#存在4个三连牌

        return 1




                                            

def okduizi(a):   

    aD=re.findall('[1-9]D',a)

    aW=re.findall('[1-9]W',a)

    aT=re.findall('[1-9]T',a)    

    if len(aD)==14  or len(aW)==14 or len(aT)==14:                

        return 0

    if len(aD)>0:

        aD=re.findall('[1-9]',str(aD))       

        aD=''.join(aD)        

    if len(aW)> 0:#        

        aW=re.findall('[1-9]',str(aW))              

        aW=''.join(aW)    

    if len(aT)>0:

        aT=re.findall('[1-9]',str(aT))        

        aT=''.join(aT)

    A_D=[]

    A_W=[]

    A_T=[]

    a_S=[aD,aW,aT]

    A_S=[A_D,A_W,A_T]  

    Fnum=0

    for i in range(0,3):

        tmp=a_S[i]

        lt=len(tmp)

        for j in range(0,10):

            n1=tmp.count(str(j))

            if n1>1:

                A_S[i].append([str(j),n1])

                if n1%2==0:

                    Fnum+=n1

    if Fnum==14:#七对情况存在       

        return 1

    Flag_G=0

    A_D=A_S[0]

    A_W=A_S[1]

    A_T=A_S[2] 

    if len(A_D)>0:#用aD中牌作对子

        les=len(A_D)      

        for i in range(0,les):        

            Dui=A_D[i][0]       

            index=aD.find(Dui)

            aD=aD[0:index]+aD[index+1:len(aD)]

            index=aD.find(Dui)

            aD=aD[0:index]+aD[index+1:len(aD)]

            #已经在aD中去除一个对子

            Flag_aD=0

            Flag_aW=0

            Flag_aT=0

            if len(aD)==0:

                Flag_aD=1

            if len(aW)==0:

                Flag_aW=1

            if len(aT)==0:

                Flag_aT=1

            if len(aD)>0:               

                Flag_aD=sanlian(aD)            

            if len(aW)>0:

                Flag_aW=sanlian(aW)            

            if len(aT)>0:

                Flag_aT=sanlian(aT)

            Sn=Flag_aT+Flag_aW+Flag_aD           

            if Sn==3:

                Flag_G=1

                return 1

            elif Sn<3:

                aD=aD+Dui+Dui           

    if len(A_W)>0:#用aW中牌作对子        

        les=len(A_W)      

        for i in range(0,les):        

            Dui=A_W[i][0]       

            index=aW.find(Dui)

            aW=aW[0:index]+aW[index+1:len(aW)]

            index=aW.find(Dui)

            aW=aW[0:index]+aW[index+1:len(aW)]

            #已经在aW中去除一个对子

            Flag_aD=0

            Flag_aW=0

            Flag_aT=0

            if len(aD)==0:

                Flag_aD=1

            if len(aW)==0:

                Flag_aW=1

            if len(aT)==0:

                Flag_aT=1

            if len(aD)>0:

                Flag_aD=sanlian(aD)

            if len(aW)>0:

                Flag_aW=sanlian(aW)

            if len(aT)>0:

                Flag_aT=sanlian(aT)

            if Flag_aD+Flag_aW+Flag_aT==3:              

                Flag_G=1

                return 1

            elif (Flag_aD+Flag_aW+Flag_aT)<3:

                aW=aW+Dui+Dui




    if len(A_T)>0:#用aT中牌作对子        

        les=len(A_T)      

        for i in range(0,les):        

            Dui=A_T[i][0]       

            index=aT.find(Dui)

            aT=aT[0:index]+aT[index+1:len(aT)]

            index=aT.find(Dui)

            aT=aT[0:index]+aT[index+1:len(aT)]

            #已经在aT中去除一个对子

            Flag_aD=0

            Flag_aW=0

            Flag_aT=0

            if len(aD)==0:

                Flag_aD=1

            if len(aW)==0:

                Flag_aW=1

            if len(aT)==0:

                Flag_aT=1

            if len(aD)>0:

                Flag_aD=sanlian(aD)

            if len(aW)>0:

                Flag_aW=sanlian(aW)

            if len(aT)>0:

                Flag_aT=sanlian(aT)

            if (Flag_aD+Flag_aW+Flag_aT)==3:

                Flag_G=1

                return 1

            elif Flag_aD+Flag_aW+Flag_aT<3:

                aT=aT+Dui+Dui    

    if Flag_G==0:

        return 0

        

    




# a='2D2D1D1D2T2T2T2T5T5T5T5T6T6T'

# a='1D2D3D2T3T4T7W8W1D1D1D9W9W9W'

# a='1D1D2D2D3D3D4D4D5D5D6D6D7W7W'

# a='1T8T6W6W5D4W1T3W6W2W5D6T1T7T'

# a = '1D1D1D2D3D4D5W6W7W8W8W8W9W9W'
a=input()
f=okduizi(a)

if f==1:

    print('true')

else:

    print('false')
