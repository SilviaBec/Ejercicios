import java.util.Scanner;
public class Ejercicio1 {
            //creo atributos o variables de la clase
        private String nombre;
        private Double estatura;
        private Scanner sc; // Creo objeto de la clase scaner
        
        //en este metodo que cree abajo le pedire al user, name y height
        public void capturar(){
            sc = new Scanner(System.in);
            System.out.println("Digite el nombre ");
            nombre = sc.nextLine();
            System.out.println("Digite su estatura: ");
            estatura = sc.nextDouble();
        }

        public void imprimir (){
            System.out.println("Nombre: "+nombre);
            System.out.println("Estatura: "+estatura);


        }


        public void clasificar(){
            if(estatura>1.60){
                System.out.println("Aceptado");
            } else{
                System.out.println("No aceptado");
            }
        }


        public static void main(String[] args) {
            Ejercicio1 objeto1;
            objeto1 = new Ejercicio1();
            // es igual a ponerlo en este formato:  Scanner nombreobj = new Scannesystem.inr
            objeto1.capturar();
            objeto1.imprimir();
            objeto1.clasificar();
        }
    }

