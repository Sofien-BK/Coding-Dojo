
public class Mammal {
	private int energy = 100;
	
	public void displayEnergy() {
		System.out.println(String.format("Energy is : %d%%", energy));
	}

	public int getEnergy() {
		return energy;
	}

	public void setEnergy(int energy) {
		this.energy = energy;
	}
	
	
}
