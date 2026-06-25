const header = document.getElementById("site-header");
const menuToggle = document.getElementById("menu-toggle");
const mobilePanel = document.getElementById("mobile-panel");
const contactForm = document.getElementById("contact-form");
const toast = document.getElementById("toast");

function showToast(message) {
  toast.textContent = message;
  toast.classList.add("show");
  clearTimeout(showToast.timer);
  showToast.timer = setTimeout(() => toast.classList.remove("show"), 2400);
}

function closeMenu() {
  menuToggle.setAttribute("aria-expanded", "false");
  mobilePanel.classList.remove("open");
  mobilePanel.setAttribute("aria-hidden", "true");
}

window.addEventListener("scroll", () => {
  header.classList.toggle("scrolled", window.scrollY > 12);
}, { passive: true });

menuToggle.addEventListener("click", () => {
  const nextOpen = menuToggle.getAttribute("aria-expanded") !== "true";
  menuToggle.setAttribute("aria-expanded", String(nextOpen));
  mobilePanel.classList.toggle("open", nextOpen);
  mobilePanel.setAttribute("aria-hidden", String(!nextOpen));
});

document.querySelectorAll('a[href^="#"]').forEach((link) => {
  link.addEventListener("click", (event) => {
    const targetId = link.getAttribute("href").slice(1);
    const target = document.getElementById(targetId);
    if (!target) return;
    event.preventDefault();
    closeMenu();
    target.scrollIntoView({ behavior: "smooth", block: "start" });
    history.pushState(null, "", `#${targetId}`);
  });
});

contactForm.addEventListener("submit", (event) => {
  event.preventDefault();
  showToast("当前为前端原型：表单尚未接入后端，请补充真实提交链路。");
});
