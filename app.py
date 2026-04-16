import streamlit as st

st.set_page_config(layout="wide")

DATA = {
    "골프 브랜드": [
        {
            "id": "brand-1",
            "date": "04.06",
            "source": "골프경제신문",
            "title": "대보골프단, 2026 시즌 출정식 진행",
            "priority": "HIGH",
            "oneLine": "브랜드와 선수단 서사가 결합되는 시즌 초 핵심 콘텐츠",
            "summary": "시즌 출정과 함께 브랜드 노출 확대",
            "insight": "스토리 기반 행사로 활용 가능",
            "actions": ["선수 협업 팝업", "테마 매장 구성"],
            "link": "https://www.golfbiz.co.kr/news/articleView.html?idxno=26122"
        },
        {
            "id": "brand-2",
            "date": "04.14",
            "source": "매일경제",
            "title": "프리미엄 골프 장비 시장 확대",
            "priority": "HIGH",
            "oneLine": "고가 장비 중심 소비 확대",
            "summary": "프리미엄 장비 수요 증가",
            "insight": "체험형 판매 필수",
            "actions": ["시타존 운영", "VIP 상담"],
            "link": "https://www.mk.co.kr/news/sports/12016692"
        }
    ]
}

PRIORITY_ORDER = {"HIGH": 0, "MID": 1, "LOW": 2}

if "selected" not in st.session_state:
    st.session_state.selected = []

st.title("골프 산업 인사이트")

col1, col2 = st.columns([3,1])

with col1:
    category = "골프 브랜드"
    cards = sorted(DATA[category], key=lambda x: PRIORITY_ORDER[x["priority"]])

    for card in cards:
        st.subheader(card["title"])
        st.caption(f"{card['date']} · {card['source']}")
        st.markdown(f"**{card['oneLine']}**")
        st.write(card["summary"])

        with st.expander("MD 인사이트"):
            st.write("인사이트:", card["insight"])
            st.write("실행:")
            for a in card["actions"]:
                st.write("-", a)

        if st.button(f"채택 {card['id']}"):
            if card not in st.session_state.selected:
                st.session_state.selected.append(card)

        st.markdown(f"[기사보기]({card['link']})")
        st.divider()

with col2:
    st.subheader("실행 리스트")
    for item in st.session_state.selected:
        st.write(item["title"])
