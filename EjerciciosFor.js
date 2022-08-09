//1. Realice un programa que enumere los paises de la siguiente lista
paises = ['Canada', 'USA', 'Mexico', 'Australia']
for(i in paises){
    console.log(i,paises[i])
}
//2.Crear un ciclo for que cuente de 0 a 100
for (i=0;i<=100;i++){
    console.log(i)
}
//3. Haz una tabla de multiplicar utilizando el ciclo for
for (i=0;i<=10;i++){
    console.log(i+" x 5 = "+i*5)
}
// 4. Imprima los números del 1 a 10 al revés utilizando el ciclo for
for (i=10; i>=0 && i<=10;i--){
    console.log(i)

}

//5. Crear un bucle que cuente todos los números pares hasta el 100
for (i=0;i<=100;i=i+2){
    console.log(i)
}

//6. Dado un número, cuente el número total de dígitos de un número
var numero= 4587965842
var numText= numero.toString();
console.log(numText.length);
for(i in numText){
    console.log(i)
}



//node cicloFor.js