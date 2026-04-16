import streamlit as st

st.set_page_config(
    page_title="롯데백화점 골프 MD 대시보드",
    page_icon="⛳",
    layout="wide",
)

CATEGORIES = [
    {
        "id": "apparel",
        "name": "골프 어패럴 / 용품",
        "description": "브랜드 동향, 시즌 매출 흐름, 신규 라인 및 협업 이슈를 반영한 영역",
        "stats": {"뉴스": 4, "우선 검토": 2, "실행 후보": 3},
        "items": [
            {
                "id": "apparel-1",
                "title": "마스터스 한정 컬렉션 확대",
                "source": "해외",
                "date": "04.11",
                "link": "https://apnews.com/article/72d5de57abba1362811f281313fb4dba",
                "summary": "마스터스 기간에 맞춰 다수 브랜드가 그린 컬러와 대회 감성을 반영한 한정 상품을 출시하며 단기 수요를 유도함.",
                "insight": "단순 상품 판매보다 대회 분위기를 소비하는 경험이 핵심이어서 이벤트성 진열과 시즌 테마존이 매출에 직접 기여할 가능성이 높음.",
                "actions": [
                    "마스터스 테마 기획전 운영",
                    "그린 컬러 중심 진열 존 구성",
                    "주말 한정 팝업 이벤트 진행",
                ],
                "priority": "HIGH",
            },
            {
                "id": "apparel-2",
                "title": "국내 골프웨어 브랜드 봄 시즌 매출 상승",
                "source": "국내",
                "date": "04.08",
                "link": "https://news.nate.com/view/20260410n19580",
                "summary": "봄 시즌 시작과 함께 주요 골프웨어 브랜드 매출이 전년 대비 상승세를 보이며 신상품 수요가 빠르게 형성되는 흐름.",
                "insight": "시즌 초반에는 브랜드별 히트 상품 선점과 빠른 진열 전환이 중요하며, 여성 및 신규 고객 비중 확대 가능성도 함께 나타남.",
                "actions": [
                    "신상품 집중 기획전 운영",
                    "시즌 초 특가 프로모션 진행",
                    "브랜드별 매대 노출 강화",
                ],
                "priority": "HIGH",
            },
            {
                "id": "apparel-3",
                "title": "골프 브랜드 신규 라인 및 협업 출시 확대",
                "source": "국내",
                "date": "04.06",
                "link": "https://www.golfbiz.co.kr/news/articleView.html?idxno=26016",
                "summary": "국내외 브랜드가 신규 라인과 협업 상품을 연속 출시하며 차별화 경쟁이 강화되는 분위기.",
                "insight": "한정성과 협업 스토리가 있는 상품은 단기 집객 효과가 높아 팝업이나 예약 판매와 연결하기에 적합함.",
                "actions": [
                    "콜라보 팝업 기획",
                    "한정 상품 존 구성",
                    "사전 예약 판매 이벤트 운영",
                ],
                "priority": "MID",
            },
        ],
    },
    {
        "id": "tournament",
        "name": "골프 대회",
        "description": "대회 결과와 시즌 이슈를 행사 및 프로모션 기획으로 연결하는 영역",
        "stats": {"대회": 2, "행사 연결": 2, "콘텐츠": 2},
        "items": [
            {
                "id": "tournament-1",
                "title": "마스터스 우승자 2연패",
                "source": "공식 대회",
                "date": "04.12",
                "link": "https://www.masters.com/en_US/news/articles/2026-04-12/2026-04-12_2026-04-12_mcilroy_makes_history_once_again.html",
                "summary": "마스터스에서 우승자가 2연패를 기록하며 대회 관심도와 미디어 노출이 집중됨.",
                "insight": "우승자 스토리와 퍼포먼스를 활용한 콘텐츠가 고객 관심을 끌 수 있으며, 매장 행사 명분으로 활용 가능.",
                "actions": [
                    "우승자 스타일 테마전 구성",
                    "대회 연계 이벤트 진행",
                    "매장 내 경기 하이라이트 활용",
                ],
                "priority": "HIGH",
            },
            {
                "id": "tournament-2",
                "title": "국내 투어 시즌 시작",
                "source": "KLPGA",
                "date": "04.13",
                "link": "https://klpga.co.kr",
                "summary": "국내 골프 투어가 본격적으로 시작되며 시즌 초반 관심도와 참여 수요가 동시에 증가하는 시기.",
                "insight": "특히 여성 골프 수요와 연계되어 시즌 초 매출 확대 기회로 작용할 가능성이 높음.",
                "actions": [
                    "국내 투어 연계 기획전 진행",
                    "여성 고객 타겟 프로모션",
                    "시즌 오프닝 이벤트 운영",
                ],
                "priority": "MID",
            },
        ],
    },
    {
        "id": "rounding",
        "name": "라운딩 및 플레이",
        "description": "골프 참여 증가, 예약 확대, 입문자 유입 흐름을 반영한 영역",
        "stats": {"뉴스": 3, "프로모션": 3, "적용": 3},
        "items": [
            {
                "id": "rounding-1",
                "title": "국내 골프 인구 증가세 지속",
                "source": "국내",
                "date": "04.10",
                "link": "https://search.naver.com/search.naver?where=news&query=%EA%B3%A8%ED%94%84%20%EC%9D%B8%EA%B5%AC%20%EC%A6%9D%EA%B0%80",
                "summary": "2030 중심으로 골프 인구가 꾸준히 증가하고 있으며 신규 유입이 이어지는 상황.",
                "insight": "라운딩 참여 확대와 입문 수요가 함께 움직이기 때문에 체험형 행사와 첫 구매 유도 프로모션이 효과적일 가능성이 높음.",
                "actions": [
                    "입문자 라운딩 연계 패키지 운영",
                    "체험 이벤트 상시 운영",
                    "첫 구매 프로모션 기획",
                ],
                "priority": "MID",
            },
            {
                "id": "rounding-2",
                "title": "골프장 예약 증가 및 주말 수요 집중",
                "source": "국내",
                "date": "04.09",
                "link": "https://search.naver.com/search.naver?where=news&query=%EA%B3%A8%ED%94%84%EC%9E%A5%20%EC%98%88%EC%95%BD%20%EC%A6%9D%EA%B0%80",
                "summary": "봄 시즌 진입과 함께 라운딩 예약이 증가하고, 특히 주말 수요가 집중되는 흐름이 나타남.",
                "insight": "금요일부터 주말까지 구매 수요가 몰릴 가능성이 높아 단기 집객형 프로모션과 즉시 구매 전환 전략이 유효함.",
                "actions": [
                    "주말 집중 프로모션 운영",
                    "라운딩 연계 할인 행사 기획",
                    "단기 이벤트 존 구성",
                ],
                "priority": "MID",
            },
            {
                "id": "rounding-3",
                "title": "저가 라운딩 프로그램 확대",
                "source": "해외 보도",
                "date": "04.13",
                "link": "https://www.axios.com/local/san-antonio/2026/04/13/san-antonio-5-golf-program-kids-bank-of-america",
                "summary": "저가 라운딩 프로그램 확대를 통해 신규 골퍼 유입이 증가하며 골프 입문 장벽이 낮아지는 흐름.",
                "insight": "입문자 대상 상품 및 체험 기회 제공 시 신규 고객 확보 가능성이 높음.",
                "actions": [
                    "입문자 전용 기획전 운영",
                    "가족 체험 이벤트 구성",
                    "초보자 패키지 상품 제안",
                ],
                "priority": "MID",
            },
        ],
    },
    {
        "id": "membership",
        "name": "회원권 시장",
        "description": "고가 고객 흐름과 프리미엄 제안 기회를 점검하는 영역",
        "stats": {"시세": 1, "VIP": 1, "전략": 1},
        "items": [
            {
                "id": "membership-1",
                "title": "회원권 시장 혼조세",
                "source": "시장 정보",
                "date": "04.08",
                "link": "https://poiup01.tistory.com/269",
                "summary": "회원권 시장은 일부 상승과 일부 하락이 혼재된 상황으로 전반적인 안정세 유지.",
                "insight": "고가 소비층은 유지되나 전반적 확대보다는 선별적 접근이 필요함.",
                "actions": [
                    "소수 우수고객 초청 행사 기획",
                    "프리미엄 상품 중심 상담 운영",
                    "고가 고객 대상 맞춤 제안",
                ],
                "priority": "LOW",
            }
        ],
    },
    {
        "id": "other",
        "name": "기타 이슈",
        "description": "집객과 콘텐츠 기회로 확장 가능한 외부 이슈를 반영한 영역",
        "stats": {"이슈": 1, "기회": 1, "테스트": 1},
        "items": [
            {
                "id": "other-1",
                "title": "마스터스 시청률 최고 수준",
                "source": "언론 보도",
                "date": "04.14",
                "link": "https://nypost.com",
                "summary": "마스터스 대회 시청률이 크게 상승하며 골프에 대한 대중적 관심도가 단기간에 확대됨.",
                "insight": "대회 기간을 활용한 오프라인 집객 이벤트 및 콘텐츠 운영 시 방문 유입 증가 기대.",
                "actions": [
                    "대회 기간 집객 이벤트 운영",
                    "매장 내 영상 콘텐츠 활용",
                    "사회관계망 실시간 연계 프로모션",
                ],
                "priority": "MID",
            }
        ],
    },
]

