import streamlit as st
import random
import time
from collections import Counter

# ==============================================================================
# DICCIONARIO Y FUNCIÓN
# ==============================================================================
COMPONENTES_NOMBRES = {
    "Elegante y Sofisticado/a": {
        "prefijos": ["Aura", "Éclat", "Symphonie", "Velours", "Lumière", "Essence", "Majesté"],
        "sufijos": ["Royale", "Prestige", "Impérial", "Souverain", "Noble", "Absolu", "Éternel"]
    },
    "Fresco y Cítrico": {
        "prefijos": ["Breeze", "Aqua", "Citrus", "Oasis", "Vitality", "Zephyr"],
        "sufijos": ["Zest", "Splash", "Fresh", "Pure", "Lush", "Verde"]
    },
    "Cálido y Dulce": {
        "prefijos": ["Douceur", "Nectar", "Velvet", "Ambre", "Delice"],
        "sufijos": ["Gourmand", "Secret", "Satin", "Elixir", "Privé"]
    }
}

def generar_nombre_dinamico(perfil_nombre):
    # Forzar una nueva semilla aleatoria basada en el tiempo actual en milisegundos
    random.seed(time.time_ns())
    
    # Buscar coincidencia parcial del nombre del perfil
    prefijos = ["Essence", "Éclat", "Aura", "Symphonie", "Velours", "Lumière", "Elixir", "Privé"]
    sufijos = ["Royale", "Prestige", "Impérial", "Souverain", "Absolu", "Éternel", "Custom", "Gold"]
    
    for clave, datos in COMPONENTES_NOMBRES.items():
        if clave.lower() in perfil_nombre.lower() or perfil_nombre.lower() in clave.lower():
            prefijos = datos["prefijos"]
            sufijos = datos["sufijos"]
            break

    prefijo = random.choice(prefijos)
    sufijo = random.choice(sufijos)
    
    # Agregar un número de lote único (entre 101 y 999) para que NUNCA sea idéntico
    lote = random.randint(101, 999)
    
    return f"{prefijo} {sufijo} N° {lote}"

# 1. Configuración de página
st.set_page_config(
    page_title="MyScent - Perfumería Personalizada", 
    page_icon="🌸", 
    layout="wide"
)

# 2. Encabezado de Marca
st.title("✨ MYSCENT")
st.caption("Tu esencia, tu perfume, tu historia")
st.divider()

# Base de datos de perfiles
PROFILES = {
    "elegante": {
        "name": "Elegante y Sofisticado/a",
        "description": "Buscas destacar con distinción, presencia impecable y un toque de sofisticación refinada.",
        "notes": ["Jazmín", "Rosa", "Sándalo", "Almizcle"],
        "formula": {"Floral": 40, "Amaderado": 30, "Almizclado": 20, "Vainilla": 10},
        "names": ["Éclat Prestige", "Aura Royale", "L'Élégance"]
    },
    "energetico": {
        "name": "Energético/a y Aventurero/a",
        "description": "Una combinación vibrante llena de frescura, movimiento y dinamismo para acompañar tu día.",
        "notes": ["Bergamota", "Limón", "Menta", "Jengibre"],
        "formula": {"Cítrico": 45, "Fresco": 25, "Especiado": 20, "Amaderado": 10},
        "names": ["Vértigo Sport", "Impulse Vital", "Energía Pura"]
    },
    "romantico": {
        "name": "Romántico/a y Sensible",
        "description": "Aromas cálidos, suaves y envolventes que expresan la calidez de tus emociones.",
        "notes": ["Rosa", "Vainilla", "Frutos Rojos", "Peonía"],
        "formula": {"Floral": 45, "Frutal": 25, "Vainilla": 20, "Almizcle": 10},
        "names": ["Amour Secret", "Esencia Dulce", "Encanto"]
    },
    "natural": {
        "name": "Natural y Sereno/a",
        "description": "Frescura herbal y acordes limpios que transmiten paz, equilibrio y conexión con lo natural.",
        "notes": ["Lavanda", "Té Verde", "Cedro", "Bergamota"],
        "formula": {"Herbal": 35, "Fresco": 30, "Cítrico": 20, "Amaderado": 15},
        "names": ["Brisa Silvestre", "Origen", "Calma Botánica"]
    },
    "misterioso": {
        "name": "Misterioso/a e Intenso/a",
        "description": "Una fragancia profunda, enigmática y con un carácter único que deja una huella inolvidable.",
        "notes": ["Ámbar", "Pachulí", "Cuero", "Vainilla"],
        "formula": {"Ámbar": 35, "Amaderado": 30, "Oriental": 20, "Vainilla": 15},
        "names": ["Nox Nocturne", "Mystère Noir", "Sombra Intensa"]
    }
}

