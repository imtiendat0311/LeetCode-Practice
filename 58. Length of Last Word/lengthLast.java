class Solution {
    public int lengthOfLastWord(String s) {
        int count = 0;
        int length = s.length();
        int i = length - 1;
        while(i>0&&s.charAt(i)==' '){
            i--;
        }
        for(; i >= 0; i--){
            if(s.charAt(i) != ' '){
                count += 1;
            } else{
                break;
            }
        }
        
        return count;
    
    }
}