PRIORITY_LABEL = {"HIGH": "높음", "MID": "중간", "LOW": "낮음"}

if "selected_ideas" not in st.session_state:
    st.session_state.selected_ideas = [
        {
            "id": "selected-1",
            "type": "팝업",
            "title": "마스터스 테마 팝업",
            "store": "잠실점",
            "status": "검토중",
        }
    ]


def determine_type(category_name: str) -> str:
    if category_name == "골프 어패럴 / 용품":
        return "기획전"
    if category_name == "골프 대회":
        return "이벤트"
    if category_name == "회원권 시장":
        return "우수고객"
    return "프로모션"


def add_selected_idea(category_name: str, item: dict) -> None:
    exists = any(idea["title"] == item["title"] for idea in st.session_state.selected_ideas)
    if exists:
        return
    st.session_state.selected_ideas.insert(
        0,
        {
            "id": f'{item["id"]}-selected',
            "type": determine_type(category_name),
            "title": item["title"],
            "store": "점포 미지정",
            "status": "검토중",
        },
    )


def remove_selected_idea(idea_id: str) -> None:
    st.session_state.selected_ideas = [
        idea for idea in st.session_state.selected_ideas if idea["id"] != idea_id
    ]


def get_filtered_categories(search_text: str, priority_filter: str, category_filter: str):
    results = []
    for category in CATEGORIES:
        if category_filter != "전체" and category["name"] != category_filter:
            continue

        items = []
        for item in category["items"]:
            haystack = " ".join(
                [item["title"], item["source"], item["summary"], item["insight"], *item["actions"]]
            ).lower()
            matches_search = (not search_text) or (search_text.lower() in haystack)
            matches_priority = priority_filter == "전체" or item["priority"] == priority_filter
            if matches_search and matches_priority:
                items.append(item)

        if items:
            new_category = dict(category)
            new_category["items"] = items
            results.append(new_category)
    return results


