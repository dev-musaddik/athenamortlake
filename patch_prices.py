import re
import json

html_file = r'e:\MUSA-BUSINESS\Athena\index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

pricing_data = {
    'threading': """[
                    {
                        header: 'Threading',
                        items: [
                            { name: 'Eyebrows', val: '£15' },
                            { name: 'Upper Lip', val: '£10' },
                            { name: 'Chin', val: '£15' },
                            { name: 'Sides', val: '£25' },
                            { name: 'Full Face (no eyebrows)', val: '£35' }
                        ]
                    },
                    {
                        header: 'Eyebrows & Eyelashes',
                        items: [
                            { name: 'Eyebrow Tinting', val: '£20' },
                            { name: 'Eyebrows Threading', val: '£15' },
                            { name: 'Eyebrows Waxing', val: '£15' },
                            { name: 'Eyebrows Tint & Shape', val: '£30' },
                            { name: 'Eyelash Tinting', val: '£20' },
                            { name: 'Henna Brows', val: '£55' },
                            { name: 'Nouveau LVL Lash Lift', val: '£65' }
                        ]
                    },
                    {
                        header: 'Facial Waxing',
                        items: [
                            { name: 'Eyebrow', val: '£15' },
                            { name: 'Upper Lip', val: '£15' },
                            { name: 'Chin', val: '£10' },
                            { name: 'Sides', val: '£25' },
                            { name: 'Neck', val: '£15' },
                            { name: 'Full Face', val: '£35' }
                        ]
                    }
                ]""",
    'laser': """[
                    {
                        header: 'Laser: Face',
                        items: [
                            { name: 'Upper Lip', val: '£15' },
                            { name: 'Chin', val: '£18' },
                            { name: 'Centre Brow', val: '£7' },
                            { name: 'Forehead', val: '£30' },
                            { name: 'Sides of Face', val: '£25' },
                            { name: 'Neck', val: '£25' },
                            { name: 'Full Face', val: '£45' },
                            { name: 'Full Face & Neck', val: '£60' }
                        ]
                    },
                    {
                        header: 'Laser: Arms',
                        items: [
                            { name: 'Under Arms', val: '£10' },
                            { name: 'Half Arms', val: '£45' },
                            { name: 'Full Arms', val: '£80' },
                            { name: 'Hands & Under Arms', val: '£30' }
                        ]
                    },
                    {
                        header: 'Laser: Upper Body',
                        items: [
                            { name: 'Lower Back', val: '£60' },
                            { name: 'Upper Back', val: '£70' },
                            { name: 'Full Back', val: '£100' },
                            { name: 'Chest', val: '£60' },
                            { name: 'Abdomen', val: '£35' },
                            { name: 'Stomach Line', val: '£20' },
                            { name: 'Chest & Abdomen', val: '£75' },
                            { name: 'Shoulders', val: '£35' },
                            { name: 'Upper Back & Shoulders', val: '£75' },
                            { name: 'Full Back & Shoulders', val: '£110' }
                        ]
                    },
                    {
                        header: 'Laser: Lower Body',
                        items: [
                            { name: 'Upper Leg', val: '£50' },
                            { name: 'Lower Leg', val: '£65' },
                            { name: 'Full Leg', val: '£80' },
                            { name: 'Bikini Line', val: '£25' },
                            { name: 'Brazilian/Hollywood', val: '£30' },
                            { name: 'Buttocks', val: '£50' },
                            { name: 'Feet & Toes', val: '£30' }
                        ]
                    },
                    {
                        header: 'Waxing: Upper Body (Strip / Hot)',
                        items: [
                            { name: 'Under Arms', val: '£15 / £20' },
                            { name: 'Full Arm', val: '£30 / -' },
                            { name: 'Half Arm', val: '£20 / -' },
                            { name: 'Stomach', val: '£10 / -' }
                        ]
                    },
                    {
                        header: 'Waxing: Lower Body (Strip / Hot)',
                        items: [
                            { name: 'Full Leg', val: '£35 / -' },
                            { name: 'Lower Leg', val: '£18 / -' },
                            { name: 'Upper Leg', val: '£22 / -' },
                            { name: 'Lower Back', val: '£30 / -' },
                            { name: 'Full Back', val: '£30 / -' },
                            { name: 'Basic Bikini', val: '£15 / £20' },
                            { name: 'High Bikini', val: '£20 / £25' },
                            { name: 'Brazilian', val: '£25 / £35' },
                            { name: 'Hollywood', val: '£30 / £40' },
                            { name: 'Buttocks', val: '£15 / £20' },
                            { name: 'Full Body', val: '£99 / £120' }
                        ]
                    }
                ]""",
    'massage': """[
                    {
                        header: 'Aromatherapy',
                        items: [
                            { name: '30 minutes', val: '£35' },
                            { name: '60 minutes', val: '£65' },
                            { name: '90 minutes', val: '£95' }
                        ]
                    },
                    {
                        header: 'Swedish Massage',
                        items: [
                            { name: '30 minutes', val: '£40' },
                            { name: '60 minutes', val: '£70' },
                            { name: '90 minutes', val: '£95' }
                        ]
                    },
                    {
                        header: 'Deep Tissue',
                        items: [
                            { name: '30 minutes', val: '£40' },
                            { name: '60 minutes', val: '£70' },
                            { name: '90 minutes', val: '£95' }
                        ]
                    },
                    {
                        header: 'Back, Neck & Shoulders',
                        items: [
                            { name: '30 minutes', val: '£40' },
                            { name: '45 minutes', val: '£60' }
                        ]
                    },
                    {
                        header: 'Head Massage',
                        items: [
                            { name: '30 minutes', val: '£35' },
                            { name: '45 minutes', val: '£45' }
                        ]
                    }
                ]""",
    'facials': """[
                    {
                        header: 'Targeted Facials',
                        items: [
                            { name: 'Extraction (60m)', val: '£85' },
                            { name: 'Hydralessence (60m)', val: '£75' },
                            { name: 'Calming & Soothing (60m)', val: '£75' },
                            { name: 'Vital Defence (60m)', val: '£70' },
                            { name: 'Purity Treatment (60m)', val: '£70' }
                        ]
                    },
                    {
                        header: 'Premium Facials',
                        items: [
                            { name: 'Time Resist Anti-Aging (90m)', val: '£120' },
                            { name: 'Athena Bespoke Signature (90m)', val: '£120' }
                        ]
                    }
                ]""",
    'hydrafacial': """[
                    {
                        header: 'Hydrafacial Treatments',
                        items: [
                            { name: 'Signature Hydrafacial', val: '£100' },
                            { name: 'Deluxe Hydrafacial', val: '£130' },
                            { name: 'Platinum Hydrafacial', val: '£160' }
                        ]
                    }
                ]""",
    'mani-pedi': """[
                    {
                        header: 'Manicures (Polish / Shellac)',
                        items: [
                            { name: 'Mini Manicure', val: '£25 / £35' },
                            { name: 'Deluxe Manicure (45m)', val: '£45 / £55' },
                            { name: 'Shellac Removal', val: '£12' }
                        ]
                    },
                    {
                        header: 'Pedicures (Polish / Shellac)',
                        items: [
                            { name: 'Mini Pedicure', val: '£35 / £45' },
                            { name: 'Deluxe Pedicure (45m)', val: '£55 / £65' },
                            { name: 'Shellac Removal', val: '£15' }
                        ]
                    }
                ]""",
    'microblading': """[
                    {
                        header: 'Microblading',
                        items: [
                            { name: 'Initial Consultation', val: 'POA' },
                            { name: 'Microblading Treatment', val: 'POA' }
                        ]
                    },
                    {
                        header: 'Semi Permanent Individual Lashes',
                        items: [
                            { name: 'Classic Lashes', val: '£65' },
                            { name: 'Light Volume Lashes', val: '£80' },
                            { name: 'Mega Volume Lashes', val: '£100' },
                            { name: 'Infills for all Lashes', val: '£50' },
                            { name: 'Lash Removal', val: '£20' }
                        ]
                    }
                ]"""
}

# The regex should find the sections array for a given service and replace it.
# We will use a regex that matches from `sections: [` to the closing `],` for that property block.

for service_id, sections_val in pricing_data.items():
    # Find the block for the service, then replace its sections property.
    # It might be safer to just use string manipulation if regex is too greedy.
    
    # We find the index of the service id
    idx = content.find(f"'{service_id}': {{")
    if idx == -1:
        continue
    
    # Within this block, find `sections: [`
    start_sections = content.find("sections: [", idx)
    if start_sections == -1:
        # if sections doesn't exist, we can inject it before faq:
        start_faq = content.find("faq: [", idx)
        if start_faq != -1:
            content = content[:start_faq] + f"sections: {sections_val},\n                " + content[start_faq:]
        continue
        
    # Find the end of the sections array. It ends with `],`
    end_sections = content.find("],", start_sections)
    if end_sections != -1:
        content = content[:start_sections] + f"sections: {sections_val}" + content[end_sections + 1:]

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Pricing injected.")
