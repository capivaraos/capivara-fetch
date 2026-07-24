# Capivara Fetch

A small, friendly **system-information viewer** for any Linux desktop — and a
brand ambassador for [CapivaraOS](https://capivaraos.org).

It shows your distro, kernel, desktop, CPU, GPU, memory and uptime in a clean
GTK4 / libadwaita window, and exports a good-looking **card** you can share.
Every shared card carries the CapivaraOS branding — that's the point. 🐹

> Built with GTK4 + libadwaita (Python). English-first; `pt_BR` translation
> planned. Ships preinstalled on upcoming CapivaraOS releases.

## Run from source (development)

No build step needed — the GNOME runtime provides GTK4, libadwaita and pycairo:

```bash
python3 run.py
```

Requirements: `python3-gobject`, `gtk4`, `libadwaita`, `python3-cairo`
(on Fedora: `sudo dnf install python3-gobject gtk4 libadwaita`).

## Build & install (meson)

```bash
meson setup builddir
meson install -C builddir
capivara-fetch
```

## Build as Flatpak

```bash
flatpak-builder --user --install --force-clean \
    build-dir build-aux/flatpak/org.capivaraos.Fetch.yml
flatpak run org.capivaraos.Fetch
```

## Project layout

| Path | What |
|------|------|
| `src/capivara_fetch/sysinfo.py` | Collects system facts (best-effort, never crashes) |
| `src/capivara_fetch/card.py` | Renders the shareable Cairo card |
| `src/capivara_fetch/window.py` | libadwaita UI: System / Share / CapivaraOS pages |
| `src/capivara_fetch/main.py` | `Adw.Application` entry point |
| `data/` | `.desktop`, AppStream metainfo, icon |
| `build-aux/flatpak/` | Flathub manifest |

## Status / TODO

- [x] System info page + shareable card (working prototype)
- [ ] Add store screenshots to the AppStream metainfo (required by Flathub)
- [ ] Wire gettext for `pt_BR` (strings already English-first)
- [ ] Replace placeholder icon with the final scalable SVG
- [ ] GPU probe that works fully inside the Flatpak sandbox
- [ ] Toast overlay for "card saved" feedback

## License

App code: **GPL-3.0-or-later**. CapivaraOS brand assets (the capybara logo)
remain © 2026 CapivaraOS Project under their own brand license.
