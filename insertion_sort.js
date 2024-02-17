function insertionSort(array) {
  const n = array.length;
  for (let i = 0; i < n; i++) {
    for (let j = i; j > 0; j--) {
      if (array[j] < array[j - 1]) {
        swap(array, j, j -1);
      }
      else {
        break;
      }
    }
  }
  return array;
}

function swap(array, index1, index2) {
  const temp = array[index1];
  array[index1] = array[index2];
  array[index2] = temp;
}