import re
import os
import json

SCREEN_FILES = {
    "splash": "screens/c2d5a0b52ea542479cf133612178b6b1.html",
    "login": "screens/bcee21f01c7545498925487cfbbe29ef.html",
    "home": "screens/f82feb95a093494bbe7b17627f194fe1.html",
    "restaurants": "screens/e43d18ba778449e58cb3d7f7c4bdac31.html",
    "food_detail": "screens/2d73da933a80458da46a5239602b72de.html",
    "cart": "screens/ed6b8b841db74cd1b5fcb372dcd7d5a2.html",
    "checkout": "screens/c70efdba228240c882aa02151e6e63f8.html",
    "order_tracking": "screens/d078a4cc1a814f94b87f2f3bd01fb82e.html",
    "profile": "screens/ad0c7ae2055f4b87b769bbb1aae7005e.html",
}

PAGE_NAMES = {
    "splash": "splash.html",
    "login": "login.html",
    "home": "home.html",
    "restaurants": "restaurants.html",
    "food_detail": "food-detail.html",
    "cart": "cart.html",
    "checkout": "checkout.html",
    "order_tracking": "order-tracking.html",
    "profile": "profile.html",
}

def get_top_nav(active_key):
    links = [
        ("home", "Home", "index.html", "home"),
        ("restaurants", "Explore", "restaurants.html", "storefront"),
        ("food_detail", "Dish Detail", "food-detail.html", "lunch_dining"),
        ("cart", "Cart (2)", "cart.html", "shopping_cart"),
        ("checkout", "Checkout", "checkout.html", "credit_card"),
        ("order_tracking", "Live Tracking", "order-tracking.html", "moped"),
        ("profile", "Profile", "profile.html", "person"),
        ("login", "Login", "login.html", "login"),
        ("splash", "Splash", "splash.html", "launch"),
    ]
    
    pills_html = []
    for key, label, href, icon in links:
        if key == active_key:
            cls = "px-3 py-1.5 rounded-full text-xs font-bold bg-[#b51c00] text-white shadow-sm flex items-center gap-1 shrink-0"
        else:
            cls = "px-3 py-1.5 rounded-full text-xs font-semibold text-slate-300 hover:text-white hover:bg-slate-800 transition-colors flex items-center gap-1 shrink-0"
        pills_html.append(f'<a href="{href}" class="{cls}"><span class="material-symbols-outlined text-[15px]">{icon}</span><span>{label}</span></a>')
    
    pills_joined = "\n".join(pills_html)
    
    return f"""
<!-- Antigravity Global Site Navigation Header (Zero Iframe, Direct Navigation) -->
<header class="sticky top-0 z-[100] w-full bg-[#111827] text-white border-b border-slate-800 shadow-md">
    <div class="max-w-4xl mx-auto px-4 h-14 flex items-center justify-between gap-3">
        <a href="index.html" class="flex items-center gap-2 shrink-0 font-extrabold text-sm text-white hover:opacity-90 transition-opacity">
            <span class="w-8 h-8 rounded-xl bg-[#b51c00] text-white flex items-center justify-center shadow-md">
                <span class="material-symbols-outlined text-lg" style="font-variation-settings: 'FILL' 1;">restaurant</span>
            </span>
            <span class="tracking-tight text-base font-bold hidden sm:inline">Foodie</span>
        </a>
        <nav class="flex items-center gap-1 overflow-x-auto no-scrollbar py-1">
            {pills_joined}
        </nav>
    </div>
</header>
<style>
.no-scrollbar::-webkit-scrollbar {{ display: none; }}
.no-scrollbar {{ -ms-overflow-style: none; scrollbar-width: none; }}
/* Versatile & responsive layout across Mobile, Tablet, and Desktop */
body > main {{
    max-width: 480px;
    margin-left: auto;
    margin-right: auto;
    box-shadow: 0 0 40px -10px rgba(0,0,0,0.12);
    min-height: calc(100vh - 56px);
    position: relative;
    background-color: #f8f9ff;
}}
@media (min-width: 768px) {{
    body {{
        background-color: #f1f5f9 !important;
    }}
    /* Align fixed bottom navigation and floating headers with the app container on desktop */
    .fixed.bottom-0 {{
        max-width: 480px !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
        right: auto !important;
    }}
    header.fixed {{
        max-width: 480px !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
        right: auto !important;
    }}
}}
</style>
"""

