

public class ArrBidim {
    public static void main(String[] args) {
        
        int [][] matriz ={{45,25,89},{26,32,77}};
        // 45 25 89
        // 26 32 77
    //Recorrido de array bidimensional con for
    //matriz.length es 2 : {45,25,89} uno y {26,32,77} es el dos, luego pongo otro for para recorrer
    //lo de adentro del corchete grande anido for
    for (int i=0; i<matriz.length; i++){
        //matriz[i].length me va a dar 3 (0,1,2) que corresponde a  {45,25,89}
        for(int j =0; j<matriz[i].length;j++){
            System.out.println(matriz[i][j]);

        }
    
    }

System.out.println("-----------------con for each------------");
    //Recorrido de array bidimensional con for each
    //el elemnto es un array de enteros tengo (2) cada uno con 3 elemntos por eso int[]
for(int[] x:matriz){ 
    for (int y: x){
        System.out.println(y);
    }
}

    }
    
//y itera a x 

}
