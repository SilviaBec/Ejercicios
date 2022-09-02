function miniMax(arr){
    const n=arr.length
    var primero=0;
    segundo=0;
    if (n<=1000000000 && n>=1){
        for (let i of arr.slice(0,4)){
                primero+=i;
        } for(i of arr.slice(arr[arr.length-5],arr[arr.length-1])){
            segundo+=i;
        }
        }console.log(primero+" "+segundo);
    }
miniMax([1,3,5,7,9])
