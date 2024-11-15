from ex import Expense

def main():
    print('Welcome to Expense Tracker app')

    expense_file_path = "expense.csv"

    expense = expense_kitna_hua()

    file_m_save_kro(expense,expense_file_path)

    summarize_expense(expense_file_path)

    


def expense_kitna_hua():
    print("kitna kharcha kiya hai? ")
    expense_name = input("kha kharcha kiya bolo? ")
    expense_amount = float(input("kitne paise yaha pe udaye h? "))
    print(f"expense name is{expense_name},{expense_amount}")

    expense_categories = [
        "Food",
        "Home",
        "Work",
        "Fun",
        "Misc"
    ]

    while True:
        print('kis catgory me kharcha kr rhe ho btao? ')
        for i,category_name in enumerate(expense_categories):
            print(f"{i+1}.{category_name}")

        value_range = f"[1-{len(expense_categories)}]"
        selected_index = int(input(f'kis category kaa kharcha kiya h? {value_range}'))-1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            print(selected_category)

            new_expense = Expense(name = expense_name,category = selected_category,amount=expense_amount)

            return new_expense


        else:
            print('galat category h bhai')

        break







def file_m_save_kro(expense : Expense,expense_file_path):
    print(f"kracha file m save ho gya hai : {expense} to {expense_file_path}")

    with open(expense_file_path,"a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")
    

def summarize_expense(expense_file_path):
    print('summary of user expense')
    expenses = []
    with open(expense_file_path,'r') as f:
        lines = f.readlines()
        for i in lines:
            name,amount,category = i.strip().split(",")
            print(f"{name} {amount} {category}")
            expense_name = Expense(name = name,amount=float(amount),category=category)
            expenses.append(expense_name)









            
            


if __name__ == "__main__":
    main()