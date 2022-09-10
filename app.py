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


    else:
        from Backend import create_Artist_and_Song_Dict
        song_data = create_Artist_and_Song_Dict()
        print(song_data)
        return render_template("User-Vote.html", data=song_data)









if __name__ == '__main__':
    app.run()
