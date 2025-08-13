# Returning a Simple Value
# Making an Argument Optional
def get_formatted_name(f_name, l_name, m_name= ''):
    if m_name:
        full_name = f_name + ' ' + m_name + ' ' + l_name
    else:
        full_name = f_name + ' ' + l_name
    return full_name

muscician = get_formatted_name('U', 'Htoo Eain Thin')
print(muscician)

muscician = get_formatted_name('U', 'Htoo Eain Thin', 'Mg')
print(muscician)