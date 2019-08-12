$("#jpost").click(function () {

    $.ajax({
        type: "GET",
        url: "/rss/jpost",
    }).done(function (data) {

        var news = JSON.parse(data);
        news.forEach(element => {
            let title = $("<li/>");
            title.text(element.title);
            let link = $("<a/>");
            link.attr("href", `${element.link}`);
            link.text(" For the full story click here");  
            title.append(link);

            $("#jpost_span").append(title);
        });

    });
});

$("#themarker").click(function () {

    $.ajax({
        type: "GET",
        url: "/rss/themarker",
    }).done(function (data) {

        var news = JSON.parse(data);
        news.forEach(element => {
            let title = $("<li/>");
            title.text(element.title);
            let link = $("<a/>");
            link.attr("href", `${element.link}`);
            link.text(" For the full story click here");  
            title.append(link);

            $("#themarker_span").append(title);
        });

    });
});
