import copy


class PhoneticAnalyzer():
    # ao to a,o
    # -ie to -i,e
    # -ia to -i,a
    # -ua to -u,a
    # -uo to -u,o

    # -ian to -i,an
    # -iao to -i,ao
    # -uan to -u,an
    # -uang to -u,ang
    # GREEDY_MODE

    # zh, ch, sh
    # ACRONYM_CACUMINAL
    def __init__(self, gm=True, ac=False):
        self.d = {}
        self.greedy_mode = gm
        self.acronym_cacuminal = ac
        rf = open('dict', 'r')
        try:
            while True:
                line = rf.readline()[:-1]
                if line:
                    cur_d = self.d
                    for ch in line:
                        cur_d.setdefault(ch, {})
                        cur_d = cur_d[ch]
                    cur_d.setdefault('leaf', True)
                else:
                    break
        except Exception as e:
            raise e
        finally:
            rf.close()

    def __segment__(self, str, next_ok, pos, r, s):
        cur_d = self.d
        for i, ch in enumerate(str):
            cur_d = cur_d.get(ch, None)
            if cur_d is None:
                return None
            is_leaf = cur_d.get('leaf', False)
            if is_leaf:
                # len is 1 and can be combined with last, ommit
                if self.greedy_mode and i == 0 and next_ok:
                    continue
                if i == len(str) - 1:
                    return s
                else:
                    if self.greedy_mode:
                        if 'uiv'.find(ch) >= 0 and str[i + 1] == 'a':
                            # check if is valid
                            if cur_d.get(str[i + 1], None):
                                continue
                    np = pos + i + 1
                    ts = copy.deepcopy(s)
                    ts.append(np)
                    n_ok = self.greedy_mode\
                        and 'aoe'.find(str[i + 1]) >= 0\
                        and cur_d.get(str[i + 1], None)
                    sr = self.__segment__(str[i + 1:], n_ok, np, r, ts)
                    if sr is not None:
                        r.append(sr)
        return None

    def segment(self, str):
        r = []
        sr = self.__segment__(str.lower(), None, 0, r, [])
        if sr is not None:
            r.append(sr)
        return sorted(r, key=lambda seg: len(seg))

    def acronym(self, str):
        str = str.lower()
        r = self.segment(str)
        segs = []
        for seg in r:
            s = [str[0]]
            for pos in seg:
                if self.acronym_cacuminal:
                    if 'zcs'.find(str[pos]) >= 0:
                        if str[pos + 1] == 'h':
                            s.append(str[pos] + 'h')
                            continue
                s.append(str[pos])
            segs.append(s)
        return segs

    def seperate(self, str):
        str = str.lower()
        r = self.segment(str)
        segs = []
        for seg in r:
            s = []
            start = 0
            for pos in seg:
                s.append(str[start:pos])
                start = pos
            s.append(str[start:])
            segs.append(s)
        return segs


if __name__ == '__main__':
    pa = PhoneticAnalyzer()
    print(pa.segment('xys'))
    print(pa.seperate('fao'))
    print(pa.seperate('mao'))
    print(pa.seperate('maou'))
    print(pa.seperate('diao'))
    print(pa.seperate('diei'))
    print(pa.seperate('dieru'))
    print(pa.acronym('wuanxin'))
    print(pa.acronym('shengou'))
    print(pa.seperate('buanerao'))
    print(pa.seperate('shuo'))
    print(pa.seperate('xinangang'))
    print(pa.seperate('tienanen'))
    print(pa.segment('gangangan'))
    print(pa.seperate('xinganxian'))
