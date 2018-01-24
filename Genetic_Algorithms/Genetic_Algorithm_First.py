
def Decode(Input):
    State = 0
    I = 0
    while I < len(Input):
        if State == 0:
            if str(Input[I]) in "+-*^":
                Input.pop(I)
            else:
                I+=1
                State=1-State
        elif State == 1:
            if str(Input[I]) not in "+-*^":
                Input.pop(I)
            else:
                I+=1
                State=1-State
    if len(Input) == 0:
        Input=[0]
    if len(Input) % 2 == 0:
        if Input[-1] in "+-*^":
            Input = Input[:-1]
    return Input

def Fitness(List):
    Operation = "+"
    Total = 0
    State = 0
    for Val in List:
        if State == 0:
            if Operation == "+":
                Total = Total + Val
            if Operation == "-":
                Total = Total - Val
            if Operation == "*":
                Total = Total * Val
            if Operation == "^":
                Total = Total ** Val
        if State == 1:
            Operation = Val
        State = 1 - State
    return Total
    
    Total = List[0]
    for I in range(1, len(List), 2):
        if List[I] == "+":
            Total = Total + List[I-1]
        elif List[I] == "-":
            Total = Total - List[I-1]
        elif List[I] == "*":
            Total = Total * List[I-1]
        elif List[I] == "^":
            Total = Total ** List[I-1]
    return Total
    
def Main():
    Code = Decode(["+", 1, "*", 2, "^", 5])
    print(Code)
    print(Fitness(Code))


Main()

