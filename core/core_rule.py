class rule:

    def default_rule_base(self):
        fuzz_zs = ['/*', '*/', '/*!', '*', '=', '`', '!', '@', '%', '.', '-', '+', '|', '%00']
        fuzz_sz = ['', ' ']
        fuzz_ch = ["%0b", "%0c", "%0d", "%0e", "%0f", "%0g", "%0h", "%0i", "% 0j"]
        fuzz = fuzz_zs + fuzz_sz + fuzz_ch
        return fuzz
    def safedog_rule_base(self):

        fuzz_payload = ["%23aa","%0a"]

        return fuzz_payload