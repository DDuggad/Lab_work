import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class DisplayUI implements ActionListener {
    JFrame f;
    JTextField t1, t2, t3;
    JButton b;

    DisplayUI() {
        f = new JFrame("Division App");
        t1 = new JTextField(10);
        t2 = new JTextField(10);
        t3 = new JTextField(10);
        b = new JButton("Divide");
        
        f.setLayout(new FlowLayout());
        f.add(new JLabel("Num1:")); f.add(t1);
        f.add(new JLabel("Num2:")); f.add(t2);
        f.add(new JLabel("Result:")); f.add(t3);
        f.add(b);
        
        b.addActionListener(this);
        f.setSize(300, 200);
        f.setVisible(true);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    public void actionPerformed(ActionEvent e) {
        try {
            int n1 = Integer.parseInt(t1.getText());
            int n2 = Integer.parseInt(t2.getText());
            t3.setText(String.valueOf(n1 / n2));
        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(f, "Please enter integers only.");
        } catch (ArithmeticException ex) {
            JOptionPane.showMessageDialog(f, "Cannot divide by Zero.");
        }
    }

    public static void main(String[] args) {
        new DisplayUI();
    }
}
