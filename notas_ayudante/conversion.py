#!/usr/bin/env python
# coding: utf-8

# # Conversión
# 
# Módulo que realiza converisiones entre representaciones en base $\beta\leq10$ de numeros enteros no negativos. Los métodos definidos en el módulo son los siguiente
# 
# * **bin2dec** - Conversión binario a decimal
# * **dec2bin** - Conversión decimal a binario
# 

# ## Conversión de binario a decimal
# 
# La función *bin2dec* convierte un número entero no negativo en su representación binaria a su correspondiente representación decimal
# 
# ### Variables de entrada
# 
# * **bin** - *str*. Número entero no negativo en representación binaria del cual queremos obtener su representación decimal.
# 
# ### Variables de salida
# 
# * **d** - *int*. Número entero no negativo del cual queremos obtener su representación binaria.
# 
# ### Datos
# * *Autor*: Jorge Zavaleta
# * *Fecha de creacion*: 12/03/2021
# * *Ultima modificación*: 12/03/2021

# In[ ]:


def bin2dec(bin):
    d,p = 0,len(bin)-1
    for i in bin:
        d += int(i)*2**p
        p -=1
    return d


# ## Conversión de decimal a binario
# 
# La función *dec2bin* convierte un número entero no negativo en su representación decimal a su correspondiente representación binaria
# 
# ### Variables de entrada
# 
# * **dec** - *int*. Número entero no negativo del cual queremos obtener su representación binaria.
# 
# ### Variables de salida
# 
# * **bin** - *str*. Representación binaria de *dec*
# 
# ### Datos
# 
# * *Autor*: Jorge Zavaleta
# * *Fecha de creacion*: 12/03/2021
# * *Ultima modificación*: 12/03/2021

# In[ ]:


def dec2bin(dec):
    bin = ""
    if dec <= 0:
        return "0"
    else:
        while dec > 0:
            bin = str(dec%2) + bin
            dec //= 2
        return bin

