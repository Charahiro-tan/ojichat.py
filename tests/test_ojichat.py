from ojichat import OjichatGenerator


def test_1():
    print("")
    g = OjichatGenerator()
    results = set()
    for i in range(10):
        result = g.generator(reset_on_finish=True)
        print(result)
        results.add(result)
    assert len(results) == 10


def test_2():
    print("")
    g = OjichatGenerator()
    result1 = g.generator()
    print(result1)
    result2 = g.generator(True)
    print(result2)
    result3 = g.generator()
    print(result3)
    g.reset()
    result4 = g.generator()
    print(result4)
    assert result1.message == result2.message
    assert result2.message != result3.message
    assert result3.message != result4.message


def test_3():
    print("")
    g1 = OjichatGenerator()
    result1 = g1.generator()
    print(result1)
    g2 = OjichatGenerator(
        result1.name, result1.seed, result1.emoji_num, result1.punc_level
    )
    result2 = g2.generator()
    print(result2)
    assert result1.message == result2.message


def test_4():
    print("")
    g = OjichatGenerator()
    result1 = g.generator()
    print(result1)
    g.set_props(name=result1.name, seed=-1)
    result2 = g.generator()
    print(result2)
    g.set_props(name="")
    result3 = g.generator()
    print(result3)
    assert result1.name == result2.name
    assert result1.message != result2.message
    assert result2.name != result3.name
    assert result2.seed == result3.seed


def test_5():
    print("")
    g = OjichatGenerator(seed=1234)
    result = g.generator()
    print(result)
    s = "いつえﾁｬﾝ、おっは〜(^з<)(^o^)今日はどんな一日だった✋❓⁉😜⁉️⁉僕はプライベートで、いつえﾁｬﾝを癒やして(^o^)😋❗あげたい😃✋って思ってるよ(＃￣З￣)😎🙂（￣▽￣）"  # noqa
    print(s)
    assert result.message == s
