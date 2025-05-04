function analyzePlaylist() {
    const playlistLink = document.getElementById('playlistLink').value;
    const resultsDiv = document.getElementById('results');
    const diagnosisDiv = document.getElementById('diagnosis');
    const specialContainer = document.getElementById('specialSongs');
    const diagnosisImage = document.getElementById('diagnosisImage');

    // Reset display
    resultsDiv.innerText = '';
    diagnosisDiv.innerText = '';
    specialContainer.innerHTML = '';
    diagnosisImage.style.display = 'none';

    if (!playlistLink) {
        resultsDiv.innerText = "Please enter a playlist link.";
        return;
    }

    fetch('http://127.0.0.1:5000/analyze', {  // Change if using Java backend
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ playlist_link: playlistLink })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Server error: ${response.statusText}`);
        }
        return response.json();
    })
    .then(data => {
        // Show basic stats
        resultsDiv.innerText = `Detected ${data.radiohead_songs} Radiohead songs, ${data.weezer_songs} Weezer songs out of ${data.total_songs} total songs. You have ${data.loser_songs} loser songs.`;

        // Call the funny diagnosis logic
        funnyDiagnosis(
            data.total_songs,
            data.radiohead_songs,
            data.special_messages,
            data.weezer_songs,
            data.loser_songs
        );
    })
    .catch(err => {
        console.error(err);
        resultsDiv.innerText = "Error analyzing playlist. Please try again.";
    });
}

function funnyDiagnosis(total_songs, radiohead_songs, special_messages, weezer_songs, loser_songs) {
    const diagnosisDiv = document.getElementById('diagnosis');
    const specialContainer = document.getElementById('specialSongs');
    const diagnosisImage = document.getElementById('diagnosisImage');

    // Clear old data
    diagnosisDiv.innerText = '';
    specialContainer.innerHTML = '';
    diagnosisImage.style.display = 'none';

    // ========== FUNNY DIAGNOSIS ==========
    let diagnosisText = '';

    if (loser_songs >= 50) {
        diagnosisText = "\nDiagnosis: You absolutely repell women.";
        diagnosisImage.style.display = 'block';  // Show image if 50+
    } else if (loser_songs >= 40) {
        diagnosisText = "\nDiagnosis: You havent talked to a woman in years have you??";
        diagnosisImage.style.display = 'block';  // Show image if 40+
    } else if (loser_songs >= 30) {
        diagnosisText = "\nDiagnosis: You once made eye contact with a woman and still havent forgotten them.";
    } else if (loser_songs >= 20) {
        diagnosisText = "\nDiagnosis: You try to talk to women but end up scaring them away... aww :(.";
    } else if (loser_songs >= 10) {
        diagnosisText = "\nDiagnosis: You think about texting women, but never do. You are a coward.";
    } else if (loser_songs <= 5 && loser_songs >= 2) {
        diagnosisText = "\nDiagnosis: You talk to women but I dunno, you are pushing it pal.";
    } else if (loser_songs === 1) {
        diagnosisText = "\nDiagnosis: Only one song, ok , you talk to women good job!";
    } else {
        diagnosisText = "\nDiagnosis: 0 songs wow!! You go outside and talk to women!!! Good Job!";
    }

    diagnosisDiv.innerText = diagnosisText;

    // ========== SPECIAL SONGS ==========
    const specialHeader = document.createElement('h3');
    specialHeader.textContent = "Special Songs Detected";
    specialContainer.appendChild(specialHeader);

    if (special_messages && special_messages.length > 0) {
        special_messages.forEach(message => {
            const li = document.createElement('li');
            li.textContent = `- ${message}`;
            specialContainer.appendChild(li);
        });
    } else {
        const li = document.createElement('li');
        li.textContent = "No special songs detected. You are safe... for now.";
        specialContainer.appendChild(li);
    }
}

// Hook up the button click event
document.getElementById('analyzeBtn').addEventListener('click', analyzePlaylist);