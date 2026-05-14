import re

html_file = r'e:\MUSA-BUSINESS\Athena\index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

seo_data = {
    'hair': {
        'seoTitle': """Luxury Hair Salon in Mortlake, Richmond""",
        'bullets': """['Master Colourists & Balayage Experts', 'L\\'Oréal Professionnel Treatments', 'Hair Fibre Restoration']""",
        'seoH2': """Experience the Ultimate Hair Transformation""",
        'subServices': """Precision Cutting, Balayage, Highlights, Keratin Treatment""",
        'seoContent': """<p>Located in the heart of Mortlake, Richmond, the Athena Hair Atelier offers an unparalleled hairdressing experience. Our master stylists are not just hairdressers; they are structural hair architects who understand the unique chemistry of your hair. Whether you are looking for a dramatic balayage transformation, precise foil highlights, or a simple, elegant cut, we utilize industry-leading L'Oréal Professionnel products to guarantee exceptional results.</p><p class="mt-4">We pride ourselves on our intensive consultation process. Before any scissors or bleach touch your hair, we assess your scalp health, hair elasticity, and lifestyle needs. This ensures your final look is not only stunning when you leave the salon but maintainable at home. Book your appointment at Richmond's premier luxury hair destination today.</p>"""
    },
    'laser': {
        'seoTitle': """Medical Laser Hair Removal in Mortlake, Richmond""",
        'bullets': """['Painless Diode Laser Technology', 'Safe for All Skin Types', 'Permanent Hair Reduction']""",
        'seoH2': """Silky, Smooth Skin with Advanced Laser Therapy""",
        'subServices': """Full Body Laser, Facial Laser, Bikini & Brazilian""",
        'seoContent': """<p>Say goodbye to the endless cycle of shaving, waxing, and painful ingrown hairs. Athena Clinical Spa in Mortlake offers the most advanced Medical Grade Diode Laser Hair Removal in the Richmond area. Our state-of-the-art systems feature built-in sapphire cooling technology, making your treatment virtually painless while aggressively targeting the hair follicle at the root.</p><p class="mt-4">Our highly trained clinicians tailor the laser settings to your specific Fitzpatrick skin type and hair density, ensuring maximum efficacy and safety. Most patients see a dramatic reduction in hair growth after just a few sessions. Experience the freedom of permanently smooth skin in our hygienic, luxury London clinic.</p>"""
    },
    'facials': {
        'seoTitle': """Advanced Skin Clinic & Facials in Mortlake, Richmond""",
        'bullets': """['Medical-Grade Skincare', 'Acne & Anti-Aging Specialists', 'Bespoke Dermatological Plans']""",
        'seoH2': """Revitalize Your Complexion with Clinical Skin Therapy""",
        'subServices': """Deep Cleansing, Chemical Peels, LED Therapy, Dermaplaning""",
        'seoContent': """<p>Achieve radiant, flawless skin at Athena Skin Clinic, the leading destination for advanced facials in Mortlake, Richmond. We go beyond traditional spa facials by utilizing clinical-grade active ingredients, chemical peels, and targeted LED light therapy. Our treatments are designed to combat complex skin issues including cystic acne, hyperpigmentation, rosacea, and premature aging.</p><p class="mt-4">Every face is unique, which is why we begin with a comprehensive digital skin mapping analysis. This allows our aesthetic practitioners to formulate a bespoke treatment protocol that repairs your skin's lipid barrier and stimulates collagen production from within. Experience a true clinical transformation and glowing results.</p>"""
    },
    'hydrafacial': {
        'seoTitle': """Official Hydrafacial™ Treatment in Mortlake, Richmond""",
        'bullets': """['Patented Vortex-Fusion Technology', 'Instant Glowing Results', 'Zero Downtime']""",
        'seoH2': """The Ultimate Deep Cleanse & Hydration Experience""",
        'subServices': """Signature Hydrafacial, Platinum Anti-Aging, Acne Clarifying""",
        'seoContent': """<p>Athena Clinical Spa is a certified provider of the world-renowned Hydrafacial™ treatment in Mortlake, Richmond. This revolutionary non-invasive procedure uses patented Vortex-Fusion technology to simultaneously extract impurities from deep within your pores while bathing the newly revealed skin in potent, hydrating super-serums.</p><p class="mt-4">In just 30 to 60 minutes, the Hydrafacial eliminates blackheads, reduces the appearance of fine lines, and instantly plumps the skin with hyaluronic acid and peptides. Because there is absolutely no downtime, it is the perfect "lunchtime" treatment or pre-event skin booster. Walk out of our London clinic with the signature Hydrafacial glow.</p>"""
    },
    'microblading': {
        'seoTitle': """Bespoke Microblading & Brows in Mortlake, Richmond""",
        'bullets': """['Golden Ratio Brow Mapping', 'Hyper-Realistic Hair Strokes', 'Medical-Grade Pigments']""",
        'seoH2': """Frame Your Face with Perfect, Semi-Permanent Brows""",
        'subServices': """Microblading, Ombre Powder Brows, Combination Brows""",
        'seoContent': """<p>Transform your facial architecture with bespoke microblading at Athena Clinic in Mortlake, Richmond. Our elite brow artists use the mathematical Golden Ratio to map the exact brow shape that flatters your unique bone structure. Using a sterile micro-blade, we implant medical-grade pigment into the upper dermal layer, creating hyper-realistic, hair-like strokes that blend seamlessly with your natural brow.</p><p class="mt-4">Whether you suffer from sparse, over-plucked brows or simply want to wake up every morning with perfect symmetry, our semi-permanent makeup solutions save you hours of daily preparation. Our pigments are rigorously tested to ensure they heal true to colour without fading into unnatural tones over time.</p>"""
    },
    'mani-pedi': {
        'seoTitle': """Luxury Nail Studio & Pedicure in Mortlake, Richmond""",
        'bullets': """['Clinical Sterilization Standards', 'Premium Gel & Shellac', 'Non-Toxic Nail Care']""",
        'seoH2': """Flawless Manicures and Restorative Foot Care""",
        'subServices': """Gel Manicure, Spa Pedicure, BIAB, Callus Peel""",
        'seoContent': """<p>Elevate your nail care routine at Athena's Luxury Nail Studio in Mortlake, Richmond. We completely reject the use of damaging electric drills and toxic acrylics that compromise your natural nail health. Instead, we focus on clinical hygiene, gentle cuticle work, and strengthening treatments like BIAB (Builder in a Bottle) to encourage natural nail growth.</p><p class="mt-4">Our spa pedicures go beyond basic polish; we incorporate clinical callus removal, exfoliating scrubs, and deep tissue foot massages to restore tired feet. Enjoy a long-lasting, high-gloss finish using premium systems like OPI and Shellac, all performed in a deeply relaxing, medical-grade sterilized environment.</p>"""
    },
    'threading': {
        'seoTitle': """Precision Threading & Hair Removal in Mortlake, Richmond""",
        'bullets': """['Organic Cotton Threading', 'Gentle on Sensitive Skin', 'Flawless Geometric Shaping']""",
        'seoH2': """The Ancient Art of Painless Facial Sculpting""",
        'subServices': """Eyebrow Threading, Upper Lip, Full Face Threading""",
        'seoContent': """<p>Experience the most precise method of facial hair removal at Athena Clinical Spa in Mortlake, Richmond. Threading is an ancient, highly skilled technique that uses a loop of 100% organic cotton thread to trap and lift hair directly from the follicle. Unlike waxing, threading does not pull or tear the delicate epidermis, making it the safest option for patients using retinols, chemical peels, or acne medications.</p><p class="mt-4">Our threading specialists are masters of geometric shaping, capable of creating incredibly crisp, clean lines that define your brows and highlight your natural bone structure. Enjoy slower, finer hair regrowth and a completely smooth, irritation-free complexion.</p>"""
    },
    'massage': {
        'seoTitle': """Full Body Massage in Mortlake, Richmond""",
        'bullets': """['Professional Certified Masseuse', 'Helps Treat Sports Injuries', 'Ultimate Relaxation']""",
        'seoH2': """Enjoy the Ultimate Relaxation from Massage Therapy""",
        'subServices': """Hand massage, Leg massage, Deep Tissue, Swedish""",
        'seoContent': """<p>Discover profound physical and mental relief at Athena Clinical Spa, the premier destination for therapeutic massage in Mortlake, Richmond. Our clinically trained massage therapists understand the intricate network of the human musculoskeletal system. Whether you are seeking ultimate relaxation to combat London city stress, or you need targeted deep tissue work for a sports injury, we tailor every session to your body's immediate requirements.</p><p class="mt-4">We employ a variety of advanced modalities, from sweeping Swedish techniques to lymphatic drainage and myofascial release. Our massages are designed to decrease cortisol levels, break down scar tissue, and improve blood circulation. Reconnect with your body and experience total restoration in our tranquil, luxury therapy suites.</p>"""
    }
}

for service_id, data in seo_data.items():
    pattern = rf"('{service_id}':\s*{{[^}}]+benefits:\s*'.*?',)"
    
    # Python multi-line replacement logic to avoid escaping nightmares in JavaScript string
    replacement = r"\1" + "\n"
    replacement += f"                seoTitle: `{data['seoTitle']}`,\n"
    replacement += f"                bullets: {data['bullets']},\n"
    replacement += f"                seoH2: `{data['seoH2']}`,\n"
    replacement += f"                subServices: `{data['subServices']}`,\n"
    replacement += f"                seoContent: `{data['seoContent']}`,"
    
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Data injected.")
