def atm_operation(balance: int, action: str, amount: int) -> int:
    if amount < 0:                
        return balance                
    
    if action == "deposit":
        return balance + amount
    elif action == "withdraw":
        if balance >= amount:
            return balance - amount
        else:
            print("Mablag' yetarli emas!")
            return balance
    return balance

balans = int(input("Balansni kiriting: "))
amal = input("Amalni tanlang (deposit/withdraw): ")
summa = int(input("Summani kiriting: "))

yangi_balans = atm_operation(balans, amal, summa)

print(f"Amal bajarildi. Joriy balans: {yangi_balans}")
