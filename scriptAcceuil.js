/* Scroll effect */
window.addEventListener("scroll", function(){
    document.querySelector("nav")
    .classList.toggle("scrolled", window.scrollY > 50);
});

/* Mobile toggle */
const hamburger = document.querySelector(".hamburger");
const navLinks = document.querySelector(".nav-links");

hamburger.addEventListener("click", () => {
    navLinks.classList.toggle("active");
    hamburger.classList.toggle("active");
});
let slides=document.querySelectorAll(".slide");

let index=0;

function showSlide(i){

slides[index].classList.remove("active");

index=(i+slides.length)%slides.length;

slides[index].classList.add("active");

}

function changeSlide(n){

showSlide(index+n);

}

function currentSlide(n){

showSlide(n);

}

setInterval(()=>{

changeSlide(1);

},5000);
