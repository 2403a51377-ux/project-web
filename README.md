# 🍔 Foodie Delivery Web App

A complete, pixel-perfect, and **Vercel-ready** web application built from the **Google Stitch** UI/UX design tokens.

---

## ⚡ Vercel Compatibility & Clean URLs

The project includes configuration for instant zero-configuration deployment to [Vercel](https://vercel.com):

- **[`vercel.json`](file:///C:/Users/nikhi/Downloads/food_web/vercel.json)**:
  - `cleanUrls: true` (removes `.html` extension from URLs)
  - Security headers (`X-Content-Type-Options`, `X-Frame-Options`, `X-XSS-Protection`)
  - Long-term caching headers for static assets
  - Clean URL rewrites
- **[`package.json`](file:///C:/Users/nikhi/Downloads/food_web/package.json)**: Standard static build and serve scripts.
- **[`.vercelignore`](file:///C:/Users/nikhi/Downloads/food_web/.vercelignore)**: Keeps deployments fast and lean by excluding build scripts and raw data.

### URL Structure on Vercel:
| Route | Page | Description |
| :--- | :--- | :--- |
| `/` | `index.html` | Home explore feed & trending food |
| `/restaurants` | `restaurants.html` | Restaurant directory & filters |
| `/food-detail` | `food-detail.html` | Dish details & cart addition |
| `/cart` | `cart.html` | Shopping cart & pricing summary |
| `/checkout` | `checkout.html` | Delivery address & payment options |
| `/order-tracking`| `order-tracking.html` | Live rider tracking on interactive map |
| `/profile` | `profile.html` | User account & order history |
| `/login` | `login.html` | Sign In / Sign Up tabs |
| `/splash` | `splash.html` | Brand splash & onboarding |

---

## 🚀 How to Deploy to Vercel

### Method 1: Using Vercel CLI (Fastest)
From this directory (`c:\Users\nikhi\Downloads\food_web`), run:
```bash
npx vercel
```
Follow the interactive prompts to link and deploy your site in seconds.

For production deployment:
```bash
npx vercel --prod
```

### Method 2: Git / GitHub
1. Initialize a git repo and push to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial Foodie delivery app"
   ```
2. Import the repository in [vercel.com/new](https://vercel.com/new). Vercel will automatically detect `vercel.json` and deploy it instantly.

---

## 📱 Cross-Device Versatility
- **Mobile First**: Fluid full-screen interface on all mobile devices (iOS Safari & Android Chrome).
- **Tablet & Desktop**: Beautiful centered container with drop shadows, responsive header navigation, and persistent bottom navigation bar.
- **No Iframes / No Flicker**: Direct, static DOM loading for instant transitions and zero blinking.