st.markdown(
    '''
    <style>
    .block-container {padding-top: 2rem; padding-bottom: 2rem;}
    .hero-card {
        background: white; border: 1px solid #e2e8f0; border-radius: 24px; padding: 28px;
    }
    .metric-card {
        background: white; border: 1px solid #e2e8f0; border-radius: 18px; padding: 18px 20px;
    }
    .section-card {
        background: white; border: 1px solid #e2e8f0; border-radius: 24px; padding: 24px; margin-bottom: 20px;
    }
    .news-card {
        background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 22px; padding: 20px; margin-top: 14px;
    }
    .mini-card {
        background: white; border: 1px solid #e2e8f0; border-radius: 18px; padding: 16px; height: 100%;
    }
    .badge {
        display: inline-block; font-size: 12px; font-weight: 700; border-radius: 999px; padding: 4px 10px;
    }
    .badge-high {background: #fee2e2; color: #b91c1c;}
    .badge-mid {background: #fef3c7; color: #b45309;}
    .badge-low {background: #e2e8f0; color: #475569;}
    .side-card {
        background: white; border: 1px solid #e2e8f0; border-radius: 22px; padding: 20px; margin-bottom: 20px;
    }
    .idea-card {
        background: white; border: 1px solid #e2e8f0; border-radius: 18px; padding: 14px; margin-bottom: 12px;
    }
    </style>
    ''',
    unsafe_allow_html=True,
)

