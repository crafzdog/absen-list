// import 'bootstrap';
// import { gsap } from "gsap";

gsap.from("#login-box",{scale:0,duration:1,delay:0.5})

var logibox = document.querySelector(".login-reg")
var regbox = document.querySelector(".register-box")
var logbox = document.querySelector(".login-box")

logibox.addEventListener("click",function(){
    gsap.to("#login-box",{opacity:0,duration:1})
    gsap.to("#login-box",{x:5000,delay:1})
    gsap.to("#regis-box",{x:0})
    gsap.to("#regis-box",{opacity:1,duration:1,delay:1.2})
    regbox.classList.add("new")
    logbox.classList.remove("new")
});

var regbox = document.querySelector(".reg-login")

regbox.addEventListener("click",function(){
    gsap.to("#regis-box",{opacity:0,duration:1})
    gsap.to("#regis-box",{x:5000,delay:1})
    gsap.to("#login-box",{x:0})
    gsap.to("#login-box",{opacity:1,duration:1,delay:1.2})
    logbox.classList.add("new")
    regbox.classList.remove("new")
})

var navbar = document.querySelector(".nav-bod")

navbar.addEventListener("click",function(){
    console.log(navbar)
})


















// Select all pentagon elements
gsap.utils.toArray(".pentagon").forEach((pentagon, index) => {
    gsap.fromTo(
        pentagon,
        {
            scale: 0,     // Start small
            opacity: 1    // Start invisible
        },
        {
            scale: 8,     // Grow to full size
            opacity: 0,   // Fade out completely
            duration: 5,  // Animation duration for each pentagon
            repeat: -1,   // Repeat indefinitely
            ease: "power1.inOut",
            delay: index * 0.5 // Stagger the start by 0.5s for each pentagon
        }
    );
});

const test2 = document.querySelector(".test2");

// Initial and target positions
let posX = 100;
let posY = 100;
let targetX = posX;
let targetY = posY;

const step = 10; // Step size for each key press
const speed = 5; // Speed for smooth animation

// Keydown event to set the target position
document.addEventListener("keydown", (event) => {
    switch (event.key) {
        case "ArrowUp":
            targetY -= step;
            break;
        case "ArrowDown":
            targetY += step;
            break;
        case "ArrowLeft":
            targetX -= step;
            break;
        case "ArrowRight":
            targetX += step;
            break;
    }
});

// Animate function for smooth movement
function animate() {
    posX += (targetX - posX) * 0.1; // Adjust position slightly toward target
    posY += (targetY - posY) * 0.1;

    // Apply updated position
    test2.style.left = `${posX}px`;
    test2.style.top = `${posY}px`;

    requestAnimationFrame(animate); // Continuously update for smooth animation
}

animate(); // Start the animation loop
