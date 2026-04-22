
import streamlit as st

st.set_page_config(
    page_title="롯데 석주 주간 골프 MD 뉴스 알림",
    page_icon="⛳이석주",
    layout="wide",
)

DATA = {
    "골프 브랜드": [
        {
            "id": "brand-1",
            "date": "04.06",
            "source": "골프경제신문",
            "title": "대보골프단, 2026 시즌 출정식 진행",
            "priority": "HIGH",
            "oneLine": "브랜드와 선수단 서사가 결합되는 시즌 초 핵심 콘텐츠",
            "summary": "KPGA·KLPGA 선수단 구성 공개와 함께 시즌 전략 발표가 진행되며 브랜드 스토리 노출이 확대됨.",
            "headlines": [
                {"title": "KPGA·KLPGA 선수단 6명 구성 공개", "url": "https://search.naver.com/search.naver?where=news&query=KPGA%20선수단"},
                {"title": "시즌 출정식 통해 운영 방향 발표", "url": "https://search.naver.com/search.naver?where=news&query=골프단%20출정식"},
                {"title": "브랜드 후원 노출 확대 계획 언급", "url": "https://search.naver.com/search.naver?where=news&query=골프%20후원%20브랜드"},
            ],
            "insight": "시즌 출정·선수단 이슈는 단순 판촉보다 ‘이유 있는 행사’로 활용 가능.",
            "actions": ["선수 협업 팝업", "시즌 테마 매장 구성"],
        },
        {
            "id": "brand-2",
            "date": "04.14",
            "source": "매일경제",
            "title": "프리미엄 골프 장비 시장 확대",
            "priority": "HIGH",
            "oneLine": "고가 장비 중심 소비 확대",
            "summary": "퍼터, 클럽 등 고가 장비 판매 비중 증가로 프리미엄 시장 경쟁 심화.",
            "headlines": [
                {"title": "프리미엄 퍼터 판매 비중 상승", "url": "https://search.naver.com/search.naver?where=news&query=프리미엄%20퍼터"},
                {"title": "고가 장비 시장 경쟁 심화", "url": "https://search.naver.com/search.naver?where=news&query=골프%20장비%20시장"},
                {"title": "브랜드별 상위 라인 강화", "url": "https://search.naver.com/search.naver?where=news&query=골프%20브랜드%20라인"},
            ],
            "insight": "체험형·상담형 판매 구조 필요.",
            "actions": ["시타존", "VIP 상담"],
        },
    ],
    "골프 경기": [
        {
            "id": "event-1",
            "date": "04.02",
            "source": "골프경제신문",
            "title": "스크린골프 대회 결선",
            "priority": "HIGH",
            "oneLine": "참여형 골프 콘텐츠 확대",
            "summary": "스크린골프 대회 결선이 진행되며 대중 참여형 콘텐츠 확대.",
            "headlines": [
                {"title": "스크린골프 결선 개최", "url": "https://search.naver.com/search.naver?where=news&query=%EC%8A%A4%ED%81%AC%EB%A6%B0%EA%B3%A8%ED%94%84%20%EA%B2%B0%EC%84%A0"},
                {"title": "참가자 규모 확대", "url": "https://search.naver.com/search.naver?where=news&query=%EC%8A%A4%ED%81%AC%EB%A6%B0%EA%B3%A8%ED%94%84%20%EC%B0%B8%EA%B0%80%EC%9E%90"},
                {"title": "온라인 중계 병행", "url": "https://search.naver.com/search.naver?where=news&query=%EC%8A%A4%ED%81%AC%EB%A6%B0%EA%B3%A8%ED%94%84%20%EC%A4%91%EA%B3%84"},
            ],
            "insight": "오프라인 참여형 이벤트로 확장 가능.",
            "actions": ["매장 이벤트", "참여형 대회"],
        }
    ],
    "골프장 현황": [
        {
            "id": "course-1",
            "date": "04.10",
            "source": "국내보도",
            "title": "골프장 예약 증가",
            "priority": "HIGH",
            "oneLine": "라운딩 수요 증가",
            "summary": "봄 시즌 진입과 함께 라운딩 예약 급증.",
            "headlines": [
                {"title": "주말 예약률 상승", "url": "https://search.naver.com/search.naver?where=news&query=%EA%B3%A8%ED%94%84%EC%9E%A5%20%EC%A3%BC%EB%A7%90%20%EC%98%88%EC%95%BD"},
                {"title": "그린피 일부 상승", "url": "https://search.naver.com/search.naver?where=news&query=%EA%B7%B8%EB%A6%B0%ED%94%BC%20%EC%83%81%EC%8A%B9"},
                {"title": "수도권 중심 수요 집중", "url": "https://search.naver.com/search.naver?where=news&query=%EA%B3%A8%ED%94%84%EC%9E%A5%20%EC%88%98%EB%8F%84%EA%B6%8C%20%EC%88%98%EC%9A%94"},
            ],
            "insight": "구매 타이밍 도래.",
            "actions": ["주말 프로모션", "라운딩 연계 행사"],
        }
    ],
    "기타 이슈": [
        {
            "id": "other-1",
            "date": "04월",
            "source": "국내 스포츠",
            "title": "러닝 시장 급성장",
            "priority": "HIGH",
            "oneLine": "스포츠 카테고리 확장 기회",
            "summary": "러닝 인구 증가와 함께 관련 상품 매출 확대.",
            "headlines": [
                {"title": "러닝화 매출 상승", "url": "https://search.naver.com/search.naver?where=news&query=%EB%9F%AC%EB%8B%9D%ED%99%94%20%EB%A7%A4%EC%B6%9C"},
                {"title": "마라톤 참가자 증가", "url": "https://search.naver.com/search.naver?where=news&query=%EB%A7%88%EB%9D%BC%ED%86%A4%20%EC%B0%B8%EA%B0%80%EC%9E%90"},
                {"title": "입문자 유입 확대", "url": "https://search.naver.com/search.naver?where=news&query=%EB%9F%AC%EB%8B%9D%20%EC%9E%85%EB%AC%B8%EC%9E%90"},
            ],
            "insight": "교차 판매 기회.",
            "actions": ["러닝 기획전", "복합 스포츠 존"],
        }
    ],
}

