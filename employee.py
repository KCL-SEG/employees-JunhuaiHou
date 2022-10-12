"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
class Employee:
    def __init__(self, name, pay, payCount, bonus, bonusCount):
        self.name = name
        self.pay = pay
        self.payCount = payCount
        self.bonus = bonus
        self.bonusCount = bonusCount

    def get_pay(self):
        return self.pay * self.payCount + self.bonus * self.bonusCount

    def __str__(self):
        statement = self.name
        if(self.payCount == 1):
            statement += f" works on a monthly salary of {self.pay}"
        else:
            statement += f" works on a contract of {self.payCount} hours at {self.pay}/hour"

        if(self.bonusCount == 0):
            statement += "."
        elif(self.bonusCount == 1):
            statement += f" and receives a bonus commission of {self.bonus}."
        else:
            statement += f" and receives a commission for {self.bonusCount} contract(s) at {self.bonus}/contract."
    
        statement += f"  Their total pay is {self.get_pay()}."

        return statement

    # Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, 1, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 25, 100, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, 1, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 25, 150, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, 1, 1500, 1)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 30, 120, 600 , 1)
