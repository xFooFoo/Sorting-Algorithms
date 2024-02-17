function bubbleSort(array) {
  const n = array.length;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n - i - 1; j++) {
      if (array[j] > array[j+1]) {
        swap(array, j, j+1);
      }
    }
  }
  //console.log(array.join(','))
  return array;
}


function swap(array, index1, index2) {
  const temp = array[index1];
  array[index1] = array[index2]
  array[index2] = temp;
}
//-------------------TEST----------------------------\\
//bubbleSort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]);