PRIORITY_ORDER = {"HIGH": 0, "MID": 1, "LOW": 2}

STORE_PROFILES = [
    {"name": "잠실점", "annualSales": "350억", "customers": "2만명", "avgTicket": "80만원", "vipRatio": 45, "avgAge": 56, "trait": "롯데월드몰 이용가능"},
    {"name": "본점", "annualSales": "250억", "customers": "1만 5천명", "avgTicket": "90만원", "vipRatio": 50, "avgAge": 47, "trait": "외국인 고객 많음"},
    {"name": "부산본점", "annualSales": "250억", "customers": "1만 8천명", "avgTicket": "80만원", "vipRatio": 40, "avgAge": 51, "trait": "바닷가"},
    {"name": "인천점", "annualSales": "200억", "customers": "1만 2천명", "avgTicket": "80만원", "vipRatio": 35, "avgAge": 43, "trait": "상권단독"},
    {"name": "동탄점", "annualSales": "150억", "customers": "1만명", "avgTicket": "80만원", "vipRatio": 40, "avgAge": 39, "trait": "젊은점포"},
    {"name": "노원점", "annualSales": "130억", "customers": "8천명", "avgTicket": "60만원", "vipRatio": 32, "avgAge": 54, "trait": "포켓상권"},
    {"name": "영등포점", "annualSales": "100억", "customers": "7천명", "avgTicket": "40만원", "vipRatio": 30, "avgAge": 60, "trait": "경쟁열위"},
    {"name": "광복점", "annualSales": "80억", "customers": "6천명", "avgTicket": "40만원", "vipRatio": 28, "avgAge": 55, "trait": "점포는큼"},
    {"name": "미아점", "annualSales": "40억", "customers": "4천명", "avgTicket": "30만원", "vipRatio": 21, "avgAge": 65, "trait": "행사효율 좋음"},
    {"name": "건대점", "annualSales": "40억", "customers": "4천명", "avgTicket": "20만원", "vipRatio": 15, "avgAge": 43, "trait": "골프 부진"},
]

