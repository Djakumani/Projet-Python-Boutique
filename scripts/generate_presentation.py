from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_AUTO_SHAPE_TYPE
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt


BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "docs"
SCREENSHOTS_DIR = DOCS_DIR / "screenshots"
OUTPUT_PATH = DOCS_DIR / "presentation_soutenance_boutique.pptx"

BG = RGBColor(247, 249, 252)
NAVY = RGBColor(17, 24, 39)
BLUE = RGBColor(37, 99, 235)
MUTED = RGBColor(75, 85, 99)
WHITE = RGBColor(255, 255, 255)


def add_background(slide, color):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_header_band(slide, title, subtitle=None):
    band = slide.shapes.add_shape(
        MSO_AUTO_SHAPE_TYPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.05)
    )
    band.fill.solid()
    band.fill.fore_color.rgb = NAVY
    band.line.fill.background()

    title_box = slide.shapes.add_textbox(Inches(0.6), Inches(0.22), Inches(8.6), Inches(0.35))
    p = title_box.text_frame.paragraphs[0]
    run = p.add_run()
    run.text = title
    run.font.size = Pt(26)
    run.font.bold = True
    run.font.color.rgb = WHITE

    if subtitle:
        sub_box = slide.shapes.add_textbox(Inches(0.6), Inches(0.62), Inches(9.0), Inches(0.25))
        p = sub_box.text_frame.paragraphs[0]
        run = p.add_run()
        run.text = subtitle
        run.font.size = Pt(11)
        run.font.color.rgb = RGBColor(209, 213, 219)


def add_bullets(slide, items, left, top, width, height):
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    first = True
    for item in items:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        p.text = item
        p.level = 0
        p.font.size = Pt(20)
        p.font.color.rgb = NAVY
        p.space_after = Pt(8)
        first = False
    return box


def add_caption(slide, text, left, top, width):
    box = slide.shapes.add_textbox(left, top, width, Inches(0.35))
    p = box.text_frame.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = text
    run.font.size = Pt(12)
    run.font.color.rgb = MUTED


def add_image_card(slide, image_name, left, top, width, height, caption):
    card = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = WHITE
    card.line.color.rgb = RGBColor(226, 232, 240)

    image_path = SCREENSHOTS_DIR / image_name
    slide.shapes.add_picture(str(image_path), left + Inches(0.12), top + Inches(0.12), width - Inches(0.24), height - Inches(0.45))
    add_caption(slide, caption, left, top + height - Inches(0.28), width)


