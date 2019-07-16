$.ajax({
    type: "GET",
    url: "/get_images",
}).done(function (data) {
    var images = JSON.parse(data);
    images.forEach(element => {
        var img = document.createElement("img");
        img.src = element;
        document.body.appendChild(img);
    });
});