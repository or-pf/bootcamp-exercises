$(document).ready(function () {
    //adding event listeners
    $('#createUserSubmit').bind('click', checkIfUserExists);
    $('#getUserSubmit').bind('click', showExistingUsers);
});

/*
users = []; //internal array of users
//Method that checks if the user exists in the internal array
checkIfUserExists = function () {
    var userName = $('#username');
    for (var i = 0; i < users.length; i++) {
        //if we found the user, return true and print a message to the user
        if (users[i] === userName.val()) {
            $('.msg').text("User already exists");
            return true;
        }
    }
    //if we haven't found the user, return false
    $('.msg').text("user created successfully");
    users.push(userName.val());
    return false;
};

showExistingUsers = function () {
    $('.msg').text(users);
    return users
};
*/

checkIfUserExists = function () {
    var owner = $('#owner').val();
    var userName = $('#username').val();
    $.ajax({
        type: "POST",
        url: "https://itc-colors.appspot.com/add_user",
        data: {
            owner: owner,
            username: userName
        },
        dataType: "json",
        success: function (responsemsg) {
            if (responsemsg.msg) {
                console.log("worked!")
                console.log(responsemsg)
                $(".msg").empty();
                $(".msg").append(responsemsg.msg)
            }
        },
        error: function (msg) {
            console.log("error");
            $(".msg").empty();
            $(".msg").append(msg)
        },

    });
};

showExistingUsers = function () {
    $.ajax({
        type: "GET",
        url: "https://itc-colors.appspot.com/users",
        data: {
            owner: $('#owner').val()
        },
        dataType: "json",
        success: function (responsemsg) {
            console.log(responsemsg)
            $(".msg").empty();
            $(".msg").append(responsemsg.msg)
            // $(".msg").append(responsemsg[0])
        },
        error: function (msg) {
            console.log("error");
            $(".msg").empty();
            $(".msg").append(msg)
        },
    });
};
