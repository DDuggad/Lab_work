import javax.sound.sampled.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class AmbientMindful extends JFrame {

    // Store our active sound clips so we can stop them later
    private Map<String, Clip> activeClips = new HashMap<>();

    public AmbientMindful() {
        // 1. Setup the Window
        setTitle("Ambient Mindful - Your Peace Station");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());
        getContentPane().setBackground(new Color(45, 45, 50)); // Dark soothing background

        // 2. Add Header
        JLabel header = new JLabel("Focus. Relax. Breathe.", SwingConstants.CENTER);
        header.setFont(new Font("Serif", Font.ITALIC, 24));
        header.setForeground(new Color(200, 230, 255));
        header.setBorder(BorderFactory.createEmptyBorder(20, 0, 20, 0));
        add(header, BorderLayout.NORTH);

        // 3. Create Button Panel
        JPanel buttonPanel = new JPanel();
        buttonPanel.setLayout(new GridLayout(2, 2, 15, 15)); // Grid layout
        buttonPanel.setOpaque(false); // Transparent background
        buttonPanel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));

        // 4. Add Sound Buttons
        // Make sure you have rain.wav, forest.wav, fire.wav in a "sounds" folder!
        buttonPanel.add(createSoundButton("Rain", "sounds/rain.wav"));
        buttonPanel.add(createSoundButton("Forest", "sounds/forest.wav"));
        buttonPanel.add(createSoundButton("Fire", "sounds/fire.wav"));
        buttonPanel.add(createSoundButton("Ocean", "sounds/ocean.wav")); // Optional

        add(buttonPanel, BorderLayout.CENTER);

        // 5. Add Footer
        JLabel footer = new JLabel("Project by Divyansh", SwingConstants.CENTER);
        footer.setForeground(Color.GRAY);
        footer.setBorder(BorderFactory.createEmptyBorder(10, 0, 10, 0));
        add(footer, BorderLayout.SOUTH);

        setLocationRelativeTo(null); // Center window on screen
        setVisible(true);
    }

    // Helper method to create stylish buttons
    private JButton createSoundButton(String label, String filePath) {
        JButton btn = new JButton(label);
        btn.setFont(new Font("SansSerif", Font.BOLD, 16));
        btn.setFocusPainted(false);
        btn.setBackground(new Color(100, 149, 237));
        btn.setForeground(Color.WHITE);

        btn.addActionListener(e -> toggleSound(btn, filePath));
        return btn;
    }

    // Logic to play/stop sound
    private void toggleSound(JButton btn, String filePath) {
        if (activeClips.containsKey(filePath)) {
            // STOP sound
            Clip clip = activeClips.get(filePath);
            clip.stop();
            clip.close();
            activeClips.remove(filePath);
            btn.setBackground(new Color(100, 149, 237)); // Reset color
            btn.setText(btn.getText().replace(" (Playing)", ""));
        } else {
            // PLAY sound
            try {
                File soundFile = new File(filePath);
                if (!soundFile.exists()) {
                    JOptionPane.showMessageDialog(this, "File not found: " + filePath);
                    return;
                }

                AudioInputStream audioIn = AudioSystem.getAudioInputStream(soundFile);
                Clip clip = AudioSystem.getClip();
                clip.open(audioIn);
                clip.loop(Clip.LOOP_CONTINUOUSLY); // Loop forever
                clip.start();

                activeClips.put(filePath, clip);
                btn.setBackground(new Color(60, 179, 113)); // Change to Green
                btn.setText(btn.getText() + " (Playing)");

            } catch (UnsupportedAudioFileException | IOException | LineUnavailableException ex) {
                ex.printStackTrace();
                JOptionPane.showMessageDialog(this, "Error playing sound: " + ex.getMessage());
            }
        }
    }

    public static void main(String[] args) {
        // Run the UI
        SwingUtilities.invokeLater(AmbientMindful::new);
    }
}