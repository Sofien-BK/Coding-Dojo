import java.util.Random;
import java.util.ArrayList;
public class PuzzleJava {

    public ArrayList<Integer> getTenRolls(){

        Random randomBot = new Random();
        ArrayList<Integer> randomTenList = new ArrayList<>();   
        for (int i=0; i<10; i++ ){
            int randomTen  = randomBot.nextInt(21);
            randomTenList.add(randomTen);
        }
        System.out.println(randomTenList);
        return randomTenList;
    }

    public char getRandomLetter(){
        Random randomBot = new Random();
        char[] alphabet = "abcdefghijklmnopqrstuvwxyz".toCharArray();
        int randomNum  = randomBot.nextInt(26);
        char randomLetter = alphabet[randomNum];
        System.out.println(randomLetter);
        return randomLetter;
    } 

    public String generatePassword (){
        char[] randomPwList = new char[8];
        for (int i=0; i <8 ; i++ ) {
            randomPwList[i]=getRandomLetter();
        } 
        String randomPw = new String(randomPwList);
        System.out.println(randomPw);
        return randomPw;
    }

    public ArrayList<String> getNewPasswordSet (int length){
        ArrayList<String> randomPws = new ArrayList<>();
        for(int x  = 0; x<length; x++){
        char[] randomPwList = new char[8];
        for (int i=0; i <8 ; i++ ) {
            randomPwList[i]=getRandomLetter();
        }
        String randomPw = new String(randomPwList);
        randomPws.add(randomPw);
    }
    System.out.println(randomPws);
    return randomPws;
    }
} 