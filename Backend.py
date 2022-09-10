

class ListDisplay:
    def __init__(self, listToDisplay):
        self.listToDisplay = listToDisplay

    def displayList(self, addExit=True):
        print("Which option would you like to choose")
        s = 1  # This is the counter to display in the output string.
        for i in self.listToDisplay:  # Loop through the menu options
            print(str(s) + ") " + i)  # Display all of the items in the list as a menu
            s += 1
        if addExit:
            print(str(s) + ") Exit" )
            s += 1
        userChoice = int(input(">"))  # Prompt the user to enter a number
        # Reruns the prompt if the user enters a number that is to big
        if userChoice == len(self.listToDisplay)+1:
            exit()
        while userChoice > len(self.listToDisplay):
            print("Invalid data. Please enter a valid number")
            print()
            print("Which option would you like to choose")
            s = 1  # This is the counter
            for i in self.listToDisplay:  # Loop through the menu options
                print(str(s) + ") " + i)  # Display all of the items in the list as a menu
                s += 1
            if addExit:
                print(str(s) + ") Exit")
                s += 1
            userChoice = int(input(">"))
            if userChoice == len(self.listToDisplay) + 1:
                exit()
        # Closes the program if the user selects "Exit"
        # At some point I would like it to step back one function
        if userChoice == (s - 1) and self.listToDisplay[-1] == "Exit":
            print("Exiting")
            exit()
        # Converts the users numerical entry into the string version of the option selected.
        userChoiceFINAL = self.listToDisplay[(int(userChoice) - 1)]
        # Return the variable
        return userChoiceFINAL



def song_List_Bar_Chart():
    import pandas as pd
    import matplotlib.pyplot as plt

    chart_data = pd.read_csv("Upcoming Track List.csv")

    plt.bar(chart_data["Song"].values, chart_data["Votes"].values)
    plt.title("Song Distribution")
    plt.xticks(rotation=70)


    plt.savefig("Bar Graph.png")
    plt.show()



def update_Song_List(user_song):
    import csv
    reader = csv.DictReader(open('Upcoming Track List.csv'))
    result = {}




    for row in reader:
        result[row["Song"]] =  int(row["Votes"])


    try:
        result[user_song] += 1
    except KeyError:
        result[user_song] = 1


    with open("Upcoming Track List.csv", "w", newline='') as cvs_file:
        spamwriter = csv.writer(cvs_file, delimiter=',')
        spamwriter.writerow(["Song","Votes"])
        for key, value in result.items():
            spamwriter.writerow([key,value])



def customer_Select_Song():
    import os

    song_list = os.listdir("templates")
    song_list.remove("Song-Dashboard.html")


    user_list = ListDisplay(song_list)
    user_choice = user_list.displayList(True)


    update_Song_List(user_choice)



#Uneeded once flask is set up, artist will view a constantly updating web page
def artist_Retrieve_Song():
    with open("Upcoming Track List.csv", "r") as f:
        current_track_list = f.read().splitlines()[1:]
    for song in current_track_list:
        song = song.split(".",1)[0]
        print(song)

    return current_track_list



def artist_Clear_Entire_List():
    with open('Upcoming Track List.csv') as inp:
        data_in = inp.readlines()
    with open('Upcoming Track List.csv', 'w') as outfile:
        outfile.writelines(data_in[0])

def artist_Clear_Specific_Song(song_to_remove):
    with open('Upcoming Track List.csv') as inp:
        data_in = inp.readlines()
    with open('Upcoming Track List.csv', 'w') as outfile:

        for row in data_in:
           if song_to_remove not in row and row != "Song,Votes":
               outfile.writelines(row)

    song_List_Bar_Chart()


def create_Artist_and_Song_Dict():
    import os

    content = {}
    for root, dirs, files in os.walk("templates"):
        if root != "templates":
            content[root[10:]] = files

    print(content)

    return content


#customer_Select_Song()
#artist_Retrieve_Song()
#song_List_Bar_Chart()
#artist_Clear_Entire_List()
#artist_Clear_Specific_Song("Let It Roll.html")
#create_Artist_and_Song_Dict()