from datetime import datetime

bank_accounts = {
1001: {
"first_name": "Alice",
"last_name": "Smith",
"id_number": "123456789",
"balance": -2500.50,
"transactions_to_execute": [
("2024-08-17 14:00:00", 1001, 1002, 300), ("2024-08-17 15:00:00", 1001, 1003, 200)],
"transaction_history": [
("2024-08-25 09:00:00", 1001, 1002, 500), ("2024-08-15 09:30:00", 1001, 1200, 1200)]},
1002:{
"first_name": "Dayana",
"last_name": "Hersko",
"id_number": "12349865",
"balance": 12500.50,
"transactions_to_execute": [
("2024-08-17 14:00:00", 1002, 1001, 600), ("2024-08-22 15:00:00", 1002, 1003, 200)],
"transaction_history": [
("2024-08-21 09:00:00", 1002, 1001, 700), ("2024-08-25 09:30:00", 500, 700, 1200)]},
1003:{
"first_name": "Dany",
"last_name": "Levy",
"id_number": "12565665",
"balance": 3000.50,
"transactions_to_execute": [
("2024-08-17 09:00:00", 1003, 1001, 600), ("2024-08-22 15:00:00", 1003, 1002, 1200)],
"transaction_history": [
("2024-08-21 09:00:00", 1002, 1001, 700), ("2024-08-22 09:30:00", 1003, 1002, 500)]},
1004:{
"first_name": "Dany",
"last_name": "Levkovitz",
"id_number": "18877665",
"balance": 8000,
"transactions_to_execute": [
("2024-08-17 09:00:00", 1004, 1001, 600), ("2024-08-22 15:00:00", 1004, 1001, 1200)],
"transaction_history": [
("2024-08-21 09:00:00", 1004, 1003, 700), ("2024-08-22 09:30:00", 1004, 1002, 500)]},
1005:{
"first_name": "Dayanad",
"last_name": "Liver",
"id_number": "18877665",
"balance": 10000,
"transactions_to_execute": [
("2024-08-17 09:00:00", 1004, 1001, 600), ("2024-08-22 15:00:00", 1004, 1001, 1200)],
"transaction_history": [
("2024-08-21 09:00:00", 1004, 1003, 700), ("2024-08-22 09:30:00", 1004, 1002, 500)]}
}
success: bool = False
def handle_menu():
        fromacc:int = 0
        toacc:int = 0
        amm:float = 0
        while True:
            choice:int = 0
            print("1. transfer money to another account")
            print("2. perform all waiting transactions")
            print("3. reports")
            print("9 - exit the program")
            choice = int(input("please type your choice"))

            match choice:
                case 1:
                    while True:
                        fromacc = int(input("from what account to transfer"))
                        if fromacc not in bank_accounts.keys():
                            Print("from account not found try again")
                            continue
                        else:
                            break
                    while True:
                        toacc = int(input("to what account to transfer"))
                        if toacc not in bank_accounts.keys():
                            print("to account not found try again")
                            continue
                        else:
                            break
                    while True:

                        try:
                            amm = float(input("what ammount would you like to transfer"))
                            if str(amm).isalpha():
                                raise ValueError()
                                continue
                        except Exception as e:
                            print("********** unknown error " + str(e))
                            continue
                        finally:
                            print("transaction is beeing processed")
                        if fromacc != 0 and toacc != 0 and amm != 0:
                            print("going to transac")
                            if transac(fromacc, toacc, amm) == True:
                                 print("the transaction was added to waiting transactions")
                        else:
                            print("one of the details was zero, please try again")
                            continue
                case 2:
                    mess_from = {key: value["transactions_to_execute"] for key, value in bank_accounts.items()}
                    mess_to = {key: value["transaction_history"] for key, value in bank_accounts.items()}
                    #mess = {{bank_accounts[key]:[bank_accounts[key]["transactions_to_execute"]]} for key in bank_accounts.keys()}
                    print(mess_from)
                    succes = all_transac(mess_from)
                    if success:
                        print("all transactions were processed")
                case 3:

                    print("1. report of all accounts in the bank")
                    print("2. report details of an account by account number")
                    print("3. report details of an account by ID number")
                    print("4. report details of an account by first name")
                    print("5. report of all account sorted by balance, ascending")
                    print("6. report of all transactions sorted by date, ascending")
                    print("7. report of all transactions from today")
                    print("8. report of all account in debit")
                    print("9. report of the total balance of all accounts")
                    print("10. return to menu")
                    choose:int = int(input("please type your choice"))
                    match choose:
                        case 1:
                            success = report1()
                        case 2:
                            try:
                                accnumber = int(input("please type an account number"))
                                if str(accnumber).isalpha():
                                    raise valueException("not an integer")
                            except Exception as e:
                                print("something wrong with your account, try again" + e)
                                if accnumber not in bank_accounts.keys():
                                    print("the account you typed does not exist, try again")
                            success = report2(accnumber)
                        case 3:
                            Idnumber = input("please type ID number of the account")
                            success = report3(Idnumber)
                        case 4:
                            firstName = input("please type the first name ")
                            success = report4(firstName)
                        case 5:
                            success = report5()
                        case 6:
                            success = report6()
                        case 7:
                            success = report7()
                        case 8:
                            success = report8()
                        case 9:
                            success = report9()

                        case _:
                            continue

                case 9:
                    print("bye bye")
                    break

                case _:
                    continue

