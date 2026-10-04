"""Moringa Pakistan — product landing page for Moringa Leaf Powder Capsules."""
import urllib.parse
from pathlib import Path

import streamlit as st

# TODO: user to confirm moringa order number
WHATSAPP_NUMBER = "923323167915"

BASE_DIR = Path(__file__).parent
ASSETS = BASE_DIR / "assets"

PRODUCT_PHOTOS = [
    "1001849088_1_2oub.jpg",  # bottle + beige capsules
    "1001849089_2_cphn.jpg",  # bottle + green capsules
    "1001849087_3_pllz.jpg",  # doctor holding bottle (60 capsules)
]

PRICE_SALE = "Rs 1,800"
PRICE_REGULAR = "Rs 2,000"

st.set_page_config(
    page_title="Moringa Capsules Pakistan — 100% Natural Moringa Leaf Powder Capsules",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="collapsed",
)

ORDER_TEXT = urllib.parse.quote(
    "Assalam-o-Alaikum! I want to order Moringa Leaf Powder Capsules "
    "(60 capsules) at Rs 1,800 with Cash on Delivery. My name and address:"
)
ORDER_LINK = f"https://wa.me/{WHATSAPP_NUMBER}?text={ORDER_TEXT}"

st.markdown(
    """
    <style>
      .block-container { max-width: 640px; padding-top: 1.2rem; }
      .hero-price { font-size: 2.4rem; font-weight: 800; color: #1b7a3d; }
      .strike { text-decoration: line-through; color: #999; font-size: 1.2rem; }
      .badge { display:inline-block; background:#e8f6ee; color:#1b7a3d;
               border:1px solid #1b7a3d; border-radius:999px;
               padding:.35rem .9rem; font-weight:700; margin:.2rem .2rem; }
      .cta { display:block; text-align:center; background:#25D366; color:#fff !important;
             font-size:1.35rem; font-weight:800; border-radius:12px;
             padding:1rem; text-decoration:none; margin:1rem 0; }
      .card { background:#f6fbf7; border:1px solid #d9ecdf; border-radius:12px;
              padding:1rem; margin:.5rem 0; }
      .disclaimer { font-size:.82rem; color:#666; }
      h1, h2, h3 { color:#14532d; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------- HERO ----------------
st.title("🌿 Moringa Capsules Pakistan")
st.markdown(
    "### 100% Natural & Organic Moringa Leaf Powder Capsules"
)

hero_img = ASSETS / PRODUCT_PHOTOS[0]
if hero_img.exists():
    st.image(str(hero_img), use_container_width=True)

st.markdown(
    f'<div class="hero-price">{PRICE_SALE} '
    f'<span class="strike">{PRICE_REGULAR}</span></div>',
    unsafe_allow_html=True,
)
st.markdown("**60 capsules per bottle · Dietary Supplement**")
st.markdown(
    '<span class="badge">✅ Cash on Delivery</span>'
    '<span class="badge">🚚 All Pakistan</span>'
    '<span class="badge">🌱 100% Natural</span>',
    unsafe_allow_html=True,
)
st.markdown(
    f'<a class="cta" href="{ORDER_LINK}" target="_blank">'
    "📲 Order on WhatsApp — Rs 1,800</a>",
    unsafe_allow_html=True,
)
st.caption("Tap the button — your order message is already written. Just send it!")

# ---------------- BENEFITS ----------------
st.header("Why Moringa Capsules Pakistan?")
st.write(
    "Moringa — known in Urdu as **Sohanjna (سوہانجنا)** — is called the "
    "\u201cmiracle tree\u201d. Our capsules are made from pure moringa leaf "
    "powder, packed in easy-to-swallow capsules."
)
for emoji, title, text in [
    ("⚡", "Energy", "Supports natural daily energy without caffeine."),
    ("🛡️", "Immunity", "Moringa leaves are rich in vitamins and antioxidants "
                        "that support your immune system."),
    ("🌱", "General Wellness", "Supports general wellness as part of a "
                               "healthy daily routine."),
    ("✅", "100% Natural", "No artificial colours, flavours or preservatives. "
                           "Just pure moringa leaf powder."),
]:
    st.markdown(
        f'<div class="card"><b>{emoji} {title}</b><br>{text}</div>',
        unsafe_allow_html=True,
    )

# ---------------- HOW TO USE ----------------
st.header("How to Use")
st.write(
    "Take **1–2 capsules daily with a glass of water**, preferably with a "
    "meal. One bottle (60 capsules) lasts about 1–2 months."
)
st.markdown(
    f'<a class="cta" href="{ORDER_LINK}" target="_blank">'
    "📲 Order Now — Cash on Delivery</a>",
    unsafe_allow_html=True,
)

# ---------------- GALLERY ----------------
st.header("Moringa Capsules Pakistan — Product Gallery")
cols = st.columns(1)
for photo in PRODUCT_PHOTOS:
    p = ASSETS / photo
    if p.exists():
        st.image(str(p), use_container_width=True)

# ---------------- FAQ ----------------
st.header("Frequently Asked Questions")
with st.expander("Is Cash on Delivery (COD) available?"):
    st.write(
        "Yes! Cash on Delivery is available all over Pakistan. "
        "You pay when your order arrives at your door."
    )
with st.expander("How long does delivery take?"):
    st.write("Delivery usually takes 3–5 working days anywhere in Pakistan.")
with st.expander("How do I order?"):
    st.write(
        "Tap any green WhatsApp button on this page — your order message is "
        "already written. Just send it and we will confirm your address."
    )
with st.expander("How many capsules are in one bottle?"):
    st.write("Each bottle contains 60 capsules of pure moringa leaf powder.")
with st.expander("What is the price?"):
    st.write(
        f"Regular price {PRICE_REGULAR} — current sale price is "
        f"**{PRICE_SALE}** with Cash on Delivery."
    )

# ---------------- FINAL CTA ----------------
st.markdown(
    f'<a class="cta" href="{ORDER_LINK}" target="_blank">'
    f"📲 Order Moringa Capsules — {PRICE_SALE} (COD)</a>",
    unsafe_allow_html=True,
)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    '<p class="disclaimer">This is a herbal dietary supplement, not a '
    "medicine. Consult a doctor if you have a medical condition, are "
    "pregnant, or take regular medication.<br><br>"
    "© 2026 Moringa Pakistan. All rights reserved.</p>",
    unsafe_allow_html=True,
)
