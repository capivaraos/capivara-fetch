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

# Desktop entry, AppStream metainfo, icon.
# NOTE: the .in suffix is a placeholder for future gettext translation merge;
# for now the files are installed verbatim.
install_data('data/org.capivaraos.Fetch.desktop.in',
  rename: 'org.capivaraos.Fetch.desktop',
  install_dir: datadir / 'applications',
)
install_data('data/org.capivaraos.Fetch.metainfo.xml.in',
  rename: 'org.capivaraos.Fetch.metainfo.xml',
  install_dir: datadir / 'metainfo',
)
install_data('data/icons/hicolor/scalable/apps/org.capivaraos.Fetch.svg',
  install_dir: datadir / 'icons/hicolor/scalable/apps',
)
install_data('data/icons/hicolor/256x256/apps/org.capivaraos.Fetch.png',
  install_dir: datadir / 'icons/hicolor/256x256/apps',
)

# Capybara head bundled for the shareable card and the CapivaraOS page.
install_data('data/capybara-head.png',
  install_dir: datadir / 'org.capivaraos.Fetch',
)

# Translations (compiles po/<lang>.po -> share/locale/<lang>/.../<domain>.mo).
subdir('po')
