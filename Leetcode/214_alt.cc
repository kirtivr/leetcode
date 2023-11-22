class Solution {
    public:

    void computelps(vector<int>&lps, string s, int m) {
        int len = 0, i = 1;
        while (i < m) {
            if (s[len] == s[i]) {
                len++;
                lps[i] = len;
                i++;
            } else {
                if (len != 0) {
                    len = lps[len - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }
    }

    string shortestPalindrome(string s) {
        int n = s.size();
        string ans = s;
        s += '#';

        for(int i = n - 1; i >= 0; i--) {
            s += s[i];
        }
        // So input abcd becomes abcd#dcba.

        vector<int> lps(2 * n + 2, 0);
        computelps(lps, s, n + n + 1);
        // lps of aacecaaa#aaacecaa is
        //        01000122012234567
        string temp = "";
        for (int i = n - 1; i >= lps[2 * n]; i--) {
            temp += s[i];
        }
        return temp + ans;
    }
}