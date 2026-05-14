import re

html_file = r'e:\MUSA-BUSINESS\Athena\index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

new_template = r"""            const data = contentData[id];
            if (!data) return;

            // Generate hero icons logic
            const b1 = data.bullets && data.bullets[0] ? data.bullets[0] : 'Certified Specialist';
            const b2 = data.bullets && data.bullets[1] ? data.bullets[1] : 'Premium Care';
            const b3 = data.bullets && data.bullets[2] ? data.bullets[2] : 'Ultimate Comfort';

            let html = `
                <div class="page-view active">
                    
                    <!-- HERO SECTION -->
                    <div class="relative w-full py-24 md:py-32 lg:py-40 flex items-center justify-center">
                        <div class="absolute inset-0 z-0">
                            <img src="${data.hero}" class="w-full h-full object-cover">
                            <div class="absolute inset-0 bg-black/60"></div>
                        </div>
                        
                        <div class="relative z-10 w-full max-w-7xl mx-auto px-6 text-white">
                            <div class="max-w-3xl">
                                <span class="text-xs uppercase tracking-widest text-amber-200 mb-4 block font-medium">Athena Mortlake Clinical Spa</span>
                                <h1 class="text-4xl md:text-6xl lg:text-7xl serif leading-tight mb-6">${data.seoTitle}</h1>
                                <p class="text-lg md:text-xl text-gray-200 font-light mb-10 max-w-2xl leading-relaxed">${data.sub} • Professional clinical treatments for unparalleled results and recovery.</p>
                                
                                <div class="grid grid-cols-2 md:grid-cols-4 gap-6 mb-10">
                                    <div class="flex items-center gap-3">
                                        <svg class="w-6 h-6 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                                        <span class="text-xs md:text-sm font-medium">${b1}</span>
                                    </div>
                                    <div class="flex items-center gap-3">
                                        <svg class="w-6 h-6 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                                        <span class="text-xs md:text-sm font-medium">${b2}</span>
                                    </div>
                                    <div class="flex items-center gap-3">
                                        <svg class="w-6 h-6 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                                        <span class="text-xs md:text-sm font-medium">${b3}</span>
                                    </div>
                                    <div class="flex items-center gap-3">
                                        <svg class="w-6 h-6 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
                                        <span class="text-xs md:text-sm font-medium">Mortlake, Richmond</span>
                                    </div>
                                </div>

                                <div class="flex flex-col sm:flex-row gap-4">
                                    <button class="bg-black text-white px-8 py-4 font-bold text-sm tracking-widest uppercase hover:bg-white hover:text-black transition-colors" onclick="window.open('https://fresha.com')">Book Now</button>
                                    <button class="bg-[#25D366] text-white px-8 py-4 font-bold text-sm tracking-widest uppercase hover:bg-[#128C7E] transition-colors flex items-center justify-center gap-2" onclick="window.open('https://wa.me/440000000000')">
                                        <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M12.031 0C5.385 0 0 5.385 0 12.031c0 2.133.551 4.156 1.558 5.96L.101 24l6.195-1.621c1.729.897 3.666 1.365 5.735 1.365 6.646 0 12.031-5.385 12.031-12.031S18.677 0 12.031 0zM17.65 16.59c-.276.776-1.593 1.488-2.186 1.547-.56.055-1.282.164-3.693-.834-2.9-1.196-4.756-4.148-4.896-4.335-.141-.188-1.168-1.55-1.168-2.955 0-1.405.733-2.096 1.011-2.392.278-.297.604-.372.805-.372.2 0 .401.003.576.012.188.009.438-.073.687.525.263.633.916 2.235 1 2.423.083.188.139.407.014.656-.126.249-.189.407-.375.633-.186.225-.395.49-.56.633-.186.164-.383.344-.173.705.21.362.936 1.549 2.015 2.511 1.396 1.246 2.564 1.636 2.923 1.782.358.146.568.125.782-.125.214-.25 1.012-1.18 1.283-1.587.271-.408.542-.34.869-.216.326.124 2.062.973 2.417 1.15.355.176.592.264.678.414.086.15.086.867-.19 1.642z"/></svg>
                                        Call To Book
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- REVIEWS SECTION -->
                    <div class="bg-stone-50 py-16 border-b border-stone-200">
                        <div class="max-w-7xl mx-auto px-6">
                            <div class="text-center flex flex-col md:flex-row items-center justify-center gap-4 mb-10">
                                <h3 class="serif text-2xl">Trusted by Local Clients</h3>
                                <div class="flex items-center text-amber-500 gap-1">
                                    <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                                    <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                                    <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                                    <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                                    <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                                </div>
                                <span class="text-sm font-bold text-gray-400 uppercase tracking-widest">Rated 5.0</span>
                            </div>
                            
                            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
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
                            </div>
                        </div>
                    </div>

                    <!-- 3 IMAGES ROW -->
                    <div class="grid grid-cols-3 gap-2 md:gap-6 max-w-7xl mx-auto px-2 md:px-6 py-10 md:py-16">
                        <img src="${data.hero}" class="w-full h-32 md:h-64 object-cover rounded-sm grayscale hover:grayscale-0 transition duration-500" style="object-position: center top;">
                        <img src="${data.hero}" class="w-full h-32 md:h-64 object-cover rounded-sm grayscale hover:grayscale-0 transition duration-500" style="object-position: center center;">
                        <img src="${data.hero}" class="w-full h-32 md:h-64 object-cover rounded-sm grayscale hover:grayscale-0 transition duration-500" style="object-position: center bottom;">
                    </div>

                    <!-- MAIN CONTENT SPLIT -->
                    <div class="max-w-7xl mx-auto px-6 py-12">
                        <div class="grid grid-cols-1 lg:grid-cols-12 gap-16 lg:gap-24">
                            
                            <!-- Left Column -->
                            <div class="lg:col-span-7">
                                <span class="text-[10px] uppercase tracking-[0.3em] font-bold text-amber-600 block mb-4">Relax • Recover • Restore</span>
                                <h2 class="text-3xl md:text-4xl serif leading-tight mb-6">${data.seoH2}</h2>
                                <p class="text-gray-600 leading-relaxed mb-12">${data.clinical}</p>

                                <!-- 4 Grid Feature Boxes -->
                                <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 mb-12">
                                    <div class="border border-stone-200 p-6 bg-stone-50 rounded-sm">
                                        <svg class="w-8 h-8 text-amber-500 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                                        <h4 class="font-bold text-sm mb-2">${b1}</h4>
                                        <p class="text-xs text-gray-500 leading-relaxed">Qualified, experienced and committed to safe, effective treatments tailored to your needs.</p>
                                    </div>
                                    <div class="border border-stone-200 p-6 bg-stone-50 rounded-sm">
                                        <svg class="w-8 h-8 text-amber-500 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                                        <h4 class="font-bold text-sm mb-2">${b2}</h4>
                                        <p class="text-xs text-gray-500 leading-relaxed">Advanced techniques that accelerate healing and relieve built-up physical tension quickly.</p>
                                    </div>
                                    <div class="border border-stone-200 p-6 bg-stone-50 rounded-sm">
                                        <svg class="w-8 h-8 text-amber-500 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                                        <h4 class="font-bold text-sm mb-2">${b3}</h4>
                                        <p class="text-xs text-gray-500 leading-relaxed">Relieves stress, eases anxiety and promotes deep relaxation for both body and mind.</p>
                                    </div>
                                    <div class="border border-stone-200 p-6 bg-stone-50 rounded-sm">
                                        <svg class="w-8 h-8 text-amber-500 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
                                        <h4 class="font-bold text-sm mb-2">Tailored to Your Body</h4>
                                        <p class="text-xs text-gray-500 leading-relaxed">Every session is customised to your specific physical concerns and comfort levels.</p>
                                    </div>
                                </div>

                                <!-- Treatment Areas Box -->
                                <div class="border border-stone-200 p-6 bg-white flex flex-col md:flex-row items-start md:items-center gap-6 mb-12">
                                    <svg class="w-10 h-10 text-amber-500 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                                    <div>
                                        <h4 class="font-bold text-sm mb-2">Treatment Capabilities</h4>
                                        <p class="text-xs text-gray-600 font-medium tracking-wide uppercase leading-loose">${data.subServices.split(',').join(' • ')}</p>
                                    </div>
                                </div>

                                <!-- CTA Mini Banner -->
                                <div class="bg-stone-100 p-8 text-center rounded-sm mb-16">
                                    <svg class="w-8 h-8 text-amber-500 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"></path></svg>
                                    <h3 class="serif text-2xl mb-6">Ready to Relax, Recover and Feel Better?</h3>
                                    <div class="flex flex-col sm:flex-row justify-center gap-4">
                                        <button class="bg-black text-white px-8 py-3 text-xs font-bold uppercase tracking-widest hover:bg-gray-800 transition" onclick="window.open('https://fresha.com')">Book Your Treatment</button>
                                        <button class="bg-[#25D366] text-white px-8 py-3 text-xs font-bold uppercase tracking-widest hover:bg-[#128C7E] transition flex items-center justify-center gap-2" onclick="window.open('https://wa.me/440000000000')">
                                            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M12.031 0C5.385 0 0 5.385 0 12.031c0 2.133.551 4.156 1.558 5.96L.101 24l6.195-1.621c1.729.897 3.666 1.365 5.735 1.365 6.646 0 12.031-5.385 12.031-12.031S18.677 0 12.031 0zM17.65 16.59c-.276.776-1.593 1.488-2.186 1.547-.56.055-1.282.164-3.693-.834-2.9-1.196-4.756-4.148-4.896-4.335-.141-.188-1.168-1.55-1.168-2.955 0-1.405.733-2.096 1.011-2.392.278-.297.604-.372.805-.372.2 0 .401.003.576.012.188.009.438-.073.687.525.263.633.916 2.235 1 2.423.083.188.139.407.014.656-.126.249-.189.407-.375.633-.186.225-.395.49-.56.633-.186.164-.383.344-.173.705.21.362.936 1.549 2.015 2.511 1.396 1.246 2.564 1.636 2.923 1.782.358.146.568.125.782-.125.214-.25 1.012-1.18 1.283-1.587.271-.408.542-.34.869-.216.326.124 2.062.973 2.417 1.15.355.176.592.264.678.414.086.15.086.867-.19 1.642z"/></svg>
                                            Call To Book
                                        </button>
                                    </div>
                                </div>

                                <!-- SEO Content Box -->
                                <div class="mb-16">
                                    <h3 class="serif text-2xl mb-6">${data.seoTitle}</h3>
                                    <div class="text-sm text-gray-600 leading-relaxed space-y-4">
                                        ${data.seoContent}
                                    </div>
                                </div>
                            </div>

                            <!-- Right Column (Sidebar) -->
                            <div class="lg:col-span-5 space-y-8 lg:self-start sticky top-24">
                                
                                <!-- Booking Fast -->
                                <div class="bg-stone-50 border border-stone-200 p-8 rounded-sm">
                                    <h3 class="serif text-2xl mb-4">Need to book fast?</h3>
                                    <p class="text-sm text-gray-600 mb-6">Call or message us to arrange your appointment today.</p>
                                    <button class="w-full mb-3 bg-[#25D366] text-white px-6 py-4 text-xs font-bold uppercase tracking-widest hover:bg-[#128C7E] transition flex items-center justify-center gap-2" onclick="window.open('https://wa.me/440000000000')">
                                        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M12.031 0C5.385 0 0 5.385 0 12.031c0 2.133.551 4.156 1.558 5.96L.101 24l6.195-1.621c1.729.897 3.666 1.365 5.735 1.365 6.646 0 12.031-5.385 12.031-12.031S18.677 0 12.031 0zM17.65 16.59c-.276.776-1.593 1.488-2.186 1.547-.56.055-1.282.164-3.693-.834-2.9-1.196-4.756-4.148-4.896-4.335-.141-.188-1.168-1.55-1.168-2.955 0-1.405.733-2.096 1.011-2.392.278-.297.604-.372.805-.372.2 0 .401.003.576.012.188.009.438-.073.687.525.263.633.916 2.235 1 2.423.083.188.139.407.014.656-.126.249-.189.407-.375.633-.186.225-.395.49-.56.633-.186.164-.383.344-.173.705.21.362.936 1.549 2.015 2.511 1.396 1.246 2.564 1.636 2.923 1.782.358.146.568.125.782-.125.214-.25 1.012-1.18 1.283-1.587.271-.408.542-.34.869-.216.326.124 2.062.973 2.417 1.15.355.176.592.264.678.414.086.15.086.867-.19 1.642z"/></svg>
                                        Call To Book
                                    </button>
                                    <button class="w-full bg-white border border-stone-200 text-black px-6 py-4 text-xs font-bold uppercase tracking-widest hover:bg-stone-50 transition flex items-center justify-center gap-2" onclick="window.open('https://wa.me/440000000000')">
                                        <svg class="w-4 h-4 text-[#25D366]" fill="currentColor" viewBox="0 0 24 24"><path d="M12.031 0C5.385 0 0 5.385 0 12.031c0 2.133.551 4.156 1.558 5.96L.101 24l6.195-1.621c1.729.897 3.666 1.365 5.735 1.365 6.646 0 12.031-5.385 12.031-12.031S18.677 0 12.031 0zM17.65 16.59c-.276.776-1.593 1.488-2.186 1.547-.56.055-1.282.164-3.693-.834-2.9-1.196-4.756-4.148-4.896-4.335-.141-.188-1.168-1.55-1.168-2.955 0-1.405.733-2.096 1.011-2.392.278-.297.604-.372.805-.372.2 0 .401.003.576.012.188.009.438-.073.687.525.263.633.916 2.235 1 2.423.083.188.139.407.014.656-.126.249-.189.407-.375.633-.186.225-.395.49-.56.633-.186.164-.383.344-.173.705.21.362.936 1.549 2.015 2.511 1.396 1.246 2.564 1.636 2.923 1.782.358.146.568.125.782-.125.214-.25 1.012-1.18 1.283-1.587.271-.408.542-.34.869-.216.326.124 2.062.973 2.417 1.15.355.176.592.264.678.414.086.15.086.867-.19 1.642z"/></svg>
                                        WhatsApp Enquiry
                                    </button>
                                </div>

                                <!-- FAQs -->
                                <div class="bg-stone-50 border border-stone-200 p-8 rounded-sm">
                                    <h3 class="serif text-2xl mb-6">Service FAQs</h3>
                                    <div class="border-t border-gray-200">
                                        ${data.faq.map((f, idx) => `
                                            <div class="faq-item border-b border-gray-200 last:border-0">
                                                <div class="faq-trigger py-4 flex justify-between items-center cursor-pointer text-sm font-bold text-gray-800" onclick="toggleFaq(this)">
                                                    <span>${f.q}</span>
                                                    <span class="faq-icon text-xl text-gray-400 font-light">+</span>
                                                </div>
                                                <div class="faq-content overflow-hidden max-h-0 transition-all duration-300">
                                                    <div class="pb-4 text-sm text-gray-600 leading-relaxed">${f.a}</div>
                                                </div>
                                            </div>
                                        `).join('')}
                                    </div>
                                </div>

                                <!-- Trust Info -->
                                <div class="bg-stone-50 border border-stone-200 p-8 rounded-sm flex items-start gap-4">
                                    <svg class="w-8 h-8 text-amber-500 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
                                    <div>
                                        <h4 class="font-bold text-sm mb-1">Serving Mortlake, Richmond</h4>
                                        <p class="text-xs text-gray-500">Premium clinical sanctuary located in the heart of London.</p>
                                    </div>
                                </div>

                                <div class="bg-stone-50 border border-stone-200 p-8 rounded-sm flex items-start gap-4">
                                    <svg class="w-8 h-8 text-amber-500 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                                    <div>
                                        <h4 class="font-bold text-sm mb-1">Professional Excellence</h4>
                                        <p class="text-xs text-gray-500">Trusted care. Real results. Your wellbeing is our priority.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- BOTTOM CTA FULL WIDTH -->
                    <div class="bg-stone-100 py-16">
                        <div class="max-w-7xl mx-auto px-6 flex flex-col md:flex-row items-center justify-between gap-8">
                            <div class="flex items-center gap-6">
                                <div class="w-16 h-16 rounded-full bg-white flex items-center justify-center shrink-0 border border-stone-200">
                                    <svg class="w-8 h-8 text-amber-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"></path></svg>
                                </div>
                                <div>
                                    <h3 class="serif text-2xl mb-1">Your Body Deserves Expert Care</h3>
                                    <p class="text-sm text-gray-600">Book your ${data.title.toLowerCase()} in Mortlake, Richmond today.</p>
                                </div>
                            </div>
                            <div class="flex flex-col sm:flex-row gap-4 shrink-0 w-full md:w-auto">
                                <button class="bg-black text-white px-8 py-4 text-xs font-bold uppercase tracking-widest hover:bg-gray-800 transition" onclick="window.open('https://fresha.com')">Book Now</button>
                                <button class="bg-[#25D366] text-white px-8 py-4 text-xs font-bold uppercase tracking-widest hover:bg-[#128C7E] transition flex items-center justify-center gap-2" onclick="window.open('https://wa.me/440000000000')">
                                    <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M12.031 0C5.385 0 0 5.385 0 12.031c0 2.133.551 4.156 1.558 5.96L.101 24l6.195-1.621c1.729.897 3.666 1.365 5.735 1.365 6.646 0 12.031-5.385 12.031-12.031S18.677 0 12.031 0zM17.65 16.59c-.276.776-1.593 1.488-2.186 1.547-.56.055-1.282.164-3.693-.834-2.9-1.196-4.756-4.148-4.896-4.335-.141-.188-1.168-1.55-1.168-2.955 0-1.405.733-2.096 1.011-2.392.278-.297.604-.372.805-.372.2 0 .401.003.576.012.188.009.438-.073.687.525.263.633.916 2.235 1 2.423.083.188.139.407.014.656-.126.249-.189.407-.375.633-.186.225-.395.49-.56.633-.186.164-.383.344-.173.705.21.362.936 1.549 2.015 2.511 1.396 1.246 2.564 1.636 2.923 1.782.358.146.568.125.782-.125.214-.25 1.012-1.18 1.283-1.587.271-.408.542-.34.869-.216.326.124 2.062.973 2.417 1.15.355.176.592.264.678.414.086.15.086.867-.19 1.642z"/></svg>
                                    Call To Book
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            `;
            container.innerHTML = html;"""

pattern = r"const data = contentData\[id\];.*?container\.innerHTML = html;"
content = re.sub(pattern, new_template, content, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Template updated successfully.")
