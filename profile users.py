import sqlite3 as bd

import random as rn


from faker import Faker

import time 

f=Faker()
num=1
start=time.time()

cx=bd.connect('file.db')
cu=cx.execute('create table if not exists users(numb integer,id integer, name text,email text,age integer)')

start1=time.time()

for i in range(1001):
    name=f.name()
    email=f.email()
    id=rn.randint(111111111,999999999)
    age=rn.randint(18,59)
    cu.execute(f'insert into users(numb,id,name,email,age) values({num},{id},"{name}","{email}",{age})')
    end=time.time()
    num+=1
    
print(f'time start {start1-start} and end time {end-start}')    
cx.commit()    
cx.close()
    
                          
                      
                      
                 
            
    
