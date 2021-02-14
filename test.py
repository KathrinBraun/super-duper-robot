def draw_board(liste):
    
    print(f"| {liste[0]} | {liste[1]} | {liste[2]} |\n-------------\n| {liste[3]} | {liste[4]} | {liste[5]} |\n-------------\n| {liste[6]} | {liste[7]} | {liste[8]} |")
    return

def control_end(liste):
    
    if liste[0] == liste[1] == liste[2]:
        return liste[0]
    if liste[3] == liste[4] == liste[5]:
        return liste[3]
    if liste[6] == liste[7] == liste[8]:
        return liste[6]
    if liste[0] == liste[3] == liste[6]:
        return liste[0]
    if liste[1] == liste[4] == liste[7]:
        return liste[1]
    if liste[2] == liste[5] == liste[8]:
        return liste[2]
    if liste[0] == liste[4] == liste[8]:
        return liste[0]
    if liste[2] == liste[4] == liste[6]:
        return liste[2]
    
    return "GoOn"

def checker(liste, brick):
    
    input_compu = '999'
    
    for i in range(1, 10):
        
        if liste[i-1] == str(i):
            liste[i-1] = brick                        #set brick
            control_status = control_end(liste)     #Control if player / compu can finish
            if control_status != "GoOn":
                input_compu = i-1
                return input_compu
            liste[i-1] = str(i)                        #reset to default
        
    return input_compu
            

def play():
    liste = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    draw_board(liste)
    brick_player = input("Would you play with 'X' or with 'O'? ").upper()
    
    while brick_player != 'X' and brick_player != 'O':
        brick_player = input("Impossible brick! Only 'X' or 'O' ").upper()
        
    
    if brick_player == "x" or brick_player == "X":
        brick_compu = "O"
        
    else:
        brick_compu = "X"
    
    import random
    start = random.randint(1, 2)
    
    status = "GoOn"
    xinput_compu = '999'
    
    while status == "GoOn":
        
        if start % 2 == 0:
            input_player = int(input("Please make your choice: "))
            
            while liste[input_player-1] == brick_player or liste[input_player-1] == brick_compu:
                input_player = int(input("Already occupied! Make a new choice: "))
            
            liste[input_player-1] = brick_player
            
        else:
            
            #if liste.count(brick_compu) > 1 or liste.count(brick_compu) > 1:
            input_compu = checker(liste, brick_compu)       # Control if compu can finish
            if input_compu == '999':
                input_compu = checker(liste, brick_player)    # Control if player could finish

                          
            if input_compu == '999':
                input_compu = random.randint(0, 8)
                
                while liste[input_compu] == brick_player or liste[input_compu] == brick_compu:
                    input_compu = random.randint(0, 8)
            
            print("Computer take: ", input_compu + 1)
            liste[input_compu] = brick_compu
                            
        start += 1
        status = control_end(liste)
        
        draw_board(liste)
        
        if liste.count(brick_player) == 5 or liste.count(brick_compu) == 5:
            return print("No winner")
       
    if status == brick_player:
        winner = 'Player'
    else:
        winner = 'Computer'
        
    print("Winner is: ", winner)
    
    return
    
play()