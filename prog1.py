cs_dept = {1001,1002,1005,1008,1010}
is_dept = {1010,1002,1005,1015,1020}
ec_dept = {1002,1005,1015,1010,1003}
res=[]

for i in cs_dept:
   if i in is_dept:
       if i in ec_dept:
           res.append(i)
print("faculty members who are working for all the departments" ,res)   


sum=[]

for i in cs_dept:
   if i not in sum:
            sum.append(i)
            
for j in is_dept:
     if j not in sum:
        if j not in ec_dept:
             sum.append(j)
          
for k in ec_dept:
    if k not in sum:
              sum.append(k)
    
print(len(sum))

employee=[]

for i in cs_dept:
    if i not in ec_dept:
        employee.append(i)
for j in is_dept:
    if j not in ec_dept:
        if j not in employee:
            employee.append(j)
print(employee)