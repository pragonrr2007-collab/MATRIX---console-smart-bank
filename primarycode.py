'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import time 
from datetime import datetime

# -------------------------
# Data structures
# -------------------------
accounts = []
transactions = []
SERVICE_CHARGE = 1.0
SMS_COST = 0.5
PRE_SCHEDULE_COST = 0.2
DEVELOPER_CODE = "dev123"

# -------------------------
# Helper functions
# -------------------------
def find_account(acc_no):
    for idx, acc in enumerate(accounts):
        if acc['acc'] == acc_no:
            return idx
    return -1

def format_time(ts):
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")

def read_amount(prompt):
    try:
        amt = float(input(prompt))
        if amt <= 0:
            print("Invalid amount.")
            return None
        return amt
    except ValueError:
        print("Invalid input.")
        return None

def verify_pin(idx):
    pin = input("Enter PIN: ").strip()
    if str(accounts[idx]['pin']) == pin:
        return True
    print("Incorrect PIN.")
    return False

# -------------------------
# Account functions
# -------------------------
def create_account():
    acc_no = input("Enter account number: ").strip()
    if find_account(acc_no) != -1:
        print("Account already exists.")
        return
    name = input("Enter name: ").strip()
    try:
        bal = float(input("Enter initial balance: ").strip())
        pin = int(input("Enter PIN: ").strip())
    except ValueError:
        print("Invalid input.")
        return
    accounts.append({'acc': acc_no, 'name': name, 'bal': bal, 'pin': pin})
    print("Account created successfully.")

def deposit_or_withdraw(is_withdraw):
    acc_no = input("Enter account number: ").strip()
    idx = find_account(acc_no)
    if idx == -1:
        print("Account not found.")
        return
    if not verify_pin(idx):
        return
    amt = read_amount("Enter amount: ")
    if amt is None: return
    if is_withdraw and amt + SERVICE_CHARGE > accounts[idx]['bal']:
        print("Insufficient funds.")
        return
    if is_withdraw:
        accounts[idx]['bal'] -= (amt + SERVICE_CHARGE)
        tx_type = "WITHDRAW"
    else:
        accounts[idx]['bal'] += amt
        tx_type = "DEPOSIT"
    transactions.append({
        'when': time.time(),
        'type': tx_type,
        'from': acc_no,
        'to': "" if is_withdraw else acc_no,
        'amount': amt,
        'fee': SERVICE_CHARGE if is_withdraw else 0,
        'is_scheduled': False,
        'scheduled_for': 0
    })
    print(f"{tx_type} successful.")

def transfer_flow():
    from_acc = input("From account: ").strip()
    idx_from = find_account(from_acc)
    if idx_from == -1:
        print("Sender account not found.")
        return
    if not verify_pin(idx_from): return
    to_acc = input("To account: ").strip()
    idx_to = find_account(to_acc)
    if idx_to == -1:
        print("Receiver not found.")
        return
    amt = read_amount("Enter amount: ")
    if amt is None: return
    total = amt + SERVICE_CHARGE
    if accounts[idx_from]['bal'] < total:
        print("Insufficient funds.")
        return
    accounts[idx_from]['bal'] -= total
    accounts[idx_to]['bal'] += amt
    transactions.append({
        'when': time.time(),
        'type': "TRANSFER",
        'from': from_acc,
        'to': to_acc,
        'amount': amt,
        'fee': SERVICE_CHARGE,
        'is_scheduled': False,
        'scheduled_for': 0
    })
    print("Transfer successful.")

def view_balance():
    acc_no = input("Enter account number: ").strip()
    idx = find_account(acc_no)
    if idx == -1:
        print("Account not found.")
        return
    if not verify_pin(idx): return
    print(f"Account: {accounts[idx]['acc']}, Balance: {accounts[idx]['bal']:.2f}")

def view_all_accounts():
    if not accounts:
        print("No accounts exist.")
        return
    for acc in accounts:
        print(f"{acc['acc']} | {acc['name']} | Balance: {acc['bal']:.2f}")

