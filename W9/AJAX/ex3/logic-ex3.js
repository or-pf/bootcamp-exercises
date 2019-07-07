$(document).ready(function () {
    setInterval(checking, 3000)
});
let checking = function () {
    $.ajax({
        type: "GET",
        url: "https://itc-colors.appspot.com/aircon/state",
        dataType: "json",
        success: function (response) {
            if (response.state === "on") {
                $("#AC-On").css("display", "block");
                $("#AC-Off").css("display", "none");
                $("#mode").text("mode is " +response.mode);
                $("#temp").text("temperture is "+response.temp);
            } else {
                $("#AC-On").css("display", "none");
                $("#AC-Off").css("display", "block");
                $("#mode").text("AC is not working");
                $("#temp").text("");
              
            }

        }
    });
}
