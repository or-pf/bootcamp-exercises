$(document).ready(function () {
    $('#addColorSubmit').bind('click', checkIfColorExists);
    $('#getColorSubmit').bind('click', showExistingColors);
});

checkIfColorExists = function () {
    var newColor = $('#colorInput').val();

    $.ajax({
        type: "POST",
        url: "https://jsonplaceholder.typicode.com/todos",
        data: {
            color: newColor
        },
        dataType: "json",
        success: function (responsemsg) {
            for (let i = 0; i < responsemsg.lenght; i++){
                if (responsemsg[i].color === newColor){
                    console.log("color already exsist")
                }
            }
            if (responsemsg.color) {
                console.log("worked!")
                console.log(responsemsg)
                $(".msg").empty();
                $(".msg").append(responsemsg.color)
                $("#colorDisplay").css("background-color", responsemsg.color);
            }
        },
        error: function (msg) {
            console.log("error");
            $(".msg").empty();
            $(".msg").append(msg)
        },

    });
};

showExistingColors = function () {
    $.ajax({
        type: "GET",
        url: "https://jsonplaceholder.typicode.com/todos",
        dataType: "json",
        success: function (responsemsg) {
            console.log(responsemsg)
            $(".msg").empty();
            for (let i = 0; i < responsemsg.lenght; i++) {
                $(".msg").append(responsemsg[i])
            }
        },
        error: function (msg) {
            console.log("error");
            $(".msg").empty();
            $(".msg").append(msg)
        },
    });
};

