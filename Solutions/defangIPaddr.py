# NAME : Defanging an IP Address
# LINK : https://leetcode.com/problems/defanging-an-ip-address/
# DATE : 03/05/2021

class Solution:
    def defangIPaddr(self, address: str) -> str:
        extra = 0
        for i in range(len(address)):
            if address[i + extra] == ".":
                address = address[:i + extra] + "[.]" + address[i + 1 + extra:]
                extra += 2
        return address
