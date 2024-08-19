from PyInstaller.utils.hooks import collect_submodules, collect_data_files

hiddenimports = collect_submodules('docx') + collect_submodules('pandas')
datas = collect_data_files('docx') + collect_data_files('pandas')
