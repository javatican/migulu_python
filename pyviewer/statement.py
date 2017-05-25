class Statement:
    current_stm = None
    def __init__(self,text, line_no, multi, prev, next):
        self.text = text
        self.line_no = line_no
        self.multi = multi
        self.prev = prev
        self.next = next
    def set_prev(self, prev):
        self.prev = prev
    def set_next(self, next):
        self.next = next
    def set_current(self):
        Statement.current_stm = self
    def get_text(self):
        return self.text
    def get_line_no(self):
        return self.line_no
    def __str__(self):
        return "[%d, %s]" % (self.line_no, self.text)
    def __repr__(self):
        return "[%d, %s]" % (self.line_no, self.text)

    @classmethod
    def set_current(cls, stm):
        Statement.current_stm = stm
    @classmethod
    def create_stms(cls, text_list):
        stm_list=[]
        for i, t in enumerate(text_list):
            st = Statement(t, i+1, False, None, None)
            stm_list.append(st)
            if i>0:
                st.set_prev(stm_list[i-1])
                stm_list[i-1].set_next(st)
        return stm_list
