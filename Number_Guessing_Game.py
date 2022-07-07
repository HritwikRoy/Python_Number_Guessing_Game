while True:
    
    import random
    print(" \n\n *** NUMBER GUESSING GAME WITH PYTHON *** \n ")
    x=input("Enter Your Name=")
    g=input(f"HEY {x}....Do you want to play this game (y or n)=")
    if(g=="y" or g=="Y" or  g=="yes"):
        random_number=random.randint(1,100)
        guess=1
        user_number=int(input(f" {x} Please guess the number : "))
        while True:
            if(user_number==random_number):
                print(f" \n YOU WIN  !!!! Guess Number = {guess} !!!!")
                break;
            elif(user_number<random_number):
                print("TOO LOW  !!!!")
                guess+=1
                user_number=int(input(f" {x} Please guess the number again:"))
            else:
                print("TOO HIGHT !!!!")
                guess+=1
                user_number=int(input(f" {x} Please guess the number again:"))
    elif(g=="n" or g=="N" or g=="no"):
        print(f"OK {x}.....THANK YOU")
        break   
