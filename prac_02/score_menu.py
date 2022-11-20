MENU = """(G)et a valid score (Must be 0-100 inclusive)
(P)rint result
(S)how stars
(Q)uit"""

def main():
    print(MENU)
    menu_input = input().upper()
    while menu_input != 'Q':
        if menu_input == 'G':
            score = int(input("Enter score: "))
        elif menu_input == 'P':
            check_score(score)
        elif menu_input == 'S':
            for i in range(0, score):
                print("*", end='')
            print("\n")
        else:
            print("Invalid input")
        print(MENU)
        menu_input = input().upper()
    print("Farewell")

def check_score(score):
    if score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    elif score < 50:
        print("Bad")
    elif score < 0:
        print("Invalid score")

main()