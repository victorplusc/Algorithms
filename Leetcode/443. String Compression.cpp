/*
443. String Compression
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.

 
Follow up:
Could you solve it using only O(1) extra space?
*/

// Time complexity: O(N)
// Space complexity: O(1)

class Solution {
public:
    int compress(vector<char>& chars) {
        int anchor = 0;
        int write = 0;
        for(int i = 0; i < chars.size(); i++){
            if ((i == chars.size()-1) || (chars[i] != chars[i+1])){
                chars[write] = chars[anchor];
                write++;
                if (i > anchor){
                    std::string s = std::to_string(i - anchor + 1);
                    for (int j = 0; j < s.size(); j++){
                        chars[write] = s[j];
                        write++;
                    }
                }
                anchor = i + 1;
            }
                
        }
        return write;
    }
};
