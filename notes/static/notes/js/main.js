var converter = new showdown.Converter();

var noteHead = document.getElementById("note-hidden-head"),
    noteBody = document.getElementById("note-hidden-body");

var containerHead = document.getElementById("note-head"),
    containerBody = document.getElementById("note-body");


var generatedHeadHtml = converter.makeHtml(noteHead.innerText),
    generatedBodyHtml = converter.makeHtml(noteBody.innerText);


containerHead.innerHTML = generatedHeadHtml;
containerBody.innerHTML = generatedBodyHtml;
