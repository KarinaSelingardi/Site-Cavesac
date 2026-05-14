import streamlit as st
from database import get_db_session, Volunteer
from notifications import send_notification

st.set_page_config(
    page_title="ONG Cavesac",
    page_icon="🤝",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Carrega CSS do arquivo externo ──────────────────────────────────
with open("style.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ── Session state para navegação ────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ── Navbar com links clicáveis ──────────────────────────────────────
pages = ["Home", "Quem Somos", "Voluntarie-se", "Como Doar", "Blog"]

# Gera o HTML da navbar com links clicáveis
nav_html = """
<div class="navbar">
  <div class="navbar-brand">ONG <span>Solidária</span></div>
  <div class="navbar-links">
"""
for p in pages:
    active = "active" if st.session_state.page == p else ""
    # Cada link agora tem um onclick que envia para o Streamlit via URL param
    page_key = p.lower().replace(" ", "-")
    nav_html += f'<a href="?page={page_key}" class="nav-link {active}">{p}</a>'
nav_html += "</div></div>"

st.markdown(nav_html, unsafe_allow_html=True)

# ── Detecta clique nos links via query params ───────────────────────
query_params = st.query_params
if "page" in query_params:
    target_page = query_params["page"]
    # Mapeia de volta para o nome correto da página
    page_map = {
        "home": "Home",
        "quem-somos": "Quem Somos",
        "voluntarie-se": "Voluntarie-se",
        "como-doar": "Como Doar",
        "blog": "Blog"
    }
    if target_page in page_map:
        st.session_state.page = page_map[target_page]

# ── Inicializa DB ───────────────────────────────────────────────────
session = get_db_session()

# ── Páginas ─────────────────────────────────────────────────────────

if st.session_state.page == "Home":
    # Hero
    st.markdown("""
    <div class="hero">
      <div class="hero-label">● Desde 2020 — Campinas, SP</div>
      <h1 class="hero-title">Transformando vidas com <em>solidariedade</em></h1>
      <p class="hero-sub">Acreditamos que pequenas ações criam grandes mudanças. Junte-se a nós e faça parte dessa história.</p>
      <div class="hero-stats">
        <div>
          <div class="hero-stat-num">1.200+</div>
          <div class="hero-stat-label">Famílias atendidas</div>
        </div>
        <div>
          <div class="hero-stat-num">340</div>
          <div class="hero-stat-label">Voluntários ativos</div>
        </div>
        <div>
          <div class="hero-stat-num">5</div>
          <div class="hero-stat-label">Anos de impacto</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Pilares
    st.markdown("""
    <div class="section">
      <div class="section-label">O que fazemos</div>
      <div class="section-title">Nossos pilares de atuação</div>
      <div class="cards-grid">
        <div class="card">
          <div class="card-icon">📚</div>
          <div class="card-title">Educação</div>
          <div class="card-text">Reforço escolar, cursos de capacitação e bolsas de estudo para jovens em situação de vulnerabilidade.</div>
        </div>
        <div class="card">
          <div class="card-icon">🍽️</div>
          <div class="card-title">Alimentação</div>
          <div class="card-text">Distribuição de cestas básicas e refeições quentes para famílias em necessidade na região.</div>
        </div>
        <div class="card">
          <div class="card-icon">🏥</div>
          <div class="card-title">Saúde</div>
          <div class="card-text">Campanhas de saúde, atendimentos psicológicos gratuitos e orientação médica comunitária.</div>
        </div>
        <div class="card">
          <div class="card-icon">🌱</div>
          <div class="card-title">Sustentabilidade</div>
          <div class="card-text">Hortas comunitárias, reciclagem e projetos de geração de renda para mães solo.</div>
        </div>
      </div>
    </div>
    <div class="divider"></div>
    """, unsafe_allow_html=True)

elif st.session_state.page == "Quem Somos":
    st.markdown("""
    <div class="page-header">
      <div class="section-label">Nossa história</div>
      <div class="section-title">Quem somos</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section">
      <p class="section-body" style="max-width:700px; font-size:1.05rem;">
        A ONG Solidária nasceu em 2020, no auge da pandemia, quando um grupo de amigos de Campinas 
        decidiu agir diante da crise social que se instalava. O que começou como uma rede de doação 
        de cestas básicas tornou-se uma das organizações mais ativas da região, com projetos em 
        educação, saúde e geração de renda.
      </p>
      <p class="section-body" style="max-width:700px; font-size:1.05rem; margin-top: 20px;">
        Somos movidos pela crença de que toda pessoa merece dignidade e oportunidade — 
        e que a comunidade tem o poder de promover essa transformação.
      </p>
    </div>
    <div class="divider"></div>
    <div class="section section-dark">
      <div class="section-label">Time</div>
      <div class="section-title" style="color:#F5F0E8;">As pessoas por trás da ONG</div>
      <div class="team-grid">
        <div class="team-card">
          <div class="team-avatar">👩</div>
          <div class="team-name">Ana Costa</div>
          <div class="team-role">Fundadora & Diretora</div>
        </div>
        <div class="team-card">
          <div class="team-avatar">👨</div>
          <div class="team-name">Rafael Lima</div>
          <div class="team-role">Coordenador de Projetos</div>
        </div>
        <div class="team-card">
          <div class="team-avatar">👩</div>
          <div class="team-name">Mariana Silva</div>
          <div class="team-role">Assistente Social</div>
        </div>
        <div class="team-card">
          <div class="team-avatar">👨</div>
          <div class="team-name">Bruno Santos</div>
          <div class="team-role">Relações Comunitárias</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.page == "Voluntarie-se":
    st.markdown("""
    <div class="page-header">
      <div class="section-label">Faça parte</div>
      <div class="section-title">Seja um voluntário</div>
    </div>
    <div class="section">
      <p class="section-body">
        Preencha o formulário abaixo. Nossa equipe entrará em contato em até 48h 
        para apresentar os projetos e encontrar a melhor forma de você contribuir.
      </p>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="form-wrapper">', unsafe_allow_html=True)
        with st.form("form_volunteer", clear_on_submit=True):
            name  = st.text_input("Nome completo")
            email = st.text_input("E-mail")
            phone = st.text_input("Telefone / WhatsApp")
            msg   = st.text_area("Habilidades ou por que quer ajudar?", height=120)
            submit = st.form_submit_button("Enviar cadastro →")
        st.markdown('</div>', unsafe_allow_html=True)

    if submit:
        if name and email and phone:
            try:
                new_v = Volunteer(name=name, email=email, phone=phone)
                session.add(new_v)
                session.commit()
                ok, email_msg = send_notification(name, email, phone)
                if ok:
                    st.success("✅ Cadastro realizado! Em breve entraremos em contato.")
                    st.balloons()
                else:
                    st.warning(f"⚠️ Dados salvos, mas o e-mail falhou: {email_msg}")
            except Exception as e:
                session.rollback()
                st.error(f"Erro ao salvar: {e}")
        else:
            st.error("Por favor preencha Nome, E-mail e Telefone.")

elif st.session_state.page == "Como Doar":
    st.markdown("""
    <div class="page-header">
      <div class="section-label">Contribua</div>
      <div class="section-title">Como fazer uma doação</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<p class="section-body">Sua contribuição mantém nossos projetos vivos. Qualquer valor faz a diferença.</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown("""
        <div class="donation-card">
          <h3>💚 PIX</h3>
          <p style="font-size:0.85rem; color:#7A7470;">Chave PIX (e-mail)</p>
          <div class="pix-key">pix@cavesac.org</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="donation-card">
          <h3>🏦 Transferência Bancária</h3>
          <div class="bank-info">
            Banco: <strong>001 — Banco do Brasil</strong><br>
            Agência: <strong>0001</strong><br>
            Conta Corrente: <strong>12345-6</strong><br>
            CNPJ: <strong>00.000.000/0001-00</strong>
          </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "Blog":
    st.markdown("""
    <div class="page-header">
      <div class="section-label">Novidades</div>
      <div class="section-title">Nosso blog</div>
    </div>
    <div class="section">
      <div class="blog-grid">
        <div class="blog-card">
          <div class="blog-img" style="background:#E8F4E8;">🌱</div>
          <div class="blog-body">
            <div class="blog-tag">Projetos</div>
            <div class="blog-card-title">Horta comunitária bate recorde de produção</div>
            <div class="blog-card-text">Em abril, nossa horta distribuiu mais de 200kg de alimentos frescos para famílias do bairro.</div>
          </div>
        </div>
        <div class="blog-card">
          <div class="blog-img" style="background:#E8EAF4;">📚</div>
          <div class="blog-body">
            <div class="blog-tag">Educação</div>
            <div class="blog-card-title">30 jovens concluem curso de informática</div>
            <div class="blog-card-text">A turma de março se forma com certificado e acesso a oportunidades no mercado de trabalho.</div>
          </div>
        </div>
        <div class="blog-card">
          <div class="blog-img" style="background:#F4EDE8;">❤️</div>
          <div class="blog-body">
            <div class="blog-tag">Comunidade</div>
            <div class="blog-card-title">Campanha de inverno arrecada 800 agasalhos</div>
            <div class="blog-card-text">Graças aos doadores, famílias do abrigo municipal receberam cobertores e roupas a tempo.</div>
          </div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ── Footer ──────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
  <div class="footer-brand">ONG <span>Cavesac</span></div>
  <p class="footer-text">
    Rua das Flores, 123 — Campinas, SP<br>
    contato@cavesac.org · (19) 99999-0000
  </p>
  <div class="footer-copy">© 2025 ONG Cavesac. Todos os direitos reservados.</div>
</div>
""", unsafe_allow_html=True)