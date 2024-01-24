public class AlfredTest {

    public static void main(String[] args){

        AlfredQuotes alfredBot = new AlfredQuotes();

        String testGreeting =  alfredBot.basicGreeting();
        String testGuestGreeting = alfredBot.guestGreeting("Beth Kane");
        String testDateAnnouncement = alfredBot.dateAnnouncement();
        String alfredTest = alfredBot.respondBeForeAlexis("I can't find my yo-yo. Maybe Alfred will know where it is.");
        String notRelevantTest = alfredBot.respondBeForeAlexis("Maybe that's what Batman is about. Not winning. But failing.."
        );
    }
}