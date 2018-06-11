class A:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def getEmail(self):
        return self.email

    @getEmail.setter
    def getEmail(self, value):
        self.email = value


a = A("abc", "abc@gmail.com")
print(a.getEmail)
print("========================")
a.getEmail = "xyz@gmail.com"
print(a.getEmail)
