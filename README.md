# Capivara Fetch

A small, friendly **system-information viewer** for any Linux desktop — and a
brand ambassador for [CapivaraOS](https://capivaraos.org).

It shows your distro, kernel, desktop, CPU, GPU, memory and uptime in a clean
GTK4 / libadwaita window, exports a good-looking **card** you can share, and
has a **Live** dashboard with real-time gauges and charts (CPU incl. per-core,
memory, network and disk I/O, load average). It can also be **pinned to the
desktop** as a compact widget where the compositor supports it (KDE, Xfce,
wlroots). Every shared card carries the CapivaraOS branding — that's the point. 🐹

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
| `src/capivara_fetch/metrics.py` | Live `/proc` sampler (CPU, mem, net, disk, load) |
| `src/capivara_fetch/widgets.py` | Cairo gauge / sparkline / per-core bar widgets |
| `src/capivara_fetch/live.py` | The Live dashboard page (1s refresh) |
| `src/capivara_fetch/widget_window.py` | Compact "pin to desktop" widget (layer-shell + fallback) |
| `src/capivara_fetch/window.py` | libadwaita UI: System / Live / Share / CapivaraOS pages |
| `src/capivara_fetch/main.py` | `Adw.Application` entry point |
| `data/` | `.desktop`, AppStream metainfo, icon, bundled capybara head |
| `build-aux/flatpak/` | Flathub manifest (bundles gtk4-layer-shell) |

## Status / TODO

- [x] System info page + shareable card
- [x] Correct host distro detection inside the Flatpak sandbox
- [x] Capybara branding on the card and the CapivaraOS page
- [x] Toast overlay for "card saved" feedback
- [x] Live dashboard (gauges, per-core bars, network/disk/load sparklines)
- [x] "Pin to desktop" compact widget (layer-shell where supported, fallback elsewhere)
- [x] GPU probe works inside the Flatpak sandbox (GNOME runtime ships `lspci`)
- [x] Store screenshots in the AppStream metainfo
- [x] Scalable SVG app icon (capybara-face badge)
- [x] gettext with a `pt_BR` translation (English-first source)
- [ ] Translate the `.desktop`/metainfo strings too (currently UI-only)
- [ ] Verify the pinned-widget mode visually on a KDE/Xfce (Marsh/Pup) session
- [ ] Submit to Flathub; then package as RPM to preinstall on CapivaraOS spins

## License

App code: **GPL-3.0-or-later**. CapivaraOS brand assets (the capybara logo)
remain © 2026 CapivaraOS Project under their own brand license.
