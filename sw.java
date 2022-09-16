import java.util.Scanner;

public class sw {
    public static void main(String[] args) {
        //Mi objeto se llama sc
    Scanner sc= new Scanner(System.in);
    System.out.println("Digite el numero de mes (1-4): ");
    int mes = sc.nextInt();
    sc.close();
    String mesLetra ="";
    switch(mes){
        case 1:
        mesLetra ="Enero";
        break;
        case 2:
        mesLetra ="Febrero";
        break;
        case 3:
        mesLetra ="Marzo";
        break;
        case 4:
        mesLetra ="Abril";
        break;
        default:
        System.out.println("Otro mes u otra cosa");
    }
    System.out.println("El mes es "+mesLetra);
    String color ="Amarillo";
    switch (color){
        case "Amarillo":
        System.out.println("Prevención");
        break;
        case "Rojo":
        System.out.println("Deténgase");
        case "Verde":
        System.out.println("Avance");
        break;
    }
        
    }
}
