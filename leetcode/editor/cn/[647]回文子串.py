# 给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。 
# 
#  回文字符串 是正着读和倒过来读一样的字符串。 
# 
#  子字符串 是字符串中的由连续字符组成的一个序列。 
# 
#  具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa" 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 由小写英文字母组成 
#  
#  Related Topics 字符串 动态规划 👍 712 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        # if not s: return count
        for i in range(len(s)):
            cnt1 = self.expandAndCount(s, i, i)  # 中心点为一个字母
            cnt2 = self.expandAndCount(s, i, i + 1)  # 中心点为2个字母
            count += (cnt1 + cnt2)
        return count

    def expandAndCount(self, s, begin, end) -> int:
        cnt = 0
        while begin >= 0 and end < len(s) and s[begin] == s[end]:
            begin -= 1
            end += 1
            cnt += 1
        return cnt

if __name__ == '__main__':
    Solution.countSubstrings("abc")

# leetcode submit region end(Prohibit modification and deletion)