def build_store_idea(store, item):
    suggestions = []

    if ("프리미엄" in item["title"] or "고가" in item["oneLine"] or any(("VIP" in a or "시타" in a) for a in item["actions"])):
        if store["vipRatio"] >= 45 or "90만원" in store["avgTicket"]:
            suggestions.append({
                "title": f'{store["name"]} 프리미엄 장비 제안 행사',
                "idea": f'{item["title"]} 이슈를 활용해 {store["name"]}에서 프리미엄 장비 상담회 또는 시타 행사를 운영하는 안을 검토합니다.',
                "reason": f'{store["name"]}은 객단가가 {store["avgTicket"]} 수준이고 우수고객 구매금액 구성비가 {store["vipRatio"]}%로 높아 프리미엄 상품 제안 수용도가 상대적으로 높습니다. 기사에서도 고가 장비 중심 소비 확대가 확인됩니다.',
            })

    if ("팝업" in item["title"] or any(("팝업" in a or "테마 매장" in a) for a in item["actions"])):
        if store["name"] == "잠실점" or "롯데월드몰" in store["trait"] or "점포는큼" in store["trait"]:
            suggestions.append({
                "title": f'{store["name"]} 체험형 골프 팝업',
                "idea": f'{store["name"]}에서 브랜드 팝업 또는 시즌 테마존을 운영해 집객형 행사로 연결하는 방안을 제안합니다.',
                "reason": f'{store["name"]}은 {store["trait"]} 특성이 있어 유동객 흡수와 체험형 이벤트 운영에 유리합니다. 기사에서 백화점 골프 팝업 확대가 언급돼 실행 명분도 충분합니다.',
            })

    if ("골프웨어" in item["title"] or "매출" in item["oneLine"] or "매출" in item["summary"]):
        if store["avgAge"] >= 50:
            suggestions.append({
                "title": f'{store["name"]} 시즌 웨어 집중 제안',
                "idea": f'{store["name"]}에서 시즌 초 골프웨어 핵심 상품을 전면 배치하고 우수 고객 대상 사전 제안 행사를 운영합니다.',
                "reason": f'{store["name"]} 고객 평균 연령대는 {store["avgAge"]}세로 핵심 골프웨어 구매층과 맞닿아 있습니다. 기사에서도 봄 시즌 웨어 매출 상승이 확인되어 시즌성 대응이 중요합니다.',
            })
        else:
            suggestions.append({
                "title": f'{store["name"]} 젊은 고객형 웨어 콘텐츠 강화',
                "idea": f'{store["name"]}에서 스타일링 중심의 골프웨어 제안전 또는 콘텐츠형 프로모션을 진행합니다.',
                "reason": f'{store["name"]} 고객 평균 연령대는 {store["avgAge"]}세이며 {store["trait"]} 특성이 있어 전통형 행사보다 콘텐츠형 웨어 제안이 더 적합합니다. 기사상 시즌 초 매출 상승 흐름과도 맞습니다.',
            })

    if ("스크린골프" in item["title"] or "참여형" in item["oneLine"]):
        if store["avgAge"] <= 45 or "젊은" in store["trait"] or store["name"] == "건대점":
            suggestions.append({
                "title": f'{store["name"]} 참여형 골프 이벤트',
                "idea": f'{store["name"]}에서 스크린골프 또는 참여형 이벤트를 열어 골프 관심 고객 유입을 확대합니다.',
                "reason": f'{store["name"]}은 평균 연령 {store["avgAge"]}세로 비교적 젊은 고객 비중이 높거나 {store["trait"]} 특성이 있어 체험형 이벤트 반응을 기대할 수 있습니다. 기사에서도 참여형 콘텐츠 확대가 확인됩니다.',
            })

    if ("예약 증가" in item["title"] or "라운딩 수요" in item["oneLine"]):
        suggestions.append({
            "title": f'{store["name"]} 라운딩 수요 대응 프로모션',
            "idea": f'{store["name"]}에서 라운딩 직전 수요를 노린 주말 프로모션이나 장비·웨어 묶음 제안을 운영합니다.',
            "reason": f'기사에서 봄 시즌 예약 증가와 수요 확대가 나타났고, {store["name"]}의 현재 연간 골프 매출 {store["annualSales"]} 및 구매고객수 {store["customers"]}를 감안하면 실구매 전환형 행사로 연결할 여지가 있습니다.',
        })

    if ("러닝" in item["title"] or "스포츠 카테고리" in item["oneLine"]):
        if "젊은" in store["trait"] or "상권단독" in store["trait"] or store["name"] == "잠실점":
            suggestions.append({
                "title": f'{store["name"]} 복합 스포츠 제안',
                "idea": f'{store["name"]}에서 골프와 러닝을 함께 묶은 복합 스포츠존 또는 교차 제안 행사를 기획합니다.',
                "reason": f'{store["name"]}의 특성인 "{store["trait"]}"은 복합 카테고리 확장에 유리합니다. 기사에서도 러닝 시장 급성장이 나타나 골프 고객 대상 교차 판매 명분이 충분합니다.',
            })

    if not suggestions:
        suggestions.append({
            "title": f'{store["name"]} 맞춤 파일럿 검토',
            "idea": f'{item["title"]} 이슈를 기반으로 {store["name"]}에서 소규모 테스트성 행사부터 검토합니다.',
            "reason": f'{store["name"]}의 특성({store["trait"]}), 객단가 {store["avgTicket"]}, 평균 연령 {store["avgAge"]}세를 고려하면 대형 행사보다는 파일럿 운영 후 확대 판단이 적절합니다.',
        })

    return suggestions

