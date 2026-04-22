import streamlit as st

st.set_page_config(
    page_title="롯데 석주 주간 골프 MD 뉴스 알림",
    page_icon="⛳",
    layout="wide",
)

PERIOD = "4/1 ~ 4/22 오전"

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
            "insight": "시즌 출정·선수단 이슈는 단순 판촉보다 '이유 있는 행사'로 활용 가능.",
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
            "date": "04.15",
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

PRIORITY_STYLE = {
    "HIGH": ("🔴 HIGH", "#fee2e2", "#dc2626"),
    "MID":  ("🟡 MID",  "#fef9c3", "#ca8a04"),
    "LOW":  ("⚪ LOW",  "#f1f5f9", "#64748b"),
}

PRIORITY_COLOR = {
    "HIGH": "#dc2626",
    "MID":  "#d97706",
    "LOW":  "#94a3b8",
}

CATEGORY_ICON = {
    "골프 브랜드": "🏌️",
    "골프 경기": "🏆",
    "골프장 현황": "⛳",
    "기타 이슈": "📰",
}

STORE_PROFILES = [
    {"name": "잠실점",   "annualSales": "350억", "customers": "2만명",    "avgTicket": "80만원", "vipRatio": 45, "avgAge": 56, "trait": "롯데월드몰 이용가능"},
    {"name": "본점",     "annualSales": "250억", "customers": "1만 5천명", "avgTicket": "90만원", "vipRatio": 50, "avgAge": 47, "trait": "외국인 고객 많음"},
    {"name": "부산본점", "annualSales": "250억", "customers": "1만 8천명", "avgTicket": "80만원", "vipRatio": 40, "avgAge": 51, "trait": "바닷가"},
    {"name": "인천점",   "annualSales": "200억", "customers": "1만 2천명", "avgTicket": "80만원", "vipRatio": 35, "avgAge": 43, "trait": "상권단독"},
    {"name": "동탄점",   "annualSales": "150억", "customers": "1만명",    "avgTicket": "80만원", "vipRatio": 40, "avgAge": 39, "trait": "젊은점포"},
    {"name": "노원점",   "annualSales": "130억", "customers": "8천명",    "avgTicket": "60만원", "vipRatio": 32, "avgAge": 54, "trait": "포켓상권"},
    {"name": "영등포점", "annualSales": "100억", "customers": "7천명",    "avgTicket": "40만원", "vipRatio": 30, "avgAge": 60, "trait": "경쟁열위"},
    {"name": "광복점",   "annualSales": "80억",  "customers": "6천명",    "avgTicket": "40만원", "vipRatio": 28, "avgAge": 55, "trait": "점포는큼"},
    {"name": "미아점",   "annualSales": "40억",  "customers": "4천명",    "avgTicket": "30만원", "vipRatio": 21, "avgAge": 65, "trait": "행사효율 좋음"},
    {"name": "건대점",   "annualSales": "40억",  "customers": "4천명",    "avgTicket": "20만원", "vipRatio": 15, "avgAge": 43, "trait": "골프 부진"},
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


# ── session state ──────────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "news"
if "category" not in st.session_state:
    st.session_state.category = "골프 브랜드"
if "selected_cards" not in st.session_state:
    st.session_state.selected_cards = []
if "expanded_id" not in st.session_state:
    st.session_state.expanded_id = None

# ── global styles ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── base ── */
.block-container { max-width: 1280px; padding-top: 0.75rem; padding-bottom: 3rem; }
html, body, [data-testid="stAppViewContainer"] { background: #f0f4f8; }

/* ── HEADER ── */
.header-bar {
    display: flex; align-items: center; justify-content: space-between;
    padding: 18px 26px; margin-bottom: 14px;
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
    border-radius: 20px;
    box-shadow: 0 4px 24px rgba(15,23,42,.22);
}
.header-left  { display: flex; align-items: center; gap: 14px; }
.header-icon  { font-size: 30px; line-height: 1; }
.header-title { font-size: 18px; font-weight: 800; color: white; letter-spacing: -.3px; }
.header-sub   { font-size: 12px; color: #93c5fd; margin-top: 3px; font-weight: 500; }
.header-right { display: flex; align-items: center; gap: 10px; }
.period-badge {
    font-size: 12px; font-weight: 600; color: #bfdbfe;
    background: rgba(255,255,255,.12); border: 1px solid rgba(255,255,255,.2);
    border-radius: 20px; padding: 5px 14px;
}
.adopted-badge {
    font-size: 12px; font-weight: 700; color: #059669;
    background: #ecfdf5; border: 1px solid #6ee7b7;
    border-radius: 20px; padding: 5px 14px;
}
.adopted-badge-none {
    font-size: 12px; color: #94a3b8;
    background: rgba(255,255,255,.08); border: 1px solid rgba(255,255,255,.12);
    border-radius: 20px; padding: 5px 14px;
}

/* ── nav underline bars ── */
.active-bar   { height: 3px; background: #2563eb; border-radius: 2px; margin-top: -6px; margin-bottom: 10px; }
.inactive-bar { height: 3px; margin-top: -6px; margin-bottom: 10px; }

/* ── CARDS ── */
.card-wrap {
    border: 1px solid #e2e8f0; border-radius: 18px;
    background: white; margin-bottom: 16px;
    box-shadow: 0 2px 12px rgba(0,0,0,.06);
    overflow: hidden;
}
.card-top-bar { height: 4px; width: 100%; }
.card-body    { padding: 20px 22px 16px; }
.card-meta    { display: flex; justify-content: space-between; align-items: center; }
.muted        { font-size: 12px; color: #94a3b8; font-weight: 500; }
.card-title   { margin-top: 8px; font-size: 17px; font-weight: 800; color: #0f172a; line-height: 1.4; }

/* ── priority badges ── */
.badge      { display: inline-block; font-size: 11px; font-weight: 700; border-radius: 8px; padding: 3px 9px; }
.badge-HIGH { background: #fee2e2; color: #dc2626; }
.badge-MID  { background: #fef3c7; color: #d97706; }
.badge-LOW  { background: #f1f5f9; color: #64748b; }

/* ── one-liner & summary ── */
.one-line {
    margin-top: 10px; font-size: 13px; font-weight: 700; color: #1d4ed8;
    display: flex; align-items: center; gap: 8px;
}
.one-line-bar { display: inline-block; width: 3px; height: 14px; background: #3b82f6; border-radius: 2px; flex-shrink: 0; }
.summary { margin-top: 8px; font-size: 13.5px; color: #475569; line-height: 1.9; }

/* ── headlines box ── */
.box {
    margin-top: 14px; border: 1px solid #e8edf3;
    background: #f8fafc; border-radius: 12px; padding: 13px 15px;
}
.small-title {
    font-size: 10px; font-weight: 800; color: #94a3b8;
    text-transform: uppercase; letter-spacing: .8px; margin-bottom: 10px;
}
.link-chip {
    display: inline-flex; align-items: center; gap: 4px;
    font-size: 12px; color: #1e40af; background: white;
    border: 1px solid #dbeafe; border-radius: 8px;
    padding: 5px 10px; margin: 0 6px 6px 0; text-decoration: none;
    transition: all .12s;
}
.link-chip:hover { background: #eff6ff; border-color: #93c5fd; }

/* ── insight section ── */
.insight-section {
    margin-top: 14px; padding: 16px 18px;
    background: linear-gradient(135deg, #f8fafc 0%, #eff6ff 100%);
    border: 1px solid #dbeafe; border-radius: 14px;
}
.insight-label {
    font-size: 10px; font-weight: 800; color: #94a3b8;
    text-transform: uppercase; letter-spacing: .8px; margin-bottom: 8px;
}
.insight-text { font-size: 13.5px; color: #334155; line-height: 1.85; }
.action-tag {
    display: inline-block; font-size: 12px; color: #1e40af;
    background: #eff6ff; border: 1px solid #bfdbfe;
    border-radius: 8px; padding: 5px 12px; margin: 3px 4px 3px 0; font-weight: 600;
}

/* ── STORE PAGE ── */
.store-header {
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
    border-radius: 16px; padding: 20px 22px; margin-bottom: 14px; color: white;
}
.store-name  { font-size: 20px; font-weight: 800; }
.store-sub   { font-size: 13px; color: #93c5fd; margin-top: 4px; font-weight: 500; }
.store-trait {
    display: inline-block; font-size: 12px; font-weight: 600; color: #bfdbfe;
    background: rgba(255,255,255,.1); border: 1px solid rgba(255,255,255,.2);
    border-radius: 20px; padding: 4px 12px; margin-top: 10px;
}

.stat-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
.stat-card {
    border: 1px solid #e2e8f0; border-radius: 12px; padding: 12px 14px;
    background: white; box-shadow: 0 1px 3px rgba(0,0,0,.04);
}
.stat-label { font-size: 10px; color: #94a3b8; font-weight: 700; text-transform: uppercase; letter-spacing: .5px; }
.stat-value { margin-top: 5px; font-weight: 800; font-size: 15px; color: #0f172a; }

.progress-section { margin-top: 12px; }
.prog-row   { margin-bottom: 14px; }
.prog-header { display: flex; justify-content: space-between; margin-bottom: 5px; }
.prog-label { font-size: 10px; font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: .5px; }
.prog-val   { font-size: 13px; font-weight: 800; color: #0f172a; }
.prog-bg    { background: #f1f5f9; border-radius: 99px; height: 8px; overflow: hidden; }
.prog-fill-blue   { height: 100%; border-radius: 99px; background: linear-gradient(90deg, #2563eb, #60a5fa); }
.prog-fill-purple { height: 100%; border-radius: 99px; background: linear-gradient(90deg, #7c3aed, #a78bfa); }

/* ── IDEA BOXES ── */
.idea-box {
    border-radius: 16px; background: white; border: 1px solid #e2e8f0;
    margin-top: 14px; box-shadow: 0 2px 10px rgba(0,0,0,.05); overflow: hidden;
}
.idea-box-head {
    display: flex; align-items: center; gap: 14px;
    padding: 14px 18px; background: #f8fafc; border-bottom: 1px solid #f1f5f9;
}
.idea-num-circle {
    width: 32px; height: 32px; border-radius: 50%; flex-shrink: 0;
    background: linear-gradient(135deg, #1d4ed8, #3b82f6);
    color: white; font-size: 14px; font-weight: 800;
    display: flex; align-items: center; justify-content: center;
}
.idea-title    { font-weight: 800; font-size: 14px; color: #0f172a; }
.idea-box-body { padding: 16px 18px; }
.idea-body     { font-size: 13.5px; color: #334155; line-height: 1.85; }
.idea-sep      { height: 1px; background: #f1f5f9; margin: 12px 0; }
.idea-reason-label {
    font-size: 10px; font-weight: 800; color: #94a3b8;
    text-transform: uppercase; letter-spacing: .5px; margin-bottom: 5px;
}
.idea-reason { font-size: 13px; color: #64748b; line-height: 1.8; }
</style>
""", unsafe_allow_html=True)

# ── header bar ─────────────────────────────────────────────────────────────────
adopted_count = len(st.session_state.selected_cards)
adopted_html = (
    f'<span class="adopted-badge">✔ 채택 {adopted_count}건</span>'
    if adopted_count > 0
    else '<span class="adopted-badge-none">채택 없음</span>'
)
st.markdown(
    f"""
    <div class="header-bar">
        <div class="header-left">
            <span class="header-icon">⛳</span>
            <div>
                <div class="header-title">롯데 석주 주간 골프 MD 뉴스</div>
                <div class="header-sub">골프 MD 주간 트렌드 및 점포 실행안 리포트</div>
            </div>
        </div>
        <div class="header-right">
            <span class="period-badge">📅 {PERIOD}</span>
            {adopted_html}
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── top navigation ─────────────────────────────────────────────────────────────
nav1, nav2, _ = st.columns([1.1, 1.4, 9])
with nav1:
    if st.button("📰 뉴스 분석", use_container_width=True, key="nav_news"):
        st.session_state.page = "news"
    st.markdown(
        '<div class="active-bar"></div>' if st.session_state.page == "news" else '<div class="inactive-bar"></div>',
        unsafe_allow_html=True,
    )
with nav2:
    if st.button("🏪 점포 인사이트", use_container_width=True, key="nav_insight"):
        st.session_state.page = "insight"
    st.markdown(
        '<div class="active-bar"></div>' if st.session_state.page == "insight" else '<div class="inactive-bar"></div>',
        unsafe_allow_html=True,
    )

# ══════════════════════════════════════════════════════════════════════════════
# NEWS PAGE
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.page == "news":

    # category tabs with icons + count
    cat_cols = st.columns(4)
    for i, cat in enumerate(DATA.keys()):
        with cat_cols[i]:
            icon = CATEGORY_ICON.get(cat, "")
            count = len(DATA[cat])
            if st.button(f"{icon} {cat} ({count})", use_container_width=True, key=f"cat_{cat}"):
                st.session_state.category = cat
            st.markdown(
                '<div class="active-bar"></div>' if st.session_state.category == cat else '<div class="inactive-bar"></div>',
                unsafe_allow_html=True,
            )

    cards = sorted(DATA[st.session_state.category], key=lambda x: PRIORITY_ORDER.get(x["priority"], 99))

    for card in cards:
        p_label, p_bg, p_color = PRIORITY_STYLE.get(card["priority"], ("", "#f1f5f9", "#64748b"))
        border_color = PRIORITY_COLOR.get(card["priority"], "#94a3b8")

        chips_html = "".join(
            f'<a class="link-chip" href="{h["url"]}" target="_blank" rel="noreferrer">↗ {h["title"]}</a>'
            for h in card["headlines"]
        )

        st.markdown(
            f"""
            <div class="card-wrap">
                <div class="card-top-bar" style="background:{border_color};"></div>
                <div class="card-body">
                    <div class="card-meta">
                        <span class="muted">{card["date"]} · {card["source"]}</span>
                        <span class="badge badge-{card["priority"]}">{p_label}</span>
                    </div>
                    <div class="card-title">{card["title"]}</div>
                    <div class="one-line"><span class="one-line-bar"></span>{card["oneLine"]}</div>
                    <div class="summary">{card["summary"]}</div>
                    <div class="box">
                        <div class="small-title">관련 기사</div>
                        {chips_html}
                    </div>
                </div>
            """,
            unsafe_allow_html=True,
        )

        # expand button
        exp_col, _ = st.columns([1.4, 7])
        with exp_col:
            label = "인사이트 ▲" if st.session_state.expanded_id == card["id"] else "인사이트 ▼"
            if st.button(label, key=f"expand_{card['id']}"):
                st.session_state.expanded_id = (
                    None if st.session_state.expanded_id == card["id"] else card["id"]
                )

        # expanded section
        if st.session_state.expanded_id == card["id"]:
            action_tags = "".join(f'<span class="action-tag">{a}</span>' for a in card["actions"])
            st.markdown(
                f"""
                <div class="insight-section">
                    <div style="display:flex;gap:24px;flex-wrap:wrap;">
                        <div style="flex:1;min-width:220px;">
                            <div class="insight-label">인사이트</div>
                            <div class="insight-text">{card["insight"]}</div>
                        </div>
                        <div style="flex:1;min-width:180px;">
                            <div class="insight-label">실행 액션</div>
                            <div style="margin-top:6px;">{action_tags}</div>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            adopt_col1, adopt_col2 = st.columns([6, 1.4])
            with adopt_col2:
                already = any(item["id"] == card["id"] for item in st.session_state.selected_cards)
                if st.button(
                    "✔ 채택됨" if already else "실행안 채택",
                    key=f"select_{card['id']}",
                    disabled=already,
                    use_container_width=True,
                ):
                    st.session_state.selected_cards.append(card)
                    st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# STORE INSIGHT PAGE
# ══════════════════════════════════════════════════════════════════════════════
else:
    selected_name = st.selectbox(
        "점포 선택",
        [item["name"] for item in STORE_PROFILES],
        index=0,
    )
    store = next(item for item in STORE_PROFILES if item["name"] == selected_name)
    insights = build_store_insights(store, st.session_state.selected_cards)

    # store header (dark)
    st.markdown(
        f"""
        <div class="store-header">
            <div class="store-name">{store["name"]}</div>
            <div class="store-sub">연간 골프 매출 {store["annualSales"]} · 구매고객 {store["customers"]} · 객단가 {store["avgTicket"]}</div>
            <span class="store-trait">📍 {store["trait"]}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    left, right = st.columns([1.1, 2.2])

    with left:
        age_pct = min(store["avgAge"], 70) / 70 * 100
        st.markdown(
            f"""
            <div style="font-size:13px;font-weight:700;color:#64748b;text-transform:uppercase;
                        letter-spacing:.5px;margin-bottom:10px;">점포 지표</div>
            <div class="stat-grid">
                <div class="stat-card">
                    <div class="stat-label">연간 골프 매출</div>
                    <div class="stat-value">{store["annualSales"]}</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">구매고객수</div>
                    <div class="stat-value">{store["customers"]}</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">객단가</div>
                    <div class="stat-value">{store["avgTicket"]}</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">평균 연령대</div>
                    <div class="stat-value">{store["avgAge"]}세</div>
                </div>
            </div>
            <div class="progress-section">
                <div class="prog-row">
                    <div class="prog-header">
                        <span class="prog-label">우수고객 구성비</span>
                        <span class="prog-val">{store["vipRatio"]}%</span>
                    </div>
                    <div class="prog-bg">
                        <div class="prog-fill-blue" style="width:{store["vipRatio"]}%;"></div>
                    </div>
                </div>
                <div class="prog-row">
                    <div class="prog-header">
                        <span class="prog-label">평균 연령</span>
                        <span class="prog-val">{store["avgAge"]}세</span>
                    </div>
                    <div class="prog-bg">
                        <div class="prog-fill-purple" style="width:{age_pct:.0f}%;"></div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        adopted_info = (
            f'<span style="font-size:13px;color:#64748b;font-weight:400;"> — 채택 뉴스 {adopted_count}건 기반</span>'
            if adopted_count > 0
            else '<span style="font-size:13px;color:#94a3b8;font-weight:400;"> — 전체 뉴스 기반</span>'
        )
        st.markdown(
            f'<div style="font-size:15px;font-weight:800;color:#0f172a;margin-bottom:8px;">'
            f'점포 맞춤 제안{adopted_info}</div>',
            unsafe_allow_html=True,
        )

        if not insights:
            st.markdown(
                '<div style="color:#94a3b8;font-size:14px;margin-top:16px;">현재 점포 특성과 연결되는 추천 실행안이 없습니다.</div>',
                unsafe_allow_html=True,
            )
        else:
            for idx, idea in enumerate(insights, start=1):
                st.markdown(
                    f"""
                    <div class="idea-box">
                        <div class="idea-box-head">
                            <div class="idea-num-circle">{idx}</div>
                            <div class="idea-title">{idea["title"]}</div>
                        </div>
                        <div class="idea-box-body">
                            <div class="idea-body">{idea["idea"]}</div>
                            <div class="idea-sep"></div>
                            <div class="idea-reason-label">근거</div>
                            <div class="idea-reason">{idea["reason"]}</div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
