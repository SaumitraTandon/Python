ans='y'
def guest():
    print('')
    print('1.Show all the records of teahcers\n2.Add records of a teacher\n3.Search records\n4.Delete record\n5.Graphical represent\n6.Change values of records')
    x=int(input('Enter the choice of no.'))
    if x==1:
        showallrecords()
    elif x==2:
        addrecords()
    elif x==3:
        search()
    elif x==4:
        delete()
    elif x==5:
        guestgr()
    elif x==6:
        changerecord()
    elif x!=[1,2,3,4,5]:
        print('\t\tINVALID INPUT')
def teachgr():
    print('1.Teachers Department\n2.Gender Graph')
    x=int(input('Enter the no.'))
    if x==1:
        deptgraph()
    elif x==2:
        sexgraph()
    elif x!=[1,2]:
        print('INVALID INPUT')
def deptgraph():
    import mysql.connector as mydb
    import matplotlib.pyplot as plt
    d1=mydb.connect(host='localhost',user='root',passwd='motimohit@1230',database='school_work')
    c1=d1.cursor()
    quer="select count(*) from teachers where dept='english';"
    c1.execute(quer)
    x=c1.fetchone()
    lst=list(x)
    quer="select count(*) from teachers where dept='history';"
    c1.execute(quer)
    y=c1.fetchone()
    lst1=list(y)
    quer="select count(*) from teachers where dept='Physics';"
    c1.execute(quer)
    z=c1.fetchone()
    lst2=list(z)
    quer="select count(*) from teachers where dept='Chemistry';"
    c1.execute(quer)
    a=c1.fetchone()
    lst3=list(a)
    quer="select count(*) from teachers where dept='IP';"
    c1.execute(quer)
    d1.commit()
    a=c1.fetchone()
    lst4=list(a)
    lstt=lst+lst1+lst2+lst3+lst4
    y=['English','History','Physics','Chemistry','IP']
    plt.bar(y,lstt,width=0.50)
    plt.xlabel('Subjects')
    plt.ylabel('No.of teachers')
    plt.show()
def sexgraph():
    import mysql.connector as mydb
    import matplotlib.pyplot as plt
    d1=mydb.connect(host='localhost',user='root',passwd='',database='school_work')
    c1=d1.cursor()
    quer='Select count(*) from teachers where gender="Male";'
    c1.execute(quer)
    x=c1.fetchone()
    lst=list(x)
    quer='Select count(*) from teachers where gender="Female";'
    c1.execute(quer)
    y=c1.fetchone()
    lst1=list(y)
    lstt=lst+lst1
    y=['Male','Female']
    plt.bar(y,lstt,width=0.50)
    plt.xlabel('Sex')
    plt.ylabel('No. of teachers')
    plt.show()
def showallrecords():
    import mysql.connector as mydb
    import pandas as pd
    pd.set_option('display.expand_frame_repr',False)
    d1=mydb.connect(host="localhost",user="root",passwd="",database="school_work")
    c1=d1.cursor()
    quer="select id from teachers;"
    c1.execute(quer)
    rec=c1.fetchall()
    lst=[]
    for t in rec:
        for x in t:
            lst.append(x)
    quer1="select name from teachers;"
    c1.execute(quer1)
    rec1=c1.fetchall()
    lst1=[]
    for t in rec1:
        for x in t:
            lst1.append(x)
    quer2="select dept from teachers;"
    c1.execute(quer2)
    rec2=c1.fetchall()
    lst2=[]
    for t in rec2:
        for x in t:
            lst2.append(x)
    quer3="select joining_date from teachers;"
    c1.execute(quer3)
    rec3=c1.fetchall()
    lst3=[]
    for t in rec3:
        for x in t:
            lst3.append(x)
    quer4="select gender from teachers;"
    c1.execute(quer4)
    rec4=c1.fetchall()
    lst4=[]
    for t in rec4:
        for x in t:
            lst4.append(x)
    quer5="select contact from teachers;"
    c1.execute(quer5)
    rec5=c1.fetchall()
    lst5=[]
    for t in rec5:
        for x in t:
            lst5.append(x)
    quer6="select sal from teachers;"
    c1.execute(quer6)
    rec6=c1.fetchall()
    lst6=[]
    for t in rec6:
        for x in t:
            lst6.append(x)
    data={"id":lst,"name":lst1,"dept":lst2,"joining date":lst3,"gender":lst4,"contact":lst5,"sal":lst6}
    df=pd.DataFrame(data)
    print(df)
def addrecords():
    import mysql.connector as mydb
    d1=mydb.connect(host="localhost",user="root",passwd="",database="school_work")
    c1=d1.cursor()
    print("")
    print("SUBJECTS: \n1. english=$30000 \n2. history=$40000 \n3. Physics=$50000 \n4. Chemistry=$60000 \n5. ip=$70000")
    print("")
    ans1="yes"
    while ans1=="yes":
        x=int(input("Enter the id:"))
        quer1="select * from teachers where id=%d;" %x
        c1.execute(quer1)
        if c1.rowcount>0:
            print("duplicate record")
        elif c1.rowcount==0:
            ans1="no"
    y=input("Enter the name:")
    a=input("Enter the dept:")
    b=input("Enter the joining date:")
    c=input("Enter the gender:")
    ans1="yes"
    while ans1=="yes":
        z=input("Enter the contact no.")
        quer="select * from teachers where contact='%s';"
        c1.execute(quer)
        if c1.rowcount>0:
            print("DUPLICATE RECORD")
        elif c1.rowcount==0:
            ans1="no"
    v=int(input("Enter the salary:"))
    quer="Insert into teachers values(%d,'%s','%s','%s','%s','%s',%d);" %(x,y,a,b,c,z,v)
    c1.execute(quer)
    d1.commit()
    print("Record Added")
    f=input("Want to see the added record:")
    if f=="y":
        quer="select * from teachers where id=%d;"%x
        c1.execute(quer)
        rec=c1.fetchone()
        tid,name,dept,joindate,gender,contact,sal=rec
        print("id= %d"%tid,"name= %s"%name,"department= %s"%dept,"joindate= %s"%joindate,"gender= %s"%gender,"contactno= %s"%contact,"salary= %d"%sal,sep="\n")
    else:
        print("Thank You")
