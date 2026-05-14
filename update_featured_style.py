import re

html_file = r'e:\MUSA-BUSINESS\Athena\index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clean up Laser headers (remove 'Laser:' prefix)
content = content.replace("header: 'Laser: Face'", "header: 'Face Treatments'")
content = content.replace("header: 'Laser: Arms'", "header: 'Arm Treatments'")
content = content.replace("header: 'Laser: Upper Body'", "header: 'Upper Body'")
content = content.replace("header: 'Laser: Lower Body'", "header: 'Lower Body'")
content = content.replace("header: 'Waxing: Upper Body (Strip / Hot)'", "header: 'Upper Body Waxing'")
content = content.replace("header: 'Waxing: Lower Body (Strip / Hot)'", "header: 'Lower Body Waxing'")

# 2. Update Featured Data to use more "Main Category" style names
featured_data = {
    'hair': """[
                    { name: 'Hair Cutting & Styling', desc: 'Precision cutting and professional styling for a flawless, high-end look.', price: 'from £65', img: 'images/hair.png' },
                    { name: 'Technical Colour Artistry', desc: 'Bespoke hand-painted highlights and balayage for a natural, sun-kissed finish.', price: 'from £120', img: 'images/hair_2.png' }
                ]""",
    'laser': """[
                    { name: 'Face Laser Treatments', desc: 'Medical-grade laser for smooth, clear and youthful facial skin. Targeted and precise.', price: 'from £45', img: 'images/laser.png' },
                    { name: 'Body Laser Treatments', desc: 'Complete hair removal for total confidence and permanent silkiness across all areas.', price: 'from £80', img: 'images/laser_2.png' }
                ]""",
    'facials': """[
                    { name: 'Deep Clean Facials', desc: 'Efficiently clears blackheads and congestion without impacting skin health.', price: 'from £85', img: 'images/skin.png' },
                    { name: 'Advanced Anti-Aging', desc: 'Bespoke facial that smooths wrinkles and delivers long-lasting dermatological results.', price: 'from £120', img: 'images/skin_2.png' }
                ]""",
    'hydrafacial': """[
                    { name: 'Signature Hydrafacial', desc: 'Deeply cleanses, extracts, and hydrates the skin using advanced vortex technology.', price: 'from £100', img: 'images/hydra.png' },
                    { name: 'Platinum Experience', desc: 'The ultimate detox, rejuvenation, and protection experience for your skin.', price: 'from £160', img: 'images/hydra_2.png' }
                ]""",
    'microblading': """[
                    { name: 'Brow Artistry', desc: 'Perfectly symmetrical, hand-drawn hair strokes for flawless, natural-looking eyebrows.', price: 'POA', img: 'images/brows.png' },
                    { name: 'Lash Enhancements', desc: 'The most dramatic lash looks for those seeking maximum impact and volume.', price: 'from £65', img: 'images/brows_2.png' }
                ]""",
    'mani-pedi': """[
                    { name: 'Manicure Studio', desc: 'Luxury hand treatment including cuticle care, massage, and long-lasting shellac color.', price: 'from £45', img: 'images/nails.png' },
                    { name: 'Pedicure Studio', desc: 'Bubble soak, exfoliation, and massage for perfectly rejuvenated and polished feet.', price: 'from £55', img: 'images/nails_2.png' }
                ]""",
    'threading': """[
                    { name: 'Precision Threading', desc: 'Expert threading to frame your face with perfectly sculpted eyebrows and clean lines.', price: 'from £15', img: 'images/threading.png' },
                    { name: 'Full Face Clarity', desc: 'Complete facial hair removal for a smooth, makeup-ready and radiant complexion.', price: 'from £35', img: 'images/threading_2.png' }
                ]""",
    'massage': """[
                    { name: 'Therapeutic Massage', desc: 'Focuses on deeper muscle layers to release chronic tension, pain and stress.', price: 'from £70', img: 'images/massage.png' },
                    { name: 'Luxury Body Rituals', desc: 'Heated stones and essential oils for the ultimate relaxation and sensory experience.', price: 'from £95', img: 'images/massage_2.png' }
                ]"""
}

# Update featured property in each service block
for service_id, feat_val in featured_data.items():
    # Replace existing featured array
    pattern = rf"('{service_id}':\s*{{.*?featured:\s*\[.*?\])"
    # We need to be careful with the inner brackets. 
    # Since we know the structure, we can try to find the end of the array.
    # A simpler way is to just find 'featured: [' and replace until the matching '],'
    
    # Let's find the start of the service block
    service_match = re.search(rf"'{service_id}':\s*{{", content)
    if not service_match: continue
    
    # Find the featured block within this service
    feat_start = content.find("featured:", service_match.end())
    if feat_start == -1: continue
    
    # Find the end of the featured array (closing bracket then comma)
    feat_end = content.find("],", feat_start) + 1
    
    # Replace it
    old_feat = content[feat_start:feat_end]
    new_feat = f"featured: {feat_val}"
    content = content.replace(old_feat, new_feat)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Headers cleaned and featured treatments updated to 'Main Category' style.")
