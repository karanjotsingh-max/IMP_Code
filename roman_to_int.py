def romanToInt(self, s: str) -> int:
        rom_dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        count=0
        i=0
        while i < len(s):
            if i+1<len(s) and rom_dict[s[i]] < rom_dict[s[i + 1]]:
                count+=rom_dict[s[i+1]]-rom_dict[s[i]]
                i+=2
            else:
                count+=rom_dict[s[i]]
                i+=1
        return count
