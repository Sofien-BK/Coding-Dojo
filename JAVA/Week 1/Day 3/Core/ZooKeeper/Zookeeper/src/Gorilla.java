
public class Gorilla extends Mammal{
	
	public void throwSomething() {
		setEnergy(getEnergy()-5);
		System.out.println("The Gorilla Thrown Something ☄️");
		System.out.println(String.format("Energy is : %d%%", getEnergy()));
	}
	
	public void eatBanans() {
		setEnergy(getEnergy()+10);
		System.out.println("The Gorilla Ate Banana , He Is Now Satisfied 🍌");
		System.out.println(String.format("Energy is : %d%%", getEnergy()));
	}
	
	public void climb() {
		setEnergy(getEnergy()-10);
		System.out.println("The Gorilla Has Climbed a Tree 🦍");
		System.out.println(String.format("Energy is : %d%%", getEnergy()));
	}
}