def score_idea(store, item):
    score = 0
    if store["vipRatio"] >= 45:
        score += 3
    if store["avgAge"] >= 50:
        score += 2
    if "젊은" in store["trait"]:
        score += 2
    if item["priority"] == "HIGH":
        score += 3
    elif item["priority"] == "MID":
        score += 1
    score += len(item["actions"])
    return score

def build_store_insights(store, selected_cards):
    source_items = selected_cards if selected_cards else [item for items in DATA.values() for item in items]
    ideas = []
    for item in source_items:
        for idea in build_store_idea(store, item):
            ideas.append({
                **idea,
                "score": score_idea(store, item),
                "sourceTitle": item["title"],
            })
    ideas.sort(key=lambda x: x["score"], reverse=True)
    return ideas[:3]

if "page" not in st.session_state:
    st.session_state.page = "news"
if "category" not in st.session_state:
    st.session_state.category = "골프 브랜드"
if "selected_cards" not in st.session_state:
    st.session_state.selected_cards = []
if "expanded_id" not in st.session_state:
    st.session_state.expanded_id = None

st.markdown("""
<style>
.block-container { max-width: 1280px; padding-top: 1.2rem; padding-bottom: 2rem; }
html, body, [data-testid="stAppViewContainer"] { background: #f8fafc; }
.main-nav-spacer { height: 0.2rem; }
.card-wrap { border: 1px solid #e2e8f0; border-radius: 24px; padding: 20px; background: white; margin-bottom: 16px; }
.muted { font-size: 12px; color: #94a3b8; }
.one-line { margin-top: 10px; color: #2563eb; font-size: 14px; font-weight: 500; }
.summary { margin-top: 6px; font-size: 14px; color: #334155; line-height: 1.8; }
.box { margin-top: 14px; border: 1px solid #e2e8f0; background: #f8fafc; border-radius: 16px; padding: 14px; }
.small-title { font-size: 12px; color: #64748b; margin-bottom: 8px; }
.link-chip { display: inline-block; font-size: 12px; color: #0f172a; text-decoration: underline; text-underline-offset: 2px; margin-bottom: 8px; }
.selected-box { border: 1px solid #e2e8f0; border-radius: 18px; padding: 14px; background: #f8fafc; margin-top: 10px; }
.idea-box { border: 1px solid #e2e8f0; border-radius: 18px; padding: 16px; background: #f8fafc; margin-top: 12px; }
</style>
""", unsafe_allow_html=True)

nav1, nav2, _ = st.columns([1.2, 1.6, 8])
with nav1:
    if st.button("뉴스 분석", use_container_width=True, key="nav_news"):
        st.session_state.page = "news"
with nav2:
    if st.button("점포 인사이트", use_container_width=True, key="nav_insight"):
        st.session_state.page = "insight"

st.markdown('<div class="main-nav-spacer"></div>', unsafe_allow_html=True)

