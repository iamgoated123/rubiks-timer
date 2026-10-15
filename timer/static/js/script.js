const time = document.getElementById("stopwatch");

let running = false;
let startTime = 0;
let interval = null;

document.addEventListener("keydown", (e) => {
    if (e.code !== "Space") return;
    e.preventDefault();
    if (e.repeat) return;

    if (!running) {

        startTime=Date.now();
        running=true;
        interval=setInterval(() => {
            const seconds = (Date.now() - startTime) / 1000;
            time.textContent = seconds.toFixed(2);

        }, 10);
    } else {

        clearInterval(interval);
        running=false;
    }
});