class Solution:
    def reverseVowels(self,s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        arr = []

        for i in range(len(s)):
            if s[i] in vowels:
                arr.append(i)

        s_list = list(s)
        j = len(arr) - 1

        for i in range(len(arr)//2):
            temp = s_list[arr[i]]
            s_list[arr[i]] = s_list[arr[j]]
            s_list[arr[j]] = temp
            j -= 1

        s = ''.join(s_list)

        return(s)


