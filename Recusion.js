
//EJERCICIO: Usar recusion para imprimir un array 
//que contenga enteros dentro de un rango dado. 

//cuando el numero de inicio (5) sea mayor al n.final (10)
//imprime el array. Sino entrar en bucle. 
function rangeOfNumbers(startNum, endNum) {
    if(startNum >endNum){
    return [];
        }else{
//Tengo una condicion cambiante y como llamé la funcion vuelve a 
//empezar despues de cambiar, evaluando la funcion desde el
//inicio ahora con la nueva condicion. 
    const arr= rangeOfNumbers(startNum+1,endNum);
        arr.unshift(startNum);
        return arr;
    }
    
};
console.log(rangeOfNumbers(5,10));