def show_history():
    acc_no = input("Enter account number: ").strip()
    idx = find_account(acc_no)
    if idx == -1:
        print("Account not found.")
        return
    print("---- Transactions ----")
    found = False
    for tx in transactions:
        if tx['from'] == acc_no or tx['to'] == acc_no:
            when_s = format_time(tx['when'])
            print(f"{when_s} | {tx['type']} | From:{tx['from']} To:{tx['to'] or '-'} Amt:{tx['amount']} Fee:{tx['fee']}")
            found = True
    if not found:
        print("No transactions for this account.")

# -------------------------
# Additional Options
# -------------------------
def account_summary():
    view_all_accounts()
    acc_no = input("Enter account number: ").strip()
    idx = find_account(acc_no)
    if idx == -1:
        print("Account not found.")
        return
    show_history()

def change_pin():
    acc_no = input("Enter account number: ").strip()
    idx = find_account(acc_no)
    if idx == -1:
        print("Account not found.")
        return
    if not verify_pin(idx): return
    try:
        newpin = int(input("Enter new PIN: ").strip())
    except ValueError:
        print("Invalid PIN.")
        return
    accounts[idx]['pin'] = newpin
    print("PIN changed successfully.")

# -------------------------
# Schedule Manager
# -------------------------
def schedule_manager():
    while True:
        print("==============================")
        print("Schedule Manager")
        print("1. Schedule Future Transaction")
        print("2. Cancel Scheduled Transaction")
        print("3. Back to Previous Menu")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            from_acc = input("From account: ").strip()
            idx_from = find_account(from_acc)
            if idx_from == -1:
                print("Sender not found.")
                continue
            if not verify_pin(idx_from): continue
            typ = input("Type (deposit/withdraw/transfer): ").strip().lower()
            amt = read_amount("Enter amount: ")
            if amt is None: continue
            to_acc = ""
            if typ == "transfer":
                to_acc = input("To account: ").strip()
                if find_account(to_acc) == -1:
                    print("Receiver not found.")
                    continue
            dt_str = input("Enter date/time (YYYY-MM-DD HH:MM:SS): ").strip()
            try:
                sch_time = time.mktime(datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S").timetuple())
                if sch_time <= time.time():
                    print("Provide future date.")
                    continue
            except ValueError:
                print("Bad date format.")
                continue
            transactions.append({
                'when': time.time(),
                'type': typ.upper(),
                'from': from_acc,
                'to': to_acc,
                'amount': amt,
                'fee': SERVICE_CHARGE + SMS_COST + PRE_SCHEDULE_COST,
                'is_scheduled': True,
                'scheduled_for': sch_time
            })
            print("Transaction scheduled.")

        elif choice == "2":
            acc_no = input("Your account number: ").strip()
            idx_acc = find_account(acc_no)
            if idx_acc == -1:
                print("Account not found.")
                continue
            if not verify_pin(idx_acc): continue
            found = False
            for i, tx in enumerate(transactions):
                if tx['is_scheduled'] and tx['from'] == acc_no:
                    print(f"Index {i} | Type:{tx['type']} | To:{tx['to'] or '-'} | Amt:{tx['amount']} | Sch:{format_time(tx['scheduled_for'])}")
                    found = True
            if not found:
                print("No scheduled transactions.")
                continue
            try:
                idx_cancel = int(input("Enter index to cancel: ").strip())
                if idx_cancel < 0 or idx_cancel >= len(transactions) or not transactions[idx_cancel]['is_scheduled']:
                    print("Invalid index.")
                    continue
                transactions[idx_cancel]['is_scheduled'] = False
                transactions[idx_cancel]['scheduled_for'] = 0
                print("Scheduled transaction cancelled.")
            except ValueError:
                print("Invalid input.")
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
        input("\nPress Enter to continue...")

# -------------------------
# Developer Options
# -------------------------
def developer_options():
    code = input("Enter developer security code: ").strip()
    if code != DEVELOPER_CODE:
        print("Access denied! Incorrect security code.")
        return
    while True:
        print("==============================")
        print("Developer Options")
        print("1. Export Data to File")
        print("2. System Report")
        print("3. Reset / Clear All Data")
        print("4. Back to Previous Menu")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            export_data()
        elif choice == "2":
            system_report()
        elif choice == "3":
            reset_all_data()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")
        input("\nPress Enter to continue...")

def export_data():
    with open("accounts_export.csv", "w") as f:
        f.write("acc,name,balance,pin\n")
        for acc in accounts:
            f.write(f"{acc['acc']},{acc['name']},{acc['bal']:.2f},{acc['pin']}\n")
    with open("transactions_export.csv", "w") as f:
        f.write("when,type,from,to,amount,fee,is_scheduled,scheduled_for\n")
        for tx in transactions:
            f.write(f"{format_time(tx['when'])},{tx['type']},{tx['from']},{tx['to']},{tx['amount']},{tx['fee']},{int(tx['is_scheduled'])},{format_time(tx['scheduled_for']) if tx['is_scheduled'] else ''}\n")
    print("Data exported to CSV successfully.")

def system_report():
    scheduled = sum(1 for tx in transactions if tx['is_scheduled'])
    print("---- System Report ----")
    print(f"Total accounts: {len(accounts)}")
    print(f"Total transactions: {len(transactions)}")
    print(f"Scheduled transactions: {scheduled}")
    print("All modules operational.")

def reset_all_data():
    confirm = input("Reset all data? (y/n): ").strip().lower()
    if confirm == "y":
        accounts.clear()
        transactions.clear()
        print("All data cleared.")
    else:
        print("Aborted.")

# -------------------------
# Balance Tools
# -------------------------
def smart_balance_calculator():
    acc_no = input("Enter account number: ").strip()
    idx = find_account(acc_no)
    if idx == -1:
        print("Account not found.")
        return
    target_str = input("Enter date/time (YYYY-MM-DD HH:MM:SS): ").strip()
    try:
        target = time.mktime(datetime.strptime(target_str, "%Y-%m-%d %H:%M:%S").timetuple())
    except ValueError:
        print("Bad date format.")
        return
    current = accounts[idx]['bal']
    scheduled_deposits = sum(tx['amount'] - tx['fee'] for tx in transactions if tx['is_scheduled'] and tx['scheduled_for'] <= target and tx['from']==acc_no and tx['type']=='DEPOSIT')
    scheduled_withdrawals = sum(tx['amount'] + tx['fee'] for tx in transactions if tx['is_scheduled'] and tx['scheduled_for'] <= target and tx['from']==acc_no and tx['type'] in ('WITHDRAW','TRANSFER'))
    sms_tax = sum(1 for tx in transactions if tx['is_scheduled'] and tx['scheduled_for'] <= target) * SMS_COST
    predicted = current + scheduled_deposits - scheduled_withdrawals - sms_tax
    print("---- Smart Balance Calculator ----")
    print(f"Account: {acc_no}")
    print(f"Current balance: {current:.2f}")
    print(f"Scheduled deposits (<=target): {scheduled_deposits:.2f}")
    print(f"Scheduled withdrawals: {scheduled_withdrawals:.2f}")
    print(f"SMS / Service tax (est.): {sms_tax:.2f}")
    print(f"Predicted balance (net): {predicted:.2f}")

def balance_predictor_ml():
    acc_no = input("Enter account number: ").strip()
    idx = find_account(acc_no)
    if idx == -1:
        print("Account not found.")
        return
    total_dep = sum(tx['amount'] for tx in transactions if (tx['from']==acc_no and tx['type']=='DEPOSIT') or (tx['type']=='TRANSFER' and tx['to']==acc_no))
    cnt_dep = sum(1 for tx in transactions if (tx['from']==acc_no and tx['type']=='DEPOSIT') or (tx['type']=='TRANSFER' and tx['to']==acc_no))
    total_wd = sum(tx['amount'] for tx in transactions if (tx['from']==acc_no and tx['type'] in ('WITHDRAW','TRANSFER')))
    cnt_wd = sum(1 for tx in transactions if (tx['from']==acc_no and tx['type'] in ('WITHDRAW','TRANSFER')))
    avg_dep = total_dep/cnt_dep if cnt_dep else 0
    avg_wd = total_wd/cnt_wd if cnt_wd else 0
    expected_change = (avg_dep - avg_wd) * 0.7
    predicted_next = accounts[idx]['bal'] + expected_change
    confidence = 50.0
    if cnt_dep + cnt_wd > 20:
        confidence = 85.0
    elif cnt_dep + cnt_wd > 5:
        confidence = 65.0
    print("---- Balance Predictor (ML) ----")
    print(f"Avg deposit: {avg_dep:.2f} | Avg withdraw: {avg_wd:.2f}")
    print(f"Expected net change: {expected_change:.2f}")
    print(f"Predicted next balance: {predicted_next:.2f}")
    print(f"Confidence: {confidence:.1f}%")

def balance_tools():
    while True:
        print("==============================")
        print("Balance Tools")
        print("1. Smart Balance Calculator (AI)")
        print("2. Balance Predictor (ML)")
        print("3. Back to Previous Menu")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            smart_balance_calculator()
        elif choice == "2":
            balance_predictor_ml()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
        input("\nPress Enter to continue...")

# -------------------------
# Additional Menu
# -------------------------
def additional_menu():
    while True:
        print("==============================")
        print("Additional Options")
        print("1. Account Summary / Statement")
        print("2. Change PIN")
        print("3. Schedule Manager")
        print("4. Developer Options")
        print("5. Delete Account")
        print("6. Balance Tools")
        print("7. Back to Main Menu")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            account_summary()
        elif choice == "2":
            change_pin()
        elif choice == "3":
            schedule_manager()
        elif choice == "4":
            developer_options()
        elif choice == "5":
            acc_no = input("Account to delete: ").strip()
            idx = find_account(acc_no)
            if idx == -1:
                print("Account not found.")
                continue
            if not verify_pin(idx): continue
            accounts.pop(idx)
            for tx in transactions:
                if tx['from']==acc_no: tx['from']=""
                if tx['to']==acc_no: tx['to']=""
            print("Account deleted.")
        elif choice == "6":
            balance_tools()
        elif choice == "7":
            break
        else:
            print("Invalid choice.")
        input("\nPress Enter to continue...")

# -------------------------
# Main Menu
# -------------------------
def main():
    while True:
        print("==============================")
        print("Main Menu")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. View Balance")
        print("6. View All Accounts")
        print("7. Transaction History")
        print("8. Scheduled Transactions")
        print("9. Additional Options")
        print("10. Exit")
        choice = input("Enter choice: ").strip()
        
        if choice == "1":
            create_account()
        elif choice == "2":
            deposit_or_withdraw(False)
        elif choice == "3":
            deposit_or_withdraw(True)
        elif choice == "4":
            transfer_flow()
        elif choice == "5":
            view_balance()
        elif choice == "6":
            view_all_accounts()
        elif choice == "7":
            show_history()
        elif choice == "8":
            # Show scheduled transaction history
            print("---- Scheduled Transactions ----")
            found = False
            for idx, tx in enumerate(transactions):
                if tx['is_scheduled']:
                    when_s = format_time(tx['when'])
                    sch_s = format_time(tx['scheduled_for'])
                    print(f"{when_s} | {tx['type']} | From:{tx['from']} To:{tx['to'] or '-'} Amt:{tx['amount']} Fee:{tx['fee']} | Scheduled for: {sch_s}")
                    found = True
            if not found:
                print("No scheduled transactions.")
        elif choice == "9":
            additional_menu()
        elif choice == "10":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