def search():
    import mysql.connector as mydb
    import pandas as pd
    d1=mydb.connect(user="root",host="localhost",passwd="",database="school_work")
    c1=d1.cursor()
    print("1. id \n2. contact no.")
    x=int(input("enter the no:")) 
    if x==1:
        tid=int(input("enter the id:"))
        quer="select * from teachers where id=%d;" % tid
        c1.execute(quer)
        if c1.rowcount>0:
            lst=list(c1.fetchone())
            iddf=pd.DataFrame({"id":lst[0],"name":lst[1],"dept":lst[2],"joindate":lst[3],"gender":lst[4],"contact":lst[5],"salary":lst[6]},index=[1])
            print(iddf)
        elif c1.rowcount==0:
            print("NO RECORD")
    elif x==2:
        cno=input("enter the contact no.:")
        quer1="select * from teachers where contact='%s'" % cno
        c1.execute(quer1)
        if c1.rowcount>0:
            row1=list(c1.fetchall()[0])
            iddf=pd.DataFrame({"id":row1[0],"name":row1[1],"dept":row1[2],"joindate":row1[3],"gender":row1[4],"contact":row1[5],"salary":row1[6]},index=[1])
            print(iddf)
        else:
            print("NO RECORD")
    else:
        print("INVAILD INPUT")
def delete():
    import mysql.connector as mydb
    d1=mydb.connect(host="localhost",user="root",passwd="",database="school_work")
    c1=d1.cursor()
    x=int(input("enter the id:"))
    quer="delete from teachers where id=%d;" %x
    rowcount=c1.execute(quer)
    if rowcount>0:
        d1.commit()
        print("Record Deleted")
    else:
        print("NO RECORD FOUND")
def changerecord():
    import mysql.connector as mydb
    import pandas as pd
    pd.set_option('display.expand_frame_repr',False)
    d1=mydb.connect(user="root",host="localhost",passwd="",database="school_work")
    c1=d1.cursor()
    tid=int(input("enter the id:"))
    quer="select * from teachers where id=%d" % tid
    c1.execute(quer)
    if c1.rowcount>0:
        row=list(c1.fetchone())
        print('')
        df=pd.DataFrame({"id":row[0],"name":row[1],"department":row[2],"joindate":row[3],"gender":row[4],"contact":row[5],"salary":row[6]},index=[1])
        print(df)
        print("\n1. id \n2. name \n3. department \n4. joindate \n5. gender \n6. contact \n7. salary")
        cr=int(input("enter the no:"))
        if cr==1:
            ans1='yes'
            while ans1=="yes":
                y=int(input("enter the id:"))
                quer1="select * from teachers where id=%d" %y
                c1.execute(quer1)
                if c1.rowcount>0:
                    print("DUPLICATE RECORD")
                elif c1.rowcount==0:
                    ans1="no"
            quer="update teachers set id=%d where id=%d" %(y,tid)
            c1.execute(quer)
            d1.commit()
            print("RECORD CHANGED")
        elif cr==2:
            y=input("enter the name:")
            quer="update teachers set name='%s' where id=%d" %(y,tid)
            c1.execute(quer)
            d1.commit()
            print("RECORD CHANGED")    
        elif cr==3:
            y=input("enter the department:")
            quer="update teachers set dept='%s' where id=%d" %(y,tid)
            c1.execute(quer)
            d1.commit()
            print("RECORD CHANGED")     
        elif cr==4:
            y=input("enter the join date:")
            quer="update teachers set joining_date='%s' where id=%d" %(y,tid)
            c1.execute(quer)
            d1.commit()
            print("RECORD CHANGED")
        elif cr==5:
            y=input("enter the gender:")
            quer="update teachers set gender='%s' where id=%d" %(y,tid)
            c1.execute(quer)
            d1.commit()
            print("RECORD CHANGED")
        elif cr==6:
            ans1="yes"
            while ans1=="yes":
                y=int(input("enter the contact no:"))
                quer1="select * from teachers where contact='%s'" %y
                c1.execute(quer1)
                if c1.rowcount>0:
                    print("DUPLICATE RECORD")
                elif c1.rowcount==0:
                    ans1="no"
            quer="update teachers set contact='%s' where id=%d" %(y,tid)
            c1.execute(quer)
            d1.commit()
            print("RECORD CHANGED")
        elif cr==7:
            y=int(input("enter the salary:"))
            quer="update teachers set sal=%d where id=%d" %(y,tid)
            c1.execute(quer)
            d1.commit()
            print("RECORD CHANGED")
        elif cr!=[1,2,3,4,5,6,7]:
            print("INVAILD INPUT")
    elif c1.rowcount==0:
        print("NO RECORD FOUND TO CHANGE")
while ans=="y":
    print("")
    print("1. show all the records of teachers \n2. add records of a teacher \n3. search records \n4. delete record \n5. Graphical representation \n6. Change values of records")  
    x=int(input("Enter the choice of no:"))
    if x==1:
        showallrecords()
    elif x==2:
        addrecords()
    elif x==3:
        search()
    elif x==4:
        delete()
    elif x==5:
        teachgr()
    elif x==6:
        changerecord()
    elif x!=[1,2,3,4,5]:
        print("\t\tINVAILD INPUT")
    ans=input("want to continue:")
