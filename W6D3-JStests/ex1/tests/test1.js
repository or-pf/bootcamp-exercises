let expect = require('chai').expect;
let assert = require('chai').assert;


function palindrome(str) {
    var re = /[\W_]/g;
    var lowRegStr = str.toLowerCase().replace(re, '');
    var reverseStr = lowRegStr.split('').reverse().join(''); 
    return reverseStr === lowRegStr;
  }


   it('should check if a string is a palindrome', function(){
    assert.equal(palindrome("wow"), true, "this is a palindrome");
});