QUESTIONS = [
    {"text": "¿Cómo describirías tu personalidad principal?", "options": {"Soy elegante y seguro/a": "elegante", "Soy activo/a y aventurero/a": "energetico", "Soy romántico/a y sensible": "romantico", "Soy tranquilo/a y natural": "natural", "Soy reservado/a e intenso/a": "misterioso"}},
    {"text": "¿En qué entorno te sientes más cómodo/a?", "options": {"Eventos o lugares sofisticados": "elegante", "Una aventura al aire libre": "energetico", "Una velada acogedora": "romantico", "Espacios abiertos y naturales": "natural", "Ambientes nocturnos e íntimos": "misterioso"}},
    {"text": "¿Qué familia olfativa despierta más tu interés?", "options": {"Florales refinados": "elegante", "Cítricos vibrantes": "energetico", "Notas dulces o frutales": "romantico", "Herbales y aromas limpios": "natural", "Amaderados y maderas orientales": "misterioso"}},
    {"text": "¿Qué mensaje deseas proyectar con tu esencia?", "options": {"Elegancia y distinción": "elegante", "Energía y dinamismo": "energetico", "Cercanía y calidez": "romantico", "Autenticidad y frescura": "natural", "Misterio y carácter exclusivo": "misterioso"}},
    {"text": "¿Qué estilo al vestir te representa mejor?", "options": {"Formal o sobrio": "elegante", "Deportivo o casual dinámico": "energetico", "Sutil, romántico o delicado": "romantico", "Cómodo, relajado y sencillo": "natural", "Estilo moderno, oscuro o urbano": "misterioso"}},
    {"text": "¿Qué sensación buscas al aplicar tu perfume diario?", "options": {"Sentirme impecable y preparado/a": "elegante", "Sentirme lleno/a de vitalidad": "energetico", "Sentirme en armonía y especial": "romantico", "Sentirme fresco/a y relajado/a": "natural", "Sentirme intrépido/a y diferente": "misterioso"}},
    {"text": "Al adquirir un producto, ¿qué atributo valoras más?", "options": {"Calidad y presentación del empaque": "elegante", "Innovación y funcionalidad": "energetico", "El concepto y los detalles emocionales": "romantico", "Simplicidad e ingredientes naturales": "natural", "Exclusividad e historia detrás del producto": "misterioso"}},
    {"text": "¿Cuál de las siguientes palabras resonaría como tu lema?", "options": {"Distinción": "elegante", "Libertad": "energetico", "Emoción": "romantico", "Armonía": "natural", "Misterio": "misterioso"}}
]

# NAVEGACIÓN POR PESTAÑAS
tab_test, tab_costos, tab_marca = st.tabs(["🌸 Test Olfativo", "📊 Simulación Financiera", "📍 Marca & Sede"])

