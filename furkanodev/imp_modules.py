# main.py
import modules 

print(modules.is_letter('f'))  
print(modules.to_lowercase('F'))  
modules.info()
text= input()
"""text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque vel velit vitae est eleifend ultricies ut sodales risus." """
analiz = modules.text_frequency_analysis(text)
print(analiz)  
