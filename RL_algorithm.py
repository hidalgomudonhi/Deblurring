#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np


# In[3]:


# The code below implements RL algorithm for one dimensional problem.
# The code took the following inputs:
# n : measurement (i,e., f), matrix is transf. matrix (TF);
# N_it, number of sample(:N_it=1 for the smooth n)
# M_t number of iteration, I11 and I22 regularization parameters
# mM,nN are the dimenion of the TF
#

def recover(n,matrix,N_it,M_it,I11,I22,mM,nN):#(X1,n,matrix,N_it,M_it,I11,I22,Alsigm,Aa,mM,nN):
    FF=[]
    rat=[]
    column2=matrix
    for j in range(N_it):
        Nn=1*np.ones(mM)#np.random.uniform(0,1,1000)
        NN=n#np.array([np.random.normal(n[k],0.0*abs(n[k])) for k in range(len(n))])#np.array([np.random.poisson(nn) for nn in n])
        s=0.01*np.ones(50)
        C=1
        I=1
        u=np.ones(mM)#np.array([-1 if NN[i]<0 else 1 for i in range(mM)]) #
    #np.array([1 if Ez[i]<=40 else np.random.uniform(0,1) for i in range(len(NN))])
        U=np.array([1+0*i  for i in range(len(NN))])#
        M=M_it
        Ec=1
        #print(U)
        for i in range(M):
            #if i<=1200:
            Ec=Ec*np.matmul(column2,Nn)/Ec
            Nr=(NN/Ec)#np.array([(NN/Ec)[i]*(-1) if (NN/Ec)[i]<0 else (NN/Ec)[i] for i in range(len(NN/Ec))]) 
            C=C*(1-s)/C
            C=C*(1-s)/C
            Nnor=np.matmul(U,column2)
            #print(Nnor)
            Nn=(np.matmul( U*Nr,column2/Nnor))*Nn
            I3=1
            YY=[]
            h=0
            while(h+1<len(Nn)):
                if Nn[h]<Nn[h-1] and Nn[h]<Nn[h+1]:
                    YY.append(Nn[h]*I22[h])

                elif Nn[h]>Nn[h-1] and Nn[h]>Nn[h+1]:
                    YY.append(Nn[h]*I11[h])

                else:
                    YY.append(Nn[h]*I3)

                h=h+1
            if Nn[-1]<YY[-1]:
                Nn=np.array(YY+[Nn[-1]])
            else:
                Nn=np.array(YY+[Nn[-1]*I11[-1]])
            #print(Nr)
                
        FF.append(Nn)
        rat.append(np.matmul(column2,Nn))
    return FF


# In[4]:


# nu=0.015 # set to zero for no-noisy case
# Sigm1=(1+nu*np.ones(len(n)))
# Sigm2=(1-n*np.ones(len(n)))
# I11=1/Sigm1
# I22=1/Sigm2
# # def recover returns restored function F


# In[ ]:




