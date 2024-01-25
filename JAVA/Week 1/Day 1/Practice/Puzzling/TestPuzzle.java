import java.util.ArrayList;
public class TestPuzzle {
    public static void main(String[] args){

        PuzzleJava puzzle = new PuzzleJava();

        ArrayList <Integer> testGetTenRolls = puzzle.getTenRolls();
        char testGetRandomLetter  = puzzle.getRandomLetter();
        String testGeneratePassword =  puzzle.generatePassword();
        ArrayList <String> testGetNewPasswordSet = puzzle.getNewPasswordSet(3);
    } 
}