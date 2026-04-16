import streamlit as st

st.set_page_config(
    page_title="골프 산업 인사이트",
    page_icon="⛳",
    layout="wide",
)

DATA = {
    "골프 브랜드": [
        {
            "id": "brand-1",
            "date": "04.06",
            "source": "골프경제신문",
            "title": "대보골프단, 2026 시즌 출정식 진행",
            "articleUrl": "https://www.golfbiz.co.kr/news/articleView.html?idxno=26122",
            "priority": "HIGH",
            "oneLine": "브랜드와 선수단 서사가 결합되는 시즌 초 핵심 콘텐츠",
            "summary": "KPGA·KLPGA 선수단 구성 공개와 함께 시즌 전략 발표가 진행되며 브랜드 스토리 노출이 확대됨.",
            "insight": "시즌 출정·선수단 이슈는 단순 판촉보다 ‘이유 있는 행사’로 활용 가능. 고객 참여형 이벤트 및 브랜드 스토리 전달에 유리.",
            "actions": [
                "선수 협업 팝업 기획",
                "시즌 출정 테마 매장 구성",
                "선수 착용 상품 큐레이션",
            ],
        },
        {
            "id": "brand-2",
            "date": "04.14",
            "source": "매일경제",
            "title": "프리미엄 골프 장비 시장 확대",
            "articleUrl": "https://www.mk.co.kr/news/sports/12016692",
            "priority": "HIGH",
            "oneLine": "고가 장비 중심 소비 확대",
            "summary": "퍼터, 클럽 등 고가 장비 판매 비중 증가로 프리미엄 시장 경쟁 심화.",
            "insight": "고가 상품은 설명형·체험형 판매에서 구매 전환율이 높음. 일반 진열 방식으로는 매출 극대화 한계.",
            "actions": [
                "시타 체험존 운영",
                "VIP 대상 1:1 상담 프로그램",
                "프리미엄 존 별도 구성",
            ],
        },
        {
            "id": "brand-3",
            "date": "04.05",
            "source": "골프경제신문",
            "title": "백화점 골프 팝업 확대",
            "articleUrls": [
                "https://search.naver.com/search.naver?where=news&query=%EA%B3%A8%ED%94%84%20%ED%8C%9D%EC%97%85",
                "https://search.naver.com/search.naver?where=news&query=%EB%B0%B1%ED%99%94%EC%A0%90%20%EA%B3%A8%ED%94%84%20%ED%96%89%EC%82%AC",
            ],
            "priority": "HIGH",
            "oneLine": "체험형 팝업 경쟁 심화",
            "summary": "주요 백화점에서 체험형 골프 팝업 확대 운영되며 고객 유입 경쟁 심화.",
            "insight": "경쟁사 실행 사례는 즉시 적용 가능. 특히 체험형 요소가 핵심 차별 포인트.",
            "actions": [
                "체험형 팝업 기획",
                "브랜드 협업 이벤트",
                "MZ 타겟 콘텐츠 운영",
            ],
        },
        {
            "id": "brand-4",
            "date": "04.09",
            "source": "패션비즈",
            "title": "골프웨어 봄 시즌 매출 상승",
            "articleUrls": [
                "https://search.naver.com/search.naver?where=news&query=%EA%B3%A8%ED%94%84%EC%9B%A8%EC%96%B4%20%EB%A7%A4%EC%B6%9C",
                "https://search.naver.com/search.naver?where=news&query=%EA%B3%A8%ED%94%84%EC%9B%A8%EC%96%B4%20%EB%B4%84",
            ],
            "priority": "HIGH",
            "oneLine": "시즌 초 매출 집중 발생",
            "summary": "봄 시즌 진입과 동시에 골프웨어 매출이 빠르게 상승.",
            "insight": "초기 2~3주 매출 집중 → 진열/재고/프로모션 타이밍이 핵심.",
            "actions": [
                "신상품 전면 배치",
                "초기 집중 프로모션",
                "브랜드별 핵심 상품 선점",
            ],
        },
    ],
    "골프 경기": [
        {
            "id": "event-1",
            "date": "04.02",
            "source": "골프경제신문",
            "title": "스크린골프 대회 결선",
            "articleUrl": "https://www.golfbiz.co.kr/news/articleView.html?idxno=26084",
            "priority": "HIGH",
            "oneLine": "참여형 골프 콘텐츠 확대",
            "summary": "스크린골프 대회 결선이 진행되며 대중 참여형 콘텐츠 확대.",
            "insight": "오프라인 매장에서도 참여형 이벤트로 확장 가능. 특히 젊은 고객 유입 효과 기대.",
            "actions": [
                "스크린골프 이벤트 운영",
                "참여형 대회 기획",
                "SNS 인증 이벤트",
            ],
        },
        {
            "id": "event-2",
            "date": "04.03",
            "source": "KLPGA",
            "title": "여자 골프 시즌 개막",
            "articleUrls": [
                "https://search.naver.com/search.naver?where=news&query=KLPGA",
                "https://search.naver.com/search.naver?where=news&query=%EC%97%AC%EC%9E%90%EA%B3%A8%ED%94%84",
            ],
            "priority": "MID",
            "oneLine": "여성 골프 수요 증가",
            "summary": "투어 개막과 함께 여성 골프 관심 증가.",
            "insight": "여성 고객 중심 상품군 강화 타이밍. 특히 웨어 중심 매출 확대 가능.",
            "actions": [
                "여성 골프웨어 기획전",
                "여성 전용 존 구성",
            ],
        },
    ],
    "골프장 현황": [
        {
            "id": "course-1",
            "date": "04.10",
            "source": "국내보도",
            "title": "골프장 예약 증가",
            "articleUrls": [
                "https://search.naver.com/search.naver?where=news&query=%EA%B3%A8%ED%94%84%EC%9E%A5%20%EC%98%88%EC%95%BD",
                "https://search.naver.com/search.naver?where=news&query=%EB%9D%BC%EC%9A%B4%EB%94%A9%20%EC%88%98%EC%9A%94",
            ],
            "priority": "HIGH",
            "oneLine": "라운딩 수요 증가",
            "summary": "봄 시즌 진입과 함께 라운딩 예약 급증.",
            "insight": "실제 필드 수요 증가 = 구매 시점 도래. 장비·웨어 동시 판매 기회.",
            "actions": [
                "주말 집중 프로모션",
                "라운딩 연계 패키지",
            ],
        },
    ],
    "기타 이슈": [
        {
            "id": "other-1",
            "date": "04월",
            "source": "국내 스포츠",
            "title": "러닝 시장 급성장",
            "articleUrls": [
                "https://search.naver.com/search.naver?where=news&query=%EB%9F%AC%EB%8B%9D",
                "https://search.naver.com/search.naver?where=news&query=%EB%A7%88%EB%9D%BC%ED%86%A4",
            ],
            "priority": "HIGH",
            "oneLine": "스포츠 카테고리 확장 기회",
            "summary": "러닝 인구 증가와 함께 관련 상품 매출 확대.",
            "insight": "골프 고객과 동일 라이프스타일 → 교차 판매 및 복합 카테고리 전략 가능.",
            "actions": [
                "러닝 기획전",
                "복합 스포츠 존 구성",
                "골프 고객 대상 교차 제안",
            ],
        },
    ],
}

CATEGORY_DESCRIPTIONS = {
    "골프 브랜드": "브랜드 출시, 신규 라인, 어패럴/용품 트렌드를 바탕으로 매출 기회를 찾는 영역",
    "골프 경기": "국내외 주요 경기와 시즌 이슈를 행사 및 프로모션 타이밍으로 해석하는 영역",
    "골프장 현황": "예약, 수요, 회원권·라운딩 흐름을 통해 구매 시점을 판단하는 영역",
    "기타 이슈": "러닝·레저·스포츠웨어 등 타 스포츠 카테고리의 확장 기회를 보는 영역",
}

PRIORITY_ORDER = {"HIGH": 0, "MID": 1, "LOW": 2}
PRIORITY_LABEL = {"HIGH": "HIGH", "MID": "MID", "LOW": "LOW"}

if "selected_cards" not in st.session_state:
    st.session_state.selected_cards = []

def sort_cards(cards):
    return sorted(cards, key=lambda x: PRIORITY_ORDER.get(x["priority"], 99))

def add_selected(card):
    if any(c["id"] == card["id"] for c in st.session_state.selected_cards):
        return
    st.session_state.selected_cards.append(card)

st.markdown("""
<style>
.block-container {
    max-width: 1280px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}
.hero {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 28px;
    padding: 28px;
    box-shadow: 0 12px 32px rgba(15, 23, 42, 0.05);
    margin-bottom: 1.5rem;
}
.panel {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 24px;
    padding: 20px;
    box-shadow: 0 8px 22px rgba(15, 23, 42, 0.04);
}
.card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 28px;
    padding: 24px;
    box-shadow: 0 10px 28px rgba(15, 23, 42, 0.04);
}
.subcard {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 18px;
    padding: 16px;
    height: 100%;
}
.badge-high {
    background: #0f172a;
    color: white;
    border: 1px solid #0f172a;
    padding: 4px 12px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 600;
}
.badge-mid {
    background: #eff6ff;
    color: #1d4ed8;
    border: 1px solid #dbeafe;
    padding: 4px 12px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 600;
}
.badge-low {
    background: white;
    color: #64748b;
    border: 1px solid #e2e8f0;
    padding: 4px 12px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 600;
}
.one-line {
    background: #eff6ff;
    border: 1px solid #dbeafe;
    color: #1e3a8a;
    border-radius: 16px;
    padding: 12px 16px;
    font-size: 14px;
    font-weight: 600;
}
.link-chip {
    display: inline-block;
    border: 1px solid #e2e8f0;
    background: white;
    color: #475569;
    border-radius: 12px;
    padding: 8px 12px;
    font-size: 12px;
    font-weight: 500;
    text-decoration: none;
    margin-right: 8px;
    margin-top: 8px;
}
.link-chip-primary {
    display: inline-block;
    border: 1px solid #dbeafe;
    background: #eff6ff;
    color: #1d4ed8;
    border-radius: 12px;
    padding: 8px 12px;
    font-size: 12px;
    font-weight: 600;
    text-decoration: none;
    margin-right: 8px;
    margin-top: 8px;
}
.small-muted {
    font-size: 12px;
    color: #94a3b8;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <div style="display:inline-flex;align-items:center;gap:8px;border:1px solid #dbeafe;background:#eff6ff;color:#1d4ed8;border-radius:999px;padding:4px 12px;font-size:12px;font-weight:600;">
    ✨ Weekly Retail Insight
  </div>
  <h1 style="margin:14px 0 0 0;font-size:32px;font-weight:700;color:#020617;">골프 산업 인사이트</h1>
  <p style="margin-top:12px;max-width:860px;font-size:14px;line-height:1.9;color:#475569;">
    백화점 골프 상품군 MD가 매주 참고할 핵심 기사만 선별해, 기사 요약에서 끝나지 않고 실제 행사와 판매 전략으로 연결할 수 있도록 정리한 화면입니다.
  </p>
</div>
""", unsafe_allow_html=True)

content_col, side_col = st.columns([3.2, 1.2], gap="large")

with content_col:
    category = st.radio(
        "카테고리",
        list(DATA.keys()),
        horizontal=True,
        label_visibility="collapsed",
    )

    st.markdown(
        f"""
        <div class="panel" style="margin-bottom:16px;">
          <div style="font-size:14px;font-weight:700;color:#1e293b;margin-bottom:8px;">카테고리 설명</div>
          <div style="font-size:14px;line-height:1.8;color:#475569;">{CATEGORY_DESCRIPTIONS[category]}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cards = sort_cards(DATA[category])

    for card in cards:
        badge_cls = {
            "HIGH": "badge-high",
            "MID": "badge-mid",
            "LOW": "badge-low",
        }[card["priority"]]

        st.markdown('<div class="card">', unsafe_allow_html=True)

        top_left, top_right = st.columns([5, 1.2], gap="small")
        with top_left:
            st.markdown(f'<div class="small-muted">{card["date"]} · {card["source"]}</div>', unsafe_allow_html=True)
            st.markdown(f'### {card["title"]}')
        with top_right:
            st.markdown(f'<div style="text-align:right;"><span class="{badge_cls}">{card["priority"]}</span></div>', unsafe_allow_html=True)

        st.markdown(f'<div class="one-line">✨ {card["oneLine"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="margin-top:16px;font-size:14px;line-height:1.9;color:#475569;">{card["summary"]}</div>', unsafe_allow_html=True)

        with st.expander("MD 인사이트 보기"):
            exp1, exp2 = st.columns(2, gap="large")
            with exp1:
                st.markdown('<div class="subcard">', unsafe_allow_html=True)
                st.markdown("**인사이트**")
                st.write(card["insight"])
                st.markdown("</div>", unsafe_allow_html=True)
            with exp2:
                st.markdown('<div class="subcard">', unsafe_allow_html=True)
                st.markdown("**실행**")
                for action in card["actions"]:
                    st.markdown(f"- {action}")
                st.markdown("</div>", unsafe_allow_html=True)

        btn1, btn2 = st.columns([1.2, 1], gap="small")
        with btn1:
            already = any(c["id"] == card["id"] for c in st.session_state.selected_cards)
            if st.button("채택됨" if already else "실행안 채택", key=f"select_{card['id']}", disabled=already, use_container_width=True):
                add_selected(card)
                st.rerun()
        with btn2:
            st.button("보류", key=f"hold_{card['id']}", use_container_width=True)

        links_html = ""
        if "articleUrl" in card:
            links_html += f'<a class="link-chip-primary" href="{card["articleUrl"]}" target="_blank" rel="noreferrer">대표 기사 보기</a>'
        if "articleUrls" in card:
            for idx, url in enumerate(card["articleUrls"], start=1):
                links_html += f'<a class="link-chip" href="{url}" target="_blank" rel="noreferrer">관련 기사 {idx}</a>'

        st.markdown(f'<div style="margin-top:10px;">{links_html}</div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown('<div style="height:16px;"></div>', unsafe_allow_html=True)

with side_col:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown("#### 실행 리스트")
    if not st.session_state.selected_cards:
        st.markdown('<div style="font-size:14px;color:#64748b;line-height:1.8;">아직 채택한 실행안이 없습니다.</div>', unsafe_allow_html=True)
    else:
        for item in st.session_state.selected_cards:
            st.markdown(
                f"""
                <div style="border:1px solid #e2e8f0;border-radius:18px;background:#f8fafc;padding:14px;margin-top:10px;">
                    <div class="small-muted">{item["date"]} · {item["source"]}</div>
                    <div style="margin-top:4px;font-size:14px;font-weight:600;color:#0f172a;line-height:1.6;">{item["title"]}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    st.markdown("</div>", unsafe_allow_html=True)
