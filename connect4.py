my_array = [["-","-","-","-","-","-","-"],["-","-","-","-","-","-","-"],["-","-","-","-","-","-","-"],["-","-","-","-","-","-","-"],["-","-","-","-","-","-","-"],["-","-","-","-","-","-","-"]]
def my_insert(arr,column,player):
    for row in range(6): 
        if (arr[5-row][column]=="-"): arr[5-row][column]=player; return 0
def check(arr):
    for a in range(4):
        for b in range(7):
            for c in range(4):
                if ((arr[a][b]!="-") and (arr[a][b]==arr[a+1][b]) and (arr[a+2][b]==arr[a+1][b]) and (arr[a+2][b]==arr[a+3][b])) or ((arr[b][a]!="-") and (arr[b][a]==arr[b][a+1]) and (arr[b][a+1]==arr[b][a+2]) and (arr[b][a+1]==arr[b][a+3])) or ((arr[a][c]!="-") and (arr[a][c]==arr[a+1][c+1]) and ((arr[a+2][c+2]==arr[a+1][c+1])) and (arr[a+2][c+2]==arr[a+3][c+3])) or ((arr[a][6-c]!="-") and (arr[a][6-c]==arr[a+1][5-c]) and ((arr[a][6-c]==arr[a+2][4-c])) and ((arr[a+2][4-c]==arr[a+3][3-c]))): #going down
                    return True
    return False
def my_print(arr):
    return ("0 1 2 3 4 5 6\n"+" ".join(arr[0])+"\n"+" ".join(arr[1])+"\n"+" ".join(arr[2])+"\n"+" ".join(arr[3])+"\n"+" ".join(arr[4])+"\n"+" ".join(arr[5])+"\n")
player1 = True
while not check(my_array+[["-","-","-","-","-","-","-"]]):
    newval = int(input(my_print(my_array)+"Now it is player " +("1" if player1 else "2")+"'s turn! Which column do you choose?\n"))
    my_insert(my_array,newval,"X" if player1 else "O")
    player1 = not player1
print("Player "+("1" if player1 else "2")+" won!")