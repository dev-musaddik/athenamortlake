import re
import json

html_file = r'e:\MUSA-BUSINESS\Athena\index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update showPage function signature and hash routing
content = content.replace("function showPage(id) {", "function showPage(id, updateHash = true) {\n            if (updateHash && id !== 'home') window.location.hash = id;\n            if (updateHash && id === 'home') window.history.replaceState(null, null, ' ');")

routing_script = """
        // URL Hash Routing
        window.addEventListener('hashchange', () => {
            let hashId = window.location.hash.substring(1);
            if (!hashId || !contentData[hashId]) {
                showPage('home', false);
            } else {
                showPage(hashId, false);
            }
        });

        window.addEventListener('load', () => {
            let hashId = window.location.hash.substring(1);
            if (hashId && contentData[hashId]) {
                showPage(hashId, false);
            }
        });
    </script>
"""
content = content.replace("</script>", routing_script)


# 2. Add reviews to each service in contentData
reviews_data = {
    'hair': [
        "{ i: 'S', n: 'Sarah M.', text: 'Absolutely transformed my hair! The balayage looks incredibly natural and the salon is gorgeous. Highly recommend.' }",
        "{ i: 'E', n: 'Emma T.', text: 'Best haircut I have ever had in Richmond. The stylist truly listened and gave me exactly what I wanted.' }",
        "{ i: 'C', n: 'Chloe R.', text: 'My hair feels so healthy and bouncy. The luxury treatment products they use make a huge difference!' }"
    ],
    'laser': [
        "{ i: 'J', n: 'Jessica W.', text: 'Virtually painless laser hair removal. I saw results after just two sessions. The clinic is spotless.' }",
        "{ i: 'A', n: 'Amy B.', text: 'Professional and thorough. The staff made me feel incredibly comfortable throughout the entire treatment.' }",
        "{ i: 'M', n: 'Megan L.', text: 'So glad I chose Athena Mortlake. Fast, efficient, and my skin has never felt smoother. Worth every penny!' }"
    ],
    'facials': [
        "{ i: 'N', n: 'Natasha P.', text: 'The most relaxing facial of my life. My skin was glowing for weeks afterwards. The aesthetician was brilliant.' }",
        "{ i: 'L', n: 'Lucy K.', text: 'My acne has cleared up significantly since starting my bespoke skin treatments here. Truly life-changing.' }",
        "{ i: 'O', n: 'Olivia S.', text: 'A luxurious experience from start to finish. The clinic smells divine and the results are instantly visible.' }"
    ],
    'hydrafacial': [
        "{ i: 'K', n: 'Katie D.', text: 'My skin has literally never felt so clean. The Hydrafacial extracted everything and left me looking radiant.' }",
        "{ i: 'R', n: 'Rachel M.', text: 'Perfect pre-event treatment. The hydration boost is incredible and my makeup goes on flawlessly now.' }",
        "{ i: 'S', n: 'Sophie H.', text: 'You can actually see what they extract from your pores! Gross but so satisfying. Highly recommend.' }"
    ],
    'microblading': [
        "{ i: 'T', n: 'Tara C.', text: 'I am obsessed with my new brows. The symmetry is perfect and the colour match is spot on. Thank you!' }",
        "{ i: 'H', n: 'Hannah F.', text: 'I was nervous about the pain but the numbing cream worked perfectly. The mapping process was very thorough.' }",
        "{ i: 'Z', n: 'Zara J.', text: 'Waking up with perfect eyebrows every day saves me so much time. Best investment in my beauty routine.' }"
    ],
    'mani-pedi': [
        "{ i: 'M', n: 'Mia V.', text: 'The best BIAB gel manicure in Mortlake. My nails last for a whole month without chipping!' }",
        "{ i: 'F', n: 'Fiona G.', text: 'The spa pedicure is heaven. The massage chair and the foot scrub are exactly what I needed.' }",
        "{ i: 'P', n: 'Penny L.', text: 'Such attention to detail! Cuticles are flawless and the color selection is massive.' }"
    ],
    'threading': [
        "{ i: 'A', n: 'Amelia B.', text: 'Quick, precise, and surprisingly painless. They really know how to shape brows to frame your face.' }",
        "{ i: 'J', n: 'Jasmine K.', text: 'I only trust Athena with my brows. The threading is so much cleaner than waxing for my sensitive skin.' }",
        "{ i: 'E', n: 'Eleanor R.', text: 'Always perfectly shaped. The aloe vera cooling gel afterwards is a lovely touch.' }"
    ],
    'massage': [
        "{ i: 'D', n: 'David S.', text: 'The deep tissue massage sorted out my terrible back pain. The therapist really knew exactly where to target.' }",
        "{ i: 'V', n: 'Victoria M.', text: 'An oasis of calm in London. I floated out of the clinic feeling completely relaxed and tension-free.' }",
        "{ i: 'G', n: 'Grace W.', text: 'Perfect pressure and the heated massage oils were divine. I will definitely be making this a monthly habit.' }"
    ]
}

