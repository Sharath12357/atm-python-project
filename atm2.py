pin=0
bal=0
def set_pin():
    while True:
        global pin
        pin1=int(input('enter a 4 digit pin:'))
        pin2=int(input('confirm your pin'))
        if pin1==pin2:
            print('pin set successful...!')
            pin=pin1
            break
        else:
            print("pin does not matches")
            continue
def deposit():
    global bal
    in_pin=int(input('enter 4 digit pin:'))
    if in_pin==pin:
        amt=int(input('enter amount:'))
        bal+=amt
        print(f'amount of {amt} rs.deposited successfully')
    else:
        print('incorrect pin')    
    
def withdraw():
    global bal
    in_pin=int(input('enter pin :'))
    if in_pin==pin:
        amt=int(input('enter the amount:'))
        if amt>bal:
            print('aukat se bahar')
        else:
            bal-=amt
            print(f'the amount withdraw {amt}rs')

    
def check_bal():
    in_pin=int(input('enter 4 digit pin'))
    if in_pin==pin:
        print(f'avilable balance in your acc:{bal}rs')
    else:
        print('invalid pin')

while True:
    print('_'*45)
    print('enter 1 for set pin')
    print('enter 2 for deposit')
    print('enter 3 for withdraw')
    print('enter 4 for check balance')
    print('enter 5 for exit')
    ch=int(input('enter your choice:'))
    if ch==1:
        set_pin()
    elif ch==2:
        deposit()
    elif ch==3:
        withdraw()
    elif ch==4:
        check_bal()
    else :
        print("bye bye!!!!")
    a=input('do you want to use(y/n)')
    if a.lower()=='y':
        continue
    else:
        print('byee byeee!!!')
        break



