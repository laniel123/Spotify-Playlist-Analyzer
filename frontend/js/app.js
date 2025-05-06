let fadeOutTimeout = null;  // Track fade-out timer globally

document.getElementById('analyzeBtn').addEventListener('click', function () {
    const playlistLink = document.getElementById('playlistLink').value.trim();
    const resultsDiv = document.getElementById('results');
    const diagnosisDiv = document.getElementById('diagnosis');
    const specialContainer = document.getElementById('specialSongs');
    const diagnosisImage = document.getElementById('diagnosisImage');
    const loader = document.getElementById('loader');

    // Cancel any ongoing fade-out to avoid hiding new results
    if (fadeOutTimeout) {
        clearTimeout(fadeOutTimeout);
        fadeOutTimeout = null;
    }

    // Fade out if showing
    if (
        resultsDiv.style.display === 'block' ||
        diagnosisDiv.style.display === 'block' ||
        specialContainer.style.display === 'block'
    ) {
        resultsDiv.style.opacity = 0;
        diagnosisDiv.style.opacity = 0;
        specialContainer.style.opacity = 0;

        fadeOutTimeout = setTimeout(() => {
            resultsDiv.style.display = 'none';
            diagnosisDiv.style.display = 'none';
            specialContainer.style.display = 'none';
            fadeOutTimeout = null;
        }, 500); // Match CSS fade-out time
    }

    // Clear old content
    resultsDiv.innerText = '';
    diagnosisDiv.innerText = '';
    specialContainer.innerHTML = '';
    diagnosisImage.style.display = 'none';

    if (!playlistLink) {
        alert("Please enter a playlist link.");
        return;
    }

    // Show spinner
    loader.style.display = 'block';

    fetch('http://127.0.0.1:5000/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ playlist_link: playlistLink })
    })
        .then(response => response.json())
        .then(data => {
            loader.style.display = 'none'; // Hide spinner

            if (data.error) {
                resultsDiv.innerText = "Error analyzing playlist. Please try again.";
                fadeIn(resultsDiv);
                return;
            }

            // 📊 Results
            resultsDiv.innerText = `I Detected ${data.radiohead_songs} Radiohead songs and ${data.weezer_songs} Weezer songs out of ${data.total_songs} total songs. You have ${data.loser_songs} loser songs.`;

            // 😂 Diagnosis
            let diagnosisText = "";

            if (data.loser_songs >= 50) {
                diagnosisText = "\nDiagnosis: You absolutely repell women.";
            } else if (data.loser_songs >= 40) {
                diagnosisText = "\nDiagnosis: You havent talked to a woman in years have you??";
            } else if (data.loser_songs >= 30) {
                diagnosisText = "\nDiagnosis: You once made eye contact with a woman and still havent forgotten them.";
            } else if (data.loser_songs >= 20) {
                diagnosisText = "\nDiagnosis: You try to talk to women but end up scaring them away... aww :(.";
            } else if (data.loser_songs >= 10) {
                diagnosisText = "\nDiagnosis: You think about texting women, but never do. You are a coward.";
            } else if (data.loser_songs <= 5 && data.loser_songs >= 2) {
                diagnosisText = "\nDiagnosis: You talk to women but I dunno, you are pushing it pal.";
            } else if (data.loser_songs === 1) {
                diagnosisText = "\nDiagnosis: Only one song, ok , you talk to women good job!";
            } else {
                diagnosisText = "\nDiagnosis: 0 songs wow!! You go outside and talk to women!!! Good Job!";
            }

            diagnosisDiv.innerText = diagnosisText;

            // 🎶 Special songs
            specialContainer.innerHTML = "<h3>Special Songs Detected</h3>";
            if (data.special_messages && data.special_messages.length > 0) {
                data.special_messages.forEach(message => {
                    const msgElem = document.createElement('p');
                    msgElem.innerText = `- ${message}`;
                    specialContainer.appendChild(msgElem);
                });
            } else {
                const noMsgElem = document.createElement('p');
                noMsgElem.innerText = "No special songs detected. You are safe... for now.";
                specialContainer.appendChild(noMsgElem);
            }

            // ✅ Fade in results
            fadeIn(resultsDiv);
            fadeIn(diagnosisDiv);
            fadeIn(specialContainer);

            // 🎉 Confetti (adjust duration here)
            const duration = 2500; // 2.5 seconds
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

            // 🔊 Play sound after confetti
            setTimeout(() => {
                const sound = document.getElementById('celebrationSound');
                sound.currentTime = -0.5; // Reset in case it played before
                sound.play();
            }, duration);

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
        })
        .catch(error => {
            console.error('Error:', error);
            loader.style.display = 'none';
            resultsDiv.innerText = "Error analyzing playlist. Please try again.";
            fadeIn(resultsDiv);
        });
});

// 🔄 Fade-in helper function
function fadeIn(element) {
    element.style.display = 'block';
    setTimeout(() => {
        element.style.opacity = 1;
    }, 10);
}