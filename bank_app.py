class Bank():
    Branch = 'Marathahalli'
    IFSC   = 'BANK0000420'
    ROI    = 0.07
    def __init__(self,Name,Mobno,Aadhar,Gender,Bal,Pin):
        self.Name   = Name
        self.Mobno  = Mobno
        self.Aadhar = Aadhar
        self.Gender = Gender
        self.Bal    = Bal
        self.Pin    = Pin
    def Details(self):
        print(f'Name            = {self.Name}')
        print(f'Mobile Number   = {self.Mobno}')
        print(f'Aadhar Number   = {self.Aadhar}')
        print(f'Gender          = {self.Gender}')
        print(f'Bal             = {self.Bal}')
        print(f'Pin             = {self.Pin}')
    @classmethod
    def UpdateBranch(cls):
        cls.Branch = 'Whitefield'
    def Withdraw(self):
        count = 3
        while count != 0:
            print(f'No.of attemps is {count}')
            if self.Password() == self.Pin:
                amount = int(input('Enter the amount to withdraw : '))
                if self.Bal >= amount:
                    if 100 <= amount <= 10000:
                        if amount % 100 == 0:
                            self.Bal -= amount
                            print('Amount debited successfully...')
                            print(f'Available balance is {self.Bal}')
                            break
                        else:
                            print('Incorrect denominations')
                    else:
                        print('Enter valid amount')
                else:
                    print('Insufficient balance')
            else:
                print('Invalid pin')
                count -= 1
        else:
            print('Try again after 24-hours')
    def Deposite(self):
        cash = int(input('Enter the amount to deposite : '))
        if 100 <= cash <= 10000:
            if cash % 100 == 0:
                self.Bal += cash
                print('Amount credited successfully...')
                print(f'Updated balance is {self.Bal}')
            else:
                print('Incorrect denominations')
        else:
            print('Enter valid amount')
    def CheckBalance(self):
        count = 3
        while count != 0:
            print(f'No.of attemps is {count}')
            if self.Password() == self.Pin:
                print(f'Available balance is {self.Bal}')
                break
            else:
                print('Invalid pin')
                count -= 1
        else:
            print('Try again after 24-hours')
    @staticmethod
    def Password():
        a = int(input('Enter 4-digit pin : '))
        return a
    def ChangePin(self):
        if self.Password() == self.Pin:
            self.Pin = int(input('Enter 4-digit pin'))

User1 = Bank('Pranay',9876543210,123456789012,'Male',20000,1234)
User2 = Bank('Dhruva',9999999999,234567890123,'Male',30000,4321)
User3 = Bank('Greeshma',8888888888,345678901234,'Female',10000,1111)
User1.Deposite()
