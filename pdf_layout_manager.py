from PyPDF2 import PdfReader, PdfWriter
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color, HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.utils import simpleSplit
from PIL import Image
import os
import glob
import traceback
from datetime import datetime

class PDFLayoutManager:
    def __init__(self, input_pdf_path):
        try:
            self.reader = PdfReader(input_pdf_path)
            self.writer = PdfWriter()
            self.page_width = 612
            self.page_height = 792
            if len(self.reader.pages) == 0:
                raise ValueError("PDF has no pages")
        except Exception as e:
            print(f"Error initializing PDF: {str(e)}")
            raise

    def create_first_page(self, content, image_path):
        try:
            packet = io.BytesIO()
            can = canvas.Canvas(packet, pagesize=(self.page_width, self.page_height))
            
            # White background
            can.setFillColor(HexColor('#FFFFFF'))
            can.rect(0, 0, self.page_width, self.page_height, fill=1)
            
            # Start position
            y_position = self.page_height - 40
            
            # Header - Botify logo
            can.setFillColor(HexColor('#6B46C1'))
            can.setFont("Helvetica-Bold", 28)  # Slightly smaller logo
            logo_text = "botify"
            logo_width = can.stringWidth(logo_text, "Helvetica-Bold", 28)
            can.drawString(50, y_position, logo_text)
            
            # Title with adjusted size
            can.setFillColor(HexColor('#1A1A1A'))
            can.setFont("Helvetica-Bold", 20)  # Smaller title
            title = "David's Bridal Executive Summary"
            can.drawString(50 + logo_width + 15, y_position + 5, title)
            
            # Tracker sheet link with reduced spacing
            y_position -= 25  # Reduced spacing
            can.setFont("Helvetica", 10)  # Smaller link text
            can.setFillColor(HexColor('#2563EB'))
            link_text = "David's Bridal Project Tracker Sheet"
            link_url = "https://docs.google.com/spreadsheets/d/1HMzI-RnBOOZZjTNa9BvBcbpBDSD8ZP-rEctoP-e25ZE/edit?gid=1098252974#gid=1098252974"
            can.drawString(50, y_position, link_text)
            text_width = can.stringWidth(link_text, "Helvetica", 10)
            can.line(50, y_position - 1, 50 + text_width, y_position - 1)
            can.linkURL(link_url, (50, y_position - 2, 50 + text_width, y_position + 8))
            
            # Image section with reduced spacing
            if image_path and os.path.exists(image_path):
                y_position -= 25  # Reduced spacing
                img = Image.open(image_path)
                img_width, img_height = img.size
                
                # Calculate dimensions for smaller image
                target_width = self.page_width - 100
                scale_factor = target_width / img_width
                new_width = target_width
                new_height = img_height * scale_factor
                
                # Limit image height
                max_height = self.page_height * 0.3  # Reduced maximum height
                if new_height > max_height:
                    scale_factor = max_height / img_height
                    new_width = img_width * scale_factor
                    new_height = max_height
                
                x_position = (self.page_width - new_width) / 2
                can.drawImage(image_path, x_position, y_position - new_height,
                            width=new_width, height=new_height,
                            preserveAspectRatio=True)
                
                y_position = y_position - new_height - 20  # Reduced spacing

            # Sections with more compact layout
            sections = [
                ("Quarter over Quarter Metrics", [
                    "Non Branded Impressions & Clicks",
                    "Branded Impressions & Clicks",
                    "Brand vs. Non Brand conversion flow"
                ]),
                ("Technical SEO", [
                    "Indexable vs. Non Indexable",
                    "Status Codes",
                    "Sitemaps",
                    "Page Speed Performance"
                ]),
                ("Content SEO", [
                    "Presence of Smart Keyword",
                    "Impact of Internal Links on Ranking",
                    "Internal Links by Segment"
                ])
            ]

            for section_title, items in sections:
                # Section header with reduced spacing
                y_position -= 5
                can.setFillColor(HexColor('#FFFFFF'))
                can.roundRect(40, y_position - 5, self.page_width - 80, 25, 8, fill=1, stroke=1)
                
                can.setFillColor(HexColor('#1A1A1A'))
                can.setFont("Helvetica-Bold", 14)  # Smaller section headers
                can.drawString(50, y_position, section_title)
                y_position -= 25  # Reduced spacing
                
                # Bullet points with smaller text and tighter spacing
                can.setFont("Helvetica", 10)  # Smaller bullet point text
                for item in items:
                    # Bullet point
                    can.circle(65, y_position + 3, 1.5, fill=1)
                    # Text
                    can.drawString(80, y_position, item)
                    y_position -= 18  # Reduced spacing between bullets
                
                y_position -= 5  # Reduced spacing between sections
            
            can.save()
            packet.seek(0)
            return PdfReader(packet)
        except Exception as e:
            print(f"Error creating first page: {str(e)}")
            print(traceback.format_exc())
            return None

    def create_team_slide(self, team_image_path):
        try:
            packet = io.BytesIO()
            can = canvas.Canvas(packet, pagesize=(self.page_width, self.page_height))
            
            # White background
            can.setFillColor(HexColor('#FFFFFF'))
            can.rect(0, 0, self.page_width, self.page_height, fill=1)
            
            # Add Glossary Header
            y_position = self.page_height - 50
            can.setFillColor(HexColor('#1A1A1A'))
            can.setFont("Helvetica-Bold", 20)
            can.drawString(50, y_position, "Glossary")
            
            # Add line under header
            can.setStrokeColor(HexColor('#E5E7EB'))
            can.setLineWidth(1)
            can.line(50, y_position - 10, self.page_width - 50, y_position - 10)
            
            if team_image_path and os.path.exists(team_image_path):
                img = Image.open(team_image_path)
                img_width, img_height = img.size
                
                # Calculate dimensions to fit width while maintaining aspect ratio
                target_width = self.page_width - 80  # 40px margin on each side
                scale_factor = target_width / img_width
                new_width = target_width
                new_height = img_height * scale_factor
                
                # If height is too large, scale based on height instead
                max_height = self.page_height - 150  # Additional space for header
                if new_height > max_height:
                    scale_factor = max_height / img_height
                    new_width = img_width * scale_factor
                    new_height = max_height
                
                # Center the image below the header
                x_position = (self.page_width - new_width) / 2
                y_position = y_position - new_height - 40  # Space below header
                
                # Draw image without shadow
                can.drawImage(team_image_path, x_position, y_position,
                            width=new_width, height=new_height,
                            preserveAspectRatio=True)
            
            can.save()
            packet.seek(0)
            return PdfReader(packet)
        except Exception as e:
            print(f"Error creating team slide: {str(e)}")
            print(traceback.format_exc())
            return None

    def process_pdf(self, cover_image_path):
        try:
            # Add first page
            first_page = self.create_first_page(None, cover_image_path)
            if first_page:
                self.writer.add_page(first_page.pages[0])
            
            # Add content pages
            target_text = "Non-Branded KPI Trends"
            start_page = None
            
            for i in range(len(self.reader.pages)):
                text = self.reader.pages[i].extract_text()
                if target_text in text:
                    start_page = i
                    break
            
            if start_page is not None:
                for i in range(start_page, len(self.reader.pages)):
                    self.writer.add_page(self.reader.pages[i])
            
            # Add team slide at the end
            inputs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inputs')
            team_slide_path = os.path.join(inputs_dir, 'team-slide.png')
            
            if os.path.exists(team_slide_path):
                team_slide = self.create_team_slide(team_slide_path)
                if team_slide:
                    self.writer.add_page(team_slide.pages[0])
            
            return True
        except Exception as e:
            print(f"Error processing PDF: {str(e)}")
            print(traceback.format_exc())
            return False

    def save(self, output_path):
        try:
            with open(output_path, 'wb') as output_file:
                self.writer.write(output_file)
            return True
        except Exception as e:
            print(f"Error saving PDF: {str(e)}")
            print(traceback.format_exc())
            return False