def build_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_background(slide, NAVY)
    accent = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.RECTANGLE, Inches(0.65), Inches(0.85), Inches(1.5), Inches(0.12))
    accent.fill.solid()
    accent.fill.fore_color.rgb = BLUE
    accent.line.fill.background()

    title_box = slide.shapes.add_textbox(Inches(0.65), Inches(1.2), Inches(8.8), Inches(1.5))
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = "Projet Django\nBoutique en ligne"
    run.font.size = Pt(28)
    run.font.bold = True
    run.font.color.rgb = WHITE

    sub = slide.shapes.add_textbox(Inches(0.68), Inches(3.0), Inches(7.6), Inches(1.2))
    p = sub.text_frame.paragraphs[0]
    run = p.add_run()
    run.text = "Cours : Management des donnees et innovation\nEquipe : Zeinabou, Assia, Awa, Alexis, Chloe"
    run.font.size = Pt(18)
    run.font.color.rgb = RGBColor(226, 232, 240)

    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_background(slide, BG)
    add_header_band(slide, "Objectif du projet", "Un site de vente en ligne avec deux roles distincts")
    add_bullets(
        slide,
        [
            "Developper une boutique en ligne avec Django et SQLite.",
            "Permettre la gestion des articles par un administrateur.",
            "Permettre l'achat d'articles par un client connecte.",
            "Mettre a jour automatiquement le stock apres achat.",
        ],
        Inches(0.8),
        Inches(1.45),
        Inches(11.8),
        Inches(4.8),
    )

    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_background(slide, BG)
    add_header_band(slide, "Fonctionnalites principales")
    add_bullets(
        slide,
        [
            "Catalogue : designation, image, stock, prix, categories.",
            "Client : connexion, inscription, achat avec quantite controlee.",
            "Administrateur : ajout, modification, suppression des articles.",
            "Base SQL SQLite et interface web Django.",
        ],
        Inches(0.8),
        Inches(1.45),
        Inches(5.8),
        Inches(4.8),
    )
    add_bullets(
        slide,
        [
            "Images chargees depuis static/img.",
            "Tests automatiques des parcours critiques.",
            "Rapport PDF et captures de demonstration prepares.",
            "Projet relancable depuis GitHub avec README.",
        ],
        Inches(6.7),
        Inches(1.45),
        Inches(5.8),
        Inches(4.8),
    )

    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_background(slide, BG)
    add_header_band(slide, "Demonstration client")
    add_image_card(slide, "01-login-page.png", Inches(0.65), Inches(1.45), Inches(3.9), Inches(5.15), "Connexion")
    add_image_card(slide, "02-catalogue-client.png", Inches(4.72), Inches(1.45), Inches(4.05), Inches(5.15), "Catalogue")
    add_image_card(slide, "03-achat-page.png", Inches(8.94), Inches(1.45), Inches(3.75), Inches(5.15), "Achat")

    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_background(slide, BG)
    add_header_band(slide, "Verification du stock et gestion admin")
    add_image_card(slide, "04-stock-apres-achat.png", Inches(0.75), Inches(1.55), Inches(5.9), Inches(4.95), "Stock apres achat")
    add_image_card(slide, "05-gestion-admin.png", Inches(6.75), Inches(1.55), Inches(5.9), Inches(4.95), "Gestion administrateur")

    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_background(slide, BG)
    add_header_band(slide, "Repartition du travail")
    rows = [
        ("Zeinabou", "Structure du projet, URLs, integration finale et verification."),
        ("Assia", "Modele Article, base SQLite, categories, admin."),
        ("Awa", "Logique d'achat, stock, vues et formulaires."),
        ("Alexis", "Templates HTML, CSS, JavaScript et rendu visuel."),
        ("Chloe", "Jeux de donnees, images, tests et contenu de presentation."),
    ]
    table = slide.shapes.add_table(6, 2, Inches(0.85), Inches(1.6), Inches(11.7), Inches(4.6)).table
    table.columns[0].width = Inches(2.2)
    table.columns[1].width = Inches(9.5)
    table.cell(0, 0).text = "Membre"
    table.cell(0, 1).text = "Contribution"
    for col in range(2):
        cell = table.cell(0, col)
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY
        for paragraph in cell.text_frame.paragraphs:
            for run in paragraph.runs:
                run.font.bold = True
                run.font.color.rgb = WHITE
                run.font.size = Pt(14)
    for row_index, (name, contribution) in enumerate(rows, start=1):
        table.cell(row_index, 0).text = name
        table.cell(row_index, 1).text = contribution
        for col in range(2):
            cell = table.cell(row_index, col)
            cell.fill.solid()
            cell.fill.fore_color.rgb = WHITE
            for paragraph in cell.text_frame.paragraphs:
                for run in paragraph.runs:
                    run.font.size = Pt(13)
                    run.font.color.rgb = NAVY

    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_background(slide, BG)
    add_header_band(slide, "Conclusion")
    add_bullets(
        slide,
        [
            "Le site repond au cahier des charges du cours.",
            "Les deux roles sont fonctionnels : client et administrateur.",
            "Le stock est mis a jour automatiquement apres achat.",
            "Le projet est teste, documente et pret pour la soutenance.",
        ],
        Inches(0.85),
        Inches(1.6),
        Inches(11.5),
        Inches(3.4),
    )

    footer = slide.shapes.add_textbox(Inches(0.85), Inches(5.65), Inches(11.4), Inches(0.7))
    p = footer.text_frame.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = "Comptes de demonstration : admin / admin123   |   client1 / client123"
    run.font.size = Pt(18)
    run.font.bold = True
    run.font.color.rgb = BLUE

    prs.save(OUTPUT_PATH)


if __name__ == "__main__":
    build_presentation()
