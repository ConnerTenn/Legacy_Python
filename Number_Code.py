#-----------
#| Imports |
#-----------

#-------------
#| Functions |
#-------------
def Start():
    Mode=str(input("1: Text->Code   2: Code->Text  Choice:"))
    if not(Mode=='1') and not(Mode=='2'):
        print("Mode %s is Invalid" % Mode)
        Start()
    Mode_Select(Mode)

def Mode_Select(Mode):
    Numbers='012458'
    Alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ. '
    if Mode=='1':
        Original=str(input("Text:"))
        Original=Original.upper()
        Original=Original.rstrip()
        for Char in Original:
            if not(Char in Alphabet):
                print('Invalid Text')
                Mode_Select(Mode)
        Original_List=list(Original)
        Text_Code(Original,Original_List)
    elif Mode=='2':
        Original=str(input("Numbers:"))
        Original=Original.upper()
        Original=Original.rstrip()
        for Char in Original:
            if not(Char in Numbers):
                print('Invalid Numbers')
                Mode_Select(Mode)
        Original_List=list(Original)
        Code_Text(Original,Original_List)

def Map_Txt_Num(Letter):
    Txt_Num={'A':[1],'B':[2],'C':[2,1],'D':[4],'E':[4,1],'F':[4,2],'G':[4,2,1],'H':[8],'I':[8,1],'J':[8,2],'K':[8,2,1],'L':[8,4],'M':[8,4,1],'N':[8,4,2],'O':[8,4,2,1],'P':[8,8],'Q':[8,8,1],'R':[8,8,2],'S':[8,8,2,1],'T':[8,8,4],'U':[8,8,4,1],'V':[8,8,4,2],'W':[8,8,4,2,1],'X':[8,8,8],'Y':[8,8,8,1],'Z':[8,8,8,2],' ':[5],'.':[5,5]}
    return Txt_Num[Letter]

def Map_Num_Txt(Letter_Build): # May not keep
    Num_Txt={'1':['A'],'2':['B'],'21':['C'],'4':['D'],'41':['E'],'42':['F'],'421':['G'],'8':['H'],'81':['I'],'82':['J'],'821':['K'],'84':['L'],'841':['M'],'842':['N'],'8421':['O'],'88':['P'],'881':['Q'],'882':['R'],'8821':['S'],'884':['T'],'8841':['U'],'8842':['V'],'88421':['W'],'888':['X'],'8881':['Y'],'8882':['Z'],'5':[' '],'55':['.']}
    return Num_Txt[Letter_Build] 

def Text_Code(Original,Original_List):
    New_List=[]
    for Letter in Original_List:
        New_List=New_List+Map_Txt_Num(Letter)
        New_List=New_List+[0]
    #New_List[len(New_List)-1]=''
    Final=''
    for Number in New_List:
        Final=Final+str(Number)
    print('"%s" = "%s"'% (Original,Final))
        

def Code_Text(Original,Original_List):
    New_List=[]
    Letter_Build=''
    for String in Original_List:
        Number=int(String)
        if Number==0:
            New_List=New_List+Map_Num_Txt(Letter_Build)
            Letter_Build=''
        else:
            Letter_Build=Letter_Build+str(Number)
    Final=''
    for Letter in New_List:
        Final=Final+str(Letter)
    print('"%s" = "%s"'% (Original,Final))

#-----------
#| Program |
#-----------
Start()

