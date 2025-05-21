# Application: Assistant IA pour la Création de Contenu Optimisé
# Technologie: Python + API Gratuite + Streamlit (hébergement gratuit)

import streamlit as st
import requests
import json
import time
import re
from datetime import datetime

# Configuration de l'application
st.set_page_config(page_title="ContentOptimizer AI", page_icon="💡", layout="wide")

# Styles CSS personnalisés
st.markdown("""
<style>
    .main-header {text-align: center; color: #1E88E5; font-size: 2.5rem; font-weight: bold; margin-bottom: 30px;}
    .sub-header {color: #424242; font-size: 1.5rem; margin-bottom: 20px;}
    .category-header {color: #0D47A1; font-size: 1.2rem; font-weight: bold; margin-top: 25px;}
    .result-container {background-color: #f0f8ff; padding: 20px; border-radius: 10px; margin-top: 20px;}
    .pro-tip {background-color: #e8f5e9; padding: 15px; border-radius: 5px; margin: 15px 0;}
    .feature-box {padding: 10px; background-color: #e3f2fd; border-radius: 5px; margin-bottom: 10px;}
</style>
""", unsafe_allow_html=True)

# En-tête de l'application
st.markdown('<h1 class="main-header">ContentOptimizer AI</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="sub-header">Optimisez votre contenu pour les moteurs de recherche et maximisez votre impact en ligne</h2>', unsafe_allow_html=True)

# Sidebar pour la navigation
st.sidebar.image("https://via.placeholder.com/150x150.png?text=Logo", use_column_width=True)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choisissez un outil:", ["Générateur de contenu SEO", "Analyse de mots-clés", "Optimisation de titres", "Vérificateur de lisibilité"])

# Plan d'abonnement
st.sidebar.markdown("---")
st.sidebar.title("Plans d'abonnement")
selected_plan = st.sidebar.selectbox("Votre plan actuel:", ["Gratuit (3 analyses/jour)", "Pro (19.99€/mois)", "Expert (49.99€/mois)"])

# Compteur d'utilisation (simulation)
st.sidebar.markdown("---")
st.sidebar.subheader("Utilisation aujourd'hui")
if selected_plan == "Gratuit (3 analyses/jour)":
    st.sidebar.progress(0.33)
    st.sidebar.text("1/3 analyses utilisées")
else:
    st.sidebar.progress(0.12)
    st.sidebar.text("6/50 analyses utilisées")

# Fonction pour simuler l'appel à une API (utilise une API gratuite ou simule une réponse)
def analyze_content(content, keywords=None, analysis_type="seo"):
    # Simulation d'un délai d'API
    with st.spinner("Analyse en cours..."):
        time.sleep(2)
    
    # À remplacer par un vrai appel API (comme TextGears API gratuite ou une autre API gratuite)
    # Ici nous simulons simplement une réponse pour la démo
    if analysis_type == "seo":
        # Calcul de quelques métriques de base
        word_count = len(content.split())
        keyword_density = 0
        if keywords:
            keyword_count = sum(1 for word in content.lower().split() if word in keywords.lower().split())
            keyword_density = keyword_count / word_count if word_count > 0 else 0
            
        # Score de lisibilité simple
        avg_sentence_length = len(content) / max(1, len(re.split(r'[.!?]', content)) - 1)
        readability_score = min(100, max(0, 100 - (avg_sentence_length - 15) * 2))
        
        return {
            "word_count": word_count,
            "keyword_density": keyword_density * 100,
            "readability_score": readability_score,
            "recommendations": [
                "Ajoutez plus de mots-clés secondaires pour améliorer votre référencement",
                "Incluez plus de sous-titres avec des balises H2 et H3",
                "Enrichissez votre contenu avec des exemples concrets",
                "Considérez l'ajout d'images ou de graphiques pertinents"
            ],
            "seo_score": min(100, 55 + (word_count / 100) + (keyword_density * 100))
        }

