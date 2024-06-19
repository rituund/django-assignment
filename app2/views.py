from django.shortcuts import render
from app2.forms import inputform

# Create your views here.
def home(request):
    result=[]
    n1=0
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            n1=data.get("input")
            if len(n1)==3:
                result=perm3(n1)
            if len(n1)==4:
                result=perm4(n1)
            if len(n1)==5:
                result=perm5(n1)
            return render(request,"app2/index.html",{'param1':n1, 'param2':result, 'form':form1})
    else:
        form1=inputform()
    return render(request,"app2/index.html",{'param1':n1, 'param2':result, 'form':form1})
            

def perm3(s3):
    c1=s3[0:1]
    c2=s3[1:2]
    c3=s3[2:3]
    list3=[]
    list3.append(c1+c2+c3)
    list3.append(c1+c3+c2)
    list3.append(c2+c1+c3)
    list3.append(c2+c3+c1)
    list3.append(c3+c1+c2)
    list3.append(c3+c2+c1)
    return list3

def perm4(s4):
    c1=s4[0:1]
    c2=s4[1:2]
    c3=s4[2:3]
    c4=s4[3:4]
    list4=[]
    part1=c1
    part2=c2+c3+c4
    temp=perm3(part2)
    for i in range(0,len(temp),1):
        list4.append(part1+temp[i])
    part1=c2
    part2=c1+c3+c4
    temp=perm3(part2)
    for i in range(0,len(temp),1):
        list4.append(part1+temp[i])
    part1=c3
    part2=c1+c2+c4
    temp=perm3(part2)
    for i in range(0,len(temp),1):
        list4.append(part1+temp[i])
    part1=c4
    part2=c1+c2+c3
    temp=perm3(part2)
    for i in range(0,len(temp),1):
        list4.append(part1+temp[i])
    return list4


def perm5(s5):
    c1=s5[0:1]
    c2=s5[1:2]
    c3=s5[2:3]
    c4=s5[3:4]
    c5=s5[4:5]
    list5=[]
    part1=c1
    part2=c2+c3+c4+c5
    temp=perm4(part2)
    for i in range(1,16,1):
        list5.append(part1+temp[i])
    part1=c2
    part2=c1+c3+c4+c5
    temp=perm4(part2)
    for i in range(1,16,1):
        list5.append(part1+temp[i])
    part1=c3
    part2=c1+c2+c4+c5
    temp=perm4(part2)
    for i in range(1,16,1):
        list5.append(part1+temp[i])
    part1=c4
    part2=c1+c2+c3+c5
    temp=perm4(part2)
    for i in range(1,16,1):
        list5.append(part1+temp[i])
    part1=c5
    part2=c1+c2+c3+c4
    temp=perm4(part2)
    for i in range(1,16,1):
        list5.append(part1+temp[i])
    return list5  


 
        