# --- PESTAÑA 1: CUESTIONARIO ---
with tab_test:
    with st.form(key="myscent_form"):
        col1, col2 = st.columns([2, 1])
        with col1:
            nombre_cliente = st.text_input("Nombre del cliente", placeholder="Ej. Fabián Bastidas")
        with col2:
            linea_perfume = st.selectbox("Línea de preferencia", ["MyScent Unisex", "MyScent For Him", "MyScent For Her"])
        
        st.divider()
        respuestas_usuario = []
        for idx, q in enumerate(QUESTIONS):
            opcion = st.radio(
                label=f"**{idx + 1}. {q['text']}**",
                options=list(q['options'].keys()),
                key=f"q_{idx}"
            )
            respuestas_usuario.append(q['options'][opcion])
            
        submit_btn = st.form_submit_button("✨ Formular mi Perfume")

    if submit_btn:
        nombre_final = nombre_cliente.strip() if nombre_cliente.strip() else "Cliente"
        conteo = Counter(respuestas_usuario)
        perfil_key = conteo.most_common(1)[0][0]
        perfil = PROFILES[perfil_key]
        nombre_sugerido = generar_nombre_dinamico(perfil['name'])
        
        st.success(f"¡Formulación completada para **{nombre_final}**!")
        
        col_res1, col_res2 = st.columns(2)
        with col_res1:
            st.subheader(f"Perfil: {perfil['name']}")
            st.write(perfil['description'])
            st.write(f"**Nombre propuesto:** {nombre_sugerido}")
            st.write("**Notas recomendadas:**")
            st.markdown(" ".join([f"`{nota}`" for nota in perfil["notes"]]))
            
        with col_res2:
            st.subheader("🧪 Composición (100 ml)")
            for acorde, porcentaje in perfil["formula"].items():
                st.write(f"**{acorde} — {porcentaje}%**")
                st.progress(porcentaje / 100)
                # Construcción de fragmentos HTML sin conflictos de llaves
        notas_formatted = "".join([f'<span style="background-color:#F0EAE1; color:#C5A059; padding:5px 12px; border-radius:15px; font-weight:bold; font-size:12px; display:inline-block; margin:3px 2px;">{n}</span>' for n in perfil['notes']])
        
        formula_formatted = ""
        for acorde, pct in perfil['formula'].items():
            formula_formatted += f'''
            <div style="font-size:13px; font-weight:bold; margin-top:10px; margin-bottom:4px;">{acorde} — {pct}%</div>
            <div style="background-color:#F0EAE1; height:10px; border-radius:5px; overflow:hidden;">
                <div style="background-color:#C5A059; height:100%; width:{pct}%;"></div>
            </div>
            '''

        html_reporte = f"""<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>MyScent - Formulación</title>
    </head>
    <body style="font-family:'Helvetica Neue', Arial, sans-serif; background-color:#F9F6F0; color:#1C1C1C; padding:40px; margin:0;">
        <div style="background:#ffffff; border-radius:12px; padding:35px; max-width:800px; margin:0 auto; box-shadow:0 4px 15px rgba(0,0,0,0.08); border-top:6px solid #C5A059;">
            <div style="text-align:center; border-bottom:1px solid #E5E0D8; padding-bottom:15px; margin-bottom:25px;">
                <h1 style="color:#C5A059; margin:0; letter-spacing:2px; font-size:28px;">MYSCENT</h1>
                <p style="color:#666; margin-top:5px; font-style:italic;">Formulación Personalizada para <b>{nombre_final}</b></p>
            </div>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:30px;">
                <div>
                    <h2 style="font-size:18px; margin-top:0; color:#1C1C1C;">Perfil: {perfil['name']}</h2>
                    <p style="font-size:14px; color:#444; line-height:1.4;">{perfil['description']}</p>
                    <p style="margin-top:15px; font-size:14px;"><b>Nombre sugerido:</b><br><span style="color:#C5A059; font-weight:bold; font-size:16px;">{nombre_sugerido}</span></p>
                    <p style="margin-top:15px; font-size:14px; margin-bottom:5px;"><b>Notas principales:</b></p>
                    <div>{notas_formatted}</div>
                </div>
                <div>
                    <h2 style="font-size:18px; margin-top:0; color:#1C1C1C;">🧪 Composición (100 ml)</h2>
                    {formula_formatted}
                </div>
            </div>
        </div>
        <script>
            window.onload = function() {{ window.print(); }}
        </script>
    </body>
    </html>
    """

        st.divider()
        st.download_button(
            label="📄 Descargar Ficha de Formulación (HTML / PDF)",
            data=html_reporte,
            file_name=f"MyScent_{nombre_final.replace(' ', '_')}.html",
            mime="text/html"
        )
