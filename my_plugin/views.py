from django.shortcuts import render
from django.http import HttpResponse
from ipam.models import IPAddress
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph

def generate_pdf(ip_addresses):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ip_addresses.pdf"'

    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    # Add a heading
    styles = getSampleStyleSheet()
    # styles.add(ParagraphStyle(name='Heading1', fontSize=14, leading=16, spaceAfter=20))
    heading = Paragraph("IP Addresses Report", styles['Heading1'])
    elements.append(heading)
    
    # Add some space after the heading
    elements.append(Spacer(1, 12))

    data = [["IP Address", "Assigned", "Description", "Interface"]]
    for ip in ip_addresses:
        data.append([
            str(ip.address),
            str(ip.assigned_object) if ip.assigned_object else "No",
            str(ip.description) if ip.description else "",
            str(ip.interface.name) if ip.interface else ""
        ])

    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightblue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)
    doc.build(elements)
    return response

def ip_addresses_view(request):
    ip_addresses = IPAddress.objects.all()
    context = {
        'object': None,  # Ensure there is an object key in the context
        'ip_addresses': ip_addresses,
    }
    return render(request, 'my_plugin/ip_addresses.html', context)

def export_ip_addresses_pdf(request):
    if request.method == 'POST':
        ip_addresses = IPAddress.objects.all()
        return generate_pdf(ip_addresses)
    else:
        return HttpResponse(status=405)  # Method Not Allowed
