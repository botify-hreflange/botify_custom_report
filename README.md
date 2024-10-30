# Botify Report Formatter

A Python-based tool specifically designed to enhance Botify's custom reports by adding branded cover pages and supplementary slides. This tool automates the process of creating professional executive summaries from Botify's raw reports.

## Purpose

This application transforms standard Botify reports by:
1. Adding a branded cover page with company logo and project overview
2. Preserving core report content starting from "Non-Branded KPI Trends"
3. Appending custom slides (like team information) at the end
4. Maintaining consistent branding and styling throughout

## Features

- Custom cover page with:
  - Botify branding
  - Project title
  - Quick-access links to project trackers
  - Overview metrics and sections
- Professional layout for executive summaries
- Team slide integration
- Automated content organization
- Hyperlink support
- Consistent styling and formatting

## Prerequisites

- Python 3.8 or higher
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd botify-report-formatter
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
   - Source Botify PDF report
   - Cover image (any PNG file except 'team-slide.png')
   - Team slide (must be named 'team-slide.png')

2. Run the script:
```bash
python pdf_layout_manager.py
```

The script will:
- Process the most recent PDF report from the inputs folder
- Add custom branding and formatting
- Include the team slide at the end
- Generate `output<YYYYMMDD>.pdf` in the project root

## File Structure

```
botify-report-formatter/
├── inputs/                # Place input files here
│   ├── *.pdf             # Botify source report
│   ├── *.png             # Cover image
│   └── team-slide.png    # Team information slide
├── pdf_layout_manager.py  # Main script
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Development Roadmap

### Current Focus
- [x] Basic PDF processing and generation
- [x] Custom cover page creation
- [x] Team slide integration
- [x] Hyperlink support
- [x] Consistent styling

### Short-term Goals
- [ ] Remove extra whitespace in generated PDFs
- [ ] Ensure all columns begin on the same page
- [ ] Add support for custom color schemes
- [ ] Improve error handling for malformed PDFs

### Future Enhancements
- [ ] Dynamic page scaling based on content
- [ ] Multiple team slide templates
- [ ] Custom font support
- [ ] Configuration file for branding settings
- [ ] Batch processing support
- [ ] PDF preview functionality
- [ ] Automated backup of source files

## Troubleshooting

Common issues:

1. Missing input files:
   - Ensure both PDF and image files are present in the `inputs` folder
   - Verify team-slide.png is named correctly
   - Check file permissions

2. Image quality issues:
   - Use high-resolution PNG images
   - Ensure images maintain aspect ratio
   - Verify image dimensions are appropriate

3. Layout issues:
   - Check input PDF formatting
   - Verify page content alignment
   - Ensure correct spacing between sections

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## Best Practices

When using this tool:
1. Always keep backup copies of original reports
2. Test with sample PDFs before processing important documents
3. Verify output PDF formatting and content
4. Maintain consistent image dimensions for cover images
5. Follow naming conventions for team slides

## License

This project is licensed under the MIT License - see the LICENSE file for details

## Acknowledgments

- Botify for the source report format
- ReportLab for PDF generation capabilities
- PyPDF2 for PDF manipulation
- Pillow for image processing