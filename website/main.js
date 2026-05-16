(function () {
  const DEFAULT_CONFIG = {
    version: "1.0",
    url: "",
    filename: "apexos-1.0-x86_64.iso",
    sha256: "",
    note:
      "ISO još nije objavljen na serveru. Prvo izgradi ISO (vidi upute) ili postavi URL u download.json.",
  };

  function readInlineConfig() {
    const el = document.getElementById("apex-download-config");
    if (!el) return null;
    try {
      return JSON.parse(el.textContent);
    } catch {
      return null;
    }
  }

  async function loadConfig() {
    const inline = readInlineConfig();
    if (location.protocol === "file:") {
      return inline || DEFAULT_CONFIG;
    }
    try {
      const res = await fetch("download.json", { cache: "no-store" });
      if (!res.ok) return inline || DEFAULT_CONFIG;
      const remote = await res.json();
      return { ...DEFAULT_CONFIG, ...inline, ...remote };
    } catch {
      return inline || DEFAULT_CONFIG;
    }
  }

  function ensureModal() {
    let modal = document.getElementById("download-modal");
    if (modal) return modal;

    modal = document.createElement("div");
    modal.id = "download-modal";
    modal.className = "modal";
    modal.hidden = true;
    modal.innerHTML = `
      <div class="modal-backdrop" data-close></div>
      <div class="modal-panel" role="dialog" aria-labelledby="modal-title">
        <h3 id="modal-title">ISO još nije dostupan za preuzimanje</h3>
        <p id="modal-body"></p>
        <div class="modal-actions">
          <a class="btn btn-primary" href="iso.html">Nema Build Apex ISO? Pomoc</a>
          <a class="btn btn-ghost" href="instalacija.html">Instalacija na laptop</a>
          <button type="button" class="btn btn-ghost" data-close>Zatvori</button>
        </div>
      </div>
    `;
    document.body.appendChild(modal);

    modal.querySelectorAll("[data-close]").forEach((el) => {
      el.addEventListener("click", () => {
        modal.hidden = true;
      });
    });
    return modal;
  }

  function showUnavailableModal(config) {
    const modal = ensureModal();
    const body = modal.querySelector("#modal-body");
    body.textContent = config.note || DEFAULT_CONFIG.note;
    modal.hidden = false;
  }

  function applyConfig(config) {
    const link = document.getElementById("iso-link");
    const note = document.getElementById("iso-note");
    const version = document.getElementById("version-label");
    const heroBtn = document.getElementById("hero-download");

    if (version && config.version) {
      version.textContent = `Apex OS ${config.version} — x86_64 (većina laptopa)`;
    }

    const hasUrl = Boolean(config.url && config.url.trim());

    if (note) {
      if (config.sha256) {
        note.textContent = `SHA-256: ${config.sha256}`;
      } else if (hasUrl) {
        note.textContent = "Klikni gumb za preuzimanje ISO datoteke.";
      } else {
        note.textContent = config.note || DEFAULT_CONFIG.note;
      }
    }

    function bindDownloadButton(btn) {
      if (!btn) return;
      btn.addEventListener("click", (e) => {
        if (hasUrl) {
          return;
        }
        e.preventDefault();
        showUnavailableModal(config);
      });
      if (hasUrl) {
        btn.href = config.url;
        if (config.filename) btn.setAttribute("download", config.filename);
        btn.removeAttribute("aria-disabled");
        btn.classList.remove("btn-disabled");
      } else {
        btn.href = "#download";
        btn.setAttribute("aria-disabled", "true");
        btn.classList.add("btn-disabled");
      }
    }

    bindDownloadButton(link);
    bindDownloadButton(heroBtn);

    if (hasUrl && link) {
      link.href = config.url;
      if (config.filename) link.setAttribute("download", config.filename);
      link.classList.remove("btn-disabled");
      link.removeAttribute("aria-disabled");
    }
  }

  loadConfig().then(applyConfig);
})();
