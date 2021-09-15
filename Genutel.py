# -*- coding: utf-8 -*-
      
archivo = open ("telefono.txt","w") 
for x in range(45860000,45870000,1):
 archivo.write(str(x) + '\n')
print (x)
archivo.close()