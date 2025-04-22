#fuction input with output (for output we use return keyword)
"""
It is doc String-->
This code for taking first name and last name
"""
def format_name(f_name,l_name):
    formated_f_name=f_name.title()
    formated_l_name=l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name("raNJit","cHAvAn"))