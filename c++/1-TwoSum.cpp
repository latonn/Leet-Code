# include <iostream>
# include <vector>
# include <map>
# include <string>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
      int i, sum;
      vector<int> results;
      map<int, int> hmap;
      for(i=0; i<nums.size() ; i++){
        if(!hmap.count(nums[i])){
          hmap.insert(pair<int, int>(nums[i], i));
        }
        if(hmap.count(target-nums[i])){
          int n = hmap[target-nums[i]];
          if(n<i){
            results.push_back(n);
            results.push_back(i);
            return results;
          }
        }
      }
      return results;
    }
};

int main(){
  Solution sol = *(new Solution());
  vector<int> input;
  vector<int> ans;
  int tmp;
  int target = 40;
  while(cin >> tmp){
    input.push_back(tmp);
  }

  ans = sol.twoSum(input, target);
  if(ans.size() != 0)
    cout << "Ans: [" << ans.front() << "," << ans.back() << "]" << endl;
  else
    cout << "There is no two sum solution!" << endl;

  return 0;
};


