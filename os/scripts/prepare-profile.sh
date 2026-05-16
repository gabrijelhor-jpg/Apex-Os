#!/usr/bin/env bash
# Kopira boot loader datoteke iz Arch releng profila (potrebno jednom prije prvog builda)
set -euo pipefail

RELENG="/usr/share/archiso/configs/releng"
DEST="$(cd "$(dirname "${BASH_SOURCE[0]}")/../archiso/apexos" && pwd)"

if [[ ! -d "$RELENG" ]]; then
  echo "Instaliraj archiso: sudo pacman -S archiso"
  exit 1
fi

for item in grub syslinux efiboot; do
  if [[ -e "$RELENG/$item" ]]; then
    cp -a "$RELENG/$item" "$DEST/"
    echo "Kopirano: $item"
  fi
done

echo "Profil spreman u $DEST"
