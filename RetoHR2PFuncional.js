
function miniMax(arr){
    const n=arr.length
    if (n<=1000000000 && n>=1){
        arr.sort(function(a, b) {return a - b;});
    const resultado1 = arr.slice(0,4).reduce((primero,i) => primero+i,0)
    const resultado2 = arr.slice(1,arr[arr.length-1]).reduce((segundo,i) => segundo+i,0)
        console.log(resultado1+" "+resultado2)       
}
}

miniMax([7,69,2,221,8974]) 


