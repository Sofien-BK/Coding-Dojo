/* 
  Given a string,
  return a new string with the duplicates excluded
  Bonus: Keep only the last instance of each character.
*/
const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "";
const expected3 = "";

const str4 = "aa";
const expected4 = "a";

/**
 * De-dupes the given string.
 */

function stringDedupe(str) { 
    var result = '';
    var freqTable = {};
    for (var i =0 ; i <=str.length - 1 ; i++){
        if (!freqTable[str[i]]){
            result+=str[i];
            freqTable [str[i]]=true;
        }

    } 
    return result;

}
console.log(stringDedupe(str2));

