#!/usr/bin/env bash
set -euo pipefail

SCRIPTS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPTS_DIR/../archiso" && pwd)"
PROFILE="apexos"

if ! command -v mkarchiso &>/dev/null; then
  echo "mkarchiso nije instaliran. Na Archu: sudo pacman -S archiso"
  exit 1
fi

if [[ "$(id -u)" -ne 0 ]]; then
  echo "Pokreni s root pravima: sudo $0"
  exit 1
fi

cd "$ROOT"

if [[ ! -d "$ROOT/$PROFILE/grub" ]]; then
  echo "Boot datoteke nedostaju — pokrećem prepare-profile.sh..."
  bash "$SCRIPTS_DIR/prepare-profile.sh"
fi

echo "Gradim Apex OS ISO (profil: $PROFILE)..."
mkarchiso -v -o "$ROOT/out" "$PROFILE"
echo ""
echo "Gotovo. ISO je u: $ROOT/out/"
