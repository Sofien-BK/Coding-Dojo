
public class Phone extends Device{

	public void makeCall () {
		System.out.println("You make a call.");
		setBattery(getBattery()-5);
		batteryLife();
	}
	
	public void playGame () {
		System.out.println("You play a game.");
		setBattery(getBattery()-20);
		batteryLife();
	}
	
	public void charge () {
		System.out.println("Your phone is charging.");
		setBattery(getBattery()+50);
		batteryLife();
	}

}
