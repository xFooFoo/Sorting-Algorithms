function quickSort(array) {
  const n = array.length;
  if ( n < 2) {
    return array;
  }

  const pivotVal = array[Math.floor(n/2)];
  // move pivot to the end in order to track index & swap ptrs
  array[Math.floor(n/2)] = array[n - 1];
  array[n - 1] = pivotVal;

  let l = 0;
  for (let i = 0; i < n - 1; i++) {
    if (array[i] < pivotVal) {
      if (i > l) {
        swap(array, l, i);
      }
      // Move the swap ptr to the right,
      l++;
    }
    // Otherwise this l ptr pts to a number greater than the pivot to be swapped
    // when we find a number smaller than the pivot in future runs
  }

  // swap l ptr with pivot, pivot is sorted at position l
  array[n-1] = array[l];
  array[l] = pivotVal;
  
  // Recursively quicksort L & R of the pivot
  const arrayL = quickSort(array.slice(0, l));
  const arrayR = quickSort(array.slice(l + 1));

  
  return [... arrayL, array[l], ...arrayR];
}

function swap(array, index1, index2) {
  const temp = array[index1];
  array[index1] = array[index2];
  array[index2] = temp;
}

// --------- TESTING -----------
quickSort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]) 
console.log(quickSort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]));