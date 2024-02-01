
public class Device {
	private int battery = 100 ;
	
	public void batteryLife (){
		System.out.println(String.format("Battery Life: %d%%", battery)); 
	}

	public int getBattery() {
		return battery;
	}

	public void setBattery(int battery) {
		this.battery = battery;
	}
	
			
}