# --- PESTAÑA 2: SIMULADOR FINANCIERO ---
with tab_costos:
    st.header("📊 Calculadora de Costos e Inventario (MyScent)")
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        costo_frasco = st.number_input("Costo Frasco y Válvula (COP)", value=10000, step=1000)
        costo_empaque = st.number_input("Costo Caja, Etiqueta y Empaque (COP)", value=5000, step=1000)
        costo_esencia_ml = st.number_input("Costo Esencia Pura (COP/ml)", value=400, step=50)
        # --- NUEVO CAMPO: BASE DE ALCOHOL Y FIJADOR ---
        costo_base_ml = st.number_input("Costo Base Alcohol / Fijador (COP/ml)", value=15, step=5)
        
    with col_c2:
        tamano_ml = st.selectbox("Tamaño del Frasco (ml)", [100, 50, 30], index=0)
        concentracion = st.slider("Concentración de Esencia (%)", 15, 30, 20)
        precio_venta = st.number_input("Precio Venta Público (COP)", value=140000, step=5000)

    # --- CÁLCULOS SEPARADOS DE ESENCIA Y BASE ---
    ml_esencia = tamano_ml * (concentracion / 100)
    ml_base = tamano_ml - ml_esencia  # Mililitros de alcohol/fijador
    
    costo_total_esencia = ml_esencia * costo_esencia_ml
    costo_total_base = ml_base * costo_base_ml  # Costo real del alcohol
    
    # CPM Total (Costo de Producción del Producto Terminado)
    cpm_total = costo_frasco + costo_empaque + costo_total_esencia + costo_total_base
    
    # Márgenes y Utilidades
    margen_bruto = precio_venta - cpm_total
    porcentaje_margen_ventas = (margen_bruto / precio_venta) * 100 if precio_venta > 0 else 0
    markup_sobre_costo = (margen_bruto / cpm_total) * 100 if cpm_total > 0 else 0

    st.divider()
    
    # Visualización de Métricas Principales
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Costo Producción (CPM)", f"${cpm_total:,.0f} COP")
    m2.metric("Margen Bruto Unitario", f"${margen_bruto:,.0f} COP")
    m3.metric("Margen sobre Ventas", f"{porcentaje_margen_ventas:.1f}%")
    m4.metric("Markup sobre Costo", f"{markup_sobre_costo:.1f}%")
    
    # Desglose claro de insumos en una tarjeta colapsable
    with st.expander("🔍 Ver desglose exacto de insumos por frasco"):
        st.write(f"* **Esencia Pura ({concentracion}%):** {ml_esencia:.1f} ml ➔ **${costo_total_esencia:,.0f} COP**")
        st.write(f"* **Base Alcohol/Fijador ({100-concentracion}%):** {ml_base:.1f} ml ➔ **${costo_total_base:,.0f} COP**")
        st.write(f"* **Envase, Válvula y Empaque:** ➔ **${costo_frasco + costo_empaque:,.0f} COP**")

# --- PESTAÑA 3: MARCA Y SEDE ---
with tab_marca:
    st.header("📍 Ubicación y Marca")
    col_i1, col_i2 = st.columns(2)
    with col_i1:
        st.markdown("""
        **Sede Principal:**  
        📍 **Centro Comercial Viva Barranquilla**  
        Cra. 51B #87-50, Local 1-36  
        Barranquilla, Atlántico  
        
        **Horarios:**  
        Lunes a Sábado: 10:00 a.m. – 8:00 p.m.  
        Domingos y Festivos: 11:00 a.m. – 6:00 p.m.
        """)
    with col_i2:
        st.markdown("""
        **Propuesta de Valor:**  
        Perfumería personalizada en tiempo real impulsada por algoritmos de análisis de perfil para garantizar una fragancia única adaptada a la personalidad del cliente.
        """)