from unicodedata import name


def greeting(name,age):
    year = 2022-age
    return f"Helo {name} you were born in {year}"

greeting("Susan", 21)



def my_country(country="Uganda", student="Susan"):
    return f"Hello {student}You are from {country}"

my_country()



def greet(name):
    return f"Hello {name}"

greet("Susan")


def greet_multiple(*names):
    for name in names:
        print(f"Hello {name}")


greet_multiple()

def sum(*numbers):
    sum=0
    for num in numbers:
        sum+=numbers
        return sum


sum()
    



# dictionary

def greet_mltiple(**kwargs):
    keys = kwargs.keys()
    if "country" in keys:
        print(f"Yoh {kwargs['name']} you are from {kwargs['country']}")
    elif "age" in keys:
        year = 2022-kwargs["age"]
        print(f"Hello {kwargs['name']} you were born in {year}")

    elif not kwargs:
     print(f"Hello Anonymous")


greet_mltiple()


def  sum_age_greet(*args, **kwargs):
    sum = 0
    for num in args:
     sum+=num
    keys = kwargs.keys()

    if "name" in keys:
	    print(f"hello {kwargs['name']}, the answer is {sum}")

    elif "country" in keys:
        print(f"Hello from {kwargs['country']}, the answer is {sum}")


    elif not kwargs:
        print(f"Hello Anonymous the answer is {sum}")
    




sum_age_greet()
















    # print(kwargs)
    # print(kwargs.keys())
    # print(kwargs.values())


# greet_mltiple(name="Kababy")
# greet_mltiple(name="Kababy", age=20, country="Uganda")