class str_rev_word:
    str1 = "Hello how are you?"
    def str_rev(self):
        list1 = self.str1.split(" ")
        list1 = list1[::-1]
        list1.join(" ")
        str2 = list1.join(" ")
        print(str2)
obj = str_rev_word()
obj.str_rev()
