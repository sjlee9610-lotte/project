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
            "date": "04.07",
            "source": "레저신문",
            "title": "5년 국내 골프용품 브랜드 점유율 조사 결과 발표",
            "priority": "HIGH",
            "oneLine": "테일러메이드·젝시오·핑 3강, 골프웨어는 말본 1위",
            "summary": "2022~2026년 5년간 국내 골퍼 사용 브랜드 조사에서 테일러메이드(17%)가 드라이버 점유율 2년 연속 1위를 유지했으며, 골프웨어 부문은 말본(16%)이 1위를 기록했다.",
            "headlines": [
                {"title": "테일러메이드 드라이버 점유율 2년 연속 1위", "url": "https://search.naver.com/search.naver?where=news&query=테일러메이드+골프+점유율+2026"},
                {"title": "젝시오 2위, 핑·캘러웨이 공동 3위 경쟁", "url": "https://search.naver.com/search.naver?where=news&query=젝시오+핑+골프+브랜드+점유율"},
                {"title": "골프웨어 말본 1위, 브랜드별 판도 변화", "url": "https://search.naver.com/search.naver?where=news&query=말본+골프웨어+2026"},
            ],
            "insight": "1위 장비 브랜드 연계 시타존·기획 상품 구성 시 구매 전환 효과가 직접적으로 기대됨.",
            "actions": ["테일러메이드 시타존 운영", "말본 골프웨어 팝업"],
        },
        {
            "id": "brand-2",
            "date": "04.10",
            "source": "한국섬유신문",
            "title": "백화점 골프웨어 매출 하락, 프리미엄 소비 피로 누적",
            "priority": "MID",
            "oneLine": "코로나 특수 소멸 후 고가 골프웨어 수요 둔화",
            "summary": "2025년 주요 백화점 골프웨어 매출이 프리미엄 라인 중심으로 하락세를 보이며, 2026년도 뚜렷한 반등보다 조정 국면 연장이 유력하다는 분석이 나왔다.",
            "headlines": [
                {"title": "주요 백화점 골프웨어 매출 하락 지속", "url": "https://search.naver.com/search.naver?where=news&query=백화점+골프웨어+매출+2026"},
                {"title": "프리미엄 골프웨어 소비 피로도 누적", "url": "https://search.naver.com/search.naver?where=news&query=프리미엄+골프웨어+시장+조정"},
                {"title": "가성비 중심 골프웨어 수요 상대적 강세", "url": "https://search.naver.com/search.naver?where=news&query=가성비+골프웨어+트렌드+2026"},
            ],
            "insight": "프리미엄 일괄 정책보다 가격대별 세분화와 차별화된 체험 제안이 필요한 시점.",
            "actions": ["중가 골프웨어 기획전", "가성비 브랜드 전면 배치"],
        },
        {
            "id": "brand-3",
            "date": "04.15",
            "source": "골프코스세미나",
            "title": "2026 골프산업 '초정밀 경영' 시대 진입",
            "priority": "HIGH",
            "oneLine": "AI·데이터 기반 경영이 골프업계 표준으로",
            "summary": "팬데믹 이후 양적 팽창에서 질적 최적화로 전환된 골프산업에서 AI·자동화·환경 가치를 결합한 '초정밀 경영'이 핵심 경쟁력으로 부상했다.",
            "headlines": [
                {"title": "골프장 AI·자동화 경영 업계 표준화 진입", "url": "https://search.naver.com/search.naver?where=news&query=골프장+AI+자동화+경영+2026"},
                {"title": "젊은 골퍼·여성 골퍼 비중 25% 돌파", "url": "https://search.naver.com/search.naver?where=news&query=여성+골퍼+젊은+골퍼+비중+2026"},
                {"title": "데이터 기반 맞춤형 골프 경험 수요 확산", "url": "https://search.naver.com/search.naver?where=news&query=데이터+기반+골프+맞춤+경험"},
            ],
            "insight": "고객 데이터 기반 맞춤 제안이 차별화된 구매 경험의 핵심이 되는 시점.",
            "actions": ["VIP 맞춤 상담 프로그램", "데이터 기반 상품 큐레이션"],
        },
    ],
    "골프 경기": [
        {
            "id": "event-1",
            "date": "04.07",
            "source": "스포츠경향",
            "title": "KLPGA 더 시에나 오픈 2026 성료, 고지원 우승",
            "priority": "HIGH",
            "oneLine": "시즌 개막전 흥행 성공, 참여형 집객 이벤트 연계 기회",
            "summary": "4월 2~5일 개최된 KLPGA 개막전 더 시에나 오픈에서 고지원이 13언더파로 우승하며 시즌 초 화제성을 이끌었다. 경기력과 화제성 모두 잡은 흥행 대회로 평가받았다.",
            "headlines": [
                {"title": "고지원, 더 시에나 오픈 2026 우승(13언더파)", "url": "https://search.naver.com/search.naver?where=news&query=고지원+더+시에나+오픈+2026"},
                {"title": "KLPGA 개막전 경기력·화제성 모두 성공", "url": "https://search.naver.com/search.naver?where=news&query=KLPGA+더시에나오픈+2026"},
                {"title": "봄 시즌 KLPGA 2026 흥행 출발 순조", "url": "https://search.naver.com/search.naver?where=news&query=KLPGA+2026+시즌+개막"},
            ],
            "insight": "시즌 개막전 화제성 → 선수 연계 팝업·KLPGA 응원 기획전으로 집객 연결 가능.",
            "actions": ["선수 응원 팝업", "KLPGA 시즌 개막 기획전"],
        },
        {
            "id": "event-2",
            "date": "04.13",
            "source": "골프한국",
            "title": "슈퍼 루키 김민솔, KLPGA iM금융오픈 우승",
            "priority": "HIGH",
            "oneLine": "신예 루키 돌풍으로 2030 팬층 확대 기대",
            "summary": "4월 9~12일 구미 개최 iM금융오픈에서 신예 김민솔이 -11타로 우승했다. 대회에 2만여 명 관중이 몰리며 지역 경제 활성화 효과까지 이끌어 참여형 골프 콘텐츠 확대를 확인했다.",
            "headlines": [
                {"title": "김민솔 iM금융오픈 우승, '슈퍼 루키' 등장", "url": "https://search.naver.com/search.naver?where=news&query=김민솔+iM금융오픈+우승+2026"},
                {"title": "대회 2만여 명 관중 몰려 지역경제 훈풍", "url": "https://search.naver.com/search.naver?where=news&query=iM금융오픈+2026+관중"},
                {"title": "공동 2위 전예성·안지현·김시현 선전", "url": "https://search.naver.com/search.naver?where=news&query=KLPGA+iM금융오픈+2026+결과"},
            ],
            "insight": "루키 선수 화제성은 2030 신규 골프 유입층과 연결 가능한 매장 이벤트 소재.",
            "actions": ["루키 선수 협업 팝업", "신규 골퍼 입문 프로모션"],
        },
        {
            "id": "event-3",
            "date": "04.21",
            "source": "골프한국",
            "title": "김민선7, KLPGA 넥센·세인트나인 마스터즈 우승",
            "priority": "MID",
            "oneLine": "브랜드 협찬 대회 흥행으로 골프웨어 노출 극대화",
            "summary": "KLPGA 4번째 대회인 넥센·세인트나인 마스터즈에서 김민선7이 우승하며 스포츠 브랜드 세인트나인의 노출 효과가 극대화됐다. 2026 KLPGA 시즌 4개 대회 모두 흥행 성공으로 평가됐다.",
            "headlines": [
                {"title": "김민선7 넥센·세인트나인 마스터즈 우승", "url": "https://search.naver.com/search.naver?where=news&query=김민선7+넥센+세인트나인+마스터즈+2026"},
                {"title": "세인트나인 골프웨어 대회 협찬 효과 부각", "url": "https://search.naver.com/search.naver?where=news&query=세인트나인+골프웨어+2026"},
                {"title": "KLPGA 4개 대회 연속 흥행 성공 평가", "url": "https://search.naver.com/search.naver?where=news&query=KLPGA+2026+시즌+흥행"},
            ],
            "insight": "대회 협찬 골프웨어 브랜드 연계 상품 기획이 시즌 초 구매 의향 고객에게 효과적.",
            "actions": ["협찬 브랜드 특별전", "선수 착용 아이템 전면 배치"],
        },
    ],
    "골프장 현황": [
        {
            "id": "course-1",
            "date": "04.08",
            "source": "레저신문",
            "title": "골프장 AI·자동화 경영 본격 궤도 진입",
            "priority": "MID",
            "oneLine": "최저임금·구인난 3중고 돌파구로 AI 자동화 채택 확산",
            "summary": "최저임금 인상과 구인난, 내장객 감소라는 3중고를 해결하기 위해 국내 골프장이 AI·자동화를 업계 표준으로 채택하기 시작했다. 스마트 예약 시스템·무인 캐디 도입이 빠르게 확산되고 있다.",
            "headlines": [
                {"title": "골프장 AI·자동화 도입 업계 표준化 진입", "url": "https://search.naver.com/search.naver?where=news&query=골프장+AI+자동화+경영+2026"},
                {"title": "무인 캐디·스마트 예약 시스템 빠른 확산", "url": "https://search.naver.com/search.naver?where=news&query=골프장+스마트+예약+자동화"},
                {"title": "내장객 감소 속 비용 절감형 경영 주목", "url": "https://search.naver.com/search.naver?where=news&query=골프장+내장객+감소+경영+2026"},
            ],
            "insight": "골프장 서비스 품질이 차별화 포인트로 부상 — 용품·웨어 판매 채널의 프리미엄 서비스 강화 기회.",
            "actions": ["라운딩 전후 장비 상담 서비스", "골프장 연계 패키지 프로모션"],
        },
        {
            "id": "course-2",
            "date": "04.14",
            "source": "골프저널",
            "title": "봄 시즌 퍼블릭 골프장 예약 급증, 가성비 라운딩 수요 본격화",
            "priority": "HIGH",
            "oneLine": "라운딩 수요 본격화, 실구매 전환 타이밍 도래",
            "summary": "4월 봄 시즌을 맞아 퍼블릭 골프장 예약이 급증하고 있으며, 그린피 20만원 이상의 부담 속에서 가성비 중심 소비 패턴이 뚜렷해지고 있다. 할인 티타임 플랫폼 활용도 급증하고 있다.",
            "headlines": [
                {"title": "퍼블릭 골프장 봄 시즌 예약률 급상승", "url": "https://search.naver.com/search.naver?where=news&query=퍼블릭+골프장+예약+봄+2026"},
                {"title": "평균 그린피 20만원대, 가성비 선택 증가", "url": "https://search.naver.com/search.naver?where=news&query=그린피+2026+퍼블릭"},
                {"title": "할인 티타임 예약 플랫폼 이용 급증", "url": "https://search.naver.com/search.naver?where=news&query=골프장+할인+예약+플랫폼+2026"},
            ],
            "insight": "봄 라운딩 수요 증가는 장비·웨어 구매 타이밍과 직결 — 주말 프로모션 및 묶음 행사 운영 적기.",
            "actions": ["봄 라운딩 시즌 기획전", "장비·웨어 묶음 할인 행사"],
        },
    ],
    "기타 이슈": [
        {
            "id": "other-1",
            "date": "04.04",
            "source": "골프코스세미나",
            "title": "여성·젊은 골퍼 비중 25% 돌파, 골프 소비 구조 변화",
            "priority": "HIGH",
            "oneLine": "2030 여성 골퍼 주류화로 새로운 소비층 부상",
            "summary": "2026년 여성과 젊은 골퍼가 전체의 25% 이상을 차지하며 골프 문화의 주류로 자리 잡았다. 이들은 스크린·필드 하이브리드 경험과 골프+웰니스 복합 서비스를 선호하며 기존 소비층과 다른 구매 패턴을 보인다.",
            "headlines": [
                {"title": "여성·젊은 골퍼 전체 비중 25% 돌파", "url": "https://search.naver.com/search.naver?where=news&query=여성+골퍼+젊은+골퍼+비중+2026"},
                {"title": "골프+웰니스 복합 라이프스타일 수요 급증", "url": "https://search.naver.com/search.naver?where=news&query=골프+웰니스+라이프스타일+2026"},
                {"title": "스크린·필드 하이브리드 멤버십 선호 확산", "url": "https://search.naver.com/search.naver?where=news&query=스크린골프+필드골프+하이브리드"},
            ],
            "insight": "2030 여성 골퍼 중심 스타일링·콘텐츠형 제안이 신규 매출 확대의 핵심 레버.",
            "actions": ["여성 골퍼 스타일링 기획전", "골프+웰니스 복합 프로모션"],
        },
        {
            "id": "other-2",
            "date": "04.18",
            "source": "골프저널",
            "title": "1인 골프·마이크로 투어 트렌드 급부상",
            "priority": "MID",
            "oneLine": "근거리 효율형 라운딩과 혼자 즐기는 솔로 골프 확산",
            "summary": "장거리 골프 여행보다 집 근처에서 짧고 효율적인 라운드를 선호하는 '마이크로 투어'와 1인 골프 문화가 2026년 골프 소비의 새로운 트렌드로 자리 잡고 있다. 1인 골퍼를 겨냥한 플랫폼·상품 기획이 주목받는다.",
            "headlines": [
                {"title": "1인 골프·솔로 골퍼 시장 빠르게 성장", "url": "https://search.naver.com/search.naver?where=news&query=1인+골프+솔로+골퍼+2026"},
                {"title": "마이크로 투어, 근거리 효율형 라운딩 선호", "url": "https://search.naver.com/search.naver?where=news&query=마이크로+골프+투어+근거리+2026"},
                {"title": "골프 소비 패턴 '효율형'으로 전환 가속", "url": "https://search.naver.com/search.naver?where=news&query=골프+소비+트렌드+효율+2026"},
            ],
            "insight": "1인 골퍼 겨냥 단품 제안 강화와 '혼자 써도 좋은 장비' 큐레이션 기획이 유효.",
            "actions": ["1인 골퍼 맞춤 장비 기획전", "효율형 용품 패키지 구성"],
        },
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

    if ("참여형" in item["oneLine"] or "루키" in item["title"] or "1인 골프" in item["title"] or "스크린골프" in item["title"]):
        if store["avgAge"] <= 45 or "젊은" in store["trait"] or store["name"] == "건대점":
            suggestions.append({
                "title": f'{store["name"]} 참여형·신규 유입 이벤트',
                "idea": f'{store["name"]}에서 루키 선수 협업 또는 참여형 이벤트를 열어 골프 관심 신규 고객 유입을 확대합니다.',
                "reason": f'{store["name"]}은 평균 연령 {store["avgAge"]}세로 비교적 젊은 고객 비중이 높거나 {store["trait"]} 특성이 있어 체험형·신규 유입 이벤트 반응을 기대할 수 있습니다. 기사에서도 루키 선수 화제성과 참여형 콘텐츠 확대가 확인됩니다.',
            })

    if ("예약" in item["title"] or "라운딩 수요" in item["oneLine"]):
        suggestions.append({
            "title": f'{store["name"]} 라운딩 수요 대응 프로모션',
            "idea": f'{store["name"]}에서 라운딩 직전 수요를 노린 주말 프로모션이나 장비·웨어 묶음 제안을 운영합니다.',
            "reason": f'기사에서 봄 시즌 예약 증가와 수요 확대가 나타났고, {store["name"]}의 현재 연간 골프 매출 {store["annualSales"]} 및 구매고객수 {store["customers"]}를 감안하면 실구매 전환형 행사로 연결할 여지가 있습니다.',
        })

    if ("여성" in item["title"] or "마이크로" in item["title"] or "1인 골프" in item["title"] or "스포츠 카테고리" in item["oneLine"]):
        if "젊은" in store["trait"] or "상권단독" in store["trait"] or store["name"] == "잠실점" or store["avgAge"] <= 47:
            suggestions.append({
                "title": f'{store["name"]} 신규 골퍼층 맞춤 제안',
                "idea": f'{store["name"]}에서 여성·젊은 골퍼와 1인 골퍼를 겨냥한 스타일링 중심 기획전 또는 효율형 용품 패키지 행사를 기획합니다.',
                "reason": f'{store["name"]}의 특성인 "{store["trait"]}"은 신규 골퍼층 유입에 유리합니다. 기사에서 여성·젊은 골퍼 비중이 25%를 돌파하고 1인 골프 트렌드가 급부상하고 있어 타깃 제안 명분이 충분합니다.',
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
.block-container { max-width: 1280px; padding-top: 1rem; padding-bottom: 3rem; }
html, body, [data-testid="stAppViewContainer"] { background: #f0fdf4; }

/* Streamlit 기본 상단 헤더·툴바 완전 제거 */
#MainMenu { visibility: hidden !important; }
header { visibility: hidden !important; height: 0 !important; }
[data-testid="stHeader"] { display: none !important; }
[data-testid="stToolbar"] { display: none !important; }
[data-testid="stDecoration"] { display: none !important; }
.stApp > header { display: none !important; }
footer { visibility: hidden !important; }

/* ── HEADER ── */
.header-bar {
    display: flex; align-items: center; justify-content: space-between;
    padding: 18px 26px; margin-bottom: 14px;
    background: linear-gradient(135deg, #064e3b 0%, #065f46 100%);
    border-radius: 20px;
    box-shadow: 0 4px 24px rgba(6,78,59,.28);
}
.header-left  { display: flex; align-items: center; gap: 14px; }
.header-icon  { font-size: 30px; line-height: 1; }
.header-title { font-size: 18px; font-weight: 800; color: white; letter-spacing: -.3px; }
.header-sub   { font-size: 12px; color: #6ee7b7; margin-top: 3px; font-weight: 500; }
.header-right { display: flex; align-items: center; gap: 10px; }
.period-badge {
    font-size: 12px; font-weight: 600; color: #a7f3d0;
    background: rgba(255,255,255,.12); border: 1px solid rgba(255,255,255,.2);
    border-radius: 20px; padding: 5px 14px;
}
.adopted-badge {
    font-size: 12px; font-weight: 700; color: #064e3b;
    background: #d1fae5; border: 1px solid #6ee7b7;
    border-radius: 20px; padding: 5px 14px;
}
.adopted-badge-none {
    font-size: 12px; color: #a7f3d0;
    background: rgba(255,255,255,.08); border: 1px solid rgba(255,255,255,.12);
    border-radius: 20px; padding: 5px 14px;
}

/* ── nav underline bars ── */
.active-bar   { height: 3px; background: #059669; border-radius: 2px; margin-top: -6px; margin-bottom: 10px; }
.inactive-bar { height: 3px; margin-top: -6px; margin-bottom: 10px; }

/* ── CARDS ── */
.card-wrap {
    border: 1px solid #d1fae5; border-radius: 18px;
    background: white; margin-bottom: 16px;
    box-shadow: 0 2px 12px rgba(6,78,59,.07);
    overflow: hidden;
}
.card-top-bar { height: 4px; width: 100%; }
.card-body    { padding: 20px 22px 16px; }
.card-meta    { display: flex; justify-content: space-between; align-items: center; }
.muted        { font-size: 12px; color: #94a3b8; font-weight: 500; }
.card-title   { margin-top: 8px; font-size: 17px; font-weight: 800; color: #064e3b; line-height: 1.4; }

/* ── priority badges ── */
.badge      { display: inline-block; font-size: 11px; font-weight: 700; border-radius: 8px; padding: 3px 9px; }
.badge-HIGH { background: #fee2e2; color: #dc2626; }
.badge-MID  { background: #fef3c7; color: #d97706; }
.badge-LOW  { background: #f1f5f9; color: #64748b; }

/* ── one-liner & summary ── */
.one-line {
    margin-top: 10px; font-size: 13px; font-weight: 700; color: #065f46;
    display: flex; align-items: center; gap: 8px;
}
.one-line-bar { display: inline-block; width: 3px; height: 14px; background: #10b981; border-radius: 2px; flex-shrink: 0; }
.summary { margin-top: 8px; font-size: 13.5px; color: #374151; line-height: 1.9; }

/* ── headlines box ── */
.box {
    margin-top: 14px; border: 1px solid #d1fae5;
    background: #f0fdf4; border-radius: 12px; padding: 13px 15px;
}
.small-title {
    font-size: 10px; font-weight: 800; color: #6ee7b7;
    text-transform: uppercase; letter-spacing: .8px; margin-bottom: 10px;
}
.link-chip {
    display: inline-flex; align-items: center; gap: 4px;
    font-size: 12px; color: #065f46; background: white;
    border: 1px solid #a7f3d0; border-radius: 8px;
    padding: 5px 10px; margin: 0 6px 6px 0; text-decoration: none;
    transition: all .12s;
}
.link-chip:hover { background: #ecfdf5; border-color: #6ee7b7; }

/* ── insight section ── */
.insight-section {
    margin-top: 14px; padding: 16px 18px;
    background: linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 100%);
    border: 1px solid #a7f3d0; border-radius: 14px;
}
.insight-label {
    font-size: 10px; font-weight: 800; color: #6ee7b7;
    text-transform: uppercase; letter-spacing: .8px; margin-bottom: 8px;
}
.insight-text { font-size: 13.5px; color: #1f2937; line-height: 1.85; }
.action-tag {
    display: inline-block; font-size: 12px; color: #065f46;
    background: #d1fae5; border: 1px solid #6ee7b7;
    border-radius: 8px; padding: 5px 12px; margin: 3px 4px 3px 0; font-weight: 600;
}

/* ── STORE PAGE ── */
.store-header {
    background: linear-gradient(135deg, #064e3b 0%, #065f46 100%);
    border-radius: 16px; padding: 20px 22px; margin-bottom: 14px; color: white;
}
.store-name  { font-size: 20px; font-weight: 800; }
.store-sub   { font-size: 13px; color: #6ee7b7; margin-top: 4px; font-weight: 500; }
.store-trait {
    display: inline-block; font-size: 12px; font-weight: 600; color: #a7f3d0;
    background: rgba(255,255,255,.1); border: 1px solid rgba(255,255,255,.2);
    border-radius: 20px; padding: 4px 12px; margin-top: 10px;
}

.stat-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
.stat-card {
    border: 1px solid #d1fae5; border-radius: 12px; padding: 12px 14px;
    background: white; box-shadow: 0 1px 3px rgba(6,78,59,.06);
}
.stat-label { font-size: 10px; color: #059669; font-weight: 700; text-transform: uppercase; letter-spacing: .5px; }
.stat-value { margin-top: 5px; font-weight: 800; font-size: 15px; color: #064e3b; }

.progress-section { margin-top: 12px; }
.prog-row   { margin-bottom: 14px; }
.prog-header { display: flex; justify-content: space-between; margin-bottom: 5px; }
.prog-label { font-size: 10px; font-weight: 700; color: #059669; text-transform: uppercase; letter-spacing: .5px; }
.prog-val   { font-size: 13px; font-weight: 800; color: #064e3b; }
.prog-bg    { background: #d1fae5; border-radius: 99px; height: 8px; overflow: hidden; }
.prog-fill-blue   { height: 100%; border-radius: 99px; background: linear-gradient(90deg, #059669, #34d399); }
.prog-fill-purple { height: 100%; border-radius: 99px; background: linear-gradient(90deg, #d97706, #fbbf24); }

/* ── IDEA BOXES ── */
.idea-box {
    border-radius: 16px; background: white; border: 1px solid #d1fae5;
    margin-top: 14px; box-shadow: 0 2px 10px rgba(6,78,59,.07); overflow: hidden;
}
.idea-box-head {
    display: flex; align-items: center; gap: 14px;
    padding: 14px 18px; background: #f0fdf4; border-bottom: 1px solid #d1fae5;
}
.idea-num-circle {
    width: 32px; height: 32px; border-radius: 50%; flex-shrink: 0;
    background: linear-gradient(135deg, #065f46, #10b981);
    color: white; font-size: 14px; font-weight: 800;
    display: flex; align-items: center; justify-content: center;
}
.idea-title    { font-weight: 800; font-size: 14px; color: #064e3b; }
.idea-box-body { padding: 16px 18px; }
.idea-body     { font-size: 13.5px; color: #1f2937; line-height: 1.85; }
.idea-sep      { height: 1px; background: #d1fae5; margin: 12px 0; }
.idea-reason-label {
    font-size: 10px; font-weight: 800; color: #6ee7b7;
    text-transform: uppercase; letter-spacing: .5px; margin-bottom: 5px;
}
.idea-reason { font-size: 13px; color: #374151; line-height: 1.8; }
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
