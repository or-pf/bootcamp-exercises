$(document).ready(function () {
    $('#get-images').bind('click', showImages);
});

showImages = function () {
    $.ajax({
        type: "GET",
        url: "http://itc-colors.appspot.com/get_images",
    
        dataType: "json",
        success: function (responsemsg) {
            console.log(responsemsg)
            $("#zero").css("background-image", `url(${responsemsg[0]})`);
            $("#one").css("background-image", `url(${responsemsg[1]})`);
            $("#two").css("background-image", `url(${responsemsg[2]})`);
            $("#three").css("background-image", `url(${responsemsg[3]})`);
            $("#four").css("background-image", `url(${responsemsg[4]})`);
            $("#five").css("background-image", `url(${responsemsg[5]})`);
            $("#six").css("background-image", `url(${responsemsg[6]})`);
      
        },
        error: function (msg) {
            console.log("error");
        },
    });
};