#!/usr/bin/env bash
set -euo pipefail

systemctl enable sddm.service
systemctl enable NetworkManager.service
systemctl enable tlp.service

echo "hr_HR.UTF-8 UTF-8" >> /etc/locale.gen
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
locale-gen

chmod +x /usr/local/bin/apex-store \
         /usr/local/bin/apex-google \
         /usr/local/bin/apex-settings \
         /usr/local/bin/apex-update \
         /usr/local/bin/apex-audio-boost 2>/dev/null || true

if ! id liveuser &>/dev/null; then
  useradd -m -G wheel,audio,video,optical,storage,network liveuser
  echo "liveuser:apex" | chpasswd
  echo "liveuser ALL=(ALL) NOPASSWD:ALL" >/etc/sudoers.d/liveuser
  chmod 440 /etc/sudoers.d/liveuser
fi

setup_desktop_shortcuts() {
  local dir="$1"
  install -d -m 755 "$dir"
  for app in apex-explorer apex-settings apex-update apex-store google-chrome apex-install; do
    cp -f "/usr/share/applications/${app}.desktop" "$dir/" 2>/dev/null || true
  done
}

if [[ -d /usr/share/calamares/branding/default ]]; then
  cp -an /usr/share/calamares/branding/default/. /etc/calamares/branding/default/ 2>/dev/null || true
fi

install -d -m 755 /etc/skel/Desktop
setup_desktop_shortcuts /etc/skel/Desktop

cat >/etc/skel/Desktop/Welcome.txt <<'EOF'
Dobrodošli u Apex OS
====================
• Explorer — datoteke i mape
• Apex Postavke — zvuk (pojačavanje), sustav
• Apex Update — ažuriranja (treba internet)
• Apex Store — nove aplikacije
• Google — preglednik

Live: liveuser / lozinka: apex
EOF

if [[ -d /home/liveuser ]]; then
  setup_desktop_shortcuts /home/liveuser/Desktop
  cp /etc/skel/Desktop/Welcome.txt /home/liveuser/Desktop/ 2>/dev/null || true
  chown -R liveuser:liveuser /home/liveuser
fi

update-desktop-database /usr/share/applications 2>/dev/null || true
