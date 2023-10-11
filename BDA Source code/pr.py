from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
import requests
import bs4
from sqlite3 import *
import matplotlib.pyplot as plt
import maskpass


def f1():
	add_window.deiconify()
	main_window.withdraw()
def f2():
	main_window.deiconify()
	add_window.withdraw()
def f3():
	update_window.deiconify()
	main_window.withdraw()
def f4():
	main_window.deiconify()
	update_window.withdraw()
def f5():
	view_window.deiconify()
	main_window.withdraw()
	vw_emp_data.delete(1.0,END)
	info=""
	con = None
	try:
		con = connect("internship.db")
		cursor = con.cursor()
		sql="select * from employee"
		cursor.execute(sql)
		data = cursor.fetchall()
		for d in data:
			info = info + " id : " + str(d[0]) + " Name : " + str(d[1]) + "\t"+ " Salary : " + str(d[2])+"\n"
		vw_emp_data.insert(INSERT,info)
	except Exception as e:
		showerror("Issue",e)
	finally:
		if con is not None:
			con.close()		



def f6():
	main_window.deiconify()
	view_window.withdraw()
def f7():
	delete_window.deiconify()
	main_window.withdraw()
def f8():
	main_window.deiconify()
	delete_window.withdraw()
def f9():
	login_window.deiconify()
	main_window.withdraw()
def f10():
	main_window.deiconify()
	login_window.withdraw()

def save():
	id = int(aw_ent_id.get())
	name = aw_ent_name.get()
	salary = int(aw_ent_salary.get())
	
	if id <0:
		showerror("Issue","Enter Positive Value")
	elif len(name)==0:
		showerror("Issue","Name Should Not be Empty")
	
	elif len(name)<2:
		showerror("Issue","Name Must contain 3 Alphabet")
	elif salary < 8000:
		showerror("Issue","Salary must be greater than 8K")
	else:
		con = None
		try:
			con=connect("internship.db")
			cursor = con.cursor()
			sql = "insert into employee values('%d','%s','%d')"
			cursor.execute(sql % (id,name,salary))
			con.commit()
			showinfo("Success","Record Added")
			aw_ent_id.delete(0,END)
			aw_ent_name.delete(0,END)
			aw_ent_salary.delete(0,END)
		
		except Exception as e:
			con.rollback()
			showerror("Issue",e)
			aw_ent_id.delete(0,END)
			aw_ent_name.delete(0,END)
			aw_ent_salary.delete(0,END)
		finally:
			if con is not None:
				con.close()

def update():
	
	con = None
	try:
		id = int(uw_ent_id.get())
		name = uw_ent_name.get()
		salary = int(uw_ent_salary.get())
		con = connect("internship.db")
		cursor = con.cursor()
		sql = "update employee set name = '%s',salary = '%d' where id = '%d'"
		cursor.execute(sql % (name,salary,id))
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Success","Record Updated")
			uw_ent_id.delete(0,END)
			uw_ent_name.delete(0,END)
			uw_ent_salary.delete(0,END)
		else:
			showerror("Issue",id," does not exists")
	except Exception as e:
		print("Issue = ",e)
	finally:
		if con is not None:
			con.close()
			print("closed")

def delete():
	con = None
	try:
		con = connect("internship.db")
		
		cursor = con.cursor()
		sql = "delete from employee where id = '%d'"
		id = int(dw_ent_id.get())
		cursor.execute(sql %(id))
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Success","Record deleted")
			dw_ent_id.delete(0,END)
		else:
			print(id," does not exists")
	except Exception as e:
		showerror("Issue",e)
	finally:
		if con is not None:
			con.close()

def barchart():
	
	
	
	con = None
	try:
		info=[]
		subjects = []
		name=['id1','id2','id3','id4','id5']
		con = connect("internship.db")
		cursor = con.cursor()
		sql = "select salary,name from employee order by salary desc limit 5"
		cursor.execute(sql)
		data = cursor.fetchall()
		
		#info.append(data)
		#showinfo("success",info)
		for i in data:
			for d in i:
				info.append(i[0])
		for i in data:
			for d in i:
				subjects.append(i[1])
		plt.bar(subjects,info,color=["red","green","pink","yellow","blue"])
		plt.xlabel("Employee")
		plt.ylabel("Salary")
		plt.title("Employee Salary")
		plt.show()
		
		
		
	except Exception as e:
		showerror("Issue",e)
	finally:
		if con is not None:
			con.close()
def login():
	user = lw_ent_user.get()
	pas = lw_ent_pas.get()
	if user == "student" and pas == "student3714":
		main_window.deiconify()
		lw_ent_pas.delete(0,END)
		login_window.withdraw()
	else:
		showerror("Issue","Incorrect Password")
		lw_ent_pas.delete(0,END)
			
	
			
			
			
	
	
#------------------------------------------------------------------------------------------------
f = ("Arial",20,"bold")
fq = ("Arial",15,"bold")
fv = ("Arial",16,"bold")

login_window = Tk()
login_window.title("Admin Login")
login_window.geometry("500x500+400+100")
login_window.configure(bg="#CCCCFF")

lw_lab_user=Label(login_window,text="Enter Admin Name",font=f)
lw_ent_user=Entry(login_window,font=f,bd=2)
lw_lab_user.pack(pady=10)
lw_ent_user.pack(pady=10) 