def transac(fromacc:int, toacc:int, amm:int) -> bool:
    bank_acc = bank_accounts[fromacc]
    print(bank_acc)
    listTuples = bank_accounts[fromacc]["transactions_to_execute"]
    print(listTuples)
    bank_accounts[fromacc]["transactions_to_execute"].append((datetime.now().strftime('%Y-%m-%d %H:%M:%S'), fromacc, toacc, amm))
    bank_acc = bank_accounts[fromacc]
    print(bank_acc)
    success = True
    return success

def all_transac(mess_from:list) ->bool:
    try:
        for key in mess_from.keys():
            if key in bank_accounts.keys():
               print("for this key", mess_from[key])
               for i in range(len(mess_from[key])):
                   bank_accounts[key]["transaction_history"].append(mess_from[key][i])
                   bank_accounts[key]["balance"] += mess_from[key][i][3]
                   print("after append", bank_accounts[key]["transaction_history"])
                   print("after balance", bank_accounts[key]["balance"])
               bank_accounts[key]["transactions_to_execute"].clear()
        success = True
        return success
        print(bank_accounts)
    except Exception as e:
        print("something went wrong" + e)
        success = Fault
        return success

def reprot1() -> bool:
    f = open("report1.txt")
    for account_number, values in bank_accounts.items():
        print(f"account number: {account_number}")
        print(f"first_name : {values["first_name"]}")
        print(f"last_name : {values["last_name"]}")
        f.write(f"account number:  {account_number} {values["first_name"]} {values["last_name"]}")
    f.close
    return True

def report2(accnumber:int) -> bool:
   print(f"account details:")
   print(f"account number: {accnumber} ")
   print(f"first name: {bank_accounts[accnumber]["first_name"]}")
   print(f"last name: {bank_accounts[accnumber]["last_name"]}")
   print(f"ID number: {bank_accounts[accnumber]["id_number"]}")
   print(f"balance: {bank_accounts[accnumber]["balance"]}")
   return True

def report3(id_paramet:str) -> bool:
    report3L = dict(filter(lambda item: item[1]["id_number"] == id_paramet, bank_accounts.items()))
    for account_number, value in report3L.items():
        print(f"account number: {account_number}")
        print(f"first_name : {value["first_name"]}")
        print(f"last_name : {value["last_name"]}")
        print(f"ID number: {value["id_number"]}")
        print(f"balance: {value["balance"]}")
    return True


def report4(firstName:str) -> bool:
    report4L = dict(filter(lambda item: firstName.upper() in (item[1]["first_name"]).upper() , bank_accounts.items()))
    for account_number, value in report4L.items():
        print(f"account number: {account_number}")
        print(f"first_name : {value["first_name"]}")
        print(f"last_name : {value["last_name"]}")
        print(f"ID number: {value["id_number"]}")
        print(f"balance: {value["balance"]}")
    return True

def report5() -> bool:
    report5L = dict(sorted(bank_accounts.items(), key=lambda item: item[1]['balance']))
    for account_number, value in report5L.items():
        print(f"account number: {account_number}")
        print(f"first_name : {value["first_name"]}")
        print(f"last_name : {value["last_name"]}")
        print(f"ID number: {value["id_number"]}")
        print(f"balance: {value["balance"]}")
    return True

def report6() -> bool:
    for i in range(len(bank_accounts.items())):
        report6L = [transaction for account_info in bank_accounts.values() for transaction in
                    account_info['transaction_history']]
        #report6L = [account_info['transaction_history'][i] for account_info in bank_accounts.values()]
        #report6L:list = [lambda (bank_accounts.items(): item[1]["transaction_history"][i])]
    print(report6L)
    #report6LS = sorted(report6L, key=lambda x: (x[0], datetime.datetime.strftime('%Y-%m-%d %H:%M:%S')))
    report6LS = sorted(report6L, key=lambda x: datetime.strptime(x[0], '%Y-%m-%d  %H:%M:%S'))
    print(report6LS)
    for j in range(len(report6LS)):
        print(report6LS[j])
    return True

def report7() -> bool:
    for i in range(len(bank_accounts.items())):
        report6L = [transaction for account_info in bank_accounts.values() for transaction in
                    account_info['transaction_history']]
    print(report6L)
    today_str = datetime.now().strftime('%Y-%m-%d')
    report6LS = list(filter(lambda x: x[0].startswith(today_str), report6L))
    print(report6LS)
    return True

def report8() -> bool:
    report8L = dict(filter(lambda item: item[1]["balance"] <= 0, bank_accounts.items()))
    if not report8L:
        print("no accounts with negative balance or empty account")
        return
    for account_number, value in report8L.items():
        print(f"account number: {account_number}")
        print(f"first_name : {value["first_name"]}")
        print(f"last_name : {value["last_name"]}")
        print(f"ID number: {value["id_number"]}")
        print(f"balance: {value["balance"]}")
    return True

def report9() -> bool:
    total_balance = sum(account_info['balance'] for account_info in bank_accounts.values())
    print(f"total balance of all accounts: {total_balance}" )

    return True

def main():
    handle_menu()


if __name__ == "__main__":
    main()