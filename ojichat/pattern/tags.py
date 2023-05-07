uniq_tags: dict[str, list[str]] = {
    # おじさんの一人称
    "FIRST_PERSON": [
        "僕",
        "ボク",
        "ﾎﾞｸ",
        "俺",
        "オレ",
        "ｵﾚ",
        "小生",
        "オジサン",
        "ｵｼﾞｻﾝ",
        "おじさん",
        "オイラ",
    ],
    # 曜日
    "DAY_OF_WEEK": [
        "月",
        "火",
        "水",
        "木",
        "金",
        "土",
        "日",
    ],
    # 地名
    "LOCATION": [
        "愛知",
        "青森",
        "秋田",
        "石川",
        "茨城",
        "岩手",
        "愛媛",
        "大分",
        "大阪",
        "岡山",
        "沖縄",
        "香川",
        "鹿児島",
        "神奈川",
        "岐阜",
        "京都",
        "熊本",
        "群馬",
        "高知",
        "埼玉",
        "佐賀",
        "滋賀",
        "静岡",
        "島根",
        "千葉",
        "東京",
        "徳島",
        "栃木",
        "鳥取",
        "富山",
        "長崎",
        "長野",
        "奈良",
        "新潟",
        "兵庫",
        "広島",
        "福井",
        "福岡",
        "福島",
        "北海道",
        "三重",
        "宮城",
        "宮崎",
        "山形",
        "山口",
        "山梨",
        "和歌山",
    ],
    # 外食
    "RESTAURANT": [
        "お寿司🍣",
        "イタリアン🍝",
        "バー🍷",
        "ラーメン屋さん🍜",
        "中華🍜",
        "ステーキハウス🥩",
        "フレンチ🍽️",
        "カクテルバー🍸",
        "ワインバー🍷",
        "スポーツバー🏀",
        "パブ🍻",
        "ビアガーデン🍺",
        "ジャズバー🎷",
    ],
    # 食べ物
    "FOOD": [
        "お惣菜",
        "サラダ🥗",
        "おにぎり🍙",
        "きんぴらごぼう",
        "ピッツァ🍕",
        "パスタ🍝",
        "スイーツ🍮",
        "ケーキ🎂",
        "ステーキ🥩",
        "お寿司🍣",
        "タコス🌮",
        "バーベキュー🍖",
        "ハンバーガー🍔",
        "クラブサンドイッチ🥪",
        "オムレツ🍳",
        "餃子🥟",
        "フレンチトースト🍞",
        "アイスクリーム🍦",
        "ドーナツ🍩",
    ],
    # 天気
    "WEATHER": [
        "曇り🌥️",
        "晴れ☀️",
        "快晴🌞",
        "大雨🌧️",
        "雨🌧️",
        "雪⛄️",
        "台風🌀",
    ],
    # 下ネタの後は「ナンチャッテ」「冗談（笑）」を使う
    "NANCHATTE": [
        "ﾅﾝﾁｬｯﾃ{EMOJI_POS}",
        "ナンチャッテ{EMOJI_POS}",
        "なんちゃって{EMOJI_POS}",
        "なんてね{EMOJI_POS}",
        "冗談{EMOJI_POS}",
        "",  # おじさんはたまに本気
    ],
    # おじさんの欲望の地、ホテル
    "HOTEL": [
        "ホテル🏨",
        "ホテル🏩",
        "旅館",
    ],
    # デートの種類
    "DATE": [
        "デート❤",
        "カラオケ🎤",
        "ドライブ🚗",
        "映画デート🎬",
        "遊園地デート🎢",
        "ショッピング🛍️",
        "パチンコ🎰",
        "サウナ🧖",
        "ゴルフ ⛳",
    ],
    # おじさんは比喩で相手を持ち上げる (川柳)
    "METAPHOR": [
        "天使",
        "女神",
        "女優さん",
        "お姫様",
    ],
}

# 文章中複数回変更&繰り返されるタグ
flex_tags: dict[str, list[str]] = {
    # ポジティブな表現の絵文字/顔文字
    "EMOJI_POS": [
        "😃♥ ",
        "😃☀ ",
        "😃",
        "😃✋",
        "❗",
        "😄",
        "😆",
        "😚",
        "😘",
        "😚",
        "💕",
        "💗",
        "😍",
        "😁",
        "😋",
        "😂",
        "😊",
        "🎵",
        "(^_^)",
        "(^o^)",
        "(^з<)",
        "（笑）",
    ],
    # ネガティヴな表現の絵文字/顔文字
    "EMOJI_NEG": [
        "💦",
        "💔",
        "😱",
        "😰",
        "😭",
        "😓",
        "😣",
        "😖",
        "😥",
        "😢",
        "😿",
        "😔",
        "🥺",
        "😧",
        "(◎ ＿◎;)",
        "(T_T)",
        "^^;",
        "(^_^;",
        "(・_・;",
        "(￣Д￣；；",
        "(^▽^;)",
        "(-_-;)",
    ],
    # ニュートラルな感情を表す絵文字/顔文字
    "EMOJI_NEUT": [
        "💤",
        "😴",
        "🙂",
        "🤑",
        "✋",
        "😪",
        "🛌",
        "😎",
        "😤",
        "😒",
        "😙",
        "😏",
        "😳",
        "😌",
        "（￣▽￣）",
        "(＃￣З￣)",
        "(^^;;",
    ],
    # 疑問を投げかけるときに利用される絵文字/顔文字
    "EMOJI_ASK": [
        "⁉",
        "❓",
        "❗❓",
        "🤔",
        "😜⁉️",
        "✋❓",
        "（￣ー￣?）",
    ],
}