lw_lab_pas=Label(login_window,text="Enter Password",font=f)
lw_ent_pas=Entry(login_window,font=f,bd=2)
lw_lab_pas.pack(pady=10)
lw_ent_pas.pack(pady=10) 
lw_btn_login = Button(login_window,text = "Log in",font=f,width=10,command=login)
lw_btn_login.pack(pady=10)

		





		
#------------------------------------------------------------------------------------------------
main_window = Toplevel(login_window)
main_window.title("E . M . S")
main_window.geometry("500x500+400+100")
main_window.configure(bg="#CCCCFF")


mw_btn_add = Button(main_window,text = "Add",font=f,width=10,command=f1)
mw_btn_add.pack(pady=10)

mw_btn_view = Button(main_window,text = "View",font=f,width=10,command=f5)
mw_btn_view.pack(pady=10)

mw_btn_update = Button(main_window,text = "Update",font=f,width=10,command=f3)
mw_btn_update.pack(pady=10)

mw_btn_delete = Button(main_window,text = "Delete",font=f,width=10,command=f7)
mw_btn_delete.pack(pady=10)

mw_btn_chart = Button(main_window,text = "Chart",font=f,width=10,bg="white",command=barchart)
mw_btn_chart.pack(pady=10)

wa = "https://www.brainyquote.com/quote_of_the_day"
res = requests.get(wa)
#print(res)
	
data = bs4.BeautifulSoup(res.text, "html.parser")
#print(data)
	
info = data.find("img", {"class":"p-qotd"})
#print(info)

#quote = info["alt"]
#print("Quote = ",quote)
quote_label = Label(main_window,text="quote",font=fq,width=45,height=10,fg="white",bg="#7393B3")
quote_label.pack(pady=13)
main_window.withdraw()


#--------------------------------------------------------------------

add_window = Toplevel(main_window)
add_window.title("Add Emp")
add_window.geometry("500x500+400+100")
add_window.configure(bg="#CCCCFF")

aw_lab_id=Label(add_window,text="Enter id",font=f)
aw_ent_id=Entry(add_window,font=f,bd=2)
aw_lab_id.pack(pady=10)
aw_ent_id.pack(pady=10) 


aw_lab_name=Label(add_window,text="Enter Name",font=f)
aw_ent_name=Entry(add_window,font=f,bd=2)
aw_lab_name.pack(pady=10)
aw_ent_name.pack(pady=10) 

aw_lab_salary=Label(add_window,text="Enter salary",font=f)
aw_ent_salary=Entry(add_window,font=f,bd=2)
aw_lab_salary.pack(pady=10)
aw_ent_salary.pack(pady=10) 

aw_btn_save = Button(add_window,text = "Save",font=f,width=10,command=save)
aw_btn_save.pack(pady=10)

aw_btn_back = Button(add_window,text = "Back",font=f,width=10,command=f2)
aw_btn_back.pack(pady=10)
add_window.withdraw()

#---------------------------------------------------------------

view_window = Toplevel(main_window)
view_window.title("View Emp")
view_window.geometry("500x500+400+100")
view_window.configure(bg="#CCCCFF")

vw_emp_data = ScrolledText(view_window,width=35,height=15,font=fv)
vw_emp_data.pack(pady=10)

vw_btn_back = Button(view_window,text = "Back",font=f,width=10,command=f6)
vw_btn_back.pack(pady=10)
view_window.withdraw()
#---------------------------------------------------------------


update_window = Toplevel(main_window)
update_window.title("Update Emp")
update_window.geometry("500x500+400+100")
update_window.configure(bg="#CCCCFF")

uw_lab_id=Label(update_window,text="Enter id",font=f)
uw_ent_id=Entry(update_window,font=f,bd=2)
uw_lab_id.pack(pady=10)
uw_ent_id.pack(pady=10) 

uw_lab_name=Label(update_window,text="Enter Name",font=f)
uw_ent_name=Entry(update_window,font=f,bd=2)
uw_lab_name.pack(pady=10)
uw_ent_name.pack(pady=10) 

uw_lab_salary=Label(update_window,text="Enter salary",font=f)
uw_ent_salary=Entry(update_window,font=f,bd=2)
uw_lab_salary.pack(pady=10)
uw_ent_salary.pack(pady=10) 

uw_btn_chart = Button(update_window,text = "Save",font=f,width=10,command=update)
uw_btn_chart.pack(pady=10)

uw_btn_chart = Button(update_window,text = "Back",font=f,width=10,command=f4)
uw_btn_chart.pack(pady=10)
update_window.withdraw()

#---------------------------------------------------------------

delete_window = Toplevel(main_window)
delete_window.title("delete Emp")
delete_window.geometry("500x500+400+100")
delete_window.configure(bg="#CCCCFF")

dw_lab_id=Label(delete_window,text="Enter id",font=f)
dw_ent_id=Entry(delete_window,font=f,bd=2)
dw_lab_id.pack(pady=10)
dw_ent_id.pack(pady=10)  

dw_btn_chart = Button(delete_window,text = "Delete",font=f,width=10,command=delete)
dw_btn_chart.pack(pady=10)

dw_btn_chart = Button(delete_window,text = "Back",font=f,width=10,command=f8)
dw_btn_chart.pack(pady=10)
delete_window.withdraw()

main_window.mainloop()