def find_latest_files():
    try:
        inputs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inputs')
        if not os.path.exists(inputs_dir):
            os.makedirs(inputs_dir)
            print(f"Created inputs folder at: {inputs_dir}")
            return None, None
        
        pdf_files = glob.glob(os.path.join(inputs_dir, '*.pdf'))
        if not pdf_files:
            print(f"No PDF files found in: {inputs_dir}")
            return None, None
        
        image_files = glob.glob(os.path.join(inputs_dir, '*.[pP][nN][gG]'))
        if not image_files:
            print(f"No PNG files found in: {inputs_dir}")
            return None, None
        
        latest_pdf = max(pdf_files, key=os.path.getctime)
        # Find the cover image (exclude team-slide.png)
        cover_images = [f for f in image_files if os.path.basename(f).lower() != 'team-slide.png']
        if not cover_images:
            return None, None
        latest_image = max(cover_images, key=os.path.getctime)
        
        return latest_pdf, latest_image
    except Exception as e:
        print(f"Error finding files: {str(e)}")
        print(traceback.format_exc())
        return None, None

def main():
    try:
        input_pdf, input_image = find_latest_files()
        
        if not input_pdf or not input_image:
            print("Missing required files. Please ensure both PDF and image files are in the inputs folder.")
            return
        
        current_date = datetime.now().strftime('%Y%m%d')
        output_dir = os.path.dirname(os.path.abspath(__file__))
        output_pdf = os.path.join(output_dir, f'output{current_date}.pdf')
        
        manager = PDFLayoutManager(input_pdf)
        
        if manager.process_pdf(input_image) and manager.save(output_pdf):
            print(f"Successfully created: {os.path.basename(output_pdf)}")
        else:
            print("Failed to process PDF")
    except Exception as e:
        print(f"Error in main: {str(e)}")
        print(traceback.format_exc())

if __name__ == "__main__":
    main()