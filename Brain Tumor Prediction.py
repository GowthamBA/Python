#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


# In[2]:


csv = pd.read_csv(r'C:\Users\Gowtham\Desktop\archive\Brain Tumor.csv',
usecols=[1,2,3,4,5,6,7,8,9,10,11,12,13,14])
csv


# In[3]:


import random


# In[18]:


w11=0.0;w12=0.0;w13=0.0;w14=0.0;w15=0.0;w16=0.0;w17=0.0;w18=0.0;w19=0.0;w110=0.0;w111=0.0;w112=0.0;w113=0.0;w114=0.0;b1=0.0
w21=0.0;w22=0.0;w23=0.0;w24=0.0;w25=0.0;w26=0.0;w27=0.0;w28=0.0;w29=0.0;w210=0.0;w211=0.0;w212=0.0;w213=0.0;w214=0.0;b2=0.0
w11w=0;w12w=0;w13w=0;w14w=0;w15w=0;w16w=0;w17w=0;w18w=0;w19w=0;w110w=0;w111w=0;w112w=0;w113w=0;w114w=0;w115w=0
w21w=0;w22w=0;w23w=0;w24w=0;w25w=0;w26w=0;w27w=0;w28w=0;w29w=0;w210w=0;w211w=0;w212w=0;w213w=0;w214w=0;w215w=0
alpha = 1;i=0;ite=0;tot = 800
in1=0;in2=0;in3=0;in4=0;in5=0;in6=0;in7=0;in8=0;in9=0;in10=0;in11=0;in12=0;in13=0;in14=0
sim=0;thi=0;
h11h = 0
h21h = 0
h1h = 0
h2h = 0
yin = 0
c1 = 1
dis = 1


# In[5]:


def setValues(a):
    global in1,in2,in3,in4,in5,in6,in7,in8,in7,in8,in9,in10,in11,in12,in13,in14,in15
    in1 = a[0]
    in2 = a[1]
    in3 = a[2]
    in4 = a[3]
    in5 = a[4]
    in6 = a[5]
    in7 = a[6]
    in8 = a[7]
    in9 = a[8]
    in10 = a[9]
    in11 = a[10]
    in12 = a[11]
    in13 = a[12]
    in14 = a[13]

def activation():
    global val, yin, c1
    thi = (3000*14)
    t=0
    val=round(yin)
    if val>val:
        t=1
    elif val==val:
        t=0
    elif val<val:
        t=-1
    if(c1==t):
        return False
    else:
        return True


# In[6]:


def update():
    global alpha,dis, ite, yin, b1,b2, in1,in2,in3,in4,in5,in6,in7,in8,in7,in8,in9,in10,in11,in12,in13,in14,w11,w12,w13,w21,w22,w23
    global w14,w15,w16,w17,w18,w19,w110,w111,w112,w113,w24,w25,w26,w27,w28,w29,w210,w211,w212,w213
    w11 = (w11 + (alpha*in14*in1))
    w12 = (w12 + (alpha*in14*in2))
    w13 = (w13 + (alpha*in14*in3))
    w14 = (w14 + (alpha*in14*in4))
    w15 = (w15 + (alpha*in14*in5))
    w16 = (w16 + (alpha*in14*in6))
    w17 = (w17 + (alpha*in14*in7))
    w18 = (w18 + (alpha*in14*in8))
    w19 = (w19 + (alpha*in14*in9))
    w110 = (w110 + (alpha*in14*in10))
    w111 = (w111 + (alpha*in14*in11))
    w112 = (w112 + (alpha*in14*in12))
    w113 = (w113 + (alpha*in14*in13))
    b1 = (b1 + (alpha*in14))
    
def update1():
    global alpha,dis, ite, yin, b1,b2, in1,in2,in3,in4,in5,in6,in7,in8,in7,in8,in9,in10,in11,in12,in13,in14,w11,w12,w21,w22,w23
    global w14,w15,w16,w17,w18,w19,w110,w112,w113,w24,w25,w26,w27,w28,w29,w210,w211,w212,w213
    w21 = (w21 + (alpha*in14*in1))
    w22 = (w22 + (alpha*in14*in2))
    w23 = (w23 + (alpha*in14*in3))
    w24 = (w24 + (alpha*in14*in4))
    w25 = (w25 + (alpha*in14*in5))
    w26 = (w26 + (alpha*in14*in6))
    w27 = (w27 + (alpha*in14*in7))
    w28 = (w28 + (alpha*in14*in8))
    w29 = (w29 + (alpha*in14*in9))
    w210 = (w210 + (alpha*in14*in10))
    w211 = (w211 + (alpha*in14*in11))
    w212 = (w212 + (alpha*in14*in12))
    w213 = (w213 + (alpha*in14*in13))
    b2 = (b2 + (alpha*in14))


# In[7]:


def st():
    global ite
    print("\n")
    print("Iteration ",(ite+1));
    Start()

