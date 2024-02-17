function selectionSort(array) {
  const n = array.length;
  for (let i = 0; i < n; i++) {
    let smallest = array[i];
    let smallestIndex = i;
    for (let j = i + 1; j < n; j++) {
      if (array[j] < smallest) {
        smallest = array[j];
        smallestIndex = j;
      }
    }
    swap(array, i, smallestIndex);
  }
  return array;
}

function swap(array, index1, index2) {
  const temp = array[index1];
  array[index1] = array[index2];
  array[index2] = temp;
}