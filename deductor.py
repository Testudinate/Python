import urllib.requestconn = urllib.request.urlopen("http://localhost:3185/monitor.htm") # + req)
#print (conn.read(1000000000))
#p = ['4.0 Transitional','LABAZDC','WRUMOSB044','Guardant Net II','Dongle license limit','Loginom Studio Pro','Loginom Viewer Pro','Loginom Studio Ent','Loginom Viewer Ent','Deductor Studio Ent','XXX']p = ['Deductor Studio Ent']
p1 = u"""b'<img align="middle"src="license.gif">&nbsp;<a href="viewobject_id0000000B.htm" target="objectparams">Deductor Studio Pro ( 0 /  0)</a>'"""
p2 = u"""b'<img align="middle" src="license.gif">&nbsp;<a href="viewobject_id0000000C.htm" target="objectparams">Deductor Viewer Pro ( 0 /  0)</a>'"""
print('1')li = []a = []
for line in conn:    
 #row = row +str(line.strip())    
if str(line.strip())==p2 or str(line.strip())==p1:        
  continue    
 a.append(str(line.strip()))l = len(a)k = 0
for j in range(0,l):    
  #print(a[j])    
  for i in range(0,len(p)):        
  #print( a[j])        
  if k > 0 and a[j]!="b''"and a[j]!="b'</ol>'" and a[j]!="b'<ol>'" and a[j]!="b'</html>'" and a[j]!="b'</body>'" and a[j]!="b'</font>'":
    #print(a[j])            
    #for ii in range(0,len(l)):            
    li.append(str(a[j]))              
    #print (a[j],"_________",p[i])        
    if p[i] in a[j] and k==0:            
    #if a[j].find(p[i])!=-1:            
    li.append(str(a[j]))            
    #print('!!!!',a[j])           
    k = 1            
    break                   
print('2')
#n = len(li)#for g in range(0,n):    
#print(li[g],end='\n') 
f = open('D:\\Program Files (x86)\\BaseGroup\\Deductor\\Deductor.txt', 'a')
for index in range(0,len(li)):    print(li[index])   
#f.write(li[index]+'\n')f.close()
