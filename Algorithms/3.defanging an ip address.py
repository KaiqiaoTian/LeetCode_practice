class Solution:
    def defangIPaddr(self, address: str) -> str:
        asd = address.replace('.','[.]')
        return asd
