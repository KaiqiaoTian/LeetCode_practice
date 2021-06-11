/*Description
Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.



*/

class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int max_candies = 0;
        vector<bool> kid;
        for(int i = 0; i < candies.size(); i++){
            max_candies = max(max_candies, candies[i]);
        }
       for(int i = 0; i < candies.size(); i++){
           if(candies[i]+extraCandies +1 > max_candies){
               kid.push_back(true);
           }else
               kid.push_back(false);
        }
    
    return kid;
    }
};
