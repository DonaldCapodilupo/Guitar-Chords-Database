/* global console*/
/*jshint esversion: 6 */

function update_Song_List(json_data) {
    var artist = selected_artist = document.getElementById("artist_list").value;
    var song_select_list = document.getElementById("song_list");


    //Clear current list
    function removeOptions() {
        var i, L = song_select_list.options.length - 1;
        for (i = L; i >= 0; i--) {
            song_select_list.remove(i);
        }
    }

    removeOptions();



    for (var song = 0; song < json_data[artist].length; song++) {
        console.log(json_data[artist][song]);
        var el = document.createElement("option");
        el.textContent = json_data[artist][song].replace(".html","");
        el.value = json_data[artist][song].replace(".html","");
        song_select_list.appendChild(el);
    }
}