import java.util.HashMap;
import java.util.Set;

public class TestHashmatique {

HashMap<String, String> trackList  = new HashMap<String, String>();

    public String getTrackByName (String name){

        trackList.put("Bared","hello go kitchen");
        trackList.put("Zoo","wolf tiger lion");
        trackList.put("Hospital","doctor client ");
        trackList.put("Dealer","weed roll joint");

        String result = new String();

        Set<String> trackTittles = trackList.keySet();
        System.out.println(trackList.get(name));
        for(String trackTittle : trackTittles){
            result = String.format("%s : %s" , trackTittle , trackList.get(trackTittle));
            System.out.println(result);
        }
        return result;
    }

}