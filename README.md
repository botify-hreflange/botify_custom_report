# PDF Layout Manager for Executive Reports

A Python-based tool to generate and customize executive reports with a professional layout, integrating custom branding and content organization.

## Features

- Custom cover page generation with branding
- Professional layout for executive summaries
- Integration of images and charts
- Hyperlink support
- Section-based content organization
- Automated PDF processing

## Prerequisites

- Python 3.8 or higher
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd pdf-layout-manager
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Place your input files in the `inputs` folder:
   - Source PDF file
   - Image file (PNG format)

2. Run the script:
```bash
python pdf_layout_manager.py
```

The script will:
- Find the latest PDF and image files in the inputs folder
- Generate a new PDF with custom formatting
- Save the output as `output<YYYYMMDD>.pdf` in the project root

## File Structure

```
pdf-layout-manager/
├── inputs/               # Place input PDFs and images here
├── pdf_layout_manager.py # Main script
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Configuration

The script supports the following default settings:
- Page size: Letter (612 x 792 points)
- Font: Helvetica (with Bold variant)
- Primary brand color: #6B46C1 (Purple)
- Maximum image height: 30% of page height

## Output

The generated PDF will include:
1. A custom cover page with:
   - Company branding (botify logo)
   - Executive summary title
   - Project tracker link
   - Custom image
   - Organized sections with bullet points

2. Subsequent pages from the source PDF starting from the "Non-Branded KPI Trends" section

## Troubleshooting

Common issues:

1. Missing input files:
   - Ensure both PDF and image files are present in the `inputs` folder
   - Check file permissions

2. Image quality issues:
   - Ensure input images are high resolution
   - PNG format is recommended

3. Layout issues:
   - Check input image dimensions
   - Verify PDF content length

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details

## Acknowledgments

- ReportLab for PDF generation
- PyPDF2 for PDF manipulation
- Pillow for image processing