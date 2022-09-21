import java.util.Scanner;
public class Ejercicio3 {

    public void capturaDatos(){
        Scanner numeros = new Scanner(System.in);
        System.out.println("Ingrese 1er valor: ");
        float valor1= numeros.nextFloat();
        System.out.println("Ingrese 2ndo valor: ");
        float valor2 = numeros.nextFloat();
        float suma, resta, multi;
        suma= suma(valor1, valor2);
        resta = resta(valor1, valor2);
        multi = mul(valor1, valor2);
        System.out.println(suma);
        System.out.println(resta);
        System.out.println(multi);
        
    }
    public float suma(float v1, float v2){
        float suma = v1+v2;
        return suma;
    }
    public float resta(float v1, float v2){
        float resta = v1-v2;
        return resta;
    }
    public float mul(float v1, float v2){
        float multi = v1*v2;
        return multi;  
    }
    public static void main(String[] args) {
        Ejercicio3 operaciones = new Ejercicio3();
        operaciones.capturaDatos();
    }
}
