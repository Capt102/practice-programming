class Splitwise:
    def solution(self):
        payment={ 
            "hari":1200,
            "vipin":1400,
            "jhon":1000,
            "tom":120,
            "vishnu":0,
            "avinash":0,
            "jini":0,
            "asok":0
            }
        total_expense=sum(payment.values())
        print(total_expense)
        indiv_split=total_expense/len(payment)

        result={k:indiv_split-v for k,v in payment.items()}
        print(result)

sp=Splitwise()
sp.solution()