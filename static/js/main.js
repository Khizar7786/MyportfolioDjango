// Mobile ki burger menu
const burger = document.getElementById('burger');
const navLinks = document.getElementById('navLinks');

burger.addEventListener('click', () => {
  navLinks.classList.toggle('open');
});

navLinks.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => navLinks.classList.remove('open'));
});

//skill bars ki animation
const fills = document.querySelectorAll('.skill-bar__fill');

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.width = entry.target.dataset.width + '%';
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.2 });

fills.forEach(fill => observer.observe(fill));
