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


it('should return a candy info', function(){
expect(getCandy(candyStore, "as12f")).to.deep.equal({name:"mint gum", id:"as12f", price:2, amount:2});
});

it('should return the price according to a given id', function () {
    expect(getPrice(candyStore, "as12f")).to.equal(2);
    expect(getPrice(candyStore, "5hd7y")).to.equal(5);
});

it('should add a new candy to the store', function () {
    addCandy(candyStore, "mnm11", "m&m", 3.5);
     expect(getCandy(candyStore, "mnm11")).to.deep.equal({name:"m&m", id:"mnm11", price:3.5, amount:1});
});

it('should reduce the candy amount by 1', function () {
    const candyId = "as12f";
    const candyAmount = getCandy(candyStore, candyId).amount;
    
    buy(candyStore, candyId);
    
    expect(getCandy(candyStore, candyId).amount).to.equal(candyAmount - 1);
});

