# Encode and Decode Strings: https://neetcode.io/problems/string-encode-and-decode/question?list=neetcode150

class Solution:
    def hash_string(self, s: str) -> str:
        hash_code = 666
        hashed_srt = ""
        for i in s:
            code = ord(i) ^ hash_code
            code_str = str(code) + ","
            hashed_srt += code_str
            return hashed_srt[0:-1]


    def unhash_string(self, s: str) ->str:
        hash_code = 666
        unhashed_str = ""
        lst_hashs = s.split(",")
        if s == "" : return ""
        for s in lst_hashs:
            code = int(s)
            org_char = chr(code ^ hash_code)
            unhashed_str += org_char
        return unhashed_str


    def encoder(self, strs: list[str]) -> str:
        encoded = ""
        for s in strs:
            hashed_srt = self.hash_string(s) + ";"
            encoded += hashed_srt

        return encoded

    def decode(self, s: str) -> list[str]:
        decoded_lst = []
        decoded = ""
        for i in range(0, len(s)):
            if s[i] != ";":
                decoded += s[i]
            else:
                decoded_lst.append(self.unhash_string(decoded))
                decoded = ""
        return decoded_lst
