

public class FeachArreglos {
    public static void main(String[] args) {
       //Esto de abajo ya es un array vacio
        String [] ciudades= {"Cali", "Medellín", "Monteria", "Bogotá"};
        System.out.println(ciudades[2]);
        System.out.println(ciudades.length);
        //Recorrer array con for clasico
        for (int i=0;i<ciudades.length;i++){
            System.out.println(ciudades[i]);
        }
        //Recorrer arreglo confor each
System.out.println("------------con for each--------");
        for(String city: ciudades){
            System.out.println(city);

        }

        int[] numeros={45,21,80,10,56};
        for (int num:numeros){
            System.out.println(num);

        }

    }   
    
}
