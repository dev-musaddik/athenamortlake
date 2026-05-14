import re

html_file = r'e:\MUSA-BUSINESS\Athena\index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

galleries = {
    'hair': "['images/hair.png', 'images/hair_2.png', 'images/hair_3.png']",
    'laser': "['images/laser.png', 'images/laser_2.png', 'images/laser.png']",
    'facials': "['images/skin.png', 'images/skin_2.png', 'images/skin.png']",
    'hydrafacial': "['images/hydra.png', 'images/hydra_2.png', 'images/hydra.png']",
    'microblading': "['images/brows.png', 'images/brows_2.png', 'images/brows.png']",
    'mani-pedi': "['images/nails.png', 'images/nails_2.png', 'images/nails.png']",
    'threading': "['images/threading.png', 'images/threading_2.png', 'images/threading.png']",
    'massage': "['images/massage.png', 'images/massage_2.png', 'images/massage.png']"
}

for service_id, gallery_array in galleries.items():
    pattern = rf"('{service_id}':\s*{{[^}}]+seoTitle:\s*`.*?`,)"
    replacement = r"\1" + f"\n                gallery: {gallery_array},"
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Galleries injected.")
