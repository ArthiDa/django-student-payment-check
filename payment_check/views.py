from django.shortcuts import render
from django.http import HttpResponse
from .models import Payment
import csv
import datetime
from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


# Create your views here.
def payment_view(request):
    payments = Payment.objects.all()
    return render(request, "payment_check/base.html", {"payments": payments})


def payment_csv_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="payments.csv"'

    writer = csv.writer(response)
    writer.writerow(
        [
            "Payment ID",
            "Token Number",
            "Student ID",
            "Student Name",
            "Service Date",
            "Total Amount",
            "Total Paid",
            "Balance Due",
            "Payment Status",
            "Payment Date",
        ]
    )

    payments = Payment.objects.all()
    counter = 1
    for payment in payments:
        writer.writerow(
            [
                counter,
                payment.token_num,
                payment.student_id,
                payment.student_name,
                payment.service_date,
                payment.total_amount,
                payment.total_paid,
                payment.balance_due,
                payment.payment_status,
                payment.payment_date,
            ]
        )
        counter += 1

    return response


def payment_pdf_view(request):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    # Add title
    styles = getSampleStyleSheet()
    elements.append(Paragraph("Payment Report", styles["Title"]))
    elements.append(Paragraph("<br/><br/>", styles["Normal"]))

    # Prepare data for the table
    data = [["S.No", "Student Name (ID)", "Amount", "Paid", "Due", "Status", "Date"]]
    payments = Payment.objects.all()
    counter = 1
    for payment in payments:
        data.append(
            [
                str(counter),
                f"{payment.student_name} ({payment.student_id})",
                f"Tk{payment.total_amount:.2f}",
                f"Tk{payment.total_paid:.2f}",
                f"Tk{payment.balance_due:.2f}",
                payment.payment_status,
                str(payment.payment_date) if payment.payment_date else "N/A",
            ]
        )
        counter += 1

    # Create table
    table = Table(
        data,
        colWidths=[
            0.7 * inch,
            2 * inch,
            1 * inch,
            1 * inch,
            1 * inch,
            1 * inch,
            1.3 * inch,
        ],
    )

    # Add style to table
    style = TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 12),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
            ("TEXTCOLOR", (0, 1), (-1, -1), colors.black),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
            ("FONTSIZE", (0, 1), (-1, -1), 10),
            ("TOPPADDING", (0, 1), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 1), (-1, -1), 6),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ]
    )
    table.setStyle(style)

    # Add table to elements
    elements.append(table)

    # Build PDF
    doc.build(elements)

    buffer.seek(0)
    response = HttpResponse(buffer, content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="payments.pdf"'

    return response
