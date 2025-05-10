import csv
from statistics import mean, median, stdev
from fpdf import FPDF

# Read data from CSV
def read_data(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [(row['Name'], int(row['Score'])) for row in reader]
    return data

# Analyze data
def analyze_data(data):
    scores = [score for _, score in data]
    return {
        'mean': mean(scores),
        'median': median(scores),
        'stdev': stdev(scores),
        'max': max(scores),
        'min': min(scores)
    }

# Generate PDF report
def generate_pdf(data, stats, output_filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Internship Performance Report", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(100, 10, txt="Name", border=1)
    pdf.cell(40, 10, txt="Score", border=1)
    pdf.ln()

    pdf.set_font("Arial", size=12)
    for name, score in data:
        pdf.cell(100, 10, txt=name, border=1)
        pdf.cell(40, 10, txt=str(score), border=1)
        pdf.ln()

    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Statistics Summary", ln=True)

    for key, value in stats.items():
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"{key.capitalize()}: {value:.2f}", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", 'I', 10)
    pdf.cell(200, 10, txt="Completion certificate will be issued on your internship end date.", ln=True, align='C')
    pdf.output(output_filename)

# Main Execution
if __name__ == "__main__":
    filename = "data.csv"
    output_pdf = "internship_report.pdf"

    data = read_data(filename)
    stats = analyze_data(data)
    generate_pdf(data, stats, output_pdf)

    print(f"Report generated: {output_pdf}")