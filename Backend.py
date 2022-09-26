

def song_URL_to_list(song_url):
    #Convert Delete Spongebob/Campfire Song.html into ("Spongebob","Campfire Song")
    return_list = song_url.replace("Delete ","").replace(".html","").split("/")
    print("Returning: " + return_list[0] + " " + return_list[1])
    return return_list

def song_List_Bar_Chart():
    import pandas as pd
    import matplotlib.pyplot as plt

    chart_data = pd.read_csv("Upcoming Track List.csv")

    plt.bar(chart_data["Song"].values, chart_data["Votes"].values)
    plt.title("Song Distribution")
    plt.xticks(rotation=70)
    plt.subplots_adjust(bottom=0.55)


    plt.savefig("static/Images/Bar Graph.png")
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



def delete_Entire_Track_List():
    with open('Upcoming Track List.csv') as inp:
        data_in = inp.readlines()
    with open('Upcoming Track List.csv', 'w') as outfile:
        outfile.writelines(data_in[0])

def delete_Specific_Song_Track_List(song_to_remove):
    #Delete Spongebob/Campfire Song.html

    artist_and_song_list = song_URL_to_list(song_to_remove)


    with open('Upcoming Track List.csv') as inp:
        data_in = inp.readlines()
    with open('Upcoming Track List.csv', 'w') as outfile:

        for row in data_in:
            if artist_and_song_list[0] in row.split(",")[0] and artist_and_song_list[1] in row.split(",")[1]:
                pass
            else:
               outfile.writelines(row)

    song_List_Bar_Chart()


def read_Entire_Track_List():
    import os

    content = {}
    for root, dirs, files in os.walk("templates"):
        if root != "templates":
            content[root[10:]] = files

    print(content)

    return content

def create_Entry_Track_List(artist, song):
    import pandas as pd

    dataframe = pd.read_csv("Upcoming Track List.csv")

    if artist in dataframe.Artist.values and song in dataframe.Song.values:
        dataframe.loc[(dataframe.Artist == artist) & (dataframe.Song == song),'Votes' ] += 1
    else:
        dataframe.loc[len(dataframe.index)] =[artist,song,1]

    dataframe.to_csv("Upcoming Track List.csv",index=False)

