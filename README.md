# benjaminmarklewis.com

A clean, single-scroll static portfolio for Benjamin Mark Lewis — inspired by the structure of Anne's Montessori Child Spaces site, but rebuilt for bioinformatics, multi-omic discovery, scientific software, publications, and career narrative.

## Local preview

```bash
./serve.sh
```

Open <http://localhost:8080>.

Use another port if needed:

```bash
PORT=8083 ./serve.sh
```

## Deploy to Raspberry Pi

First-time Pi setup:

```bash
ssh larry@larrys-pi4.local
sudo mkdir -p /var/www/benjaminmarklewis
sudo chown -R larry:www-data /var/www/benjaminmarklewis
sudo chmod -R 750 /var/www/benjaminmarklewis
```

Add `Caddyfile.benjaminmarklewis.example` to `/etc/caddy/Caddyfile`, validate, and reload:

```bash
sudo caddy validate --config /etc/caddy/Caddyfile
sudo systemctl reload caddy
```

Deploy from this repo:

```bash
./deploy-pi.sh
```

Dry run:

```bash
./deploy-pi.sh --dry-run
```

LAN preview after Caddy is configured:

```text
http://larrys-pi4.local:8083
```

## Structure

- `index.html` — single-scroll portfolio
- `styles.css` — responsive design system
- `assets/img/` — portrait and project images
- `404.html`, `robots.txt`, `sitemap.xml` — launch basics
- `deploy-pi.sh` — rsync deployment to Raspberry Pi
- `Caddyfile.benjaminmarklewis.example` — local preview + public domain blocks

## Notes

No build step is required. This is intentionally simpler than the previous Jekyll/al-folio site so it can be self-hosted exactly like the Montessori static site.

## Cloudflare Tunnel cutover plan

Current public `benjaminmarklewis.com` still uses GoDaddy nameservers and GitHub Pages:

- NS: `ns37.domaincontrol.com`, `ns38.domaincontrol.com`
- Apex A records: GitHub Pages `185.199.*.153`
- `www`: `gitbenlewis.github.io`

Prepared Pi state:

- Webroot: `/var/www/benjaminmarklewis`
- Local Caddy preview: `http://192.168.0.214:8083/` / `http://larrys-pi4.local:8083/`
- Cloudflare Tunnel ingress has been prepared to send:
  - `benjaminmarklewis.com` → `http://localhost:8083`
  - `www.benjaminmarklewis.com` → `http://localhost:8083`

Before changing GoDaddy nameservers:

1. Add `benjaminmarklewis.com` as a Cloudflare zone.
2. Let Cloudflare import current DNS records.
3. Preserve/inspect any verification or mail records.
4. Remove/replace only the web records when ready for cutover.
5. Route the tunnel DNS records after the Cloudflare zone exists:

```bash
cloudflared tunnel route dns montessorichildspaces benjaminmarklewis.com
cloudflared tunnel route dns --overwrite-dns montessorichildspaces www.benjaminmarklewis.com
```

Then switch GoDaddy nameservers to the two assigned Cloudflare nameservers and verify:

```bash
dig +short NS benjaminmarklewis.com @1.1.1.1
curl -I https://benjaminmarklewis.com
curl -I https://www.benjaminmarklewis.com
```

Rollback is to restore the old GoDaddy nameservers or restore the GitHub Pages A/CNAME records in Cloudflare.
