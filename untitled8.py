# -*- coding: utf-8 -*-
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon

st.title("Interaktywny Mikołaj Bandzior 🎅💰")

# --- Interaktywne elementy ---
lewa_reka = st.slider("Kąt lewej ręki (stopnie)", 0, 90, 45)
prawa_reka = st.slider("Kąt prawej ręki (stopnie)", 0, 90, 45)
kolor_czapki = st.color_picker("Kolor czapki", "#ff0000")
kolor_koszulki = st.color_picker("Kolor koszulki", "#ff0000")

fig, ax = plt.subplots(figsize=(6, 8))

# --- GŁOWA ---
ax.add_patch(Circle((0.5, 0.78), 0.15, color="#f2d6b3"))

# --- CZAPKA ---
ax.add_patch(Polygon([[0.35, 0.88], [0.65, 0.88], [0.5, 1.02]], color=kolor_czapki))
ax.add_patch(Rectangle((0.32, 0.85), 0.36, 0.05, color="white"))
ax.add_patch(Circle((0.5, 1.02), 0.05, color="white"))

# --- TWARZ ---
ax.add_patch(Circle((0.45, 0.81), 0.02, color="black"))
ax.add_patch(Circle((0.55, 0.81), 0.02, color="black"))
ax.add_patch(Circle((0.5, 0.76), 0.03, color="red"))

# --- BRODA ---
ax.add_patch(Polygon([[0.38, 0.74], [0.62, 0.74], [0.75, 0.50], [0.25, 0.50]], color="white"))

# --- KOSZULKA ---
ax.add_patch(Circle((0.50, 0.33), 0.21, color=kolor_koszulki))

# --- DŁUGIE RĄCZKI (interaktywne) ---
import math

# funkcja do obracania ręki
def rotate_point(x, y, cx, cy, angle):
    # angle w stopniach
    rad = math.radians(angle)
    xr = cx + (x - cx) * math.cos(rad) - (y - cy) * math.sin(rad)
    yr = cy + (x - cx) * math.sin(rad) + (y - cy) * math.cos(rad)
    return xr, yr

# lewa ręka
x0, y0, w, h = 0.24, 0.45, 0.14, 0.18
x1, y1 = rotate_point(x0, y0, 0.31, 0.54, -lewa_reka)
ax.add_patch(Rectangle((x1, y1), w, h, color="red"))
ax.add_patch(Circle((x1, y1), 0.05, color="#f2d6b3"))

# prawa ręka
x0, y0 = 0.62, 0.45
x1, y1 = rotate_point(x0, y0, 0.69, 0.54, prawa_reka)
ax.add_patch(Rectangle((x1, y1), 0.14, 0.18, color="red"))
ax.add_patch(Circle((x1+0.14, y1+0.09), 0.05, color="#f2d6b3"))

# --- OKRĄGŁY WOREK ---
ax.add_patch(Circle((0.85, 0.18), 0.14, color="#8b4513"))
ax.add_patch(Circle((0.90, 0.28), 0.03, color="yellow"))

# --- NOGI ---
ax.add_patch(Rectangle((0.40, 0.05), 0.08, 0.13, color="red"))
ax.add_patch(Rectangle((0.52, 0.05), 0.08, 0.13, color="red"))

# --- BUTY ---
ax.add_patch(Rectangle((0.36, 0.00), 0.16, 0.06, color="black"))
ax.add_patch(Rectangle((0.48, 0.00), 0.16, 0.06, color="black"))

# --- PREZENTY ---
ax.add_patch(Rectangle((0.10, 0.05), 0.10, 0.10, color="#ff4444"))
ax.add_patch(Rectangle((0.145, 0.05), 0.02, 0.10, color="yellow"))
ax.add_patch(Rectangle((0.10, 0.095), 0.10, 0.02, color="yellow"))

ax.add_patch(Rectangle((0.22, 0.05), 0.12, 0.12, color="#44aaff"))
ax.add_patch(Rectangle((0.265, 0.05), 0.02, 0.12, color="white"))
ax.add_patch(Rectangle((0.22, 0.10), 0.12, 0.02, color="white"))

ax.add_patch(Rectangle((0.10, 0.18), 0.14, 0.14, color="#33cc33"))
ax.add_patch(Rectangle((0.163, 0.18), 0.02, 0.14, color="red"))
ax.add_patch(Rectangle((0.10, 0.245), 0.14, 0.02, color="red"))

# --- USTAWIENIA ---
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.15)
ax.axis('off')

# --- Streamlit ---
st.pyplot(fig)
