#!/usr/bin/env bash
# shellcheck disable=SC2034

iso_name="apexos"
iso_label="APEXOS_$(date --date='@'"$SOURCE_DATE_EPOCH" +%Y%m)"
iso_publisher="Apex OS <https://github.com/apex-os>"
iso_application="Apex OS Live"
iso_version="$(date --date='@'"$SOURCE_DATE_EPOCH" +%Y.%m.%d)"
install_dir="arch"
buildmodes=('iso')
boot_modes=('uefi')
arch="x86_64"
pacman_conf="pacman.conf"
airootfs_image_type="squashfs"
airootfs_image_tool_options=('-comp' 'xz' '-Xbcj' 'x86' '-b' '1M' '-Xdict-size' '1M')
bootstrap_packages=('arch-install-scripts' 'mkinitcpio-archiso' 'mkinitcpio-nfs-utils' 'xz')
