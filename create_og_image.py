from PIL import Image, ImageDraw, ImageFont
import os

def create_og_image():
    # Create image with gradient background
    width, height = 1200, 630
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    # Create gradient background (dark blue)
    for y in range(height):
        # Gradient from #0a0e17 to #1a1f2e
        r = int(10 + (26 - 10) * y / height)
        g = int(14 + (31 - 14) * y / height)
        b = int(23 + (46 - 23) * y / height)
        draw.rectangle([(0, y), (width, y + 1)], fill=(r, g, b))
    
    # Try to use a nice font, fall back to default if not available
    try:
        font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 72)
        font_medium = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 42)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
        font_stat = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
        font_stat_label = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    except:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()
        font_stat = ImageFont.load_default()
        font_stat_label = ImageFont.load_default()
    
    # Colors
    white = (255, 255, 255)
    cyan = (0, 217, 255)
    light_gray = (200, 200, 200)
    
    # Draw accent line
    draw.rectangle([(540, 100), (660, 104)], fill=cyan)
    
    # Draw name
    name = "ANUBHAV VERMA"
    name_bbox = draw.textbbox((0, 0), name, font=font_large)
    name_width = name_bbox[2] - name_bbox[0]
    draw.text(((width - name_width) / 2, 130), name, fill=white, font=font_large)
    
    # Draw title
    title = "Product Manager | AI Products"
    title_bbox = draw.textbbox((0, 0), title, font=font_medium)
    title_width = title_bbox[2] - title_bbox[0]
    draw.text(((width - title_width) / 2, 220), title, fill=cyan, font=font_medium)
    
    # Draw tagline
    tagline = "Built 2 AI products that reduce decision time by 90%"
    tagline_bbox = draw.textbbox((0, 0), tagline, font=font_small)
    tagline_width = tagline_bbox[2] - tagline_bbox[0]
    draw.text(((width - tagline_width) / 2, 290), tagline, fill=light_gray, font=font_small)
    
    # Draw stats
    stats = [
        ("2", "Products Shipped"),
        ("10x", "Faster Decisions"),
        ("7+", "PM Frameworks")
    ]
    
    stat_y = 380
    stat_spacing = 280
    start_x = (width - (stat_spacing * 3 - 100)) / 2
    
    for i, (value, label) in enumerate(stats):
        x = start_x + i * stat_spacing
        
        # Value
        value_bbox = draw.textbbox((0, 0), value, font=font_stat)
        value_width = value_bbox[2] - value_bbox[0]
        draw.text((x + (stat_spacing - value_width) / 2 - 90, stat_y), value, fill=cyan, font=font_stat)
        
        # Label
        label_bbox = draw.textbbox((0, 0), label, font=font_stat_label)
        label_width = label_bbox[2] - label_bbox[0]
        draw.text((x + (stat_spacing - label_width) / 2 - 90, stat_y + 60), label, fill=light_gray, font=font_stat_label)
    
    # Save image
    output_path = os.path.join(os.path.dirname(__file__), 'static', 'og-image.png')
    img.save(output_path, 'PNG', quality=95)
    print(f"✅ OG image created: {output_path}")
    print(f"   Size: 1200x630px")

if __name__ == '__main__':
    create_og_image()
