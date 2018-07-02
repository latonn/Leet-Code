# include <iostream>
# include <stack>
# include <string>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
      stack<char> parentheses;
      s.append(1, '#');
      
      int i = 0;
      while(s[i] != '#'){
        if(s[i]=='(' || s[i]=='[' || s[i]=='{') {
          parentheses.push(s[i]);
        }
        else{
          switch(s[i]){
            case ')' :
              if(parentheses.empty() || parentheses.top() != '('){
                return false;
                break;
              }
              else{
                parentheses.pop();
                break;
              }
            case ']' :
              if(parentheses.empty() || parentheses.top() != '['){
                return false;
                break;
              }
              else{
                parentheses.pop();
                break;
              }
            case '}' :
              if(parentheses.empty() || parentheses.top() != '{'){
                return false;
                break;
              }
              else{
                parentheses.pop();
                break;
              }
          }
        }
        i++;
      }
      if(parentheses.empty()) return true;
      else return false;
    }
};

int main(){
  Solution sol = *(new Solution());
 
  string input;
  bool ans;
  while(getline(cin, input)){
    ans = sol.isValid(input);
    if(ans) cout << "It is valid." << endl;  
    else cout << "It's not valid." << endl;
  }

  return 0;
};


