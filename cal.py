'''importing tkinter library which is  the inbuilt python module that is used to create GUI applications and
 its alreay inculded in python no need to install it in your system'''
from tkinter import *

'''importing tkcalendar library and also before that install it in your system by  using command
(pip install tkcalendar) in terminal. '''
from tkcalendar import *
#defining tkinter window as while you make GUI projects there is Tk window necessary which we here initialize   by variable Calendar.
Calendar = Tk()

'''creating  a function which display the date by taking (current_date) which display date 
in pattern you want and (user_date) which takes the date from GUI calender and overall this 
function  return or display the date which you have selected from button. '''
def select_date():
    current_date = display_cal.get_date()
    user_date=Label(text=current_date)
    user_date.pack(padx=4,pady=4)

    
'''now in this calendar code we are using 2 widgets :Widgets are objects  that represent buttons, frames etc.
 1 button
 2 label '''

'''by using  label widgets and initializing it by (display_cal) in which we are taking a date pattern 
which shows your day with the particular date pattern as you want.'''
display_cal= Calendar(Calendar,setmode="day",date_pattern='d/m/yy')    

#taking pady and padx which shows  the number of pixels surrounding the widget  for horizontal or vertical padding.
display_cal.pack(padx=20,pady=20)

#by using button widgets  for the calendar and give any name to the button you want by taking it in a varible.
Button_cal=Button(Calendar,text="Select the date",command=select_date)
Button_cal.pack(padx=20,pady=20)

#taking  the dimension ,  calendar title name and background color of the calendar as per choice and at the the tkinter event loop.
Calendar.geometry('500x500')
Calendar.title("GUI Calendar")
Calendar.configure(bg="blue")
Calendar.mainloop()
