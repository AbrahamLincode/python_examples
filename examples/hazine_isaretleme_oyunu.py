row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

for i in range(0,5):
    position = ""
    col = input("select column 1-3 ?")  # pozisyonun kolun değerini alma 
    match col:
        case "1" | "2" | "3":
            position += col
        case _:
            print("please enter only values between 1 and 3")

    row = input("select row ?")
    match row:
        case    "1" | "2" | "3":
            position += row
        case _:
            print("please enter only values between 1 and 3")

    map[int(position[1])-1][int(position[0])-1] = "X"

    print(f"{row1}\n{row2}\n{row3}")

