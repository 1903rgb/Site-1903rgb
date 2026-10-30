(() => {
  "use strict";
  const $ = (id) => document.getElementById(id);

  // Menu mobile
  const burger = $("burger"), menu = $("menu");
  const closeMenu = () => { menu.classList.remove("open"); burger.setAttribute("aria-expanded", "false"); };
  burger.addEventListener("click", () => { const o = menu.classList.toggle("open"); burger.setAttribute("aria-expanded", String(o)); });
  menu.querySelectorAll("a").forEach((a) => a.addEventListener("click", closeMenu));
  document.addEventListener("keydown", (e) => { if (e.key === "Escape" && menu.classList.contains("open")) { closeMenu(); burger.focus(); } });

  // Mur de maquettes : pause
  const wall = $("wall"), wt = $("wall-toggle");
  wt.addEventListener("click", () => { const p = wall.classList.toggle("paused"); wt.setAttribute("aria-pressed", String(p)); wt.textContent = p ? "Lecture" : "Pause"; });

  // Filtres et « voir tout » sur mobile
  const grid = $("grid"), btns = [...document.querySelectorAll(".filters button")], cards = [...grid.querySelectorAll(".card")];
  btns.forEach((b) => b.addEventListener("click", () => {
    const f = b.dataset.f;
    btns.forEach((x) => x.setAttribute("aria-pressed", String(x === b)));
    cards.forEach((c) => { c.hidden = !(f === "all" || c.dataset.cat === f); });
    grid.classList.toggle("all", f !== "all");
  }));
  $("more").addEventListener("click", () => { grid.classList.add("all"); cards[6] && cards[6].focus(); });

  // Copier l'adresse
  const out = $("copied");
  $("copy").addEventListener("click", () => {
    const t = "1903rgb@gmail.com";
    const done = () => { out.textContent = "Adresse copiée"; setTimeout(() => (out.textContent = ""), 2400); };
    const sel = () => { const r = document.createRange(); r.selectNodeContents($("mail")); const s = getSelection(); s.removeAllRanges(); s.addRange(r); out.textContent = "Adresse sélectionnée, copiez-la"; };
    if (navigator.clipboard) navigator.clipboard.writeText(t).then(done).catch(sel); else sel();
  });

  // Formulaire de rendez-vous
  const ENDPOINT = "https://api.web3forms.com/submit";
  const ACCESS_KEY = "dae0c910-f6f4-419a-8588-f95cfcf4809e"; // clé Web3Forms (publique, liée à 1903rgb@gmail.com)
  const form = $("book"), fo = $("f-out"), send = $("f-send"), loaded = Date.now();
  const d = $("f-jour"); const t = new Date(); t.setDate(t.getDate() + 1); d.min = t.toISOString().slice(0, 10);
  const req = ["f-nom", "f-activite", "f-email"].map($);
  const say = (cls, msg) => { fo.className = "form-msg " + cls; fo.textContent = msg; };
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    req.forEach((i) => { i.removeAttribute("aria-invalid"); i.removeAttribute("aria-describedby"); });
    const bad = req.find((i) => !i.value.trim() || (i.type === "email" && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(i.value.trim())));
    if (bad) {
      bad.setAttribute("aria-invalid", "true"); bad.setAttribute("aria-describedby", "f-out");
      say("err", bad.type === "email" ? "Vérifiez votre adresse email, elle semble incomplète." : "Indiquez votre nom, votre activité et votre email pour qu’on puisse vous répondre.");
      bad.focus(); return;
    }
    const tel = $("f-tel");
    if (tel.value && !tel.checkValidity()) { tel.setAttribute("aria-invalid", "true"); say("err", "Le numéro de téléphone ne semble pas valide."); tel.focus(); return; }
    const data = Object.fromEntries(new FormData(form));
    if (data._honey || Date.now() - loaded < 3000) { form.reset(); say("ok", "Demande envoyée."); return; } // robots
    delete data._honey;
    if (!ACCESS_KEY) { say("err", "Le formulaire est en cours d’activation. Écrivez-nous à 1903rgb@gmail.com ou en DM sur Instagram (@_1903rgb_)."); return; }
    data.access_key = ACCESS_KEY;
    data.subject = "Demande de rendez-vous : " + String(data.activite).slice(0, 80);
    data.from_name = "Site 1903RGB";
    send.disabled = true; send.textContent = "Envoi…";
    const ctrl = new AbortController(); const timer = setTimeout(() => ctrl.abort(), 15000);
    try {
      const fd = new FormData(); Object.entries(data).forEach(([k, v]) => fd.append(k, v)); // requête « simple » : pas de pré-vérification CORS
      const r = await fetch(ENDPOINT, { method: "POST", headers: { Accept: "application/json" }, body: fd, signal: ctrl.signal, referrerPolicy: "strict-origin-when-cross-origin" });
      const j = await r.json().catch(() => ({}));
      if (!r.ok || j.success === false) throw new Error(String(r.status));
      form.reset(); say("ok", "Demande envoyée. On vous confirme le créneau par email sous 48 h.");
    } catch (_) {
      say("err", "L’envoi n’a pas fonctionné. Écrivez-nous à 1903rgb@gmail.com ou en DM sur Instagram (@_1903rgb_).");
    } finally { clearTimeout(timer); send.disabled = false; send.textContent = "Demander mon rendez-vous"; }
  });
})();
