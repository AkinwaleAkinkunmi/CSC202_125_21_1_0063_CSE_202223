#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Functions with outputs
# Uses keyword return

def format_name(f_name, l_name):
    """Takes in input of the first and last name and formats it to 
    returns the title case version of the name. """
    formatted_fname = f_name.title()
    formatted_lname = l_name.title()    
    
    return f"{formatted_fname} {formatted_lname}"
    
formatted_string = format_name("wale", "akiNkuNmi")
print(formatted_string)

#Challenge 1 - Days in Month

def is_leap(year):
    #Docstrings
    """Check if a year is a leap year"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True 
            else:
                return False
        else:
            return True
    else:
        return False
        
def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid Month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) == True and month == 2:
        return 29
    return month_days[month - 1]
    

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
    


# In[ ]:




