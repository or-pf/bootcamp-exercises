const HEIGHT = 3;
const WIDTH = 4;

class Game {
    constructor() {
        this.board = new Board(HEIGHT, WIDTH);
    }

    randomizeCards() {
        cardsArray.forEach(card => {
            card.picNumber = Math.floor((Math.random() * 12) + 1);
        });

    }
}