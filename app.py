from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/Song-Dashboard', methods=['GET', 'POST'])
def song_Dashboard():
    return render_template("Song-Dashboard.html")



@app.route('/', methods=['GET', 'POST'])
def user_Add_Song():
    if request.method == "POST":
        if request.form['submit_button'] == 'view_results':
            return redirect(url_for("song_Dashboard"))
        if request.form['submit_button'] == 'submit_song':
            from Backend import read_Entire_Track_List,update_Song_List

            song_data = read_Entire_Track_List()

            update_Song_List()


            return render_template("User-Vote.html", data=song_data,confirmation=True)


    else:
        from Backend import read_Entire_Track_List
        song_data = read_Entire_Track_List()
        print(song_data)
        return render_template("User-Vote.html", data=song_data)









if __name__ == '__main__':
    app.run()
