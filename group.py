p=int(input("enter the value of p"))
if p<100 or p>200:
    print("the number is not valid")
r=p%4
if r==0:
    q=p/4
    print(int(q,"participant of group A"))
    print(int(q,"participant of group B"))
    print(int(q,"participant of group C"))
    print(int(q,"participant of group D"))
else:
    w=p//4
    z=p-3*w
    print(w, "participant of group A")
    print(w, "participant of group B")
    print(w, "participant of group C")
    print(z, "participant of group D")




    
    
    
    
