
import code as s
s.create("sastra",25)

s.create("src",70,3600) 

s.read("sastra")

s.read("src")

s.create("sastra",50)

s.modify("sastra",55)
 
s.delete("sastra")

t1=Thread(target=(create or read or delete),args=(key_name,value,timeout))
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout))
t2.start()
t2.sleep()
