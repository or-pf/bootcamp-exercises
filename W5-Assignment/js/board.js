class Board {
    constructor(height, width) {
        this.boardLayout = this.createBoardCards(height, width);
    }

    createBoardCards(height, width) {
        let cardsArray = [];
        for (let i = 0; i < height; i++) {
            let rowArray = [];
            for (let j = 0; j < width; j++) {
                let card = new Card()
                rowArray.push(card);
            }
            cardsArray.push(rowArray);
        }
        return cardsArray;

        
    }
    /*AssignPics(){

        for (let i= 0; i < (random.length); i++){
            card.picNumber =i;
        }
    }*/
    
}

$('button').click(function() {
    
    $('.output').empty();
    
    for (var a = [0, 1, 2, 3, 4, 5], i = a.length; i--; ) {
        var random = a.splice(Math.floor(Math.random() * (i + 1)), 1)[0];
        $('.output').append('<span>' + random + '</span>');
            // card.picNumber = random;
    }
    
})
.click();