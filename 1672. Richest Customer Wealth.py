class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        greater_val=0
        pointer=0
        for customer in accounts:
            total_money=sum(customer)
            if pointer==0:
                greater_val=total_money
            else:
                if total_money>greater_val:
                    greater_val=total_money
        return greater_val       