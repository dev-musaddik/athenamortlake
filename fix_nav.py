import re

html_file = r'e:\MUSA-BUSINESS\Athena\index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all href="#" that have onclick with href="javascript:void(0);"
content = content.replace('href="#" onclick="showPage', 'href="javascript:void(0);" onclick="showPage')
content = content.replace('href="#" onclick="scrollToFooter', 'href="javascript:void(0);" onclick="scrollToFooter')
content = content.replace('href="#" onclick="toggleMobileMenu', 'href="javascript:void(0);" onclick="toggleMobileMenu')
content = content.replace("href='#' onclick='showPage", "href='javascript:void(0);' onclick='showPage")

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Navigation fixed.")