# Fonction pour générer des suggestions de titres optimisés
def generate_titles(topic, keywords):
    # Simulation d'un délai d'API
    with st.spinner("Génération des titres optimisés..."):
        time.sleep(1.5)
    
    # Génération de titres basés sur des formats populaires
    base_titles = [
        f"Comment {topic} peut transformer votre {keywords}",
        f"{keywords.title()}: {topic.capitalize()} en 5 étapes simples",
        f"Les 7 secrets de {topic} que personne ne vous dit sur {keywords}",
        f"Pourquoi {topic} est essentiel pour votre succès en {keywords}",
        f"Guide complet: Maîtrisez {topic} pour dominer {keywords} en 2025",
    ]
    return base_titles

# Pages de l'application
if page == "Générateur de contenu SEO":
    st.markdown('<h3 class="category-header">Générateur de contenu optimisé pour le SEO</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        sujet = st.text_input("Sujet principal:", placeholder="Ex: marketing digital pour petites entreprises")
        keywords = st.text_input("Mots-clés principaux (séparés par des virgules):", placeholder="Ex: marketing digital, PME, stratégie en ligne")
        tone = st.selectbox("Tonalité:", ["Informatif", "Persuasif", "Didactique", "Conversationnel", "Professionnel"])
        word_count = st.slider("Nombre de mots cible:", 300, 2000, 800, 100)
    
    with col2:
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        st.subheader("Options avancées")
        include_stats = st.checkbox("Inclure des statistiques", value=True)
        include_examples = st.checkbox("Inclure des exemples concrets", value=True)
        include_cta = st.checkbox("Ajouter un appel à l'action", value=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="pro-tip">', unsafe_allow_html=True)
        st.markdown("**💡 Astuce Pro**: Les contenus de 1200-1500 mots sont généralement mieux classés dans les résultats de recherche Google.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("Générer du contenu optimisé"):
        if not sujet or not keywords:
            st.error("Veuillez remplir tous les champs obligatoires.")
        else:
            # Simuler la génération de contenu
            with st.spinner("Génération du contenu optimisé en cours..."):
                time.sleep(3)
                
            st.success("Contenu généré avec succès!")
            
            # Afficher le résultat
            st.markdown('<div class="result-container">', unsafe_allow_html=True)
            st.subheader("Votre contenu optimisé")
            st.markdown(f"""
            # {sujet.title()}: Guide Complet et Stratégies Efficaces
            
            ## Introduction
            Dans le monde concurrentiel d'aujourd'hui, {sujet} est devenu un élément essentiel pour toute entreprise souhaitant développer sa présence en ligne. Cet article explore les meilleures pratiques et stratégies pour maximiser votre impact dans ce domaine.
            
            ## Pourquoi {sujet.title()} est important
            Les recherches montrent que 82% des consommateurs recherchent des informations en ligne avant d'effectuer un achat. C'est pourquoi maîtriser {sujet} n'est plus une option mais une nécessité pour rester compétitif.
            
            ## Stratégies clés pour réussir
            1. **Analyse approfondie de votre audience**
            2. **Création de contenu de qualité**
            3. **Optimisation pour les moteurs de recherche**
            4. **Engagement sur les réseaux sociaux**
            5. **Mesure et ajustement de vos performances**
            
            ## Conclusion
            En intégrant ces stratégies dans votre approche de {sujet}, vous pourrez obtenir des résultats significatifs et durables.
            
            ## Appel à l'action
            Prêt à transformer votre approche de {sujet}? Téléchargez notre guide gratuit pour approfondir ces stratégies!
            """)
            
            # Analyse SEO du contenu généré
            sample_content = f"Le {sujet} est un élément essentiel pour les entreprises modernes. En utilisant les bons {keywords}, vous pouvez améliorer significativement vos résultats."
            analysis = analyze_content(sample_content, keywords)
            
            st.markdown("### Analyse SEO du contenu")
            col1, col2, col3 = st.columns(3)
            col1.metric("Score SEO", f"{int(analysis['seo_score'])}/100")
            col2.metric("Nombre de mots", analysis['word_count'])
            col3.metric("Densité de mots-clés", f"{analysis['keyword_density']:.1f}%")
            
            st.markdown("### Recommandations d'amélioration")
            for rec in analysis['recommendations']:
                st.markdown(f"- {rec}")
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Option pour télécharger ou partager
            st.download_button(
                label="Télécharger le contenu (Format Word)",
                data=sample_content,
                file_name=f"{sujet.replace(' ', '_')}_content.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

elif page == "Analyse de mots-clés":
    st.markdown('<h3 class="category-header">Analyse de mots-clés</h3>', unsafe_allow_html=True)
    st.write("Identifiez les mots-clés les plus pertinents pour votre secteur d'activité.")
    
    niche = st.text_input("Votre niche ou secteur d'activité:", placeholder="Ex: cours de yoga en ligne")
    location = st.text_input("Localisation (optionnel):", placeholder="Ex: Paris, France")
    
    if st.button("Analyser les mots-clés"):
        if not niche:
            st.error("Veuillez spécifier votre niche ou secteur d'activité.")
        else:
            with st.spinner("Recherche des meilleurs mots-clés..."):
                time.sleep(2.5)
            
            st.success("Analyse terminée!")
            
            # Tableau de résultats simulés
            st.markdown('<div class="result-container">', unsafe_allow_html=True)
            st.subheader("Mots-clés recommandés")
            
            data = {
                "Mot-clé": [
                    f"cours de {niche}", 
                    f"{niche} débutant", 
                    f"{niche} en ligne",
                    f"apprendre {niche}",
                    f"tutoriel {niche}",
                    f"formation {niche} certifiante",
                    f"{niche} avancé",
                    f"meilleur {niche}"
                ],
                "Volume recherche": [
                    "3,600", "2,900", "4,200", "1,800", "2,100", "1,400", "950", "3,200"
                ],
                "Difficulté": [
                    "68%", "42%", "57%", "35%", "29%", "61%", "27%", "72%"
                ],
                "CPC": [
                    "1.24€", "0.87€", "1.45€", "0.65€", "0.78€", "1.92€", "0.55€", "1.35€"
                ]
            }
            
            # Ajouter localisation si spécifiée
            if location:
                data["Mot-clé"].extend([f"{niche} {location}", f"{niche} près de {location}"])
                data["Volume recherche"].extend(["980", "720"])
                data["Difficulté"].extend(["32%", "25%"])
                data["CPC"].extend(["1.08€", "0.95€"])
            
            # Afficher le tableau
            st.table(data)
            
            # Graphique de tendance
            st.markdown("### Tendance de recherche")
            st.line_chart({
                "Cours en ligne": [100, 120, 132, 145, 180, 210, 205, 220, 240, 260, 280, 300],
                "Cours présentiel": [300, 290, 270, 250, 230, 210, 200, 190, 185, 180, 175, 170]
            })
            
            st.markdown("### Recommandations")
            st.markdown("""
            - Concentrez-vous sur les mots-clés à volume élevé et difficulté moyenne
            - Créez du contenu autour de 'cours de {} en ligne' qui montre une tendance croissante
            - Envisagez des mots-clés de longue traîne comme 'comment apprendre {} facilement'
            """.format(niche, niche))
            st.markdown('</div>', unsafe_allow_html=True)

elif page == "Optimisation de titres":
    st.markdown('<h3 class="category-header">Optimisation de titres pour articles et publications</h3>', unsafe_allow_html=True)
    st.write("Créez des titres accrocheurs qui attirent l'attention et optimisés pour le SEO.")
    
    topic = st.text_input("Sujet de votre article:", placeholder="Ex: techniques de méditation")
    main_keyword = st.text_input("Mot-clé principal:", placeholder="Ex: méditation pleine conscience")
    
    if st.button("Générer des titres optimisés"):
        if not topic or not main_keyword:
            st.error("Veuillez remplir tous les champs requis.")
        else:
            titles = generate_titles(topic, main_keyword)
            
            st.success("Titres générés avec succès!")
            
            st.markdown('<div class="result-container">', unsafe_allow_html=True)
            st.subheader("Titres optimisés suggérés")
            
            for i, title in enumerate(titles, 1):
                st.markdown(f"**{i}. {title}**")
                # Afficher un score et une analyse pour chaque titre
                col1, col2, col3 = st.columns(3)
                col1.metric("Score SEO", f"{80 + i}%")
                col2.metric("Score Émotionnel", f"{70 + i * 2}%")
                col3.metric("CTR Estimé", f"{4 + i * 0.5:.1f}%")
            
            st.markdown("### Caractéristiques d'un titre efficace")
            st.markdown("""
            - **Inclut le mot-clé principal** (idéalement au début)
            - **Évoque une émotion** (curiosité, urgence, excitation)
            - **Promet une valeur claire** (bénéfice, solution à un problème)
            - **Longueur optimale** (50-60 caractères pour Google)
            - **Utilise des chiffres ou listes** quand c'est pertinent
            """)
            st.markdown('</div>', unsafe_allow_html=True)

elif page == "Vérificateur de lisibilité":
    st.markdown('<h3 class="category-header">Vérificateur de lisibilité et optimisation SEO</h3>', unsafe_allow_html=True)
    st.write("Analysez et améliorez votre contenu pour qu'il soit plus lisible et mieux classé.")
    
    content = st.text_area("Collez votre texte ici:", height=250, placeholder="Entrez le texte que vous souhaitez analyser...")
    keywords_to_check = st.text_input("Mots-clés à vérifier (séparés par des virgules):", placeholder="Ex: intelligence artificielle, machine learning")
    
    if st.button("Analyser le contenu"):
        if not content:
            st.error("Veuillez entrer du contenu à analyser.")
        else:
            analysis = analyze_content(content, keywords_to_check)
            
            st.success("Analyse terminée!")
            
            st.markdown('<div class="result-container">', unsafe_allow_html=True)
            # Afficher les scores
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Score SEO", f"{int(analysis['seo_score'])}/100")
            col2.metric("Lisibilité", f"{int(analysis['readability_score'])}/100")
            col3.metric("Mots", analysis['word_count'])
            col4.metric("Densité mots-clés", f"{analysis['keyword_density']:.1f}%")
            
            # Afficher les recommandations
            st.markdown("### Recommandations d'amélioration")
            for rec in analysis['recommendations']:
                st.markdown(f"- {rec}")
            
            # Afficher des statistiques détaillées
            st.markdown("### Statistiques détaillées")
            detailed_stats = {
                "Nombre de caractères": len(content),
                "Nombre de mots": analysis['word_count'],
                "Nombre de phrases": len(re.split(r'[.!?]', content)) - 1,
                "Temps de lecture estimé": f"{max(1, round(analysis['word_count'] / 200))} minute(s)",
                "Niveau de lecture": "Intermédiaire",
                "Mots-clés manquants": "Aucun" if analysis['keyword_density'] > 1 else "Intégrez plus de mots-clés principaux"
            }
            
            for key, value in detailed_stats.items():
                st.markdown(f"**{key}:** {value}")
            
            # Afficher un texte optimisé suggéré
            st.markdown("### Version optimisée suggérée")
            st.markdown(f"*Une version optimisée de votre texte sera disponible avec l'abonnement Pro.*")
            
            if selected_plan == "Gratuit (3 analyses/jour)":
                st.info("Passez à l'abonnement Pro pour accéder à toutes les fonctionnalités d'optimisation.")
            st.markdown('</div>', unsafe_allow_html=True)

# Section de conversion (footer de l'application)
st.markdown("---")
st.markdown("## Commencez à monétiser votre contenu dès aujourd'hui!")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    Rejoignez plus de 5,000 créateurs de contenu qui utilisent ContentOptimizer AI pour:
    - Générer du contenu optimisé qui se classe mieux dans les résultats de recherche
    - Attirer plus de visiteurs sur leur site web ou blog
    - Augmenter leurs revenus publicitaires et d'affiliation
    - Gagner du temps dans leur processus de création de contenu
    """)

with col2:
    st.markdown('<div style="background-color:#f0f7ff; padding:15px; border-radius:10px; text-align:center;">', unsafe_allow_html=True)
    st.markdown("### Essayez le Plan Pro")
    st.markdown("**19.99€/mois**")
    st.markdown("✅ Analyses illimitées")
    st.markdown("✅ Optimisation avancée")
    st.markdown("✅ Priorité aux nouvelles fonctionnalités")
    st.button("Passer à l'abonnement Pro", key="upgrade_button")
    st.markdown('</div>', unsafe_allow_html=True)

# Afficher l'heure actuelle simulée
st.markdown(f"<div style='text-align:center; color:gray; font-size:0.8rem;'>Dernière mise à jour: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</div>", unsafe_allow_html=True)
