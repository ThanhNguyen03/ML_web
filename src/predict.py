from tkinter import *
import joblib


def show_entry_fields():
    p1=int(e1.get())
    p2=int(e2.get())

    model = joblib.load('kmeans_modellll.pkl')
    result=model.predict([[p1,p2]])
    print("Khách hàng này thuộc cụm số: ", result[0])

    if result[0] == 0:
        Label(master, text="Khách hàng có thu nhập trung bình hàng năm và chi tiêu hàng năm trung bình").grid(row=31)
    elif result[0]==1:
        Label(master, text="Khách hàng có thu nhập hàng năm cao nhưng chi tiêu hàng năm thấp").grid(row=31)
    elif result[0]==2:
        Label(master, text="Khách hàng có thu nhập hàng năm thấp và chi tiêu hàng năm thấp").grid(row=31)
    elif result[0]==3:
        Label(master, text="Khách hàng có thu nhập hàng năm thấp nhưng chi tiêu hàng năm cao").grid(row=31)
    elif result[0]==4:
        Label(master, text="Khách hàng có thu nhập hàng năm cao và chi tiêu hàng năm cao").grid(row=31)

master = Tk()
master.title("Phân khúc khách hàng bằng Machine Learning")

label = Label(master, text = "Phân khúc khách hàng bằng Machine Learning"
                          , bg = "black", fg = "white"). \
                               grid(row=0,columnspan=2)

Label(master,text="Thu nhập hàng năm").grid(row=1)
Label(master, text="Điểm chi tiêu").grid(row=2)


e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)

Button(master, text='Predict', command=show_entry_fields).grid()

mainloop()