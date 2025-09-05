
class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name.lower()
        self.phone = phone
        self.email = email
        self.address = address

    # def __repr__(self) -> str:
    #     return f"Name: {self.name.title()}, \nPhone No. {self.phone}, \nEmail: {self.email}, \nAddress: {self.address}"

    def __str__(self) -> str:
        return f"{self.name} | {self.phone} | {self.email} | {self.address}"
    
    def to_dict(self):
        return {
            'phone' : self.phone,
            'email' : self.email,
            'address' : self.address
        }

    @staticmethod
    def from_dict(name,data):
        return Contact(name,data['phone'],data['email'],data['address'])
    
    def update(self, name=None, phone=None, email=None, address=None):
        if name:
            self.name = name
        if phone:
            self.phone = phone
        if email:
            self.email = email
        if address:
            self.address = address