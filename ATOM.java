public class ATOM
{
	int protons;
	int neutrons;
	int electrons;
	
	protected int  electronCharge;
	
	public ATOM (int p, int n, int e)
	{
		this.protons = p;
		this.neutrons = n;
		this.electrons = e;
	}
	
	void setProtons(int p){
	this.protons = p;}
	
	int getNuetrons(){
	return neutrons;}
	
	public static void main (String [] arg)
	{
		ATOM ob1 = new ATOM(10,20,30);
		
		ob1.setProtons(10);
		int x=ob1.getNuetrons();
		
		System.out.println(x);
	}
}