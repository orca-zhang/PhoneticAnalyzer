# PhoneticAnalyzer

``` py
    import * from PhoneticAnalyzer
 
    pa = PhoneticAnalyzer(greedy_mode=True, acronym_cacuminal=False)
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
```

``` shell
[]
[['fa', 'o']]
[['mao']]
[['ma', 'ou']]
[['diao']]
[['di', 'ei']]
[['die', 'ru']]
[['w', 'a', 'x']]
[['s', 'g'], ['s', 'o']]
[['bu', 'a', 'ne', 'rao'], ['bu', 'an', 'e', 'rao'], ['bu', 'an', 'er', 'ao']]
[['shuo']]
[['xi', 'nan', 'gang'], ['xi', 'nang', 'ang'], ['xin', 'an', 'gang'], ['xin', 'ang', 'ang']]
[['tie', 'na', 'nen'], ['tie', 'nan', 'en'], ['ti', 'en', 'a', 'nen'], ['ti', 'en', 'an', 'en']]
[[3, 6], [3, 7], [4, 6], [4, 7]]
[['xin', 'gan', 'xian'], ['xing', 'an', 'xian']]
```
