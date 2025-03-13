const div = document.querySelector("div");

let deg = 100; // Initial gradient angle
let speed = 0.2; // Lower value = slower animation

function animateGradient() {
    deg = (deg + speed) % 360; // Slowly increment angle
    div.style.background = `linear-gradient(${deg}deg, rgba(255, 223, 45, 0.486) 0%, rgba(200, 161, 20, 0.525) 50%, rgba(255, 209, 69, 0.54) 100%)`;

    requestAnimationFrame(animateGradient); // Recursively call for next frame
}

// Start the animation
requestAnimationFrame(animateGradient);
