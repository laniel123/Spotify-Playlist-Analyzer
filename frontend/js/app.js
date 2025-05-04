let fadeOutTimeout = null;

const analyzeBtn = document.getElementById('analyzeBtn');
const playlistInput = document.getElementById('playlistLink');
const resultsDiv = document.getElementById('results');
const diagnosisDiv = document.getElementById('diagnosis');
const specialContainer = document.getElementById('specialSongs');
const loader = document.getElementById('loader');
const volumeSlider = document.getElementById('volumeSlider');

const yaySound = document.getElementById('celebrationSound');

// Set initial volume
yaySound.volume = volumeSlider.value;

// Keep volume in sync with slider
volumeSlider.addEventListener('input', function () {
    yaySound.volume = this.value;
});

analyzeBtn.addEventListener('click', function () {
    const playlistLink = playlistInput.value.trim();

    if (fadeOutTimeout) {
        clearTimeout(fadeOutTimeout);
        fadeOutTimeout = null;
    }

    if (resultsDiv.style.display === 'block' || diagnosisDiv.style.display === 'block' || specialContainer.style.display === 'block') {
        resultsDiv.style.opacity = 0;
        diagnosisDiv.style.opacity = 0;
        specialContainer.style.opacity = 0;

        fadeOutTimeout = setTimeout(() => {
            resultsDiv.style.display = 'none';
            diagnosisDiv.style.display = 'none';
            specialContainer.style.display = 'none';
            fadeOutTimeout = null;
        }, 500);
    }

    resultsDiv.innerText = '';
    diagnosisDiv.innerText = '';
    specialContainer.innerHTML = '';

    if (!playlistLink) {
        alert("Please enter a playlist link.");
        return;
    }

    loader.style.display = 'block';

    fetch('http://127.0.0.1:5000/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ playlist_link: playlistLink })
    })
        .then(response => response.json())
        .then(data => {
            loader.style.display = 'none';

            if (data.error) {
                resultsDiv.innerText = "Error analyzing playlist. Please try again.";
                resultsDiv.style.display = 'block';
                setTimeout(() => { resultsDiv.style.opacity = 1; }, 10);
                return;
            }

            resultsDiv.innerText = `I Detected ${data.radiohead_songs} Radiohead songs and ${data.weezer_songs} Weezer songs out of ${data.total_songs} total songs. You have ${data.loser_songs} loser songs.`;

            let diagnosisText = "";

            if (data.loser_songs >= 50) {
                diagnosisText = "\nDiagnosis: You absolutely repell women.";
            } else if (data.loser_songs >= 40) {
                diagnosisText = "\nDiagnosis: You haven't talked to a woman in years have you??";
            } else if (data.loser_songs >= 30) {
                diagnosisText = "\nDiagnosis: You once made eye contact with a woman and still haven't forgotten them.";
            } else if (data.loser_songs >= 20) {
                diagnosisText = "\nDiagnosis: You try to talk to women but end up scaring them away.";
            } else if (data.loser_songs >= 10) {
                diagnosisText = "\nDiagnosis: You think about texting women, but never do.";
            } else if (data.loser_songs <= 5 && data.loser_songs >= 2) {
                diagnosisText = "\nDiagnosis: You talk to women but you are pushing it.";
            } else if (data.loser_songs === 1) {
                diagnosisText = "\nDiagnosis: Only one song, you talk to women good job.";
            } else {
                diagnosisText = "\nDiagnosis: 0 songs, you go outside and talk to women. Good job.";
            }

            diagnosisDiv.innerText = diagnosisText;

            specialContainer.innerHTML = "<h3>Special Songs Detected</h3>";
            if (data.special_messages && data.special_messages.length > 0) {
                data.special_messages.forEach(message => {
                    const msgElem = document.createElement('p');
                    msgElem.innerText = `- ${message}`;
                    specialContainer.appendChild(msgElem);
                });
            } else {
                const noMsgElem = document.createElement('p');
                noMsgElem.innerText = "No special songs detected.";
                specialContainer.appendChild(noMsgElem);
            }

            resultsDiv.style.display = 'block';
            diagnosisDiv.style.display = 'block';
            specialContainer.style.display = 'block';

            setTimeout(() => {
                resultsDiv.style.opacity = 1;
                diagnosisDiv.style.opacity = 1;
                specialContainer.style.opacity = 1;
            }, 10);

            const duration = 2500;
            const animationEnd = Date.now() + duration;

            (function frame() {
                confetti({
                    particleCount: 5,
                    angle: 60,
                    spread: 55,
                    origin: { x: 0 }
                });
                confetti({
                    particleCount: 5,
                    angle: 120,
                    spread: 55,
                    origin: { x: 1 }
                });
                if (Date.now() < animationEnd) {
                    requestAnimationFrame(frame);
                }
            })();

            if (parseFloat(yaySound.volume) > 0) {
                yaySound.currentTime = 0;
                yaySound.play();
            }
        })
        .catch(error => {
            console.error('Error:', error);
            loader.style.display = 'none';
            resultsDiv.innerText = "Error analyzing playlist. Please try again.";
            resultsDiv.style.display = 'block';
            setTimeout(() => { resultsDiv.style.opacity = 1; }, 10);
        });
});