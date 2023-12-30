# simulates the bank account with basic functions of deposit, transfer, withdrawal and interest
class BankAccount:
    # class variable to check the last account number
    _lastAccNum = 1000
    # constructor
    # @param self: the object
    # @param balance: initial balance in the account
    # @param accName: name of the account
    # @param accountType: type of the account (saving/checking)
    def __init__(self,balance, accName,accountType):
        self._accNum = 0
        # each account has 1 higher than the last account number
        BankAccount._lastAccNum += 1
        self._accNum += BankAccount._lastAccNum
        self._balance = balance
        self._accName = accName
        self._accountType = accountType
        self._interestRate = 3
        
    # get the balance in the account
    # @return: current balance in the account
    def getBalance(self):
        return self._balance
    
    # get name of the account
    # @return: name of the account
    def getName(self):
        return self._accName
    
    # get type of the account
    # @ return: the type of the account
    def getAccountType(self):
        return self._accountType
    
    # get number of the account
    # @ return: the number of the account
    def getAccNum(self):
        return self._accNum
    
    # withdraws the given amount from the account
    # @param amount: amount to withdraw
    def withdraw(self, amount):
        try:
            # raise ValueError when the withdrawal exceeds the current balance
            if self._balance - amount < 0:
                raise ValueError
            # if the error was not raised, withdraw the amount from the account
            self._balance -= amount
        # when ValueError raise, print the error message
        except ValueError:
            print()
            print(" %s has insufficient funds" % self._accName)
            print()
    
    # deposit the given amount into the account
    # @param amount: amount to deposit
    def deposit(self, amount):
        self._balance += amount
    
    # transfers the given amount to another BankAccout
    # @param BankAccout: target BankAccout for the transfer
    # @param amount: amount to transfer
    def transfer(self, BankAccount, amount):
        try:
            # raise ValueError when the transfer exceeds the current balance
            if self._balance - amount < 0:
                raise ValueError
            # if the error was not raised, transfer the amount from the account
            self._balance -= amount
            BankAccount._balance += amount
        # when ValueError raise, print the error message
        except ValueError:
            print()
            print(" %s has insufficient funds" % self._accName)
            print()
            
    # displays the account information
    def displayAccountInfo(self):
        print("The account name:",self._accName)
        print("The account num:", self._accNum)
        print("The account type:",self._accountType)
        print("The account balance: $%.2f" %self._balance)
        print()
    # adds interest to the account only when the account type is saving
    def addInterest(self):
        if self._accountType == "saving":
            # call static method percentOf from Financial class
            interest = Financial.percentOf(self._balance, self._interestRate)
            # add interest to the account balance
            self._balance += interest
            
            
# simulates the financial methods for calculations
class Financial:
    # static method 
    # calculates the given percentage of given balance
    @staticmethod
    # @param balance: the balance to calculate the percent
    # @param interestRate: the interest rate as percentage
    def percentOf(balance, interestRate):
        return balance * (interestRate/100)        
        
        
        
        
        
        
        