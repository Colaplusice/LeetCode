# 字符串
class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        """
        点会被忽略
        +号后面的东西会被忽略
        """
        new_list = set([])
        for em in emails:
            em_list = em.split("@")
            sec_em = em_list[0][: em_list[0].index("+")]
            begin = "".join(sec_em.split("."))
            new_list.add(begin + em_list[1])
        return len(new_list)


if __name__ == "__main__":

    sol = Solution()
    sol.numUniqueEmails(
        [
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com",
        ]
    )
