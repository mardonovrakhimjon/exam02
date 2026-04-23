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
print(atm_operation(100000, "deposit", 50000)) # 150000

print(atm_operation(100000, "withdraw", 20000)) # 80000