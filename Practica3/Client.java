import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;
import java.util.ArrayList;
import java.awt.*;
import javax.swing.*;
import java.awt.event.*;

public class Client {
    static BufferedReader in;
    JFrame intro;
    JFrame principal;
    MySocket sc;
    String username;
    JTextField usernamefield;
    JTextArea messages;
    String s_message;
    JTextField msg_send;
    JTextArea usr_TextArea;
    JTextArea incorrect_usr;
    JList<String> list;
    DefaultListModel<String> dlmodel;
    List<String> lista;
    int i;

    public Client() {
        super();
        this.sc = new MySocket("localhost", 2345);
        this.intro = new JFrame("ChatApp");
        this.principal = new JFrame("ChatApp");
        this.dlmodel = new DefaultListModel<String>();
        this.list = new JList<String>(this.dlmodel);
        this.lista = new ArrayList<>();
    }

    public void initChat() {
        intro.setLayout(new BorderLayout(2, 2));
        intro.getRootPane().setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        intro.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel user = new JPanel();
        user.setLayout(new BoxLayout(user, BoxLayout.LINE_AXIS));
        usernamefield = new JTextField(25);
        JButton button = new JButton("Entrar");
        button.addActionListener(new enterUsername());
        JLabel uflabel = new JLabel("Nom d'usuari:  ");

        user.add(uflabel);
        user.add(usernamefield);
        user.add(Box.createHorizontalStrut(25));
        user.add(button);

        intro.add(user, BorderLayout.CENTER);
        intro.pack();
        intro.setLocationRelativeTo(null);
        intro.setVisible(true);
    }

    public void chatView() {
        principal.setLayout(new BorderLayout(2, 2));
        principal.getRootPane().setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        principal.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        principal.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                sc.write_line("Exit?%" + username);
            }
        });

        JPanel chat_Panel = new JPanel();
        chat_Panel.setLayout(new BoxLayout(chat_Panel, BoxLayout.PAGE_AXIS));
        messages = new JTextArea(25, 25);
        messages.setEditable(false);
        chat_Panel.add(new JScrollPane(messages));
        messages.setLineWrap(true);
        messages.setWrapStyleWord(true);

        JPanel msg_Panel = new JPanel();
        msg_Panel.setLayout(new BoxLayout(msg_Panel, BoxLayout.LINE_AXIS));
        msg_send = new JTextField(20);
        JButton sendbutton = new JButton("Envia");
        sendbutton.addActionListener(new sendMessage());
        JLabel slabel = new JLabel("Missatge:  ");
        msg_Panel.add(slabel);
        msg_Panel.add(msg_send);
        msg_Panel.add(sendbutton);

        JPanel usr_Panel = new JPanel();
        usr_Panel.setLayout(new BoxLayout(usr_Panel, BoxLayout.PAGE_AXIS));
        JScrollPane scrollpanel = new JScrollPane(list);
        scrollpanel.setPreferredSize(new Dimension(100, 50));
        usr_Panel.add(scrollpanel);

        principal.add(chat_Panel, BorderLayout.LINE_START);
        principal.add(usr_Panel, BorderLayout.LINE_END);
        principal.add(msg_Panel, BorderLayout.PAGE_END);
        principal.pack();
        principal.setLocationRelativeTo(null);
        principal.setVisible(true);
    }

    public class enterUsername implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            username = usernamefield.getText();
            if (username.length() > 0) {
                sc.write_line(username);
                System.out.println("User "+username);
                String connected = sc.read_line();
                if (connected.equals("Exist")) {
                    System.out.println("El usuari ja existeix");
                    JOptionPane.showMessageDialog(intro, "Usuari ja existeix", "Error", JOptionPane.ERROR_MESSAGE);

                } else {
                    llistaActualitzada("11" + username);
                    intro.setVisible(false);
                    chatView();
                    new Thread() {
                        public void run() {
                            String linia;
                            while ((linia = sc.read_line()) != null) {
                                if (linia.contains("?%")) {
                                    System.out.println(linia);
                                    llistaActualitzada(linia);
                                } else {
                                    System.out.print("Missatge: "+linia + "\n");
                                    messages.append(linia + " \n");
                                }
                            }
                        }

                    }.start();
                }
            }
        }
    }

    public class sendMessage implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            s_message = msg_send.getText();
            if (s_message.length() > 0) {
                System.out.println("Enviem missatge");
                msg_send.setText("");
                sc.write_line(s_message);
                messages.append(username + ": " + s_message + "\n");
            }

        }
    }

    public void llistaActualitzada(String nickname) {
        String name;
        if (nickname.contains("Exit?%")) {
            name = nickname.substring(6);
            if (lista.contains(name)) {
                lista.remove(name);
                dlmodel.removeElement(name);
                System.out.println("Eliminem NOM");
            }
        } else {
            name = nickname.substring(2);
            if (!lista.contains(name)) {
                lista.add(name);
                dlmodel.addElement(name);
                sc.write_line("?%" + username);
                System.out.println("Afegim NOM " + name);
            }
        }

        /*
         * usr_TextArea.removeAll();
         * usr_TextArea.append(this.list.getComponents().toString());
         */
    }

 public static void main(String[] args) {

        Client newclient = new Client();
        newclient.initChat();
    }
}
