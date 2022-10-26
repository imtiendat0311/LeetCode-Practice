// faster than 100% other java submission
// use less mem than 99% other java submission
class Solution {
    public int romanToInt(String s) {
        char[] symbol ={'I','V','X','L','C','D','M'};
        int[] value = {1,5,10,50,100,500,1000};
        int number=0;
        for(int i=0;i<s.length();i++){
            for(int j=0;j<symbol.length;j++){
                if(s.charAt(i)==(symbol[j])){
                    if((j==0||j==2||j==4) && i<(s.length()-1)){
                        if(s.charAt(i+1)==symbol[j+1]||s.charAt(i+1)==symbol[j+2]){
                            number=number-value[j];
                            break;
                        }
                        else{
                            number=number+value[j];
                            break;
                        }
                    }
                    else{
                        number=number+value[j];
                        break;
                    }
                }
            }
        }
   return number; }
}
      