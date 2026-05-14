import re

html_file = r'e:\MUSA-BUSINESS\Athena\index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

featured_data = {
    'hair': """[
                    { name: 'Signature Cut & Blowout', desc: 'Precision cutting and professional styling for a flawless, high-end look.', price: '£65', img: 'images/hair.png' },
                    { name: 'Luxury Balayage', desc: 'Bespoke hand-painted highlights for a natural, sun-kissed finish.', price: 'From £120', img: 'images/hair_2.png' }
                ]""",
    'laser': """[
                    { name: 'Full Face Rejuvenation', desc: 'Medical-grade laser treatment for smooth, clear and youthful facial skin.', price: '£45', img: 'images/laser.png' },
                    { name: 'Full Leg Smooth', desc: 'Complete hair removal for total confidence and permanent silkiness.', price: '£80', img: 'images/laser_2.png' }
                ]""",
    'facials': """[
                    { name: 'Extraction Deep Clean', desc: 'Efficiently clears blackheads and congestion without impacting skin health.', price: '£85', img: 'images/skin.png' },
                    { name: 'Time Resist Anti-Aging', desc: 'Bespoke facial that smooths wrinkles and delivers long-lasting results.', price: '£120', img: 'images/skin_2.png' }
                ]""",
    'hydrafacial': """[
                    { name: 'Platinum Hydrafacial', desc: 'The ultimate detox, rejuvenation, and protection experience for your skin.', price: '£160', img: 'images/hydra.png' },
                    { name: 'Signature Glow', desc: 'Deeply cleanses, extracts, and hydrates the skin using super serums.', price: '£100', img: 'images/hydra_2.png' }
                ]""",
    'microblading': """[
                    { name: 'Signature Microblading', desc: 'Perfectly symmetrical, hand-drawn hair strokes for flawless eyebrows.', price: 'POA', img: 'images/brows.png' },
                    { name: 'Mega Volume Lashes', desc: 'The most dramatic lash look for those seeking maximum impact.', price: '£100', img: 'images/brows_2.png' }
                ]""",
    'mani-pedi': """[
                    { name: 'Deluxe Shellac Manicure', desc: 'Luxury hand treatment including cuticle care, massage, and long-lasting color.', price: '£55', img: 'images/nails.png' },
                    { name: 'Luxury Spa Pedicure', desc: 'Bubble soak, exfoliation, and massage for perfectly rejuvenated feet.', price: '£65', img: 'images/nails_2.png' }
                ]""",
    'threading': """[
                    { name: 'Precision Brow Shaping', desc: 'Expert threading to frame your face with perfectly sculpted eyebrows.', price: '£15', img: 'images/threading.png' },
                    { name: 'Full Face Clarity', desc: 'Complete facial threading for a smooth, makeup-ready complexion.', price: '£35', img: 'images/threading_2.png' }
                ]""",
    'massage': """[
                    { name: 'Signature Deep Tissue', desc: 'Focuses on deeper muscle layers to release chronic tension and pain.', price: '£70', img: 'images/massage.png' },
                    { name: 'Hot Stone Aromatherapy', desc: 'Heated stones and essential oils for the ultimate relaxation experience.', price: '£95', img: 'images/massage_2.png' }
                ]"""
}

# Find each service block and inject 'featured' property.
for service_id, feat_val in featured_data.items():
    # Look for the start of the service object
    start_match = re.search(rf"'{service_id}':\s*{{", content)
    if not start_match:
        continue
    
    # Check if 'featured' already exists in this block
    # We find the next closing brace for this service
    block_start = start_match.end()
    block_end = content.find("},", block_start) # Rough estimate for service block end
    
    if "featured:" in content[block_start:block_end]:
        continue

    # Inject 'featured' after the 'benefits' line
    # Benefits can be wrapped in single quotes or backticks
    pattern = rf"('{service_id}':\s*{{.*?benefits:\s*['`].*?['`],)"
    replacement = r"\1" + f"\n                featured: {feat_val},"
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    if new_content != content:
        content = new_content

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Featured data injected.")
