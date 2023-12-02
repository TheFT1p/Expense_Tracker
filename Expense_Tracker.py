
import datetime
class Expense_Tracker():

    brojac = 1
    type = ['Budget', 'Expense']   #NOT RELEVANT, BUT I'LL KEEP IT
    category_list = ['Groceries', 'Transportation', 'Entertainment']
    budget_list = ['Income', 'Side Job']
    def __init__(self, name, budget = 0): #DO I NEED THESE ATTRIBUTES?
        self._name = name
        self._date = datetime.date.today()
        self._budget = budget
        self._tracker = []      #THIS WILL KEEP ALL THE RECORDS OF INCOMES AND EXPENSES
        self._user_id = Expense_Tracker.brojac
        self._tracker.append((self._user_id, self._date, self._budget, 'Income', 'Budget'))
        Expense_Tracker.brojac += 1

#[(user_id, date, value, category, type)]

    @property
    def name(self):
        return self._name

    @name.setter
    def category(self, value):
        self._name = value.title()

    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, value):
        self._category = value.title()

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, datetime.date):
            raise ValueError("Please use yyyy-mm-dd date format")
        else:
            self._date = value
    
    @property
    def budget(self):
        return self._budget
    @budget.setter
    def budget(self, value):
        self._budget = int(value)

    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, value):
        self._description = value

    @classmethod
    def Add_Category(cls, value):
        if value.title() not in Expense_Tracker.category_list:
            Expense_Tracker.category_list.append(value)
        else:
            raise KeyError("You already have this category")

    @classmethod
    def Change_Category(cls, old_value, new_value):
        if old_value.title() not in Expense_Tracker.category_list:
            raise ValueError("You CANNOT change category that doesn't exist")
        else:
            Expense_Tracker.category_list.remove(old_value.title())   #CHANGE METHOD SO THAT YOU FIND POSITION AND CHANGE IT WITHIN THE SAME POSITION
            Expense_Tracker.category_list.append(new_value)

    @classmethod
    def Remove_Category(cls, value):
        if value.title() not in Expense_Tracker.category_list:
            raise ValueError("It already doesnt exist.")
        else:
            Expense_Tracker.category_list.remove(value.title())

    # [(user_id, date, value, category, type)]

    #[(date, value, category, type)]
    def Add_Expense(self, expense_value, category, date = datetime.date.today()):

        if self._budget > expense_value:
            self._budget -= expense_value
            self._tracker.append((self._user_id, date, expense_value, category, 'Expense'))
            print(f"Success! Current budget left: {self._budget}")
        elif self._budget == expense_value:
            self._budget -= expense_value
            self._tracker.append((self._user_id, date, expense_value, category, 'Expense'))

            print(f"Success! Current budget left: {self._budget}, you're out of budget now!")
        else:
            raise ValueError("You cannot spend more than you have!")


    def Add_Budget(self, value, category = 'Income'):
        self._budget += value
        self._tracker.append((self._user_id, datetime.date.today(), value, category, 'Income'))
        print(f"You've successfully added {value}. Your budget is now {self._budget}")


    # def Print_All_Records(self):
    #     for record in self._tracker:
    #         print(record, sep=' SEP ', end='NOVI RED')

    def Print_All_Records(self):
        print(self._tracker)

    def Expense_Overview(self):
        expense_list = [item[2] for item in self._tracker if item[4] == 'Expense']
        income_list = [item[2] for item in self._tracker if item[4] == 'Budget']
        expenses = sum(expense_list)
        incomes = sum(income_list)
        print(f"Total Expenses: ${expenses}\nTotal Income: ${incomes}\nSavings: ${incomes-expenses}")


#[(user_id, date, value, category, type)]



klijent = Expense_Tracker('Dusan', 10000)
klijent.Add_Budget(5000,'Side Job')
klijent.Add_Expense(6969, 'Groceries')
klijent.Add_Budget(4200,'Side Job')

klijent.Print_All_Records()
klijent.Expense_Overview()






















