#!/usr/bin/env python3
import os
import subprocess
import locale
import gettext

# Configurar gettext
LOCALE_PATH = '/usr/share/locale'
gettext.bindtextdomain('biglinux-game-ready', LOCALE_PATH)
gettext.textdomain('biglinux-game-ready')
_ = gettext.gettext

def check_gpu():
    try:
        if 'AMD' in subprocess.getoutput('lspci') and 'VGA' in subprocess.getoutput('lspci'):
            return 'amd'
        if 'NVIDIA' in subprocess.getoutput('lspci') and 'VGA' in subprocess.getoutput('lspci'):
            return 'nvidia'
        return 'unknown'
    except Exception as e:
        print(f"Error detecting GPU: {e}")
        return 'unknown'

def main():
    # Detectar GPU
    gpu_type = check_gpu()
    print(_("GPU detected: {}").format(gpu_type))

    # Mostrar instruções
    print(_("\nIMPORTANT: Please follow these instructions:"))
    for instruction in [
        _("1. Login to your Steam account when the window opens"),
        _("2. After logging in, go to:"),
        _("   Steam menu -> Settings -> Compatibility"),
        _("3. Check 'Enable Steam Play for all other titles'"),
        _("4. Click OK to save settings"),
        _("5. Change language if desired, this setting is in Settings -> Interface"),
        _("6. Restart Steam and enjoy gaming!")
    ]:
        print(instruction)

    # Iniciar Steam
    subprocess.Popen(['steam'])

    print(_("\nSetup complete!"))
    print(_("To show/hide performance monitor during game: Shift_R + F12"))

if __name__ == "__main__":
    main()