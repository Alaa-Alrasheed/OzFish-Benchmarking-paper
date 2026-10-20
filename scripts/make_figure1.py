"""Recreate Figure 1 from the species counts reported in manuscript Table 6.

Run with Python and reportlab. The vector PDF is written to the repository root.
Optional raster export: pdftoppm -singlefile -r 1000 -png figure1.pdf figure1
"""
from pathlib import Path

from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[1]
pdfmetrics.registerFont(TTFont("ChartArial", "C:/Windows/Fonts/arial.ttf"))
c = canvas.Canvas(str(ROOT / "figure1.pdf"), pagesize=(576, 432), initialFontName="ChartArial")
c.setTitle("Long-Tail Distribution (Species Count)")
c.setAuthor("")
left, bottom, width, height = 58, 40, 500, 350
scale = height / 170
c.setFillColor(HexColor("#e5e5e5"))
c.rect(left, bottom, width, height, fill=1, stroke=0)
c.setFont("ChartArial", 10)
for tick in range(0, 161, 20):
    y = bottom + tick * scale
    c.setStrokeColor(Color(1, 1, 1))
    c.setLineWidth(0.6)
    c.line(left, y, left + width, y)
    c.setFillColor(HexColor("#666666"))
    c.drawRightString(left - 7, y - 3, str(tick))
for i, (label, value, color) in enumerate(zip(
    ["Head (>100)", "Medium (21-100)", "Tail (<=20)"],
    [112, 161, 48], ["#1f77b4", "#ff7f0e", "#2ca02c"],
)):
    x = left + width * (i + 0.5) / 3
    c.setFillColor(HexColor(color))
    c.rect(x - 55, bottom, 110, value * scale, fill=1, stroke=0)
    c.setFillColor(HexColor("#000000"))
    c.drawCentredString(x, bottom + value * scale + 5, str(value))
    c.setFillColor(HexColor("#666666"))
    c.drawCentredString(x, bottom - 15, label)
c.setFillColor(HexColor("#000000"))
c.setFont("ChartArial", 14)
c.drawCentredString(left + width / 2, 405, "Long-Tail Distribution (Species Count)")
c.saveState()
c.translate(18, bottom + height / 2)
c.rotate(90)
c.setFont("ChartArial", 11)
c.drawCentredString(0, 0, "Number of Species")
c.restoreState()
c.showPage()
c.save()
