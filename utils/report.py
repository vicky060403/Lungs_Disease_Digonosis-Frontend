from io import BytesIO
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer,
    Image
)


def create_report(patient, prediction, confidence, image=None):

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        rightMargin=25,
        leftMargin=25,
        topMargin=25,
        bottomMargin=25,
    )

    styles = getSampleStyleSheet()

    title = styles["Title"]
    title.alignment = TA_CENTER

    heading = styles["Heading2"]

    normal = styles["BodyText"]

    story = []

    # =====================================================
    # Header
    # =====================================================

    story.append(
        Paragraph(
            "<font color='#0B72B9'><b>LUNG DISEASE DIAGNOSIS SYSTEM</b></font>",
            title,
        )
    )

    story.append(
        Paragraph(
            "<b>AI Powered Chest X-ray Diagnosis Report</b>",
            styles["Heading3"],
        )
    )

    story.append(Spacer(1, 15))

    report_id = datetime.now().strftime("LDD-%Y%m%d-%H%M%S")

    header = Table([
        ["Report ID", report_id],
        ["Date", datetime.now().strftime("%d-%m-%Y %H:%M")]
    ])

    header.setStyle(TableStyle([

        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#EAF4FF")),

        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),

        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),

        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),

    ]))

    story.append(header)

    story.append(Spacer(1, 20))

    # =====================================================
    # Patient Information
    # =====================================================

    story.append(Paragraph("Patient Information", heading))

    patient_table = Table([

        ["Patient Name", patient["name"]],

        ["Age", str(patient["age"])],

        ["Gender", patient["gender"]],

        ["Doctor", patient["doctor"]],

        ["Symptoms", patient["symptoms"]],

    ], colWidths=[130, 330])

    patient_table.setStyle(TableStyle([

        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),

        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#F2F6FC")),

        ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),

        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),

    ]))

    story.append(patient_table)

    story.append(Spacer(1, 20))

    # =====================================================
    # Uploaded X-ray
    # =====================================================

    if image is not None:

        story.append(Paragraph("Uploaded Chest X-ray", heading))

        image_bytes = BytesIO(image.getvalue())

        xray = Image(image_bytes)

        xray.drawHeight = 3 * inch
        xray.drawWidth = 3 * inch

        story.append(xray)

        story.append(Spacer(1, 20))

    # =====================================================
    # Prediction
    # =====================================================

    story.append(Paragraph("AI Diagnosis", heading))

    risk = "HIGH" if prediction == "PNEUMONIA" else "LOW"

    recommendation = (
        "Consult a physician immediately. Further clinical evaluation is recommended."
        if prediction == "PNEUMONIA"
        else
        "No signs of Pneumonia detected. Continue regular health monitoring."
    )

    diagnosis_table = Table([

        ["Prediction", prediction],

        ["Confidence", f"{confidence:.2f}%"],

        ["Risk Level", risk],

        ["Recommendation", recommendation]

    ], colWidths=[130, 330])

    diagnosis_table.setStyle(TableStyle([

        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),

        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#F2F6FC")),

        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),

        ("TEXTCOLOR",
         (1, 0),
         (1, 0),
         colors.red if prediction == "PNEUMONIA" else colors.green),

        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),

    ]))

    story.append(diagnosis_table)

    story.append(Spacer(1, 25))

    # =====================================================
    # Disclaimer
    # =====================================================

    story.append(Paragraph("Medical Disclaimer", heading))

    story.append(

        Paragraph(

            "This report is generated using an Artificial Intelligence model "
            "and is intended to assist healthcare professionals. "
            "It should not replace clinical judgment or professional diagnosis.",

            normal

        )

    )

    story.append(Spacer(1, 25))

    # =====================================================
    # Footer
    # =====================================================

    footer = Paragraph(

        "<font size=10>"
        "<b>Lung Disease Diagnosis System</b><br/>"
        "Built with PyTorch • BentoML • Docker • AWS • Streamlit"
        "</font>",

        styles["Heading4"]

    )

    story.append(footer)

    doc.build(story)

    buffer.seek(0)

    return buffer