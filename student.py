class Student:
    country="Kenya"
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        
       

    def greeting(self):
        return f"Hello {self.first_name}, from {self.country}, welcome to {self.school}"


    def full_name(self):
        return f"My name is {self.first_name}, {self.last_name}"
    
    def year_of_birth(self):
        return f"You were born in march {2022-self.age}"

    def initial(self):
        return f"{self.first_name[0]}, {self.last_name[0]}"


