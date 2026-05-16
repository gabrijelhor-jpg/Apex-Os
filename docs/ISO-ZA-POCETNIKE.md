# ISO — objašnjenje za početnike

## Što je ISO? (jednostavno)

**ISO** je jedna velika datoteka koja **sadrži cijeli Apex OS** spreman za kopiranje na USB.

Zamisli je kao **DVD s filmom**, samo umjesto filma unutra je operativni sustav:

| Uobičajeni život | Apex OS |
|------------------|---------|
| Kupiš Windows na USB/DVD | Imaš `apexos-....iso` datoteku |
| Umetneš u laptop i instaliraš | Zapišeš ISO na USB → boot → instalacija |

Ekstenzija datoteke je npr. **`apexos-1.0-x86_64.iso`** (veličina često **3–5 GB**).

**Bez ISO datoteke ne možeš instalirati Apex na laptop** — to je „instalacijski medij”, kao što Windows ima svoj ISO.

---

## Zašto ga ti još nemaš?

Apex OS je **projekt koji se gradi** — ISO se ne skida gotov s Microsoft trgovine, nego se **jednom izgradi** (ručno ili preko interneta/GitHuba), pa se onda:

1. stavi na web za preuzimanje, ili  
2. koristi samo za sebe na USB-u.

Dok ISO ne postoji, gumb **Preuzmi** na stranici pokazuje poruku — to je normalno.

---

## Kako dobiti ISO? (3 načina)

### Način A — Najlakše na Windowsu: GitHub (preporuka)

Računalo u oblaku **izgradi ISO umjesto tebe**. Treba ti besplatni GitHub račun.

1. Registriraj se na [github.com](https://github.com)
2. Kreiraj novi repozitorij (npr. `apex-os`)
3. Uploadaj cijelu mapu `Apex` s Desktopa (ili koristi GitHub Desktop)
4. Na GitHubu: **Actions** → workflow **Build Apex ISO** → **Run workflow**
5. Pričekaj 30–90 minuta (prvi put može duže)
6. U istom runu: **Artifacts** → preuzmi `apexos-iso` — unutra je `.iso` datoteka

Detaljnije korake vidi u [GITHUB-ISO.md](GITHUB-ISO.md).

---

### Način B — Na svom PC-u (WSL / Linux)

Za naprednije. Treba **Arch Linux** okruženje (npr. WSL2 s Archom), ~20 GB prostora, internet tijekom gradnje.

Kratko:

```bash
sudo pacman -S archiso
cd Apex/os/scripts
sudo bash prepare-profile.sh
sudo bash build.sh
```

ISO izlazi u: `Apex/os/archiso/out/`

Puno detalja: [BUILD.md](BUILD.md)

---

### Način C — Netko drugi ti pošalje ISO

Ako prijatelj ili developer već izgradi ISO, može ti dati datoteku na USB ili WeTransfer. Provjeri da datoteka završava na **`.iso`**.

---

## Što napraviti KAD imaš ISO?

1. Preuzmi **`apexos-....iso`** na Windows
2. Instaliraj [Rufus](https://rufus.ie)
3. U Rufusu: odaberi ISO → odaberi USB (8 GB+) → START
4. Slijedi [INSTALACIJA-HR.md](INSTALACIJA-HR.md) za boot i instalaciju na laptop

---

## Česta pitanja

**Mogu li Apex instalirati bez ISO-a?**  
Ne na pravi način. Moras imati ISO (ili netko mora napraviti USB za tebe).

**Je li ISO virus?**  
Ne — to je slika diska. Windows Defender ponekad pita pri pisanju na USB; to je normalno za Linux ISO.

**Koliko traje gradnja?**  
GitHub Actions: ~30–90 min. Na slabijem PC-u i duže.

**Trebam li internet nakon instalacije Apex-a?**  
Ne za osnovni rad. Internet treba za preuzimanje ISO-a i za **Apex Store** (nove aplikacije).
