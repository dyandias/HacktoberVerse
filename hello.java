import  javax.swing.*;
class hello
{
	public static void main(String[] args)
	{
		JFrame f=new JFrame("Applet");
		JLabel lb1;
		lb1=new JLabel("HNDIT" );lb1.setBounds(50,50,100,30);

		f.add(lb1);
		f.setSize(600,300); f.setLayout(null); f.setVisible(true);
	}
}
	/*	
		lb2; JButton cmd1; JTextField tf1,tf2;
	
		lb2=new JLabel("second value:");lb2.setBounds(50,100,100,30);
		tf1=new JTextField(); tf1.setBounds(150,50,100,30);
		tf2=new JTextField(); tf2.setBounds(150,100,100,30);
		cmd1=new JButton("Add"); cmd1.setBounds(150,150,75,30);
				
		 f.add(lb2); f.add(tf1); f.add(tf2); f.add(cmd1);
	*/