# Navigation link wiring script without any postMessage or reloads
NAV_LINKS_SCRIPT = """
<script>
document.addEventListener("DOMContentLoaded", function() {
    // Wire bottom navigation bar links to their direct pages
    document.querySelectorAll('[data-path="explore-feed"]').forEach(el => {
        el.setAttribute("href", "index.html");
    });
    document.querySelectorAll('[data-path="search-and-browse"]').forEach(el => {
        el.setAttribute("href", "restaurants.html");
    });
    document.querySelectorAll('[data-path="cart-summary"]').forEach(el => {
        el.setAttribute("href", "cart.html");
    });
    document.querySelectorAll('[data-path="account-profile"]').forEach(el => {
        el.setAttribute("href", "profile.html");
    });
});
</script>
"""

def process_splash(html):
    html = html.replace('id="getStartedBtn" type="button"', 'id="getStartedBtn" type="button" onclick="window.location.href=\'login.html\'"')
    html = re.sub(r'(<button[^>]*>\s*<span>Already have an account\?</span>\s*<span[^>]*>Log In</span>\s*</button>)',
                  r'<a href="login.html" class="w-full py-3.5 text-center font-label-lg text-label-lg text-on-surface-variant hover:text-on-surface transition-colors flex items-center justify-center gap-1.5"><span>Already have an account?</span><span class="text-primary-container font-bold hover:underline">Log In</span></a>',
                  html)
    html = re.sub(r'<button class="font-label-md text-label-md text-on-surface-variant hover:text-primary transition-colors px-3 py-1.5 rounded-full hover:bg-surface-container" type="button">\s*Skip\s*</button>',
                  r'<a href="index.html" class="font-label-md text-label-md text-on-surface-variant hover:text-primary transition-colors px-3 py-1.5 rounded-full hover:bg-surface-container">Skip</a>',
                  html)
    return html

def process_login(html):
    html = re.sub(r'<button([^>]*?)id="submitAuthBtn"([^>]*)>', r'<button\1id="submitAuthBtn"\2 onclick="window.location.href=\'index.html\'">', html)
    html = html.replace('onclick="socialAuth(\'Google\')"', 'onclick="window.location.href=\'index.html\'"')
    html = html.replace('onclick="socialAuth(\'Apple\')"', 'onclick="window.location.href=\'index.html\'"')
    html = html.replace('onclick="guestLogin()"', 'onclick="window.location.href=\'index.html\'"')
    return html

def process_home(html):
    html = html.replace('href="#"', 'href="javascript:void(0)"')
    html = re.sub(r'(<h[34][^>]*>.*?(?:Burger|Dumpling|Pizza|Taco|Ramen).*?</h[34]>)',
                  r'<a href="food-detail.html" class="hover:underline hover:text-primary">\1</a>',
                  html, flags=re.IGNORECASE)
    html = re.sub(r'(<span>\s*View All\s*</span>|<span>\s*See All\s*</span>)',
                  r'<a href="restaurants.html" class="text-primary font-bold hover:underline">\1</a>',
                  html, flags=re.IGNORECASE)
    html = re.sub(r'(<div class="relative">\s*<img alt="Profile"[^>]*>\s*</div>)',
                  r'<a href="profile.html" class="block cursor-pointer hover:opacity-80 transition-opacity">\1</a>',
                  html)
    return html

def process_restaurants(html):
    html = re.sub(r'<button aria-label="Go Back"([^>]*)>', r'<a href="index.html" aria-label="Go Back"\1>', html)
    html = html.replace('</button><img alt="Foodie Brand Logo"', '</a><img alt="Foodie Brand Logo"')
    html = re.sub(r'(<div class="bg-surface-container-lowest rounded-2xl[^"]*">)',
                  r'\1<a href="food-detail.html" class="absolute inset-0 z-10" aria-label="View restaurant menu"></a>',
                  html)
    return html

