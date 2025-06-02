

public class main {

    public static void main(String[] args) {
        System.out.println("Hello World!");
        System.out.println(returnJava("file"));
        System.out.println(sum(5, 1));
    }

    public static String returnJava (String word) {
        return word + ".java";
    }

    public static int sum (int a, int b) {
        return a + b;
    }
}