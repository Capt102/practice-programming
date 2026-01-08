class Validinvalid:
    def solution(self,vari):
        symbol_variable={
            "[":"]",
            "(":")",
            "{":"}",
            "<":">"
        }
        stack=[]
        for i in vari:
            if i in symbol_variable:
                stack.append(i)
            else:
                print("invalid")

