function kangaroo(x1, v1, x2, v2){
    for(var i=0;i<101;i++ ){
        if(x1+(v1*i) == x2+(v2*i)){
            return 'YES'
        } 
        else{
            return 'NO'
        }
    }
    
}

console.log(kangaroo(0,2,5,3))
