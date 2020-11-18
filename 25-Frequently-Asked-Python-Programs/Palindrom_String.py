#Un palindrom este un cuvant care se citeste la fel si de la inceput la sfarsit si de la sfarsit la inceput.

s=input("enter a string: ") #abcde

#varianta 1: find reverse of string, and check if reverse and original are same or not.
#print(s[:])     #abcde        #printeaza stringul de la inceput la final
#print(s[0:5])   #abcde        #printeaza de la index 0 la index 5
#print(s[0:5:1]) #abcde        #printeaza de la index 0 la index 5 cu pasi de cate 1
#print(s[::])    #abcde        #printeaza de la index 0 la final cu pasi de cate 1
#print(s[::-1])  #edcba        #printeaza de la sfarsit la inceput
reverse=(s[::-1])
if reverse==s:
    print("palindrome")
else:
    print("not palindrome")
