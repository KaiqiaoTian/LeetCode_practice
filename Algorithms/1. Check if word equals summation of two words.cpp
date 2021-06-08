class Solution {
public:
    
    int sumofword(string s)
    {
        int sum = 0;
        for(int i = 0; i < s.length(); i++){
            int w = s[i] -97;
            sum = sum*10 + w;
        }
        return sum;
    }
    
    
    bool isSumEqual(string firstWord, string secondWord, string targetWord) {
        if(sumofword(firstWord) + sumofword(secondWord) == sumofword(targetWord))
            return true;
        else
            return false;
        
    }
};
