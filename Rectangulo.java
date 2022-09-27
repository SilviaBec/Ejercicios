//a la clase padre e hija les quite el modificador
//extends indica que es una hija de otra clase
class Rectangulo extends Area{ //clase hija
    //atributo propio de mi clase
    private String figura ="Rectángulo";
    double area(){
        return dimension1*dimension2;
    }
    
    public static void main(String[] args) {
        Rectangulo obj1 = new Rectangulo();
        System.out.println(obj1.figura);
        obj1.mostrarDimensiones();
        System.out.println(obj1.area());
    }

    
}
