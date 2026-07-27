project('capivara-fetch',
  version: '0.1.0',
  meson_version: '>= 0.62.0',
)

python = import('python').find_installation('python3')
i18n = import('i18n')
python_dir = python.get_install_dir()
datadir = get_option('prefix') / get_option('datadir')

# Python package.
install_subdir('src/capivara_fetch',
  install_dir: python_dir,
  exclude_directories: ['__pycache__'],
)

# Executable launcher.
conf = configuration_data()
conf.set('PYTHON_DIR', python_dir)
configure_file(
  input: 'capivara-fetch.in',
  output: 'capivara-fetch',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir'),
  install_mode: 'rwxr-xr-x',
)

# Desktop entry and AppStream metainfo: translatable keys/elements are merged
# from the po/ catalogs (gettext ITS rules handle .desktop and .metainfo.xml).
i18n.merge_file(
  input: 'data/org.capivaraos.Fetch.desktop.in',
  output: 'org.capivaraos.Fetch.desktop',
  type: 'desktop',
  po_dir: 'po',
  install: true,
  install_dir: datadir / 'applications',
)
i18n.merge_file(
  input: 'data/org.capivaraos.Fetch.metainfo.xml.in',
  output: 'org.capivaraos.Fetch.metainfo.xml',
  type: 'xml',
  po_dir: 'po',
  install: true,
  install_dir: datadir / 'metainfo',
)
# App icon: the capybara logo, shipped as PNG at several hicolor sizes.
foreach size : ['64', '128', '256', '512']
  install_data(
    'data/icons/hicolor' / size + 'x' + size / 'apps/org.capivaraos.Fetch.png',
    install_dir: datadir / 'icons/hicolor' / size + 'x' + size / 'apps',
  )
endforeach

# Capybara head bundled for the shareable card and the CapivaraOS page.
install_data('data/capybara-head.png',
  install_dir: datadir / 'org.capivaraos.Fetch',
)

# Translations (compiles po/<lang>.po -> share/locale/<lang>/.../<domain>.mo).
subdir('po')
