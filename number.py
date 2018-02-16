import os

if __name__ == '__main__':
    count = 0
    number = raw_input("Enter a name: ")
    name  = number.lower()
    for i in range(0, len(name)):
        temp = name[i]
        if temp == 'a' or temp =='j' or temp == 's':
            count += 1
        elif temp == 'b' or temp == 'k' or temp == 't':
            count += 2
        elif temp == 'c' or temp == 'l' or temp == 'u':
            count += 3
        elif temp == 'd' or temp == 'm' or temp =='v':
            count += 4
        elif temp == 'e' or temp == 'n' or temp =='w':
            count += 5
        elif temp == 'f' or temp == 'o' or temp =='x':
            count += 6
        elif temp == 'g' or temp == 'p' or temp =='y':
            count += 7
        elif temp == 'h' or temp == 'q' or temp =='z':
            count += 8
        elif temp == 'i' or temp == 'r':
            count += 9
        elif temp == ' ':
            count += 0

    while count > 9:
        s = 0
        while count:
            s, count = s + count % 10, count // 10
        count = s
        if count == 11 or count == 22:
            break

    os.system('clear')
    print("Your name is : %s" % (number))
    print("Your true number is : %d" % (count))
    if count == 1:
        print("Your key traits are : Single-Minded, Positive, Obstinate, Ambitious, Assertive, Independent")
    if count == 2:
        print("Your key traits are : Feminine, Soft, Sweet, Peaceful, Tidy, Modest, Followers")
    if count == 3:
        print("Your key traits are : Brilliant, Imaginative, Versatile, Energetic, Bold, Vivid, Witty.")
    if count == 4:
        print("Your key traits are : Solid, Practical, Uninspired, Organized, Calm, Steady, Industrious")
    if count == 5:
        print("Your key traits are : Restless, Jumpy, Clever, Impatient, Adventerous, Attractive")
    if count == 6:
        print("Your key traits are : Harmonical, Domestic, Equable, Kind, Relaible, Loyal, Idealistic, Affectionate")
    if count == 7:
        print("Your key traits are : Scholar Philosopher, Mystic, Occulist, Dignified, Reserved")
    if count == 8:
        print("Your key traits are : Succesful, Strong, Tough, Practical, Cautious, Tenacious")
    if count == 9:
        print("Your key traits are : Large-minded, Visionary, Idealistic, Romantic, Passionate")
    if count == 11:
        print("Your key traits are : You have a special message to give to the world. Powerful personality.")
    if count == 22:
        print("Your key traits : Almost superhuman personality.")
