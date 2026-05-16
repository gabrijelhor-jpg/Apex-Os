# Izgradnja Apex ISO-a

## Preduvjeti

- **Arch Linux** (fizički, VM ili WSL2 s Arch)
- ~20 GB slobodnog prostora
- Internet **samo tijekom builda** (preuzimanje paketa); gotovi ISO radi offline

## Koraci

```bash
sudo pacman -S --needed archiso mkinitcpio-archiso

cd /path/to/Apex/os/archiso
sudo mkarchiso -v apexos
```

Izlaz: `os/archiso/out/apexos-*.iso`

## Windows (WSL2)

1. Instaliraj WSL2 i [Arch WSL](https://wiki.archlinux.org/title Install_Arch_Linux_on_WSL) ili Ubuntu + Docker s Arch imageom.
2. Kloniraj repo u WSL datotečni sustav (`~/Apex`, ne `/mnt/c/...` — sporije).
3. Pokreni `os/scripts/build.sh`.

## Testiranje

- **QEMU:** `qemu-system-x86_64 -m 4096 -enable-kvm -cdrom out/apexos-*.iso`
- **Pravi laptop:** USB, UEFI boot, Secure Boot često mora biti isključen za custom ISO.

## Prilagodba paketa

Uredi `os/archiso/apexos/packages.x86_64` — lista aplikacija u live sustavu.
