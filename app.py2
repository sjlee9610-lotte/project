import streamlit as st
import anthropic
from datetime import datetime

# ── 페이지 설정 ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="롯데백화점 골프 MD팀 AI 인사이트",
    page_icon="⛳",
    layout="wide",
)

# ── CSS ──────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1a3a5c 0%, #2d6a4f 100%);
        padding: 2rem;
        border-radius: 12px;
        color: white;
        margin-bottom: 2rem;
    }
    .card {
        background: #f8f9fa;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 1.2rem;
        margin-bottom: 1rem;
    }
    .tag-popup    { background:#d4edda; color:#155724; padding:2px 8px; border-radius:12px; font-size:0.75rem; font-weight:600; }
    .tag-vip      { background:#cce5ff; color:#004085; padding:2px 8px; border-radius:12px; font-size:0.75rem; font-weight:600; }
    .tag-promo    { background:#fff3cd; color:#856404; padding:2px 8px; border-radius:12px; font-size:0.75rem; font-weight:600; }
    .kpi-box      { background:#ffffff; border:2px solid #2d6a4f; border-radius:10px; padding:1rem; text-align:center; }
    .kpi-number   { font-size:2rem; font-weight:700; color:#2d6a4f; }
    .kpi-label    { font-size:0.85rem; color:#555; }
    .step-badge   { background:#1a3a5c; color:white; border-radius:50%; width:28px; height:28px;
                    display:inline-flex; align-items:center; justify-content:center; font-weight:700; margin-right:8px; }
</style>
""", unsafe_allow_html=True)

# ── 헤더 ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
    <h1 style="margin:0">⛳ 롯데백화점 골프 MD팀 AI 인사이트 시스템</h1>
    <p style="margin:0.5rem 0 0; opacity:0.85">정보 → 실행으로 연결하는 AI 기반 MD 운영 플랫폼</p>
</div>
""", unsafe_allow_html=True)

# ── 사이드바 ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### ⚙️ 분석 설정")
    category = st.selectbox(
        "정보 카테고리",
        ["브랜드 런칭 및 신제품", "골프 대회 및 우승자", "시장 및 소비자 트렌드", "장비 및 기술 변화", "기타"],
    )
    action_type = st.multiselect(
        "실행 유형 필터",
        ["팝업", "초청 행사 (VIP)", "프로모션"],
        default=["팝업", "초청 행사 (VIP)", "프로모션"],
    )
    st.divider()
    st.markdown("### 📊 이번 주 KPI")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="kpi-box"><div class="kpi-number">12</div><div class="kpi-label">실행 아이디어</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="kpi-box"><div class="kpi-number">3</div><div class="kpi-label">행사 기획</div></div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    with col3:
        st.markdown('<div class="kpi-box"><div class="kpi-number">2h</div><div class="kpi-label">정보수집 절감</div></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="kpi-box"><div class="kpi-number">28%</div><div class="kpi-label">실행 전환율</div></div>', unsafe_allow_html=True)
    st.divider()
    st.caption(f"마지막 업데이트: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

# ── 탭 구성 ──────────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["🔍 뉴스 분석 & 인사이트", "💡 MD 실행 아이디어", "📋 주간 리포트"])

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — 뉴스 분석 & 인사이트
# ══════════════════════════════════════════════════════════════════════════════
with tab1:
    st.markdown("#### 골프 산업 뉴스를 입력하면 AI가 자동으로 분석합니다")

    news_input = st.text_area(
        "뉴스 내용 입력",
        placeholder="예) 테일러메이드가 2025년 신형 드라이버 Qi35를 출시하며 AI 기반 피팅 서비스를 함께 론칭했습니다...",
        height=150,
    )

    col_btn1, col_btn2 = st.columns([1, 5])
    with col_btn1:
        analyze_btn = st.button("🤖 AI 분석 시작", type="primary", use_container_width=True)

    if analyze_btn and news_input.strip():
        with st.spinner("AI가 뉴스를 분석 중입니다..."):
            try:
                client = anthropic.Anthropic()

                system_prompt = """당신은 롯데백화점 골프 MD팀의 전문 AI 어시스턴트입니다.
골프 산업 뉴스를 분석하여 다음 3가지를 제공합니다:

1. **주요 이슈 요약** (2~3문장, 핵심 내용만)
2. **시장 변화 및 의미 분석** (백화점 비즈니스 관점에서)
3. **백화점 활용 가능성** (고객, 매출, 브랜드 관점)

반드시 한국어로 답변하고, 각 섹션을 명확히 구분해주세요."""

                user_prompt = f"""다음 골프 산업 뉴스를 분석해주세요:

카테고리: {category}
뉴스 내용: {news_input}"""

                response = client.messages.create(
                    model="claude-sonnet-4-20250514",
                    max_tokens=1000,
                    system=system_prompt,
                    messages=[{"role": "user", "content": user_prompt}],
                )

                analysis = response.content[0].text

                st.success("✅ 분석 완료")
                st.markdown("---")

                st.markdown("### 📝 AI 분석 결과")
                st.markdown(
                    f'<div class="card">{analysis.replace(chr(10), "<br>")}</div>',
                    unsafe_allow_html=True,
                )

                # 세션에 저장 (탭2에서 활용)
                if "analyses" not in st.session_state:
                    st.session_state.analyses = []
                st.session_state.analyses.append({
                    "category": category,
                    "news": news_input,
                    "analysis": analysis,
                    "time": datetime.now().strftime("%H:%M"),
                })

            except Exception as e:
                st.error(f"분석 중 오류가 발생했습니다: {e}")

    elif analyze_btn:
        st.warning("뉴스 내용을 입력해주세요.")

    # 분석 히스토리
    if "analyses" in st.session_state and st.session_state.analyses:
        st.markdown("---")
        st.markdown("#### 🗂️ 오늘의 분석 히스토리")
        for i, item in enumerate(reversed(st.session_state.analyses[-5:]), 1):
            with st.expander(f"[{item['time']}] {item['category']} — {item['news'][:40]}..."):
                st.markdown(item["analysis"])


# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 — MD 실행 아이디어
# ══════════════════════════════════════════════════════════════════════════════
with tab2:
    st.markdown("#### 뉴스 기반 MD 실행 아이디어를 자동으로 생성합니다")

    col_a, col_b = st.columns(2)
    with col_a:
        idea_news = st.text_area(
            "뉴스/인사이트 입력",
            placeholder="분석된 뉴스나 시장 인사이트를 입력하세요...",
            height=120,
        )
    with col_b:
        store_context = st.text_area(
            "점포 컨텍스트 (선택)",
            placeholder="예) 잠실점, VIP 고객 비중 높음, 골프 전문관 보유...",
            height=120,
        )

    selected_types = st.multiselect(
        "원하는 실행 유형",
        ["팝업", "초청 행사 (VIP)", "프로모션"],
        default=["팝업", "프로모션"],
    )

    if st.button("💡 실행 아이디어 생성", type="primary"):
        if idea_news.strip():
            with st.spinner("MD 실행 아이디어를 생성 중입니다..."):
                try:
                    client = anthropic.Anthropic()

                    types_str = ", ".join(selected_types) if selected_types else "팝업, 초청 행사, 프로모션"

                    system_prompt = """당신은 롯데백화점 골프 MD팀의 실행 전문 AI입니다.
주어진 뉴스/인사이트를 바탕으로 구체적인 MD 실행 아이디어를 제안합니다.

각 아이디어는 다음 형식으로 작성하세요:
**[실행 유형] 아이디어 제목**
- 내용: 구체적인 행사/프로모션 내용
- 대상 고객: 타겟 고객층
- 예상 효과: 매출 또는 고객 경험 관점
- 실행 난이도: 쉬움 / 보통 / 어려움

2~3개의 아이디어를 제안하세요. 반드시 한국어로 답변하세요."""

                    user_prompt = f"""다음 정보를 바탕으로 MD 실행 아이디어를 생성해주세요:

뉴스/인사이트: {idea_news}
점포 컨텍스트: {store_context if store_context.strip() else '일반 점포'}
원하는 실행 유형: {types_str}"""

                    response = client.messages.create(
                        model="claude-sonnet-4-20250514",
                        max_tokens=1000,
                        system=system_prompt,
                        messages=[{"role": "user", "content": user_prompt}],
                    )

                    ideas = response.content[0].text
                    st.success("✅ 아이디어 생성 완료")
                    st.markdown("---")

                    # 실행 유형 태그 표시
                    tag_html = ""
                    for t in selected_types:
                        if t == "팝업":
                            tag_html += '<span class="tag-popup">팝업</span> '
                        elif "VIP" in t:
                            tag_html += '<span class="tag-vip">VIP 초청</span> '
                        else:
                            tag_html += '<span class="tag-promo">프로모션</span> '

                    st.markdown(f"**적용 실행 유형:** {tag_html}", unsafe_allow_html=True)
                    st.markdown("### 💡 생성된 실행 아이디어")
                    st.markdown(
                        f'<div class="card">{ideas.replace(chr(10), "<br>")}</div>',
                        unsafe_allow_html=True,
                    )

                    # 세션 저장
                    if "ideas" not in st.session_state:
                        st.session_state.ideas = []
                    st.session_state.ideas.append({
                        "news": idea_news,
                        "ideas": ideas,
                        "types": selected_types,
                        "time": datetime.now().strftime("%H:%M"),
                    })

                except Exception as e:
                    st.error(f"아이디어 생성 중 오류가 발생했습니다: {e}")
        else:
            st.warning("뉴스/인사이트 내용을 입력해주세요.")

    # 저장된 아이디어
    if "ideas" in st.session_state and st.session_state.ideas:
        st.markdown("---")
        st.markdown("#### 📌 저장된 아이디어")
        for item in reversed(st.session_state.ideas[-3:]):
            types_label = " / ".join(item["types"])
            with st.expander(f"[{item['time']}] {types_label} — {item['news'][:35]}..."):
                st.markdown(item["ideas"])


# ══════════════════════════════════════════════════════════════════════════════
# TAB 3 — 주간 리포트
# ══════════════════════════════════════════════════════════════════════════════
with tab3:
    st.markdown("#### 주간 골프 MD 리포트를 자동 생성합니다")

    col_r1, col_r2 = st.columns(2)
    with col_r1:
        week_news = st.text_area(
            "이번 주 주요 뉴스 (줄바꿈으로 구분)",
            placeholder="1. 테일러메이드 신제품 출시\n2. KLPGA 투어 개막\n3. 친환경 골프웨어 트렌드 부상...",
            height=180,
        )
    with col_r2:
        sales_data = st.text_area(
            "내부 데이터 (선택)",
            placeholder="예) 지난주 골프 카테고리 매출 전주 대비 +8%, 아이언 품목 판매 증가...",
            height=180,
        )

    report_week = st.text_input("리포트 기준 주차", value=f"{datetime.now().strftime('%Y년 %m월')} {(datetime.now().day - 1) // 7 + 1}주차")

    if st.button("📋 주간 리포트 생성", type="primary"):
        if week_news.strip():
            with st.spinner("주간 리포트를 작성 중입니다..."):
                try:
                    client = anthropic.Anthropic()

                    system_prompt = """당신은 롯데백화점 골프 MD팀의 주간 리포트 작성 전문 AI입니다.
다음 구조로 주간 리포트를 작성하세요:

## 📊 [기간] 골프 MD 주간 리포트

### 1. 이번 주 핵심 이슈 요약
(3~5개 불릿)

### 2. 시장 트렌드 분석
(브랜드, 소비자, 기술 관점)

### 3. 내부 데이터 인사이트
(제공된 경우 활용, 없으면 일반적 관점 제시)

### 4. 이번 주 추천 실행 액션
| 우선순위 | 실행 유형 | 내용 | 기대 효과 |
(표 형식)

### 5. 다음 주 모니터링 포인트
(2~3가지)

반드시 한국어로 작성하세요."""

                    user_prompt = f"""다음 정보로 주간 리포트를 작성해주세요:

기준 주차: {report_week}
이번 주 뉴스: {week_news}
내부 데이터: {sales_data if sales_data.strip() else '없음'}"""

                    response = client.messages.create(
                        model="claude-sonnet-4-20250514",
                        max_tokens=1000,
                        system=system_prompt,
                        messages=[{"role": "user", "content": user_prompt}],
                    )

                    report = response.content[0].text
                    st.success("✅ 리포트 생성 완료")
                    st.markdown("---")
                    st.markdown(report)

                    # 다운로드 버튼
                    st.download_button(
                        label="⬇️ 리포트 다운로드 (.txt)",
                        data=report,
                        file_name=f"골프MD_주간리포트_{report_week.replace(' ', '_')}.txt",
                        mime="text/plain",
                    )

                except Exception as e:
                    st.error(f"리포트 생성 중 오류가 발생했습니다: {e}")
        else:
            st.warning("이번 주 뉴스를 입력해주세요.")

# ── 푸터 ─────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#888; font-size:0.8rem;'>"
    "롯데백화점 골프 MD팀 AI 인사이트 시스템 | Problem → Data → Insight → Action → Execution"
    "</p>",
    unsafe_allow_html=True,
)
