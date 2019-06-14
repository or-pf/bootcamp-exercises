class Board {
    constructor(height, width) {
        this.cards = this.createBoardCards(height, width);
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

    randomizeCards() {

        cardsArray.forEach(card => {
            card.picNumber = Math.floor((Math.random() * 12) + 1);
        });
        // let randomNum = Math.floor((Math.random() * 12) + 1);
        // this.picNumber = randomNum

    }
}