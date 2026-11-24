import javax.sound.sampled.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.io.File;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class AmbientMindful extends JFrame {

    // Store active sound clips so we can stop or loop them cleanly
    private final Map<String, Clip> activeClips = new HashMap<>();

    public AmbientMindful() {
        // 1. Setup the Window
        setTitle("Ambient Mindful - Your Peace Station");
        setSize(420, 320);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());
        getContentPane().setBackground(new Color(45, 45, 50)); // Dark soothing background

        // Stop all audio on exit
        addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                stopAllClips();
            }
        });

        // 2. Add Header
        JLabel header = new JLabel("Focus. Relax. Breathe.", SwingConstants.CENTER);
        header.setFont(new Font("Serif", Font.ITALIC, 24));
        header.setForeground(new Color(200, 230, 255));
        header.setBorder(BorderFactory.createEmptyBorder(20, 0, 15, 0));
        add(header, BorderLayout.NORTH);

        // 3. Create Button Panel
        JPanel buttonPanel = new JPanel();
        buttonPanel.setLayout(new GridLayout(2, 2, 15, 15)); // Grid layout
        buttonPanel.setOpaque(false); // Transparent background
        buttonPanel.setBorder(BorderFactory.createEmptyBorder(15, 20, 15, 20));

        // 4. Add Sound Buttons with robust relative path resolution
        buttonPanel.add(createSoundButton("Rain", "sounds/rain.wav"));
        buttonPanel.add(createSoundButton("Forest", "sounds/forest.wav"));
        buttonPanel.add(createSoundButton("Fire", "sounds/fire.wav"));
        buttonPanel.add(createSoundButton("Ocean", "sounds/ocean.wav"));

        add(buttonPanel, BorderLayout.CENTER);

        // 5. Add Footer
        JLabel footer = new JLabel("Project by Divyansh - Optimized Audio", SwingConstants.CENTER);
        footer.setForeground(Color.GRAY);
        footer.setBorder(BorderFactory.createEmptyBorder(10, 0, 15, 0));
        add(footer, BorderLayout.SOUTH);

        setLocationRelativeTo(null); // Center window on screen
        setVisible(true);
    }

    // Resolves sound files whether run from repository root or the OOJ folder
    private File resolveSoundFile(String relativePath) {
        File direct = new File(relativePath);
        if (direct.exists()) return direct;

        File inOoj = new File("OOJ/AmbientMindful", relativePath);
        if (inOoj.exists()) return inOoj;

        try {
            File codeDir = new File(AmbientMindful.class.getProtectionDomain().getCodeSource().getLocation().toURI());
            if (codeDir.isFile()) codeDir = codeDir.getParentFile();
            File relativeToCode = new File(codeDir, relativePath);
            if (relativeToCode.exists()) return relativeToCode;
        } catch (Exception ignored) {
        }

        return direct; // Fallback to direct path for error message
    }

    // Helper method to create stylish buttons
    private JButton createSoundButton(String label, String relativePath) {
        JButton btn = new JButton(label);
        btn.setFont(new Font("SansSerif", Font.BOLD, 16));
        btn.setFocusPainted(false);
        btn.setBackground(new Color(100, 149, 237));
        btn.setForeground(Color.WHITE);

        btn.addActionListener(e -> toggleSound(btn, relativePath));
        return btn;
    }

    // Logic to play/stop sound with optimized audio compatibility
    private void toggleSound(JButton btn, String relativePath) {
        if (activeClips.containsKey(relativePath)) {
            // STOP sound
            Clip clip = activeClips.remove(relativePath);
            if (clip != null) {
                clip.stop();
                clip.close();
            }
            btn.setBackground(new Color(100, 149, 237)); // Reset color
            btn.setText(btn.getText().replace(" (Playing)", ""));
        } else {
            // PLAY sound
            File soundFile = resolveSoundFile(relativePath);
            if (!soundFile.exists()) {
                JOptionPane.showMessageDialog(this, "Sound file not found: " + relativePath + 
                    "\nSearched at: " + soundFile.getAbsolutePath(), "Missing Audio", JOptionPane.ERROR_MESSAGE);
                return;
            }

            try {
                AudioInputStream rawIn = AudioSystem.getAudioInputStream(soundFile);
                AudioFormat baseFormat = rawIn.getFormat();

                // Ensure format is PCM_SIGNED 16-bit for universal mixer playback
                AudioFormat decodedFormat = new AudioFormat(
                        AudioFormat.Encoding.PCM_SIGNED,
                        baseFormat.getSampleRate(),
                        16,
                        baseFormat.getChannels(),
                        baseFormat.getChannels() * 2,
                        baseFormat.getSampleRate(),
                        false
                );

                AudioInputStream audioIn = AudioSystem.getAudioInputStream(decodedFormat, rawIn);
                Clip clip = AudioSystem.getClip();
                clip.open(audioIn);
                clip.loop(Clip.LOOP_CONTINUOUSLY); // Continuous ambient loop
                clip.start();

                activeClips.put(relativePath, clip);
                btn.setBackground(new Color(60, 179, 113)); // Change to Green
                btn.setText(btn.getText() + " (Playing)");

            } catch (UnsupportedAudioFileException | IOException | LineUnavailableException ex) {
                ex.printStackTrace();
                JOptionPane.showMessageDialog(this, "Error playing audio: " + ex.getMessage(),
                        "Playback Error", JOptionPane.ERROR_MESSAGE);
            }
        }
    }

    private void stopAllClips() {
        for (Clip clip : activeClips.values()) {
            if (clip != null) {
                try {
                    clip.stop();
                    clip.close();
                } catch (Exception ignored) {
                }
            }
        }
        activeClips.clear();
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(AmbientMindful::new);
    }
}
