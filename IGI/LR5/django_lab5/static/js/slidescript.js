let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("slide");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}

const navs = document.getElementById("navs");
const prev = document.querySelector(".prev");
const next = document.querySelector(".next");

const pags = document.getElementById("pags");
const pagination = document.querySelector(".pagination");

navs.addEventListener("change", () => {
    prev.style.display = next.style.display = navs.checked ? "none" : "block";
})

pags.addEventListener("change", () => {
    pagination.style.display = pags.checked ? "none" : "block";
})