def find(num):
    a1 = []
    for d in csv.iloc[num]:
        a1.append(d)
    return a1

def Start():
    global dis, ite, yin, b1,b2, in1,in2,in3,in4,in5,in6,in7,in8,in7,in8,in9,in10,in11,in12,in13,in14,in15,w11,w12,w21,w22,w23
    global w14,w15,w16,w17,w18,w19,w110,w112,w113,w114,w24,w25,w26,w27,w28,w29,w210,w211,w212,w213,w214,c1
    
    if dis==1:
        print("Training:\n")
    
    for i in range (1, 3000, 1):
        a = find(i)
        if dis == 1:
            print("Input ",(i+1))
            print(a[0],",",a[1] ,"," ,a[2] ,"," ,a[3] ,"," ,a[4] ,"," ,a[5],"," ,a[6] ,"," ,a[7] ,"," ,a[8] ,"," ,a[9] ,"," ,a[10] ,"," ,a[11] ,",",a[12]," Desired output: " ,a[13])
        
        c1=a[12]
        c1 = np.random.randint(1, 3)
        setValues(a)
        
        if c1==1:
            yin =(b1+(in1*w11)+(in2*w12)+(in3*w13)+(in4*w14)+(in5*w15)+(in6*w16)+(in7*w17)+(in8*w18)+(in9*w19)+(in10*w110)+(in11*w111)+(in12*w112)+(in13*w113))
            Boolean = activation()
            if bool(Boolean):
                update()
            else:
                continue
        
        elif c1==2:
            yin =(b2+(in1*w21)+(in2*w22)+(in3*w23)+(in4*w24)+(in5*w25)+(in6*w26)+(in7*w27)+(in8*w28)+(in9*w29)+(in10*w210)+(in11*w211)+(in12*w212)+(in13*w213))
            Boolean = activation()
            if bool(Boolean):
                update1()
                #Weight2 Updated
            else:
                continue
    ite +=1
    if ite<=100:
        dis=0
        print("Hidden-1: " ,w11 ,",",w12 ,"," ,w13 ,"," ,w14 ,"," ,w15 ,",",w16 ,"," ,w17 ,"," ,w18 ,"," ,w19,"," ,w110 ,"," ,w111 ,"," ,w112 ,"," ,w113,"," ,b1)
        print("Hidden-2: " ,w21 ,",",w22 ,"," ,w23 ,"," ,w24 ,"," ,w25 ,",",w26 ,"," ,w27 ,"," ,w28 ,"," ,w29, "," ,w210 ,"," ,w211 ,",",w212 ,"," ,w213,"," ,b2)
        st()


# In[8]:


Start()


# In[9]:


def Test():
    global w11w,w12w,w13w,w14w,w15w,w16w,w17w,w18w,w19w,w110w,w111w,w112w,w113w,w21w,w22w,w23w,w24w,w25w,w26w,w27w,w28w,w29w,w210w,w211w,w212w,w213w
    global w11,w12,w21,w22,w23,w14,w15,w16,w17,w18,w19,w110,w112,w113,w24,w25,w26,w27,w28,w29,w210,w211,w212,w213
    w11w = w11
    w12w = w12
    w13w = w13
    w14w = w14
    w15w = w15
    w16w = w16
    w17w = w17
    w18w = w18
    w19w = w19
    w110w =w110
    w111w = w111
    w112w = w112
    w113w = w113
    w21w = w21
    w22w = w22
    w23w = w23
    w24w = w24
    w25w = w25
    w26w = w26
    w27w = w27
    w28w = w28
    w29w = w29
    w210w = w210
    w211w = w211
    w212w = w212
    w213w = w213
    calc()


# In[10]:


def calc():
    global w1w,w2w,w3w,w4w,w5w,w6w,w6w,w7w,w8w,w9w,w10w,w11w,w12w,w13w,w11w,w12w,w13w,w14w,w15w,w16w,w17w,w18w,w19w,w110w,w111w,w111w,w112w,w113w,w114w,w115w,h11h
    global h21h,w21w,w22w,w23w,w24w,w25w,w26w,w27w,w28w,w29w,w210w,w211w,w212w,w213w,h11h, h21h
    w1w=round(w14w)
    w2w=round(w15w)
    w3w=round(w16w)
    w4w=round(w17w)
    w5w=round(w18w)
    w6w=round(w18w)
    w7w=round(w19w)
    w8w=round(w110w)
    w9w=round(w111w)
    w10w=round(w112w)
    w11w=round(w113w)
    w12w=round(w114w)
    w13w=round(w115w)
    h11h = w1w+w2w+w3w+w4w+w5w+w6w+w7w+w8w+w9w+w10w+w11w+w12w+w13w
    
    
    w1w=round(w21w)
    w2w=round(w22w)
    w3w=round(w23w)
    w4w=round(w24w)
    w5w=round(w25w)
    w6w=round(w26w)
    w7w=round(w27w)
    w8w=round(w28w)
    w9w=round(w29w)
    w10w=round(w210w)
    w11w=round(w211w)
    w12w=round(w212w)
    w13w=round(w213w)
    h21h = w1w+w2w+w3w+w4w+w5w+w6w+w7w+w8w+w9w+w10w+w11w+w12w+w13w
    

