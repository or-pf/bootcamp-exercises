let expect = require('chai').expect;
let assert = require('chai').assert;




function transposeArray(arr) {
    var transArray = [];
    for (var i=0; i<arr.length; i++) {
      var rowLen = arr[i].length;
      transArray.push([]);
      for (var j=0; j<rowLen; j++) {
        transArray[i].push(arr[j][i]);
      }
    }
    return transArray;
  }

it('should return a transpose array', function(){
    expect(transposeArray([[1,2],[1,2]])).to.deep.equal([[1,1],[2,2]]);
    });



// function transpose(matrix){
//     var result = new Array (matrix[0].length);
//     for (var i= 0; i < result.length; i++){
//         result[i] = new Array (matrix.length);
//         for (var j=0; j< result[i].length; j++){
//             result[i][j]= matrix[j][i]; 
//         }
//     }
//     return result;
// }


// function transposeArray(array, arrayLength){
//     var newArray = [];
//     for(var i = 0; i < array.length; i++){
//         newArray.push([]);
//     };

//     for(var i = 0; i < array.length; i++){
//         for(var j = 0; j < arrayLength; j++){
//             newArray[j].push(array[i][j]);
//         };
//     };

//     return newArray;
// }