def process_food_detail(html):
    html = html.replace("onclick=\"history.back()\"", "onclick=\"window.location.href='index.html'\"")
    script_inject = """
    <div id="cartToast" class="fixed top-20 left-1/2 -translate-x-1/2 z-50 hidden bg-[#006947] text-white px-5 py-3 rounded-2xl shadow-xl flex items-center gap-3 transition-all duration-300">
        <span class="material-symbols-outlined text-[22px]">check_circle</span>
        <span class="font-bold text-sm">Added to your cart!</span>
        <a href="cart.html" class="ml-2 px-3 py-1 bg-white text-[#006947] rounded-lg text-xs font-extrabold hover:bg-slate-100 uppercase tracking-wide">View Cart</a>
    </div>
    <script>
    document.addEventListener("DOMContentLoaded", function() {
        const addBtn = document.querySelector('button[aria-label*="cart" i]') || document.querySelector('button.bg-primary, button.bg-primary-container');
        if (addBtn) {
            addBtn.addEventListener('click', function(e) {
                const toast = document.getElementById('cartToast');
                if (toast) {
                    toast.classList.remove('hidden');
                    setTimeout(() => {
                        window.location.href = 'cart.html';
                    }, 800);
                }
            });
        }
    });
    </script>
    """
    html = html.replace('</body>', script_inject + '</body>')
    return html

def process_cart(html):
    html = re.sub(r'<button aria-label="Go Back"([^>]*)>', r'<a href="index.html" aria-label="Go Back"\1>', html)
    html = html.replace('</button>\n<div class="flex flex-col">\n<h1 class="font-headline-md', '</a>\n<div class="flex flex-col">\n<h1 class="font-headline-md')
    html = re.sub(r'(<button class="[^"]*bg-primary[^"]*"[^>]*>.*?Proceed to Checkout.*?</button>)',
                  r'<a href="checkout.html" class="w-full">\1</a>',
                  html, flags=re.DOTALL)
    html = html.replace('onclick="proceedToCheckout()"', 'onclick="window.location.href=\'checkout.html\'"')
    return html

def process_checkout(html):
    html = html.replace("onclick=\"history.back()\"", "onclick=\"window.location.href='cart.html'\"")
    html = html.replace('onclick="closeOrderModal()"', 'onclick="window.location.href=\'order-tracking.html\'"')
    return html

def process_order_tracking(html):
    html = html.replace("onclick=\"history.back()\"", "onclick=\"window.location.href='index.html'\"")
    home_btn = """
    <div class="fixed bottom-4 left-4 right-4 z-40 max-w-md mx-auto">
        <a href="index.html" class="w-full h-14 bg-surface-container-lowest/95 backdrop-blur-xl border border-primary/20 text-[#b51c00] hover:bg-[#b51c00] hover:text-white rounded-full flex items-center justify-center gap-2 font-headline-sm text-headline-sm font-bold shadow-lg transition-all active:scale-95">
            <span class="material-symbols-outlined text-[20px]">home</span>
            <span>Return to Home</span>
        </a>
    </div>
    """
    html = html.replace('</body>', home_btn + '</body>')
    return html

def process_profile(html):
    html = html.replace("onclick=\"history.back()\"", "onclick=\"window.location.href='index.html'\"")
    html = re.sub(r'(<span>\s*Order History\s*</span>|<span>\s*Past Orders\s*</span>)',
                  r'<a href="order-tracking.html" class="hover:text-primary">\1</a>',
                  html, flags=re.IGNORECASE)
    html = re.sub(r'(<span>\s*Log Out\s*</span>|<span>\s*Sign Out\s*</span>)',
                  r'<a href="login.html" class="text-error font-bold">\1</a>',
                  html, flags=re.IGNORECASE)
    return html

def main():
    processors = {
        "splash": process_splash,
        "login": process_login,
        "home": process_home,
        "restaurants": process_restaurants,
        "food_detail": process_food_detail,
        "cart": process_cart,
        "checkout": process_checkout,
        "order_tracking": process_order_tracking,
        "profile": process_profile,
    }

    print("Generating clean, standalone, zero-blinking pages...")
    for key, path in SCREEN_FILES.items():
        out_name = PAGE_NAMES[key]
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # Run page processor
        proc = processors.get(key)
        if proc:
            content = proc(content)

        # Inject top navigation bar right after <body ...>
        top_nav = get_top_nav(key)
        content = re.sub(r'(<body[^>]*>)', r'\1' + top_nav, content, count=1)

        # Inject standard nav link wiring (NO postMessage!)
        content = content.replace("</body>", NAV_LINKS_SCRIPT + "</body>")

        with open(out_name, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [OK] Generated {out_name}")

    # Set index.html directly to home.html content!
    with open("home.html", "r", encoding="utf-8") as f:
        home_content = f.read()
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(home_content)
    print("  [OK] Generated index.html (Direct Home Page, NO IFRAMES)")

if __name__ == "__main__":
    main()

