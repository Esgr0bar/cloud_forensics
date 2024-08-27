from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class ReportGenerator:
    def generate_report(self, findings, report_path):
        c = canvas.Canvas(report_path, pagesize=letter)
        c.drawString(100, 750, "Cloud Forensics Report")
        c.drawString(100, 730, "Findings:")
        for i, finding in enumerate(findings, start=1):
            c.drawString(100, 730 - (i * 20), finding)
        c.save()
        return report_path
