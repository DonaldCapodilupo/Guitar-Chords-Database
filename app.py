from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/Song-Dashboard', methods=['GET', 'POST'])
def song_Dashboard():
    from Backend import song_List_Bar_Chart, artist_Retrieve_Song
    song_List_Bar_Chart()
    track_list = artist_Retrieve_Song()
    if request.method == "POST" :
        print(request.form["submit_button"])
        #Go Back
        if request.form['submit_button'] == "Go Back":
            return redirect(url_for("user_Add_Song"))
        #Show Chords and Lyrics
        if "Delete" not in  request.form['submit_button']:
            song_information =request.form['submit_button'].replace("[","").replace("]","").replace("'","").split(",")
            song_to_play =  song_information[0] +"/" + song_information[1].lstrip() + ".html"
            return render_template("Song-Dashboard.html", current_tracklist=track_list, song_information=song_to_play)
        #Delete Song
        else:
            from Backend import delete_Specific_Song_Track_List

            delete_Specific_Song_Track_List(request.form["submit_button"])

            song_List_Bar_Chart()
            track_list = artist_Retrieve_Song()

            return render_template("Song-Dashboard.html", current_tracklist=track_list)
    if request.method == "GET":
        return render_template("Song-Dashboard.html", current_tracklist=track_list)



@app.route('/Song-Results', methods=['GET', 'POST'])
def song_Results():
    from Backend import song_List_Bar_Chart, artist_Retrieve_Song
    song_List_Bar_Chart()
    track_list = artist_Retrieve_Song()
    if request.method == "POST":
        return redirect(url_for("user_Add_Song"))
    if request.method == "GET":
        return render_template("Song-Vote-Results.html", current_tracklist=track_list)



@app.route('/', methods=['GET', 'POST'])
def user_Add_Song():
    if request.method == "POST":
        if request.form['submit_button'] == 'view_results':
            return redirect(url_for("song_Results"))
        if request.form['submit_button'] == 'submit_song':
            from Backend import read_Entire_Track_List, create_Entry_Track_List

            song_data = read_Entire_Track_List()
            print(request.form["artist_list"])
            print(request.form["song_list"])

            create_Entry_Track_List(request.form["artist_list"], request.form["song_list"])

            return render_template("User-Vote.html", data=song_data, confirmation=[request.form["artist_list"],
                                                                                   request.form["song_list"]])


    else:
        from Backend import read_Entire_Track_List
        song_data = read_Entire_Track_List()
        print(song_data)
        return render_template("User-Vote.html", data=song_data)


if __name__ == '__main__':
    app.run()