if st.session_state.page == "news":
    cat_cols = st.columns(4)
    for i, cat in enumerate(DATA.keys()):
        with cat_cols[i]:
            if st.button(cat, use_container_width=True, key=f"cat_{cat}"):
                st.session_state.category = cat

    cards = sorted(DATA[st.session_state.category], key=lambda x: PRIORITY_ORDER.get(x["priority"], 99))

    for card in cards:
        st.markdown('<div class="card-wrap">', unsafe_allow_html=True)
        top1, top2 = st.columns([7, 1])
        with top1:
            st.markdown(f'<div class="muted">{card["date"]} · {card["source"]}</div>', unsafe_allow_html=True)
            st.markdown(f'### {card["title"]}')
        with top2:
            st.markdown(f'<div style="text-align:right;font-size:12px;">{card["priority"]}</div>', unsafe_allow_html=True)

        st.markdown(f'<div class="one-line">{card["oneLine"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="summary">{card["summary"]}</div>', unsafe_allow_html=True)

        headlines_html = "".join(
            f'<a class="link-chip" href="{h["url"]}" target="_blank" rel="noreferrer">{h["title"]}</a><br/>'
            for h in card["headlines"]
        )
        st.markdown(
            f"""
            <div class="box">
                <div class="small-title">관련 기사</div>
                {headlines_html}
            </div>
            """,
            unsafe_allow_html=True,
        )

        exp_col, _ = st.columns([1, 7])
        with exp_col:
            label = "인사이트 ▲" if st.session_state.expanded_id == card["id"] else "인사이트 ▼"
            if st.button(label, key=f"expand_{card['id']}"):
                st.session_state.expanded_id = None if st.session_state.expanded_id == card["id"] else card["id"]

        if st.session_state.expanded_id == card["id"]:
            info1, info2 = st.columns(2)
            with info1:
                st.markdown("**인사이트**")
                st.write(card["insight"])
            with info2:
                st.markdown("**실행**")
                for action in card["actions"]:
                    st.markdown(f"- {action}")

            bottom_left, bottom_right = st.columns([5, 1.5])
            with bottom_left:
                chips = "".join(
                    f'<a href="{h["url"]}" target="_blank" rel="noreferrer" style="display:inline-block;border:1px solid #e2e8f0;border-radius:12px;padding:8px 12px;margin-right:8px;margin-top:8px;font-size:12px;color:#0f172a;text-decoration:none;background:white;">{h["title"]}</a>'
                    for h in card["headlines"]
                )
                st.markdown(chips, unsafe_allow_html=True)
            with bottom_right:
                already = any(item["id"] == card["id"] for item in st.session_state.selected_cards)
                if st.button("채택됨" if already else "실행안 채택", key=f"select_{card['id']}", disabled=already, use_container_width=True):
                    st.session_state.selected_cards.append(card)
                    st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

else:
    selected_name = st.selectbox("점포 선택", [item["name"] for item in STORE_PROFILES], index=0)
    store = next(item for item in STORE_PROFILES if item["name"] == selected_name)
    insights = build_store_insights(store, st.session_state.selected_cards)

    left, right = st.columns([1.2, 2])
    with left:
        st.markdown("### 점포 선택 및 특성")
        stats = [
            ("연간 골프 매출", store["annualSales"]),
            ("구매고객수", store["customers"]),
            ("객단가", store["avgTicket"]),
            ("우수고객 구성비", f'{store["vipRatio"]}%'),
            ("평균 연령대", f'{store["avgAge"]}세'),
            ("점포 특성", store["trait"]),
        ]
        for k, v in stats:
            st.markdown(
                f"""
                <div class="selected-box">
                    <div class="muted">{k}</div>
                    <div style="margin-top:4px;font-weight:600;">{v}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    with right:
        st.markdown("### 점포 맞춤 제안")
        if not insights:
            st.write("현재 점포 특성과 연결되는 추천 실행안이 없습니다.")
        else:
            for idx, idea in enumerate(insights, start=1):
                st.markdown(
                    f"""
                    <div class="idea-box">
                        <div class="muted">제안 {idx}</div>
                        <div style="margin-top:4px;font-weight:700;color:#0f172a;">{idea["title"]}</div>
                        <div style="margin-top:10px;font-size:14px;color:#334155;line-height:1.8;"><b>제안:</b> {idea["idea"]}</div>
                        <div style="margin-top:10px;font-size:14px;color:#475569;line-height:1.9;"><b>근거:</b> {idea["reason"]}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