for service_id, reviews in reviews_data.items():
    reviews_str = "[\n                    " + ",\n                    ".join(reviews) + "\n                ]"
    pattern = rf"('{service_id}':\s*{{[^}}]+gallery:\s*\[.*?\],)"
    replacement = r"\1" + f"\n                reviews: {reviews_str},"
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# 3. Update the HTML template to use dynamic reviews
old_reviews_html = """                            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                                <div class="bg-white p-8 border border-stone-200 rounded-sm shadow-sm">
                                    <div class="flex items-center gap-4 mb-4">
                                        <div class="w-10 h-10 rounded-full bg-amber-100 flex items-center justify-center text-amber-700 font-bold">S</div>
                                        <div>
                                            <h4 class="font-bold text-sm">Sarah M.</h4>
                                            <div class="flex text-amber-400 text-[10px]">★★★★★</div>
                                        </div>
                                    </div>
                                    <p class="text-sm text-gray-600 leading-relaxed">"Amazing experience! The treatment relieved so much tension. Highly recommended."</p>
                                </div>
                                <div class="bg-white p-8 border border-stone-200 rounded-sm shadow-sm">
                                    <div class="flex items-center gap-4 mb-4">
                                        <div class="w-10 h-10 rounded-full bg-amber-100 flex items-center justify-center text-amber-700 font-bold">J</div>
                                        <div>
                                            <h4 class="font-bold text-sm">James T.</h4>
                                            <div class="flex text-amber-400 text-[10px]">★★★★★</div>
                                        </div>
                                    </div>
                                    <p class="text-sm text-gray-600 leading-relaxed">"Perfect after training sessions. Professional, knowledgeable and very effective. Will be back!"</p>
                                </div>
                                <div class="bg-white p-8 border border-stone-200 rounded-sm shadow-sm">
                                    <div class="flex items-center gap-4 mb-4">
                                        <div class="w-10 h-10 rounded-full bg-amber-100 flex items-center justify-center text-amber-700 font-bold">L</div>
                                        <div>
                                            <h4 class="font-bold text-sm">Lisa R.</h4>
                                            <div class="flex text-amber-400 text-[10px]">★★★★★</div>
                                        </div>
                                    </div>
                                    <p class="text-sm text-gray-600 leading-relaxed">"So relaxing and restorative. I left feeling lighter, looser and completely recharged. Thank you!"</p>
                                </div>
                            </div>"""

new_reviews_html = """                            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                                ${(data.reviews || []).map(r => `
                                <div class="bg-white p-8 border border-stone-200 rounded-sm shadow-sm">
                                    <div class="flex items-center gap-4 mb-4">
                                        <div class="w-10 h-10 rounded-full bg-amber-100 flex items-center justify-center text-amber-700 font-bold">${r.i}</div>
                                        <div>
                                            <h4 class="font-bold text-sm">${r.n}</h4>
                                            <div class="flex text-amber-400 text-[10px]">★★★★★</div>
                                        </div>
                                    </div>
                                    <p class="text-sm text-gray-600 leading-relaxed">"${r.text}"</p>
                                </div>`).join('')}
                            </div>"""

content = content.replace(old_reviews_html, new_reviews_html)

# Quick fix for close buttons calling showPage('home') without passing false during hash changes,
# but actually it's fine since we want click to update hash.

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Routing and reviews injected.")
