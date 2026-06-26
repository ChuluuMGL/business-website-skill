# SEO And GEO Readiness

Use this reference when building public, client-preview, SEO-sensitive, or AI-search/GEO-sensitive business websites.

## Principle

Treat GEO as disciplined SEO for AI-mediated discovery. Do not add hidden text, fake FAQs, fake citations, or special "AI schema" that is not backed by visible page content. Make the business easy to crawl, quote, summarize, and trust.

## Required For Public Launch

- Each indexable page has one clear `<title>` and one useful meta description.
- The HTML document has a correct `lang` attribute.
- Main content is available as crawlable text, not only canvas, image, animation, or client-only state.
- The page has one primary `h1`, descriptive section headings, and meaningful internal links.
- Canonical URLs are present after the final domain/path is known.
- Open Graph and Twitter Card metadata match the visible title, description, URL, and preview image.
- Images that communicate information have meaningful `alt`; decorative images have empty `alt`.
- Public launch pages are not blocked by `noindex`, restrictive `robots.txt`, login walls, or blocked CSS/JS.
- Multi-page sites include a sitemap or clear sitemap generation plan.

## Structured Data

Use JSON-LD only when it matches visible content.

- Company/corporate site: `Organization` and `WebSite`.
- Local or venue-based business: `LocalBusiness` only with confirmed address, phone, hours, and geo facts.
- Product/software site: `Product`, `SoftwareApplication`, or `WebApplication` only when the visible page supports those claims.
- Multi-page site: `BreadcrumbList` when breadcrumbs or page hierarchy are visible.
- FAQ schema: only when real visible FAQs exist.

Never add ratings, reviews, customers, awards, prices, addresses, or service areas unless they come from source materials.

## GEO-Friendly Content

- First screen states audience, problem, offer, proof, and action in direct text.
- Include concise summary blocks that answer: who, what, for whom, where, proof, process, and next step.
- Keep evidence close to claims: metrics, certifications, case names, reports, screenshots, or source labels.
- Use specific section headings that work as standalone answers.
- Provide comparison, process, FAQ, and proof-library modules when they reflect real buyer questions.
- Keep important content visible in the DOM before heavy animation or tabs.
- Do not create many near-duplicate pages only to target query variants.

## Preview And Staging Controls

- For private previews, use `noindex` or hosting-level access control.
- Before public handoff, remove `noindex` and verify the canonical domain.
- To limit snippets or AI-feature excerpts, use standard controls such as `nosnippet`, `data-nosnippet`, `max-snippet`, or `noindex` only when the user explicitly requests that behavior.
- Do not block CSS, JS, or images required to understand the page.

## Handoff Notes

Report:

- indexability status: public/indexable or private/noindex
- canonical URL status
- sitemap/robots status
- structured data types used and source basis
- unresolved SEO/GEO fields such as final domain, preview image, legal name, address, or contact details