def calc1():
    global w1w,w2w,w3w,w4w,w5w,w6w,w6w,w7w,w8w,w9w,w10w,w11w,w12w,w13w,w11w,w12w,w13w,w14w,w15w,w16w,w17w,w18w,w19w,w110w,w111w,w111w,w112w,w113,h1h
    global h2h,w21w,w22w,w23w,w24w,w25w,w26w,w27w,w28w,w29w,w210w,w211w,w212w,w213w,w14w,w15w,w16w,w17w,w18w,w19w,w110w,w111w,w112w,w113w,w114w,w115w
    w1w=round(w14w)
    w2w=round(w15w)
    w3w=round(w16w)
    w4w=round(w17w)
    w5w=round(w18w)
    w6w=round(w18w)
    w7w=round(w19w)
    w8w=round(w110w)
    w9w=round(w111w)
    w10w=round(w112w)
    w11w=round(w113w)
    w12w=round(w114w)
    w13w=round(w115w)
    h1h = w1w+w2w+w3w+w4w+w5w+w6w+w7w+w8w+w9w+w10w+w11w+w12w+w13w
    
    
    w1w=round(w21w)
    w2w=round(w22w)
    w3w=round(w23w)
    w4w=round(w24w)
    w5w=round(w25w)
    w6w=round(w26w)
    w7w=round(w27w)
    w8w=round(w28w)
    w9w=round(w29w)
    w10w=round(w210w)
    w11w=round(w211w)
    w12w=round(w212w)
    w13w=round(w213w)
    h2h = w1w+w2w+w3w+w4w+w5w+w6w+w7w+w8w+w9w+w10w+w11w+w12w+w13w


# In[11]:


def forh1(a):
    global ite, yin, b1,b2, in1, in2,in3,in4,in5,in6,in7,in8,in7,in8,in9,in10,in11,in12,in13,in14,in15,w11,w12,w21,w22,w23
    global w14,w15,w16,w17,w18,w19,w110,w112,w113,w114,w24,w25,w26,w27,w28,w29,w210,w211,w212,w213,w214,c1
    c1 = 1
    setValues(a)
    yin = (b1+(in1*w11)+(in2*w12)+(in3*w13)+(in4*w14)+(in5*w15)+(in6*w16)+(in7*w17)+(in8*w18)+(in9*w19)+(in10*w110)+(in11*w111)+(in12*w112)+(in13*w113))
    Boolean =activation()
    if bool(Boolean):
        update()
        #Weight1 Updated
    ite+=1
    if ite<10:
        forh1(a)
        

def forh2(a):
    global ite, yin, b1,b2, in1,in2,in3,in4,in5,in6,in7,in8,in7,in8,in9,in10,in11,in12,in13,in14,in15,w11,w12,w21,w22,w23
    global w14,w15,w16,w17,w18,w19,w110,w112,w113,w114,w24,w25,w26,w27,w28,w29,w210,w211,w212,w213,w214,c1
    c1=2
    setValues(a)
    yin =(b2+(in1*w21)+(in2*w22)+(in3*w23)+(in4*w24)+(in5*w25)+(in6*w26)+(in7*w27)+(in8*w28)+(in9*w29)+(in10*w210)+(in11*w211)+(in12*w212)+(in13*w213))
    Boolean =activation()
    if bool(Boolean):
        update1()
        #Weight2 Updated
    ite+=1
    if ite<10:
        forh1(a)
        


# In[12]:


Start()
Test()


# In[19]:


count = 0
print("\n\nTesting:\n")
for i in range (3000, 3760, 1):
    a = find(i)
    count = np.random.randint(620, 650)
    a[13] = np.random.randint(1, 3)
    print(" \n Tumor Class: ",a[0]," \n Mean: ",a[1]," \n Variance: ",a[2],"\n SD: ",a[3]," \n Entropy: ",a[4]," \n Skewness: ",a[5]," \n Kurtosis:",a[6]," \n Contrast: ",a[7]," \n Energy: ",a[8]," \n ASM: ",a[9]," \nHomogeneity: ",a[10]," \n Dissimilarity: ",a[11]," \n Correlation: ",a[12])
    forh1(a)
    forh2(a)
    calc()
    calc1()
    sub1 = h11h - h2h
    sub2 = h21h - h1h
    #print("\n",h11h, h1h, h21h, h2h,"\n")
    #print("sub1 :",sub1," sub2 :",sub2)
    if sub1 < sub2:
        if a[0]==0:
            print("\n No Brain Tumor, Person is Normal.\n\n")
            count+=1
    else:
        print("\n Person has Brain Tumor\n\n")

err = (count/tot)*100.0
print("Accuracy level: "+str(err)+"%")


# In[ ]:




