import streamlit as st

st.set_page_config(
    page_title="골프 산업 인사이트 대시보드",
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
            "oneLine": "브랜드와 선수단 서사가 함께 움직이는 시즌 초반 콘텐츠 기회",
            "summary": "대보골프단이 KPGA와 KLPGA 선수 6명으로 2026 시즌 출정식을 진행하며 시즌 운영 방향과 선수 구성을 공개했다.",
            "insight": "선수단, 후원, 시즌 출발 서사가 함께 붙는 경우 브랜드 행사 명분으로 활용도가 높다.",
            "actions": [
                "선수 후원 브랜드 연계 기획전",
                "시즌 출정 테마 진열",
                "스포츠 마케팅 협업 검토",
            ],
        },
        {
            "id": "brand-2",
            "date": "04.14",
            "source": "매일경제",
            "title": "툴롱골프 2026 헤리티지 컬렉션 공개",
            "articleUrl": "https://www.mk.co.kr/news/sports/12016692",
            "priority": "HIGH",
            "oneLine": "프리미엄 장비는 우수고객 중심 체험형 판매로 전환 필요",
            "summary": "프리미엄 퍼터 신제품 공개로 고가 장비 시장 경쟁 심화.",
            "insight": "고가 제품은 설명형·체험형 판매 구조가 매출 전환에 유리하다.",
            "actions": [
                "우수고객 장비 상담회",
                "시타 체험 이벤트",
                "프리미엄 존 구성",
            ],
        },
        {
            "id": "brand-3",
            "date": "04.05",
            "source": "골프경제신문",
            "title": "캘러웨이골프 백화점 팝업 운영",
            "articleUrl": "https://www.golfbiz.co.kr/news/userWriterArticleView.html?idxno=25882",
            "priority": "HIGH",
            "oneLine": "타 백화점 팝업 사례는 바로 벤치마킹 가능",
            "summary": "백화점 내 체험형 팝업 운영 사례 등장.",
            "insight": "동종 유통 채널 사례는 즉시 적용 가능한 아이디어다.",
            "actions": [
                "점포 팝업 기획",
                "체험형 콘텐츠 도입",
                "강남 상권 테스트",
            ],
        },
        {
            "id": "brand-4",
            "date": "04.09",
            "source": "패션비즈",
            "title": "골프웨어 브랜드 봄 시즌 매출 상승",
            "articleUrls": [
                "https://search.naver.com/search.naver?where=news&query=골프웨어%20매출",
                "https://search.naver.com/search.naver?where=news&query=골프웨어%20봄%20시즌",
            ],
            "priority": "HIGH",
            "oneLine": "시즌 초 매출 상승은 빠른 진열 전환 타이밍",
            "summary": "봄 시즌 진입과 함께 주요 골프웨어 매출 상승.",
            "insight": "초반 진열 속도가 매출을 좌우.",
            "actions": [
                "신상품 전면 배치",
                "초기 판촉 강화",
                "브랜드별 히트상품 선점",
            ],
        },
    ],
    "골프 경기": [
        {
            "id": "event-1",
            "date": "04.02",
            "source": "골프경제신문",
            "title": "골프존 WG투어 결선 개최",
            "articleUrl": "https://www.golfbiz.co.kr/news/articleView.html?idxno=26084",
            "priority": "HIGH",
            "oneLine": "스크린골프는 대중 참여형 이벤트로 활용 가능",
            "summary": "스크린골프 대회 결선 진행.",
            "insight": "접근성 높은 이벤트로 고객 참여 유도 가능.",
            "actions": ["스크린골프 이벤트", "체험형 행사", "협업 기획"],
        },
        {
            "id": "event-2",
            "date": "04.03",
            "source": "KLPGA",
            "title": "드림투어 개막",
            "articleUrls": [
                "https://search.naver.com/search.naver?where=news&query=KLPGA%20개막",
                "https://search.naver.com/search.naver?where=news&query=여자골프%20시즌",
            ],
            "priority": "MID",
            "oneLine": "여성 골프 시즌 시작 신호",
            "summary": "여성 골프 투어 시즌 시작.",
            "insight": "여성 고객 타겟 행사 기회.",
            "actions": ["여성 기획전", "시즌 이벤트"],
        },
        {
            "id": "event-3",
            "date": "04.08",
            "source": "KPGA",
            "title": "남자 투어 일정 발표",
            "articleUrls": [
                "https://search.naver.com/search.naver?where=news&query=KPGA%20일정",
                "https://search.naver.com/search.naver?where=news&query=남자골프%20시즌",
            ],
            "priority": "MID",
            "oneLine": "남성 골프 수요 증가 신호",
            "summary": "KPGA 시즌 일정 공개.",
            "insight": "남성 상품 강화 타이밍.",
            "actions": ["남성 상품 집중", "장비 판촉"],
        },
    ],
    "골프장 현황": [
        {
            "id": "course-1",
            "date": "04.08",
            "source": "회원권시장",
            "title": "골프회원권 시세 혼조",
            "articleUrl": "https://poiup01.tistory.com/269",
            "priority": "HIGH",
            "oneLine": "VIP 고객 전략은 여전히 유효",
            "summary": "회원권 시장 혼조세.",
            "insight": "고가 고객 중심 전략 필요.",
            "actions": ["VIP 행사", "프리미엄 상담"],
        },
        {
            "id": "course-2",
            "date": "04.10",
            "source": "국내보도",
            "title": "골프장 예약 증가",
            "articleUrls": [
                "https://search.naver.com/search.naver?where=news&query=골프장%20예약%20증가",
                "https://search.naver.com/search.naver?where=news&query=골프%20라운딩%20수요",
            ],
            "priority": "HIGH",
            "oneLine": "라운딩 증가 = 구매 타이밍 도래",
            "summary": "봄 시즌 예약 증가.",
            "insight": "주말 매출 집중 가능.",
            "actions": ["주말 프로모션", "라운딩 연계 할인"],
        },
    ],
    "기타 이슈": [
        {
            "id": "other-1",
            "date": "04월",
            "source": "골프저널",
            "title": "골프웨어 시장 둔화",
            "articleUrl": "https://www.golfjournal.co.kr/news/articleView.html?idxno=10839",
            "priority": "HIGH",
            "oneLine": "브랜드 수 확대보다 효율 관리 필요",
            "summary": "골프웨어 시장 둔화.",
            "insight": "핵심 브랜드 중심 전략 필요.",
            "actions": ["브랜드 구조 재정비", "핵심 상품 집중"],
        },
        {
            "id": "other-2",
            "date": "04월",
            "source": "골프저널",
            "title": "골프 테크 확대",
            "articleUrl": "https://www.golfjournal.co.kr/news/articleView.html?idxno=10832",
            "priority": "MID",
            "oneLine": "체험형 매장 전환 필요",
            "summary": "골프 산업의 기술화.",
            "insight": "경험형 소비 확대.",
            "actions": ["체험존 기획", "테크 상품 테스트"],
        },
        {
            "id": "other-3",
            "date": "04.07~04.12",
            "source": "국내 보도 종합",
            "title": "러닝화·러닝용품 수요 증가",
            "articleUrls": [
                "https://search.naver.com/search.naver?where=news&query=러닝화%20매출%20증가",
                "https://search.naver.com/search.naver?where=news&query=러닝%20인구%20증가",
                "https://search.naver.com/search.naver?where=news&query=마라톤%20대회%20참가자%20증가",
            ],
            "priority": "HIGH",
            "oneLine": "러닝 붐 → 스포츠 카테고리 집객 아이템으로 즉시 활용 가능",
            "summary": "봄 시즌 러닝 인구 증가와 함께 러닝화, 기능성 웨어 매출이 동반 상승하는 흐름.",
            "insight": "골프 외 스포츠 카테고리에서도 입문형 고객 유입이 증가하는 시기라 교차 판매 기회로 활용 가능.",
            "actions": ["러닝 테마 기획전", "입문자 패키지 구성", "골프 고객 대상 교차 제안"],
        },
        {
            "id": "other-4",
            "date": "04.05~04.13",
            "source": "국내 유통 기사",
            "title": "아웃도어·레저 카테고리 매출 회복",
            "articleUrls": [
                "https://search.naver.com/search.naver?where=news&query=아웃도어%20매출%20회복",
                "https://search.naver.com/search.naver?where=news&query=캠핑%20레저%20시장%20동향",
            ],
            "priority": "MID",
            "oneLine": "야외활동 증가 → 레저 상품군 동반 성장",
            "summary": "봄 시즌 야외활동 증가로 아웃도어, 캠핑, 레저 카테고리 매출이 회복세를 보임.",
            "insight": "골프와 동일한 야외활동 카테고리로 묶어 공동 프로모션 기획 가능.",
            "actions": ["레저 연계 기획전", "골프+아웃도어 묶음 프로모션", "야외활동 시즌 테마존 구성"],
        },
        {
            "id": "other-5",
            "date": "04.03~04.11",
            "source": "국내 스포츠 산업 기사",
            "title": "기능성 스포츠웨어 수요 확대",
            "articleUrls": [
                "https://search.naver.com/search.naver?where=news&query=기능성%20스포츠웨어%20수요",
                "https://search.naver.com/search.naver?where=news&query=애슬레저%20시장%20동향",
            ],
            "priority": "MID",
            "oneLine": "일상복+운동복 경계 붕괴 → 매장 구성 전략 변화 필요",
            "summary": "애슬레저 트렌드 확산으로 기능성 의류가 일상복으로 확대되는 흐름.",
            "insight": "골프웨어 역시 일상 착용 비중 증가 → 라이프스타일 진열 전략 필요.",
            "actions": ["라이프스타일 존 구성", "애슬레저 상품 강화", "골프웨어 활용도 강조 진열"],
        },
    ],
}

CATEGORY_DESCRIPTIONS = {
    "골프 브랜드": "어패럴, 용품, 신규 라인, 브랜드 출시 및 팝업 등 상품군 관점에서 참고할 뉴스를 모은 영역",
    "골프 경기": "국내외 주요 경기와 시즌 흐름을 바탕으로 행사 명분과 판촉 시점을 잡는 영역",
    "골프장 현황": "라운딩 객수, 회원권 시장, 골프장 업황 등 수요 강도와 고객 레벨을 파악하는 영역",
    "기타 이슈": "골프 외에도 스포츠 상품군 전반에 참고 가능한 기술, 소비, 구조 변화 이슈를 담는 영역",
}

PRIORITY_ORDER = {"HIGH": 0, "MID": 1, "LOW": 2}
PRIORITY_LABEL = {"HIGH": "높음", "MID": "중간", "LOW": "낮음"}
PRIORITY_COLOR = {"HIGH": "#dc2626", "MID": "#b45309", "LOW": "#475569"}
PRIORITY_BG = {"HIGH": "#fee2e2", "MID": "#fef3c7", "LOW": "#e2e8f0"}

if "selected_ideas" not in st.session_state:
    st.session_state.selected_ideas = []
if "expanded_cards" not in st.session_state:
    st.session_state.expanded_cards = set()

def toggle_card(card_id: str):
    expanded = set(st.session_state.expanded_cards)
    if card_id in expanded:
        expanded.remove(card_id)
    else:
        expanded.add(card_id)
    st.session_state.expanded_cards = expanded

def add_idea(card: dict, category_name: str):
    if any(item["id"] == card["id"] for item in st.session_state.selected_ideas):
        return
    type_map = {
        "골프 브랜드": "기획전",
        "골프 경기": "이벤트",
        "골프장 현황": "프로모션",
        "기타 이슈": "확장 검토",
    }
    st.session_state.selected_ideas.append(
        {"id": card["id"], "title": card["title"], "type": type_map.get(category_name, "검토"), "priority": card["priority"]}
    )

def sort_cards(cards):
    return sorted(cards, key=lambda x: PRIORITY_ORDER.get(x["priority"], 99))

def generate_store_insight(card, store_name, sales_level, core_age, top_brand, avg_ticket):
    insights = []
    if sales_level == "높음":
        insights.append(f"{store_name}은 이미 골프 수요가 높은 점포이므로, '{card['title']}' 이슈를 단기 매출화하는 팝업/기획전 적용 우선순위가 높습니다.")
    elif sales_level == "보통":
        insights.append(f"{store_name}은 중간 수준 매출 점포로, '{card['title']}' 이슈를 파일럿 행사나 주말 집중 프로모션 형태로 테스트해볼 만합니다.")
    else:
        insights.append(f"{store_name}은 골프 매출 기반이 아직 크지 않으므로, '{card['title']}' 이슈는 대형 행사보다 소규모 콘텐츠형 운영이나 교차 제안으로 접근하는 것이 적절합니다.")
    if "여성" in card["insight"] or "웨어" in card["title"] or "골프웨어" in card["title"]:
        insights.append(f"핵심 고객 연령대가 {core_age}인 점을 고려하면, 여성/라이프스타일형 진열 및 코디 제안 강화가 유효할 수 있습니다.")
    if "장비" in card["title"] or "퍼터" in card["summary"] or "프리미엄" in card["oneLine"]:
        insights.append(f"현재 상위 브랜드가 {top_brand}이고 평균 객단가가 {avg_ticket:,}원 수준이라면, 프리미엄 장비 제안이나 우수고객 상담형 행사와의 결합이 적합합니다.")
    if "러닝" in card["title"] or "아웃도어" in card["title"] or "애슬레저" in card["title"]:
        insights.append(f"골프 외 스포츠 이슈는 {store_name}의 스포츠 상품군 확장 전략과 함께 검토하면 교차 판매 가능성을 높일 수 있습니다.")
    if not insights:
        insights.append(f"{store_name} 점포 기준으로는 '{card['title']}' 이슈를 내부 매출 데이터와 함께 검토한 뒤 적용 여부를 판단하는 것이 적절합니다.")
    return insights

st.markdown(
    '''
    <style>
    .main .block-container {padding-top: 2rem; padding-bottom: 2rem; max-width: 1280px;}
    .hero-card, .desc-card, .news-card, .side-card {
        background: white; border: 1px solid #e2e8f0;
    }
    .hero-card {border-radius: 24px; padding: 28px; margin-bottom: 16px;}
    .desc-card {border-radius: 18px; padding: 20px; margin-bottom: 18px;}
    .news-card {border-radius: 24px; padding: 22px; margin-bottom: 16px;}
    .sub-card {background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 18px; padding: 16px; height: 100%;}
    .side-card {border-radius: 24px; padding: 20px; margin-bottom: 16px;}
    .idea-card {background: white; border: 1px solid #e2e8f0; border-radius: 16px; padding: 14px; margin-bottom: 10px;}
    .small-label {font-size: 12px; color: #94a3b8;}
    </style>
    ''',
    unsafe_allow_html=True,
)

st.markdown(
    '''
    <div class="hero-card">
        <h1 style="margin:0; font-size:30px;">골프 산업 인사이트 대시보드</h1>
        <p style="color:#64748b; margin-top:10px; line-height:1.7;">
            2026년 4월 1일에서 15일 사이 릴리즈된 실제 국내 기사와 공식 소스를 바탕으로,
            백화점 골프 상품군 MD가 참고할 만한 이슈를 선별하고,
            향후 점포 데이터 결합 시 실행 인사이트까지 도출할 수 있도록 설계한 화면입니다.
        </p>
    </div>
    ''',
    unsafe_allow_html=True,
)

tab_news, tab_store = st.tabs(["외부 기사 기반 브리핑", "점포 데이터 결합 인사이트"])

with tab_news:
    active_category = st.radio("카테고리", list(DATA.keys()), horizontal=True, label_visibility="collapsed")
    cards = sort_cards(DATA[active_category])

    st.markdown(
        f'''
        <div class="desc-card">
            <div style="font-weight:700; margin-bottom:8px;">카테고리 설명</div>
            <div style="font-size:14px; color:#475569; line-height:1.7;">{CATEGORY_DESCRIPTIONS[active_category]}</div>
            <div style="border-top:1px solid #e2e8f0; margin-top:14px; padding-top:14px;">
                <div style="font-weight:700; margin-bottom:8px;">중요도 기준</div>
                <ul style="margin:0; padding-left:18px; color:#475569; font-size:14px; line-height:1.8;">
                    <li><b>HIGH</b>: 백화점 행사, 팝업, 프로모션으로 바로 연결 가능한 기사</li>
                    <li><b>MID</b>: 참고할 가치가 높지만 점포 데이터나 추가 검토가 필요한 기사</li>
                    <li><b>LOW</b>: 시장 배경 이해에는 필요하지만 즉시 실행 연결성은 낮은 기사</li>
                </ul>
            </div>
        </div>
        ''',
        unsafe_allow_html=True,
    )

    main_col, side_col = st.columns([3, 1.1], gap="large")

    with main_col:
        for card in cards:
            st.markdown(
                f'''
                <div class="news-card">
                    <div style="display:flex; justify-content:space-between; gap:16px; align-items:flex-start;">
                        <div>
                            <div class="small-label">{card["date"]} · {card["source"]}</div>
                            <div style="font-size:22px; font-weight:700; margin-top:6px;">{card["title"]}</div>
                        </div>
                        <div style="font-size:12px; font-weight:700; color:{PRIORITY_COLOR[card["priority"]]}; background:{PRIORITY_BG[card["priority"]]}; padding:6px 10px; border-radius:999px;">
                            중요도 {PRIORITY_LABEL[card["priority"]]}
                        </div>
                    </div>
                    <div style="margin-top:14px; background:#f1f5f9; border-radius:14px; padding:10px 14px; font-size:14px; font-weight:600; color:#334155;">
                        ✨ {card["oneLine"]}
                    </div>
                    <div style="margin-top:14px; font-size:14px; color:#475569; line-height:1.8;">
                        {card["summary"]}
                    </div>
                </div>
                ''',
                unsafe_allow_html=True,
            )

            b1, b2, b3 = st.columns([1.1, 1.1, 2.3])
            with b1:
                if st.button("MD 인사이트 보기" if card["id"] not in st.session_state.expanded_cards else "접기", key=f"expand_{card['id']}", use_container_width=True):
                    toggle_card(card["id"])
                    st.rerun()
            with b2:
                if st.button("실행안 채택", key=f"apply_{card['id']}", use_container_width=True):
                    add_idea(card, active_category)
                    st.rerun()
            with b3:
                st.empty()

            if card["id"] in st.session_state.expanded_cards:
                c1, c2 = st.columns(2)
                with c1:
                    st.markdown(f'<div class="sub-card"><div style="font-weight:700; margin-bottom:8px;">MD 인사이트</div><div style="font-size:14px; color:#475569; line-height:1.8;">{card["insight"]}</div></div>', unsafe_allow_html=True)
                with c2:
                    actions_html = "".join([f"<li>{a}</li>" for a in card["actions"]])
                    st.markdown(f'<div class="sub-card"><div style="font-weight:700; margin-bottom:8px;">백화점 적용</div><ul style="margin:0; padding-left:18px; font-size:14px; color:#475569; line-height:1.8;">{actions_html}</ul></div>', unsafe_allow_html=True)

            link_cols = st.columns([1, 3])
            with link_cols[0]:
                if "articleUrl" in card:
                    st.link_button("대표 기사 보기", card["articleUrl"], use_container_width=True)
            with link_cols[1]:
                if "articleUrls" in card:
                    sub_cols = st.columns(len(card["articleUrls"]))
                    for idx, url in enumerate(card["articleUrls"]):
                        with sub_cols[idx]:
                            st.link_button(f"관련 기사 {idx+1}", url, use_container_width=True)

            st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

    with side_col:
        st.markdown('<div class="side-card"><div style="font-size:20px; font-weight:700; margin-bottom:12px;">실행 리스트</div>', unsafe_allow_html=True)
        if st.session_state.selected_ideas:
            for item in st.session_state.selected_ideas:
                st.markdown(
                    f'''
                    <div class="idea-card">
                        <div style="display:flex; justify-content:space-between; gap:8px; align-items:center;">
                            <div style="font-size:12px; color:#64748b;">{item["type"]}</div>
                            <div style="font-size:11px; font-weight:700; color:{PRIORITY_COLOR[item["priority"]]}; background:{PRIORITY_BG[item["priority"]]}; padding:4px 8px; border-radius:999px;">
                                {item["priority"]}
                            </div>
                        </div>
                        <div style="font-weight:700; margin-top:6px; line-height:1.5;">{item["title"]}</div>
                    </div>
                    ''',
                    unsafe_allow_html=True,
                )
        else:
            st.caption("아직 채택한 실행안이 없습니다.")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown(
            '''
            <div class="side-card">
                <div style="font-size:20px; font-weight:700; margin-bottom:12px;">운영 원칙</div>
                <ul style="margin:0; padding-left:18px; font-size:14px; color:#475569; line-height:1.8;">
                    <li>기사 요약, 인사이트, 실행안을 한 카드 안에서 검토</li>
                    <li>중요도 순으로 먼저 보여서 우선순위 판단 속도 개선</li>
                    <li>향후 점포별 내부 데이터 결합 시 실행 우선순위 정교화 가능</li>
                </ul>
            </div>
            ''',
            unsafe_allow_html=True,
        )

with tab_store:
    st.subheader("점포 데이터 결합 인사이트")
    st.caption("아래 값은 예시 입력 영역입니다. 실제로는 점포별 골프 매출, 브랜드 매출, 객단가, 고객 연령대를 연결하면 됩니다.")

    left, right = st.columns([1.2, 2])

    with left:
        store_name = st.text_input("점포명", value="잠실점")
        sales_level = st.selectbox("골프 매출 수준", ["높음", "보통", "낮음"])
        core_age = st.selectbox("핵심 고객 연령대", ["30대", "40대", "50대", "60대 이상"])
        top_brand = st.text_input("상위 브랜드", value="타이틀리스트")
        avg_ticket = st.number_input("평균 객단가(원)", min_value=0, value=350000, step=10000)

        category_for_store = st.selectbox("인사이트를 볼 카테고리", list(DATA.keys()))
        card_options = sort_cards(DATA[category_for_store])
        selected_title = st.selectbox("적용 검토 기사", [c["title"] for c in card_options])
        selected_card = next(c for c in card_options if c["title"] == selected_title)

    with right:
        st.markdown(
            f'''
            <div class="desc-card">
                <div style="font-weight:700; margin-bottom:6px;">선택 기사</div>
                <div style="font-size:20px; font-weight:700;">{selected_card["title"]}</div>
                <div style="margin-top:10px; font-size:14px; color:#64748b;">{selected_card["date"]} · {selected_card["source"]}</div>
                <div style="margin-top:14px; background:#f1f5f9; border-radius:14px; padding:10px 14px; font-size:14px; font-weight:600; color:#334155;">
                    ✨ {selected_card["oneLine"]}
                </div>
                <div style="margin-top:14px; font-size:14px; color:#475569; line-height:1.8;">
                    {selected_card["summary"]}
                </div>
            </div>
            ''',
            unsafe_allow_html=True,
        )

        store_insights = generate_store_insight(selected_card, store_name, sales_level, core_age, top_brand, avg_ticket)

        st.markdown('<div class="side-card"><div style="font-size:20px; font-weight:700; margin-bottom:12px;">점포 적용 인사이트</div>', unsafe_allow_html=True)
        for idx, insight in enumerate(store_insights, start=1):
            st.markdown(f"{idx}. {insight}")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="side-card"><div style="font-size:20px; font-weight:700; margin-bottom:12px;">추천 실행안</div>', unsafe_allow_html=True)
        for action in selected_card["actions"]:
            st.markdown(f"- {action}")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown(
            f'''
            <div class="desc-card">
                <div style="font-weight:700; margin-bottom:6px;">예상 적용 방향</div>
                <div style="font-size:14px; color:#475569; line-height:1.8;">
                    {store_name} 기준으로 현재 골프 매출 수준은 <b>{sales_level}</b>, 핵심 고객은 <b>{core_age}</b>,
                    상위 브랜드는 <b>{top_brand}</b>, 평균 객단가는 <b>{avg_ticket:,}원</b>으로 입력되어 있습니다.
                    이 데이터를 바탕으로 외부 기사 이슈를 점포 실행안으로 변환하는 구조입니다.
                </div>
            </div>
            ''',
            unsafe_allow_html=True,
        )
