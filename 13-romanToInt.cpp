# include <iostream>
# include <vector>
# include <map>
# include <string>
using namespace std;

class Solution {
public:
    int romanToInt(string s){
      int index=0, num=0, tmp=0;
      while(index<s.size()){
        char c = s[index++];
        switch(c){
          case 'I': num += 1; tmp = 1; break;
          case 'V': num += tmp==1? 3 : 5; break;
          case 'X': num += tmp==1? 8 : 10; tmp = 10; break;
          case 'L': num += tmp==10? 30 : 50; break;
          case 'C': num += tmp==10? 80 : 100; tmp = 100; break; 
          case 'D': num += tmp==100? 300 : 500; break;
          case 'M': num += tmp==100? 800 : 1000; break;
        }
      }
    return num;
    }
};

int main(){
  Solution sol = *(new Solution());
  int ans;

  string input;
  cout << "Please insert a roman number: " << endl;
  cin >> input;

  ans = sol.romanToInt(input);
  cout << "Ans: " << ans << endl;

  return 0;
};