search_col, priority_col, category_col = st.columns([1.4, 1, 1])
with search_col:
    search_text = st.text_input("검색", placeholder="기사 제목, 인사이트, 실행안 검색")
with priority_col:
    priority_filter = st.selectbox("중요도", ["전체", "HIGH", "MID", "LOW"])
with category_col:
    category_filter = st.selectbox("카테고리", ["전체"] + [c["name"] for c in CATEGORIES])

filtered = get_filtered_categories(search_text, priority_filter, category_filter)
total_news = sum(len(c["items"]) for c in CATEGORIES)
visible_news = sum(len(c["items"]) for c in filtered)
high_priority = sum(1 for c in filtered for i in c["items"] if i["priority"] == "HIGH")

st.markdown('<div class="hero-card">', unsafe_allow_html=True)
hero_left, hero_right = st.columns([2.2, 1])
with hero_left:
    st.markdown("### ⛳ 주간 골프 MD 대시보드")
    st.caption("4/1~4/15 실제 기사 기반")
    st.write("기사 요약, 인사이트, 실행안을 한 화면에서 검토하고 실행 리스트로 넘길 수 있는 실무형 화면입니다.")
with hero_right:
    m1, m2 = st.columns(2)
    m3, m4 = st.columns(2)
    with m1:
        st.markdown(f'<div class="metric-card"><div style="font-size:12px;color:#64748b;">전체 뉴스</div><div style="font-size:28px;font-weight:700;">{total_news}</div></div>', unsafe_allow_html=True)
    with m2:
        st.markdown(f'<div class="metric-card"><div style="font-size:12px;color:#64748b;">현재 표시</div><div style="font-size:28px;font-weight:700;">{visible_news}</div></div>', unsafe_allow_html=True)
    with m3:
        st.markdown(f'<div class="metric-card"><div style="font-size:12px;color:#64748b;">실행 리스트</div><div style="font-size:28px;font-weight:700;">{len(st.session_state.selected_ideas)}</div></div>', unsafe_allow_html=True)
    with m4:
        st.markdown(f'<div class="metric-card"><div style="font-size:12px;color:#64748b;">우선 검토</div><div style="font-size:28px;font-weight:700;">{high_priority}</div></div>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

tab_news, tab_manage = st.tabs(["뉴스 브리핑", "실행 관리"])

with tab_news:
    main_col, side_col = st.columns([2.1, 1])

    with main_col:
        if not filtered:
            st.info("조건에 맞는 뉴스가 없습니다. 검색어나 필터를 조정해보세요.")

        for category in filtered:
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown(f"## {category['name']}")
            st.caption(category["description"])

            stat_cols = st.columns(3)
            stat_items = list(category["stats"].items())
            for idx, (label, value) in enumerate(stat_items):
                with stat_cols[idx]:
                    st.markdown(
                        f'<div class="metric-card"><div style="font-size:12px;color:#64748b;">{label}</div><div style="font-size:22px;font-weight:700;">{value}</div></div>',
                        unsafe_allow_html=True,
                    )

            for item in category["items"]:
                already_selected = any(idea["title"] == item["title"] for idea in st.session_state.selected_ideas)

                st.markdown('<div class="news-card">', unsafe_allow_html=True)
                head_left, head_right = st.columns([4, 1])
                with head_left:
                    st.caption(f'{item["date"]} · {item["source"]}')
                    st.markdown(f"### {item['title']}")
                    st.link_button("기사 보기", item["link"])
                with head_right:
                    badge_cls = {"HIGH": "badge badge-high", "MID": "badge badge-mid", "LOW": "badge badge-low"}[item["priority"]]
                    st.markdown(
                        f'<div style="text-align:right;"><span class="{badge_cls}">중요도 {PRIORITY_LABEL[item["priority"]]}</span></div>',
                        unsafe_allow_html=True,
                    )

                c1, c2, c3 = st.columns(3)
                with c1:
                    st.markdown('<div class="mini-card">', unsafe_allow_html=True)
                    st.markdown("**기사 요약**")
                    st.write(item["summary"])
                    st.markdown("</div>", unsafe_allow_html=True)
                with c2:
                    st.markdown('<div class="mini-card">', unsafe_allow_html=True)
                    st.markdown("**인사이트**")
                    st.write(item["insight"])
                    st.markdown("</div>", unsafe_allow_html=True)
                with c3:
                    st.markdown('<div class="mini-card">', unsafe_allow_html=True)
                    st.markdown("**실행안**")
                    for action in item["actions"]:
                        st.markdown(f"- {action}")
                    st.markdown("</div>", unsafe_allow_html=True)

                b1, b2, _ = st.columns([1, 1, 2])
                with b1:
                    if st.button(
                        "실행안 채택" if not already_selected else "이미 채택됨",
                        key=f'select-{item["id"]}',
                        disabled=already_selected,
                        use_container_width=True,
                    ):
                        add_selected_idea(category["name"], item)
                        st.rerun()
                with b2:
                    st.button("보류", key=f'hold-{item["id"]}', use_container_width=True)
                st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

    with side_col:
        st.markdown('<div class="side-card">', unsafe_allow_html=True)
        st.markdown("### 실행 리스트")
        for idea in st.session_state.selected_ideas:
            st.markdown(
                f'''
                <div class="idea-card">
                    <div style="font-size:12px;color:#64748b;">{idea["type"]}</div>
                    <div style="font-weight:700; margin-top:4px;">{idea["title"]}</div>
                    <div style="font-size:12px;color:#64748b; margin-top:6px;">{idea["store"]}</div>
                </div>
                ''',
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="side-card">', unsafe_allow_html=True)
        st.markdown("### 운영 원칙")
        st.markdown(
            '''
- 기사 요약, 인사이트, 실행안을 한 카드 안에서 검토
- 채택 즉시 실행 리스트로 이동해 상태 관리
- 중요도와 카테고리 기준으로 빠르게 우선순위 판단
            '''
        )
        st.markdown("</div>", unsafe_allow_html=True)

with tab_manage:
    st.markdown("## 실행 관리")
    st.caption("채택한 안건의 상태를 관리하고 우선순위를 정리합니다.")

    if not st.session_state.selected_ideas:
        st.info("채택된 실행안이 없습니다.")
    else:
        for idea in list(st.session_state.selected_ideas):
            with st.container(border=True):
                left, right = st.columns([2, 2])
                with left:
                    st.markdown(f"**{idea['title']}**")
                    st.caption(f'{idea["type"]} · {idea["store"]}')
                with right:
                    new_status = st.selectbox(
                        "상태",
                        ["검토중", "진행중", "완료", "보류"],
                        index=["검토중", "진행중", "완료", "보류"].index(idea["status"]),
                        key=f'status-{idea["id"]}',
                    )
                    idea["status"] = new_status
                if st.button("삭제", key=f'delete-{idea["id"]}'):
                    remove_selected_idea(idea["id"])
                    st.rerun()

    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("검토중", sum(1 for i in st.session_state.selected_ideas if i["status"] == "검토중"))
    with m2:
        st.metric("진행중/완료", sum(1 for i in st.session_state.selected_ideas if i["status"] in ["진행중", "완료"]))
    with m3:
        st.metric("보류", sum(1 for i in st.session_state.selected_ideas if i["status"] == "보류"))
