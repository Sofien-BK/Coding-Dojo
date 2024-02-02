
public class Bat extends Mammal{
	public Bat() {
		setEnergy(300);
	}
	
	public void fly() {
		setEnergy(getEnergy()-50);
		System.out.println("The Bat Is Airborne 🦇");
		displayEnergy();
	}
	
	public void eatHumans() {
		setEnergy(getEnergy()+25);
		System.out.println("The Bat Eat A Human , He Is Now Satisfied 🦇");
		displayEnergy();
	}
	
	public void attackTown() {
		setEnergy(getEnergy()-100);
		System.out.println("The Bat Is Attacking A Town 🦇");
		displayEnergy();
	}
}
