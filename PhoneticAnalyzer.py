import copy

# a/o/e
# -ie to -i,e
# -ia to -i,a
ONE_AOE_ENABLE = False

# -ian to -i,an
# -iao to -i,ao
# -uan to -u,an
# -uang to -u,ang
FORCE_SEPERATE = False

# zh, ch, sh
ACRONYM_CACUMINAL = False


class PhoneticAnalyzer():
    def __init__(self):
        self.d = {}
        rf = open('dict', 'r')
        try:
            while True:
                line = rf.readline()[:-1]
                if line:
                    if not ONE_AOE_ENABLE and len(line) == 1:
                        continue
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

    def __segment__(self, str, pos, r, s):
        cur_d = self.d
        for i, ch in enumerate(str):
            cur_d = cur_d.get(ch, None)
            if cur_d is None:
                return None
            is_leaf = cur_d.get('leaf', False)
            if is_leaf:
                if i == len(str) - 1:
                    return s
                else:
                    if not FORCE_SEPERATE and not ONE_AOE_ENABLE:
                        if 'ui'.find(ch) >= 0 and str[i + 1] == 'a':
                            if i + 2 < len(str):
                                if str[i + 2] == 'n':
                                    continue
                                else:
                                    if ch == 'i' and str[i + 2] == 'o':
                                        continue
                    ts = copy.deepcopy(s)
                    ts.append(pos + i + 1)
                    sr = self.__segment__(str[i + 1:], pos + i + 1, r, ts)
                    if sr is not None:
                        r.append(sr)
        return None

    def segment(self, str):
        r = []
        self.__segment__(str.lower(), 0, r, [])
        return sorted(r, key=lambda seg: len(seg))

    def acronym(self, str):
        str = str.lower()
        r = self.segment(str)
        segs = []
        for seg in r:
            s = []
            for pos in [0] + seg:
                if ACRONYM_CACUMINAL:
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
    print(pa.seperate('angengan'))
    print(pa.seperate('gangangan'))
    print(pa.seperate('xinganxian'))
