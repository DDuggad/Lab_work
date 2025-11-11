import java.util.Scanner;

class Book {
    String name, author;
    double price;
    int num_pages;

    Book(String n, String a, double p, int pages) {
        name = n; author = a; price = p; num_pages = pages;
    }

    public String toString() {
        return "Name: " + name + ", Author: " + author + ", Price: " + price + ", Pages: " + num_pages;
    }
}

public class BookDemo {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.print("Enter number of books: ");
        int n = s.nextInt();
        Book[] b = new Book[n];

        for (int i = 0; i < n; i++) {
            System.out.println("Enter Name, Author, Price, Pages for book " + (i + 1) + ":");
            b[i] = new Book(s.next(), s.next(), s.nextDouble(), s.nextInt());
        }

        System.out.println("\nBook Details:");
        for (Book x : b) System.out.println(x);
        s.close();
    }
}