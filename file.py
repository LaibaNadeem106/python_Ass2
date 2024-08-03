#Adding two numbers

def add_two_num():
    first_num=int(input("enter first num:"))
    sec_num=int(input("enter second num:"))
    total_sum=first_num + sec_num
    print(f"the total sum is {total_sum}")

add_two_num()

#Agreement bot 
def agreement_bot():
    favorite_animal=input("what is your favorite animal?")
    print(f"My favorite animal is also {favorite_animal}!")

agreement_bot()

#Fahrenheit to calculus
def fahrenheit_to_cal():
    degrees_fahrenheit=float(input("Enter temp in fahrenheit:"))
    degrees_calculus=(degrees_fahrenheit-32)*5.0/9.0
    print(f"Temperature:{degrees_fahrenheit}F={degrees_calculus}C")

fahrenheit_to_cal()

#Triangle Perimeters


def tri_perimeter():
    side2=float(input("what is the length of side2?"))
    side1=float(input("what is the length of side1?"))
    side3=float(input("what is the length of side3?"))
    perimeter=side1+side2+side3
    print(f"the perimeter of the triangle is {perimeter}")

tri_perimeter()

#square_num

def sq_num():
    num=float(input("type a number to see its square:"))
    sq=num*num
    print(f"{num} squared is {sq}")
sq_num()

#del a num from list

def delete_num():
    num=[1,2,3,4,5]
    num.remove(3)
    print(num)
delete_num()

#creating a list by addinng elements

def add_lists():
    list1=[1,2,3]
    list2=[4,5,6]
    list1.extend(list2)
    print(list1)

add_lists()

#pop_method
def pop_method():
    items=[10,20,30,40]
    removed_item=items.pop()
    print(f"the list after pop:{items}")
    print(f"the removed item: {removed_item}")
pop_method()

#index_method

def index_method():
    colors=['red','blue','green','yellow']
    index_of_green=colors.index('green')
    print(f"the index of 'green' is {index_of_green}")
index_method()

#challenge questions
#get last element
def get_last_element(lst):
    print(f"the last element is: {lst[-1]}")
get_last_element([1,2,3,4])

#get list
def get_a_list():
    values=[]
    while True:
        value=input("enter a value:")
        if value=="":
            break
        values.append(value)
    print(f"here is the list:{values}")
get_a_list()