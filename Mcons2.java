public class Mcons2 {
    String nombre;
    int edad;
    int nota;
    String cargo;
    boolean coordinador;
    //una cosa son los atributos de mi clase(nombre edad)
    //y otra los parametros de un metodo(nom ed)
    public Mcons2(String nombre, int edad, int nota){
    this.nombre = nombre;
    this.edad = edad;
    this.nota= nota;
    }

    public Mcons2(String nombre, int edad, String cargo,boolean coordinador){
        this.nombre= nombre;
        this.edad=edad;
        this.cargo=cargo;
        this.coordinador= coordinador;

    }



    public static void main(String[] args) {
        Mcons2 obj = new Mcons2("Katy", 20, 5);
        //Creo otro objeto ademas de Katy
        Mcons2 obj2 = new Mcons2("Pedro", 35, "docente", true);
        System.out.println(obj.nombre);
        System.out.println(obj.edad);
        System.out.println(obj2.nombre);
    }
}
