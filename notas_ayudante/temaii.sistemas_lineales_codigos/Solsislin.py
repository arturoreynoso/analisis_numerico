#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Modulos
import numpy as np


# In[ ]:


# Excepciones
class sslException(Exception):
    
    def __init__(self,valor):
        self.valor = str(valor)
        
    def __str__(self):
        errores = {"0":"Las dimensiones son diferentes. La matriz debe ser cuadrada.",
                  "1":"Los elementos de la diagonal son cero. La matriz no es invertible.",
                  "2":"Los elementos de la diagonal son cero.",
                  "3":"Los elementos de la diagonal deben ser positivos."}
        if self.valor in errores:
            return f"Error {self.valor}. {errores[self.valor]}"
        else:
            return "Error no clasificado"


# ## Solvers

# In[ ]:


# Sistema triangular inferior
def STI(L,rhs):
    m,n = L.shape
    if m != n:
        raise sslException(0)
    b = rhs.copy()
    x = np.empty((n,),dtype = "float64")
    for j in range(n):
        if L[j,j] == 0:
             raise sslException(1)
        x[j] = b[j]/L[j,j]
        for i in range(j+1,n):
            b[i] = b[i] - L[i,j]*x[j]
    return x

# Sistema triangular superior
def STS(U,rhs):
    m,n = U.shape
    if m != n:
        raise sslException(0)
    b = rhs.copy()
    x = np.zeros(b.shape,dtype = "float64")
    for j in reversed(range(n)):
        if U[j,j] == 0:
            raise sslException(1)
        else:
            x[j] = b[j]/U[j,j]
            for i in range(j):
                b[i] = b[i] - U[i,j]*x[j]
    return x


# In[ ]:


# Metodo de Gauss sin pivoteo
def Gauss(M,rhs):
    A,b = M.copy(),rhs.copy()
    m,n = A.shape
    if m != n:
        raise slsException(0)
    for j in range(n-1):
        if A[j,j] == 0:
            raise slsException(2)
        for k in range(j+1,n):
            l = -A[k,j]/A[j,j]
            for i in range(j+1,n):
                A[k,i] = A[k,i] + l*A[j,i]
            b[k] = b[k] + l*b[j]
    return STS(A,b)

# Sistema tridiagonal
def triDiagluSol(d,e,f,b):
    n = d.size
    l = np.zeros((n-1,),dtype = "float64")
    u = np.array(d,copy = True,dtype = "float64")
    for j in range(1,n):
        l[j-1] = e[j-1]/u[j-1]
        u[j] = d[j] - l[j-1]*f[j-1]
    l = np.append(b[0],l)
    for j in range(1,n):
        l[j] = b[j] - l[j-1]*l[j]
    u[-1] = l[-1]/u[-1]
    for j in reversed(range(n-1)):
        u[j] = (l[j] - f[j]*u[j+1])/u[j]
    return u


# ## Factorizaciones

# In[ ]:


# Factorización LU sin pivoteo
def lu(M):    
    m,n = M.shape
    if m != n:
        raise slsException(0)
    U,L = M.copy(),np.eye(n)
    for j in range(n-1):
        if U[j,j] == 0:
            raise slsException(2)        
        for k in range(j+1,n):
            L[k,j] = U[k,j]/U[j,j]
            for i in range(j+1,n):
                U[k,i] = U[k,i] - L[k,j]*U[j,i]
        U[j+1:,j] = 0
    return L,U

# Factorización LU de sistemas tridiagonales
def triDiaglu(d,e,f):
    n = d.size
    l = np.zeros((n-1,),dtype = "float64")
    u = np.array(d,copy = True,dtype = "float64")
    for j in range(1,n):
        l[j-1] = e[j-1]/u[j-1]
        u[j] = d[j] - l[j-1]*f[j-1]
    return l,u

# Factorización de Cholesky
def chol(M):
    m,n = M.shape
    if m != n:
        raise slsException(0)
    L = np.zeros(M.shape,dtype = "float64")
    for k in range(n):
        s = 0.0
        for r in range(k):
            s += L[k,r]**2
        L[k,k] = np.sqrt(M[k,k] - s)
        for j in range(k+1,n):
            s = 0.0
            for r in range(k):
                s += L[j,r]*L[k,r]
            L[j,k] = (M[j,k] - s)/L[k,k]
    return L

