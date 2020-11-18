#Mai intai se va creea un file cu numele my_module in care vom scrie:
def produs(x,y):
    return x*y
#apoi vom creea alt file in care vom importa modului nostru:
import my_module
print (my_module.produs(10,4))

#ambele fisiere vor fi salvate in acelasi folder