import java.util.Date;

public class AlfredQuotes {

    public String basicGreeting(){
        System.out.println("Hello,lovely to  see you. How are you?"); 
        return "Hello,lovely to  see you. How are you?";
    }

    public String guestGreeting(String name){
       String result = String.format("%s %s", basicGreeting(), name);
       System.out.println(result);
       return result;
    }

    public String dateAnnouncement() {
        Date date = new Date();
        String result = String.format("It is currently %s", date.toString());  
        System.out.println(result);
        return result;
    } 

    public String respondBeForeAlexis(String conversation){
        if (conversation.indexOf("Alexis") >= 0){
        System.out.println("Right away, sir. She certainly isn't sophisticated enough for that."); 
        return "Right away, sir. She certainly isn't sophisticated enough for that.";
        } if (conversation.indexOf("Alfred") >= 0) {
        System.out.println("At your service. As you wish, naturally."); 
        return "At your service. As you wish, naturally.";
        }else {
            System.out.println("Right. And with that I shall retire.");
            return "Right. And with that I shall retire.";
        }
    }

}

//todo Ninja Bonus !!!