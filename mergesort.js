
function mergesort(data) {
    //base case
    if (data.length <= 1) {
        //console.log(data)
        return data
    }
    //const on medianIndex, L/R Array is crucial to prevent it from being changed in subseqeunt msort calls
    const medianIndex = Math.floor(data.length / 2)
    //console.log("MedianIndex: " + data.length/2)
    //keeps splitting then eventually becomes a single element
    const leftArray = mergesort(data.slice(0, medianIndex))
    const rightArray = mergesort(data.slice(medianIndex))
    //console.log("leftArray: " + leftArray.toString())
    //console.log("rightArray: " + rightArray.toString())
    //starts merging L&R together once everything's split up
    return merge(leftArray, rightArray)
}
    

function merge(leftArray, rightArray) {
    //compare left-most element from each array and put in new list
    mergedArray = []
    let [l, r] = [0, 0] //index for left / right array
    while (l < leftArray.length && r < rightArray.length) {
        if (leftArray[l] < rightArray[r]) {
            mergedArray.push(leftArray[l])
            l += 1
        }
        else { //covers case where both values are the same
            mergedArray.push(rightArray[r])
            r += 1
        }
    } 
    //Once one array is fully in the mergedArray, append the rest of the other array
    while (l < leftArray.length) {
        mergedArray.push(leftArray[l])
        l += 1
    }
    while (r < rightArray.length) {
        mergedArray.push(rightArray[r])
        r += 1
    }
    console.log("mergedArray: " + mergedArray)
    return mergedArray
}

function arraysAreEqual(arr1, arr2) {
    if (arr1.length !== arr2.length) {
        return false;
    }

    for (let i = 0; i < arr1.length; i++) {
        if (arr1[i] !== arr2[i]) {
            return false;
        }
    }

    return true;
}

//-------------------  TESTING WITH RANDOM INPUT  ---------------------\\
randomNumbers = [];
for (i = 0; i < 100; i++) {
    randomNumber = Math.floor(Math.random() * 1001);
    randomNumbers.push(randomNumber);
}

//console.log(randomNumbers)
original = randomNumbers
answer = original.sort(function (a, b) {
    return a - b; // for ascending order instead of alphabetical order
})
output = mergesort(original)

if (arraysAreEqual(answer, output)) {
    console.log("Mergesort has sorted successfully")
} else {
    console.log("Mergesort has sorted UNSUCCESSFULLY")
    //console.log(answer)
    //console.log(output)
}

