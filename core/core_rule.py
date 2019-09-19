class rule:

    def default_rule_base(self):
        fuzz_zs = ['/*', '*/', '/*!', '*', '=', '`', '!', '@', '%', '.', '-', '+', '|', '%00']
        fuzz_sz = ['', ' ']
        fuzz_ch = ["%0b", "%0c", "%0d", "%0e", "%0f", "%0g", "%0h", "%0i", "%0j"]
        fuzz = fuzz_zs + fuzz_sz + fuzz_ch
        return fuzz
    def safedog_rule_base(self):

        fuzz_payload = ["%23aa","%0a"]

        return fuzz_payload

    def Comment_rule_base(self):

        comment = {
            "start":["/*","/*!","/*!50000"],
            "end":["*/"]
        }
        return comment

    def dseaf_rule_base(self):
        fuzz = {
            "fuzz_sz" : ["&nbsp;", "&lt;", "&gt;", "&amp;", "&auot;", "&apos;", "&cent;", "&pound;", "&yen;", "&euro"],
            "fuzz_zs" : ["%00", "%20", "%0a", "%23", "0b", "%26", "%2b","%00"]
        }
        return fuzz

