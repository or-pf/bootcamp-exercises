let expect = require('chai').expect;
let assert = require('chai').assert;

var candyStore = {
    candies: [
        {
            name: "mint gum",
            id: "as12f",
            price: 2,
            amount: 2
        },
        {
            name: "twix",
            id: "5hd7y",
            price: 5,
            amount: 4
        },
    ],
    cashRegister: 200
}

function getCandy(candyStore, id) {
    return candyStore.candies.find(x => x.id === id);
}

function getPrice(candyStore, id) {
    return getCandy(candyStore, id).price;
}

function addCandy(candyStore, id, name, price) {
    const candy = getCandy(candyStore, id);
    if (candy) {
        candy.amount++;
    } else {
        candyStore.candies.push({
            name: name,
            id: id,
            price: price,
            amount: 1
        });
    }
}

function buy(candyStore, id) {
    var candy = getCandy(candyStore, id);
    if (candy.amount > 0) {
        candyStore.cashRegister += candy.price;
        candy.amount--;
    }
}

